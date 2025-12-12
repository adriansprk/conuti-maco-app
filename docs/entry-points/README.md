# Entry Point Documentation

This directory contains the main entry point files for the MaCo API workspace.

## Files

- **`BUSINESS_PROCESS_MAP.md`** - Entry Point 1: Business goal discovery
  - Maps business goals to MaKo processes
  - Use when you have a business goal (e.g., "register customer")
  
- **`AI_AGENT_SETUP.md`** - Entry Point 2: Technical implementation
  - Technical setup and schema reference
  - Use when you have a specific BDEW process ID or message
  
- **`PROCESS_GRAPH.json`** - Machine-readable process dependency graph
  - Fast lookup by BDEW ID, trigger event, or role
  - Process sequences, prerequisites, and dependencies
  - Business scenarios with step-by-step workflows

## Usage

### For Business Discovery

1. Start with `BUSINESS_PROCESS_MAP.md`
2. Find your business scenario
3. Use `PROCESS_GRAPH.json` to check dependencies
4. Follow the workflow

### For Technical Implementation

1. Start with `AI_AGENT_SETUP.md`
2. Lookup process in `PROCESS_GRAPH.json`
3. Check schemas and business rules
4. Build implementation

## Maintenance

These files are **generated/curated** from external sources:

- `PROCESS_GRAPH.json` - Generated from:
  - `docs-offline/prozessübersicht-*.md` (workflow sequences)
  - `maco-api-documentation/_build/*.min.json` (API schemas)
  - `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/*.yaml` (business rules)

- `BUSINESS_PROCESS_MAP.md` - Curated business scenarios
- `AI_AGENT_SETUP.md` - Technical reference guide

### Updating After External Repo Changes

When external repos (`maco-api-documentation`, `docs-offline`) are updated:

1. **Check for changes**: `./scripts/sync/check-changes.sh`
2. **Sync changes**: `./scripts/sync/sync-changes.sh`
3. **Regenerate PROCESS_GRAPH.json**: `./scripts/sync/update-process-graph.py` (when implemented)
4. **Update entry point docs** if needed (manual review)

See `scripts/sync/README.md` for detailed sync workflow.
