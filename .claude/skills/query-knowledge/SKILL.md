---
name: query-knowledge
description: >-
  Answer questions and generate insight from the Agentic Transformation Navigator knowledge base
  (graph, ontology, semantic layer, knowledge base) with temporal correctness — current state only,
  dated and cited, so you never get a stalled answer. Use whenever the user asks about dimensions,
  criteria, maturity levels, engagement phases, craft guides, templates, or transformation concepts.
  By default answers use only status:current facts; superseded facts appear only when the user asks
  for history or "as of <date>". The read-side counterpart to ingest-document.
---

# Query the knowledge base (time-aware)

Answer from the **current** state of the knowledge graph, always **dated and cited**, and
frame the **insight** — not just the raw fact. Superseded facts are history: never present
them as current. This skill is read-only; it changes nothing.

Paths are relative to the workspace root. Tools (dependency-free, run from `src/semantic/`):

- **`query.py`** — temporality-aware entity & relationship lookup. Current-only by default.
  `python query.py "<term>"` · `--rel <relation>` · `--history` · `--as-of YYYY-MM-DD` · `--stale`
- **`search.py`** — TF-IDF passage recall + entity resolution across the whole corpus.
  `python search.py "<question>"` · `--entity "<term>"` · `-n <k>`
- The graph itself (`semantic/knowledge-graph.json`), entity pages
  (`knowledge-base/entities/*.md`), thematic notes (`knowledge-base/0X-*.md`), and the
  ontology (`ontology/ontology.md`) for what the relationship/types *mean*.

## Method

1. **Resolve.** Turn the question into entities and/or topics. Use `query.py "<term>"` to pin
   the entity (it returns the best match + alternates) and `search.py` for passage recall when
   the question is thematic ("how does the autonomy gate work").
2. **Retrieve — current only.** Read facts from `query.py` (which already filters to
   `status:current` and traverses relationships). For multi-hop questions, follow the edges it
   prints (the ontology names what each relation means). Cross-check narrative in the relevant
   `knowledge-base/` note.
3. **Check temporality before answering:**
   - If the resolving fact is **superseded**, `query.py` auto-steers to the current successor —
     answer from that, and only mention the old value if the user asked for history.
   - If a fact carries an `as_of` / `valid_from`, **state it**.
   - If a fact has **no date** (legacy), treat it as current but say it's undated if precision
     matters.
   - Run `query.py --stale` if you need to know what's been superseded recently.
4. **Answer** concisely and **cite**: entity id(s) + the `sources` / `source_doc`.
5. **Frame the insight** (this is the point, not an extra): after the direct answer, add
   - **So what** — what the answer implies (a gap, a risk, a dependency).
   - **Action** — what the user could decide or do, if anything.
   - **Open** — what the KB does *not* answer here (missing data, undated fact).
     Never bluff: if the graph doesn't know, say so.

## History & point-in-time (only when asked)

- "what did we believe before / what changed" → `query.py "<term>" --history` (shows the
  superseded predecessors with their date ranges).
- "as of <date>" → `query.py "<term>" --as-of <date>` (valid-time slice).

## Performance & model

This is a retrieve-summarize-cite flow — the graph does the heavy lifting, so it runs well on
a **faster model**. Prefer **Sonnet** for everyday Q&A and **Haiku** for pure fact lookups;
reserve Opus for reasoning-heavy tasks. Keep latency down by **using the warm `agentic-nav-kg`
MCP tools** (loaded once) instead of spawning `query.py` per call. Batch related lookups into
one call to cut round-trips.

## Guardrails

- **Current-by-default.** Do not surface `superseded` or `proposed` facts as if current.
- **Always date & cite.** An undated, uncited number is not an answer here.
- **Distinguish stated vs inferred.** Don't upgrade an inference to a fact.
- **Read-only.** If the user wants to *change* the knowledge, hand off to the ingest side.
- **Don't invent edges.** If two entities aren't connected in the graph, say the link is
  unstated rather than asserting it.
