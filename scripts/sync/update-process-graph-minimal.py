#!/usr/bin/env python3
"""
update-process-graph-minimal.py - Generate minimal PROCESS_GRAPH.json index

This script creates a minimal index that points to source documentation files,
preserving original context and letting agents read the actual docs.

Philosophy: "Point, don't interpret"
- Only extract factual mappings (BDEW IDs → files, process names → files)
- No inferred triggers, roles, prerequisites, or relationships
- Agents read source docs for details
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set
from collections import defaultdict

# Configuration
WORKSPACE_ROOT = Path(__file__).parent.parent.parent
DOCS_OFFLINE = WORKSPACE_ROOT / "docs-offline"
ENTRY_POINTS = WORKSPACE_ROOT / "docs" / "entry-points"
LLM_TXT = WORKSPACE_ROOT / "docs" / "llm.txt"
OUTPUT_FILE = ENTRY_POINTS / "PROCESS_GRAPH.json"


def extract_bdew_ids_from_content(content: str) -> Set[str]:
    """Extract BDEW Prüfidentifikatoren from content - only factual references."""
    pruefis = set()
    
    # PI_55016 references (most reliable)
    pi_pattern = r'PI_(\d{5})'
    pruefis.update(re.findall(pi_pattern, content))
    
    # Tab titles: 📄55016
    tab_pattern = r'📄(\d{5})'
    pruefis.update(re.findall(tab_pattern, content))
    
    # Card titles: <Card title="55016"
    card_pattern = r'<Card[^>]*title=["\'](\d{5})["\']'
    pruefis.update(re.findall(card_pattern, content))
    
    # Mermaid comments: *1 Prüfi: 55016
    mermaid_pattern = r'\*\d+\s+Prüfi:\s*([\d,\s]+)'
    mermaid_matches = re.findall(mermaid_pattern, content)
    for match in mermaid_matches:
        pruefis.update(re.findall(r'(\d{5})', match))
    
    # Filter: only valid BDEW Prüfi ranges (0xxxx, 1xxxx, 2xxxx, 3xxxx, 5xxxx)
    valid_ranges = [
        r'^0[1-9]\d{3}$',  # 0xxxx (MaloIdent)
        r'^1[0-9]\d{3}$',  # 1xxxx
        r'^2[0-9]\d{3}$',  # 2xxxx
        r'^3[0-9]\d{3}$',  # 3xxxx
        r'^5[0-9]\d{3}$',  # 5xxxx (main processes)
    ]
    
    filtered = set()
    for pruefi in pruefis:
        if any(re.match(pattern, pruefi) for pattern in valid_ranges):
            filtered.add(pruefi)
    
    return filtered


def extract_triggers_from_content(content: str) -> Set[str]:
    """Extract trigger event names - only from explicit references."""
    triggers = set()
    
    # XML Card structures: <Card title="START_LIEFERBEGINN"
    card_pattern = r'<Card[^>]*title=["\'](START_\w+)["\']'
    triggers.update(re.findall(card_pattern, content))
    
    # Tab titles: 📄START_LIEFERBEGINN
    tab_pattern = r'📄(START_\w+)'
    triggers.update(re.findall(tab_pattern, content))
    
    return triggers


def extract_process_name_from_file(file_path: Path, content: str) -> str:
    """Extract process name from filename or title - minimal inference."""
    filename_lower = file_path.name.lower()
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""
    
    # Use filename as primary identifier (most stable)
    # Remove common suffixes: -rolle-lf-3119288f0.md → kündigung-lfn
    name = file_path.stem
    name = re.sub(r'-rolle-[a-z]+-\d+[a-z]\d+$', '', name)
    name = re.sub(r'-\d+[a-z]\d+$', '', name)  # Remove hash suffixes
    
    return name


def build_minimal_index() -> Dict:
    """Build minimal index pointing to source files."""
    
    # Indexes
    by_bdew_id = defaultdict(list)  # BDEW ID → list of files
    by_trigger = defaultdict(list)   # Trigger → list of files
    by_filename = {}                  # Filename → metadata
    by_process_name = defaultdict(list)  # Process name → list of files
    
    # Process all markdown files
    for md_file in DOCS_OFFLINE.glob("*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')
            filename = md_file.name
            
            # Extract factual data only
            pruefis = extract_bdew_ids_from_content(content)
            triggers = extract_triggers_from_content(content)
            process_name = extract_process_name_from_file(md_file, content)
            
            # File metadata (minimal)
            file_info = {
                "filename": filename,
                "path": f"docs-offline/{filename}",
                "is_prozessuebersicht": "prozessübersicht" in filename.lower(),
                "has_mermaid": "```mermaid" in content,
            }
            
            # Index by BDEW ID
            for pruefi in pruefis:
                by_bdew_id[pruefi].append(file_info)
            
            # Index by trigger
            for trigger in triggers:
                by_trigger[trigger].append(file_info)
            
            # Index by filename
            by_filename[filename] = file_info
            
            # Index by process name
            by_process_name[process_name].append(file_info)
            
        except Exception as e:
            print(f"⚠️  Error processing {md_file.name}: {e}")
    
    # Build minimal graph structure
    graph = {
        "$schema": "./schemas/process-graph-schema.json",
        "version": "2.0.0-minimal",
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "description": "Minimal index pointing to source documentation. Agents should read source files for details.",
        "philosophy": "Point, don't interpret. This index helps discover files; agents read source docs for context.",
        
        "indexes": {
            "by_bdew_id": dict(by_bdew_id),
            "by_trigger": dict(by_trigger),
            "by_filename": by_filename,
            "by_process_name": dict(by_process_name),
        },
        
        "source_files": {
            "total": len(by_filename),
            "with_bdew_ids": len([f for f in by_filename.values() if any(f["filename"] in str(by_bdew_id.get(p, [])) for p in extract_bdew_ids_from_content(""))]),
            "with_triggers": len([f for f in by_filename.values() if any(f["filename"] in str(by_trigger.get(t, [])) for t in extract_triggers_from_content(""))]),
            "with_mermaid": len([f for f in by_filename.values() if f["has_mermaid"]]),
            "prozessuebersicht": len([f for f in by_filename.values() if f["is_prozessuebersicht"]]),
        },
        
        "usage": {
            "discovery": "Use indexes to find relevant files, then read source documentation",
            "example": {
                "find_by_bdew_id": "indexes.by_bdew_id['55001'] → list of files mentioning this Prüfi",
                "find_by_trigger": "indexes.by_trigger['START_LIEFERBEGINN'] → list of files with this trigger",
                "find_by_process": "indexes.by_process_name['lieferbeginn'] → list of files for this process",
            },
            "next_steps": [
                "1. Use index to find relevant files",
                "2. Read the actual markdown files for full context",
                "3. Parse Mermaid diagrams directly from source",
                "4. Extract roles, prerequisites, relationships from source docs",
                "5. Cross-reference with API schemas and business rules",
            ]
        },
        
        # Empty - agents build this from source docs
        "processes": {},
        "business_scenarios": {},
        "ebd_reference": {},
    }
    
    return graph


def main():
    """Main function to generate minimal PROCESS_GRAPH.json."""
    print("🔨 Generating minimal PROCESS_GRAPH.json (source file index only)...")
    print("")
    
    if not DOCS_OFFLINE.exists():
        print(f"❌ docs-offline directory not found: {DOCS_OFFLINE}")
        return 1
    
    if not ENTRY_POINTS.exists():
        ENTRY_POINTS.mkdir(parents=True, exist_ok=True)
    
    print("📚 Reading markdown files and extracting factual references...")
    graph = build_minimal_index()
    
    print("💾 Writing PROCESS_GRAPH.json...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    print(f"  ✅ Written to: {OUTPUT_FILE}")
    print("")
    
    # Summary
    print("📊 Summary:")
    print(f"  ✅ Files indexed: {graph['source_files']['total']}")
    print(f"  ✅ BDEW IDs found: {len(graph['indexes']['by_bdew_id'])}")
    print(f"  ✅ Triggers found: {len(graph['indexes']['by_trigger'])}")
    print(f"  ✅ Process names: {len(graph['indexes']['by_process_name'])}")
    print(f"  ✅ Files with Mermaid: {graph['source_files']['with_mermaid']}")
    print(f"  ✅ Prozessübersicht files: {graph['source_files']['prozessuebersicht']}")
    print("")
    print("✅ Generation complete!")
    print("")
    print("💡 Philosophy: This is a discovery index, not a processed graph.")
    print("   Agents should use it to find files, then read source docs for details.")
    print("   This minimizes errors from interpretation and preserves original context.")
    
    return 0


if __name__ == '__main__':
    exit(main())
