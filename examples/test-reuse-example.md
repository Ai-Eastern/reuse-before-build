# Reuse the existing test suite

This example points to a runnable synthetic project, not a production claim.

The [retry helper](../evals/fixtures/retry-service/src/retry.mjs) already enforces
an attempt limit and propagates the last error. Its [test suite](../evals/fixtures/retry-service/test/retry.test.mjs)
covers immediate success and success on the third attempt. It does not yet
assert final-error identity or invalid attempt counts.

Ask an agent to cover those missing boundaries while keeping production
behavior unchanged. A useful result extends the current Node test file and
uses its assertion library; it does not install another runner or rewrite
the retry implementation.

From the fixture directory:

```sh
node --test
```

The baseline has two tests. That count does not prove the new boundaries are
covered: inspect the new assertions and the newly executed result. See
[scenario 03](../evals/scenarios/03-test-borrow.md) and the
[evaluation instructions](../evals/README.md) for an isolated run. Actual
validation evidence and its limits are recorded in [validation](../docs/validation.md).
