---
id: criterion.8_1
type: Criterion
label: "8.1 Agentic Threat Model & Coverage"
aliases: ["8.1", "Agentic Threat Model & Coverage"]
tags: ["criterion", "dim-8"]
sources: ["dimensions.json"]
---

# 8.1 Agentic Threat Model & Coverage

**Type:** Criterion  ·  **ID:** `criterion.8_1`

**Also known as:** 8.1, Agentic Threat Model & Coverage

Agentic risk is categorically different; standard appsec misses it; a minor flaw cascades via autonomy.

## Attributes

- **dimension:** 8
- **criterion_id:** 8.1
- **anchors:** {'L1': 'Traditional appsec only; no agent threat model', 'L2': 'Awareness; partial coverage', 'L3': 'Agentic threat model applied; core risks covered', 'L4': 'Full agentic risk set + cascade/blast-radius thinking; updated regularly', 'L5': 'Threat model engineered into builds; continuously updated against new exploits'}
- **probing_questions:** [{'q': 'Does the team maintain an agentic threat model (e.g., OWASP Top 10 for Agentic Apps) distinct from traditional appsec/LLM security, applied as standard?', 'looking_for': 'Tests agent-specific threat awareness. Strong: a maintained agentic threat model used in builds. Weak: only traditional appsec → agent-specific risks missed.'}, {'q': 'Does it cover the agent-specific risks (goal hijacking, tool misuse, identity/privilege abuse, memory poisoning, inter-agent comms, cascading failures, rogue agents)?', 'looking_for': 'Tests coverage. Strong: the full agentic risk set. Weak: only prompt injection, or partial.'}, {'q': "Does the team account for the 'progressive breach' — a minor flaw cascading via autonomy into system-wide compromise?", 'looking_for': 'Tests the cascade insight. Strong: blast-radius/cascade thinking. Weak: treats each flaw as isolated.'}, {'q': 'Is the threat model updated as new agentic exploits emerge?', 'looking_for': 'Tests currency. Strong: regularly updated. Weak: static/one-time.'}]

## Relationships (incoming)

- [Dimension 8: Security & Risk](./dim__8.md) → has_criterion
- [Agentic Threat Model](./template__agentic_threat_model.md) → references_criterion

## Sources

- dimensions.json
