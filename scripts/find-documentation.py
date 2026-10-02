#!/usr/bin/env python3
"""Find Strom documentation with explicit format version and role filters."""

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/entry-points/PROCESS_GRAPH.json"


def key(value):
    value = value.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def search(graph, lookup, query, version, role, include_supplemental=False, perspective=None):
    indexes = graph["indexes"]
    paths = indexes[lookup].get(key(query) if lookup == "by_process_name" else query, [])
    results = []
    for path in paths:
        info = indexes["by_path"][path]
        if info.get("industry") not in {"strom", "shared"}:
            continue
        if info["source"] == "supplemental":
            if not include_supplemental:
                continue
        elif info["version"] != version:
            continue
        if info["kind"] == "process" and role and info.get("role") != role:
            continue
        if info["kind"] == "process" and perspective and info.get("perspective") != perspective:
            continue
        results.append(info)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    query = parser.add_mutually_exclusive_group(required=True)
    query.add_argument("--pi")
    query.add_argument("--process")
    query.add_argument("--trigger")
    parser.add_argument("--version", required=True, choices=("202604", "202610"))
    parser.add_argument("--role", default="LF", help="Process perspective; default LF. Use another role explicitly when needed.")
    parser.add_argument("--perspective", help="Optional participant view such as LFN or LFA")
    parser.add_argument("--include-supplemental", action="store_true")
    args = parser.parse_args()
    lookup = "by_bdew_id" if args.pi else "by_process_name" if args.process else "by_trigger"
    value = args.pi or args.process or args.trigger
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    results = search(graph, lookup, value, args.version, args.role.upper(), args.include_supplemental,
                     args.perspective.upper() if args.perspective else None)
    print(json.dumps({"query": value, "version": args.version, "role": args.role.upper(),
                      "perspective": args.perspective.upper() if args.perspective else None,
                      "industry": "strom", "results": results}, ensure_ascii=False, indent=2))
    return 0 if results else 1


if __name__ == "__main__":
    sys.exit(main())
