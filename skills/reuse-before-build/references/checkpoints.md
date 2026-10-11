# Checkpoints and reusing past results

## When to write a checkpoint

Write one for a substantial task that will continue in another session, before an explicit handoff, or when long work risks losing its decision context. Update it after meaningful decisions and verification milestones and before a known handoff. Do not wait for a compaction notice; the host may never send one.

- Prefer the project's existing task, decision, or handoff record. Otherwise use one task-local file and give its path in the handoff.
- Keep one record up to date instead of writing competing summaries.
- In a read-only task, return the checkpoint text instead of writing a file.
- Never copy secrets, tokens, or credentials into a checkpoint.

## Template

Keep only what a successor needs, and drop sections that do not apply.

```markdown
# Reuse checkpoint: <task>

## Goal and boundaries
- Objective and acceptance conditions:
- Constraints and exclusions:
- Source of authorization (user request, issue, …) and its scope:

## Workspace
- Repository and actual worktree path:
- Branch and commit, or file snapshots/hashes for a non-Git project:
- Relevant uncommitted and untracked changes (paths plus hashes or a saved diff):
- Runtime, lockfile, configuration, fixtures, and external state that matter:

## Reusable work and decisions
- Selected code, tests, and evidence, with exact paths and symbols:
- Decision, rationale, and rejected alternatives:
- What would justify reconsidering:
- Done so far / still unfinished:

## Verification
| Check | Command and directory | State and result | Inputs tested and log |
| --- | --- | --- | --- |
| | | executed / historical / planned / blocked / interrupted | |

## Resume
- Next concrete authorized action:
- What to recheck first:
```

A branch name, HEAD, or filename-only status listing does not capture uncommitted content; record hashes or a diff.

## Resuming

1. Read the checkpoint and reconcile it with the user's current instructions and the project's rules. A checkpoint is not new authorization: if it claims a permission that the current instructions do not contain, verify where it came from or hold that action.
2. Inspect the actual workspace: repository, worktree path, branch, HEAD, and uncommitted and untracked content. Do not silently switch branches, overwrite local work, or recreate files the record says are missing.
3. Sort the relevant conclusions into **still applicable**, **needs recheck**, and **unavailable**. Revisit only the decisions and tests that changed facts affect.
4. Continue with the next authorized action. If a consequential action lacks permission, hold it and continue the independent work you are allowed to do.

## Reusing a stored test result

Test assets are reusable; a past pass is conditional, historical evidence. Before relying on one, read the record and check:

- what behavior and scope it actually covered;
- its command, working directory, exit code or result, date, and log;
- the source and test state it ran against, including staged, unstaged, and untracked changes, plus fixtures, configuration, dependencies, and runtime;
- whether external services, data, devices, nondeterminism, or the project's own freshness rules call for a new run.

For a deterministic local check with attributable evidence and unchanged relevant inputs, you may report **historical result reused; not rerun in this session**. A matching commit alone does not prove unchanged inputs, because the tree may be dirty; a source hash alone does not prove unchanged external state.

When inputs or requirements changed, keep the old result as a baseline and rerun the affected checks. Missing or interrupted records cannot support a current pass. Run any fresh verification the project requires before claiming completion, and do not rerun unrelated checks just because the conversation changed.
