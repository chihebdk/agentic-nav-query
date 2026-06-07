---
id: criterion.5_4
type: Criterion
label: "5.4 Reference Patterns & Architectural Governance by Agent Type/Autonomy"
aliases: ["5.4", "Reference Patterns & Architectural Governance by Agent Type/Autonomy"]
tags: ["criterion", "dim-5"]
keywords: ["agent", "architectural", "criterion", "dim-5", "governance", "patterns", "reference", "type/autonomy"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__5_4.md
---

# 5.4 Reference Patterns & Architectural Governance by Agent Type/Autonomy  ·  _Criterion_

Standardized patterns per type/autonomy make builds reliable and govern churn; fuzzy types cause misaligned builds.

**Key facts:** dimension=5; criterion_id=5.4; anchors={'L1': 'Every build improvises; types undefined', 'L2': 'Some informal patterns', 'L3': 'Documented patterns per type/autonomy; types clearly defined', 'L4': 'Architectural governance used; framework/runtime/harness decision guide; stable-vs-moving guidance', 'L5': 'Mature pattern catalog + lightweight governance; build-to-delete isolates churn from durable assets'}; probing_questions=[{'q': 'Do you have documented, standardized design patterns / reference architectures per agent type and autonomy level?', 'looking_for': 'Tests a pattern catalog. Strong: a maintained, used catalog. Weak: every build improvises architecture.'}, {'q': 'Are the agent types clearly defined (augmentation, AI assistant, task-based autonomous, in/on/out-of-loop, conversational, multi-turn conversational)?', 'looking_for': 'Tests shared vocabulary. Strong: clear definitions teams use. Weak: fuzzy/overloaded terms → misaligned builds.'}, {'q': 'Is there architectural governance (review against the patterns) used without becoming a bottleneck?', 'looking_for': 'Tests lightweight governance. Strong: used and proportionate. Weak: none, or a heavy gate everyone bypasses.'}, {'q': 'What dictates the choice of framework, runtime, and harness for a given agent — a documented decision guide or individual preference?', 'looking_for': 'Tests decision discipline. Strong: a decision guide tied to type/autonomy. Weak: per-person preference → fragmentation.'}, {'q': 'How do you guide teams to bet on STABLE components vs the fast-moving parts (models/frameworks change ~every 6 months)?', 'looking_for': 'Tests adaptability/build-to-delete. Strong: explicit stable-vs-moving guidance; durable assets isolated from churn. Weak: no guidance → rework every cycle.'}].

**Connected to:** Dimension 5: Agentic Platform & Control Plane (Operating Model) → has_criterion; Agent → references_criterion; Template vs Client Backlog → references_criterion; The Agent Spectrum & the 90% Rule → references_criterion.

**Sourced from:** dimensions.json.
