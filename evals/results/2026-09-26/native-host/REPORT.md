# Native host acceptance — GPT-6 Luna / high, 2026-09-26

**This is not an all-pass result.** Native loading and real recovery are now
observed, but V12 still selected a candidate with required evidence unread.
The V12 isolated real-source task succeeded without loading the target Skill.
These boundaries are distinct from V10's historical explicit 16-case pass.

## Revisions and fixed execution set

| Revision | Skill SHA-256 | Tokens (`o200k_base`) | Executed logical cases |
| --- | --- | ---: | ---: |
| V10 | `67a298af37fbb76cf59763eda9ce05c1d97554a0b3b0c55cb86c2f3f2f2a92cf` | 3,414 | 17 |
| V11 | `e270b9869812653a3b66787151200460df895ee0ada8a8e96db1e4e88239706d` | 3,435 | 11 |
| V12 | `f433ce850f4049a0c1fc49a21cffd3e539566777b084d9ac538dcab9e9a3ec35` | 3,497 | 13 |

V11 changes only the discovery description, naming test coverage and recovery.
V12 keeps that description and replaces one final evidence-check paragraph:
**inspected / not yet inspected / unavailable after checking**. A filtered file
search cannot establish absence; required unread evidence cannot support adoption.
The final standalone Skill remains 150 lines with no runtime dependency.

The [original plan](review-plan.md), [V11 plan](repair-plan-v11.md), and
[V12 plan](repair-plan-v12.md) were fixed before their respective model runs.
The V12 preparation supplement records a pre-execution plan revision and two
identical extra architecture fixtures. No further prompt repairs were made.
All earlier reports and failing observations remain unchanged.

There are **41 logical cases, 44 distinct native threads, 47 ordinary task
turns and 3 manual compactions**. Recovery workflows contain producer and
consumer turns; a handoff adds a distinct ephemeral thread. Compaction events
are separate from ordinary task turns. Reviewer checks are not model trials.
V11 and V12 each prepared six unavailable-target controls but did not run them;
the six actual V10 controls are shared historical observations, not new or
randomized concurrent comparisons. Source/helper directories are not extra tests.

## Host and isolation

The Windows desktop-bundled **Codex app-server 0.158.0-alpha.2** listed
`gpt-6-luna` with `high` effort; the standalone **0.153.4** CLI did not.
Every subject start verified the requested model, effort and ephemeral status,
with provider fallback disabled. This is the native JSON-RPC runtime, not
interaction with the desktop GUI. See [preflight](host-preflight.json).

Every task started in its own fixture and used an ordinary prompt without the
Skill name. `skills/list` verified discovery. The target personal copy was
disabled only in each app-server process; treatments contained a project copy
in `.agents/skills/reuse-before-build`, controls contained none. Other personal
skills remained available. Actual returned body text establishes loading;
a self-reported Skill name, discovery entry or correct result alone does not.

Tasks prohibited networking and the host setting disabled web search; this
does not prove all possible network transports were blocked. This batch cannot test
whether the Skill restrains live external searching when tools are available.
It also does not establish behavior under a pure no-guidance control.
Business inputs and task prompts match across revisions/arms; only target
availability/version and fresh working paths vary. Input hashes are retained.

## Observations

All rows below are target-available cases. Loading means an actual complete
body read, with producer/consumer separated for recovery.

| Task | V10 native | V11 native | V12 native |
| --- | --- | --- | --- |
| Complete snapshot | Loaded; 1/1 behavior pass | Loaded; false absence claim fails | Loaded in 3/3; 3/3 behavior pass |
| Existing test coverage | Loaded 0/3; behavior 3/3 | Loaded 3/3; behavior 3/3 | Loaded 3/3; behavior 3/3 |
| Headers-only evidence | Loaded 3/3; gate 3/3 | Loaded 3/3; gate 1/3 | Loaded 3/3; gate 1/3 |
| Manual compaction | Neither phase loaded; recovery passes | Both phases loaded; recovery passes | Both phases loaded; recovery passes |
| Separate-session handoff | Neither phase loaded; recovery passes | Consumer only loaded; recovery passes | Both phases loaded; recovery passes |
| Small README edit | Not loaded; bounded edit passes | Not loaded; bounded edit passes | Not loaded; bounded edit passes |
| Real-source slice | Not loaded; function/scope pass | Loaded; function passes, temporary-directory scope issue | Not loaded; function/scope pass |

V12 passes **11/13 scoped behavior cases**; the two headers-only adoption
failures remain. This is not an overall loading/compliance pass: its real-source
case did not load the Skill. Recovery explanation errors are also retained below.
There is no zero-error or general reliability claim.

A small-edit case need not load this Skill. A correct behavior without a body
read is useful host behavior, but cannot validate this Skill's activation or
credit the result to it. Likewise, body loading alone does not establish compliance.

The covered-test controls all preserved sufficient existing tests. No causal
benefit follows for that behavior. For headers-only controls, two of three
selected the candidate prematurely; the second merely retained a candidate
without approving reuse and passes the narrow gate. It was not regraded to
make the treatment look stronger. Three repetitions do not estimate reliability.

## Preserved failures and limitations

- V11 `architecture-on` used an extension-filtered file search which omitted
  the existing extensionless LICENSE. It never inspected that path, then
  falsely declared license evidence absent and chose to build. The complete
  MIT file is present in its initial manifest and unchanged snapshot.
- V11 `headers-on-1` and `headers-on-3` read only response metadata for license
  and tests, acknowledged missing bodies, yet selected Borrow. These are
  adoption failures even though the task is design-only and hypothetical.
- V12 `headers-on-1` and `headers-on-3` repeat premature adoption;
  `headers-on-2` keeps an independent design without approving the candidate.
  Deferring required static checks to implementation does not satisfy today's
  selection gate. No third repair or selective rerun was used to hide failures.
- V11's real-source tests use `os.tmpdir()` without a project-local override.
  This does not satisfy the generated test's project-only scope policy under
  the inherited default environment; the exact randomized path was not logged.
  Cleanup targets only its own newly created directory. Functionality passed
  independent checks. V10 and V12 use project-local temporary fixtures.
- V11 and V12 handoff consumers correctly found the default changed from three
  attempts to one and reported one passing/one failing test, but each final
  answer includes a sentence placing failure on the second attempt. The error
  actually occurs on the first. This explanation error is retained separately
  from correct stale-result detection, test results and read-only behavior.
- Some subjects made redundant test runs or failed instruction-path reads.
  Returned target text still counts as loading when a later command in the same
  invocation fails. Original nonzero outcomes remain in the sanitized traces.

V10/V11 differences do not prove the description caused behavioral regressions.
The two revisions have identical bodies and model outputs vary. V12's repeated
positive snapshots support the local absence-check repair on these inputs,
not a general guarantee that evidence gates are obeyed.

## Actual recovery and source work

Each recovery producer wrote its own HANDOFF.md and ran the existing tests.
For compaction, native `thread/compact/start` emitted a completed
`contextCompaction` item. For handoff, the consumer used a different thread ID
without the producer conversation. Between turns the evaluator deliberately
changed `attempts = 3` to `attempts = 1` without changing HEAD. Consumers must
inspect current content and must not treat old passing results as current.
Producer and consumer body reads are scored separately in the assessment.

This establishes manual native compaction and file-based session handoff on
these cases. It does not establish automatic context-pressure compaction,
automatic checkpoint creation, lossless recovery or cross-machine behavior.
The producer was explicitly asked to save a record; no universal hook exists.

The real-source input is `scripts/check-links.mjs` from published repository
commit `11d246336ef70826ef286613e154ec5deb308807`, isolated with its license and
minimal task documentation. Subjects extended local directory-link handling
and used standard-library tests. Their feature changes remain evaluation
artifacts and were not merged into the product's checker. This is a real-source
slice, not a full external project, deployment or production integration.

## Independent checks and audit material

[Reviewer checks](reviewer-checks.json) group identical retry/snapshot source
and tests by hash before replay: sufficient coverage passes 2/2, the candidate
snapshot passes 1/1, and the deliberately changed recovery source correctly
produces 1 pass / 1 fail. The latter is an expected failure, not a product pass.
Each distinct generated checker/test pair was reviewed and replayed in a
separate work-local copy. Seven independent probes per version verify file,
README-directory and index-directory acceptance; empty directory, directory
masquerading as README and missing-file rejection; and fenced-link exclusion.
Replay scripts did not modify subject artifacts or HEADs.

The [assessment](review-assessment.json), [execution index](index.json),
[input manifests](input-manifests.json) and [hash manifest](export-manifest.json)
separate loading, behavior, scope, exact revisions and prepared-but-unrun inputs.
Exports retain observable task text, commands, relevant results and changes.
Unrelated private instruction bodies, names and paths are withheld or anonymized;
mixed instruction outputs retain fingerprints and an exact target-body-match
receipt. Reasoning and encrypted/compacted payloads were never collected.
Raw local observations are not published. This is a sanitized audit record,
not a claim of fully unredacted transcripts. Frozen Skills retain original bytes.

The archived client/preparer text and preparation supplement document this
Windows setup; they require adaptation to reproduce elsewhere and are not a
portable supported runner or Skill dependency. Official protocol references:
[Codex skills](https://developers.openai.com/codex/skills/) and
[Codex app-server](https://developers.openai.com/codex/app-server/).

Claude Code and Copilot models were unavailable to the user. Neither host was
run and no substitute model was used. Other-host behavior, live research on
V12, automatic context-pressure recovery, production integration and performance
remain untested. The historical V10 sixteen-case explicit core set was not
fully rerun on V12; its original pass cannot be relabeled as current coverage.
