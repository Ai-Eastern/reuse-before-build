# Borrow: extend a local queue test

Illustrative scenario, not a test receipt. The files below are hypothetical.

**Request:** add delayed execution to an existing durable queue.

## Reuse Decision

- **Decision:** Borrow.
- **Scope:** extend the local queue and its tests.
- **Evidence:** inspect `src/jobs/queue.ts::claimDue`, `test/jobs/queue.test.ts`, and the existing fake-clock fixture. In this scenario the local implementation supports persistence and acknowledgements but does not yet filter jobs by their due time. Verify the local code's license scope before reuse.
- **Compatibility:** delayed execution needs explicit due-time behavior; retry and acknowledgement tests alone do not establish it.
- **Reuse boundary:** retain the existing persistence, runner, fixtures, and retry tests. Extend the due-time predicate and its focused tests. No external package is selected or added.
- **Tests:** add cases for before the due time, exactly at the due time, and persistence across restart. Retain existing retry and duplicate-delivery coverage.
- **Verification:** planned; this document does not claim those tests have run.
- **Next:** make the smallest change within the existing queue and execute the relevant suite.

If the inspected queue cannot provide the required persistence or time semantics, revisit the decision. If an external dependency becomes necessary, verify its actual version and license before adopting it.
