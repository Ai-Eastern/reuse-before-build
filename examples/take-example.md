# Take: an existing HTTP client

Illustrative scenario, not a test receipt. The paths below describe a hypothetical consuming project.

**Request:** add a retrying request to a service that already has a shared HTTP client.

## Reuse Decision

- **Decision:** Take.
- **Scope:** the retry implementation.
- **Evidence:** inspect `src/infra/http/client.ts::requestWithRetry`, its callers, and the retry assertions in `test/http-client.test.ts`. Confirm the existing retry limit, error policy, and runtime match this endpoint. Inspect the consuming project's license and any file-level notices rather than assuming local code has no restrictions.
- **Search scope:** the shared client and its tests are a direct fit; external discovery is unnecessary.
- **Tests:** reuse the existing runner and retry fixture. Add an endpoint case only if the integration introduces uncovered behavior.
- **Verification:** planned, not executed in this illustrative example.
- **Next:** call the existing client and run the affected tests after any integration change.

Finding a file with the right name is insufficient. The real agent must read the implementation and test assertions before choosing Take.
