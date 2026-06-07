---
id: criterion.5_8
type: Criterion
label: "5.8 Cross-Team Alignment (Governance, Data, Quality)"
aliases: ["5.8", "Cross-Team Alignment (Governance, Data, Quality)"]
tags: ["criterion", "dim-5"]
sources: ["dimensions.json"]
---

# 5.8 Cross-Team Alignment (Governance, Data, Quality)

**Type:** Criterion  ·  **ID:** `criterion.5_8`

**Also known as:** 5.8, Cross-Team Alignment (Governance, Data, Quality)

A platform misaligned with governance, data, and quality produces ungoverned, ungrounded, low-accuracy agents.

## Attributes

- **dimension:** 5
- **criterion_id:** 5.8
- **anchors:** {'L1': 'Platform siloed from governance/data/quality', 'L2': 'Ad-hoc coordination', 'L3': 'Regular alignment with governance and data', 'L4': 'Governance paved into the platform; data access joint; quality gating with accuracy improvement', 'L5': 'Shared roadmap/rhythms; governance, data and quality embedded in the platform by design'}
- **probing_questions:** [{'q': 'How aligned are the platform team and the governance body — are guardrails/policies built INTO the platform (paved), or bolted on later?', 'looking_for': 'Tests governance-by-design. Strong: governance embedded in the golden path. Weak: governance separate/after-the-fact → bypassed.'}, {'q': 'How aligned are the platform team and the data/document teams (the agentic platform needs governed data/document access)?', 'looking_for': "Tests platform<->data alignment (capability itself = Dim 3). Strong: joint ownership of knowledge access. Weak: siloed → agents can't reach data."}, {'q': 'Is there an evals/quality gating function, with an accuracy threshold and a continuous-improvement process tied to the platform?', 'looking_for': 'Tests quality as a platform function (eval practice = Dim 4.5). Strong: quality gating + accuracy improves over time through usage. Weak: no quality function → accuracy stagnates.'}, {'q': 'Do these teams share roadmap and operating rhythms, or operate independently?', 'looking_for': 'Tests operating-rhythm alignment. Strong: shared rhythms/roadmap. Weak: independent → drift and misalignment.'}]

## Relationships (outgoing)

- cross_references → [4.5 Evaluation & Quality (Evals)](./criterion__4_5.md)

## Relationships (incoming)

- [Dimension 5: Agentic Platform & Control Plane (Operating Model)](./dim__5.md) → has_criterion

## Sources

- dimensions.json
