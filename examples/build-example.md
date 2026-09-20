# Build: a missing domain predicate

Illustrative scenario, not a test receipt. The paths and user constraint below are hypothetical.

**Request:** implement the project's effective-date rule using local code only; the user explicitly excludes new dependencies and external code reuse for this task.

## Reuse Decision

- **Decision:** Build.
- **Scope:** the missing effective-date predicate, not a new rules framework.
- **Evidence:** inspect `src/policy/approval.ts`, the domain's timestamp type, and `test/policy/approval.test.ts`. In this scenario the existing predicate checks approver identity but has no effective-date rule. The existing date parser is reusable; it does not itself implement the domain rule.
- **Rejected alternatives:** the identity predicate does not evaluate time; the date parser supplies a timestamp but cannot decide approval eligibility. External implementations are excluded by the explicit task constraint, not by a failed search.
- **Tests:** reuse the established test runner and domain fixtures; cover the specified start/end boundary and invalid dates.
- **Verification:** planned, not executed.
- **Next:** add the smallest domain predicate using the existing parser and run the affected tests.

Without that explicit constraint, a non-trivial Build decision still needs a relevant completed search. Do not cite imaginary rule engines or treat a network outage as permission to build.
