# Task

Use the supplied Reuse Before Build skill. Improve checks for two retry
boundaries: when every attempt fails, preserve the exact final error object
and stop at the configured attempt count; when `attempts` is zero, reject
without calling the operation.

Keep the helper's public contract and production source unchanged. Work
only in this fixture. Do not use the network, install packages, commit, or push.
