# Offline Documentation Index

This directory contains **232 documentation pages** downloaded from `doc.macoapp.de` for offline access by AI agents.

## 📊 Statistics

- **Total files**: 232 markdown files
- **Index files**: 
  - `index.json` - Simple filename → URL mapping
  - `enhanced-index.json` - Enhanced mapping with BDEW IDs and process names

## 🔍 How to Use

### ⭐ **For AI Agents: Use `llm.txt` as the Index**

**Primary Index**: `llm.txt` - This is the original index that provides context and structure.

**Why `llm.txt`?**
- ✅ Already contains all context (process names, BDEW IDs, descriptions)
- ✅ Hierarchical structure (Lieferant > Kündigung LFA > Prozessübersicht)
- ✅ Human-readable format
- ✅ Maps to the downloaded markdown files

**What was missing?** The actual markdown content - which is now available in `docs-offline/*.md`

**Alternative**: `enhanced-index.json` - JSON version of `llm.txt` structure (optional, for programmatic access)

**Usage Examples:**

1. **Find documentation by BDEW ID**:
   ```markdown
   # In llm.txt, search for [55078]
   - Prüfi > UTILMD-Strom [55078](https://doc.macoapp.de/55078-1305072m0.md)
   
   # Then read the downloaded file:
   docs-offline/55078-1305072m0.md
   ```

2. **Find Prozessübersicht (workflow documentation)**:
   ```markdown
   # In llm.txt, search for "Prozessübersicht"
   - Lieferant > Kündigung LFA [Prozessübersicht](https://doc.macoapp.de/prozessübersicht-860885m0.md)
   
   # Then read the downloaded file:
   docs-offline/prozessübersicht-860885m0.md
   ```

3. **Find by process name**:
   ```markdown
   # In llm.txt, search for "Kündigung"
   - Lieferant [Kündigung LFA](https://doc.macoapp.de/kündigung-lfa-3118804f0.md)
   - Lieferant > Kündigung LFA [Prozessübersicht](https://doc.macoapp.de/prozessübersicht-860885m0.md)
   - Lieferant > Kündigung LFA > EBD [EBD E_0614](https://doc.macoapp.de/lf_0614.md)
   
   # Then read the downloaded files from docs-offline/
   ```

### Alternative: `index.json`

**Secondary Index**: `index.json` - Simple filename → URL mapping
- Use only if you already know the exact filename
- Less useful for AI agents (no semantic search)
- Useful for quick URL lookups

### Example: Process 55016 (Kündigung)

1. **Find BDEW ID documentation**:
   - Check `enhanced-index.json` → `by_bdew_id["55016"]`

2. **Find Prozessübersicht**:
   - File: `prozessübersicht-860885m0.md`
   - Shows complete workflow with 6 steps

3. **Find related EBD**:
   - File: `lf_0614.md` (EBD E_0614 decision tree)

## 📁 File Structure

```
docs-offline/
├── README.md                    # This file
├── index.json                   # Simple filename → URL mapping
├── enhanced-index.json          # Enhanced mapping (BDEW IDs, process names)
├── prozessübersicht-*.md        # Workflow documentation (9 files)
├── 55077-*.md, 55078-*.md      # BDEW process documentation
├── kündigung-*.md               # Process-specific docs
├── lieferbeginn-*.md            # Process-specific docs
└── ... (232 total files)
```

## 🎯 Key Documentation Types

### Prozessübersicht (Process Overview)
- **Purpose**: Shows complete workflow with step-by-step API call sequences
- **Example**: `prozessübersicht-860885m0.md` (Kündigung LFA)
- **Value**: Critical for understanding API call order and dependencies

### Process Documentation
- **Purpose**: Detailed process descriptions
- **Example**: `kündigung-lfa-3118804f0.md`
- **Value**: Business context and requirements

### EBD (Entscheidungsbaumdiagramm)
- **Purpose**: Decision tree diagrams
- **Example**: `lf_0614.md` (EBD E_0614)
- **Value**: Conditional logic and decision points

### API Documentation
- **Purpose**: API endpoint documentation
- **Example**: `trigger-maco-app-3036543f0.md`
- **Value**: Technical API reference

## 🔄 Updating Documentation

To update/download all documentation:

```bash
./scripts/download-docs.sh
python3 scripts/create-enhanced-index.py
```

## 📝 Notes

- All files are UTF-8 encoded markdown
- URLs are preserved in index files for reference
- Documentation is downloaded from `doc.macoapp.de`
- Files are named using URL-decoded filenames (e.g., `übersicht-849494m0.md`)

