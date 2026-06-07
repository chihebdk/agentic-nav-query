---
id: criterion.4_4
type: Criterion
label: "4.4 Graduation to Autonomy (in-loop -> operator -> out-of-loop)"
aliases: ["4.4", "Graduation to Autonomy (in-loop -> operator -> out-of-loop)"]
tags: ["criterion", "dim-4"]
sources: ["dimensions.json"]
---

# 4.4 Graduation to Autonomy (in-loop -> operator -> out-of-loop)

**Type:** Criterion  ·  **ID:** `criterion.4_4`

**Also known as:** 4.4, Graduation to Autonomy (in-loop -> operator -> out-of-loop)

Autonomy is earned through a gate, not pursued; most work is most valuable in-loop/operator.

## Attributes

- **dimension:** 4
- **criterion_id:** 4.4
- **anchors:** {'L1': 'Push for autonomy everywhere', 'L2': 'Autonomy decided ad-hoc', 'L3': 'Stages explicit; autonomy case-by-case; most work stays in-loop/operator', 'L4': 'Four-condition gate governs graduation; augmentation-first; reversible', 'L5': 'Gated, reversible, audited graduation; out-of-loop only where proven; centralized runtime keeps it safe'}
- **probing_questions:** [{'q': 'Do you treat the path as in-loop -> operator -> out-of-loop, with most work staying in-loop/operator by design?', 'looking_for': 'Tests the graduation mindset. Strong: stages explicit; most work stops early by design. Weak: out-of-loop treated as the goal → autonomous-first failure.'}, {'q': 'Is autonomy earned through the four-condition gate (stable pattern; bounded failure cost; evaluable; volume & leverage)?', 'looking_for': 'Tests the gate. Strong: all four required before graduating. Weak: autonomy granted on enthusiasm → high-impact failures.'}, {'q': 'Is graduation reversible — do you pull work back when conditions no longer hold?', 'looking_for': 'Tests governance of autonomy. Strong: work is pulled back when it starts failing. Weak: one-way promotion → silent drift into failure.'}, {'q': 'Does a centralized runtime/harness make out-of-loop safe (guardrails, human checkpoints, audit)?', 'looking_for': 'Tests safe-autonomy infrastructure. Strong: out-of-loop runs with guardrails/checkpoints/audit. Weak: autonomy without a safety harness → uncontained risk.'}]

## Relationships (incoming)

- [Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy)](./dim__4.md) → has_criterion
- [Problem-First Scoping](./craft__problem_first_scoping.md) → supports_craft
- [Augmentation-First](./concept__augmentation_first.md) → references_criterion
- [Autonomy Gate](./concept__autonomy_gate.md) → references_criterion
- [Autonomy Ladder](./concept__autonomy_ladder.md) → references_criterion
- [Agent](./concept__agent.md) → references_criterion
- [Capability Ladder](./concept__capability_ladder.md) → references_criterion
- [Evals & Guardrails](./craft__evals_guardrails.md) → references_criterion
- [Production Readiness](./craft__production_readiness.md) → references_criterion
- [Autonomy Gate Checklist](./template__autonomy_gate_checklist.md) → references_criterion
- [Production Readiness Checklist](./template__production_readiness_checklist.md) → references_criterion
- [Reversibility & Recovery Cost Rubric](./template__reversibility_recovery_cost_rubric.md) → references_criterion
- [Pairing Mode Playbook](./template__pairing_mode_playbook.md) → references_criterion

## Sources

- dimensions.json
