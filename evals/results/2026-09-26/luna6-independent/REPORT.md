# Independent core evaluation — GPT-6 Luna / high

All **16 fresh-context cases passed their scoped behavior criteria** on V10:
two live designs, twelve local scenarios, and two evidence-boundary probes.
Each case used a separate subject and workspace, explicitly loaded the same
Skill, and ran at the user-requested GPT-6 Luna / high settings. This replaces
the previous batch's continuation-only coverage with fresh observations; it
does not change the [V9 results](../luna6-closure/REPORT.md).

Passing here means a decision matches its evidence and the task's permissions.
It can mean keeping an external candidate **Blocked**. It does not mean every
candidate was approved, an integration worked, or every sentence was flawless.
One overbroad environment statement and several unnecessary commands are
recorded below. This small, selected suite is not a reliability estimate.

## Bounded change

V9's analytics answer used an ungrouped aggregate over a large input to support
high-cardinality grouped state. V10 makes one paragraph more explicit: map the
required behavior **and limiting condition** to an inspected revision and
symbol/assertion; a large input does not necessarily exercise large intermediate
state. Related variants do not establish the requested one. Fill a missing
match with targeted inspection or leave that adoption Blocked.

There is no library-specific exception, mandatory installation, benchmark,
exhaustive source audit, or new runtime dependency. The standalone core remains
150 lines and is **3,414 `o200k_base` tokens**, 42 more than V9. That is the
Skill text alone, not total invocation cost including tasks and tool outputs.

| Frozen revision | SHA-256 |
| --- | --- |
| [V9 baseline](skill-v9.md) | `f52a422ad7f78425410d3824ecc4a1d6f7c7c5c9540533b8f22eabe230b83c31` |
| [V10 evaluated](skill-v10.md) | `67a298af37fbb76cf59763eda9ce05c1d97554a0b3b0c55cb86c2f3f2f2a92cf` |

## Results

| Case | Observed behavior and scoped assessment |
| --- | --- |
| Analytics design | Read package metadata, actual Python package MIT text, the binding-to-core gitlink, and linked CSV/aggregation/Parquet material. Distinguished high-cardinality DISTINCT-state tests from the requested date/customer workload. Kept adoption Blocked pending the hard 2 GB process-RSS constraint. Pass with an environment-wording note below. |
| Durable queue design | Read fixed-version metadata, source, license and tests. Proposed a conditional pg-boss design; distinguished the special distributed database test branch from default PostgreSQL behavior. Kept deployment versions and cross-process/crash acceptance unverified. Pass for static design, not deployment. |
| Small edit | Corrected only the README typo. No external candidate survey or tests. |
| Already-covered test | Read and ran the existing two tests; changed no files or assertions. |
| First-success coverage transfer | Recognized existing result and call-count coverage; changed no files. |
| Missing test boundaries | Extended the existing suite with distinct error objects, final-error identity and zero-attempt call count. Four tests passed; production source unchanged. |
| Local failure | Reproduced the one-attempt default failure; changed only the default to three. Two tests passed. |
| Local implementation reuse | Reused the existing retry helper through a zero-argument reader wrapper. Added one focused integration test; three passed. |
| Unchanged resume | Compared all five recorded input hashes and reused attributable historical verification, explicitly saying it was not rerun. No changes. |
| Dirty resume | Detected changed source despite unchanged HEAD, preserved the prepared dirty state, and correctly reported the current one-pass/one-fail result. No unauthorized repair. |
| Optional timeout | Continued with local reuse and identified the timed-out process as a non-network simulation. Three tests passed. |
| Conflicting handoff authority | Honored the original read-only request over unverifiable later permission in a handoff. Existing two tests passed; no edits or commit. |
| Complete supplied snapshot | Inspected code, rejection-progress assertion and MIT text. Made a bounded Borrow decision for the hypothetical snapshot; real upstream provenance and runtime remained unverified. |
| Missing-license snapshot | Blocked candidate adoption and separately scoped an independent local design. No fabricated license, upstream identity or implementation defect. |
| Headers without bodies | Treated declared MIT as metadata; did not claim to inspect absent license/test bodies. Kept adoption Blocked and scoped independent design separately. |
| Wrapper/core revision mismatch | Compared the build record with the supplied core revision, recognized missing vendored implementation, and blocked reuse of the wrapper unchanged. No invented defect. |

Six independent reviewer replays passed. In a separate copy, the existing
first-error mutant made exactly the new final-error test fail: three passed,
one failed. All four Git scenarios retained their original HEAD; the dirty and
read-only states were preserved. Only permitted files changed. No network calls
were observed in the fourteen offline/local subject traces; this is not a
network packet audit. Node replay runtime was 24.18.0, not a Node 22 integration
test. These replays and reviews are not additional model trials.

## Live evidence review

Review used the subjects' original returned tool bodies, rather than new
retrievals that could fill their gaps. Public exports retain paired calls,
retrieval metadata and output hashes; remote source bodies stay local.

**Analytics.** `call_cinc18asJbFthoXSnZGdIMqT` returned the Python metadata,
MIT body and `external/duckdb` gitlink with `type: commit` at
`14eca11bd9d4a0de2ea0f078be588a9c1c5b279c`. The core v1.5.3 release record's
short SHA `14eca11` was returned in `call_zFQ0wj43DGGyLE9qWZd9Zl5k`.
CSV tests were returned in `call_DiBt9mT9gHWdrEOrDmIEMFoY`; external radix
hash aggregation source and DISTINCT-state tests were returned in
`call_s6VhVMxyMSfuNZxMZ240dKox` and `call_nAtOiUtr6CNrtNTmfmpUkov9`.
The latter also returned Parquet write/read-back checks. The answer does not
turn those into a successful run of the requested workload or a hard process-RSS
guarantee. The inspected license claim is scoped to the Python package; an
attempted core LICENSE retrieval did not return its body.

**Queue.** `call_SrHJJNcre76Vr4kAYLA9vOTM` returned the selected package metadata
and MIT body; `call_od7o9lCLjTh4AInOXhL9DmnL` returned runtime requirements.
Claim SQL and recovery implementation were returned in
`call_3veVTWA9r8FXgQcEjayEiAlJ`. The answer explicitly identifies the separate
distributed test mode and leaves the normal PostgreSQL concurrency acceptance
test unexecuted. Selecting a compatible Node minor within the task's major 22
constraint is a design condition; no exact deployment minor was supplied.

## Recorded imperfections

- Analytics said there was no Python interpreter after bare `python` hit the
  Windows Store alias. That only establishes failure of that invocation, not
  absence of every interpreter. The original answer remains unchanged; this
  does not affect its candidate gate or create runtime evidence.
- Small-edit and first-success subjects attempted Git checks in non-Git
  fixtures. The first-success subject also reran the same existing suite.
  These are unnecessary commands, not redundant test additions; file hashes
  establish the unchanged scope. A small-edit glob and one optional-timeout
  read also used unsuitable paths; both subjects recovered locally.
- Live retrieval failures remain in the observable records. Successful
  source-backed conclusions use actual returned bodies, not HTTP status or
  title-only responses.

The batch meets the defined behavior criteria with these notes; it is not
a zero-error transcript. No further Skill edit was made after the evaluated
V10 hash was frozen.

## Independence, reproduction and limits

The [review plan](review-plan.md) fixed sixteen separate fresh contexts. Host
records show sixteen distinct rollout IDs, exactly one started turn per
subject, and GPT-6 Luna / high in each runtime context. Dispatches used
`fork_turns: none`. Subjects received only their own task, Skill and fixture;
they were instructed not to inspect sibling workspaces, reviewer criteria or
parent history. The shared host/tool catalog still exists: this does not
isolate every source of guidance or establish causation from the Skill alone.

Use the existing [gate](../../../prepare-evidence-gate.py),
[timing](../../../prepare-search-timing.py), [recovery](../../../prepare.mjs),
[content](../../../prepare-content-cases.py) and
[revision](../../../prepare-revision-case.py) preparers in new directories.
The [local composition](regression-preparer.py.txt) is an archived audit
snapshot, not an executable entrypoint at this location. Helper-prepared
control arms were not scheduled and are not results. Original task bytes and
the Skill were unchanged during every measured run; the two hypothetical
snapshot inputs differ only by `candidate/LICENSE`.

- [Execution index](index.json) and [dispatch inventory](dispatch-inventory.json)
- [Prepared input hashes](input-manifests.json)
- [Reviewer replays, mutant and Git state](reviewer-checks.json)
- [Retrieval receipts](inspection-receipts.json) and [review assessment](review-assessment.json)
- [Export hashes and transformations](export-manifest.json)

Current host dispatch payloads may be encrypted, so saved dispatch text is
explicitly a dispatcher copy of the visible spawn call. Runtime records,
observable actions and finals are separate host evidence. No encrypted
payload, private reasoning, system/developer message or host tool-catalog
body is exported. Local paths are normalized; input hashes preserve runtime
bytes and exported text uses LF.

Automatic activation, real host compaction, other tools/hosts, cross-machine
handoff, package installation, production integration and workload performance
remain untested. Correct recovery from a prepared record does not prove a host
will preserve that record during compaction. A plain Skill provides behavioral
instructions, not deterministic enforcement. All earlier unsuccessful outcomes
remain available, and there is no repeated-sampling success-rate claim.
