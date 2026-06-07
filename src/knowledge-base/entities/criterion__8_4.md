---
id: criterion.8_4
type: Criterion
label: "8.4 Observability, Audit Trails & Detection"
aliases: ["8.4", "Observability, Audit Trails & Detection"]
tags: ["criterion", "dim-8"]
sources: ["dimensions.json"]
---

# 8.4 Observability, Audit Trails & Detection

**Type:** Criterion  ·  **ID:** `criterion.8_4`

**Also known as:** 8.4, Observability, Audit Trails & Detection

The breach happens inside, invisibly; provable actions need tamper-evident logs.

## Attributes

- **dimension:** 8
- **criterion_id:** 8.4
- **anchors:** {'L1': 'Little/no agent logging', 'L2': 'Basic logs; gaps in agent-to-agent', 'L3': 'Tamper-evident trails for priority agents; traceable actions', 'L4': 'Anomaly/rogue-agent detection; agentic security monitoring fleet-wide', 'L5': 'Provable, tamper-evident audit + real-time detection across the fleet'}
- **probing_questions:** [{'q': "Are all agent actions and agent-to-agent data exchanges logged with tamper-evident trails (no 'invisible breach')?", 'looking_for': 'Tests auditability. Strong: tamper-evident, complete logs incl. agent-to-agent. Weak: gaps → invisible breaches.'}, {'q': 'Does the team detect anomalies/abuse and rogue-agent behavior in agentic workloads?', 'looking_for': 'Tests detection. Strong: anomaly/rogue-agent detection. Weak: no detection → compromise undetected.'}, {'q': 'Can every agent action be traced to the identity and intent it acted under?', 'looking_for': 'Tests traceability. Strong: full action-to-identity/intent traceability. Weak: untraceable actions.'}, {'q': 'Is security monitoring built for agentic workloads, not just generic appsec?', 'looking_for': 'Tests fit-for-agent monitoring. Strong: agentic security monitoring. Weak: generic appsec only.'}]

## Relationships (incoming)

- [Dimension 8: Security & Risk](./dim__8.md) → has_criterion

## Sources

- dimensions.json
