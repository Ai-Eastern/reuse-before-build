---
name: reuse-before-build
description: Apply a reuse-first decision gate before implementing non-trivial coding work. Use when a task may duplicate an existing project feature, library, GitHub repository, official example, or licensed implementation, or when reuse, adaptation, licensing, maintenance, or compatibility needs explicit evidence.
---

# Reuse Before Build

Use this workflow before coding a non-trivial feature. The goal is an evidence-backed decision, not a general architecture review.

## Trigger and scope

Trigger for new integrations, substantial features, infrastructure, data handling, security-sensitive code, or work that sounds like “add a reusable component.” Do not force a full external search for a clearly scoped rename, typo fix, or small local edit; still inspect the local context.

## Required gate

1. Read the applicable project rules, architecture notes, source code, tests, and dependency manifests.
2. Search the project for an existing implementation, near-duplicate, extension point, and tests. Record paths and relevant symbols.
3. For non-trivial work, search GitHub, official documentation, and package registries as applicable. Prefer primary sources. Do not download or copy third-party code automatically.
4. Keep one candidate record per artifact: name, source/path, version, license, maintenance, compatibility, fit, and verification status. Merge aliases and near-duplicates before comparing candidates.
5. Check source, version, license, maintenance signals, security posture, compatibility, integration cost, and evidence quality. Treat unknown license, unclear provenance, or insufficient evidence as a stop condition.
6. Choose exactly one outcome: `Take`, `Borrow`, `Build`, `Blocked`, or `Needs human approval`.

## Decision thresholds

- **Take**: An existing implementation meets the requirements with acceptable source, version, license, maintenance, compatibility, and verification evidence. Use it directly and cite the evidence.
- **Borrow**: No direct fit exists, but a credible implementation supplies a useful pattern, interface, workflow, or test strategy. State exactly what is adapted and what is deliberately not copied; make local differences explicit.
- **Build**: Take and Borrow cannot reasonably satisfy the requirements. Explain why, including the searched scope and rejected candidates, before implementing a new solution.
- **Blocked**: A required fact is unavailable or contradictory, such as an unknown license, inaccessible source, or unresolved compatibility risk. Stop and report the missing evidence.
- **Needs human approval**: A decision would require accepting a legal, security, data, or operational risk outside the agent’s authority. Stop and ask for approval.

If a known risk requires an authorized exception, choose `Needs human approval`; if the decision cannot be evaluated because required facts are missing, choose `Blocked`. Do not use `Build` to evade either stop condition.

Do not call something `Build` merely because searching is inconvenient. Do not call something `Take` when it requires substantial local changes; that is usually `Borrow`. Never invent repository, license, maintenance, or compatibility facts.

## Standard output

Return this exact shape before implementation:

```markdown
## Reuse Decision

Decision: Take | Borrow | Build | Blocked | Needs human approval

### Evidence
- Project search:
- GitHub / official search:
- License:
- Maintenance:
- Compatibility:
- Verification:

### Rationale

### Next step
```

For `Take`, name the artifact and the verification plan. For `Borrow`, identify the borrowed idea and local adaptation boundary. For `Build`, list the meaningful rejected candidates and the smallest new design. For `Blocked` or `Needs human approval`, name the exact decision-stopping question and do not begin implementation.

## Exceptions and verification

For a small local change, give a brief local-search result and proceed if the change is clearly bounded. For every other task, verify the selected path with focused tests, an existing example, or a minimal reproduction before claiming success. Keep evidence separate from inference, and cite URLs or file paths where available.
