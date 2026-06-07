---
id: criterion.4_6
type: Criterion
label: "4.6 AgentOps: Observability, Reliability, Cost & Trajectory Capture"
aliases: ["4.6", "AgentOps: Observability, Reliability, Cost & Trajectory Capture"]
tags: ["criterion", "dim-4"]
sources: ["dimensions.json"]
---

# 4.6 AgentOps: Observability, Reliability, Cost & Trajectory Capture

**Type:** Criterion  ·  **ID:** `criterion.4_6`

**Also known as:** 4.6, AgentOps: Observability, Reliability, Cost & Trajectory Capture

Agents fail invisibly; unconstrained loops/fleets and cost are production risks; trajectories are the improvement dataset.

## Attributes

- **dimension:** 4
- **criterion_id:** 4.6
- **anchors:** {'L1': 'Flying blind; no tracing/controls', 'L2': 'Basic logging', 'L3': 'Structured tracing + basic reliability for priority agents', 'L4': 'Full tracing across handoffs; circuit breakers/loop guards/fleet supervision; gateway cost control; drift detection', 'L5': 'Always-on observability + reliability + cost optimization; trajectories feed the flywheel'}
- **probing_questions:** [{'q': 'Do you trace every model/tool/retrieval/reasoning step as structured spans across handoffs?', 'looking_for': 'Agents fail in ways that look like success. Strong: nested structured tracing. Weak: black-box → undetected failures.'}, {'q': 'Do you enforce circuit breakers, loop guards, iteration/token limits, and fleet supervision?', 'looking_for': 'Tests reliability controls. Strong: loops/fleets bounded and supervised. Weak: runaway loops/cost, no fleet view.'}, {'q': 'Do you track semantic SLIs and detect drift (action / policy / trigger / learning)?', 'looking_for': 'Tests behavioral monitoring. Strong: drift detected on baselines. Weak: only infra metrics → slow divergence unnoticed.'}, {'q': 'Is cost governed via a gateway, and are trajectories captured and fed back (link to Dim 2)?', 'looking_for': 'Tests cost control + the flywheel. Strong: central gateway + trajectory capture feeding improvement. Weak: fragmented cost, no trajectory data.'}]

## Relationships (incoming)

- [Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy)](./dim__4.md) → has_criterion
- [Production Readiness](./craft__production_readiness.md) → supports_craft
- [Agent](./concept__agent.md) → references_criterion
- [Evals & Guardrails](./craft__evals_guardrails.md) → references_criterion
- [Observability Minimum](./craft__observability_minimum.md) → references_criterion
- [Production Readiness Checklist](./template__production_readiness_checklist.md) → references_criterion

## Sources

- dimensions.json
