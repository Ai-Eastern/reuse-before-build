# Search timing and test reuse — GPT-5.6 Luna / medium

Recorded on 2026-09-21 (Asia/Shanghai; telemetry timestamps use UTC).
**17 completed model runs**, not 17 passes. Search timing and direct test
reuse showed useful behavior; candidate source/license inspection remained
unreliable even after a follow-up rule. The failures are retained below.

## Setup and revisions

All evaluated agents used fresh context with `gpt-5.6-luna`, reasoning
`medium`. The exporter checked the actual host `turn_context` model and
effort on every recorded turn; each record includes those fields and the
dispatch, rather than relying on the agent's own model claim.

The host was Codex desktop on Windows with PowerShell and Node.js 24.18.0.
Node.js 22 was the architecture task's target, not the installed test runtime.
Each task used the repository's MIT retry fixture in a separate directory.
Control and treatment shared identical initial task/source/test bytes;
treatment additionally received the frozen Skill and an instruction to use
it. Both could access public internet tools. Neither received the reviewer
rubric or parent conversation. Scope isolation was instructional, not an OS
sandbox. There were no package installations or real database integrations.

| Revision | Frozen Skill SHA-256 | Executed runs |
| --- | --- | --- |
| [V1: event-based timing](skill-v1.md) | `591bb93753616250d04cd6635069015bb2f7ffa8a92e24154fda5482b4e1c355` | 6 initial control/treatment pairs = 12 |
| [V2: logical coverage, no redundant edits](skill-v2.md) | `9b953ba824a9ed5004db7982945c94673c3aea272dff42c5ea4fb4a0b7172fc4` | Original covered task, treatment only; first-success transfer, both arms = 3 |
| [V3: discriminating test inputs, provisional candidates](skill-v3.md) | `a77d13420dddd2608d623941983c0b0e7dd5ab8dc9f7e44fa300d14425400534` | Test gap and changed requirements, treatment only = 2 |

V3 is the Skill published with this report. The other cases were not rerun
on V3. Follow-ups did not silently replace initial failures, and V3 has no
fresh control runs. The prepared manifests contain more workspaces than
were executed: [V1](v1-prepared-inputs.json), [V2](v2-prepared-inputs.json),
[V3](v3-prepared-inputs.json). Only the [17-record index](index.json) counts
as model evaluations.

## Initial paired observations

| Case | Without full Skill | With V1 Skill | Review |
| --- | --- | --- | --- |
| Small typo | [Only README changed](luna_small_control.json) | [Only README changed](luna_small_skill.json) | Both stayed local; no unnecessary tests or survey. |
| Already-covered third attempt | [Added a redundant length assertion](luna_covered_control.json) | [Added the same redundant assertion](luna_covered_skill.json) | Both tests passed, but neither respected direct reuse without an unnecessary edit. |
| Missing boundary tests | [Extended existing tests; 4/4 passed](luna_gap_control.json) | [Extended existing tests; 4/4 passed](luna_gap_skill.json) | Both reused the runner and preserved production code. Treatment did not distinguish first from last error; see mutation check below. |
| Local regression | [Restored default attempts from 1 to 3](luna_failure_control.json) | [Same bounded repair](luna_failure_skill.json) | Both reproduced locally, changed only the helper, and passed 2/2 tests. No candidate survey. |
| Unchanged resumption | [Read saved evidence; no edits](luna_resume_control.json) | [Compared hashes; no edits](luna_resume_skill.json) | Both ran 2/2 tests and stayed local. A relevant fresh check is permitted; this does not demonstrate avoided test execution. |
| New durable-work requirement | [Custom PostgreSQL queue design](luna_changed_control.json) | [Local inspection, public search, then Graphile Worker proposal](luna_changed_skill.json) | Control wrote reference URLs without fetching them. Treatment searched at the appropriate point, but selected Borrow without inspecting candidate source/license. Evidence gate failed. |

No external candidate research was observed in either arm of the five local
cases. That is not evidence that the Skill alone caused restraint: the
control already behaved well on this dimension. The changed-requirement
treatment made one failed JavaScript search call followed by one successful
search batch; these are not two successful searches. Its existing retry
tests did not validate a durable queue.

## Follow-ups and what changed

V1's `deepEqual(seen, [1, 2, 3])` already guaranteed the number and order of
calls. Adding `seen.length === 3` did not improve coverage. V2 made this
logical implication explicit and required no edit when coverage is complete.

- [Original task, V2 treatment](luna_covered_skill_v2.json): no files changed;
  existing 2/2 tests passed. There was no new control run for this repetition.
- First-success transfer: [control](luna_variant_control.json) rewrote an
  existing `[1]` assertion into call-count checks, without additional
  behavioral coverage; [V2 treatment](luna_variant_skill_v2.json) left files
  unchanged and passed the existing tests. Both ran the tests twice; this
  is no evidence of fewer executions or lower cost.
- [Test gap, V3 treatment](luna_gap_skill_v3.json): used distinct errors and
  asserted the final object's identity, preserving production code and the
  two baseline cases. All four tests passed. The mutation check now failed
  for the intended reason, demonstrating a meaningful assertion.
- [Changed requirements, V3 treatment](luna_changed_skill_v3.json): local
  inspection again preceded public search. It correctly separated the old
  local retry decision and Node 24 historical tests from new Node 22 queue
  requirements. **It still chose Borrow after only a search batch**, without
  source or license inspection. The added provisional-candidate rule did
  not reliably enforce the evidence gate in this run. Its design remains
  an unverified candidate proposal; no package compatibility is established.

## A green test can still miss the defect

The V1 treatment threw the same error object on every attempt. Its final
identity check could not distinguish the first error from the last one.
A reviewer copied the completed outputs to separate directories and applied
the same [intentional mutant](first-error-mutant.mjs): remember the first
error and throw it at the last attempt, leaving the call-count behavior
unchanged. Formal model workspaces were not modified.

| Completed suite against the mutant | Observed result | Meaning |
| --- | --- | --- |
| V1 control | [3 passed, 1 failed](mutation-control.tap) | Caught first-versus-last error defect. |
| V1 treatment | [4 passed](mutation-skill.tap) | Missed the defect despite a green suite. |
| V3 treatment | [3 passed, 1 failed](mutation-skill-v3.tap) | Caught the defect; [unchanged production baseline passed 4/4](mutation-v3-baseline.tap). |

See the [initial mutation receipt](mutation-evidence.json) and
[V3 receipt](mutation-evidence-v3.json) for commands and hashes. These are
reviewer checks, not additional model trials. They establish this particular
distinction, not exhaustive test quality.

## Evidence limits and harness deviations

- The host supplied common coding instructions and an installed Skill
  catalog to both arms. Control was prohibited from reading Skill bodies.
  This is **full-Skill versus no-full-Skill** in the same host, not a model
  with no guidance. Explicit loading does not test automatic triggering.
- One pair per initial case and a few targeted follow-ups do not establish
  a pass rate, token savings, or a causal effect of one paragraph alone.
  Follow-up cases were chosen after observing failures; they are not a
  preregistered or blinded statistical benchmark.
- In V1 covered-test treatment, an attempted cross-task notification to
  `/root` failed. V1 test-gap treatment and V3 architecture treatment also
  queried the host tool catalog for collaboration tools. These are harness
  deviations, retained in the records. No successful cross-task information
  retrieval or global Skill-body read was observed.
- Records contain observable tool calls/results, input/output hashes,
  changed-file contents, final answers, and separate reviewer test replays.
  They are not a network packet audit. No observed call means only that no
  call appears in this exported host telemetry.
- Private reasoning and system/developer messages are excluded. Local
  paths are normalized; internal chat metadata is removed. Remote page
  bodies and host tool descriptions are omitted, retaining hashes/sizes and
  remote URLs. See [export transformations and integrity hashes](export-manifest.json).
  These are sanitized records, not complete raw transcripts.
- No Claude Code, Cursor, Copilot CLI, Gemini CLI, OpenCode, or Windsurf
  behavior was evaluated. Real host compaction and cross-machine handoff
  were not exercised. Search timing success is distinct from validated
  adoption or runtime integration.

## Reproduce or extend

Use the [paired preparation instructions](../../../README.md) and keep the
[reviewer rubric](../../../search-timing-reviewer.md) away from the model.
The preparer creates seven pairs; it does not run agents. Use a fresh
directory and context per run, preserve identical shared inputs, pin the
Skill hash and actual model/effort, and report all failures. To repeat an
older treatment, replace the prepared Skill with the corresponding frozen
snapshot before dispatch and update its input hash. Fixture source and
baseline tests are available in [retry-service](../../../fixtures/retry-service/README.md).
