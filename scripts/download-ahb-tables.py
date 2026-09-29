#!/usr/bin/env python3
"""
Downloads all AHB tables from ahb-tabellen.hochfrequenz.de (public API, no auth required).
Usage: python3 scripts/download-ahb-tables.py [--versions FV2510 FV2604 FV2610] [--workers 10] [--refresh]

Without --refresh, existing files are skipped. With --refresh, every Prüfi is re-fetched
and overwritten only when the upstream content differs (reported as UPDATED).
"""

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import urllib.request
import urllib.error

BASE_URL = "https://ahb-tabellen.hochfrequenz.de/api"
REPO_ROOT = Path(__file__).parent.parent
TARGET_DIR = REPO_ROOT / "ahb-tables"


def fetch_json(url: str, timeout: int = 30):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def _without_guids(data):
    """Upstream regenerates line GUIDs on re-parse; ignore them when detecting content changes."""
    return {**data, "lines": [{k: v for k, v in l.items() if k != "guid"} for l in data.get("lines", [])]}


def download_ahb(fv: str, prufi: str, outfile: Path, refresh: bool = False):
    """Returns (status, prufi) where status is OK | UPDATED | SAME | SKIP | EMPTY | FAIL"""
    if outfile.exists() and not refresh:
        return ("SKIP", prufi)

    url = f"{BASE_URL}/ahb/{fv}/{prufi}"
    tmp = outfile.with_suffix(".tmp")

    data = fetch_json(url)
    if data is None:
        return ("FAIL", prufi)

    if not isinstance(data, dict) or "lines" not in data:
        return ("EMPTY", prufi)

    status = "OK"
    if outfile.exists():
        if _without_guids(json.loads(outfile.read_text(encoding="utf-8"))) == _without_guids(data):
            return ("SAME", prufi)
        status = "UPDATED"

    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.rename(outfile)
    return (status, prufi)


def process_version(fv: str, workers: int, refresh: bool = False) -> dict:
    print(f"\n=== Processing {fv} ===")

    prufi_data = fetch_json(f"{BASE_URL}/pruefidentifikatoren/{fv}")
    if not prufi_data:
        print(f"[✗] Failed to fetch Prüfidentifikatoren list for {fv}")
        return {}

    prufi_list = [d["pruefidentifikator"] for d in prufi_data]
    total = len(prufi_list)
    print(f"[✓] Found {total} Prüfidentifikatoren in {fv}")

    outdir = TARGET_DIR / fv
    outdir.mkdir(parents=True, exist_ok=True)

    existing = len(list(outdir.glob(f"AHB_{fv}_*.json")))
    print(f"[!] Already have {existing} / {total} files")

    results = {"OK": [], "UPDATED": [], "SAME": [], "SKIP": [], "EMPTY": [], "FAIL": []}
    completed = 0

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                download_ahb, fv, prufi, outdir / f"AHB_{fv}_{prufi}.json", refresh
            ): prufi
            for prufi in prufi_list
        }

        for future in as_completed(futures):
            status, prufi = future.result()
            results[status].append(prufi)
            completed += 1

            if status == "OK":
                print(".", end="", flush=True)
            elif status == "UPDATED":
                print("u", end="", flush=True)
            elif status in ("SKIP", "SAME"):
                print("·", end="", flush=True)
            elif status in ("FAIL", "EMPTY"):
                print("F", end="", flush=True)

            if completed % 50 == 0:
                print(f" [{completed}/{total}]", flush=True)

    print()  # newline after progress dots

    final = len(list(outdir.glob(f"AHB_{fv}_*.json")))
    print(
        f"[✓] {fv} complete: "
        f"{len(results['OK'])} downloaded, "
        f"{len(results['UPDATED'])} updated, "
        f"{len(results['SAME'])} unchanged, "
        f"{len(results['SKIP'])} skipped, "
        f"{len(results['FAIL']) + len(results['EMPTY'])} failed "
        f"→ {final} total files"
    )

    if results["UPDATED"]:
        print(f"[!] Updated: {', '.join(sorted(results['UPDATED']))}")
    stale = sorted(
        f.stem.split("_")[-1] for f in outdir.glob(f"AHB_{fv}_*.json")
    )
    stale = [p for p in stale if p not in set(prufi_list)]
    if stale:
        print(f"[!] Local files no longer listed upstream (not deleted): {', '.join(stale)}")
    if results["FAIL"]:
        print(f"[!] Failed downloads: {', '.join(results['FAIL'])}")
    if results["EMPTY"]:
        print(f"[!] Empty responses: {', '.join(results['EMPTY'])}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Download AHB tables from hochfrequenz.de")
    parser.add_argument(
        "--versions", nargs="+", default=["FV2510", "FV2604", "FV2610"],
        help="Format versions to download (default: FV2510 FV2604 FV2610)"
    )
    parser.add_argument(
        "--workers", type=int, default=10,
        help="Number of parallel download workers (default: 10)"
    )
    parser.add_argument(
        "--refresh", action="store_true",
        help="Re-fetch existing files and overwrite those whose upstream content changed"
    )
    args = parser.parse_args()

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Target directory: {TARGET_DIR}")
    print(f"Workers: {args.workers}")

    for fv in args.versions:
        process_version(fv, args.workers, args.refresh)

    print(f"\n[✓] All done. Files saved to: {TARGET_DIR}")


if __name__ == "__main__":
    main()
