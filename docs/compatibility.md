# Compatibility and installation

[English README](../README.md) · [中文说明](../README.zh-CN.md) · [Validation](validation.md)

Checked against the linked documentation on **2026-09-20**. Host support changes over time; this page separates documented support from observed results.

## What a support claim means

- **Documented format support:** the host documents loading an Agent Skill from a folder containing `SKILL.md`. This is a plausible installation route, not a behavioral test of this skill.
- **Installation checked:** a named installer and environment discovered and copied this skill successfully. This does not establish that an agent loaded or followed it.
- **Behavior evaluated:** a recorded agent run checks a specific task and result. It applies to that revision, host, model, and environment only.

The skill follows the [Agent Skills format](https://agentskills.io/specification) and needs only its own `SKILL.md`. Keep `LICENSE` with distributed copies. No plugin manifest, MCP server, hook, database, or bundled executable is required.

## Host matrix

Paths below are relative to the project root and end with `reuse-before-build/SKILL.md`. Choose one supported location; copying the same skill into several discovery locations can create ambiguity.

| Host / surface | Documented project directory | Revision-scoped evidence | Official reference |
| --- | --- | --- | --- |
| Codex local app / CLI / IDE | `.agents/skills/` | Prior revision: `skills@1.7.0` project installation checked on Windows with Node.js 24.18.0; see [validation](validation.md) for dated behavior evidence | [Codex skills](https://developers.openai.com/codex/skills/) |
| Claude Code local CLI | `.claude/skills/` | Format documented; current revision not runtime-tested in Claude Code | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| GitHub Copilot CLI | `.github/skills/` or `.agents/skills/` | Format documented; current revision not runtime-tested in Copilot CLI | [Copilot skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [CLI installation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) |
| Cursor local agent | `.cursor/skills/` or `.agents/skills/` | Format documented; not runtime-tested | [Cursor skills](https://cursor.com/docs/skills) |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` | Format documented; not runtime-tested | [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) |
| OpenCode | `.opencode/skills/` or `.agents/skills/` | Format documented; not runtime-tested; consult documentation matching your major version | [OpenCode skills](https://opencode.ai/docs/skills/) |
| Windsurf / Cascade | `.windsurf/skills/` | Format documented; not runtime-tested | [Cascade skills](https://docs.devin.ai/desktop/cascade/skills) |

Cloud agents and remote sessions need the skill available in their own environment. A local personal installation does not establish availability in a cloud task. Copilot CLI validation would not by itself establish behavior in VS Code or the Copilot coding agent.

### Historical author observations

The previous README reported manual exercises in Codex, Claude Code, and GitHub Copilot CLI. The repository did not include the host/model versions, raw transcripts, or a reproducible comparison. Those reports remain historical context, not validation of this revision or a ranking of the tools. Current observations and checks belong in [validation.md](validation.md).

## Optional installer

The examples pin [Vercel's skills CLI 1.7.0](https://github.com/vercel-labs/skills/tree/v1.7.0). Its [package manifest](https://github.com/vercel-labs/skills/blob/v1.7.0/package.json) requires **Node.js >=22.20.0**. That requirement belongs to the optional installer, not to `reuse-before-build`.

To install from GitHub, run from your target project:

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

For a local source installation, use a clean checkout or source archive. Run the following from a **separate consuming project**, replacing the source path with the absolute path to that checkout:

**PowerShell**

```powershell
$skillSource = (Resolve-Path 'C:\path\to\reuse-before-build').Path
npx skills@1.7.0 add "$skillSource" --skill reuse-before-build --agent codex --copy -y
```

**POSIX shell**

```sh
skill_source=/absolute/path/to/reuse-before-build
npx skills@1.7.0 add "$skill_source" --skill reuse-before-build --agent codex --copy -y
```

Do not run `add .` in the skill source checkout. In CLI 1.7.0, a destination inside the source can produce a skipped copy even when the process exits successfully. Inspect the installed files rather than relying on exit status alone. See the [installer's overlap handling](https://github.com/vercel-labs/skills/blob/v1.7.0/src/installer.ts) and the [local validation record](validation.md).

These commands use project scope and copy files. They do not request a global installation. Consult the pinned installer's documentation or `--help` for other agents; its supported-agent list does not imply this skill was behavior-tested on each agent. Package-manager caches may still be written outside the project as part of normal `npx` operation.

### Why GitHub CLI is not the recommended route

In the local check with GitHub CLI **2.97.0**, discovery failed for this repository's root-level `SKILL.md`. The upstream report [cli/cli#13552](https://github.com/cli/cli/issues/13552) describes the same repository shape. This is a version-specific discovery limitation, not a claim that `gh skill` is generally unavailable. Use the checked installer or a manual copy; retest future GitHub CLI versions before documenting them as working here.

## Manual installation

No Node.js is needed. Use a complete local checkout containing the revision you intend to install. The PowerShell copy below was checked in a separate local directory: both installed files matched their sources by SHA-256. POSIX instructions have not been executed on a Unix host in this validation run.

From your **target project**, install using the host's directory from the table. Replace the source path with your local checkout's location. For Codex:

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

Preserve the `reuse-before-build` folder name and keep `SKILL.md` directly inside it. Do not create an extra nested `reuse-before-build` folder. Examples, templates, and evaluation assets can stay in the source checkout.

For a personal installation, use the location documented by the host and confirm its discovery behavior. Current Codex documentation lists `~/.agents/skills/` for personal skills. Older instructions and some installers use `~/.codex/skills/` or `$CODEX_HOME/skills`; support depends on your installed version. This guide does not declare those locations invalid, remove existing installations, or require a global configuration change.

Downloading a raw `main/SKILL.md` URL obtains the currently published file. It cannot deliver unpublished local changes. Preserve the matching license notice if using a downloaded file.

## Verify discovery and behavior

1. Confirm the installed folder contains `SKILL.md` with `name: reuse-before-build` in its frontmatter.
2. Open the project in the intended host and check its discovered skills. Refresh or restart according to that host's documentation if the new skill is absent.
3. Explicitly select or mention `reuse-before-build` and use the first-task prompt in the README.
4. Check the output against actual source files: did it find relevant existing code and tests, distinguish historical evidence from current verification, and justify its next step?

Some hosts select skills automatically; an explicit first invocation makes troubleshooting easier. A successful file copy or an expected heading in the response is insufficient to demonstrate useful behavior. See the [validation guide](validation.md) for reproducible checks and result boundaries.

## Updating and removing

For a manual copy, compare your installed files with the intended source revision before updating. Preserve local edits, replace this skill's `SKILL.md` and `LICENSE`, and repeat the discovery check. Optional documentation and evaluation assets can stay in the source checkout.

For installer-managed copies, use the management commands documented for your installed `skills` version. Update and removal commands were not exercised in this validation run, so this page does not present them as tested procedures. A local-source installation is a copy: editing the source checkout does not automatically update the installed files.

To remove a manual installation, first confirm the exact installed `reuse-before-build` directory and whether it is a copy or a symlink. Remove only that entry using your file manager; leave shared skill directories and unrelated skills intact. Reload the host and check that the intended entry is gone. If it remains, inspect other discovery locations for a second copy.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| The skill is absent | Correct host directory, project opened in that environment, exact filename, valid frontmatter, and any workspace trust or administrator restrictions |
| An old version runs | Compare the installed file with the source revision; check for a personal or plugin copy and the host's precedence rules |
| Node.js is too old or unavailable | Use the manual copy path; the skill itself does not execute Node.js |
| `gh skill` finds no skills | Check the root-level discovery limitation above and use a documented alternative |
| Local installation says skipped | Run from a separate consuming project with an absolute source path; verify that the destination contains the intended file |
| Installation worked but the agent skips the workflow | Invoke the skill explicitly, inspect which copy loaded, and record the host/model/task when reporting the issue |
| External research is unavailable | Record the limitation; use valid local evidence where sufficient and identify any fact that still blocks the actual decision |
| A previous check passed but the code changed | Match the historical record to its revision, command, and environment, then run the relevant current check |

Report issues with the skill revision, host/version, model, OS, installation method, task, expected behavior, and sanitized evidence. Never include credentials or private project content without permission.
