# Borrow example: job queue adapter

## Request

“Add delayed background jobs using a durable queue.”

## Reuse Decision

Decision: Borrow

### Evidence

- Project search: no durable queue implementation; an internal `JobHandler` interface can be reused.
- GitHub / official search: the official Redis Streams consumer-group pattern matches delivery and retry needs, but its deployment and message schema do not match this service.
- License: the referenced documentation and client library have an acceptable license for evaluation; confirm the selected package before adding it.
- Maintenance: official documentation and the candidate client show current maintenance signals.
- Compatibility: local deployment uses Redis, but the service requires its own idempotency key and tracing conventions.
- Verification: a local integration test must cover retry, acknowledgement, and duplicate delivery.

### Rationale

Borrow the consumer-group workflow and failure semantics, not a repository’s application code. Adapt storage names, message schema, observability, and idempotency to local conventions.

### Next step

Confirm the package license and version, write the adapter behind `JobHandler`, and verify the three failure cases before rollout.
