---
id: criterion.6_5
type: Criterion
label: "6.5 Eval Loop & Reasoning Capture"
aliases: ["6.5", "Eval Loop & Reasoning Capture"]
tags: ["criterion", "dim-6"]
sources: ["dimensions.json"]
---

# 6.5 Eval Loop & Reasoning Capture

**Type:** Criterion  ·  **ID:** `criterion.6_5`

**Also known as:** 6.5, Eval Loop & Reasoning Capture

Capturing reasoning makes the agentic step improvable, auditable, and a candidate for graduation.

## Attributes

- **dimension:** 6
- **criterion_id:** 6.5
- **anchors:** {'L1': 'No eval; outcomes only (if anything)', 'L2': 'Basic eval; no reasoning capture', 'L3': 'Eval loop + reasoning (accept/override/escalate) captured', 'L4': 'Reasoning feeds quality + the flywheel; decisions auditable', 'L5': 'Reasoning capture is a managed asset driving improvement and trust'}
- **probing_questions:** [{'q': "How established is the team's practice of building an eval loop for the agentic/judgment step — a standard, or only on some builds?", 'looking_for': 'Tests eval maturity. Strong: eval loops are standard for agentic steps. Weak: ad-hoc or absent.'}, {'q': 'How systematically does the team capture the reasoning (accept/override/decline/delegate/escalate, with the why) — not just outcomes — across agentic workflows?', 'looking_for': 'Tests judgment-capture maturity. Strong: systematic reasoning capture. Weak: only outcomes logged; reasoning lost.'}, {'q': 'Is captured reasoning consistently routed into quality improvement and the knowledge flywheel (Dim 2), or does it sit unused?', 'looking_for': 'Tests the link to the moat. Strong: consistently fed back. Weak: captured-but-unused, or not captured.'}, {'q': "How auditable are the team's agentic decisions by design — is explainability/auditability a standard, or retrofitted case-by-case?", 'looking_for': 'Tests auditability maturity. Strong: auditable by design. Weak: black-box, retrofitted under pressure.'}]

## Relationships (incoming)

- [Dimension 6: Agentic Workflow Redesign & Human-AI Pairing](./dim__6.md) → has_criterion
- [Skills-as-Documentation](./concept__skills_as_documentation.md) → references_criterion
- [Evals & Guardrails](./craft__evals_guardrails.md) → references_criterion

## Sources

- dimensions.json
