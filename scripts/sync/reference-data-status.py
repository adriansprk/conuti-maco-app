#!/usr/bin/env python3
"""Check or snapshot AHB tables + EBD diagram reference data for scripts/sync."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WORKSPACE_ROOT = SCRIPT_DIR.parent.parent
AHB_DIR = WORKSPACE_ROOT / "ahb-tables"
EBD_DIR = WORKSPACE_ROOT / "ebd-diagrams"
AHB_API = "https://ahb-tabellen.hochfrequenz.de/api"


def fetch_json(url: str, timeout: int = 30):
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return json.loads(resp.read())


def version_sort_key(fv: str) -> tuple[int, int]:
    match = re.fullmatch(r"FV(\d{2})(\d{2})", fv)
    if not match:
        return (0, 0)
    return (int(match.group(1)), int(match.group(2)))


def discover_ebd_versions() -> list[str]:
    if not EBD_DIR.is_dir():
        return []
    return sorted(
        [p.name for p in EBD_DIR.iterdir() if p.is_dir() and p.name.startswith("FV")],
        key=version_sort_key,
    )


def ebd_latest_version() -> str | None:
    format_versions = EBD_DIR / "format_versions.json"
    if format_versions.exists():
        data = json.loads(format_versions.read_text(encoding="utf-8"))
        latest = data.get("latest")
        if isinstance(latest, str) and latest:
            return latest
    versions = discover_ebd_versions()
    return versions[-1] if versions else None


def count_ebd_json(fv: str) -> int:
    return len(list((EBD_DIR / fv).glob("E_*.json")))


def load_ahb_versions() -> list[str]:
    index_path = AHB_DIR / "INDEX.json"
    if not index_path.exists():
        return []
    data = json.loads(index_path.read_text(encoding="utf-8"))
    return list(data.get("versions") or [])


def count_ahb_files(fv: str) -> int:
    return len(list((AHB_DIR / fv).glob(f"AHB_{fv}_*.json")))


def probe_ahb_api_version(fv: str) -> int | None:
    try:
        data = fetch_json(f"{AHB_API}/pruefidentifikatoren/{fv}")
    except Exception:
        return None
    return len(data) if isinstance(data, list) else None


def discover_new_ahb_api_versions(known: list[str]) -> list[str]:
    if not known:
        return []
    latest = sorted(known, key=version_sort_key)[-1]
    year, month = int(latest[2:4]), int(latest[4:6])
    candidates = []
    if month == 4:
        candidates.append(f"FV{year:02d}10")
        candidates.append(f"FV{year + 1:02d}04")
    else:
        candidates.append(f"FV{year + 1:02d}04")
        candidates.append(f"FV{year + 1:02d}10")
    return [fv for fv in candidates if fv not in known and probe_ahb_api_version(fv) is not None]


def snapshot() -> dict:
    ahb_versions = load_ahb_versions()
    ahb_counts = {fv: count_ahb_files(fv) for fv in ahb_versions}
    ebd_versions = discover_ebd_versions()
    latest_ebd = ebd_latest_version()
    return {
        "ahb_tables": {
            "versions": ahb_versions,
            "version_counts": ahb_counts,
        },
        "ebd_diagrams": {
            "format_versions": ebd_versions,
            "latest_format_version": latest_ebd,
            "ebd_count_latest": count_ebd_json(latest_ebd) if latest_ebd else 0,
        },
    }


def check(ahb_only: bool = False, ebd_only: bool = False) -> int:
    issues = 0
    check_ahb = not ebd_only
    check_ebd = not ahb_only

    if check_ahb:
        if not AHB_DIR.is_dir():
            print("ahb-tables: missing")
            issues += 1
        else:
            versions = load_ahb_versions()
            if not versions:
                print("ahb-tables: INDEX.json missing or has no versions")
                issues += 1
            else:
                for fv in versions:
                    local = count_ahb_files(fv)
                    api = probe_ahb_api_version(fv)
                    if api is None:
                        print(f"ahb-tables: could not query API for {fv}")
                        issues += 1
                    elif local != api:
                        print(f"ahb-tables: {fv} drift local={local} api={api}")
                        issues += 1
                    else:
                        print(f"ahb-tables: {fv} ok ({local} Prüfidentifikatoren)")
                for fv in discover_new_ahb_api_versions(versions):
                    api = probe_ahb_api_version(fv)
                    print(
                        f"ahb-tables: new API format version available: "
                        f"{fv} ({api} Prüfidentifikatoren)"
                    )
                    issues += 1

    if check_ebd:
        if not EBD_DIR.is_dir():
            print("ebd-diagrams: missing")
            issues += 1
        else:
            latest = ebd_latest_version()
            versions = discover_ebd_versions()
            print(f"ebd-diagrams: format versions local={versions}")
            if latest:
                print(
                    f"ebd-diagrams: latest={latest} "
                    f"({count_ebd_json(latest)} E_*.json files)"
                )
            else:
                print("ebd-diagrams: no FV* directories found")
                issues += 1

    return 1 if issues else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=["check", "check-ahb", "check-ebd", "snapshot"],
        help="check* = report drift (exit 1 if issues); snapshot = JSON metadata for version-tracker",
    )
    args = parser.parse_args()

    if args.command == "check":
        sys.exit(check())
    if args.command == "check-ahb":
        sys.exit(check(ahb_only=True))
    if args.command == "check-ebd":
        sys.exit(check(ebd_only=True))

    print(json.dumps(snapshot(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
