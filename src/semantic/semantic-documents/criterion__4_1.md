---
id: criterion.4_1
type: Criterion
label: "4.1 Use-Case Selection & Pattern Fit"
aliases: ["4.1", "Use-Case Selection & Pattern Fit"]
tags: ["criterion", "dim-4"]
keywords: ["criterion", "dim-4", "fit", "pattern", "selection", "use-case"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__4_1.md
---

# 4.1 Use-Case Selection & Pattern Fit  ·  _Criterion_

Not every process needs an agent; pattern over-reach is a top cause of cost and failure.

**Key facts:** dimension=4; criterion_id=4.1; anchors={'L1': "'Everything is an agent'; no decision framework", 'L2': 'Some screening; pattern chosen ad-hoc', 'L3': 'Decision framework applied (intelligence vs reliability; agent-or-not); simplest pattern matched', 'L4': 'Pattern fit governs the portfolio; deterministic/human-in-loop chosen where right', 'L5': 'Disciplined pattern selection org-wide; the agent is what remains after deterministic extraction'}; probing_questions=[{'q': "For each candidate, do you ask 'does this need intelligence or reliability?' and 'does this need to be an agent at all?' before building?", 'looking_for': "Tests the decision discipline. Strong: an explicit decision framework; deterministic workflow / human-in-loop are valid outcomes. Weak: 'everything is an agent' → wrong tool, cost, failure."}, {'q': 'Can you prove the required accuracy with evaluation data, and are errors recoverable and detectable?', 'looking_for': 'Tests fitness-for-agent. Strong: accuracy provable, errors recoverable/detectable. Weak: unprovable accuracy or undetectable high-impact errors → should not be an autonomous agent.'}, {'q': "Do you match the simplest pattern (LLM-as-function -> single -> hybrid -> subagent -> multi), or default to 'an agent' / 'multi-agent'?", 'looking_for': 'Guards against pattern over-reach. Strong: simplest pattern that works. Weak: multi-agent by default → cost, coordination failure.'}, {'q': 'Are deterministic workflow and human-in-loop assistant treated as valid (often preferred) outcomes?', 'looking_for': 'Tests honesty about where AI fits. Strong: yes, and chosen often. Weak: agents forced onto deterministic work → fragility dressed up as autonomy.'}].

**Connected to:** Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy) → has_criterion; 5.3 Governed Use-Case & PoC Intake → cross_references; Problem-First Scoping → supports_craft; The Agent Spectrum & the 90% Rule → supports_craft; Augmentation-First → references_criterion; Agent → references_criterion; The 90% Rule → references_criterion; Use-Case Intake → references_criterion.

**Sourced from:** dimensions.json.
