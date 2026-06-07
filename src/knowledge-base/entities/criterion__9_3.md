---
id: criterion.9_3
type: Criterion
label: "9.3 Responsible AI Principles & Practices"
aliases: ["9.3", "Responsible AI Principles & Practices"]
tags: ["criterion", "dim-9"]
sources: ["dimensions.json"]
---

# 9.3 Responsible AI Principles & Practices

**Type:** Criterion  ·  **ID:** `criterion.9_3`

**Also known as:** 9.3, Responsible AI Principles & Practices

RAI as a poster doesn't change outcomes; operationalization into gates does.

## Attributes

- **dimension:** 9
- **criterion_id:** 9.3
- **anchors:** {'L1': 'No RAI practice', 'L2': 'RAI principles stated, not operationalized', 'L3': 'RAI gates + bias/fairness testing for priority work', 'L4': 'RAI embedded by design across the lifecycle; owned + measured', 'L5': 'RAI is a managed, measured, by-design capability across all agents'}
- **probing_questions:** [{'q': 'Are RAI principles operationalized into design/lifecycle gates, not just stated?', 'looking_for': 'Tests operationalization. Strong: RAI gates in the lifecycle. Weak: a poster, not a practice.'}, {'q': 'Do you test for bias/fairness and other RAI risks as standard?', 'looking_for': 'Tests RAI testing. Strong: standard bias/fairness testing. Weak: none → unsafe/biased outputs ship.'}, {'q': 'Is RAI embedded across the lifecycle (by design), or bolted on?', 'looking_for': 'Tests by-design RAI. Strong: embedded by design. Weak: retrofitted/after-the-fact.'}, {'q': 'Is there ownership for RAI and a way to measure adherence?', 'looking_for': 'Tests RAI accountability. Strong: owned + measured. Weak: nobody owns it; unmeasured.'}]

## Relationships (incoming)

- [Dimension 9: Governance & Responsible AI](./dim__9.md) → has_criterion
- [Evals & Guardrails](./craft__evals_guardrails.md) → references_criterion
- [Tool Design & Permissioning](./craft__tool_design_permissioning.md) → references_criterion

## Sources

- dimensions.json
