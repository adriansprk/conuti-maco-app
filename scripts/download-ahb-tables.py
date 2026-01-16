#!/usr/bin/env python3
"""
Download AHB tables from ahb-tabellen.hochfrequenz.de for all known Prüfidentifikatoren.

Usage:
    python download-ahb-tables.py [--format json|csv] [--output-dir ./ahb-tables] [--version FV2510]
"""
from __future__ import annotations

import argparse
import json
import csv
import os
import sys
import time
from pathlib import Path
from typing import Optional, List, Dict, Any

try:
    import requests
    USE_REQUESTS = True
except ImportError:
    import ssl
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError
    USE_REQUESTS = False

# All known Prüfidentifikatoren from maco-api-documentation
KNOWN_PRUEFIS = [
    # Core LIEFERBEGINN processes
    55001, 55002, 55003, 55004, 55005, 55006, 55007, 55008, 55009,
    55010, 55011, 55012, 55013, 55014, 55015, 55016, 55017, 55018,
    55022, 55023, 55024,
    55035, 55036, 55037, 55038, 55039, 55040, 55041, 55042, 55043, 55044,
    55051, 55052, 55053,
    55060,
    55074, 55075, 55077, 55078, 55080,
    55095,
    55109, 55110,
    55126, 55136, 55137,
    55156,
    55168, 55169, 55170, 55173, 55175, 55177, 55180,
    55194,
    55218, 55220, 55225, 55227, 55230, 55232,
    # 555xx series
    55553, 55555, 55557, 55559,
    # 556xx series (LIEFERBEGINN alternatives and Stammdatenänderung)
    55600, 55601, 55602, 55603, 55604, 55605, 55607, 55608, 55609,
    55611, 55613, 55614, 55615, 55616, 55617, 55618, 55619, 55620,
    55621, 55622, 55623, 55624, 55625, 55626, 55627, 55628, 55629, 55630,
    55632, 55633, 55634, 55635, 55636, 55638, 55639, 55640,
    55641, 55642, 55643, 55644, 55645, 55646, 55647, 55648, 55649, 55650,
    55651, 55652, 55654, 55655, 55656, 55657, 55659, 55660,
    55661, 55662, 55663, 55664, 55665, 55666, 55667, 55669, 55670,
    55672, 55673, 55674,
    55684, 55686, 55688, 55691, 55692,
]

# Additional Prüfis that might exist (13xxx series for index/overview pages)
ADDITIONAL_PRUEFIS = [
    13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010,
    13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020,
]

BASE_URL = "https://ahb-tabellen.hochfrequenz.de/api/ahb"


def download_ahb(pruefi: int, version: str = "FV2510") -> Optional[Dict[str, Any]]:
    """Download AHB table for a specific Prüfidentifikator."""
    url = f"{BASE_URL}/{version}/{pruefi}"
    
    if USE_REQUESTS:
        try:
            response = requests.get(
                url,
                headers={
                    "Accept": "application/json",
                    "User-Agent": "AHB-Downloader/1.0"
                },
                timeout=30
            )
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"  ⚠️  HTTP Error for {pruefi}: {e}", file=sys.stderr)
            return None
        except requests.exceptions.RequestException as e:
            print(f"  ⚠️  Request Error for {pruefi}: {e}", file=sys.stderr)
            return None
        except json.JSONDecodeError as e:
            print(f"  ⚠️  JSON decode error for {pruefi}: {e}", file=sys.stderr)
            return None
    else:
        # Fallback to urllib with SSL context
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        request = Request(url)
        request.add_header("Accept", "application/json")
        request.add_header("User-Agent", "AHB-Downloader/1.0")
        
        try:
            with urlopen(request, timeout=30, context=ssl_context) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data
        except HTTPError as e:
            if e.code == 404:
                return None
            print(f"  ⚠️  HTTP Error {e.code} for {pruefi}: {e.reason}", file=sys.stderr)
            return None
        except URLError as e:
            print(f"  ⚠️  URL Error for {pruefi}: {e.reason}", file=sys.stderr)
            return None
        except json.JSONDecodeError as e:
            print(f"  ⚠️  JSON decode error for {pruefi}: {e}", file=sys.stderr)
            return None


def json_to_csv(data: Dict[str, Any]) -> List[List[str]]:
    """Convert AHB JSON data to CSV rows.
    
    The API returns JSON with 'lines' array containing objects with these fields:
    - segment_group_key: Segmentgruppe (e.g., "SG2", "SG4")
    - section_name: Segmentname (e.g., "MP-ID Absender")
    - segment_code: Segment (e.g., "NAD", "DTM")
    - data_element: Datenelement (e.g., "3035", "2380")
    - value_pool_entry: Qualifier/Code value (e.g., "MS", "137")
    - name: Description/Name
    - ahb_expression: Pflichtfeld-Kennzeichen (e.g., "X", "Muss", "Kann")
    - conditions: Bedingungen/Hinweise
    """
    rows = []
    
    # Header row matching the original CSV format from the website
    headers = ["Segmentgruppe", "Segmentname", "Segment", "Datenelement", 
               "Qualifier", "Name", "Pflichtfeld-Kennzeichen", "Bedingung / Hinweis / Format"]
    rows.append(headers)
    
    # Get the lines array from the JSON
    items = []
    if isinstance(data, dict):
        items = data.get("lines", data.get("rows", data.get("data", [])))
    elif isinstance(data, list):
        items = data
    
    for item in items:
        if isinstance(item, dict):
            row = [
                str(item.get("segment_group_key", "") or ""),
                str(item.get("section_name", "") or ""),
                str(item.get("segment_code", "") or ""),
                str(item.get("data_element", "") or ""),
                str(item.get("value_pool_entry", "") or ""),
                str(item.get("name", "") or ""),
                str(item.get("ahb_expression", "") or ""),
                str(item.get("conditions", "") or ""),
            ]
            rows.append(row)
        elif isinstance(item, list):
            rows.append([str(x) for x in item])
    
    return rows


def save_json(data: dict, filepath: Path):
    """Save data as JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_csv(data: dict, filepath: Path):
    """Save data as CSV file."""
    rows = json_to_csv(data)
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(
        description="Download AHB tables from ahb-tabellen.hochfrequenz.de"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["json", "csv", "both"],
        default="json",
        help="Output format (default: json)"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=Path("./ahb-tables"),
        help="Output directory (default: ./ahb-tables)"
    )
    parser.add_argument(
        "--version", "-v",
        default="FV2510",
        help="Format version (default: FV2510)"
    )
    parser.add_argument(
        "--include-additional",
        action="store_true",
        help="Also try to download 13xxx series prüfis"
    )
    parser.add_argument(
        "--delay", "-d",
        type=float,
        default=0.2,
        help="Delay between requests in seconds (default: 0.2)"
    )
    parser.add_argument(
        "--pruefi", "-p",
        type=int,
        nargs="+",
        help="Download only specific prüfi(s)"
    )
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = args.output_dir / args.version
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Determine which prüfis to download
    if args.pruefi:
        pruefis = args.pruefi
    else:
        pruefis = KNOWN_PRUEFIS.copy()
        if args.include_additional:
            pruefis.extend(ADDITIONAL_PRUEFIS)
    
    print(f"📥 Downloading AHB tables for {len(pruefis)} Prüfidentifikatoren...")
    print(f"   Version: {args.version}")
    print(f"   Output: {output_dir}")
    print(f"   Format: {args.format}")
    print()
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for i, pruefi in enumerate(sorted(pruefis), 1):
        print(f"[{i:3d}/{len(pruefis)}] Downloading {pruefi}...", end=" ", flush=True)
        
        data = download_ahb(pruefi, args.version)
        
        if data is None:
            print("❌ Not found or error")
            skip_count += 1
        else:
            try:
                filename_base = f"AHB_{args.version}_{pruefi}"
                
                if args.format in ("json", "both"):
                    json_path = output_dir / f"{filename_base}.json"
                    save_json(data, json_path)
                
                if args.format in ("csv", "both"):
                    csv_path = output_dir / f"{filename_base}.csv"
                    save_csv(data, csv_path)
                
                print(f"✅ Saved")
                success_count += 1
            except Exception as e:
                print(f"⚠️  Save error: {e}")
                error_count += 1
        
        # Rate limiting
        if i < len(pruefis):
            time.sleep(args.delay)
    
    print()
    print(f"📊 Summary:")
    print(f"   ✅ Downloaded: {success_count}")
    print(f"   ⏭️  Skipped (not found): {skip_count}")
    print(f"   ❌ Errors: {error_count}")
    print(f"   📁 Output directory: {output_dir}")


if __name__ == "__main__":
    main()
