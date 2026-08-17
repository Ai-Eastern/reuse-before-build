# Blocked example: missing evidence

## Reuse Decision

Decision: Blocked

### Evidence

- Project search: No local implementation of the requested image-processing adapter was found.
- GitHub / official search: A candidate repository was found, but its source page and release metadata could not be fetched.
- License: No authoritative license file was available. The repository hosting page alone is not license evidence.
- Maintenance: Latest commit date could not be verified.
- Compatibility: The candidate's supported runtime and API could not be verified.
- Verification: No code was downloaded or executed.

### Rationale

The candidate may be useful, but the missing provenance, license, maintenance, and compatibility evidence prevents a safe Take or Borrow decision. Build is also premature because the external search was not completed successfully.

### Next step

Retry the authoritative source and package metadata in a network-enabled session. Do not begin implementation until the missing facts are verified or the user explicitly rules out external reuse.
