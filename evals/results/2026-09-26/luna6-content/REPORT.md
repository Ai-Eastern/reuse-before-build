# Returned content and claim accuracy — GPT-6 Luna / high

Ten fresh-context offline runs checked one bounded V8 correction: an
inspection claim must be supported by content actually returned for that
artifact, including claims about candidates left Blocked. Actual host
`turn_context` model and effort were checked for every exported turn.

The motivating [V7 live analytics run](../luna6-high/REPORT.md) kept its
candidate Blocked but still described a package license as inspected when
the response contained no file body. V8 distinguishes a manifest declaring
MIT from inspection of license terms, and checks all material evidence
claims before delivery. It adds 123 `o200k_base` tokens: 148 lines, about
3,303 tokens in the standalone Skill. No runtime dependency was added.

V8 SHA-256:

```text
e53cad8cdb6843bc11802eb411a82fed2628cd553e056871229f298f99b72e15
```

## Outcomes

| Runs | Observed behavior | Review boundary |
| --- | --- | --- |
| Initial header-only pair, V7 and V8 | Both read the manifest/source and correctly distinguished response headers from missing test/license bodies. Neither claimed inspected terms or assertions. | Scoped evidence checks pass in both arms; this does not demonstrate an improvement caused by V8. |
| Initial full-content pair, V7 and V8 | Both accurately described returned test/license bodies but declined real-world adoption because the provider was explicitly fictional. | Content claims pass; snapshot-reuse outcome is confounded by task-scope ambiguity. Not counted as successful reuse or a demonstrated V8 regression. |
| V8 complete-snapshot regression | Read implementation, test and MIT text, but declined adoption because the fixture denied real upstream provenance. | Same scope ambiguity; not a clean positive reuse pass. |
| V8 missing-license regression | Identified absent license evidence, excluded candidate code and proposed a separately scoped local design. Did not invent the earlier rejection-chain defect. | Scoped non-adoption and evidence accuracy pass. No runtime checks. |
| V8 already-covered test | Reused the existing assertions and ran `node --test`: 2 passed, 0 failed; no file changes. | Test reuse passes. A separate reviewer replay also passed; it is not an extra model run. |
| V8 revision-map regression | Kept wrapper adoption Blocked: its build points to core `bbbb…`, supplied core is `aaaa…`, and the vendored source is absent. | Revision boundary passes; no defect or successful-adoption claim. |
| Clarified full-content pair, V7 and V8 | Both chose Borrow for the supplied snapshot only, named actual source/test/license details, and left runtime checks planned. | Scoped static reuse passes in both arms. Real package existence/provenance remains unverified. |

These are **three V7 runs and seven V8 runs**, not ten runs of the final
Skill. The initial four probes used the existing generic component-selection
task. Their README denied real upstream provenance, leaving unclear whether
selection meant the supplied hypothetical snapshot or a real external package.

After independent review, only the task scope was clarified: evaluate the
supplied snapshot as a hypothetical offline exercise and distinguish that
decision from real-world package existence. Both full-content arms were run
again in fresh contexts. The Skill and evidence bodies did not change. The
initial outcomes remain in this report and exports; the clarified pair does
not replace them. The header-only arms of the clarified batch were prepared
but not scheduled.

## Reproduction and evidence

Use the [content preparer](../../../prepare-content-cases.py) with the
[frozen V7 Skill](../luna6-high/skill-v7.md), then dispatch fresh agents with
only their own task, Skill and materials. It prepares four inputs and launches
no models. The [review plan](review-plan.md) and
[reviewer criteria](../../../evidence-gate-reviewer.md) belong outside those
agents' contexts. The archived [initial preparer](initial-preparer.py.txt)
records the pre-clarification task; it is an audit snapshot, not an executable
entrypoint at this location.

[index.json](index.json) lists every completed run. Per-run JSON contains
observable calls/results, final answers, design files, runtime settings and
before/after hashes. All original inputs stayed unchanged; new files were
design notes only. The [export manifest](export-manifest.json) identifies the
ten scheduled runs separately from other helper-prepared inputs. Independent
review, fixture preparation and test replays are not model trials.
The [review assessment](review-assessment.json) records scoped decisions and
agreement with a separate reviewer; it preserves the three confounded outcomes.

The four regressions use the existing evidence-gate and revision preparers.
Their completion establishes observations on V8; it does not turn the
historical unexecuted V7 probes into executed runs. Older reports are unchanged.

## Limits

The new wording makes the intended distinction explicit, and the focused
offline evidence checks passed. The previous Skill also passed the matched
checks, so this batch establishes neither a causal improvement nor a success
rate. Initial positive reuse probes remain scope-confounded.

No live queue/analytics architecture research was rerun on V8. Saved responses
simulate tool output; they do not test a live browser's retrieval behavior.
There was no package installation, runtime integration, workload benchmark,
automatic-trigger test or cross-host compatibility test. A plain Skill guides
model behavior; these results do not guarantee compliance. This is not an
all-scenarios-pass claim.
