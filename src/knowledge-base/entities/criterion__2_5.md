---
id: criterion.2_5
type: Criterion
label: "2.5 Trajectory Capture & Learning Flywheel"
aliases: ["2.5", "Trajectory Capture & Learning Flywheel"]
tags: ["criterion", "dim-2"]
sources: ["dimensions.json"]
---

# 2.5 Trajectory Capture & Learning Flywheel

**Type:** Criterion  ·  **ID:** `criterion.2_5`

**Also known as:** 2.5, Trajectory Capture & Learning Flywheel

Closed-loop feedback is the compounding mechanism that widens the gap over rivals.

## Attributes

- **dimension:** 2
- **criterion_id:** 2.5
- **anchors:** {'L1': 'No trajectory capture', 'L2': 'Ad-hoc logging', 'L3': 'Trajectories captured for key skills/agents', 'L4': 'Closed-loop improvement on priority skills; corrections stored with assets', 'L5': 'Systematic flywheel; every interaction improves the library; trajectories a managed moat'}
- **probing_questions:** [{'q': 'Do you capture agent/skill execution trajectories (successes and failures)?', 'looking_for': "Trajectories are the improvement dataset ('the harness is the dataset'). Strong: captured systematically. Weak: not captured → no basis to learn."}, {'q': 'Does each use of a skill/agent feed back to improve it?', 'looking_for': 'Tests the closed loop that makes assets compound. Strong: usage improves the asset. Weak: static assets → they decay.'}, {'q': 'Are corrections stored with the skill/data for the next iteration?', 'looking_for': 'Probes whether learning is retained. Strong: corrections persisted with the asset. Weak: lessons lost → same failures recur.'}, {'q': 'Who owns the improvement loop?', 'looking_for': 'Tests accountability for continuous improvement. Strong: a named owner. Weak: nobody → the flywheel never turns.'}]

## Relationships (incoming)

- [Dimension 2: Knowledge Building & Capability Reuse](./dim__2.md) → has_criterion
- [Knowledge Moat](./concept__knowledge_moat.md) → references_criterion
- [Skill](./concept__skill.md) → references_criterion
- [Evals & Guardrails](./craft__evals_guardrails.md) → references_criterion
- [Agent Memory](./craft__agent_memory.md) → references_criterion

## Sources

- dimensions.json
