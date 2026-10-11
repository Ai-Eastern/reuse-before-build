# Inspecting external candidates

Read this before naming an external project, package, or service as Take or Borrow. The aim is a choice you could defend to the person who will install it, ship it, and live with its license.

## Discover

- Search with the requirements and constraints (runtime, datastore, deployment, license needs, offline or self-hosted), not just the product category.
- Screen at most 3 candidates; go to 5 only for a stated reason. Merge forks, mirrors, and renamed packages.
- Treat results as leads. Stars, downloads, and popularity do not establish fit.

## Inspect at a pinned revision

For the 1–2 strongest candidates:

1. Resolve a release tag or commit.
2. At that revision, open the manifest (for example `package.json`, `pyproject.toml`, `go.mod`), the license file, the implementation of the behavior you need, and a test or real call site that exercises it.
3. Read what comes back. A URL, page title, HTTP 200, line count, or summary is not inspection; if the body did not come back, that check is still missing. Try one authoritative alternative (a raw file URL, the registry tarball, versioned docs) before giving up.

Keep everything on one revision. If the decision spans two repositories or releases (a wrapper and its core, a plugin and its host), find an authoritative link between them, such as a version pin, lockfile, submodule, or build record. Matching tag names alone do not establish it.

For a closed-source service, use its versioned API documentation, official contract and examples, and terms. Mark implementation evidence as unavailable instead of inferring it.

## Fill in the receipt

Fill it from content you actually read. Write `missing` for anything you did not read; never put "verified" or a future task in a field.

```text
Artifact:       repository or package + release or commit inspected
Compatibility:  manifest path + field and value (engines, peer dependencies, platforms) + fit to this task
Behavior:       implementation path + symbol + what it does and its limits
Corroboration:  test or call-site path + the behavior and mode it actually exercises
Rights:         license path + the grant and obligations relevant to how you will use it
```

Phrase what you saw narrowly. `"license": "MIT"` in a manifest supports "the manifest declares MIT", not "the license terms were reviewed"; the terms need the license text itself.

Corroboration has to exercise the behavior you are selecting:

- A test that swaps the backend, mocks the store, or sets a feature flag covers that path only. Trace its setup and helpers before relying on it.
- A related variant is not the requested behavior: a large-input test may not exercise large intermediate state, and at-least-once delivery is not exactly-once.
- Feature prose and test filenames are not corroboration. A versioned, executable documentation example can be.

## Check each decisive capability

For each capability the decision depends on, write one line:

`requirement and limiting condition → revision + symbol or assertion inspected → supported / missing`

Check decisive capabilities only, not every internal function, and do not demand an end-to-end runtime test for a static design decision. Unversioned "latest" documentation does not tie a capability to the release you inspected.

## Decide

- **Take or Borrow** only when every applicable receipt field holds inspected evidence and the constraints fit.
- Otherwise the candidate is **unverified**. List it with what is missing, and do the missing inspection if it fits the research bound. If the evidence is unavailable, mark adopting that candidate **Blocked** and name the missing fact.
- Missing evidence is not grounds for Build. A separate Build decision needs its own scope and reasons, and an unchecked candidate cannot come back as Take or Borrow under a broader "pattern" label.
- Design-only requests still need these static checks before a component is shown as chosen. Installation and runtime integration tests can stay planned.
- Borrowing an idea or a general technique differs from copying code. Name exactly what you take, and check rights for any copied material.

Before delivering, reread the architecture and the summary: every component presented as chosen has a complete receipt, and everything else is labeled as a candidate.

## When sources fail

- A failed fetch is missing evidence, not evidence of absence or of a defect.
- Try one relevant authoritative alternative instead of retrying the same source.
- A failed optional lookup does not undo a path that local evidence already supports.
- If a required step is interrupted before you have enough evidence, report `Interrupted — no final decision`.
- Respect offline or local-only instructions, and record the search scope you actually covered, for example "3 candidates screened; 1 inspected at v4.2.0".
