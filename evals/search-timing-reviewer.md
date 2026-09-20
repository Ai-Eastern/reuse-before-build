# Search timing comparison — reviewer only

Do not provide this rubric to the evaluated model. Use fresh GPT-5.6 Luna
sessions at **medium** reasoning effort for both arms. Fix the Skill hash
before starting. Every task has byte-identical shared inputs; only the
treatment arm receives the full `SKILL.md` and an instruction to use it.
Both arms can use read-only public internet tools. Do not forbid the action
being measured in the task prompt.

| Case | Observe in actions, file differences, and final answer |
| --- | --- |
| small-edit | Only the README typo changes; no external candidate survey or unrelated test/framework additions. |
| covered-test | Reads relevant assertions and uses the existing runner; does not duplicate the already-covered third-attempt test or change production code. |
| covered-variant | Recognizes that the existing first-success result and `[1]` assertions already guarantee one call; runs existing coverage without a redundant rewrite. |
| test-gap | Extends existing coverage for final-error identity, configured call count, and zero-attempt rejection with zero calls; preserves production code and existing meaningful assertions. |
| local-failure | Diagnoses the local default-attempt regression; restores behavior and runs affected checks rather than replacing the retry implementation or researching a new package solely because a test failed. |
| unchanged-resume | Reconciles historical evidence with current inputs, distinguishes reused historical results from fresh execution, and avoids unnecessary candidate research; no source edits. A relevant fresh run is not automatically a failure. |
| changed-requirement | Recognizes the old in-process decision's limited scope, inspects local assets, then researches the newly missing durable capability before recommending components; cites primary evidence, distinguishes proposal from runtime proof, and keeps the task design-only. |

Record whether local source/test inspection preceded edits or candidate
search. Distinguish a targeted official API/error lookup from a new project
survey; do not fail a justified factual lookup. Missing telemetry is unknown,
not proof of no network action. Grade behavior rather than exact wording,
Take/Borrow/Build labels, or any preferred external package.

Passing tests alone do not establish useful coverage. For final-error
identity, the inputs must distinguish the last error from earlier errors;
throwing the same object every time cannot check that distinction. For
external adoption, search-result excerpts alone do not satisfy the Skill's
source, interface, and license inspection gate. Record timing and evidence
quality separately when one passes and the other does not.

Export only task prompts, observable tool calls/results, user-facing final
answers, environment/model settings, snapshots, and review conclusions.
Exclude private reasoning and unrelated system/developer instructions.
Record any forbidden cross-run/global-skill reads as contamination, not as
a successful clean comparison.

Desktop sessions may still expose the installed skill catalog and common
agent instructions in both arms. The control prohibits loading Skill bodies,
but that does not remove shared descriptions or general coding guidance.
Describe this as **full-Skill versus no-full-Skill** within the same host,
not an otherwise unprompted model. Explicit loading does not test automatic
discovery. A single pair per case is exploratory, not a success rate or
causal proof that the new timing paragraph alone made the difference.
