# reuse-before-build

An evidence-backed Take / Borrow / Build workflow that helps coding agents check what already exists before creating another implementation.

It addresses the repeated “build it again” problem: duplicate project code, overlooked official solutions, incompatible dependencies, and avoidable license or maintenance risk. It is a decision gate, not a generic prompt, because it requires concrete searches and a traceable outcome before implementation.

## Install

Copy this folder into an Agent Skills directory supported by your agent runtime. The required file is `SKILL.md`; the examples are optional reading material. No runtime dependency or script is required.

The workflow is standard-compatible and has been manually exercised in Codex against eight task scenarios covering direct reuse, adaptation, new implementation, missing license evidence, approval-required risk, bounded edits, duplicate local work, and official examples. Other agents may load it manually by attaching or pasting `SKILL.md`; only agents whose skill loaders recognize this format are considered verified. This is not a claim of support for every coding agent.

## Workflow

1. Read project rules, relevant source, tests, and manifests.
2. Search the project for existing implementations and duplicates.
3. For non-trivial work, search GitHub, official documentation, and package registries where relevant.
4. Check provenance, version, license, maintenance, compatibility, integration cost, and verification evidence.
5. Output one decision: `Take`, `Borrow`, `Build`, `Blocked`, or `Needs human approval`.
6. Implement only after the evidence supports the decision.

### Take

Use an existing implementation when it already satisfies the requirements with acceptable evidence. Verify the source, version, license, compatibility, and focused behavior.

### Borrow

Adapt a useful pattern when no direct fit exists. Name what is borrowed, what is not copied, and how local constraints change the design.

### Build

Create a new implementation only after local and relevant external searches show that Take and Borrow are not reasonable. Record rejected candidates and the smallest justified design.

See [examples/take-example.md](examples/take-example.md), [examples/borrow-example.md](examples/borrow-example.md), and [examples/build-example.md](examples/build-example.md).

## Decision table

| Evidence | Decision | Action |
| --- | --- | --- |
| Direct fit, acceptable risk, verified | Take | Use and verify |
| Useful pattern, local adaptation required | Borrow | Adapt with boundaries |
| No reasonable fit after search | Build | Implement the smallest solution |
| Missing or contradictory required evidence | Blocked | Stop and report |
| Risk exceeds agent authority | Needs human approval | Stop and ask |

If an external page cannot be fetched or a license, maintenance, provenance, or compatibility fact cannot be verified, stop at `Blocked`; do not fill the gap from memory or turn the failed search into `Build`.

## Limits

This Skill does not automatically copy third-party code, download repositories, provide legal advice, replace security review, replace TDD or ADR processes, or maintain a real-time compatibility database. License checks are evidence gathering, not legal approval. Small local edits can use a lightweight local-search path.

## License and contribution

MIT licensed. Contributions are welcome when they keep the workflow provider-neutral, concise, evidence-based, and useful across compatible Agent Skills runtimes. The canonical repository is the repository containing this file; if you redistribute it, preserve the MIT notice.
