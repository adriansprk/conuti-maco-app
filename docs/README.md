# Documentation Directory

This directory contains all documentation and entry point files for the MaCo API workspace.

## Structure

```
docs/
├── entry-points/          # Main entry point files
│   ├── AI_AGENT_SETUP.md          # Entry Point 2: Technical implementation
│   ├── BUSINESS_PROCESS_MAP.md    # Entry Point 1: Business discovery
│   ├── PROCESS_GRAPH.json         # Machine-readable process graph
│   └── README.md                  # Entry points documentation
└── llm.txt                # Documentation index (237 entries)
```

## Entry Points

### Entry Point 1: Business Goal Discovery

**File**: `entry-points/BUSINESS_PROCESS_MAP.md`

Use when you have a business goal (e.g., "register new customer", "cancel contract").

### Entry Point 2: Technical Implementation

**File**: `entry-points/AI_AGENT_SETUP.md`

Use when you have a specific BDEW process ID or MaKo message (e.g., "55077", "START_LIEFERBEGINN").

### Process Dependency Graph

**File**: `entry-points/PROCESS_GRAPH.json`

Machine-readable JSON file for fast lookups:
- Process by BDEW ID: `indexes.by_bdew_id["55077"]`
- Process by trigger: `indexes.by_trigger["START_LIEFERBEGINN"]`
- Process docs by name: `indexes.by_process_name["lieferbeginn"]`

⚠️ Note: In this repo `PROCESS_GRAPH.json` is generated as a **minimal discovery index** (`version: 2.0.0-minimal`).
The sections `processes`, `business_scenarios`, `ebd_reference` exist but are currently **empty**. Derive dependencies by reading the referenced `docs-offline/*.md` sources (Mermaid + prose).

## Documentation Index

**File**: `llm.txt`

Index of 237 documentation entries. Use to find which documentation files you need for a specific process.

## Maintenance

### Updating After External Repo Changes

When external repositories (`maco-api-documentation`, `docs-offline`) are updated:

1. **Check for changes**: `./scripts/sync/check-changes.sh`
2. **Sync changes**: `./scripts/sync/sync-changes.sh`
3. **Regenerate PROCESS_GRAPH.json**: `./scripts/sync/update-process-graph.py` (when implemented)

See `scripts/sync/README.md` for detailed workflow.

### File Locations

All entry point files have been moved to `docs/entry-points/` for better organization. The AI agent rules have been updated to reference these new paths.
