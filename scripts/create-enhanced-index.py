#!/usr/bin/env python3
"""
create-enhanced-index.py - Create enhanced index mapping BDEW IDs to documentation
"""

import json
import re
from pathlib import Path

def extract_bdew_mappings():
    """Extract BDEW ID mappings from llm.txt"""
    llm_file = Path('llm.txt')
    docs_dir = Path('docs-offline')
    
    # Read llm.txt
    with open(llm_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all URLs and their context
    pattern = r'- (.+?)\s*\[(\d{5})\]\(https://doc\.macoapp\.de/([^)]+)\)'
    matches = re.findall(pattern, content)
    
    # Also extract URLs without BDEW IDs
    url_pattern = r'- (.+?)\s*\(https://doc\.macoapp\.de/([^)]+)\)'
    url_matches = re.findall(url_pattern, content)
    
    # Build index
    index = {
        'by_bdew_id': {},
        'by_process_name': {},
        'by_filename': {},
        'prozessuebersicht': {}
    }
    
    # Process BDEW ID mappings
    for context, bdew_id, url in matches:
        filename = url.split('/')[-1]
        # Decode URL encoding
        filename = filename.replace('%C3%BC', 'ü').replace('%C3%A4', 'ä').replace('%C3%B6', 'ö')
        filename = filename.replace('%C3%9C', 'Ü').replace('%C3%84', 'Ä').replace('%C3%96', 'Ö')
        filename = filename.replace('%C3%9F', 'ß')
        
        file_path = docs_dir / filename
        if file_path.exists():
            if bdew_id not in index['by_bdew_id']:
                index['by_bdew_id'][bdew_id] = []
            index['by_bdew_id'][bdew_id].append({
                'context': context.strip(),
                'filename': filename,
                'url': f'https://doc.macoapp.de/{url}'
            })
    
    # Process all URLs (including those without BDEW IDs)
    for context, url in url_matches:
        filename = url.split('/')[-1]
        # Decode URL encoding
        filename = filename.replace('%C3%BC', 'ü').replace('%C3%A4', 'ä').replace('%C3%B6', 'ö')
        filename = filename.replace('%C3%9C', 'Ü').replace('%C3%84', 'Ä').replace('%C3%96', 'Ö')
        filename = filename.replace('%C3%9F', 'ß')
        
        file_path = docs_dir / filename
        if file_path.exists():
            # Extract process name from context
            process_name = context.strip()
            
            # Check if it's a Prozessübersicht
            if 'Prozessübersicht' in process_name or 'prozessübersicht' in filename.lower():
                # Try to extract BDEW ID from context
                bdew_match = re.search(r'\[(\d{5})\]', process_name)
                if bdew_match:
                    bdew_id = bdew_match.group(1)
                    if bdew_id not in index['prozessuebersicht']:
                        index['prozessuebersicht'][bdew_id] = []
                    index['prozessuebersicht'][bdew_id].append({
                        'context': process_name,
                        'filename': filename,
                        'url': f'https://doc.macoapp.de/{url}'
                    })
            
            # Add to process name index
            if process_name not in index['by_process_name']:
                index['by_process_name'][process_name] = []
            index['by_process_name'][process_name].append({
                'filename': filename,
                'url': f'https://doc.macoapp.de/{url}'
            })
            
            # Add to filename index
            index['by_filename'][filename] = {
                'context': process_name,
                'url': f'https://doc.macoapp.de/{url}'
            }
    
    return index

def main():
    print("🔍 Creating enhanced index...")
    
    index = extract_bdew_mappings()
    
    # Save enhanced index
    output_file = Path('docs-offline/enhanced-index.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Enhanced index created: {output_file}")
    print(f"   📊 BDEW IDs mapped: {len(index['by_bdew_id'])}")
    print(f"   📊 Process names mapped: {len(index['by_process_name'])}")
    print(f"   📊 Prozessübersicht entries: {len(index['prozessuebersicht'])}")
    print(f"   📊 Total files indexed: {len(index['by_filename'])}")
    
    # Show sample entries
    if index['by_bdew_id']:
        print("\n📋 Sample BDEW ID mappings:")
        for bdew_id in list(index['by_bdew_id'].keys())[:5]:
            print(f"   {bdew_id}: {len(index['by_bdew_id'][bdew_id])} doc(s)")

if __name__ == '__main__':
    main()

