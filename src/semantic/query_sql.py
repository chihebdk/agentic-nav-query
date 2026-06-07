# -*- coding: utf-8 -*-
"""Indexed, temporality-aware query over semantic/optimus.db (built by pipeline/build_sqlite.py).

Same answers as query.py, but via SQLite indexes + FTS5 — no full-JSON parse, partial loads.
Current-only by default; --history / --as-of for the temporal trail; --search for passages.

    python query_sql.py "value delivery office"        # entity + provenance + relations
    python query_sql.py "igm technology" --rel led_by
    python query_sql.py "igm technology" --history
    python query_sql.py "igm technology" --as-of 2026-03-15
    python query_sql.py --search "how does the ABR allocate funding" -n 5
    python query_sql.py --stale
"""
import os, sys, json, sqlite3, re

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

DB = os.environ.get("OPTIMUS_DB") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "optimus.db")
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row


def fts_query(term):
    # quote each token so FTS5 treats punctuation/ids literally
    toks = re.findall(r"[A-Za-z0-9]+", term)
    return " OR ".join(f'"{t}"' for t in toks) if toks else '""'


def resolve(term, prefer_current=True):
    r = con.execute("SELECT id FROM nodes WHERE id=?", (term,)).fetchone()
    if r:
        return r["id"], []
    # exact label / alias (case-insensitive)
    rows = con.execute(
        "SELECT id FROM nodes WHERE label=? COLLATE NOCASE "
        "UNION SELECT node_id FROM aliases WHERE alias=? COLLATE NOCASE", (term, term)).fetchall()
    if rows:
        ids = [x[0] for x in rows]
        return ids[0], ids[1:6]
    # FTS ranked
    try:
        rows = con.execute(
            "SELECT f.id, n.status, bm25(node_fts) AS r FROM node_fts f "
            "JOIN nodes n ON n.id=f.id WHERE node_fts MATCH ? "
            "ORDER BY (CASE WHEN n.status='current' THEN 0 ELSE 1 END), r LIMIT 6",
            (fts_query(term),)).fetchall()
    except sqlite3.OperationalError:
        rows = []
    if not rows:
        return None, []
    return rows[0]["id"], [x["id"] for x in rows[1:]]


def node(nid):
    return con.execute("SELECT * FROM nodes WHERE id=?", (nid,)).fetchone()


def label(nid):
    r = con.execute("SELECT label FROM nodes WHERE id=?", (nid,)).fetchone()
    return r["label"] if r else nid


def valid_on(n, date):
    if n["valid_from"] and date < n["valid_from"]:
        return False
    if n["valid_to"] and date >= n["valid_to"]:
        return False
    return True


def show_entity(nid, history=False, rel=None, as_of=None):
    n = node(nid)
    print(f"\n=== {n['label']}  [{n['type']}]  ({nid}) ===")
    if n["status"] == "superseded" and not history and not as_of and n["superseded_by"]:
        sb = n["superseded_by"]
        if node(sb):
            print(f"⚠️  SUPERSEDED (valid_to={n['valid_to']}). Current → {label(sb)} ({sb}). Showing current.\n")
            return show_entity(sb, history, rel, as_of)
    prov = [f"status={n['status']}"]
    for k in ("as_of", "valid_from", "valid_to", "source_doc"):
        if n[k]:
            prov.append(f"{k}={n[k]}")
    print("  ·  ".join(prov))
    al = [r["alias"] for r in con.execute("SELECT alias FROM aliases WHERE node_id=?", (nid,))]
    if al:
        print("aka: " + ", ".join(dict.fromkeys(al)))
    if n["summary"]:
        print("\n" + n["summary"])
    attrs = json.loads(n["attributes"] or "{}")
    if attrs:
        print("\nAttributes:")
        for k, v in attrs.items():
            if v not in (None, "", [], {}):
                print(f"  - {k}: {v}")

    def keep(other_id):
        m = node(other_id)
        if not m:
            return True
        if as_of is not None:
            return valid_on(m, as_of)
        if not history and m["status"] == "superseded":
            return False
        return True

    relclause = " AND rel=?" if rel else ""
    args = [nid] + ([rel] if rel else [])
    out_rows = con.execute(f"SELECT rel,dst,status FROM edges WHERE src=?{relclause}", args).fetchall()
    inc_rows = con.execute(f"SELECT rel,src,status FROM edges WHERE dst=?{relclause}", args).fetchall()

    def edge_live(e):
        return history or as_of is not None or e["status"] != "superseded"

    out = [(e["rel"], e["dst"]) for e in out_rows if edge_live(e) and keep(e["dst"])]
    inc = [(e["rel"], e["src"]) for e in inc_rows if edge_live(e) and keep(e["src"])]
    if out:
        print("\nRelationships (outgoing):")
        for rl, tgt in out[:40]:
            m = node(tgt)
            flag = "" if (not m or m["status"] == "current") else f"  [{m['status']}]"
            print(f"  {rl} → {label(tgt)}{flag}")
    if inc:
        print("\nRelationships (incoming):")
        for rl, src in inc[:40]:
            m = node(src)
            flag = "" if (not m or m["status"] == "current") else f"  [{m['status']}]"
            print(f"  {label(src)}{flag} → {rl}")
    if history:
        preds = [r["id"] for r in con.execute("SELECT id FROM nodes WHERE superseded_by=?", (nid,))]
        if n["supersedes"]:
            sv = json.loads(n["supersedes"])
            preds += sv if isinstance(sv, list) else [sv]
        preds = [p for p in dict.fromkeys(preds) if node(p)]
        if preds:
            print("\nHistory (superseded predecessors):")
            for p in preds:
                m = node(p)
                print(f"  - {m['label']} ({p})  valid {m['valid_from']}→{m['valid_to']}")
    src = json.loads(n["sources"] or "[]")
    if src:
        print("\nSources: " + ", ".join(src))
    print()


def search(query, n=8):
    print(f"\n== Passage search: {query} ==\n")
    rows = con.execute(
        "SELECT path, title, bm25(docs_fts) AS r FROM docs_fts WHERE docs_fts MATCH ? "
        "ORDER BY r LIMIT ?", (fts_query(query), n)).fetchall()
    for r in rows:
        print(f"  {r['r']:.3f}  {r['title'][:58]:<58}  {r['path']}")
    print()


def stale():
    sc = con.execute("SELECT status, count(*) c FROM nodes GROUP BY status").fetchall()
    print("\nstatus_counts: " + ", ".join(f"{r['status']}={r['c']}" for r in sc))
    sup = con.execute("SELECT id,label,valid_to,superseded_by FROM nodes WHERE status='superseded'").fetchall()
    print(f"\nSuperseded ({len(sup)}):")
    for r in sup:
        print(f"  - {r['label']} ({r['id']})  valid_to={r['valid_to']} → {r['superseded_by'] or '?'}")
    if not sup:
        print("  (none — every fact is current)")
    print()


def main():
    args = sys.argv[1:]
    history = "--history" in args
    if history:
        args.remove("--history")
    if "--stale" in args:
        stale(); return
    n = 8
    if "-n" in args:
        i = args.index("-n"); n = int(args[i + 1]); del args[i:i + 2]
    if "--search" in args:
        args.remove("--search")
        search(" ".join(args).strip(), n); return
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
        print(f"No entity matched '{term}'. Try --search for passages, or --stale.")
        return
    show_entity(nid, history=history, rel=rel, as_of=as_of)
    if alts:
        print("Other matches: " + ", ".join(f"{label(a)} ({a})" for a in alts))


if __name__ == "__main__":
    main()
