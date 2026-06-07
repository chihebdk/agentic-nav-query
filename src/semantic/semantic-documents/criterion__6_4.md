---
id: criterion.6_4
type: Criterion
label: "6.4 Human-AI Pairing Mode & Its Control Mechanism"
aliases: ["6.4", "Human-AI Pairing Mode & Its Control Mechanism"]
tags: ["criterion", "dim-6"]
keywords: ["control", "criterion", "dim-6", "human-ai", "mechanism", "mode", "pairing"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__6_4.md
---

# 6.4 Human-AI Pairing Mode & Its Control Mechanism  ·  _Criterion_

Each mode has a different required control; choosing a mode without its mechanism is the common failure. (On-loop = real-time escalation; out-of-loop = after-the-fact review.)

**Key facts:** dimension=6; criterion_id=6.4; anchors={'L1': 'Mode chosen with no mechanism (e.g., out-of-loop, no after-the-fact check)', 'L2': 'Partial mechanisms', 'L3': 'Each mode has its required mechanism built (real-time escalation / after-the-fact sampling / skill-triggered augmentation)', 'L4': 'Mechanisms robust; user truly orchestrates via skills in-loop; escalation + post-hoc validation reliable', 'L5': 'Pairing mechanisms re-calibrated from usage; right mode + mechanism by design'}; probing_questions=[{'q': 'How mature is the team at selecting the pairing mode (in/on/out-of-loop) per agentic step AND building its required control mechanism — standardized, or case-by-case?', 'looking_for': 'Tests mode+mechanism maturity. Strong: a standard practice where each mode ships with its mechanism. Weak: mode labels chosen, mechanisms missing.'}, {'q': "For in-the-loop augmentation, how consistently does the team deliver skills the user can trigger and orchestrate the workflow through (vs. tools the user can't really drive)?", 'looking_for': "Tests augmentation maturity. Strong: skill-triggered, user-orchestrated augmentation as a norm. Weak: nominal 'augmentation' the user can't actually drive."}, {'q': 'For on-the-loop work (the agent acts autonomously under REAL-TIME human monitoring, with the ability to intervene), does the team have a standard, reusable escalation/intervention procedure (who/when/how) applied across builds?', 'looking_for': 'Tests supervised-autonomy maturity. On-the-loop = the human watches in real time and steps in on exceptions AS THEY HAPPEN. Strong: a reusable real-time escalation/intervention pattern. Weak: ad-hoc or absent.'}, {'q': 'For out-of-the-loop work (the agent runs fully autonomously with NO real-time oversight), does the team have an established AFTER-THE-FACT validation practice (scanning/sampling via tooling, audit/logs) plus an escalation path for cases the agent itself flags?', 'looking_for': 'Tests safe-autonomy maturity. Out-of-the-loop = no runtime oversight; control is after-the-fact. Strong: standard post-hoc sampling/scanning + escalation path. Weak: autonomy shipped with no after-the-fact check.'}].

**Connected to:** Dimension 6: Agentic Workflow Redesign & Human-AI Pairing → has_criterion.

**Sourced from:** dimensions.json.
