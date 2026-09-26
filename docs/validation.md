# Validation and evidence

Evidence is tied to the evaluated Skill hash. This page retains the earlier
2026-09-20 test/recovery runs, an earlier 2026-09-21 architecture run, and the
new GPT-5.6 Luna / medium comparison. Follow-ups did not rerun every scenario
on the final revision. These observations imply neither a release tag nor
universal host compatibility.

## Candidate inspection — 2026-09-26

The [new evidence-gate report](../evals/results/2026-09-26/evidence-gate/REPORT.md)
records **11 additional GPT-5.6 Luna / medium runs**, verified from actual host
runtime settings. Two fresh previous/current pairs exercised queue and CSV
analytics designs; three local regressions checked supplied candidates and
already-covered tests. Four targeted follow-ups used the final revision:

```text
62651b60cc1ed43af2d8d8d6aa7a2a58dbbec46a834b56bd1139dc9b3e353f7c
```

The final revision replaced generic verification labels with artifact-specific
receipts. Both live follow-ups read versioned implementation and license
contents, improving on search-only selection. The queue design still lacked
versioned test/call-site corroboration; the analytics design lacked usable
test contents and did not establish the relationship between core and Python
binding revisions. The offline missing-license case blocked dependency adoption
but mixed conceptual Borrow and local Build labels. These remain partial
results, not a reliably enforced adoption gate.

The complete offline fixture remained usable; the V4 local-test regression
kept files unchanged and passed two tests. That local regression was not rerun
on the final revision. No runtime integration, performance, automatic activation,
or cross-host claims follow from these observations. The report retains every
run, failed fetch, frozen Skill revision, and the input/output evidence.

## Architecture discovery — 2026-09-21 (historical architecture revision)

A fresh-context Codex desktop subagent explicitly loaded the architecture
revision, identified by this `SKILL.md` SHA-256:

```text
75308a77e0357d058fa886f0125719ddb51f41ef04547850fd4195e261c224f7
```

The [task](../evals/results/2026-09-21/architecture-task.md) requested only a
design for a Node.js 22/PostgreSQL background-job service with no added Redis.
The empty workspace contained the Skill; no candidate names, parent history,
or reviewer conclusions were supplied. The agent screened three external
candidates, deep-read two, and produced component boundaries, tradeoffs,
source references, and unexecuted integration checks. It distinguished
database transaction guarantees from external-side-effect idempotency.

- [Agent design](../evals/results/2026-09-21/architecture-result.md)
- [Source and inspection receipt](../evals/results/2026-09-21/architecture-sources.json)
- [Reviewer checks and export hashes](../evals/results/2026-09-21/architecture-review.json)

The reviewer checked the result against the task, confirmed the unchanged
Skill hash and two permitted workspace outputs, and spot-checked pinned
upstream package, transaction implementation, and test sources through GitHub.
The source receipt is agent-produced, not a full raw tool transcript; not
every upstream claim was independently revalidated. No packages were installed,
database connections opened, or runtime tests run. The model identifier was
not captured. This is one explicitly invoked, source-backed design observation,
not an automatic-trigger test, runtime compatibility proof, comparative
benchmark, or guarantee of a particular architectural choice.

Both format validators, local documentation links, the unchanged fixture's
two baseline tests, and six English/Chinese README views were also checked.
Those are structural checks, not additional agent behavior evaluations.

## Search timing and test reuse — 2026-09-21

Seventeen fresh GPT-5.6 Luna / medium runs were verified against actual host
runtime settings: six initial control/treatment pairs, three V2 follow-ups,
and two V3 treatment-only follow-ups. The shared agent catalog means this
compares the full Skill body with no full body, not a model without guidance.

| Revision | Skill SHA-256 | Observations |
| --- | --- | --- |
| V1 | `591bb93753616250d04cd6635069015bb2f7ffa8a92e24154fda5482b4e1c355` | Both arms stayed local in five local scenarios. Both made a redundant coverage edit. Treatment searched after changed requirements but selected Borrow without source/license inspection. Its final-error test also failed to distinguish different errors. |
| V2 | `9b953ba824a9ed5004db7982945c94673c3aea272dff42c5ea4fb4a0b7172fc4` | Original covered task and first-success transfer treatment runs reused tests without edits. Transfer control rewrote already-sufficient assertions. |
| V3 (2026-09-21 revision) | `a77d13420dddd2608d623941983c0b0e7dd5ab8dc9f7e44fa300d14425400534` | Test-gap follow-up used distinct errors and caught a reviewer-injected first-error defect. Architecture follow-up still skipped required source/license inspection despite the new explicit gate. |

The V1 treatment's tests passed 4/4 even against a deliberately wrong
first-error implementation. V3's tests passed 4/4 on the correct source and
failed the relevant case on that mutant. Reviewer checks are separate from
model trials. The other scenarios were not rerun on V3. Neither architecture
trial validates package adoption or runtime integration. Do not infer a
success rate, universal causal effect, or automatic activation.

The [complete report](../evals/results/2026-09-21/luna-search-timing/REPORT.md)
contains frozen instructions, input hashes, dispatches, observable actions,
actual runtime settings, mutation receipts, and disclosed harness deviations.
It preserves all runs, including failures; private reasoning is excluded.

## Earlier test and recovery evaluations — 2026-09-20

The earlier evaluated `SKILL.md` SHA-256 is:

```text
1b288be48c3b74a77d1fecc26abba3037b599613e13a2761128776e60b563c68
```

Environment: Windows, Node.js 24.18.0, Python 3.12.14, and Git for Windows
2.55.0. The Python tools below are development checks, not skill runtime
dependencies.

## Earlier revision: what was checked

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
local links, the fixture, recovery-scenario preparation, and paired timing inputs. Action revisions
and the reference validator are pinned. Inspect [GitHub Actions runs](https://github.com/Ai-Eastern/reuse-before-build/actions/workflows/validate.yml)
for the result associated with a particular commit. Local checks and model trials alone do not establish remote CI success.

In the original six-scenario harness, scenarios 01, 02, 05, and 06 were not
run through agents in the 2026-09-20 batch. The newer paired timing experiment
uses separate scenario IDs and records its own executed set. The revised skill
has not been behavior-tested in Claude Code, Copilot CLI, Cursor, Gemini
CLI, OpenCode, or Windsurf. Automatic activation, real host compaction,
cross-machine handoffs, and dynamic external-service checks remain outside
these observations. See [compatibility](compatibility.md) for documented
installation routes and evidence levels.
