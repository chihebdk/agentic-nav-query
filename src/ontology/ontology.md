# Agentic Transformation Navigator — Ontology

A lightweight domain ontology (OWL/RDFS-style) for the Agentic Transformation Navigator knowledge system. It defines the **classes** (entity types) and **object properties** (relationship types) used across the knowledge graph (`semantic/knowledge-graph.json`).

- **Namespace:** `https://agentic-nav.ravl.io/kg/` (prefix `atn:`)
- **Classes:** 9  ·  **Object properties:** 25  ·  **Temporal/provenance properties:** 7
- **Validated against graph:** 9 node types, 12 relationship types  (all mapped ✓)

## Classes

| Class | Description |
| --- | --- |
| `atn:Dimension` | One of the nine assessment dimensions — a major capability area scored in the maturity model (e.g., Strategy, Knowledge, Data, Build, Platform, Workflow, Workforce, Security, Governance). |
| `atn:Criterion` | A specific, scoreable criterion within a dimension (e.g., 1.1 AI Vision). Has L1-L5 maturity anchors and probing questions stored as attributes. |
| `atn:Chapter` | A playbook chapter — a narrative unit teaching one or more dimensions with recommendations, anti-patterns, case vignettes, and a backlog slice. |
| `atn:CraftGuide` | A deep how-to reference on a specific build or operations topic (e.g., evals-and-guardrails, retrieval-craft, production-readiness). |
| `atn:Template` | A reusable artifact template grounded in the methodology (e.g., backlog-story, roadmap-waves, threat-model, autonomy-gate-checklist). |
| `atn:EngagementPhase` | One of the 8 phases of the consulting engagement workflow (Scope, Frame, Capture, Synthesize, Gap, Roadmap, Drive, Deliver). |
| `atn:Method` | A consulting methodology or principle applied throughout the engagement (McKinsey method, interview method, analysis method, deliverable standards, diagram toolkit, state management). |
| `atn:Concept` | A named idea, principle, or construct in the transformation vocabulary (e.g., autonomy gate, build-to-delete, the 90% rule, knowledge moat, SCQA). |
| `atn:BuildingBlock` | One of the seven corrected Rewired building blocks in the narrative journey model that map to dimensions. |

## Object properties

| Property | Domain | Range | Inverse | Meaning |
| --- | --- | --- | --- | --- |
| `atn:has_criterion` | Dimension | Criterion | `criterion_of` | Dimension contains this criterion. |
| `atn:criterion_of` | Criterion | Dimension | `has_criterion` | Criterion belongs to this dimension. |
| `atn:covers_dimension` | Chapter | Dimension | `covered_by_chapter` | Chapter teaches or covers this dimension. |
| `atn:covered_by_chapter` | Dimension | Chapter | `covers_dimension` | Dimension is taught in this chapter. |
| `atn:references_criterion` | Chapter|CraftGuide|Template|Method | Criterion | `referenced_by` | Content references or supports this criterion. |
| `atn:referenced_by` | Criterion | Chapter|CraftGuide|Template|Method | `references_criterion` | Criterion is referenced by this content. |
| `atn:applies_to_phase` | Method|Template|CraftGuide | EngagementPhase | `uses_method` | Method/template/guide applies in this engagement phase. |
| `atn:uses_method` | EngagementPhase | Method|Template|CraftGuide | `applies_to_phase` | Phase uses this method, template, or guide. |
| `atn:produces_artifact` | EngagementPhase | Template | `produced_in_phase` | Phase produces artifacts using this template. |
| `atn:produced_in_phase` | Template | EngagementPhase | `produces_artifact` | Template is used/produced in this phase. |
| `atn:supports_craft` | CraftGuide | Criterion|Dimension | `supported_by_craft` | Craft guide supports these criteria or dimensions. |
| `atn:supported_by_craft` | Criterion|Dimension | CraftGuide | `supports_craft` | Criterion/dimension is supported by this craft guide. |
| `atn:depends_on` | EngagementPhase | EngagementPhase | — | Phase depends on prior phase completion. |
| `atn:precedes` | EngagementPhase|Chapter | EngagementPhase|Chapter | `follows` | Sequencing — this comes before. |
| `atn:follows` | EngagementPhase|Chapter | EngagementPhase|Chapter | `precedes` | Sequencing — this comes after. |
| `atn:maps_to_dimension` | BuildingBlock | Dimension | `mapped_from_block` | Building block maps to these dimensions. |
| `atn:mapped_from_block` | Dimension | BuildingBlock | `maps_to_dimension` | Dimension is mapped from this building block. |
| `atn:related_to` | Concept|CraftGuide|Template|Criterion|Dimension | Concept|CraftGuide|Template|Criterion|Dimension | — | Semantic link between knowledge items. |
| `atn:exemplifies` | Concept | Criterion|Dimension | `exemplified_by` | Concept exemplifies or is central to a criterion or dimension. |
| `atn:exemplified_by` | Criterion|Dimension | Concept | `exemplifies` | Criterion/dimension is exemplified by this concept. |
| `atn:uses_template` | CraftGuide|Method|EngagementPhase | Template | `used_by` | Guide/method/phase uses this template. |
| `atn:used_by` | Template | CraftGuide|Method|EngagementPhase | `uses_template` | Template is used by this guide/method/phase. |
| `atn:cross_references` | Criterion | Criterion | — | Criterion cross-references another (e.g., Dim 5.5 ties to Dim 8). |
| `atn:part_of` | Concept | Concept | `contains` | Concept is part of a larger concept. |
| `atn:contains` | Concept | Concept | `part_of` | Concept contains sub-concepts. |

## Temporal & provenance vocabulary

Optional annotation properties on **any** node or edge that capture *when* a fact was recorded, *when* it is valid, and *what it replaced* — so queries return the current state instead of stale answers while history stays auditable. See `pipeline/TEMPORAL_SCHEMA.md`. Backward-compatible: an item without them is `status: current`.

| Property | Kind | Meaning |
| --- | --- | --- |
| `atn:asOf` | date | When this fact was recorded/observed (transaction time). |
| `atn:validFrom` | date | When the fact became true in the world (valid time). |
| `atn:validTo` | date | When the fact stopped being true; absent = still holds. |
| `atn:status` | string | current | superseded | proposed. |
| `atn:supersedes` | ref | The entity/claim this fact replaces. |
| `atn:supersededBy` | ref | The newer fact that retired this one. |
| `atn:sourceDoc` | string | Slug of the document that introduced/changed this fact. |

## Design notes

- The ontology is intentionally **lightweight** (RDFS/OWL-lite): named classes, typed object properties with domain/range and selected inverses. It is meant for navigation, validation and retrieval — not heavy reasoning.
- **Instances** live in `semantic/knowledge-graph.json` (nodes) and `semantic/triples.nt` (RDF).
- Multi-valued domains/ranges are written `A|B` (union).
- The same vocabulary backs the per-entity pages in `knowledge-base/entities/` and the semantic documents in `semantic/semantic-documents/`.
- **Sessions & outcomes (events):** `Session` models a dated event (interview/workshop/meeting); it is `recorded_in` a `Document` and may be an `instance_of` a `GovernanceForum`. It `raised` `ActionItem`/`Decision`/`Question` outcomes. Interviews are also the source that populates each `Person`'s `powerMap` (stance/concerns/decision_rights/engagement_log).
- **`state` vs `status`:** `ActionItem`/`Question` carry a domain-lifecycle **`state`** (open|in_progress|blocked|done|cancelled|deferred / open|answered|obsolete) — this is the business state of the outcome and is **distinct** from the node-level temporal **`status`** (current|superseded|proposed) used for knowledge supersession. A resolved action item is `state:done` + `resolved_by` + `resolved_on`, while remaining `status:current`.
