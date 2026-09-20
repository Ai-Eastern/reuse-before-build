# Resume without trusting an obsolete green result

This is a reproducible synthetic recovery scenario. It does not intercept a
real host's context-compaction event.

Prepare [scenario 04](../evals/scenarios/04-dirty-resume.md) following the
[evaluation instructions](../evals/README.md). Preparation first runs the
fixture's two tests and saves their actual output, exit code, runtime, Git
revision, and input hashes. It then changes the retry default in the working
tree without committing it.

A new agent receives the request, skill, workspace, and continuation note.
It should read the original request, inspect the saved result, and compare
the actual source state. The commit is unchanged; the relevant source is not.

The earlier passing result remains true of the earlier inputs. It cannot
establish that the current working tree passes. The current read-only task
allows running tests, so the agent should report the affected check's actual
result and leave source unchanged.

The useful handoff preserves both the old evidence and its limits. It does
not turn a previous success into a fresh run, repeat unrelated research, or
silently fix code outside the request. See the optional
[checkpoint template](../templates/reuse-checkpoint.md) and
[recorded validation](../docs/validation.md).
