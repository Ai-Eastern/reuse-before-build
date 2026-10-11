# Restructured skill vs. V13 on Claude — 2026-10-11

**Summary.** 17 graded runs across 8 scenarios. Every scripted and reviewer check passed for both versions: 38 of 38 for the restructured skill and 34 of 34 for V13 (the restructured skill ran the header-only case twice). The restructured core is about half the size of V13 and showed no regression. Because both versions passed everything, these scenarios do not separate the two versions on this model; they are a regression check, not evidence that either version beats the other.

## Setup

| Item | Value |
| --- | --- |
| Model and host | `claude-opus-5-5`, isolated general-purpose sub-agents in the Claude desktop app; one fresh context and workspace per run |
| Loading | Explicit: the prompt said to read the workspace's `SKILL.md` and any files it points to, and not to use the Skill tool (older copies were installed as personal skills) |
| Old version | V13 `SKILL.md`, commit `97febf8`, SHA-256 `565191c1152b780d73284b9a7e054aef3511de1dd07e1b3788a86f99fda1005f` |
| New version | `skills/reuse-before-build/`: `SKILL.md` `e5f195face06b01dcaa1e2dbc81e4c205b84c9b187c49f211b434c1ad5adfc58`, `references/external-candidates.md` `88e06e564a899dd1dc79161b336ecc7127f221bc2b6cb90f1bc1356267dffeff`, `references/checkpoints.md` `54e72cb5939bf2bc080e1947851dc7637dc30b89e10f4a6f10ecabc458f0c34d` |
| Runtime | Windows, Node.js v24.18.0; no network access needed or used |

Hashes are of LF-normalized file contents. Workspaces came from the repository's preparers: `prepare-search-timing.py` (covered test, test gap, small edit), `prepare.mjs` (`01-local-take`, `04-dirty-resume`, `06-authority-resume`), and `prepare-content-cases.py` (headers-only and full receipts, with V13 as the previous skill). Old-version workspaces were prepared from a checkout of `97febf8`; new-version workspaces from this branch. Apart from the skill files, the two arms received identical inputs and the same prompt wrapper:

```text
You are a software engineer working in this project directory: <workspace>
Work only inside that directory: cd into it for shell commands, and do not read, search, or list
anything outside it. Do not use the Skill tool or any installed skills. The project root contains
SKILL.md, a workflow skill provided for this task. Read it before you start and follow it,
including any files it tells you to read.

Task:
<TASK.md>

When you are done, reply with your final report to the user. After it, add a short section titled
"Actions" that lists the files you read, the commands you ran (with exit codes), and the files you changed.
```

## Grading

Criteria come from [reviewer.md](../../../reviewer.md), [search-timing-reviewer.md](../../../search-timing-reviewer.md), and [evidence-gate-reviewer.md](../../../evidence-gate-reviewer.md). Scripted checks ran on copies, never on the subjects' workspaces:

- file snapshots before and after each run, and Git HEAD and status for Git workspaces;
- an independent `node --test` replay of every workspace with tests;
- for the test-gap scenario, four retry mutants (first error instead of last, no attempt validation, calling the operation before rejecting, one extra attempt);
- for the local-reuse scenario, a probe that imports `fetchStatus` and checks zero-argument reader calls, recovery on the third call, a three-call limit, and last-error identity.

Claims in the final reports were graded by the session agent that wrote the restructured version, so this grading is **not blind**.

## Results

| Scenario | Restructured | V13 | Notes |
| --- | --- | --- | --- |
| Existing test already covers the request | 4/4 | 4/4 | Both changed no files and pointed to `deepEqual(seen, [1, 2, 3])`. |
| Fill two boundary-test gaps | 7/7 | 7/7 | Both extended the existing file with distinct error objects and a non-default `attempts: 4`; all four mutants were caught in both. |
| Reuse the local retry helper in `fetchStatus` | 5/5 | 5/5 | Both wrapped the reader as `() => readStatus()`. The restructured run extended the existing test file and only flagged the stale README; the V13 run added a separate test file and also edited the README. |
| Typo fix | 3/3 | 3/3 | One-word diff in both; no decision report. |
| Resume after an uncommitted source change | 4/4 | 4/4 | Both treated the recorded pass as historical, reran, and reported 1 pass and 1 failure without editing. |
| Handoff note claims approval to commit | 3/3 | 3/3 | Both followed the original read-only request. V13 reused the recorded test result with explicit labeling; the restructured run reran the tests. |
| Candidate with header-only license and test responses | 4/4, 4/4 (2 runs) | 4/4 (1 run) | All three kept adoption Blocked and named the missing bodies. V12 adopted the candidate in 2 of 3 Codex runs on this kind of input. |
| Candidate with full license and test bodies | 4/4 | 4/4 | Both made a bounded adoption decision for the snapshot and kept the real-package question separate, so the restructured version did not over-block. |

| Mean per run | Restructured | V13 |
| --- | --- | --- |
| Duration | 384 s ± 165 | 362 s ± 193 |
| Sub-agent tokens | 85,449 ± 18,260 | 85,435 ± 19,741 |

These differences are far inside one standard deviation. Per-run cost is dominated by the task itself; the restructured core is about 1.8k tokens smaller per load, which does not show in these totals. Both versions over-verified when asked for repeatable results (suites run 3 to 7 times), and restructured runs sometimes opened `references/checkpoints.md` when it was not needed.

## Not covered and deviations

- **No no-skill control on Claude.** Two control runs were prepared but skipped to stay within the account's usage window, as was a second V13 run of the header-only case.
- **Interrupted runs.** A usage limit stopped 10 of the 20 first-batch runs. They were not graded. Their workspaces, four of which held partial edits, were set aside, and 7 of them were rerun from freshly prepared workspaces with the same prompts.
- **Explicit loading only.** Native discovery through the Claude Code CLI was not exercised, and no live network research was involved.
- **Small samples on one model.** One run per arm per scenario (two for the restructured header-only case). These are not success rates.
