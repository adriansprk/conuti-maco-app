#!/usr/bin/env python3
"""Regenerate ahb-tables/INDEX.json and INDEX.md from downloaded AHB files."""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
TARGET_DIR = REPO_ROOT / "ahb-tables"


def version_sort_key(fv: str) -> tuple[int, int]:
    match = re.fullmatch(r"FV(\d{2})(\d{2})", fv)
    if not match:
        return (0, 0)
    return (int(match.group(1)), int(match.group(2)))


def load_entry(path: Path, fv: str) -> dict | None:
    data = json.loads(path.read_text(encoding="utf-8"))
    meta = data.get("meta")
    if not isinstance(meta, dict):
        return None

    prufi = str(meta.get("pruefidentifikator") or path.stem.split("_")[-1])
    return {
        "pruefidentifikator": prufi,
        "description": meta.get("description", ""),
        "direction": meta.get("direction", ""),
        "versionsnummer": meta.get("versionsnummer", ""),
        "veroeffentlichungsdatum": meta.get("veroeffentlichungsdatum", ""),
        "lines_count": len(data.get("lines", [])),
    }


def discover_versions() -> list[str]:
    versions = [p.name for p in TARGET_DIR.iterdir() if p.is_dir() and p.name.startswith("FV")]
    return sorted(versions, key=version_sort_key)


def build_index() -> dict:
    versions = discover_versions()
    by_version: dict[str, list[dict]] = {}
    by_pruefidentifikator: dict[str, dict[str, dict]] = {}

    for fv in versions:
        entries: list[dict] = []
        for path in sorted((TARGET_DIR / fv).glob(f"AHB_{fv}_*.json")):
            entry = load_entry(path, fv)
            if entry is None:
                continue
            entries.append(entry)
            by_pruefidentifikator.setdefault(entry["pruefidentifikator"], {})[fv] = entry
        by_version[fv] = sorted(entries, key=lambda row: row["pruefidentifikator"])

    return {
        "description": (
            "AHB tables index - generated from ahb-tabellen.hochfrequenz.de (public API). "
            "Run scripts/download-ahb-tables.py to refresh."
        ),
        "source": "https://ahb-tabellen.hochfrequenz.de/api",
        "versions": versions,
        "by_version": by_version,
        "by_pruefidentifikator": by_pruefidentifikator,
    }


def truncate(text: str, width: int) -> str:
    text = text.replace("|", "/")
    if len(text) <= width:
        return text
    return text[: max(width - 1, 0)] + "…"


def render_markdown(index: dict) -> str:
    lines = [
        "# AHB Tables Index",
        "",
        "Anwendungshandbücher (AHB) for all BDEW Prüfidentifikatoren.",
        "Downloaded from [ahb-tabellen.hochfrequenz.de](https://ahb-tabellen.hochfrequenz.de) "
        "(public API, no auth required).",
        "",
        "**Refresh:** `python3 scripts/download-ahb-tables.py` then "
        "`python3 scripts/generate-ahb-index.py`",
        "",
        "## Available Versions",
        "",
    ]

    for fv in index["versions"]:
        count = len(index["by_version"].get(fv, []))
        lines.append(f"- **{fv}**: {count} Prüfidentifikatoren")

    lines.extend(
        [
            "",
            "## How to Use (for Agents)",
            "",
            "",
            "## Direction Reference (LF perspective)",
            "",
            "| Direction | Meaning | LF Role |",
            "|-----------|---------|---------|",
            "| `LF → NB` | Outbound | LF sends to NB |",
            "| `NB → LF` | Inbound | LF receives from NB |",
            "| `LF → MSB` | Outbound | LF sends to MSB |",
            "| `MSB → LF` | Inbound | LF receives from MSB |",
            "| other | varies | check meta.direction |",
            "",
        ]
    )

    for fv in index["versions"]:
        lines.extend(
            [
                f"## {fv} — All Prüfidentifikatoren",
                "",
                "| Prüfi | Description | Direction | Version | Date | Lines |",
                "|-------|-------------|-----------|---------|------|-------|",
            ]
        )
        for row in index["by_version"].get(fv, []):
            lines.append(
                "| {pruefidentifikator} | {description} | {direction} | "
                "{versionsnummer} | {veroeffentlichungsdatum} | {lines_count} |".format(
                    pruefidentifikator=row["pruefidentifikator"],
                    description=truncate(str(row["description"]), 50),
                    direction=truncate(str(row["direction"]), 42),
                    versionsnummer=row["versionsnummer"],
                    veroeffentlichungsdatum=row["veroeffentlichungsdatum"],
                    lines_count=row["lines_count"],
                )
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    index = build_index()
    (TARGET_DIR / "INDEX.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (TARGET_DIR / "INDEX.md").write_text(render_markdown(index), encoding="utf-8")

    for fv in index["versions"]:
        count = len(index["by_version"].get(fv, []))
        print(f"[✓] {fv}: {count} Prüfidentifikatoren")
    print(f"[✓] Wrote {TARGET_DIR / 'INDEX.json'} and {TARGET_DIR / 'INDEX.md'}")


if __name__ == "__main__":
    main()
