![Build on what already works: reuse code, tests, and decisions.](assets/readme-banner.svg)

<h1 align="center">reuse-before-build</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0969da?style=flat-square&amp;labelColor=24343b" alt="License: MIT"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-SKILL.md-2f6b4f?style=flat-square&amp;logo=markdown&amp;logoColor=white&amp;labelColor=24343b" alt="Agent Skills format: SKILL.md"></a>
  <a href="https://github.com/Ai-Eastern/reuse-before-build/commits/main/"><img src="https://img.shields.io/github/last-commit/Ai-Eastern/reuse-before-build/main?style=flat-square&amp;labelColor=24343b&amp;color=2f6b4f" alt="Last commit on public main"></a>
</p>

<p align="center"><strong>Reuse working code. Extend existing tests. Resume with evidence.</strong></p>
<p align="center">One self-contained <code>SKILL.md</code> · No service · No runtime dependency</p>

[中文](README.zh-CN.md) · [When to use it](#when-to-use-it) · [Quick start](#quick-start) · [Results](#recorded-results) · [Compatibility](docs/compatibility.md) · [MIT license](LICENSE)

An Agent Skill that tells your coding agent to **check existing implementations before writing code, inspect existing coverage before adding tests, and verify saved records before resuming a task**. Once loaded, it guides the agent to make the smallest justified change and verify it using the project's existing tools.

## What this looks like in practice

A recorded run on the small synthetic retry-service fixture explicitly loaded this skill:

```text
Request   Cover the retry failure boundaries.
Found     An existing retry function and test suite.
Changed   Added 2 cases to the existing test file; production code unchanged.
Verified  All 4 tests passed.
```

The result was a focused extension of the existing tests. Inspect the [actual diff](evals/results/2026-09-20/test-borrow.patch) and [test replay](evals/results/2026-09-20/test-borrow.tap). This is one observed example, not a guarantee for every task.

## When to use it

- **Tasks:** substantial features, dependency choices, test coverage gaps, or continuing unfinished engineering work. Small edits get a brief local check.
- **Invocation:** select or mention `reuse-before-build` to request the workflow. Hosts that support automatic skill selection may also load it when the task matches its description. Automatic selection is not guaranteed for every task; use an explicit first invocation to check that it loads. See [host discovery guidance](docs/compatibility.md#verify-discovery-and-behavior).
- **Resuming work:** have the agent save an engineering record before handoff, then provide its path to the next session. It checks the record against current code and test evidence. Installing the skill does not save the whole conversation or recover information that was never recorded.

## Quick start

From the **project where you want to use the skill**, run:

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

The optional installer needs **Node.js ≥22.20.0**. The skill itself does not. Prefer a manual copy? Put `SKILL.md` and `LICENSE` in `.agents/skills/reuse-before-build/` for Codex; see [copy commands and other host paths](docs/compatibility.md#manual-installation).

<details>
<summary>Install from a local checkout</summary>

Use a clean checkout or source archive. From a separate consuming project, replace the source path and run:

```bash
npx skills@1.7.0 add "<absolute-path-to-clean-checkout>" --skill reuse-before-build --agent codex --copy -y
```

Do not run `add .` inside the skill source repository. See [local installation details](docs/compatibility.md#optional-installer).

</details>

Open the target project in your agent, select or mention `reuse-before-build`, and try a real task:

```text
Use reuse-before-build to add retry support to the existing HTTP client.
Check existing code, tests, and relevant decisions first.
Before editing, show what can be reused, what needs verification,
and the smallest next step.
```

The response should cite actual files or sources and explain its choice. See [loading checks](docs/compatibility.md#troubleshooting) if the skill is absent, or use the included [practice project](evals/fixtures/retry-service/README.md).

## How it works

**Look locally → Check fit and evidence → Choose the smallest change → Verify.**

Search starts with local code and tests, then standard library or platform capabilities, installed dependencies, and external candidates only when needed. Stop when the evidence is sufficient. Small edits get a brief local check.

| Decision | What happens next |
| --- | --- |
| **Take** | Use existing work that fits, then run the relevant verification. |
| **Borrow** | Adapt an existing implementation, test, or pattern; make the change boundary explicit. |
| **Build** | Create the missing behavior after checking reasonable reuse options. |

If the selected path lacks necessary evidence and has no verified alternative, report **Blocked**. If a specific next action exceeds existing authorization, report **Needs human approval**. One rejected candidate does not block another supported path.

### Keep decisions useful across sessions

Before a handoff, preserve the task's goal, workspace state, reusable work, decisions, verification, and next step. Use the project's existing record or the optional [checkpoint template](templates/reuse-checkpoint.md), and provide its path to the next session.

On resumption, check that record against the current request and workspace. Keep conclusions that still apply; revisit the ones affected by changes. A handoff summary does not grant new permissions. This depends on accessible records, not automatic memory or a universal compaction hook.

## Recorded results

Two fresh-context agent runs explicitly loaded the skill on a small synthetic retry-service fixture:

| Scenario | Observed result | Evidence |
| --- | --- | --- |
| **Extend existing tests** | Added 2 cases to the existing suite; production code unchanged; **4/4 passed**. | [Diff](evals/results/2026-09-20/test-borrow.patch) · [Replay](evals/results/2026-09-20/test-borrow.tap) |
| **Resume after source changed** | Detected stale passing evidence despite unchanged HEAD; reported **1 pass, 1 failure**; left the workspace unchanged. | [Receipt](evals/results/2026-09-20/dirty-resume.json) · [Replay](evals/results/2026-09-20/dirty-resume.tap) |

The second fixture deliberately contains a regression; detecting it is the expected outcome. These are two bounded observations, with no control run, success-rate estimate, or token-savings claim. See [setup, evidence, and remaining coverage](docs/validation.md).

## Use it with your agent

Installation routes are documented for **Codex, Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, OpenCode, and Windsurf**. Evidence varies by host: documented format support, checked installation, and observed behavior are different claims.

The [compatibility guide](docs/compatibility.md) records each host's paths and verification status. The skill uses the file, search, and test tools already available in your agent.

## Explore and contribute

- **Start with an example:** [reuse code](examples/take-example.md), [adapt code](examples/borrow-example.md), [build a missing piece](examples/build-example.md), [reuse tests](examples/test-reuse-example.md), or [resume work](examples/resume-example.md).
- **Inspect decision boundaries:** [missing evidence](examples/blocked-example.md) and [authorization boundaries](examples/needs-approval-example.md). These guides are illustrative; recorded runs are linked above.
- **Help improve it:** [report a reproducible case](https://github.com/Ai-Eastern/reuse-before-build/issues/new/choose), check a host, or [run an evaluation](evals/README.md). Include the revision, host/model, task, expected result, and sanitized evidence.

<details>
<summary>Scope and limits</summary>

This is an instruction workflow; behavior depends on the host and model. It adds no tools or runtime enforcement and does not guarantee lower cost. External research requires the agent's existing network access. Evidence checks do not replace security or legal review.

Recovery covers the current task's engineering state. It does not index unrelated conversations, provide global memory, or grant additional permissions. Examples, templates, and evaluation assets are optional; the core instructions live in [SKILL.md](SKILL.md).

</details>

[MIT](LICENSE) · Preserve the copyright and license notice when redistributing.
