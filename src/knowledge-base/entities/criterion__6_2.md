---
id: criterion.6_2
type: Criterion
label: "6.2 Error Reversibility & Recovery-Cost Assessment"
aliases: ["6.2", "Error Reversibility & Recovery-Cost Assessment"]
tags: ["criterion", "dim-6"]
sources: ["dimensions.json"]
---

# 6.2 Error Reversibility & Recovery-Cost Assessment

**Type:** Criterion  ·  **ID:** `criterion.6_2`

**Also known as:** 6.2, Error Reversibility & Recovery-Cost Assessment

If errors are undetectable or irreversible with high/impossible recovery cost, an autonomous agent is the wrong choice; recovery cost is part of agentic TCO.

## Attributes

- **dimension:** 6
- **criterion_id:** 6.2
- **anchors:** {'L1': 'Reversibility/recovery cost not considered; agents act on irreversible steps', 'L2': 'Considered ad-hoc, after build', 'L3': 'Detectability/reversibility/recovery-cost assessed for priority steps and drives design', 'L4': 'Standard: irreversible/high-cost actions behind checkpoints or human-in-loop; recovery cost in TCO', 'L5': 'Disciplined gate input across the portfolio; continuously re-evaluated; feeds intake (5.3) and TCO (1.5)'}
- **probing_questions:** [{'q': 'When designing an agentic step, does the team systematically assess whether errors are DETECTABLE and REVERSIBLE, and the COST/possibility of recovery — or is this overlooked?', 'looking_for': 'Tests the reversibility discipline. Strong: a standard assessment of detectability, reversibility, and recovery cost. Weak: not considered until something goes wrong.'}, {'q': 'Does that assessment DRIVE the design (deterministic-vs-agentic, pairing mode, agent-or-not), or is it considered only after build?', 'looking_for': 'Tests whether it actually gates design. Strong: reversibility/cost shapes the design up front. Weak: bolted on / rationalized after the fact.'}, {'q': 'For irreversible or high-recovery-cost actions, does the team keep a human in the loop or place the irreversible step behind a human checkpoint, as a standard?', 'looking_for': 'Tests safe design for irreversibility. Strong: irreversible steps behind a checkpoint / human-in-loop by default. Weak: autonomous agents act on irreversible, high-cost steps.'}, {'q': "Is error-recovery cost included in the agent's total cost of ownership (and fed to the intake gate / Dim 1.5)?", 'looking_for': 'Tests cost honesty. Strong: recovery cost counted in TCO and at the gate. Weak: recovery cost ignored → TCO understated, bad go/no-go calls.'}]

## Relationships (outgoing)

- cross_references → [1.5 Investment & Funding Model](./criterion__1_5.md)

## Relationships (incoming)

- [1.5 Investment & Funding Model](./criterion__1_5.md) → cross_references
- [Dimension 6: Agentic Workflow Redesign & Human-AI Pairing](./dim__6.md) → has_criterion
- [8.5 Risk Triage & Right-to-Deploy](./criterion__8_5.md) → cross_references
- [Autonomy Gate](./concept__autonomy_gate.md) → references_criterion
- [Problem-First Scoping](./craft__problem_first_scoping.md) → references_criterion
- [UX of AI](./craft__ux_of_ai.md) → references_criterion
- [Autonomy Gate Checklist](./template__autonomy_gate_checklist.md) → references_criterion
- [Reversibility & Recovery Cost Rubric](./template__reversibility_recovery_cost_rubric.md) → references_criterion

## Sources

- dimensions.json
