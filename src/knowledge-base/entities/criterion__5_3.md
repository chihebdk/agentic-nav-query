---
id: criterion.5_3
type: Criterion
label: "5.3 Governed Use-Case & PoC Intake"
aliases: ["5.3", "Governed Use-Case & PoC Intake"]
tags: ["criterion", "dim-5"]
sources: ["dimensions.json"]
---

# 5.3 Governed Use-Case & PoC Intake

**Type:** Criterion  ·  **ID:** `criterion.5_3`

**Also known as:** 5.3, Governed Use-Case & PoC Intake

Ungoverned intake is the source of PoC sprawl; the gate enforces Dim 4.1/Dim 1 criteria.

## Attributes

- **dimension:** 5
- **criterion_id:** 5.3
- **anchors:** {'L1': 'PoCs start anywhere; nothing killed', 'L2': 'Informal review', 'L3': 'Managed gate applies agent-or-not & value criteria', 'L4': 'Autonomy level decided + validated at the gate; portfolio actively managed (kill/scale)', 'L5': 'Disciplined intake; no sprawl; gate prevents low-value builds'}
- **probing_questions:** [{'q': "How are candidate agent use cases intake'd and decided — a managed gate, or do PoCs start anywhere?", 'looking_for': 'Tests intake governance. Strong: a managed intake/gate. Weak: anyone starts a PoC → sprawl.'}, {'q': 'Does the gate apply the selection criteria (agent-or-not, business value, autonomy level) BEFORE work starts?', 'looking_for': 'Tests up-front rigor (criteria defined in Dim 4.1/Dim 1). Strong: criteria enforced at the gate. Weak: built first, justified later.'}, {'q': 'How do you prevent PoC sprawl — is the PoC portfolio actively managed, with kill/scale decisions?', 'looking_for': 'Tests portfolio discipline. Strong: managed portfolio, things get killed. Weak: PoCs accumulate, nothing killed.'}, {'q': 'Is the target autonomy level decided at the gate (via a quick validation PoC), or discovered later in dev/deploy?', 'looking_for': 'Tests when autonomy is decided. Strong: decided + validated at the gate. Weak: emerges late → rework, risk.'}]

## Relationships (outgoing)

- cross_references → [4.1 Use-Case Selection & Pattern Fit](./criterion__4_1.md)

## Relationships (incoming)

- [Dimension 5: Agentic Platform & Control Plane (Operating Model)](./dim__5.md) → has_criterion
- [9.6 Agent Registry, Intake & Lifecycle Governance](./criterion__9_6.md) → cross_references
- [Autonomy Gate](./concept__autonomy_gate.md) → references_criterion

## Sources

- dimensions.json
