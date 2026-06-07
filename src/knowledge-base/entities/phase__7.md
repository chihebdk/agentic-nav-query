---
id: phase.7
type: EngagementPhase
label: "Phase 7: Drive the First Waves"
aliases: ["Phase 7", "Drive the First Waves"]
tags: ["engagement-phase", "phase-7"]
sources: ["engagement-workflow.md"]
---

# Phase 7: Drive the First Waves

**Type:** EngagementPhase  ·  **ID:** `phase.7`

**Also known as:** Phase 7, Drive the First Waves

Run the cadence (weekly forum: demos, blockers, scale/kill); track metrics and value-driver trees; enforce stage-gates; generate next steps; iterate until first wave(s) clear acceptance.

## Attributes

- **number:** 7
- **artifact:** Next-steps memos + updated backlog/state.
- **exit_check:** First wave(s) complete; re-assess.
- **templates_used:** ['template.next_steps_memo']

## Relationships (outgoing)

- depends_on → [Phase 6: Roadmap & Client Backlog](./phase__6.md)
- produces_artifact → [Next Steps Memo](./template__next_steps_memo.md)
- precedes → [Phase 8: Deliverables & Readout](./phase__8.md)

## Relationships (incoming)

- [Phase 6: Roadmap & Client Backlog](./phase__6.md) → precedes
- [Phase 8: Deliverables & Readout](./phase__8.md) → depends_on

## Sources

- engagement-workflow.md
