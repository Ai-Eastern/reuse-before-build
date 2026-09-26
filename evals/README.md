# Small behavior evaluations

## External-candidate evidence gate

To compare two full Skill versions, use Python 3.10+ and Node.js 22+:

```sh
python evals/prepare-evidence-gate.py /absolute/existing-parent/gate-run evals/results/2026-09-21/luna-search-timing/skill-v3.md
```

The script reuses the timing fixture/checkpoints and prepares seven model
inputs: two previous/current pairs for live architecture research, two
current-only synthetic offline candidates, and an existing-test regression.
It launches no models. The offline candidates differ only by the supplied
license; their provider metadata is fictional and does not establish real
upstream provenance. A small helper directory from timing preparation may
also exist; only `gate-manifest.json` lists the seven planned model runs.

Give fresh GPT-5.6 Luna / medium agents only their own `TASK.md`, `SKILL.md`,
and workspace. Both comparison arms load a full Skill; do not describe this
as a no-Skill control. Keep the [reviewer criteria](evidence-gate-reviewer.md)
and previous outcomes out of their contexts. Preserve actual tool results,
runtime settings, input hashes, and unsuccessful outcomes. Save new results
in a new dated location; preparation alone is not behavior validation.

The [2026-09-26 report](results/2026-09-26/evidence-gate/REPORT.md) records
eleven executed comparisons/follow-ups, including incomplete inspection.

## Search-timing evaluation

The current timing preparer requires Python 3.10+ and the standard library
only. From the repository root, pass a **new absolute directory** whose parent
already exists:

```sh
python evals/prepare-search-timing.py /absolute/existing-parent/luna-search-timing
```

PowerShell:

```powershell
python .\evals\prepare-search-timing.py 'D:\existing-work\luna-search-timing'
```

It creates exactly seven control/skill pairs, records shared inputs and the
current `SKILL.md` hash, and launches no agents or model processes. Give each
fresh model only its own workspace and `TASK.md`; treatment must load its
local `SKILL.md`, while control must not load a Skill body. Use identical
model/effort settings and permit public research in both arms. Keep the
[reviewer rubric](search-timing-reviewer.md) away from the evaluated model.
See the [recorded comparison](results/2026-09-21/luna-search-timing/REPORT.md)
for dispatches and results; save new runs under a new dated location.
The existing agent catalog is shared across arms, so the comparison is full
Skill body versus no Skill body, not a no-guidance baseline.

The six-scenario material below is historical and remains available for the
earlier fixture evaluation.

This directory contains one MIT project fixture, six agent task inputs, and
a separate reviewer guide. It uses Node.js standard libraries and Git; it
does not install dependencies or invoke a model CLI. It is a reproducible
starting point for manual or agent evaluation, not a published success rate.

Check the fixture directly:

```sh
cd evals/fixtures/retry-service
node --test
```

Prepare one fresh isolated work directory from the repository root. Supply
an absolute path whose parent already exists; the destination must not exist:

```sh
node evals/prepare.mjs 01-local-take /absolute/existing-parent/run-01
```

PowerShell example:

```powershell
node .\evals\prepare.mjs 04-dirty-resume 'D:\existing-work\run-04'
```

The script copies only the fixture, that scenario as `TASK.md`, the current
repository `SKILL.md`, and the project license. It initializes a local Git
baseline with command-scoped identity and disabled hooks. It never changes
global Git configuration, writes to an implicit home directory, adds a
remote, or launches an agent. The script refuses existing destinations and
leaves partial output for inspection if preparation fails; retry with a new
directory. No cleanup or overwrite command is provided.

The script runs the baseline tests and records the real command, timestamps,
exit code, Node version, HEAD, status, input hashes, and raw TAP in
`.git/reuse-eval-baseline/`. For the dirty scenario, it then changes the
working source without committing. For the timeout scenario, it records a
real timed-out local Node process explicitly labeled as a lookup simulation.

Give a fresh evaluating agent access only to the prepared directory, ask it
to load that directory's `SKILL.md`, and supply its `TASK.md`. Do not give it
`evals/reviewer.md`, this preparation script, prior reviewer conclusions, or
other scenario inputs. Do not give it write access to the source repository.
Use a fresh directory and context for each independent run.

Available scenario IDs:

- `01-local-take`
- `02-small-edit`
- `03-test-borrow`
- `04-dirty-resume`
- `05-optional-timeout`
- `06-authority-resume`

After the run, a separate reviewer uses [reviewer.md](reviewer.md), the diff,
and actual command outputs. Record the model and host where available.
Results from one agent, host, or model do not establish support for another.
These task inputs exercise recovery behavior; a plain Skill cannot guarantee
that a host exposes or intercepts every real context-compaction event.

## Architecture discovery

The separate [architecture task](results/2026-09-21/architecture-task.md)
uses a fresh empty workspace, an explicitly loaded Skill, and live public
sources for a design-only request. It is outside the six fixture scenarios
and is not prepared by `prepare.mjs`. See [validation](../docs/validation.md)
for its recorded revision, evidence, and verification limits.
