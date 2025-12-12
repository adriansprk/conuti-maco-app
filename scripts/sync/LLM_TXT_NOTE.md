# llm.txt Source and Workflow

## Source

**`llm.txt` is manually downloaded from the online documentation** (`doc.macoapp.de`), not from `maco-api-documentation` repo.

## Workflow

```
doc.macoapp.de (online)
    ↓
llm.txt (manually downloaded)
    ↓
scripts/download-docs.sh
    ↓
docs-offline/*.md (downloaded markdown files)
    ↓
Extract Mermaid diagrams
    ↓
PROCESS_GRAPH.json (generated)
```

## Process

1. **Download `llm.txt`** from `doc.macoapp.de` (manual step)
2. **Place in workspace**: `docs/llm.txt`
3. **Run download script**: `./scripts/download-docs.sh`
   - Extracts URLs from `llm.txt`
   - Downloads markdown files to `docs-offline/`
4. **Generate PROCESS_GRAPH.json**:
   - Extract Mermaid diagrams from markdown files
   - Parse process sequences, dependencies, prerequisites
   - Combine with API schemas and business rules
   - Generate `docs/entry-points/PROCESS_GRAPH.json`

## File Locations

- **`docs/llm.txt`** - Manually downloaded from online docs (workspace-specific)
- **`docs-offline/*.md`** - Downloaded markdown files (232 files)
- **`docs/entry-points/PROCESS_GRAPH.json`** - Generated from markdown files + schemas

## Updating Workflow

When online documentation updates:

```bash
# 1. Manually download updated llm.txt from doc.macoapp.de
#    Save to: docs/llm.txt

# 2. Download updated markdown files
./scripts/download-docs.sh

# 3. Regenerate PROCESS_GRAPH.json (when script implemented)
# Manual workflow:
./scripts/download-docs.sh
python3 scripts/sync/update-process-graph-minimal.py
# OR manually update PROCESS_GRAPH.json
```

## Sync System

The sync system now correctly reflects that:
- ✅ `llm.txt` is **NOT** part of `maco-api-documentation` repo
- ✅ It's **workspace-specific** (manually downloaded)
- ✅ `PROCESS_GRAPH.json` is **generated** from `docs-offline/` markdown files
- ✅ Mermaid diagrams are **extracted** from markdown files during generation

## Notes

- `maco-api-documentation/README.MD` references `../llm.txt` because it expects it in the workspace root (parent directory)
- The sync system no longer tries to sync `llm.txt` from the repo
- Use manual workflow: `download-docs.sh` → `update-process-graph-minimal.py`
