---
id: criterion.3_4
type: Criterion
label: "3.4 Data Quality & Readiness"
aliases: ["3.4", "Data Quality & Readiness"]
tags: ["criterion", "dim-3"]
keywords: ["criterion", "data", "dim-3", "quality", "readiness"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__3_4.md
---

# 3.4 Data Quality & Readiness  ·  _Criterion_

'Relying on the knowledge source without governing its quality produces confident but unreliable systems.'

**Key facts:** dimension=3; criterion_id=3.4; anchors={'L1': 'Quality unmanaged; GIGO', 'L2': 'Quality checked ad-hoc', 'L3': 'Quality/freshness assured for priority sources; retrieval-ready', 'L4': 'Quality SLAs; low latency; structured/labeled at scale', 'L5': 'Continuous, automated quality + freshness; readiness by design'}; probing_questions=[{'q': 'What is the quality/freshness of the data agents rely on, and how is it assured?', 'looking_for': 'Tests quality assurance. Strong: assured quality/freshness. Weak: unmanaged → garbage-in at machine scale, hallucinations.'}, {'q': 'Is data appropriately structured/labeled for retrieval?', 'looking_for': 'Probes retrieval-readiness. Strong: structured/labeled/chunked for use. Weak: raw dumps → poor retrieval.'}, {'q': "What's the latency between source-of-truth and what the agent sees?", 'looking_for': 'Tests staleness risk. Strong: low, understood latency. Weak: unknown/high → agents act on stale data.'}, {'q': "Are you delaying value waiting for 'perfect' data you may not need?", 'looking_for': "Guards against the over-correction (availability has diminishing returns). Strong: pragmatic 'good-enough' threshold. Weak: endless cleanup before any value."}].

**Connected to:** Dimension 3: Data, Knowledge Sources & Retrieval → has_criterion; Retrieval Craft → supports_craft.

**Sourced from:** dimensions.json.
