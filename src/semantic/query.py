# -*- coding: utf-8 -*-
"""Temporality-aware entity & relationship query over the Optimus knowledge graph.

Complements search.py (which does keyword/passage recall). This tool answers from the
*current* state by default — superseded facts are hidden unless you ask for history or a
point-in-time slice — so you never get a stalled answer. Every fact is reported with its
status and date.

Usage:
    python query.py "value delivery office"        # current state + provenance + relations
    python query.py "igm technology" --rel led_by  # filter to one relationship
    python query.py "igm technology" --history     # include superseded predecessors
    python query.py "igm technology" --as-of 2026-03-15   # valid-time slice
    python query.py --stale                         # audit: list all superseded facts

Exit notes: dates are ISO YYYY-MM-DD. A node with no temporal fields is treated as
status:current and always-valid (legacy data stays answerable).
"""
import os, re, json, sys
from collections import Counter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(HERE, "knowledge-graph.json"), encoding="utf-8"))
NODES = {n["id"]: n for n in G["nodes"]}
EDGES = G["edges"]

STOP = set("a an the of to in on for and or with by as at is are be this that those it its from "
           "into within across each per via not no only etc vs they their our we you".split())


def tok(t):
    return [w for w in re.findall(r"[a-z][a-z0-9&/+\-]{1,}", t.lower())
            if w not in STOP and len(w) > 1]


def status(n):
    return n.get("status", "current")


def is_current(n):
    return status(n) == "current"


def valid_on(n, date):
    """Is node n's fact valid on ISO `date`? Undated facts are always valid."""
    vf = n.get("valid_from")
    vt = n.get("valid_to")
    if vf and date < vf:
        return False
    if vt and date >= vt:
        return False
    return True


def resolve(term, prefer_current=True):
    """Return (best_id, alternates[]) for a free-text term."""
    if term in NODES:
        return term, []
    tl = term.lower()
    qset = set(tok(term))
    scored = []
    for nid, n in NODES.items():
        if n.get("_roster"):  # roster people are many; only match them on strong hits
            pass
        hay = " ".join([n["label"]] + n.get("aliases", []) + n.get("tags", [])).lower()
        s = 0
        if tl == n["label"].lower() or any(tl == a.lower() for a in n.get("aliases", [])):
            s += 10
        elif tl in n["label"].lower() or any(tl in a.lower() for a in n.get("aliases", [])):
            s += 5
        s += len(qset & set(tok(hay)))
        if prefer_current and is_current(n):
            s += 0.5
        if s:
            scored.append((s, nid))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        return None, []
    return scored[0][1], [i for _, i in scored[1:6]]


def prov_line(n):
    bits = [f"status={status(n)}"]
    for k in ("as_of", "valid_from", "valid_to", "source_doc"):
        if n.get(k):
            bits.append(f"{k}={n[k]}")
    return "  ·  ".join(bits)


def show_entity(nid, history=False, rel_filter=None, as_of=None):
    n = NODES[nid]
    print(f"\n=== {n['label']}  [{n['type']}]  ({nid}) ===")

    # staleness guard: if the user landed on a superseded node, steer to the current one
    if status(n) == "superseded" and not history and not as_of:
        sb = n.get("superseded_by")
        if sb and sb in NODES:
            print(f"⚠️  This fact is SUPERSEDED (valid_to={n.get('valid_to','?')}). "
                  f"Current version → {NODES[sb]['label']} ({sb}). Showing the current one.\n")
            return show_entity(sb, history, rel_filter, as_of)
        print(f"⚠️  This fact is SUPERSEDED and has no recorded successor.")

    print(prov_line(n))
    if n.get("aliases"):
        print("aka: " + ", ".join(n["aliases"]))
    if n.get("summary"):
        print("\n" + n["summary"])
    attrs = n.get("attributes") or {}
    if attrs:
        print("\nAttributes:")
        for k, v in attrs.items():
            if v not in (None, ""):
                print(f"  - {k}: {v}")

    # relationships (current-only unless --history / --as-of)
    def edge_ok(e):
        if rel_filter and e["rel"] != rel_filter:
            return False
        if e.get("status") == "superseded" and not history:
            return False
        return True

    def node_ok(i):
        m = NODES.get(i)
        if not m:
            return True
        if as_of is not None:
            return valid_on(m, as_of)
        if not history and status(m) == "superseded":
            return False
        return True

    out = [(e["rel"], e["to"]) for e in EDGES if e["from"] == nid and edge_ok(e) and node_ok(e["to"])]
    inc = [(e["rel"], e["from"]) for e in EDGES if e["to"] == nid and edge_ok(e) and node_ok(e["from"])]
    if out:
        print("\nRelationships (outgoing):")
        for rel, tgt in out[:40]:
            m = NODES.get(tgt)
            flag = "" if (not m or is_current(m)) else f"  [{status(m)}]"
            print(f"  {rel} → {m['label'] if m else tgt}{flag}")
    if inc:
        print("\nRelationships (incoming):")
        for rel, src in inc[:40]:
            m = NODES.get(src)
            flag = "" if (not m or is_current(m)) else f"  [{status(m)}]"
            print(f"  {m['label'] if m else src}{flag} → {rel}")

    # history chain
    if history:
        preds = [i for i in (n.get("supersedes") if isinstance(n.get("supersedes"), list)
                             else ([n["supersedes"]] if n.get("supersedes") else []))]
        # also nodes that point here via superseded_by
        preds += [i for i, m in NODES.items() if m.get("superseded_by") == nid]
        preds = [p for p in dict.fromkeys(preds) if p in NODES]
        if preds:
            print("\nHistory (superseded predecessors):")
            for p in preds:
                m = NODES[p]
                pa = m.get("attributes") or {}
                av = "; ".join(f"{k}={v}" for k, v in pa.items()) if pa else m.get("summary", "")[:80]
                print(f"  - {m['label']} ({p})  valid {m.get('valid_from','?')}→{m.get('valid_to','?')}  {av}")

    if n.get("sources"):
        print("\nSources: " + ", ".join(n["sources"]))
    print()


def show_stale():
    sup = [n for n in NODES.values() if status(n) == "superseded"]
    prop = [n for n in NODES.values() if status(n) == "proposed"]
    print(f"\nGraph status_counts: {G['meta'].get('status_counts', {'current': len(NODES)})}")
    print(f"\nSuperseded facts ({len(sup)}):")
    for n in sup:
        sb = n.get("superseded_by")
        print(f"  - {n['label']} ({n['id']})  valid_to={n.get('valid_to','?')}  → {sb or '?'}")
    if prop:
        print(f"\nProposed (not yet confirmed) ({len(prop)}):")
        for n in prop:
            print(f"  - {n['label']} ({n['id']})")
    if not sup and not prop:
        print("  (none — every fact is current)")
    print()


def main():
    args = sys.argv[1:]
    history = "--history" in args
    if history:
        args.remove("--history")
    if "--stale" in args:
        show_stale()
        return
    rel = None
    if "--rel" in args:
        i = args.index("--rel"); rel = args[i + 1]; del args[i:i + 2]
    as_of = None
    if "--as-of" in args:
        i = args.index("--as-of"); as_of = args[i + 1]; del args[i:i + 2]
    term = " ".join(args).strip()
    if not term:
        print(__doc__); return
    nid, alts = resolve(term, prefer_current=(as_of is None))
    if not nid:
        print(f"No entity matched '{term}'. Try search.py for passages, or --stale.")
        return
    show_entity(nid, history=history, rel_filter=rel, as_of=as_of)
    if alts:
        print("Other matches: " + ", ".join(f"{NODES[a]['label']} ({a})" for a in alts))


if __name__ == "__main__":
    main()
