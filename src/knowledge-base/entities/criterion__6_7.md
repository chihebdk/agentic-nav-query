---
id: criterion.6_7
type: Criterion
label: "6.7 Human-AI Interaction & UX Design"
aliases: ["6.7", "Human-AI Interaction & UX Design"]
tags: ["criterion", "dim-6"]
sources: ["dimensions.json"]
---

# 6.7 Human-AI Interaction & UX Design

**Type:** Criterion  ·  **ID:** `criterion.6_7`

**Also known as:** 6.7, Human-AI Interaction & UX Design

Adoption and safe use depend on the interface, not just model quality: users must see uncertainty, verify, correct, and escalate. Bad UX causes over-trust or abandonment regardless of model accuracy.

## Attributes

- **dimension:** 6
- **criterion_id:** 6.7
- **anchors:** {'L1': 'Raw model output dumped to users; no failure/loading/empty states; no correction path', 'L2': 'Basic UI; some error handling; uncertainty/correction ad-hoc', 'L3': 'Failure/loading/empty states, escalation/correction paths, and uncertainty/citations designed as standard', 'L4': 'UX patterns reused across builds; trust calibrated (provenance, confidence); the creator->editor human boundary designed in', 'L5': 'Interaction quality measured (trust calibration, override/abandonment, in-UI task success) and continuously improved; UX is a managed asset'}
- **probing_questions:** [{'q': 'How does the team design the INTERFACE around the agentic step — failure, loading, and empty states; what the user sees when the model errs, a tool times out, or retrieval is empty — as a standard, or is raw model output dumped to the user?', 'looking_for': 'Tests interaction maturity. Strong: failure/loading/empty states designed as a norm. Weak: raw output dumped; the UI breaks on the unhappy path.'}, {'q': "How does the team communicate UNCERTAINTY and PROVENANCE (confidence, what's supported, citations/sources) so users can calibrate trust rather than over- or under-trust the agent?", 'looking_for': 'Tests trust-calibration design. Strong: uncertainty + provenance surfaced so users verify appropriately. Weak: confident-looking output with no way to judge or check it.'}, {'q': "Is the human's CORRECTION / OVERRIDE / ESCALATION path designed into the experience itself (not just a backend capability) — can the user easily challenge, fix, or escalate when the AI is wrong?", 'looking_for': "Tests the human-boundary-in-the-UI (creator->editor). Strong: an obvious in-product correct/override/escalate path. Weak: the user can't easily contest a wrong answer."}, {'q': 'Does the team MEASURE and improve interaction quality over time (trust calibration, override/abandonment rates, in-UI task success), or is UX a one-time build?', 'looking_for': 'Tests UX-as-managed-asset. Strong: interaction metrics tracked and the UX iterated. Weak: shipped once, never measured.'}]

## Relationships (incoming)

- [Dimension 6: Agentic Workflow Redesign & Human-AI Pairing](./dim__6.md) → has_criterion
- [UX of AI](./craft__ux_of_ai.md) → supports_craft

## Sources

- dimensions.json
