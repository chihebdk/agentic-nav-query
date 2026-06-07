---
id: criterion.8_7
type: Criterion
label: "8.7 AI Hygiene & Shadow-AI / Human-Trust Risk"
aliases: ["8.7", "AI Hygiene & Shadow-AI / Human-Trust Risk"]
tags: ["criterion", "dim-8"]
keywords: ["ai", "criterion", "dim-8", "human-trust", "hygiene", "risk", "shadow-ai"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__8_7.md
---

# 8.7 AI Hygiene & Shadow-AI / Human-Trust Risk  ·  _Criterion_

The greatest data risk is often inside the firewall; human-agent trust exploitation is a real agentic risk.

**Key facts:** dimension=8; criterion_id=8.7; anchors={'L1': 'No hygiene controls; shadow AI unmanaged', 'L2': 'Some policy/comms', 'L3': 'In-context controls + shadow-AI awareness', 'L4': 'AI-DLP + shadow-AI management; over-trust safeguards; hygiene enablement', 'L5': 'Hygiene engineered in; shadow AI controlled; human-trust risk actively managed'}; probing_questions=[{'q': 'Are there controls against data leakage via careless prompts to external/unsanctioned tools (in-context nudges, AI-DLP)?', 'looking_for': 'Tests inside-the-firewall risk. Strong: in-context controls + AI-DLP. Weak: sensitive data freely pasted into external tools.'}, {'q': 'Does the team detect and manage shadow AI (unsanctioned agents/tools)?', 'looking_for': 'Tests shadow-AI control. Strong: shadow-AI discovery/management. Weak: unsanctioned agents proliferate unseen.'}, {'q': 'Are people protected against human-agent trust exploitation (over-trusting confident-but-wrong agents)?', 'looking_for': 'Tests human-trust risk. Strong: safeguards + awareness against over-trust. Weak: people act on confident-but-wrong outputs.'}, {'q': 'Is AI-hygiene enablement in place (with Dim 7 training and Dim 3.6 data classification)?', 'looking_for': 'Tests hygiene enablement. Strong: hygiene training + data classification. Weak: none → repeated leakage.'}].

**Connected to:** cross_references → 3.6 Data Governance, Privacy & Rights for AI/Agent Use; Dimension 8: Security & Risk → has_criterion.

**Sourced from:** dimensions.json.
