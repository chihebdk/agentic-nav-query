---
id: criterion.6_6
type: Criterion
label: "6.6 Improvement Flywheel & Continuous Agentic Redesign"
aliases: ["6.6", "Improvement Flywheel & Continuous Agentic Redesign"]
tags: ["criterion", "dim-6"]
sources: ["dimensions.json"]
---

# 6.6 Improvement Flywheel & Continuous Agentic Redesign

**Type:** Criterion  ·  **ID:** `criterion.6_6`

**Also known as:** 6.6, Improvement Flywheel & Continuous Agentic Redesign

Trust and accuracy are earned through usage and continuous improvement; override rate is the key signal.

## Attributes

- **dimension:** 6
- **criterion_id:** 6.6
- **anchors:** {'L1': 'Static agentic step; no signal-driven refinement', 'L2': 'Occasional manual tweaks', 'L3': 'Usage signals drive refinement; override rate tracked', 'L4': 'Reversible (mode changes / pull-back); refinement is signal-driven', 'L5': 'Compounding flywheel; trust/accuracy rise with use; scoped to agentic workflows'}
- **probing_questions:** [{'q': "How mature is the team's flywheel — do usage signals (override rate, escalations, corrections) systematically drive refinement, or is improvement reactive/manual?", 'looking_for': 'Tests flywheel maturity. Strong: systematic, signal-driven refinement. Weak: reactive, manual, or none.'}, {'q': 'Is reversibility an established discipline — does the team re-calibrate pairing modes or pull work back based on signals, as a norm?', 'looking_for': 'Tests governance maturity. Strong: reversibility is practiced. Weak: one-way promotion, no recalibration.'}, {'q': 'Does the team track override rate (and similar health signals) as a standard metric for agentic steps?', 'looking_for': 'Tests the key-signal discipline. Strong: override rate tracked as standard. Weak: not tracked — blind to a failing skill.'}, {'q': 'Across its agentic workflows over time, how well can the team demonstrate compounding — trust and accuracy rising with use?', 'looking_for': 'Tests demonstrable compounding. Strong: evidence of compounding. Weak: flat, no evidence.'}]

## Relationships (incoming)

- [Dimension 6: Agentic Workflow Redesign & Human-AI Pairing](./dim__6.md) → has_criterion
- [Production Readiness](./craft__production_readiness.md) → references_criterion

## Sources

- dimensions.json
