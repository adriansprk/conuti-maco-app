# AI Agent Setup Guide for MaCo API Documentation

This guide explains how to set up and use the MaCo API documentation schemas with AI agents.

**Entry Point**: Use this guide when you start with a **specific MaKo message or BDEW process ID** (e.g., "55078", "START_LIEFERBEGINN").  
**Alternative Entry Point**: If you have a business goal, start with [`BUSINESS_PROCESS_MAP.md`](./BUSINESS_PROCESS_MAP.md) instead.

## 📁 Workspace Structure

```
maco_agent_workspace/
├── BUSINESS_PROCESS_MAP.md          # ⭐ START HERE: Business concept → Process mapping
├── llm.txt                          # ⭐ Documentation index (maps BDEW IDs to docs)
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
1. BUSINESS_PROCESS_MAP.md - Business concept to process mapping (START HERE for business goal discovery)
2. llm.txt - Documentation index (use to find which docs you need)
3. docs-offline/ - 232 offline documentation files (Prozessübersicht, process descriptions, EBD diagrams)
4. maco-edi-testfiles/ - EDI test files showing real-world message examples (inbound/outbound, .edi and .json formats)
5. _build/bo4e-openapi.min.json - Complete BO4E data structures
6. _build/macoapp-schreiben.min.json - Write operations schema (outbound)
7. _build/macoapp-lesen.min.json - Read operations schema (inbound)
8. _build/macoapp-trigger.min.json - Trigger events schema (outbound)
9. _build/maloident-macoapp.min.json - MaloIdent requests (outbound)
10. _build/maloident-lieferant.min.json - MaloIdent responses (inbound webhook)
11. pythons/createPiFromTemplater/templater/yaml_output/[ID].yaml - Business rules
12. macoapp-schreiben/components/requestBodies/PIs/PI_[ID].yml - Process schemas

Your Goals:
- Help discover which processes are needed for business goals
- Identify required data fields and backend service requirements
- Construct valid API payloads for specific market processes
- Map business concepts to technical implementations
```

### Documentation Index (`llm.txt`)

The `llm.txt` file in the workspace root provides a **documentation map** that:
- Maps BDEW Process IDs (e.g., 55078) to human-readable documentation URLs
- Links to detailed process descriptions on `doc.macoapp.de` (online)
- Provides context about roles (LF, NB, MSB) and business processes
- Includes references to BO4E objects and API endpoints

**Example entries:**
- `Prüfi > UTILMD-Strom [55078]` → Links to process documentation
- `Objekte [Marktlokation]` → Links to BO4E object documentation
- `Trigger (MACO APP) [Lieferbeginn]` → Links to API endpoint docs

**✅ Important**: The documentation markdown files linked in `llm.txt` are **now available offline** in `docs-offline/` directory (232 files downloaded).

**How to use with schemas:**
1. Find the BDEW ID or process name in `llm.txt` to get documentation context
2. Extract the filename from the URL (e.g., `prozessübersicht-860885m0.md`)
3. Read the downloaded file from `docs-offline/` directory
4. Use the corresponding YAML files (`yaml_output/`, `PIs/`) for technical structure
5. Cross-reference with BO4E schemas (`_build/bo4e-openapi.min.json`) for data types
6. Check `docs-offline/enhanced-index.json` for programmatic lookups (optional)

### Workflow for Building Payloads

1. **Identify the BDEW Process ID** (e.g., 55078)
2. **Check Documentation**: `llm.txt` → Find `[55078]` to get process context and documentation URL
3. **Check Example Messages**: `maco-edi-testfiles/inbound/` or `outbound/` → Find `55078_*.json` for real-world examples
4. **Check Business Rules**: `yaml_output/55078.yaml` for mandatory fields and validation rules
5. **Check Process Schema**: `PIs/PI_55078.yml` for OpenAPI request structure
6. **Cross-reference BO4E Schema**: `bo4e-openapi.min.json` for data types and object definitions
7. **Build Payload**: Combine mandatory fields with correct types, using test files as examples

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
2. **Use `llm.txt`** to find which documentation files you need
3. **Read workflow docs** from `docs-offline/` (Prozessübersicht files)
4. **Check business rule YAMLs** (`yaml_output/[ID].yaml`) for mandatory fields
5. **Review process schemas** (`PIs/PI_[ID].yml`) for API structure
6. **Cross-reference BO4E schema** (`bo4e-openapi.min.json`) for data types
7. **Map to backend requirements** - What data to collect, what services to build

### For Technical Implementation (Entry Point 2: Specific Message/BDEW ID)
1. **Start with `AI_AGENT_SETUP.md`** - Technical reference for specific messages
2. **Use `llm.txt`** to find documentation for the specific BDEW ID
3. **Read process documentation** from `docs-offline/` (process descriptions, workflows)
4. **Use `bo4e-openapi.min.json`** for understanding data structures
5. **Use business rule YAMLs** (`yaml_output/[ID].yaml`) to identify mandatory fields
6. **Cross-reference** with process-specific schemas (`PIs/PI_[ID].yml`)
7. **Validate** against BO4E types before constructing payloads
8. **Build payload** and implement backend service

## 📝 Notes

- All `.min.json` files are now **formatted** (pretty-printed) despite the name
- The build process uses `@redocly/openapi-cli` for validation
- Warnings are informational and don't affect output quality
- Schemas are automatically rebuilt when source files change

