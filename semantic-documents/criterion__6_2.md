---
id: criterion.6_2
type: Criterion
label: "6.2 Error Reversibility & Recovery-Cost Assessment"
aliases: ["6.2", "Error Reversibility & Recovery-Cost Assessment"]
tags: ["criterion", "dim-6"]
keywords: ["assessment", "criterion", "dim-6", "error", "recovery-cost", "reversibility"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__6_2.md
---

# 6.2 Error Reversibility & Recovery-Cost Assessment  ·  _Criterion_

If errors are undetectable or irreversible with high/impossible recovery cost, an autonomous agent is the wrong choice; recovery cost is part of agentic TCO.

**Key facts:** dimension=6; criterion_id=6.2; anchors={'L1': 'Reversibility/recovery cost not considered; agents act on irreversible steps', 'L2': 'Considered ad-hoc, after build', 'L3': 'Detectability/reversibility/recovery-cost assessed for priority steps and drives design', 'L4': 'Standard: irreversible/high-cost actions behind checkpoints or human-in-loop; recovery cost in TCO', 'L5': 'Disciplined gate input across the portfolio; continuously re-evaluated; feeds intake (5.3) and TCO (1.5)'}; probing_questions=[{'q': 'When designing an agentic step, does the team systematically assess whether errors are DETECTABLE and REVERSIBLE, and the COST/possibility of recovery — or is this overlooked?', 'looking_for': 'Tests the reversibility discipline. Strong: a standard assessment of detectability, reversibility, and recovery cost. Weak: not considered until something goes wrong.'}, {'q': 'Does that assessment DRIVE the design (deterministic-vs-agentic, pairing mode, agent-or-not), or is it considered only after build?', 'looking_for': 'Tests whether it actually gates design. Strong: reversibility/cost shapes the design up front. Weak: bolted on / rationalized after the fact.'}, {'q': 'For irreversible or high-recovery-cost actions, does the team keep a human in the loop or place the irreversible step behind a human checkpoint, as a standard?', 'looking_for': 'Tests safe design for irreversibility. Strong: irreversible steps behind a checkpoint / human-in-loop by default. Weak: autonomous agents act on irreversible, high-cost steps.'}, {'q': "Is error-recovery cost included in the agent's total cost of ownership (and fed to the intake gate / Dim 1.5)?", 'looking_for': 'Tests cost honesty. Strong: recovery cost counted in TCO and at the gate. Weak: recovery cost ignored → TCO understated, bad go/no-go calls.'}].

**Connected to:** cross_references → 1.5 Investment & Funding Model; 1.5 Investment & Funding Model → cross_references; Dimension 6: Agentic Workflow Redesign & Human-AI Pairing → has_criterion; 8.5 Risk Triage & Right-to-Deploy → cross_references; Autonomy Gate → references_criterion; Problem-First Scoping → references_criterion; UX of AI → references_criterion; Autonomy Gate Checklist → references_criterion; Reversibility & Recovery Cost Rubric → references_criterion.

**Sourced from:** dimensions.json.
