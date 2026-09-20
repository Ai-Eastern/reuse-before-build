# Validation and evidence

Local evaluation recorded on **2026-09-20**, for the skill revision identified
by its SHA-256 below. These observations do not imply a release tag,
a remote CI result, or universal host compatibility.

The evaluated `SKILL.md` SHA-256 is:

```text
1b288be48c3b74a77d1fecc26abba3037b599613e13a2761128776e60b563c68
```

Environment: Windows, Node.js 24.18.0, Python 3.12.14, and Git for Windows
2.55.0. The Python tools below are development checks, not skill runtime
dependencies.

## What was checked

| Layer | Observed result | What it does not prove |
| --- | --- | --- |
| Skill format | Agent Skills `skills-ref` at commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379` accepted the skill directory; the local skill-creator quick validator also passed | Correct agent decisions |
| Standalone installation | `skills@1.7.0` copied the revised `SKILL.md` and `LICENSE` into a separate project's Codex skill directory; both SHA-256 hashes matched the source | Native discovery or implicit activation in a new Codex session |
| Manual installation | The documented PowerShell copy produced matching skill and license files in an isolated project | POSIX commands executed on a Unix host |
| Fixture | The unmodified retry fixture passed both baseline tests | Coverage of the additional task boundaries |
| Scenario preparation | Six isolated scenarios prepared successfully with genuine passing baseline records; rejection of existing/relative destinations and inherited Git-environment isolation were checked | Six agent evaluations |
| Behavior: test reuse | A fresh-context agent extended the existing test file, preserved production code, and verified four passing tests | Statistical reliability or another model's behavior |
| Behavior: recovery | A fresh-context agent detected changed uncommitted source despite unchanged HEAD, ran the affected tests, and correctly reported one failure without editing | Automatic interception of a real host compaction event |

The two behavior runs used separate in-session Codex subagents with no parent
conversation history. Each was explicitly given its prepared `SKILL.md` and
`TASK.md`, instructed to stay in that fixture, and not given the reviewer
guide. This is instruction-scoped evaluation, not OS security isolation.
The exact model identifier was not captured. There is no without-skill
control run, cost comparison, or general success-rate claim.

## Inspect the behavior evidence

**Scenario 03 — extend existing tests.** The agent read the existing helper
and assertions, added final-error identity/attempt-count and zero-attempt
coverage to the existing file, and left production-source hashes unchanged.
The reviewer inspected the diff and replayed the test command: 4 tests
passed, exit 0.

- [Snapshot and replay receipt](../evals/results/2026-09-20/test-borrow.json)
- [Baseline TAP](../evals/results/2026-09-20/test-borrow-baseline.tap)
- [Actual test diff](../evals/results/2026-09-20/test-borrow.patch)
- [Reviewer replay TAP](../evals/results/2026-09-20/test-borrow.tap)

**Scenario 04 — stale passing result.** Preparation ran a genuine 2/2 green
baseline, then changed the retry default from three attempts to one without
committing. The agent inspected the saved evidence and current source,
identified the mismatch, and reported the existing third-attempt test's
failure. The reviewer replay found 1 pass and 1 failure, exit 1; the only
source diff remained the intentionally prepared change.

- [Snapshot and replay receipt](../evals/results/2026-09-20/dirty-resume.json)
- [Earlier passing TAP](../evals/results/2026-09-20/dirty-resume-baseline.tap)
- [Prepared dirty diff, unchanged after evaluation](../evals/results/2026-09-20/dirty-resume.patch)
- [Reviewer replay TAP](../evals/results/2026-09-20/dirty-resume.tap)

The failure in scenario 04 is the expected fixture state; correctly reporting
it is the evaluated behavior. Exported TAP normalizes local absolute paths
to `<fixture>`. Replay logs are fresh reviewer runs, not a transcript of the
evaluating agent's complete tool history. See [evaluation instructions](../evals/README.md),
the separate [reviewer guide](../evals/reviewer.md), and
[asset checks](../evals/ASSET_CHECKS.md) to reproduce or extend these checks.

## Reproduce the local checks

Use Node.js 22 or newer for the development fixture. The optional installer
has its own stricter requirement of Node.js >=22.20.0. From a complete clean
checkout:

```sh
node scripts/check-links.mjs
node --check evals/prepare.mjs
node --test evals/fixtures/retry-service/test/retry.test.mjs
```

The link check covers local inline Markdown file links, excluding fenced
examples; it does not check remote URLs, reference-style links, or heading
anchors. It is a documentation check, not a behavior test.

For the pinned reference format check, use a disposable Python environment:

```sh
python -m pip install 'git+https://github.com/agentskills/agentskills@69ef37e9424c0a7ea9dd2293b559e43ec8176379#subdirectory=skills-ref'
skills-ref validate /absolute/path/to/reuse-before-build
```

The directory basename must match the skill name. Pass its absolute path;
this reference-validator revision does not normalize `.` before checking
that name. Local validation used a workspace-only `pip --target` directory
and a process-local Python module path, without changing global packages.

For behavior evaluation, prepare fresh directories and give separate agents
the scenario input as described in [evals](../evals/README.md). Keep the
expected outcomes away from the evaluating agent. Do not install directly
from a development checkout containing scratch runs: the pinned installer
copies local files without honoring `.gitignore`. Use a clean source
checkout or the distributed archive.

## CI and remaining coverage

The [CI workflow](../.github/workflows/validate.yml) checks skill format,
local links, the fixture, and recovery-scenario preparation. Action revisions
and the reference validator are pinned. Inspect [GitHub Actions runs](https://github.com/Ai-Eastern/reuse-before-build/actions/workflows/validate.yml)
for the result associated with a particular commit. The local evaluation
above predates the first remote run; local execution alone does not establish
remote CI success.

Behavior scenarios 01, 02, 05, and 06 have prepared inputs but were not run
through fresh evaluating agents in this validation batch. The revised skill
has not been behavior-tested in Claude Code, Copilot CLI, Cursor, Gemini
CLI, OpenCode, or Windsurf. Automatic activation, real host compaction,
cross-machine handoffs, and dynamic external-service checks remain outside
these observations. See [compatibility](compatibility.md) for documented
installation routes and evidence levels.
