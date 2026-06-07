---
id: criterion.8_6
type: Criterion
label: "8.6 Incident Response, Containment & Resilience"
aliases: ["8.6", "Incident Response, Containment & Resilience"]
tags: ["criterion", "dim-8"]
keywords: ["containment", "criterion", "dim-8", "incident", "resilience", "response"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__8_6.md
---

# 8.6 Incident Response, Containment & Resilience  ·  _Criterion_

Unconstrained agents/loops are production risks; cascading failures must be contained and reversible.

**Key facts:** dimension=8; criterion_id=8.6; anchors={'L1': 'No kill-switch/IR for agents', 'L2': 'Some monitoring; manual response', 'L3': 'Circuit breakers/rollback for priority agents', 'L4': 'Three lines of defense; kill-switches standard; agentic IR playbook', 'L5': 'Automated containment + blast-radius limits; rehearsed agentic IR; fast recovery'}; probing_questions=[{'q': 'Are three lines of defense in place (pre-deploy gates, runtime enforcement, production monitoring)?', 'looking_for': 'Tests defense-in-depth. Strong: all three lines. Weak: missing a line → blind spot.'}, {'q': 'Are circuit breakers, loop guards, kill-switches, and rollback standard for agents?', 'looking_for': 'Tests containment controls. Strong: standard kill-switch/rollback. Weak: no way to halt a runaway agent.'}, {'q': 'Is there an agentic incident-response playbook (detect -> contain -> recover -> blameless postmortem) for agent-specific failures?', 'looking_for': 'Tests IR readiness. Strong: an agentic IR playbook. Weak: generic IR or none.'}, {'q': 'Does the team contain cascading / inter-agent failures (blast-radius limits)?', 'looking_for': 'Tests cascade containment. Strong: blast-radius limits. Weak: one failure cascades across the fleet.'}].

**Connected to:** Dimension 8: Security & Risk → has_criterion; Production Readiness → references_criterion; Observability Minimum → references_criterion.

**Sourced from:** dimensions.json.
