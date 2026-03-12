#!/usr/bin/env python3
"""
Downloads all AHB tables from ahb-tabellen.hochfrequenz.de (public API, no auth required).
Usage: python3 scripts/download-ahb-tables.py [--versions FV2510 FV2604] [--workers 10]
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


def download_ahb(fv: str, prufi: str, outfile: Path):
    """Returns (status, prufi) where status is OK | SKIP | EMPTY | FAIL"""
    if outfile.exists():
        return ("SKIP", prufi)

    url = f"{BASE_URL}/ahb/{fv}/{prufi}"
    tmp = outfile.with_suffix(".tmp")

    data = fetch_json(url)
    if data is None:
        return ("FAIL", prufi)

    if not isinstance(data, dict) or "lines" not in data:
        return ("EMPTY", prufi)

    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.rename(outfile)
    return ("OK", prufi)


def process_version(fv: str, workers: int) -> dict:
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

    results = {"OK": [], "SKIP": [], "EMPTY": [], "FAIL": []}
    completed = 0

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                download_ahb, fv, prufi, outdir / f"AHB_{fv}_{prufi}.json"
            ): prufi
            for prufi in prufi_list
        }

        for future in as_completed(futures):
            status, prufi = future.result()
            results[status].append(prufi)
            completed += 1

            if status == "OK":
                print(".", end="", flush=True)
            elif status == "SKIP":
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
        f"{len(results['SKIP'])} skipped, "
        f"{len(results['FAIL']) + len(results['EMPTY'])} failed "
        f"→ {final} total files"
    )

    if results["FAIL"]:
        print(f"[!] Failed downloads: {', '.join(results['FAIL'])}")
    if results["EMPTY"]:
        print(f"[!] Empty responses: {', '.join(results['EMPTY'])}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Download AHB tables from hochfrequenz.de")
    parser.add_argument(
        "--versions", nargs="+", default=["FV2510", "FV2604"],
        help="Format versions to download (default: FV2510 FV2604)"
    )
    parser.add_argument(
        "--workers", type=int, default=10,
        help="Number of parallel download workers (default: 10)"
    )
    args = parser.parse_args()

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Target directory: {TARGET_DIR}")
    print(f"Workers: {args.workers}")

    for fv in args.versions:
        process_version(fv, args.workers)

    print(f"\n[✓] All done. Files saved to: {TARGET_DIR}")


if __name__ == "__main__":
    main()
