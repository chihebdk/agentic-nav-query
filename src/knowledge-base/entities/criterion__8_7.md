---
id: criterion.8_7
type: Criterion
label: "8.7 AI Hygiene & Shadow-AI / Human-Trust Risk"
aliases: ["8.7", "AI Hygiene & Shadow-AI / Human-Trust Risk"]
tags: ["criterion", "dim-8"]
sources: ["dimensions.json"]
---

# 8.7 AI Hygiene & Shadow-AI / Human-Trust Risk

**Type:** Criterion  ·  **ID:** `criterion.8_7`

**Also known as:** 8.7, AI Hygiene & Shadow-AI / Human-Trust Risk

The greatest data risk is often inside the firewall; human-agent trust exploitation is a real agentic risk.

## Attributes

- **dimension:** 8
- **criterion_id:** 8.7
- **anchors:** {'L1': 'No hygiene controls; shadow AI unmanaged', 'L2': 'Some policy/comms', 'L3': 'In-context controls + shadow-AI awareness', 'L4': 'AI-DLP + shadow-AI management; over-trust safeguards; hygiene enablement', 'L5': 'Hygiene engineered in; shadow AI controlled; human-trust risk actively managed'}
- **probing_questions:** [{'q': 'Are there controls against data leakage via careless prompts to external/unsanctioned tools (in-context nudges, AI-DLP)?', 'looking_for': 'Tests inside-the-firewall risk. Strong: in-context controls + AI-DLP. Weak: sensitive data freely pasted into external tools.'}, {'q': 'Does the team detect and manage shadow AI (unsanctioned agents/tools)?', 'looking_for': 'Tests shadow-AI control. Strong: shadow-AI discovery/management. Weak: unsanctioned agents proliferate unseen.'}, {'q': 'Are people protected against human-agent trust exploitation (over-trusting confident-but-wrong agents)?', 'looking_for': 'Tests human-trust risk. Strong: safeguards + awareness against over-trust. Weak: people act on confident-but-wrong outputs.'}, {'q': 'Is AI-hygiene enablement in place (with Dim 7 training and Dim 3.6 data classification)?', 'looking_for': 'Tests hygiene enablement. Strong: hygiene training + data classification. Weak: none → repeated leakage.'}]

## Relationships (outgoing)

- cross_references → [3.6 Data Governance, Privacy & Rights for AI/Agent Use](./criterion__3_6.md)

## Relationships (incoming)

- [Dimension 8: Security & Risk](./dim__8.md) → has_criterion

## Sources

- dimensions.json
