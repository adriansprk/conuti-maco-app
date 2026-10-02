#!/usr/bin/env python3
"""Build discovery indexes for the new mirror and the legacy supplement.

Indexes point to source pages; they do not infer process order or decisions.
"""

from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import urlsplit, unquote
from documentation_scope import is_gas

ROOT = Path(__file__).resolve().parents[1]
NEW = ROOT / "docs-offline"
OLD = ROOT / "docs-supplemental"
FULL_INDEX = ROOT / "docs/dokumentation/llms-index.txt"
OUT = ROOT / "docs/entry-points/PROCESS_GRAPH.json"
CHECK = "--check" in sys.argv[1:]


def write_json(path, data):
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if CHECK:
        if not path.is_file() or path.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"Stale index: {path.relative_to(ROOT)}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")


def key(value):
    value = value.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def ids(text, path):
    result = set(re.findall(r"PI_(\d{5})", text))
    result.update(re.findall(r"\[(\d{5})\]\([^)]*?/pruefi/", text))
    for match in re.finditer(r"\*\d+\s+Prüfi:\s*([\d,\s]+)", text):
        result.update(re.findall(r"\d{5}", match.group(1)))
    canonical = re.fullmatch(r"PI_(\d{5})\.md", Path(path).name)
    if canonical:
        result.add(canonical.group(1))
    return sorted(result)


def read_title(text, fallback):
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback


def page_metadata(path, text, source, url):
    version = re.search(r"/(202604|202610)/", path)
    role = re.search(r"^docs-offline/prozessdoku/\d{6}/([^/]+)/", path)
    if role:
        role_segment = role.group(1)
        perspective = role_segment.split("--", 1)[1] if "--" in role_segment else None
        role = role_segment.split("--", 1)[0]
    else:
        legacy_role = re.search(r"rolle-([a-z]+)", path, re.I)
        role = legacy_role.group(1).upper() if legacy_role else None
        perspective = None
    view = re.search(r"^#\s+.*?— Sicht\s+(\w+)", text, re.M)
    if view:
        perspective = view.group(1)
    kind = "process" if "/prozessdoku/" in path else "interface" if "/schnittstellen/" in path else "reference" if "/referenz/" in path else "supplement" if source == "supplemental" else "other"
    industry = "strom" if re.search(r"(?:·|\|)\s*Strom\s*(?:·|\|)", text[:1200], re.I) or kind == "process" else "shared"
    return {
        "path": path, "source": source, "url": url,
        "version": version.group(1) if version else None,
        "industry": industry, "role": role, "perspective": perspective, "kind": kind,
        "title": read_title(text, Path(path).stem),
        "has_mermaid": "```mermaid" in text,
        "has_svg": "<Systembild svg=" in text,
    }


def main():
    manifest = {}
    for line in FULL_INDEX.read_text(encoding="utf-8").splitlines():
        match = re.search(r"\]\((https://dokumentation\.macoapp\.de/[^)]+\.md)\)", line)
        if match:
            url = match.group(1)
            path = unquote(urlsplit(url).path.lstrip("/"))
            if not is_gas(path, line):
                manifest[path] = url

    missing = sorted(p for p in manifest if not (NEW / p).is_file())
    if missing:
        raise SystemExit(f"Missing {len(missing)} mirrored pages, first: {missing[0]}")
    write_json(NEW / "index.json", manifest)

    legacy_index = json.loads((OLD / "index.json").read_text(encoding="utf-8"))
    for url in re.findall(r"\]\((https://doc\.macoapp\.de/[^)]+\.md)\)", (OLD / "llm.txt").read_text(encoding="utf-8")):
        filename = unquote(urlsplit(url).path.rsplit("/", 1)[-1])
        legacy_index[filename] = url
    for page in OLD.glob("*.md"):
        legacy_index.setdefault(page.name, None)
    legacy_index = {name: url for name, url in legacy_index.items() if not is_gas(name, name)}
    write_json(OLD / "index.json", dict(sorted(legacy_index.items())))
    by_id = defaultdict(list)
    by_trigger = defaultdict(list)
    by_process = defaultdict(list)
    by_path = {}
    by_filename = defaultdict(list)
    counts = defaultdict(int)

    def add(path, url, source):
        text = (ROOT / path).read_text(encoding="utf-8", errors="replace")
        if is_gas(path, text):
            return
        info = page_metadata(path, text, source, url)
        by_path[path] = info
        by_filename[Path(path).name].append(info)
        counts[source] += 1
        for number in ids(text, path):
            by_id[number].append(info)
        for trigger in set(re.findall(r"\bSTART_[A-Z0-9_]+\b", text)):
            by_trigger[trigger].append(info)
        if info["kind"] == "process" or source == "supplemental" and info["has_mermaid"]:
            process_title = info["title"].split(" — Sicht ")[0]
            by_process[key(process_title)].append(info)

    for path, url in sorted(manifest.items()):
        add(f"docs-offline/{path}", url, "new")
    for filename, url in sorted(legacy_index.items()):
        path = OLD / filename
        if path.is_file() and path.suffix == ".md":
            add(f"docs-supplemental/{filename}", url, "supplemental")

    def rank(info):
        path = info["path"]
        canonical_pi = bool(re.search(r"/pruefi/[^/]+/PI_\d{5}\.md$", path))
        kind_rank = 0 if canonical_pi else {"process": 1, "interface": 2, "reference": 3, "supplement": 4}.get(info["kind"], 5)
        return (kind_rank, -int(info["version"] or 0), path)

    def compact(mapping):
        return {k: [x["path"] for x in sorted(v, key=lambda info: (
            0 if Path(info["path"]).name == f"PI_{k}.md" else 1, rank(info)))]
            for k, v in sorted(mapping.items())}

    def source_only(mapping, source):
        return {k: paths for k, paths in (
            (k, [info["path"] for info in sorted(v, key=lambda info: (
                0 if Path(info["path"]).name == f"PI_{k}.md" else 1, rank(info))) if info["source"] == source])
            for k, v in sorted(mapping.items())
        ) if paths}

    write_json(NEW / "enhanced-index.json", {
        "source": "https://dokumentation.macoapp.de/llms-index.txt",
        "industry": "strom",
        "by_bdew_id": source_only(by_id, "new"),
        "by_trigger": source_only(by_trigger, "new"),
        "by_process_name": source_only(by_process, "new"),
    })
    write_json(OLD / "enhanced-index.json", {
        "source": "https://doc.macoapp.de/llms.txt",
        "industry": "strom",
        "by_bdew_id": source_only(by_id, "supplemental"),
        "by_trigger": source_only(by_trigger, "supplemental"),
        "by_process_name": source_only(by_process, "supplemental"),
    })
    graph = {
        "version": "4.0.0-strom-source-index",
        "manifest_sha256": hashlib.sha256(FULL_INDEX.read_bytes()).hexdigest(),
        "description": "Strom source discovery only. Read the linked pages; do not infer process branches from SVG order.",
        "source_files": dict(counts),
        "indexes": {
            "by_bdew_id": compact(by_id),
            "by_trigger": compact(by_trigger),
            "by_process_name": compact(by_process),
            "by_path": by_path,
            "by_filename": compact(by_filename),
        },
        "processes": {},
        "business_scenarios": {},
        "ebd_reference": {},
    }
    write_json(OUT, graph)
    print(f"Indexed {counts['new']} new and {counts['supplemental']} supplemental Strom/shared pages")
    print(f"Prüfis: {len(by_id)}; triggers: {len(by_trigger)}; process names: {len(by_process)}")


if __name__ == "__main__":
    if sys.argv[1:] not in ([], ["--check"]):
        raise SystemExit("Usage: rebuild-documentation-indexes.py [--check]")
    main()
