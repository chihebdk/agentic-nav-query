---
id: criterion.4_1
type: Criterion
label: "4.1 Use-Case Selection & Pattern Fit"
aliases: ["4.1", "Use-Case Selection & Pattern Fit"]
tags: ["criterion", "dim-4"]
sources: ["dimensions.json"]
---

# 4.1 Use-Case Selection & Pattern Fit

**Type:** Criterion  ·  **ID:** `criterion.4_1`

**Also known as:** 4.1, Use-Case Selection & Pattern Fit

Not every process needs an agent; pattern over-reach is a top cause of cost and failure.

## Attributes

- **dimension:** 4
- **criterion_id:** 4.1
- **anchors:** {'L1': "'Everything is an agent'; no decision framework", 'L2': 'Some screening; pattern chosen ad-hoc', 'L3': 'Decision framework applied (intelligence vs reliability; agent-or-not); simplest pattern matched', 'L4': 'Pattern fit governs the portfolio; deterministic/human-in-loop chosen where right', 'L5': 'Disciplined pattern selection org-wide; the agent is what remains after deterministic extraction'}
- **probing_questions:** [{'q': "For each candidate, do you ask 'does this need intelligence or reliability?' and 'does this need to be an agent at all?' before building?", 'looking_for': "Tests the decision discipline. Strong: an explicit decision framework; deterministic workflow / human-in-loop are valid outcomes. Weak: 'everything is an agent' → wrong tool, cost, failure."}, {'q': 'Can you prove the required accuracy with evaluation data, and are errors recoverable and detectable?', 'looking_for': 'Tests fitness-for-agent. Strong: accuracy provable, errors recoverable/detectable. Weak: unprovable accuracy or undetectable high-impact errors → should not be an autonomous agent.'}, {'q': "Do you match the simplest pattern (LLM-as-function -> single -> hybrid -> subagent -> multi), or default to 'an agent' / 'multi-agent'?", 'looking_for': 'Guards against pattern over-reach. Strong: simplest pattern that works. Weak: multi-agent by default → cost, coordination failure.'}, {'q': 'Are deterministic workflow and human-in-loop assistant treated as valid (often preferred) outcomes?', 'looking_for': 'Tests honesty about where AI fits. Strong: yes, and chosen often. Weak: agents forced onto deterministic work → fragility dressed up as autonomy.'}]

## Relationships (incoming)

- [Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy)](./dim__4.md) → has_criterion
- [5.3 Governed Use-Case & PoC Intake](./criterion__5_3.md) → cross_references
- [Problem-First Scoping](./craft__problem_first_scoping.md) → supports_craft
- [The Agent Spectrum & the 90% Rule](./craft__the_agent_spectrum_the_90_rule.md) → supports_craft
- [Augmentation-First](./concept__augmentation_first.md) → references_criterion
- [Agent](./concept__agent.md) → references_criterion
- [The 90% Rule](./concept__the_90_rule.md) → references_criterion
- [Use-Case Intake](./template__use_case_intake.md) → references_criterion

## Sources

- dimensions.json
