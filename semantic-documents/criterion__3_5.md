---
id: criterion.3_5
type: Criterion
label: "3.5 Retrieval & Context Engineering (RAG, grounding)"
aliases: ["3.5", "Retrieval & Context Engineering (RAG, grounding)"]
tags: ["criterion", "dim-3"]
keywords: ["context", "criterion", "dim-3", "engineering", "grounding", "rag", "retrieval"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__3_5.md
---

# 3.5 Retrieval & Context Engineering (RAG, grounding)  ·  _Criterion_

The agent-specific core: a context-first architecture is what turns pilots into production.

**Key facts:** dimension=3; criterion_id=3.5; anchors={'L1': 'No retrieval; raw prompts', 'L2': 'Basic RAG; flat vector store, no eval', 'L3': 'Governed RAG over key sources', 'L4': 'Agentic RAG; domain-tuned embeddings; grounding measured', 'L5': 'Context-first architecture; knowledge graph + agentic RAG; grounding continuously optimized'}; probing_questions=[{'q': 'How do agents retrieve and assemble context (RAG, knowledge graph, embeddings)?', 'looking_for': 'Tests the agent-specific core. Strong: a deliberate retrieval architecture. Weak: raw prompts/no retrieval → ungrounded answers.'}, {'q': 'Is retrieval governed and evaluated, or a flat vector dump?', 'looking_for': 'Probes retrieval quality discipline. Strong: governed, measured retrieval (agentic RAG). Weak: flat vector store, no eval → confident but unreliable.'}, {'q': 'Do you tune embeddings/chunking for your domain?', 'looking_for': 'Tests precision of grounding. Strong: domain-tuned embeddings/chunking. Weak: generic defaults → poor recall/precision.'}, {'q': 'How do you measure and reduce hallucination/grounding failures?', 'looking_for': 'Tests whether grounding quality is managed. Strong: grounding metrics + remediation. Weak: no measurement → silent failures.'}].

**Connected to:** Dimension 3: Data, Knowledge Sources & Retrieval → has_criterion; Retrieval Craft → supports_craft.

**Sourced from:** dimensions.json.
