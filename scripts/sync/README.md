# External Repository Sync System

This directory contains scripts and configuration for tracking and syncing changes from external repositories (like `maco-api-documentation`) that affect our generated files like `PROCESS_GRAPH.json`.

## Problem

External repositories (`maco-api-documentation`, `docs-offline`) will change as Conuti's documentation progresses. We need to:

1. **Track changes** in external repos
2. **Detect when updates are needed** for our generated files
3. **Update PROCESS_GRAPH.json** and other generated files accordingly
4. **Maintain version history** of what we've synced

## Files

- `version-tracker.json` - Tracks versions and sync status of external repos
- `check-changes.sh` - Checks for changes in external repos
- `sync-changes.sh` - Syncs changes and updates tracking metadata
- `rebuild-schemas.sh` - Rebuilds formatted JSON schemas (when build script changes)
- `update-process-graph-minimal.py` - Generates minimal PROCESS_GRAPH.json index (pointing only, no interpretation)

## Usage

### Check for Changes

```bash
./scripts/sync/check-changes.sh
```

This will:
- Check if `maco-api-documentation` has new commits
- Check if `docs-offline` has new files
- Report what needs updating

### Sync Changes

```bash
./scripts/sync/sync-changes.sh
```

This will:
- Update version tracking metadata
- Update PROCESS_GRAPH.json generation timestamp
- Report what was synced

### Rebuild Schemas (When Build Script Changes)

```bash
# When build script (scripts/build-openapi-json.sh) changes
./scripts/sync/rebuild-schemas.sh
```

This will:
- Run the build script to regenerate `_build/*.min.json` files
- Ensure schemas are formatted (readable, not minified)
- Verify dependencies (jq, npx) are available

**Why**: The build script uses `jq` to format JSON files. If the script changes, schemas may need regeneration.

### Update Documentation and PROCESS_GRAPH.json

**Manual workflow** (keeps separation clean):

```bash
# Step 1: Download markdown files (if llm.txt updated)
./scripts/download-docs.sh

# Step 2: Regenerate minimal index
python3 scripts/sync/update-process-graph-minimal.py
```

This will:
- Use `docs/llm.txt` (manually downloaded from doc.macoapp.de)
- Download/update markdown files to `docs-offline/`
- Generate minimal `PROCESS_GRAPH.json` index (pointing to source files only)

**Note**: `llm.txt` is **manually downloaded** from `doc.macoapp.de`, not from `maco-api-documentation` repo. See `LLM_TXT_NOTE.md` for details.

**Philosophy**: Scripts only point to files. Agents interpret source docs.

## Version Tracking

The `version-tracker.json` file tracks:

- **Last sync timestamp** for each external repo
- **Last commit hash** (for git repos)
- **File counts** (for non-git repos)
- **What files affect what** (mapping of external files to our generated files)
- **Sync actions** (what to do when files change)

## Workflow

1. **External repo updates** (e.g., Conuti releases new API version)
2. **Pull/update external repo** in workspace
3. **Run `check-changes.sh`** to see what changed
   - ⚠️ If build script changed, you'll see a warning
4. **If build script changed**: Run `rebuild-schemas.sh` to regenerate formatted schemas
5. **If online docs updated**: 
   - Manually download updated `llm.txt` from `doc.macoapp.de` → `docs/llm.txt`
   - Run `./scripts/download-docs.sh` to download markdown files
   - Run `python3 scripts/sync/update-process-graph-minimal.py` to regenerate index
6. **Run `sync-changes.sh`** to update tracking
7. **Test** updated schemas and PROCESS_GRAPH.json
8. **Commit** changes

## Build Script Tracking

The build script (`maco-api-documentation/scripts/build-openapi-json.sh`) is **critical** because it:
- Formats JSON files using `jq` to make them readable (not minified)
- Generates all `_build/*.min.json` files
- If it changes, schemas may need regeneration

**Detection**: `check-changes.sh` will warn if the build script changed.

**Action**: Run `rebuild-schemas.sh` to regenerate schemas with the updated script.

## Build Script Details

The build script (`maco-api-documentation/scripts/build-openapi-json.sh`) performs:

1. **Bundles** YAML files into JSON using `@redocly/openapi-cli`
2. **Formats** JSON using `jq` to make it readable (not minified)
3. **Outputs** formatted files as `*.min.json` (despite the name, they're formatted)

**Key line**: `jq . "${OUTPUT_DIR}/${output_filename}.json" > "${OUTPUT_DIR}/${output_filename}.min.json"`

If this formatting step changes, all `_build/*.min.json` files need regeneration.

## Documentation Workflow

**`llm.txt`** is manually downloaded from `doc.macoapp.de` (not from `maco-api-documentation` repo):

1. **Download** `llm.txt` from online docs → `docs/llm.txt`
2. **Download markdown files**: `./scripts/download-docs.sh` (uses URLs from `llm.txt`)
3. **Generate PROCESS_GRAPH.json**: Creates minimal index pointing to source files
4. **Agents read source files**: Extract meaning, relationships, details from actual docs

See `LLM_TXT_NOTE.md` for complete workflow details.

## Scripts

### `update-process-graph-minimal.py`

**Purpose**: Generate minimal PROCESS_GRAPH.json index (pointing only, no interpretation)

**Philosophy**: "Point, don't interpret" - Scripts point to source files, agents interpret them.

**Usage**:
```bash
python3 scripts/sync/update-process-graph-minimal.py
```

**Dependencies**: None (pure Python, no external libraries needed)

**What it does** (pointing only):
1. **Reads markdown files** from `docs-offline/` (234+ files)
2. **Extracts factual references**:
   - BDEW IDs (Prüfidentifikatoren) from PI_ references, Tab titles, Card titles, Mermaid comments
   - Trigger event names from XML Card structures
   - Process names from filenames
3. **Creates indexes**:
   - `by_bdew_id`: BDEW ID → list of files mentioning it
   - `by_trigger`: Trigger → list of files with this trigger
   - `by_process_name`: Process name → list of files for this process
   - `by_filename`: Filename → metadata (has Mermaid, is Prozessübersicht)
4. **Outputs minimal index**: `docs/entry-points/PROCESS_GRAPH.json`

**What it does NOT do** (interpretation - left to agents):
- ❌ Infer triggers, roles, prerequisites
- ❌ Process relationships or dependencies
- ❌ Business scenarios
- ❌ Process definitions with interpreted fields

**Output**: `docs/entry-points/PROCESS_GRAPH.json` (minimal index)

**Example Output**:
```
🔨 Generating minimal PROCESS_GRAPH.json (source file index only)...
📚 Reading markdown files and extracting factual references...
💾 Writing PROCESS_GRAPH.json...
  ✅ Written to: docs/entry-points/PROCESS_GRAPH.json
📊 Summary:
  ✅ Files indexed: 234
  ✅ BDEW IDs found: 143
  ✅ Triggers found: 17
  ✅ Process names: 158
```

See `MINIMAL_INDEX_PHILOSOPHY.md` for the rationale behind this approach.

## Future Enhancements

- [ ] Automated diff detection for schema files
- [ ] Automatic schema rebuild on build script changes
- [ ] Automatic PROCESS_GRAPH.json regeneration on schema changes
- [ ] Validation of generated PROCESS_GRAPH.json against source files
- [ ] CI/CD integration to auto-sync on external repo updates
- [ ] Change log generation showing what was updated

## Integration with CI/CD

```yaml
# Example GitHub Actions workflow
on:
  schedule:
    - cron: '0 0 * * *'  # Daily check
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check for changes
        run: ./scripts/sync/check-changes.sh
      - name: Sync changes
        run: ./scripts/sync/sync-changes.sh
      - name: Regenerate PROCESS_GRAPH.json
        run: python3 scripts/sync/update-process-graph-minimal.py
      - name: Create PR if changes
        # Create PR if PROCESS_GRAPH.json changed
```
