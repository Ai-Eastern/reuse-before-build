"""Prepare previous/current Skill comparisons and bounded regression cases."""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import runpy
import shutil
import sys

repo = Path(__file__).resolve().parent.parent
timing = runpy.run_path(str(repo / 'evals/prepare-search-timing.py'))
snapshot = timing['snapshot']

ANALYTICS = ('为一个 Python 3.12 项目设计本地日志分析方案：每天处理约 20 GB CSV，'
             '按日期和客户分组汇总，再输出 Parquet。进程内存上限 2 GB，允许使用临时磁盘，'
             '不部署数据库服务。请给出有依据的组件选型、复用边界和待验证项。本次只做设计，不安装依赖。')
LIMITER = ('项目使用 Node.js 22，需要限制异步任务同时执行的数量，并在任务失败后继续处理后续任务。'
           '请根据这里提供的候选材料提出组件选型、适配边界与验证计划。本次只做设计；'
           '环境离线，不访问网络，不安装依赖。')
SOURCE = '''export function limit(max) {
  if (!Number.isInteger(max) || max < 1) throw new RangeError('positive max required');
  let active = 0;
  const queue = [];
  const start = () => {
    while (active < max && queue.length) {
      const {fn, resolve, reject} = queue.shift();
      active++;
      Promise.resolve().then(fn).then(resolve, reject).finally(() => { active--; start(); });
    }
  };
  return fn => new Promise((resolve, reject) => { queue.push({fn, resolve, reject}); start(); });
}
'''
TEST = '''import assert from 'node:assert/strict';
import test from 'node:test';
import { limit } from './index.mjs';
test('a failed task releases the slot', async () => {
  const run = limit(1);
  let release;
  const barrier = new Promise(resolve => { release = resolve; });
  let secondStarted = false;
  const error = new Error('first');
  const first = run(async () => { await barrier; throw error; });
  const second = run(() => { secondStarted = true; return 'next'; });
  await Promise.resolve();
  assert.equal(secondStarted, false);
  release();
  await assert.rejects(first, e => e === error);
  assert.equal(await second, 'next');
});
'''


def prepare(destination, previous_skill):
    previous_bytes = previous_skill.read_bytes()
    # Reuse the existing fixture, checkpoint generation, guards, and hashes.
    tasks = dict(timing['TASKS'])
    timing['TASKS'].clear()
    timing['TASKS'].update({
        'changed-requirement': tasks['changed-requirement'],
        'covered-test': tasks['covered-test'],
    })
    with contextlib.redirect_stdout(io.StringIO()):
        timing['prepare'](destination)
    (destination / 'changed-requirement/control/SKILL.md').write_bytes(previous_bytes)
    for arm in ['control', 'skill']:
        root = destination / 'analytics' / arm
        root.mkdir(parents=True)
        (root / 'TASK.md').write_text(ANALYTICS + '\n', encoding='utf-8', newline='\n')
        (root / 'SKILL.md').write_bytes(previous_bytes if arm == 'control' else (repo / 'SKILL.md').read_bytes())
    for case in ['snapshot-a', 'snapshot-b']:
        root = destination / case / 'skill'
        candidate = root / 'candidate'
        candidate.mkdir(parents=True)
        shutil.copy2(repo / 'SKILL.md', root / 'SKILL.md')
        (root / 'TASK.md').write_text(LIMITER + '\n', encoding='utf-8', newline='\n')
        (root / 'README.md').write_text('Synthetic evaluation workspace; no production implementation exists.\n'
            'candidate/ contains a supplied external-project snapshot for offline assessment.\n'
            'The provider is fictional and its provenance fields are simulated fixture facts.\n'
            'The parent evaluation repository license is not evidence of rights to that simulated third-party artifact.\n', encoding='utf-8', newline='\n')
        (candidate / 'package.json').write_text(json.dumps({'name': '@fixture/async-limit', 'version': '1.0.0',
            'type': 'module', 'engines': {'node': '>=22'}, 'exports': './index.mjs'}, indent=2) + '\n', encoding='utf-8', newline='\n')
        (candidate / 'index.mjs').write_text(SOURCE, encoding='utf-8', newline='\n')
        (candidate / 'index.test.mjs').write_text(TEST, encoding='utf-8', newline='\n')
        (candidate / 'README.md').write_text('# Async limiter fixture\n\n'
            'Provider: Fictional Fixture Authors; snapshot version: 1.0.0.\n'
            'API: limit(max) returns run(fn), accepting an asynchronous task function.\n'
            'This snapshot claims bounded concurrency and progress after rejection.\n'
            'Delivery contains no network fetch or upstream verification record.\n', encoding='utf-8', newline='\n')
        if case == 'snapshot-a':
            shutil.copy2(repo / 'LICENSE', candidate / 'LICENSE')
    runs = []
    for case, arms in [('changed-requirement', ['control', 'skill']), ('analytics', ['control', 'skill']),
                       ('snapshot-a', ['skill']), ('snapshot-b', ['skill']), ('covered-test', ['skill'])]:
        for arm in arms:
            root = destination / case / arm
            runs.append({'case': case, 'arm': arm, 'initial_hashes': snapshot(root)})
        if len(arms) == 2:
            a, b = runs[-2:]
            assert {k:v for k,v in a['initial_hashes'].items() if k != 'SKILL.md'} == {k:v for k,v in b['initial_hashes'].items() if k != 'SKILL.md'}
    manifest = {'previous_skill_sha256': hashlib.sha256(previous_bytes).hexdigest(),
                'current_skill_sha256': timing['digest'](repo / 'SKILL.md'), 'planned_runs': runs}
    (destination / 'gate-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'directory': str(destination), 'prepared_model_runs': len(runs), 'models_launched': 0}))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python evals/prepare-evidence-gate.py <new-absolute-directory> <previous-SKILL.md>')
    prepare(Path(sys.argv[1]), Path(sys.argv[2]))
