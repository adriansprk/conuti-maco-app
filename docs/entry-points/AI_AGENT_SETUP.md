# AI Agent Setup Guide for MaCo API Documentation

This guide explains how to set up and use the MaCo API documentation schemas with AI agents.

**Entry Point**: Use this guide when you start with a **specific MaKo message or BDEW process ID** (e.g., "55078", "START_LIEFERBEGINN").  
**Alternative Entry Point**: If you have a business goal, start with [`BUSINESS_PROCESS_MAP.md`](./BUSINESS_PROCESS_MAP.md) instead.

**Documentation source order:** This workspace is Strom only. Select a format version and use `scripts/find-documentation.py` to find a versioned new process or interface page under `docs-offline/`. The older `docs-supplemental/` snapshot remains for applicable Mermaid branches, implementation PNGs, and historical or operational details. `PROCESS_GRAPH.json` v4 points to both sources and identifies provenance, version, role, industry and document type; it is a discovery index, not a process graph with inferred dependencies.

## 📁 Workspace Structure

```
maco_agent_workspace/
├── docs/
│   └── entry-points/
│       ├── PROCESS_GRAPH.json               # ⭐ INDEX: lookup indexes to source docs (minimal, discovery-only in this repo)
│       ├── BUSINESS_PROCESS_MAP.md          # ⭐ Entry Point 1: Business concept → process mapping
│       └── AI_AGENT_SETUP.md                # ⭐ Entry Point 2: This file
├── docs/dokumentation/llms.txt            # New site's curated index
├── docs/dokumentation/llms-index.txt      # New site's complete index
├── docs-offline/                          # New versioned documentation mirror
├── docs-supplemental/llm.txt              # Older site's separate index
├── docs-supplemental/                      # Offline process docs (Mermaid diagrams, Prozessübersicht, EBD markdown)
│   ├── prozessdiagramme-png/          # 54 PNG diagrams (technical HOW)
│   │   └── INDEX.md                   # Text index for PNG discovery
│   └── ...                            # Process markdown docs
├── ebd-diagrams/                      # EBD decision trees (JSON/DOT/SVG/PUML) (validation WHAT)
├── maco-api-documentation/          # Main API documentation
│   ├── _build/                      # Generated consolidated schemas (READ THESE)
│   │   ├── bo4e-openapi.min.json   # ⭐ PRIMARY: Complete BO4E schema (formatted)
│   │   ├── macoapp-lesen.min.json  # Read operations schema
│   │   ├── macoapp-schreiben.min.json # Write operations schema
│   │   └── events-openapi.min.json # Event triggers schema
│   ├── pythons/createPiFromTemplater/templater/yaml_output/
│   │   └── [BDEW_ID].yaml          # Business rules (e.g., 55078.yaml)
│   └── macoapp-schreiben/components/requestBodies/PIs/
│       └── PI_[BDEW_ID].yml         # Process-specific schemas
├── bo4e-schema/                     # BO4E base schemas (source)
└── cdoc-schema/                     # CDoc schemas
```

## 🎯 Key Files for AI Agents

### 1. Master Schema Files (Primary Reference)

**Core Schemas**:
- **`_build/bo4e-openapi.min.json`** - Complete BO4E schema with all data structures (317KB)
- **`_build/macoapp-schreiben.min.json`** - Write operations (3.8MB, comprehensive)
- **`_build/macoapp-lesen.min.json`** - Read operations (317KB)
- **`_build/macoapp-trigger.min.json`** - Trigger events (outbound to Conuti)
- **`_build/events-openapi.min.json`** - Event triggers (409KB, alternative/legacy)

**MaloIdent Schemas**:
- **`_build/maloident-macoapp.min.json`** - Send MaloIdent requests (outbound)
- **`_build/maloident-lieferant.min.json`** - Receive MaloIdent responses (inbound webhook)
- **`_build/maloident-netzbetreiber.min.json`** - NB operations (reference only)

**Why `.min.json`?** Despite the name, these are now **formatted** (not minified) for readability.

**API Directions**:
- **Outbound**: Your backend → Conuti API (trigger events, send data)
- **Inbound**: Conuti → Your backend (webhooks, read operations)

### 2. Business Rules (BDEW Process Definitions)
- **Location**: `pythons/createPiFromTemplater/templater/yaml_output/[BDEW_ID].yaml`
- **136 YAML files** covering different BDEW processes (e.g., 55078.yaml)
- These define **mandatory fields** and **business logic** for each process

### 3. Process-Specific Schemas
- **Location**: `macoapp-schreiben/components/requestBodies/PIs/PI_[BDEW_ID].yml`
- These are the OpenAPI request body schemas for specific processes

## 🔧 Build Process

The schemas are built using:
- **Tool**: `@redocly/openapi-cli` (via npx, no global install needed)
- **Process**: Bundles multiple YAML files into single JSON files
- **Output**: Formatted JSON files in `_build/` directory

### Building Schemas

```bash
cd maco-api-documentation
nodemon  # Watches for changes and auto-rebuilds
# OR manually:
./scripts/build-openapi-json.sh
```

### Build Warnings

The build process shows **197 validation warnings** about `no-$ref-siblings` in the external BO4E schema. These are:
- ✅ **Informational only** - don't affect functionality
- ✅ **From external schema** - not your code
- ✅ **Build still succeeds** - output is valid

**Recommendation**: Keep warnings visible to catch schema issues early.

## 🤖 AI Agent Instructions

### System Context Prompt

```
You are an expert AI assistant for the German Energy Market (MaKo), specifically 
for the Conuti MaCo API.

Your Resources:
1. PROCESS_GRAPH.json - **Minimal discovery index** (machine-readable pointers to source docs via `indexes.*`)
2. BUSINESS_PROCESS_MAP.md - Business concept to process mapping (START HERE for business goal discovery)
3. llm.txt - Documentation index (use to find which docs you need)
4. docs-offline/ - 3,447 Strom/shared versioned pages; docs-supplemental/ - 346 older Strom/shared pages retained for branch logic
5. maco-edi-testfiles/ - EDI test files showing real-world message examples (inbound/outbound, .edi and .json formats)
6. _build/bo4e-openapi.min.json - Complete BO4E data structures
7. _build/macoapp-schreiben.min.json - Write operations schema (outbound)
8. _build/macoapp-lesen.min.json - Read operations schema (inbound)
9. _build/macoapp-trigger.min.json - Trigger events schema (outbound)
10. _build/maloident-macoapp.min.json - MaloIdent requests (outbound)
11. _build/maloident-lieferant.min.json - MaloIdent responses (inbound webhook)
12. pythons/createPiFromTemplater/templater/yaml_output/[ID].yaml - Business rules
13. macoapp-schreiben/components/requestBodies/PIs/PI_[ID].yml - Process schemas

Your Goals:
- Help discover which processes are needed for business goals
- Identify required data fields and backend service requirements
- Construct valid API payloads for specific market processes
- Map business concepts to technical implementations
```

### Documentation indexes

- `docs/dokumentation/llms.txt`: curated new-site index.
- `docs/dokumentation/llms-index.txt`: scoped index for the 3,447 mirrored Strom/shared pages.
- `docs-offline/index.json` and `enhanced-index.json`: local exact-path and Prüfi/trigger/process lookup for the new site.
- `docs-supplemental/llm.txt`: separate old-site index. Its offline pages and indexes are under `docs-supplemental/`.
- `PROCESS_GRAPH.json`: combined paths to both sources; each `by_path` entry identifies its source and version.

Read the new page first for the applicable format version. Use old Mermaid or PNG material for conditions and architecture where it adds detail, then verify payloads with local YAML and test files.

### Workflow for Building Payloads

1. **Identify the BDEW Process ID** (e.g., 55078)
2. **Discover the right source docs**: `docs/entry-points/PROCESS_GRAPH.json` → `indexes.by_bdew_id["55078"]`; read the `docs-offline/...` page for the applicable version and matching `docs-supplemental/...` Mermaid if needed.
3. **Check Documentation**: `docs/dokumentation/llms.txt` or `llms-index.txt` for the new-site source URL.
4. **Check Example Messages** for the selected version when available. Existing `v202510` outbound JSON and inbound EDI fixtures are examples for that version only; label them as older when working with 202604 or 202610.
5. **Check Business Rules**: `yaml_output/55078.yaml` for mandatory fields and validation rules
6. **Check Process Schema**: `PIs/PI_55078.yml` for OpenAPI request structure
7. **Cross-reference BO4E Schema**: `bo4e-openapi.min.json` for data types and object definitions
8. **Build Payload**: Combine mandatory fields with correct types, using test files as examples

### Using PROCESS_GRAPH.json for Fast Lookup

```javascript
// NOTE (this repo, PROCESS_GRAPH v4.0.0-strom-source-index):
// - Use `indexes.*` for discovery.
// - `processes`, `business_scenarios`, `ebd_reference` exist but are currently empty.
// - Read versioned docs-offline pages first; use docs-supplemental Mermaid for conditional branches.

// Find files mentioning a BDEW Prüfi / Prozess-ID
PROCESS_GRAPH.indexes.by_bdew_id["55077"]  // → ["docs-offline/...", "docs-supplemental/...", ...]

// Find files by trigger event
PROCESS_GRAPH.indexes.by_trigger["START_LIEFERBEGINN"]  // → source paths

// Find process docs by name (normalized)
PROCESS_GRAPH.indexes.by_process_name["lieferbeginn"]  // → versioned process paths and legacy Mermaid paths

// Find docs by filename (when you already know it)
PROCESS_GRAPH.indexes.by_filename["prozessübersicht-860885m0.md"]  // → list of matching source paths
```

⚠️ Note: `PROCESS_GRAPH.business_scenarios` is currently empty in this repo. Use `BUSINESS_PROCESS_MAP.md` (and the linked offline docs) for scenario narratives.

### Example: Process 55078

```yaml
# Step 1: Check business rules
pythons/createPiFromTemplater/templater/yaml_output/55078.yaml

# Step 2: Check process schema  
macoapp-schreiben/components/requestBodies/PIs/PI_55078.yml

# Step 3: Reference BO4E types
_build/bo4e-openapi.min.json (search for "MESSLOKATION", etc.)
```

## 📊 Schema File Sizes

**Core Schemas**:
- `bo4e-openapi.min.json`: 317KB
- `macoapp-schreiben.min.json`: 3.8MB (comprehensive write operations)
- `macoapp-lesen.min.json`: 317KB
- `macoapp-trigger.min.json`: ~409KB
- `events-openapi.min.json`: 409KB

**MaloIdent Schemas**:
- `maloident-macoapp.min.json`: ~295KB
- `maloident-lieferant.min.json`: ~331KB
- `maloident-netzbetreiber.min.json`: ~342KB

## ✅ Current Setup Status

- ✅ Schemas are **formatted** (not minified) for AI readability
- ✅ Single consolidated files for easy consumption
- ✅ Validation enabled (catches schema issues)
- ✅ Auto-rebuild on changes (nodemon)
- ✅ 136 business rule YAML files available

## 🚀 Recommendations for AI Agents

### For Business Discovery (Entry Point 1: Business Goal)
1. **Start with `BUSINESS_PROCESS_MAP.md`** - Maps business goals to processes
2. **Use `PROCESS_GRAPH.json` (`indexes.*`)** - Find the right `docs-supplemental/...` sources fast
3. **Derive dependencies/prerequisites** - Read new process prose and matching legacy Mermaid in `docs-supplemental/` (follow any `ref` links)
4. **Use `llm.txt`** to find which documentation files you need
5. **Read workflow docs** from `docs-supplemental/` (Prozessübersicht files)
6. **Check business rule YAMLs** (`yaml_output/[ID].yaml`) for mandatory fields
7. **Review process schemas** (`PIs/PI_[ID].yml`) for API structure
8. **Cross-reference BO4E schema** (`bo4e-openapi.min.json`) for data types
9. **Map to backend requirements** - What data to collect, what services to build

### For Technical Implementation (Entry Point 2: Specific Message/BDEW ID)
1. **Start with `PROCESS_GRAPH.json` (`indexes.*`)** - Use `indexes.by_bdew_id` / `indexes.by_trigger` / `indexes.by_process_name` for discovery
2. **Derive dependencies/prerequisites** - Read the referenced `docs-supplemental/...` sources (Mermaid + prose)
3. **Use `llm.txt`** to find documentation for the specific BDEW ID
4. **Read process documentation** from `docs-supplemental/` (process descriptions, workflows)
5. **Use `bo4e-openapi.min.json`** for understanding data structures
6. **Use business rule YAMLs** (`yaml_output/[ID].yaml`) to identify mandatory fields
7. **Cross-reference** with process-specific schemas (`PIs/PI_[ID].yml`)
8. **Validate** against BO4E types before constructing payloads
9. **Build payload** and implement backend service

## 📝 Notes

- All `.min.json` files are now **formatted** (pretty-printed) despite the name
- The build process uses `@redocly/openapi-cli` for validation
- Warnings are informational and don't affect output quality
- Schemas are automatically rebuilt when source files change
