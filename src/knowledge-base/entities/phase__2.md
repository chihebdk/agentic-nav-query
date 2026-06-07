---
id: phase.2
type: EngagementPhase
label: "Phase 2: Frame Interviews"
aliases: ["Phase 2", "Frame Interviews"]
tags: ["engagement-phase", "phase-2"]
sources: ["engagement-workflow.md"]
---

# Phase 2: Frame Interviews

**Type:** EngagementPhase  ·  **ID:** `phase.2`

**Also known as:** Phase 2, Frame Interviews

For each stakeholder role, generate an interview guide by selecting and tailoring probing questions from dimensions relevant to that role; sequence open→specific (funnel); add evidence prompts.

## Attributes

- **number:** 2
- **artifact:** Interview guides + tracker.
- **exit_check:** Guides ready for the planned interviews.
- **templates_used:** ['template.interview_guide']

## Relationships (outgoing)

- depends_on → [Phase 1: Scope & Plan](./phase__1.md)
- produces_artifact → [Interview Guide](./template__interview_guide.md)
- precedes → [Phase 3: Capture & Analyze](./phase__3.md)

## Relationships (incoming)

- [Phase 1: Scope & Plan](./phase__1.md) → precedes
- [Phase 3: Capture & Analyze](./phase__3.md) → depends_on
- [Interview Method](./method__interview_method.md) → applies_to_phase

## Sources

- engagement-workflow.md
