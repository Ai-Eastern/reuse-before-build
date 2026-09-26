# Candidate evidence follow-up — GPT-6 Luna / high

Recorded 2026-09-26, Asia/Shanghai. **Nine completed model runs, not nine
passes and not a complete final-version regression suite.** The model and
reasoning effort were explicitly requested by the project owner and verified
from actual host runtime events for every exported turn.

The final revision made the analytics agent keep a candidate unresolved when
its version linkage and corroboration were missing. The queue agent inspected
versioned source and tests, and no longer presented a special database-mode
test as proof of the normal PostgreSQL path. These are bounded observations;
runtime compatibility, integration and performance were not verified. Independent
review accepts the final queue design's static evidence, but grades analytics
partial: its Blocked decision is appropriate, while its Python-package license
claim exceeds the contents actually returned by the tool.

## Revisions and executed set

The starting point was published commit `534844b`. We changed the instructions
only after observing baseline behavior with the new model configuration.

| Skill snapshot | SHA-256 | Completed runs |
| --- | --- | --- |
| [V5, published baseline](skill-v5.md) | `62651b60cc1ed43af2d8d8d6aa7a2a58dbbec46a834b56bd1139dc9b3e353f7c` | Queue, analytics, missing-license snapshot, revision-map transfer: 4 |
| [V6, first correction](skill-v6.md) | `5f1dc8921368ecc88b91d61af2ebe7612a360fccd1f7d5e66e1874ddf7a0eda6` | Queue, analytics, missing-license snapshot: 3 |
| [V7, final correction](skill-v7.md) | `8e5aef4b38de9888fe5379e49b79c07e2c55a4d1b22921e54a57eee06e6f2e95` | Queue and analytics: 2 |

Every measured run used a fresh context, its own workspace and a full Skill.
Shared task files were byte-identical across repeated cases, including copied
historical checkpoint/TAP inputs. Only the Skill differed. Agents did not
receive the parent conversation, reviewer criteria, previous outcomes or
proposed fixes. They still shared the host's common instructions and catalog;
the workspaces were instruction-scoped, not OS security sandboxes.

This is a same-model instruction comparison with live research variability,
not a no-Skill control or a causal comparison with GPT-5.6 Luna / medium.
Model and effort both changed from the [earlier experiment](../evidence-gate/REPORT.md).
Different live runs selected different upstream releases or retrieval routes.

## What changed

V5 analytics still selected an artifact without linking the Python and core
revisions. V6 therefore required an inspectable build/submodule/version mapping,
clarified meaningful corroboration, and reconciled final component choices
with the receipt. Executable, versioned documentation examples remain valid
call sites for the behavior they actually demonstrate. Missing candidate
evidence must not become an invented defect or an unsupported Build decision.

V6 queue retrieved a concurrent-fetch test, but it used a special PGlite /
distributed mode instead of normal PostgreSQL claiming. V7 added a check of
test setup, backend, mocks, feature flags and implementation branches before
transferring test evidence. The core remains standalone: 146 lines, about
3,180 `o200k_base` tokens, up 234 from V5. That is a tokenizer measurement,
not a guaranteed provider billing count.

The [review plan and repair history](review-plan.md) preserve both hypotheses
and the two bounded corrections. No third repair was made to chase a pass.

## Observed outcomes

| Case | V5 baseline | V6 | V7 final follow-up |
| --- | --- | --- | --- |
| Durable PostgreSQL queue | [Pinned source/license and executable API examples](luna6_queue_v5.json); these support their demonstrated interfaces, while multi-worker corroboration remained limited | [Read actual tests](luna6_queue_v6.json), but generalized a PGlite/distributed-mode concurrent-fetch test to normal PostgreSQL | [Read pinned retry, fetch and expiry tests](luna6_queue_v7.json); no longer cites the special-mode test as ordinary PostgreSQL proof. Multiple-process and crash behavior remain planned integration checks. |
| CSV → grouping → Parquet | [Selected DuckDB](luna6_analytics_v5.json) with unlinked Python/core tags and incomplete versioned corroboration | [Retrieved the Python tag's core gitlink](luna6_analytics_v6.json), but the v1.5.5 test lookup returned no body. The actual test contents read were from v1.5.1; its Take decision still lacked selected-version corroboration. | [Kept DuckDB adoption Blocked](luna6_analytics_v7.json) when the gitlink and versioned corroboration were unavailable. The option-only decision is appropriate, but its package-license claim remains unverified. |
| Missing-license snapshot | [Blocked adoption](luna6_snapshot_b_v5.json), but its final answer asserted an unsupported `.finally()` rejection risk | [Blocked candidate adoption separately from an independent design](luna6_snapshot_b_v6.json), without repeating that defect claim | Not executed |
| Core/wrapper revision transfer | [Detected different core commits and missing vendored source](luna6_revision_v5.json); correctly left unchanged wrapper adoption Blocked | Not executed | Prepared, not executed |
| Complete licensed snapshot | Not executed | Not executed | Prepared, not executed |
| Already-covered retry behavior | Not executed | Not executed | Prepared, not executed |

**A safe Blocked decision is a gate observation, not successful adoption.**
The final analytics run did not finish component selection. It avoided turning
an incomplete receipt into a selected stack, while continuing an explicitly
provisional design. This does not show that retrieval became more reliable:
V6 found a gitlink that V7 did not retrieve.

**A returned page header is not an inspected file.** V6 claimed to inspect
v1.5.5 `parquet_hive.test`, but that response contained only the source header
and total-line count. The actual numbered test contents returned were v1.5.1;
no inspected mapping established that the tests were unchanged. V7 likewise
described the Python package's v1.5.5 license as inspected MIT evidence even
though that file's response contained no body. The core license did return
contents. This does not establish that the package lacks a license; it means
the claimed package-specific inspection was not demonstrated. These reporting
errors are retained, and neither run receives an unqualified pass.

**Test inspection is also scoped evidence.** V7's queue tests concern retries,
future-job eligibility and expiry supervision. They were inspected, not run.
They do not prove this project's multi-process crash recovery, target database
configuration or external-effect idempotency. The original local retry tests
cover a different in-process contract and do not validate any queue choice.

**The baseline defect claim was incorrect.** In the supplied limiter,
`.then(resolve, reject)` handles the task rejection and returns normally;
the intermediate promise therefore fulfills before its cleanup handler.
The final answer's unhandled-rejection claim was unsupported by that path.
A reviewer replay passed the existing rejection-progress test under Node.js
24.18.0; it was not exhaustive verification or a Node.js 22 run. The original
answer is retained unchanged in the record, rather than silently repaired.
The initial reviewer also accepted that risk; a subsequent control-flow trace
corrected the review before the final assessment.

## Coverage limit and evidence boundaries

After dispatching the two final live tasks, spawning the complete-snapshot
probe returned **`agent thread limit reached`**. No model ran for that probe.
The final missing-license, already-covered-test and revision-map probes were
also not started. Prepared inputs are retained; none count as completed tests
or passes. The revision transfer fixture has one V5 observation, not a completed
previous/current comparison. Earlier V6 local evidence cannot be relabeled V7.

- Nine executed runs: four V5, three V6, two V7. Reviewer work and local test
  replays are excluded from that count. Final-version coverage is incomplete.
- Candidate fixtures, providers and revision identifiers are synthetic. Their
  license files and build records test reasoning about supplied evidence; they
  do not establish real upstream provenance or platform compatibility.
- No evaluated agent changed the supplied source, tests, Skill or checkpoint
  inputs. Some wrote design/decision Markdown. No packages were installed,
  external source executed, databases accessed or benchmarks run.
- Several guessed paths failed or returned unusable content. Tool failures and
  unsuccessful decisions remain visible in the records. The live search budget
  is exploratory, not a measured latency or cost benchmark.
- [Observable records](index.json) include task dispatches, verified model/effort,
  tool calls/results, final answers, changed files and input/output hashes.
  [Inspection receipts](inspection-receipts.json) identify retrieved contents;
  they do not certify that the agent interpreted those contents correctly.
- [Review assessment](review-assessment.json) separates static design, decision
  discipline, receipt accuracy and unexecuted coverage. Independent review
  findings were checked against the recorded tool bodies before publication.
- Private reasoning, system/developer messages, host catalog descriptions and
  full remote page bodies are excluded. A task-local working copy of public
  tool outputs supported review and is not published. See the
  [export transformations and hashes](export-manifest.json).

These observations do not establish a general success rate, reliable automatic
activation, other-host behavior, real compaction recovery, or complete behavior
coverage. Format/CI checks are reported separately from agent decisions.

## Reproduce

Use the [evaluation preparation instructions](../../../README.md), select the
declared model/effort, and retain actual runtime settings. The main preparer
creates seven inputs; the separate revision preparer creates two. Neither
launches a model. Keep reviewer criteria and previous outcomes out of fresh
agent contexts, and report the subset actually executed.
