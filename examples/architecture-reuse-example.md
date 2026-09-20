# Architecture: discover implementations before choosing boundaries

**Illustrative workflow, not an executed evaluation.** No repository was searched or candidate inspected for this example. It names no selected package and reports no test results. The decisions below are conditional on evidence a real task would need to collect.

## Constrained request

Design durable webhook delivery for a new TypeScript service using PostgreSQL. The design needs scheduled attempts, bounded retries, recovery after worker restart, and tenant-scoped delivery records. Duplicate delivery is possible, so explain idempotency. Avoid adding another datastore. This request authorizes research and design only, not dependency installation or implementation.

## Discover before committing to a stack

1. Check the project's available code, prior decisions, platform capabilities, and dependencies. Reuse a supported fit if one exists. A new project may have no implementation yet; that is a reason to look for relevant implementations, not evidence that the delivery engine must be written from scratch.
2. If a material gap remains and network research is allowed, search GitHub and official repositories for durable job or webhook delivery implementations that fit the runtime and datastore constraints. Screen at most three initial candidates; do not turn the search into a popularity ranking.
3. Deep-read the one or two strongest candidates. Trace how work is persisted, claimed, retried, acknowledged, and recovered. Inspect the actual API and relevant tests. Establish whether guarantees such as at-least-once execution cover this use case; do not infer them from a project description.
4. Check compatibility and integration work: supported runtime and database versions, transaction boundaries, schema ownership, worker lifecycle, deployment needs, and failure visibility. Inspect maintenance evidence, provenance, and the license covering any dependency or code that would be reused.

Record actual source URLs, revisions, relevant symbols or contracts, and inspected test locations in the real decision. This illustration supplies none of those facts. Existing upstream tests are reusable evidence about their covered behavior; they do not prove that the proposed integration works.

## Turn evidence into architecture boundaries

The following is a possible design **if inspection supports each decision**:

| Scope | Conditional decision | Architectural effect |
| --- | --- | --- |
| Durable scheduling, retry state, and worker recovery | **Take** an implementation whose inspected behavior and license meet the constraints. | Put the verified engine behind a small delivery adapter; avoid designing a second persistence and scheduling engine. |
| Adapter or worker lifecycle pattern | **Borrow** only an applicable pattern, with its source and rights checked before copying code. | Adapt the boundary between the selected engine and application behavior without importing an unrelated framework. |
| Tenant-scoped delivery identity and product-specific retry policy | **Build** only the missing behavior after checking what the selected implementation already provides. | Keep product policy in the application layer and pass supported scheduling operations to the engine. |

The resulting proposal would explain why an existing engine can own durable execution while the application owns tenant isolation and delivery policy. If inspection shows a required guarantee is absent or integration is too costly, reject that candidate and revise those boundaries. A library's existence alone does not settle the design.

## Design handoff and verification boundary

Deliver the component boundaries, selected or rejected candidates with their evidence, integration cost, license obligations, and unresolved checks. Keep the implementation step separate from this architecture-only request.

Plan focused checks for the proposed integration: restart recovery, attempt limits, duplicate delivery, and tenant isolation. Reuse the selected implementation's relevant tests or fixtures where applicable and state which application guarantees still need coverage. **These checks are planned, not executed.** Preserve the decision and its open questions in the project's existing design record for the next session.

If existing assets already meet the need, stop without compulsory internet research. If the user prohibits network access, respect that boundary and assess available sources. Missing evidence for an essential candidate stays an open or blocked decision; it is not proof that a custom implementation is necessary.
