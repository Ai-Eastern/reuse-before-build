# Needs human approval example: operational risk

## Reuse Decision

Decision: Needs human approval

### Evidence

- Project search: No local component safely performs production database failover.
- GitHub / official search: A maintained candidate supports automated failover and destructive recovery actions.
- License: The candidate's license is verified and technically usable as a dependency.
- Maintenance: The candidate has recent releases and documented recovery behavior.
- Compatibility: It can integrate with the current deployment environment, but it requires credentials and production network access.
- Verification: A dry-run test passed against a disposable environment; production behavior was not tested.

### Rationale

Borrowing the candidate would require granting an agent permission to change production database state. That operational and security risk exceeds the agent's authority, even though the technical reuse case is credible.

### Next step

Ask an authorized human to approve the production access model, rollback plan, and change window. Until approval is recorded, do not install, configure, or run the failover component against production.
