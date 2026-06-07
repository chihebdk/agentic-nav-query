---
id: criterion.9_2
type: Criterion
label: "9.2 Policy & Policy-as-Code"
aliases: ["9.2", "Policy & Policy-as-Code"]
tags: ["criterion", "dim-9"]
keywords: ["criterion", "dim-9", "policy", "policy-as-code"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__9_2.md
---

# 9.2 Policy & Policy-as-Code  ·  _Criterion_

Many 'judgment' rules simply aren't formalized; deterministic policy-as-code is testable, reproducible, and enforced pre-action.

**Key facts:** dimension=9; criterion_id=9.2; anchors={'L1': 'Policies on paper; unenforced', 'L2': 'Some policies; manual checks', 'L3': 'Hard/soft rules classified; some policy-as-code for priority agents', 'L4': 'Policy engine enforces executable rules pre-action; LLM-drafted, human-reviewed', 'L5': 'Max hard-rule coverage enforced pre-action; policy pipeline with regression tests'}; probing_questions=[{'q': 'Are AI/agent policies current and enforced (acceptable use, autonomy limits, data use)?', 'looking_for': 'Tests living policy. Strong: current, enforced policies. Weak: policies in PDFs nobody enforces.'}, {'q': 'Are rules classified hard (deterministic -> policy-as-code) vs soft (judgment -> human escalation), with max hard-rule coverage?', 'looking_for': "Tests rule formalization. Strong: hard rules codified; soft to humans. Weak: everything 'judgment', nothing enforceable."}, {'q': 'Is there a policy engine that evaluates agent actions against executable rules BEFORE they execute?', 'looking_for': 'Tests pre-action enforcement. Strong: a policy engine gates actions. Weak: rules checked after the fact, or not at all.'}, {'q': 'Are policies authored with LLM assistance at dev time but human-reviewed (not interpreted at runtime)?', 'looking_for': "Tests rule authoring discipline. Strong: LLM-drafted, human-approved, deterministic at runtime. Weak: runtime LLM 'interpretation' of policy."}].

**Connected to:** Dimension 9: Governance & Responsible AI → has_criterion; Role-Based Enablement → references_criterion.

**Sourced from:** dimensions.json.
