# Build example: domain-specific policy evaluator

## Request

“Add a policy evaluator for our nested, time-bounded approval rules.”

## Reuse Decision

Decision: Build

### Evidence

- Project search: no policy evaluator, rule AST, or compatible extension point exists.
- GitHub / official search: generic rule engines were reviewed, but none support the required nested approvals and effective-date semantics without replacing core domain behavior.
- License: rejected candidates have no acceptable direct reuse path for this requirement; no third-party code will be copied.
- Maintenance: irrelevant to the final decision because the candidates do not fit the domain semantics.
- Compatibility: generic engines would introduce a second expression language and conflict with the service’s typed domain model.
- Verification: define table-driven tests for precedence, effective dates, missing approvals, and denied access before implementation.

### Rationale

Take is not a fit and Borrow would preserve the wrong semantics while adding an unnecessary dependency. A small typed evaluator is the narrowest justified implementation.

### Next step

Write the domain cases and tests first, then implement the smallest evaluator behind a local interface.
