# External-candidate inspection — GPT-5.6 Luna / medium

Recorded 2026-09-26, Asia/Shanghai. **11 completed model runs, not 11 passes.**
The final revision elicited real, versioned source and license reads in both
live design tasks. It still did not reliably complete every corroboration
check before recommending a component. This is measured progress, not a
claim that the evidence gate is now reliably enforced.

## What changed and how it was evaluated

The [previous experiment](../../2026-09-21/luna-search-timing/REPORT.md)
found search-only selection even after a provisional-candidate warning.
This experiment tested two narrow changes:

- **V4:** ordered discovery, inspection, evidence checks, then decision;
  design-only scope still requires static source/compatibility/rights checks.
- **V5:** replaced generic `verified` check cells with a concrete receipt:
  inspected revision, metadata field/value, implementation symbol, test or
  call site, and license grant/obligations. Missing facts stay missing.

| Instructions | SHA-256 | Actual runs |
| --- | --- | --- |
| [Previous V3](../../2026-09-21/luna-search-timing/skill-v3.md) | `a77d13420dddd2608d623941983c0b0e7dd5ab8dc9f7e44fa300d14425400534` | Two fresh live-design controls |
| [V4](skill-v4.md) | `55506701d7435b9be4080cb6f053904fd6c47534e273634c91be73294da7b141` | Two paired live designs plus three local regressions |
| [V5, final revision](skill-v5.md) | `62651b60cc1ed43af2d8d8d6aa7a2a58dbbec46a834b56bd1139dc9b3e353f7c` | Four targeted treatment-only follow-ups |

Each run had a fresh context and its own directory. Actual host `turn_context`
events confirm **gpt-5.6-luna / medium** for every recorded turn. Dispatches
and runtime settings are included in each record. Both comparison arms loaded
a full Skill; neither received the reviewer rubric, prior results, or parent
conversation. Shared task inputs were byte-identical within each live pair.
The host still supplied common instructions and a Skill catalog to both arms.
These are instruction-scoped workspaces, not OS sandboxes.

The original queue task uses Node.js 22/PostgreSQL with no Redis. The transfer
task asks for Python 3.12, 20 GB CSV aggregation into Parquet, 2 GB memory,
temporary disk, and no database server. Neither design authorizes installation
or runtime integration. The offline cases use a fictional supplied limiter
snapshot; one includes a license and one does not. Their provenance is
simulated, not evidence about a real provider. Fixture tests ran under the
available Node.js 24.18.0, not the target Node.js 22.

## Initial comparisons and local regressions

| Case | Previous V3 | V4 | Assessment |
| --- | --- | --- | --- |
| Durable queue | [Search-only selection](gate_queue_previous.json) | [Opened official pages and an actual license](gate_queue_current.json), but npm metadata returned 403 and no implementation/revision was inspected | Partial improvement; V4 still selected Borrow prematurely. |
| CSV analytics | [Searched official documentation/license information](gate_analytics_previous.json) | [Similar documentation-led selection](gate_analytics_current.json) | Neither established a fixed source revision with implementation/test evidence before selecting DuckDB. |
| Complete offline snapshot | No control | [Read manifest, code, test, license; 1 test passed](gate_snapshot_a.json) | Bounded reuse of the supplied fixture was supported; real upstream adoption remained unverified. |
| Offline snapshot without license | No control | [Identified missing rights and withheld dependency adoption](gate_snapshot_b.json) | Correctly avoided adopting the artifact; a separate local Build proposal must be assessed on its own grounds. |
| Already-covered retry behavior | No control | [Existing assertions reused; no files changed; 2 tests passed](gate_covered.json) | The lightweight local path was preserved in V4. This case was not rerun on V5. |

V4's queue response marked evidence `verified` while leaving the exact release
and implementation inspection unfinished. That observation motivated the V5
receipt fields; the V4 failures remain in the record.

## V5 follow-ups: progress and remaining gaps

**[Durable queue](gate_queue_v5.json): actual versioned inspection.** The run
retrieved Graphile Worker `v0.18.0/package.json`, `LICENSE.md`,
`src/sql/getJobs.ts`, and `src/sql/failJobs.ts`. These returned real contents,
unlike earlier guessed paths that returned 404. The design recorded a
conditional Node patch-version requirement and left runtime integration
planned. However, it used general task/runner documentation for corroboration
rather than reading a versioned test or independent call site. Broader recovery
claims were not fully tied to the inspected code. The complete receipt gate
therefore remains only partially satisfied.

**[CSV analytics](gate_analytics_v5.json): actual source/license inspection,
incomplete revision linkage.** The run read DuckDB `v1.4.1` license and
`physical_hash_aggregate.cpp`. Its test-directory lookup returned no usable
test contents. Python compatibility came from a separate Python-binding
repository commit, without establishing its relationship to the selected
core release. It still selected Borrow. RSS, spill, throughput, wheel support,
and the real workload remained planned checks; they were not measured.

**[Complete offline snapshot](gate_snapshot_a_v5.json): bounded positive
case.** Manifest, implementation, rejection-progress test, and license were
read; the supplied test passed. The model distinguished the licensed fixture
from a verified real production dependency and left Node 22 execution planned.
This shows the new workflow need not block all reuse when evidence is available.

**[Offline snapshot without license](gate_snapshot_b_v5.json): adoption
blocked, scope wording still needs care.** The receipt explicitly recorded
missing rights and blocked dependency adoption/copying. It separately proposed
Borrow for the conceptual scheduling pattern and Build for a local implementation.
That is not evidence of permission to reuse the candidate's code or tests.
The mixed labels make the reuse scope less clear than it should be; no legal
conclusion or successful candidate adoption is claimed here.

V5 has no fresh controls. These four targeted follow-ups were selected after
V4 results; they do not constitute a full rerun or an unbiased success rate.
No further wording changes were silently tested until a passing result appeared.

## Evidence and review boundary

- [Run index](index.json), [V4 prepared inputs](v4-prepared-inputs.json), and
  [V5 prepared inputs](v5-prepared-inputs.json) separate preparation from
  execution. Each batch prepares seven inputs; only eleven agents ran across
  the two batches. Unused directories do not count as evaluations.
- [Primary-open receipts](inspection-receipts.json) retain requested references,
  returned-line counts, failures, and content hashes. A returned directory page
  or a URL in prose is not a source/test inspection. A failed request is not
  a successful read. V5 queue also had two JavaScript syntax failures, which
  were corrected before subsequent calls; failed calls are preserved.
- A separate read-only Luna review compared observable actions, returned
  contents, and final recommendations with the [reviewer criteria](../../../evidence-gate-reviewer.md).
  The reviewer agreed that V5 materially improved source/license inspection
  while complete corroboration remained unreliable. Review is not another
  measured model trial.
- Exported records exclude private reasoning and system/developer messages.
  Local workspace paths are normalized, host tool-catalog descriptions and
  remote page bodies are omitted, and export files use LF. Metadata, tool
  requests, result hashes, changed files, and final answers remain. See
  [export transformations and file hashes](export-manifest.json). The private
  working review copy of public page outputs is not included in the repository.
- Host tool telemetry is not a network packet audit. No installation,
  production integration, or performance benchmark was performed. A passing
  fixture test does not make the external design gate pass.
- Live search results vary. The repeated task, shared host catalog, targeted
  follow-ups, and tiny sample prevent causal or success-rate claims. Automatic
  Skill triggering, other hosts/models, closed-source services, and real
  context compaction were not evaluated in this batch.

To reproduce, use the [preparation instructions](../../../README.md), keep
review criteria away from the evaluated model, pin the Skill hash and actual
model settings, and save results in a new dated directory. Preserve incomplete
receipts and incorrect final selections rather than grading by formatting alone.
