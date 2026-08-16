# Take example: repository HTTP client

## Request

“Add retrying HTTP requests to the service.”

## Reuse Decision

Decision: Take

### Evidence

- Project search: `src/infra/http/client.ts` already exposes the required client and `test/http-client.test.ts` covers retries.
- GitHub / official search: not needed; a local implementation is a direct fit.
- License: project license covers the local code.
- Maintenance: maintained with the service.
- Compatibility: already used by the target service and its runtime.
- Verification: extend the existing focused test for the new endpoint.

### Rationale

The project already has the right abstraction and behavior. Adding another HTTP client would duplicate configuration and error handling.

### Next step

Use the existing client, add the smallest endpoint-specific test, and run the focused suite.
