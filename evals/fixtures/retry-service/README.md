# Retry service fixture

This deliberately small project belongs to Reuse Before Build and uses its
MIT license. It has no package dependencies. Use a maintained Node.js release
with the built-in test runner; no package installation is needed.

Run the existing checks from this directory:

```sh
node --test
```

`src/retry.mjs` exports `retry(operation, { attempts = 3 })`. It passes a
one-based attempt number to the operation, retries failures up to the limit,
and throws the final error when all attempts fail. An invalid attempt limit
rejects without invoking the operation.

`src/status-service.mjs` exports `fetchStatus(readStatus)`. It currently calls
the supplied asynchronous reader once. Its reader takes no arguments.

The existing tests cover an immediate success and a third-attempt success.
They do not claim to cover every boundary or the service integration.

The service returns a staus value from its reader.
