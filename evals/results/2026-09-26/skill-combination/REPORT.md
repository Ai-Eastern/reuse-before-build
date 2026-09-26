# Explicit Skill combination — 2026-09-26

The V13 addition shares one evidence inventory, reuse decision and verification
plan across active Skills. Existing adequate tests remain the runnable check;
necessary decision records and planning-only scope survive terse-output
preferences. It adds no companion dependency or host-enforced precedence.

Eight fresh **GPT-6 Luna / high** subjects explicitly read reuse-before-build
and the unchanged local ponytail Skill, in both orders. All eight passed the
bounded loading, behavior, scope and workflow criteria. No case introduced a
duplicate implementation, standalone demo, second test runner or competing
decision record. Some repeated verification commands remain visible below.

This is an explicit combination check, not natural dual activation, a causal
before/after comparison, a reliability estimate or a full core rerun. The
[previous V12 evidence-gate failures](../native-host/REPORT.md) were not repaired
or rerun by this change. They must not be treated as resolved by these passes.

## Frozen inputs and execution

| Input | Value |
| --- | --- |
| Target | V13; 158 lines; 3,664 `o200k_base` tokens; +8 lines / +167 tokens over V12 |
| Target SHA-256 | `565191c1152b780d73284b9a7e054aef3511de1dd07e1b3788a86f99fda1005f` |
| Companion | Local ponytail snapshot, unchanged default `full` intensity |
| Companion SHA-256 | `1316a2f3f95741d2300b116fe0c2d81ce4a9568656ed0a62643f54aaf09957f2` |
| Host | Desktop-bundled Codex app-server `0.158.0-alpha.2`, Windows |
| Model | `gpt-6-luna`, `high`, provider fallback disabled |
| Subjects | 8 distinct ephemeral threads, one ordinary task turn each |
| Runtime for code checks | Node.js `v24.18.0`, existing built-in `node:test` runner |

The [fixed plan](review-plan.md) preceded execution. Each task was repeated
once with each read order: `rp` reads reuse-before-build then ponytail; `pr`
reverses that order. The business files and task wording were identical
between each pair, except for the explicit invocation order in `TASK.md`.
Prompts did not include the reviewer answers. There was one candidate and
no failing-case tune-and-retry loop.

Other discovered Skills were disabled in each child process; exactly the two
project-local copies were enabled. No global configuration was changed.
Returned full bodies and their order were verified from command outputs,
not from the subject's claim that it used a Skill. All eight returned both
complete bodies in the requested order, with the declared model and effort.
The target and companion hashes and each fixture's initial HEAD stayed fixed.

Networking, installation, services and commits were prohibited by task scope;
web search was disabled. This is an observation of task actions, not a claim
that all network transports were physically blocked. Pytest was unavailable
locally and was not installed; these cases do not validate pytest or other
third-party framework/fixture compatibility.

## Results

| Cases | Requested task | Observed result in both orders |
| --- | --- | --- |
| `covered-rp`, `covered-pr` | Check default-three retry coverage already present | No files changed; reused the existing two passing tests. |
| `adapt-rp`, `adapt-pr` | Add transient recovery to `fetchStatus` while keeping reader calls argument-free | Imported the unchanged `retry` helper through `retry(() => readStatus())`; extended the original test file and updated its existing README; four tests passed. |
| `gap-rp`, `gap-pr` | Cover final-error identity, attempt count and zero-attempt rejection | Changed only the original test file; used distinct errors and strict final-object identity; four tests passed. |
| `design-rp`, `design-pr` | Evaluate the supplied hypothetical MIT snapshot and retain the design handoff | Read the actual manifest, source, test and license; changed only existing `DECISIONS.md`; retained evidence, boundaries and next checks without implementation or installation. |

The design conclusions apply to a fictional supplied snapshot, not a real
package or verified upstream. Both records distinguish inspected static
evidence from unexecuted runtime checks. A terse-output preference did not
erase the required record or expand planning into implementation.

An independent reviewer checked the returned bodies, edits, final answers
and scope. A separate replay used copies outside the subject directories:

- Five distinct source/test groups passed **18/18** existing and added tests.
- Both adapters had identical production hashes, so one independent probe
  group covered first success, third success and final-error identity with
  zero reader arguments: **3/3 passed**.
- The previously available first-error mutant was replayed against each gap
  variant. Each produced **3 passes and 1 expected failure**, solely in the
  added final-error identity assertion.
- Both design artifacts changed only `DECISIONS.md`; reviewer work changed
  no subject files or HEADs. Reviewer executions are not extra model trials.

## Remaining limits and inefficiencies

Both covered cases ran the same deterministic suite twice. `adapt-pr` reran
its tests after a README-only correction. These are redundant verification
commands, not evidence that the two Skills created separate implementations
or test workflows. This batch does not establish zero repeated operations.

`design-rp` recovered from a failed PowerShell here-string write after checking
the existing file. The original failure is retained. It was not a clean
command transcript, although the final scoped artifact passed review.

`gap-rp` checked a nondefault positive attempt count of two; `gap-pr` explicitly
used three, equal to the default. The latter does not distinguish a defect
that ignores other positive configured counts. Both meet the frozen
first-error mutation check; broader configuration mutation coverage is not
claimed.

No natural dual-trigger test, real context-pressure compaction, GUI test,
other host/model, production integration or live-search timing trial was
added. Ponytail's other intensities were not tested. The historical V10
16-case core pass belongs to V10; this eight-case V13 batch does not replace
it or clear the two V12 headers-only adoption failures.

## Audit artifacts

- [Frozen target Skill](skill-v13.md), [companion identity](companion.json)
  and [input manifest](input-manifest.json).
- [Input equivalence](business-equivalence.json) and [case index](index.json)
  link the eight distinct subjects and their sanitized observable traces.
- [Independent review](review.json) and [replay receipts](replays.json) keep
  model outcomes separate from reviewer verification.
- [Client](combination-client.py.txt), [base native client](native-client.py.txt)
  and [input preparer](input-preparer.py.txt) are audit text for this local
  setup, not portable launchers or required Skill dependencies.
- [Export manifest](export-manifest.json) hashes the public artifacts.

The private companion body is not redistributed. Outputs that returned it
are omitted as a whole, with original-output hashes and pre-redaction
full-body/order receipts retained. Unrelated personal Skill identities and
local paths are sanitized. These are bounded public observables, not complete
raw logs; the companion hash identifies the evaluated local snapshot rather
than certifying compatibility with every ponytail distribution.
