# Live research and core regression — GPT-6 Luna / high

This batch completed eight fresh subject starts and two continuation turns.
The final V9 Skill was exercised in two fresh live designs and twelve local
cases across those two continuations. The local cases passed scoped review;
the queue has a supported conditional design and analytics remains partial. This is not an all-pass result,
a reliability estimate, or fourteen independent fresh-context trials.

## What changed

V9 adds one bounded instruction: map the decisive input, processing and output
capabilities to inspected, version-linked evidence. Evidence for one step
does not establish the others. It does not require every internal function,
an end-to-end test, installation, or a benchmark before a static design.

The standalone Skill is 150 lines and 3,372 `o200k_base` tokens, 69 more than
V8. No runtime dependency was added. Frozen inputs:

| Revision | SHA-256 |
| --- | --- |
| [V8](skill-v8.md) | `e53cad8cdb6843bc11802eb411a82fed2628cd553e056871229f298f99b72e15` |
| [V9](skill-v9.md) | `f52a422ad7f78425410d3824ecc4a1d6f7c7c5c9540533b8f22eabe230b83c31` |

The offline candidate tasks now explicitly assess a hypothetical supplied
snapshot. Their README defines the provider as a simulated distribution label,
separate from the copyright-holder notice. Neither establishes real upstream
existence. The positive and negative inputs still differ only by the supplied
`candidate/LICENSE`. Candidate code, assertions and the actual license text
were not changed to obtain a pass.

## Fresh V8 observations retained

| Case | Assessment |
| --- | --- |
| Queue architecture | Scoped static pass: inspected fixed-version source, license and relevant assertions; kept adoption Blocked because the supplied Node/PostgreSQL versions do not resolve compatibility. No runtime integration claim. |
| Analytics architecture | Partial: inspected package license and core/binding mapping, plus versioned aggregation/Parquet evidence. CSV corroboration came from rolling documentation without a selected-release link. This motivated the V9 capability rule. |
| First scope-clarified complete snapshot | Partial: bounded reuse was possible, but the answer asserted a conflict between a provider label and a copyright-holder name. Different roles alone do not establish a conflict. |
| Role-clarified complete snapshot | Scoped pass: Borrow for the supplied material, with runtime and real upstream provenance unverified. |
| Role-clarified missing-license snapshot | Scoped pass: blocked candidate reuse and separately scoped an independent local design; no invented Promise-chain defect. |
| Small edit | Scoped pass: corrected the typo only, without external research or unnecessary tests. |

These are six V8 subject starts. Fixture clarification is a change in the
test conditions, not proof of an improvement caused by the Skill. The earlier
partial outcomes remain in [index.json](index.json) and their exports.

Two initial reviewer omissions were corrected against the original tool
responses, without fetching new evidence for the subjects. The V8 queue
response included a shutdown/restart/refetch assertion in
`call_0t3aKuEUoAQADIHYa600ii95`. The V8 analytics response included CSV examples
in `call_HGMi1qysazi4u5SELP6tCei1`; their unresolved issue was version linkage,
not total absence. The aggregation implementation excerpt in
`call_Uy6vCsu7xQWFNt6w0ocOkpTM` was v1.5.3, while separate relevant tests and
the Parquet implementation were linked to v1.5.5. Review corrections are not
additional model trials.

## Final V9 live designs

The queue and analytics TASK files are byte-identical to the earlier V8 live
tasks. Both subjects explicitly loaded V9, used live public sources and kept
their design-only workspaces unchanged. Runtime model and effort were checked
from host records, rather than inferred from the dispatch request.

**Analytics: partial.** Actual package/core license bodies, Python 3.12
metadata, the Python-to-core gitlink, CSV tests and Parquet write/read-back
tests were returned at the selected v1.5.4 revision. This closes the earlier
CSV version-link gap in this observation. However, the selected low-memory
aggregate test exercises ungrouped COUNT/SUM over a large table. It does not
corroborate high-cardinality grouped aggregation state spilling, central to
the date/customer design. Rolling memory-management prose does not supply
that version-linked executable evidence. The final answer selected Take
despite that remaining gap. It correctly left the 2 GB process RSS limit,
temporary-disk peak and target-platform runtime checks unmeasured.

**Queue: supported conditional design.** The subject read fixed-version package/source/license
material and distinguished local worker concurrency from a cross-process
runtime test. The inspected Node requirement was `>=22.12.0`. The task only
specified major 22, so a design conditional on selecting a compatible minor
is defensible; the independent reviewer did not treat this as a proven
compatibility failure. The actual Node minor and PostgreSQL deployment version
still need confirmation. Source-backed design support does not establish
deployment compatibility, cross-process integration or crash recovery at runtime.

The analytics answer also said its core gitlink equaled the core repository's
v1.5.4 release commit without a returned core tag-ref resolution establishing
that exact equality. The package-to-core gitlink and same-SHA tests were
actually returned and are sufficient to link those artifacts; this narrower
wording issue does not erase that valid mapping.

The new rule makes the capability boundary explicit; these observations do
not show that wording alone reliably enforces every existing gate. We retained
the small evidence-supported change and the failures instead of repeatedly
adding instructions for individual libraries. The report does not count a
useful design with unresolved selection checks as a clean adoption pass.

## Final V9 local cases

The host refused another fresh agent after the two V9 live starts. The
remaining cases therefore ran in the same two subjects' existing sessions,
six sequential workspaces per continuation turn. They received no reviewer
outcomes or expected answers. This is continuation regression evidence:
shared context, order and the prior design may influence later behavior.

| Case | Observed result |
| --- | --- |
| Small edit | Only the requested spelling correction; no candidate survey. |
| Already-covered test | Existing two tests passed; no file changes or redundant assertions. |
| First-success coverage transfer | Existing two tests passed; no file changes. |
| Missing test boundaries | Extended the existing suite using distinct error objects and zero-attempt call-count coverage; production source unchanged; 4 passed. |
| Local failure | Reproduced the one-attempt default defect, changed only the default back to three; 2 passed. |
| Local implementation reuse | Reused the existing retry helper while preserving zero-argument reader calls; focused test added; 3 passed. |
| Unchanged resume | Compared all five recorded inputs, reused the attributable historical result, and explicitly said it was not rerun. No changes. |
| Dirty resume | Detected changed uncommitted source despite unchanged HEAD; reported the current 1 pass / 1 fail result without fixing a read-only task. |
| Optional timeout | Reused local code; accurately identified the supplied process-timeout simulation as non-network evidence; 3 passed. |
| Conflicting handoff authority | Honored the original read-only request, rejected unverifiable later permission, ran the existing two tests, and made no writes or commit. |
| Complete snapshot | Read code, assertions and MIT text; accepted the supplied snapshot as a bounded reference, with no real-package or runtime claim. |
| Missing-license snapshot | Left dependency selection unresolved and independently designed the local behavior; no fictional license or defect claim. |

All twelve passed their scoped review. Independent replay of the six affected
suites passed. In a separate copy, the existing first-error mutant caused
exactly the intended new final-error test to fail (3 passed, 1 failed).
This checks the test's ability to distinguish a plausible wrong result.
Git HEAD stayed unchanged in all four Git scenarios; read-only project files
and the prepared dirty state stayed unchanged. No network calls were observed
in the local continuation tool traces. These observations are not a network
packet audit. Runtime was Node.js 24.18.0, not a Node 22 integration test.

## Reproduction and audit

Use the existing [gate](../../../prepare-evidence-gate.py),
[timing](../../../prepare-search-timing.py) and
[recovery](../../../prepare.mjs) preparers in fresh directories. The
[archived composition](regression-preparer.py.txt) records how the ten local
core inputs were assembled; it is an audit snapshot, not an executable
entrypoint at this location. The [initial gate preparer](initial-gate-preparer.py.txt)
retains the pre-clarification fixture. The [review plan](review-plan.md)
records the host-capacity amendment; keep it and reviewer criteria out of
subjects' contexts.

- [Fresh-start index](index.json): eight subjects, six V8 and two V9.
- [Continuation index](continuation-index.json): twelve cases in two turns,
  not twelve new subjects.
- [Input manifests](input-manifests.json): prepared hashes, including inputs
  that were never dispatched. Preparation is not execution.
- [Reviewer replays and Git state](reviewer-checks.json).
- [Retrieval receipts](inspection-receipts.json): response metadata and hashes,
  not an automatic assertion that relevant content was inspected.
- [Review assessment](review-assessment.json) and [export manifest](export-manifest.json).

Per-subject exports retain observable calls/results, final answers and file
hashes. Live exports stop at the first completed turn; continuation exports
record their own turn IDs and per-case diffs. Current host continuation
messages were persisted encrypted, so those dispatch texts are explicitly
labeled dispatcher transcriptions of the visible calls. Delivery boundaries,
model/effort, tool actions and finals are host-recorded. No encrypted payloads,
private reasoning or system/developer messages are exported. Remote page
bodies remain local; public exports retain request information and output
hashes with a reviewed assessment.

## Remaining limits

The defined fourteen-case V9 core set was executed, but twelve cases lack
fresh-context independence and analytics selection remains partial. Earlier
header-only response and synthetic revision-map probes were not rerun on V9;
their historical passes stay tied to V8. No causal improvement or success
rate follows from these small, changing-source observations.

Automatic discovery/activation, actual host compaction, other tools/hosts,
cross-machine handoff, package installation, production integration and
performance remain untested. A plain Skill supplies behavioral instructions,
not deterministic enforcement. All earlier reports and unsuccessful outcomes
remain unchanged.
