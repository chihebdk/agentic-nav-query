---
id: criterion.4_6
type: Criterion
label: "4.6 AgentOps: Observability, Reliability, Cost & Trajectory Capture"
aliases: ["4.6", "AgentOps: Observability, Reliability, Cost & Trajectory Capture"]
tags: ["criterion", "dim-4"]
keywords: ["agentops", "capture", "cost", "criterion", "dim-4", "observability", "reliability", "trajectory"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__4_6.md
---

# 4.6 AgentOps: Observability, Reliability, Cost & Trajectory Capture  ·  _Criterion_

Agents fail invisibly; unconstrained loops/fleets and cost are production risks; trajectories are the improvement dataset.

**Key facts:** dimension=4; criterion_id=4.6; anchors={'L1': 'Flying blind; no tracing/controls', 'L2': 'Basic logging', 'L3': 'Structured tracing + basic reliability for priority agents', 'L4': 'Full tracing across handoffs; circuit breakers/loop guards/fleet supervision; gateway cost control; drift detection', 'L5': 'Always-on observability + reliability + cost optimization; trajectories feed the flywheel'}; probing_questions=[{'q': 'Do you trace every model/tool/retrieval/reasoning step as structured spans across handoffs?', 'looking_for': 'Agents fail in ways that look like success. Strong: nested structured tracing. Weak: black-box → undetected failures.'}, {'q': 'Do you enforce circuit breakers, loop guards, iteration/token limits, and fleet supervision?', 'looking_for': 'Tests reliability controls. Strong: loops/fleets bounded and supervised. Weak: runaway loops/cost, no fleet view.'}, {'q': 'Do you track semantic SLIs and detect drift (action / policy / trigger / learning)?', 'looking_for': 'Tests behavioral monitoring. Strong: drift detected on baselines. Weak: only infra metrics → slow divergence unnoticed.'}, {'q': 'Is cost governed via a gateway, and are trajectories captured and fed back (link to Dim 2)?', 'looking_for': 'Tests cost control + the flywheel. Strong: central gateway + trajectory capture feeding improvement. Weak: fragmented cost, no trajectory data.'}].

**Connected to:** Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy) → has_criterion; Production Readiness → supports_craft; Agent → references_criterion; Evals & Guardrails → references_criterion; Observability Minimum → references_criterion; Production Readiness Checklist → references_criterion.

**Sourced from:** dimensions.json.
