![Build on what already works: reuse code, tests, and decisions.](assets/readme-banner.svg)

<h1 align="center">reuse-before-build</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0969da?style=flat-square&amp;labelColor=24343b" alt="License: MIT"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-SKILL.md-2f6b4f?style=flat-square&amp;logo=markdown&amp;logoColor=white&amp;labelColor=24343b" alt="Agent Skills format: SKILL.md"></a>
  <a href="https://github.com/Ai-Eastern/reuse-before-build/actions/workflows/validate.yml"><img src="https://github.com/Ai-Eastern/reuse-before-build/actions/workflows/validate.yml/badge.svg" alt="Validation status"></a>
</p>

<p align="center"><strong>An Agent Skill that makes your coding agent look for existing code, tests, and libraries to reuse before it writes new ones.</strong></p>
<p align="center">For Claude Code, Codex, and other agents that support Agent Skills · No service · No runtime dependency</p>

[中文](README.zh-CN.md) · [Install](#install) · [Try it](#try-it) · [How it works](#how-it-works) · [Results](#results) · [Compatibility](docs/compatibility.md)

Coding agents tend to write a helper next to one that already exists, add tests that verify nothing new, or recommend a library whose code and license nobody read. This skill puts a short check in front of building: the agent searches your project, the standard library, and your installed dependencies, and looks at GitHub and official sources only when a real gap remains. It then decides to **Take** (use as is), **Borrow** (adapt), or **Build** (write only the missing part), citing what it actually read.

## What changes in practice

Same task and project, run without and with the skill (GPT-5.6 Luna, 2026-09-21; [report](evals/results/2026-09-21/luna-search-timing/REPORT.md)):

```text
Request   Make sure retry returns on the first success without calling the operation again.
          Keep production code unchanged.
Without   Edited the test file to "strengthen" the first-success case: a diff, but no new coverage.
With      Pointed out that the existing assertion seen == [1] already proves a single call,
          changed nothing, and ran the existing tests.
```

## When to use it

- **Good fit:** choosing a library, framework, or architecture; implementing a feature or helper that may already exist; adding or checking tests; picking up work from a handoff.
- **Not needed:** typos, renames, and other small edits. The skill keeps those to a quick local look.
- **How to invoke:** mention `reuse-before-build` in your request. Some agents load it automatically when a task matches; name it explicitly the first time to make sure it loads.

## Install

Copy the [`skills/reuse-before-build`](skills/reuse-before-build/SKILL.md) folder into your agent's skills directory. Keep the whole folder: `SKILL.md` reads files from `references/` when it needs them.

**Claude Code**, for all your projects (to install for one project, copy into that project's `.claude/skills/` instead):

```bash
git clone --depth 1 https://github.com/Ai-Eastern/reuse-before-build.git /tmp/reuse-before-build
```

```bash
cp -R /tmp/reuse-before-build/skills/reuse-before-build ~/.claude/skills/
```

**Codex and other agents**, with the skills CLI (run in your project; needs Node.js ≥22.20.0):

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

Replace `codex` with `claude-code` or another agent name. Paths for GitHub Copilot CLI, Cursor, Gemini CLI, OpenCode, and Windsurf, and Windows commands, are in the [compatibility guide](docs/compatibility.md#manual-installation).

## Try it

```text
Use reuse-before-build to add retry support to the existing HTTP client.
Check existing code, tests, and relevant decisions first.
Before editing, show what can be reused, what needs verification,
and the smallest next step.
```

For architecture planning:

```text
Use reuse-before-build to design durable webhook delivery for a new project.
Check GitHub and official repositories where existing assets leave a gap.
Show what to Take, Borrow, or Build and how that changes the architecture.
Keep this to design; do not install dependencies or implement code.
```

A good answer names the files or sources it actually read before it decides. To practice first, use the bundled [retry-service project](evals/fixtures/retry-service/README.md). If the skill does not load, see [troubleshooting](docs/compatibility.md#troubleshooting).

## How it works

**Find existing work → check that it really fits → choose the smallest scope → verify.**

| Decision | When | What happens next |
| --- | --- | --- |
| **Take** | Existing work already does what is needed | Use it and run the relevant check |
| **Borrow** | Existing code, tests, or a pattern fit with adaptation | Name what is reused and make the smallest change |
| **Build** | Nothing reasonable fits after searching | Build only the missing part and note rejected options |
| **Blocked** | A fact the decision depends on is unavailable | Name the missing fact and keep doing independent work |
| **Needs human approval** | The next step goes beyond what you authorized | Prepare it and ask first |

- **Local first.** It searches outside the project only for a real capability or compatibility gap. A new session, a new file, or a failing test is not a reason to search again.
- **Evidence, not impressions.** Before adopting an outside library, it pins a version and reads the manifest, license, implementation, and a test or call site. Anything it could not read stays labeled *unverified*.
- **Existing tests first.** It reads the current runner and assertions, extends them only for real gaps, and leaves covered behavior alone.
- **Resume with checks.** A handoff note or old test result is a claim to verify against the current workspace, and it cannot grant new permissions.

The full rules are in [`SKILL.md`](skills/reuse-before-build/SKILL.md). Details for inspecting outside libraries and writing checkpoints are in [external-candidates.md](skills/reuse-before-build/references/external-candidates.md) and [checkpoints.md](skills/reuse-before-build/references/checkpoints.md).

## Results

| What was checked | What we saw | Details |
| --- | --- | --- |
| **This version vs. the previous one** — Claude Opus 5.5, 2026-10-11 | 8 scenarios, 17 runs: both versions passed every check, so the shorter rewrite showed no regression. With full evidence, this version still adopted a suitable library instead of blocking. | [Report](evals/results/2026-10-11/claude-restructure/REPORT.md) |
| **With vs. without the skill** — earlier version, GPT-5.6 Luna, 2026-09-21 | 17 runs with no-skill controls. With the skill, the agent left already-sufficient tests alone and wrote an assertion that caught a deliberately wrong implementation. | [Report](evals/results/2026-09-21/luna-search-timing/REPORT.md) |
| **Known weak spot** — checking outside libraries | Earlier versions sometimes recommended a library before reading its source and license: both architecture trials in the row above, and 2 of 3 header-only runs with V12 in the Codex app (the no-skill control also did in 2 of 3). On Claude, this version kept such a library unverified; it has not been retested on Codex. | [Report](evals/results/2026-09-26/native-host/REPORT.md) |

Each row is a small sample on one model, not a success rate. Earlier development rounds (V10–V13 on Codex), methods, and file hashes are in [validation](docs/validation.md).

## Use it with other skills

When paired with a simplification skill such as ponytail, the agent shares one reuse decision and one verification plan, uses existing sufficient tests, and simplifies without dropping necessary evidence. See the [cooperation rules](docs/compatibility.md#combining-workflow-skills).

## Explore and contribute

- **Start with an example:** [discover implementations for an architecture](examples/architecture-reuse-example.md), [reuse code](examples/take-example.md), [adapt code](examples/borrow-example.md), [build a missing piece](examples/build-example.md), [reuse tests](examples/test-reuse-example.md), or [resume work](examples/resume-example.md).
- **Inspect decision boundaries:** [missing evidence](examples/blocked-example.md) and [authorization boundaries](examples/needs-approval-example.md). These guides are illustrative; recorded runs are linked above.
- **Help improve it:** [report a reproducible case](https://github.com/Ai-Eastern/reuse-before-build/issues/new/choose), check a host, or [run an evaluation](evals/README.md). Include the revision, host and model, task, expected result, and sanitized evidence.

<details>
<summary>Scope and limits</summary>

This is an instruction workflow; behavior depends on the host and model. It adds no tools or runtime enforcement and does not guarantee lower cost. External research needs the agent's existing network access. Evidence checks do not replace security or legal review.

Resuming covers the current task's engineering state. It does not index unrelated conversations, provide global memory, or grant additional permissions. Examples and evaluation assets are optional; the skill itself is the [`skills/reuse-before-build`](skills/reuse-before-build/SKILL.md) folder.

</details>

[MIT](LICENSE) · Preserve the copyright and license notice when redistributing.
