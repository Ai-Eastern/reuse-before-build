"""Prepare an offline core/wrapper revision comparison; launches no models."""
from pathlib import Path
import hashlib
import json
import runpy
import shutil
import sys

repo = Path(__file__).resolve().parent.parent
gate = runpy.run_path(str(repo / 'evals/prepare-evidence-gate.py'))
TASK = ('评估供应商 wrapper 2.0.0 是否能原样用于 Node.js 22 的异步任务并发限制，'
        '并保证单个任务失败后继续处理后续任务。根据提供的材料给出采用决定、依据与后续步骤。'
        '本次只做设计，不修改供应商代码、不安装依赖；环境离线，不访问网络。')


def prepare(destination, previous_skill):
    previous = previous_skill.read_bytes()
    if not destination.is_absolute() or destination.exists():
        raise ValueError('Pass a new absolute directory; existing destinations are never overwritten')
    destination.parent.resolve(strict=True)
    destination.mkdir()
    runs = []
    for arm in ['control', 'skill']:
        root = destination / 'revision-map' / arm
        core, wrapper = root / 'core', root / 'wrapper'
        core.mkdir(parents=True)
        wrapper.mkdir()

        def write(path, value):
            path.write_text(value + '\n', encoding='utf-8', newline='\n')

        def data(path, value):
            write(path, json.dumps(value, indent=2))

        write(root / 'TASK.md', TASK)
        (root / 'SKILL.md').write_bytes(previous if arm == 'control' else (repo / 'SKILL.md').read_bytes())
        write(root / 'README.md', '# Supplied vendor materials\n\n'
              'This is a synthetic offline fixture with fictional providers and simulated revisions.\n'
              'core/ and wrapper/ are separately supplied source snapshots. No production implementation exists.\n'
              'Only supplied files are available; no upstream verification or installation was performed.')
        data(core / 'package.json', {'name': '@fixture/core', 'version': '1.0.0', 'type': 'module',
                                    'engines': {'node': '>=22'}, 'exports': './index.mjs'})
        data(core / 'SNAPSHOT.json', {'repository': 'fictional/core', 'commit': 'a' * 40})
        write(core / 'index.mjs', gate['SOURCE'].rstrip())
        write(core / 'index.test.mjs', gate['TEST'].rstrip())
        data(wrapper / 'package.json', {'name': '@fixture/wrapper', 'version': '2.0.0', 'type': 'module',
                                       'engines': {'node': '>=22'}, 'exports': './index.mjs'})
        data(wrapper / 'BUILD.json', {'repository': 'fictional/wrapper', 'commit': 'c' * 40,
                                     'vendored_core': {'repository': 'fictional/core', 'commit': 'b' * 40,
                                                       'path': 'vendor/core'}})
        write(wrapper / 'index.mjs', "import { limit } from './vendor/core/index.mjs';\n"
              "export const createRunner = max => limit(max);")
        write(wrapper / 'index.test.mjs', gate['TEST'].replace('limit', 'createRunner').rstrip())
        write(wrapper / 'README.md', '# Wrapper 2.0.0\n\n'
              'API: createRunner(max) returns run(task). The release uses the core snapshot named in BUILD.json.\n'
              'The delivery contains wrapper source and tests, not its vendored source tree.')
        for folder in [core, wrapper]:
            shutil.copy2(repo / 'LICENSE', folder / 'LICENSE')
        runs.append({'case': 'revision-map', 'arm': arm, 'initial_hashes': gate['snapshot'](root)})
    assert {k: v for k, v in runs[0]['initial_hashes'].items() if k != 'SKILL.md'} == {
        k: v for k, v in runs[1]['initial_hashes'].items() if k != 'SKILL.md'}
    manifest = {'previous_skill_sha256': hashlib.sha256(previous).hexdigest(),
                'current_skill_sha256': gate['timing']['digest'](repo / 'SKILL.md'), 'planned_runs': runs}
    (destination / 'gate-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'directory': str(destination), 'prepared_model_runs': len(runs), 'models_launched': 0}))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python evals/prepare-revision-case.py <new-absolute-directory> <previous-SKILL.md>')
    prepare(Path(sys.argv[1]), Path(sys.argv[2]))
