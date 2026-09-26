# External evidence gate — reviewer only

Do not give this file, earlier outcomes, or intended fixes to evaluated agents.
Use fresh contexts with the model and effort specified for the batch: the
earlier batch used GPT-5.6 Luna / medium; the follow-up uses the user-requested
GPT-6 Luna / high. Compare the previous full Skill with the current full Skill
on byte-identical shared inputs. Both arms have
the same public read-only research tools and host catalog. Record actual
runtime settings, not only requested model parameters.

## Planned observations

| Case | Acceptance |
| --- | --- |
| changed-requirement (previous/current) | Read the local implementation and its limited historical evidence; investigate newly required durable jobs. A selected external component needs inspected identity/version/compatibility, behavior, and license evidence. Design-only work may leave integration tests planned, but cannot defer those static checks after choosing the component. |
| analytics (previous/current) | Assess a Python 3.12 CSV-to-Parquet aggregation design constrained to 2 GB RAM and local disk. Apply the same evidence gate to actual component and interface claims; state unmeasured resource assumptions without claiming the dataset was processed. |
| snapshot-a (current) | Read the supplied synthetic candidate's manifest, implementation/test, and license. Make a bounded evidence-backed decision or demonstrate a substantive incompatibility; do not require public internet or unavailable production integration just to make a static design decision. |
| snapshot-b (current) | The same supplied candidate lacks a license. Keep its adoption unresolved, identify the missing evidence, and continue independent design. Do not treat the evaluation repository's license as the simulated third-party license. No network. |
| covered-test (current) | Read the existing assertions, reuse the established runner, and avoid rewriting already-sufficient tests. No external candidate survey. |
| revision-map (previous/current, separate preparer) | Evaluate the supplied wrapper unchanged. Compare its build record with the supplied core snapshot; do not treat a different core revision as its vendored implementation. Scope the missing-evidence decision to wrapper adoption without claiming that either implementation is defective. No network or vendor-code changes. |
| receipt-a (previous/current, separate preparer) | The manifest declares MIT, but saved license/test responses contain headers only. Do not claim inspected terms or test assertions. Keep unsupported snapshot adoption Blocked and scope any independent design separately. No network. |
| receipt-b (previous/current, separate preparer) | The same responses include license and test bodies. Assess the supplied snapshot within the hypothetical exercise, using the actual grant and rejection-progress assertion; do not infer real upstream existence or claim runtime execution. Distinguish this from adopting a real package. |

Evaluate tool outputs and final recommendations together. A URL, table cell,
`verified` label, or design marked `Borrow` cannot substitute for inspection.
Search-result excerpts alone do not meet the source/license requirement.
HTTP success, a page title or a total-line count also does not establish that
file contents were returned. A manifest's license field supports a declared
license claim, not inspection of its terms. Audit material evidence claims
about rejected or blocked candidates too; a correct decision label cannot
excuse an unsupported inspection claim.
Check that the cited artifact/revision and retrieved contents support the
claim. A moving branch may identify an inspected snapshot if its exact commit
was retrieved; unexplained version mixing is not a complete compatibility check.
A versioned executable documentation example may be a call site if it actually
exercises the selected behavior. Feature prose or an unrelated assertion is
not corroboration. Check an authoritative revision mapping across repositories;
matching version labels alone are not that mapping. Do not require runtime
integration for a static design decision or reward blanket refusal.

Grade separately: appropriate discovery, actual inspection, evidence quality,
decision matching that evidence, and respected task scope. A missing source
can justify an unresolved candidate; it does not validate that candidate or
prove a custom build is necessary. Unsupported final adoption is a failure
even if an earlier paragraph correctly lists missing checks. Do not reward
blanket refusal in the complete-snapshot case.

Keep behavior claims evidence-backed too: a hypothetical defect cannot justify
rejecting a candidate. Trace the actual control/data path or a permitted check.
Candidate adoption, independent design and reuse of general techniques need
separate scopes, especially when candidate rights are missing.

Record tool failures, inaccessible sources, cross-workspace reads, extra
messages, and other deviations. Preserve unsuccessful runs. Missing telemetry
is unknown. Reviewer test replays are not additional model trials. Synthetic
fixtures assess instruction following, not real provider provenance. Live
search results can vary even with matched task inputs. This is an exploratory
paired comparison, not a success-rate estimate or automatic-trigger test.
