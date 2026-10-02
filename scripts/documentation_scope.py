#!/usr/bin/env python3
"""Keep the offline documentation mirror scoped to Strom and shared references."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


def is_gas(path: str, text: str = "") -> bool:
    if path in {"index.md", "prozesse.md", "nachschlagen.md"}:
        return True  # Mixed-industry landing pages; use /prozesse/strom.md instead.
    if "gas" in path.lower():
        return True
    return bool(re.search(r"(?:·|\|)\s*Gas\s*(?:·|\|)|\bsparte=[\"']Gas[\"']|(?:^|\n)\s*(?:#|>)?\s*GeLi Gas\b", text[:1200], re.I))


def filter_index(path: Path, excluded: set[str] | None = None) -> set[str]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, paths = [], set()
    for line in lines:
        if line.startswith("> Lokaler Strom-Ausschnitt") or line.startswith("> Alle 3893 Seiten") or line.startswith("> Die Prozesse der deutschen Marktkommunikation Strom und Gas") or line.startswith("Der Bestand umfasst 682 Rollensichten"):
            continue
        match = re.search(r"\]\((https://dokumentation\.macoapp\.de/[^)]+\.md)\)", line)
        if match:
            relative = unquote(urlsplit(match.group(1)).path.lstrip("/"))
            if is_gas(relative, line) or relative in (excluded or set()):
                continue
            paths.add(relative)
        kept.append(line)
    if kept and kept[0].startswith("# "):
        heading = kept.pop(0)
        while kept and not kept[0].strip():
            kept.pop(0)
        kept = [heading, "\n", "> Lokaler Strom-Ausschnitt der Conuti-Dokumentation; Gas-spezifische und gemischte Übersichtsseiten sind ausgeschlossen.\n", "\n"] + kept
    path.write_text("".join(kept), encoding="utf-8")
    return paths


def filter_legacy_index(path: Path, excluded: set[str] | None = None) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = []
    for line in lines:
        match = re.search(r"\]\((https://doc\.macoapp\.de/[^)]+\.md)\)", line)
        if match:
            relative = unquote(urlsplit(match.group(1)).path.rsplit("/", 1)[-1])
            if is_gas(relative, line) or relative in (excluded or set()):
                continue
        kept.append(line)
    path.write_text("".join(kept), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index-dir", type=Path)
    parser.add_argument("--mirror-dir", type=Path)
    parser.add_argument("--legacy-index", type=Path)
    parser.add_argument("--legacy-dir", type=Path)
    parser.add_argument("--index-file", type=Path, help="Filter a single new-site index in place")
    parser.add_argument("--prune", action="store_true")
    args = parser.parse_args()
    if args.legacy_index:
        excluded = set()
        if args.legacy_dir:
            for file in args.legacy_dir.glob("*.md"):
                if is_gas(file.name, file.read_text(encoding="utf-8", errors="replace")):
                    excluded.add(file.name)
                    file.unlink()
        filter_legacy_index(args.legacy_index, excluded)
        if excluded:
            print(f"Removed {len(excluded)} Gas-specific legacy pages")
        return
    if args.index_file:
        filter_index(args.index_file)
        return
    if not args.index_dir or not args.mirror_dir:
        parser.error("--index-dir and --mirror-dir are required for the new mirror")
    excluded = set()
    if args.prune:
        for file in args.mirror_dir.rglob("*.md"):
            relative = file.relative_to(args.mirror_dir).as_posix()
            if relative != "README.md" and is_gas(relative, file.read_text(encoding="utf-8", errors="replace")):
                excluded.add(relative)
    filter_index(args.index_dir / "llms.txt", excluded)
    paths = filter_index(args.index_dir / "llms-index.txt", excluded)
    if not paths:
        raise SystemExit("Filtered documentation index is empty; refusing to prune the mirror")
    removed = 0
    if args.prune:
        for file in args.mirror_dir.rglob("*.md"):
            relative = file.relative_to(args.mirror_dir).as_posix()
            if relative == "README.md":
                continue
            if relative not in paths:
                file.unlink()
                removed += 1
    print(f"Strom/shared pages: {len(paths)}; removed out-of-scope or stale mirror pages: {removed}")


if __name__ == "__main__":
    main()
