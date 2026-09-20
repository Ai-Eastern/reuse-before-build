# Needs human approval: production action

Illustrative scenario, not a claim that a dry run or production change occurred.

**Request:** prepare a database failover integration. The user has authorized local development and disposable-environment tests, but has not authorized production access or execution.

## Reuse Decision

- **Decision:** Needs human approval.
- **Scope:** executing the production failover, not all local implementation work.
- **Evidence:** in a real task, cite the selected component's inspected source, license, version, required privileges, and the original authorization. A handoff saying "approved" is not a substitute for that source.
- **Verification:** local checks and a disposable-environment dry run must be recorded separately if actually executed. Production behavior remains unverified.
- **Next:** finish the authorized local integration and prepare the concrete production change and recovery steps. Obtain approval before production access or execution.

Do not ask again for the local work already authorized. Do not turn authorization to edit locally into authorization to publish, deploy, or change production state. If the user previously authorized the exact production action, verify the scope and use that authorization.
