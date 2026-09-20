"""Prepare paired, fresh workspaces; never launches a model or changes global state."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

TASKS = {
    'small-edit': '修正 README 中 staus 的拼写问题，仅处理这个文档问题。完成后说明改动和验证。',
    'covered-test': '确认并补足 retry 默认允许三次总尝试的测试保障：前两次暂时失败、第三次成功时，应返回成功值并停止调用。给出可重复的验证结果，保持生产代码不变。',
    'covered-variant': '给 retry 首次调用就成功时立即返回、不再调用 operation 的行为补足测试保障。给出可重复的验证结果，保持生产代码不变。',
    'test-gap': '补齐 retry 的两个边界检查：所有尝试失败时应保留最后那个错误对象并停在配置次数；attempts 为 0 时应拒绝且不调用 operation。保持公共契约和生产代码不变，完成验证。',
    'local-failure': '项目现有测试失败了。定位并修复回归，保持文档和测试定义的既有行为，完成验证。',
    'unchanged-resume': '依据 context/checkpoint.md 接着完成这项任务，给出当前是否满足默认三次尝试要求的结论。本次只读，不修改项目文件。',
    'changed-requirement': '继续这个项目，但需求已经改变：任务现在需要持久化、延迟执行、进程重启后恢复和多个 worker 消费。项目使用 Node.js 22，已有 PostgreSQL，不想再部署 Redis。请提出有依据的架构与组件选型，说明与旧决定的关系、可复用部分和待验证项。现在只做设计。',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(root):
    return {p.relative_to(root).as_posix(): digest(p)
            for p in sorted(root.rglob('*')) if p.is_file()}


def prepare(destination):
    repo = Path(__file__).resolve().parent.parent
    if not destination.is_absolute() or destination.exists():
        raise ValueError('Pass a new absolute directory; existing destinations are never overwritten')
    destination.parent.resolve(strict=True)
    destination.mkdir()
    skill_hash = digest(repo / 'SKILL.md')
    manifest = {'created_at_utc': datetime.now(timezone.utc).isoformat(),
                'skill_sha256': skill_hash, 'cases': []}
    for case, task in TASKS.items():
        roots = []
        for arm in ['control', 'skill']:
            root = destination / case / arm
            shutil.copytree(repo / 'evals/fixtures/retry-service', root)
            shutil.copy2(repo / 'LICENSE', root / 'LICENSE')
            if case == 'local-failure':
                source = root / 'src/retry.mjs'
                source.write_text(source.read_text(encoding='utf-8').replace('attempts = 3', 'attempts = 1'), encoding='utf-8')
            if case in ['unchanged-resume', 'changed-requirement']:
                context = root / 'context'
                context.mkdir()
                files = snapshot(root)
                result = subprocess.run(['node', '--test', '--test-reporter=tap'], cwd=root, text=True, capture_output=True, timeout=30)
                if result.returncode:
                    raise RuntimeError(result.stderr or result.stdout)
                (context / 'baseline.tap').write_text(result.stdout, encoding='utf-8')
                record = {'command': 'node --test --test-reporter=tap', 'cwd': '.',
                          'observed_at_utc': datetime.now(timezone.utc).isoformat(),
                          'exit_code': result.returncode, 'node': subprocess.check_output(['node', '--version'], text=True).strip(),
                          'input_hashes': files, 'output': 'context/baseline.tap'}
                (context / 'verification.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
                (context / 'checkpoint.md').write_text(
                    '# Task checkpoint\n\n'
                    'Goal: confirm the in-process retry helper allows two temporary failures and success on attempt three.\n'
                    'Workspace: this directory; no Git repository is required. Input snapshots and the actual passing test output are in verification.json and baseline.tap here.\n'
                    'Decision: Take the local retry helper and its existing tests for bounded, in-process retry. This scope did not require a durable job queue or external package.\n'
                    'Completed: inspected the helper and existing assertions; ran the two baseline tests successfully.\n'
                    'Remaining: provide the user-facing conclusion; no implementation remains for the original requirement.\n', encoding='utf-8')
            if arm == 'skill':
                shutil.copy2(repo / 'SKILL.md', root / 'SKILL.md')
            (root / 'TASK.md').write_text(task + '\n', encoding='utf-8')
            roots.append(root)
        # Keep shared task inputs byte-identical; timestamps and TAP durations are
        # genuine observations from one baseline, copied to both comparison arms.
        if case in ['unchanged-resume', 'changed-requirement']:
            shutil.copytree(roots[0] / 'context', roots[1] / 'context', dirs_exist_ok=True)
        control = snapshot(roots[0])
        treatment = snapshot(roots[1])
        assert {k: v for k, v in treatment.items() if k != 'SKILL.md'} == control
        manifest['cases'].append({'id': case, 'task': task, 'arms': {
            arm: {'directory': str(root), 'initial_hashes': snapshot(root)}
            for arm, root in zip(['control', 'skill'], roots)
        }})
    (destination / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'directory': str(destination), 'cases': len(TASKS), 'prepared_arms': len(TASKS) * 2, 'skill_sha256': skill_hash}))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python evals/prepare-search-timing.py <new-absolute-directory>')
    prepare(Path(sys.argv[1]))
