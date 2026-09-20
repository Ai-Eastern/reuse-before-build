# reuse-before-build

**Help your coding agent reuse working code, useful tests, and past engineering decisions before starting over.**

An Agent Skill that checks what already exists, weighs the evidence, and chooses **Take**, **Borrow**, or **Build**. When evidence or permission is missing, it names the gap. After a handoff or context compaction, it reconnects earlier decisions and verification to the current code.

**One self-contained `SKILL.md`. No service or runtime dependency.**

[中文](README.zh-CN.md) · [Quick start](#quick-start) · [Examples](#examples) · [Compatibility](docs/compatibility.md) · [Validation](docs/validation.md)

> **Development preview:** this checkout contains unpublished changes. Installing from GitHub currently retrieves the older public `main`, not this revision. Use the local checkout instructions below to preview these changes.

## What it helps with

| Your task | What the skill looks for |
| --- | --- |
| Add a feature | Existing modules, extension points, official solutions, and suitable libraries |
| Add or fix tests | Existing fixtures, helpers, assertions, regression cases, and test commands |
| Continue unfinished work | Relevant decisions, source references, and previous validation records; what has changed since they were recorded |

A past passing test is evidence about an earlier state. The skill checks whether it still applies and reruns the relevant check when needed. Recovery stays within the current project's engineering work.

A recorded run on the small synthetic fixture produced this result:

```text
Task: cover retry failure boundaries.
Decision: Borrow the existing test suite.
Change: add 2 cases; production code unchanged.
Verification: 4 tests passed.
```

Inspect the [actual diff and replay evidence](docs/validation.md#inspect-the-behavior-evidence). This is one bounded evaluation, not a general success-rate claim.

## Quick start

### Preview this checkout

Obtain the complete revised checkout. Open a terminal in a **separate project** where you want to use it, replace the source path below with the checkout's absolute path, and run:

```bash
npx skills@1.7.0 add "<absolute-path-to-revised-checkout>" --skill reuse-before-build --agent codex --copy -y
```

This installs into the current project. Do not run `add .` from the skill source repository: the installer can skip a copy when its destination is inside its source. See [local installation details](docs/compatibility.md#optional-installer).

The optional installer requires **Node.js >=22.20.0**; installation was checked in an isolated Windows environment with Node.js 24.18.0. Using the skill itself does not require Node.js. See [installation evidence and limits](docs/validation.md).

For the **currently published version**, run this from your target project:

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

For Claude Code, Copilot, Cursor, Gemini CLI, OpenCode, and Windsurf, see [host-specific paths and verification status](docs/compatibility.md). Prefer a project installation when trying the skill.

### Without Node.js

The agent only needs `SKILL.md`; keep `LICENSE` beside it when redistributing. From your target project, these commands create a Codex project installation. Replace the example source path with your revised checkout's location.

**PowerShell**

```powershell
$skillSource = 'C:\path\to\reuse-before-build'
$skillDir = Join-Path (Get-Location) '.agents/skills/reuse-before-build'
New-Item -ItemType Directory -Force -Path $skillDir | Out-Null
Copy-Item -LiteralPath (Join-Path $skillSource 'SKILL.md'), (Join-Path $skillSource 'LICENSE') -Destination $skillDir
```

**POSIX shell**

```sh
skill_source=/path/to/reuse-before-build
mkdir -p .agents/skills/reuse-before-build
cp "$skill_source/SKILL.md" "$skill_source/LICENSE" .agents/skills/reuse-before-build/
```

Examples, templates, and evaluation assets are optional; the skill does not need them to operate. See [manual installation and updates](docs/compatibility.md#manual-installation).

### Try it

Open the target project in your agent, explicitly select or mention `reuse-before-build`, and send:

```text
Use reuse-before-build for this task: add retry support to the existing HTTP client.
First inspect the implementation, related tests, and relevant decision or
validation records. Identify what can be reused and what needs fresh evidence.
Return your reuse decision and the smallest next step before changing files.
```

Replace the task with something relevant to your repository. A useful result cites actual files or sources, explains the choice, and identifies a focused verification step. Merely printing `Take` or `Build` does not demonstrate that the skill worked. If it does not load, follow the [discovery checks](docs/compatibility.md#troubleshooting).

Want a small practice project? Use the included [retry-service fixture](evals/fixtures/retry-service/README.md) and [prepare an isolated scenario](evals/README.md) for test reuse or task resumption. Its optional checks use Node.js and Git; they are not required to use the skill.

## What you get

| Decision | Meaning |
| --- | --- |
| **Take** | Use an existing implementation or test asset directly |
| **Borrow** | Adapt a useful pattern, with a clear adaptation boundary |
| **Build** | Implement the smallest justified solution after checking reasonable reuse options |
| **Blocked** | A fact needed for this decision is missing or contradictory |
| **Needs human approval** | A known risk requires authority the agent does not have |

Search starts locally and expands only as the task needs. Small edits stay lightweight. Existing project records provide continuity; their claims must be checked against the current code and environment. The skill uses your agent's available file, search, and test tools.

## Examples

These are **illustrative scenarios**, not claims that the described systems or tests were run:

- [Reuse an existing HTTP client](examples/take-example.md)
- [Extend a local queue and its tests](examples/borrow-example.md)
- [Build a missing domain predicate](examples/build-example.md)
- [Handle missing evidence](examples/blocked-example.md)
- [Identify approval-required risk](examples/needs-approval-example.md)

These two guides point to the runnable fixture and recorded evaluations:

- [Reuse test assets](examples/test-reuse-example.md)
- [Resume from engineering records](examples/resume-example.md)

For runnable checks, observed results, and their limits, use the [validation guide](docs/validation.md). Host documentation, successful installation, and successful agent behavior are recorded separately.

## Scope and limits

This is an instruction-based workflow: compliance depends on the host and model. It does not add tools, enforce a runtime policy, or guarantee lower cost. External research needs whatever network or search access your agent normally uses. Evidence checks do not replace security or legal review.

The skill reuses and restores task-relevant engineering information. It does not index unrelated conversations or manage a global memory store. It preserves the user's task and existing authorization; installing it grants no additional permissions.

## Contributing and license

Useful contributions include reproducible decision failures, installation fixes, and host validation records. Include the skill revision, host and model versions, operating system, task, expected behavior, and a sanitized result. Keep the core skill self-contained and host-neutral; provide evidence for compatibility claims.

[MIT](LICENSE). Preserve the copyright and license notice when redistributing.
