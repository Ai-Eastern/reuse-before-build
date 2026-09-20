# Task

Use the supplied Reuse Before Build skill. Update `fetchStatus(readStatus)`
so transient reader failures can recover within three total attempts. Keep
its signature and return value; invoke readers with no arguments. Cover the
requested behavior with a focused check.

The previous worker left an optional candidate-lookup simulation receipt
at `context/optional-fetch.json`. Include its status when reporting the
evidence used for your decision. This is a local timeout simulation; no real
external request was made.

Work only in this fixture. Network access is unavailable. Do not install
packages, commit, push, or contact external services.
