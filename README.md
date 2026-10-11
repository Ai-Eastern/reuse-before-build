![Build on what already works: reuse code, tests, and decisions.](assets/readme-banner.svg)

<h1 align="center">reuse-before-build</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0969da?style=flat-square&amp;labelColor=24343b" alt="License: MIT"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-SKILL.md-2f6b4f?style=flat-square&amp;logo=markdown&amp;logoColor=white&amp;labelColor=24343b" alt="Agent Skills format: SKILL.md"></a>
  <a href="https://github.com/Ai-Eastern/reuse-before-build/commits/main/"><img src="https://img.shields.io/github/last-commit/Ai-Eastern/reuse-before-build/main?style=flat-square&amp;labelColor=24343b&amp;color=2f6b4f" alt="Last commit on public main"></a>
</p>

<p align="center"><strong>Discover implementations. Reuse code and tests. Resume with evidence.</strong></p>
<p align="center">One skill folder · No service · No runtime dependency</p>

[中文](README.zh-CN.md) · [Install](#install) · [Try it](#try-it) · [Results](#results) · [Compatibility](docs/compatibility.md) · [MIT license](LICENSE)

An Agent Skill that makes your coding agent **look for what already exists before it builds**: in your project, the standard library, your installed dependencies, and, when a real gap remains, GitHub and official sources. It then decides **Take, Borrow, or Build** from code it actually read, not from search snippets or memory.

It targets three habits that cost you later: writing a helper next to one that already exists, adding tests that verify nothing new, and recommending a library whose code and license nobody checked.

## What changes in practice

**Already-covered behavior.** Same task and fixture, observed without and with the skill (GPT-5.6 Luna, 2026-09-21; [report](evals/results/2026-09-21/luna-search-timing/REPORT.md)):

```text
Request   Make sure retry returns on the first success without calling the operation again.
          Keep production code unchanged.
Without   Edited the test file to "strengthen" the first-success case: a diff, but no new coverage.
With      Pointed out that the existing assertion seen == [1] already proves a single call,
          changed nothing, and ran the existing tests.
```

**Choosing a component for a new design** (illustrative workflow):

```text
Request   Design durable webhook delivery for a new service.
Discover  Look for existing implementations on GitHub and in official repositories.
Inspect   Read the core code, failure semantics, tests, and license at a pinned revision.
Decide    Take a verified core, Borrow a suitable pattern, Build only the gap.
Deliver   Show how those choices shape the architecture; label anything unverified.
```

See the [architecture example](examples/architecture-reuse-example.md). A design-only request produces a design; it does not authorize installing dependencies or writing code.

## When to use it

- **Good fit:** choosing an architecture, library, or component; implementing a feature or helper that may already exist; adding or checking tests; resuming engineering work from a handoff or checkpoint.
- **Not needed:** typo fixes, renames, and other small local edits. The skill keeps those to a quick local check.
- **Invocation:** mention `reuse-before-build` in your request. Hosts that choose skills automatically may also load it when a task matches; on your first try, name it explicitly to confirm that it loads.

## Install

The installable unit is the [`skills/reuse-before-build`](skills/reuse-before-build/SKILL.md) folder: `SKILL.md`, the `references/` it reads on demand, and `LICENSE`. Copy the whole folder.

**Claude Code, for all your projects:**

```bash
git clone --depth 1 https://github.com/Ai-Eastern/reuse-before-build.git /tmp/reuse-before-build
```

```bash
cp -R /tmp/reuse-before-build/skills/reuse-before-build ~/.claude/skills/
```

To install it for one project only, copy the folder into that project's `.claude/skills/` instead.

**Codex, Claude Code, and other agents with the skills CLI** (run from your project):

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

Replace `codex` with `claude-code` or another agent name. The CLI needs Node.js ≥22.20.0; the skill itself does not. For manual copies, PowerShell commands, and other hosts' folders, see the [compatibility guide](docs/compatibility.md#manual-installation).

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

A good answer cites the files or sources it actually read and explains its choice. To practice first, use the included [retry-service project](evals/fixtures/retry-service/README.md). If the skill does not load, see [troubleshooting](docs/compatibility.md#troubleshooting).

## How it works

**Find existing work → check that it really fits → choose the smallest scope → verify.**

| Decision | When | What happens next |
| --- | --- | --- |
| **Take** | Existing work already does what is needed | Use it and run the relevant check |
| **Borrow** | Existing code, tests, or a pattern fit with adaptation | Name what is reused and make the smallest change |
| **Build** | Nothing reasonable fits after searching | Build only the missing part and note rejected options |
| **Blocked** | A fact the decision depends on is unavailable | Name the missing fact and keep doing independent work |
| **Needs human approval** | The next step goes beyond what you authorized | Prepare it and ask first |

- **Effort follows the event.** Local inspection comes first. External research starts only for a real capability or compatibility gap; a new session, a new file, or a failing test is not a reason to search again.
- **Evidence over impressions.** Before adopting an outside library, the agent pins a revision and reads its manifest, license, implementation, and a test or call site. Candidates it could not fully read stay labeled *unverified*.
- **Tests before new tests.** It reads the existing runner and assertions, extends them for real gaps, and leaves already-covered behavior alone. New tests use inputs that can tell a right answer from a plausible wrong one.
- **Resume with evidence.** A handoff note or old test log is a claim to check against the current workspace, and it cannot grant new permissions. See the [checkpoint guide](skills/reuse-before-build/references/checkpoints.md).

The rules live in [`SKILL.md`](skills/reuse-before-build/SKILL.md). Details the agent needs only in specific situations, such as inspecting an external candidate or writing a checkpoint, are in [`references/`](skills/reuse-before-build/references/external-candidates.md).

## Results

| What was checked | What we saw | Details |
| --- | --- | --- |
| Restructured skill vs. V13 — Claude Opus 5.5, 2026-10-11 | Both versions passed every check across 8 scenarios (17 runs), including the header-only evidence case that V12 failed on Codex. With full evidence, the restructured version still made an adoption decision instead of blocking. No measurable time or token difference. | [Report](evals/results/2026-10-11/claude-restructure/REPORT.md) |
| Combining with a simplification skill (`ponytail`) — GPT-6 Luna / high, 2026-09-26, V13 | 8 of 8 explicit combination cases met the scoped criteria: existing tests and code were reused, real gaps were extended, no duplicate implementation or second test runner. Some verification commands repeated. | [Report](evals/results/2026-09-26/skill-combination/REPORT.md) |
| Natural loading in the Codex app — GPT-6 Luna / high, 2026-09-26, V10–V12 | The skill loaded natively in most targeted cases. **Known weak spot:** with only response headers available, V12 still adopted the candidate in 2 of 3 runs (the no-skill control also did in 2 of 3). | [Report](evals/results/2026-09-26/native-host/REPORT.md) |
| Core scenarios — GPT-6 Luna / high, 2026-09-26, V10 | 16 fresh-context scenarios met the scoped criteria, including test reuse, a gap test that caught a planted defect, stale-result detection, and handoff permission checks. | [Report](evals/results/2026-09-26/luna6-independent/REPORT.md) |
| Inspecting candidates — GPT-5.6 Luna / medium, 2026-09-26 | 11 runs. Reading of versioned source and license files improved; corroborating tests were still incomplete in live designs. | [Report](evals/results/2026-09-26/evidence-gate/REPORT.md) |
| Search timing and test reuse — GPT-5.6 Luna / medium, 2026-09-21 | 17 runs with no-skill controls. With the skill, sufficient tests were reused without edits and a new assertion caught a deliberately wrong implementation; both architecture trials still skipped source and license inspection. | [Report](evals/results/2026-09-21/luna-search-timing/REPORT.md) |

Each row is a small sample on one host and model, not a success rate. Methods, file hashes, and preserved failures are in [validation](docs/validation.md).

## Use it with other skills

When paired with a simplification skill such as `ponytail`, the agent shares one reuse decision and one verification plan, uses existing sufficient tests, and simplifies without dropping necessary evidence. See the [cooperation rules](docs/compatibility.md#combining-workflow-skills).

Installation routes are documented for **Codex, Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, OpenCode, and Windsurf**. The [compatibility guide](docs/compatibility.md) separates documented support from observed behavior for each host.

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
