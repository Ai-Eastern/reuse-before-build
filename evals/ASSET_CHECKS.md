# Fixture and preparation checks

Observed on 2026-09-20 using Windows, Node.js `v24.18.0`, and
`git version 2.55.0.windows.3`. These are checks of the evaluation assets;
they are **not agent behavior results** or cross-platform certification.

| Command or check | Observed result |
| --- | --- |
| `node --check evals/prepare.mjs` | Exit 0 |
| `node --test evals/fixtures/retry-service/test/retry.test.mjs` | 2 tests; 2 passed; 0 failed; exit 0 |
| `node evals/prepare.mjs <each-of-the-six-scenario-ids> <fresh-absolute-directory>` | All 6 prepared successfully; each recorded a clean Git baseline and an actual test run with exit 0 |
| `node --test --test-reporter=tap` in the prepared `04-dirty-resume` fixture | 1 passed; 1 failed; exit 1; failing case was the third-attempt default behavior |
| `git status --short` in that dirty fixture | ` M src/retry.mjs`; baseline HEAD retained |
| Prepare again into an existing destination | Rejected before overwrite: `Refusing existing destination` |
| Prepare using a relative destination | Rejected with absolute-path usage requirement |
| Prepare while inherited `GIT_DIR` and `GIT_WORK_TREE` point at another location | Correct isolated repository created; the sentinel location was not created |
| Inspect prepared fixture contents | Reviewer guide, preparation script and other scenario prompts were not copied |

The dirty fixture's failure is intentional: it demonstrates that a genuine
old passing result can coexist with a currently failing uncommitted change.
Preparation itself records the original TAP and snapshot before that change.

An initial Windows run exposed Git rejecting Node's Windows null-device
path as a global configuration file. Preparation now uses a regular empty
configuration file inside its own new work directory; all checks above were
performed after this correction. No user or global Git configuration was
changed.

Repeat relevant checks when these assets change. Actual agent runs require
separate fresh contexts, the recorded skill version, observed actions, and
independent review against `reviewer.md`. Passing these asset checks does not
show that an agent follows the Skill or handles a real host compaction event.
