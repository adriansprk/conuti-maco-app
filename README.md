# MaCo API Documentation Workspace

This workspace helps you enable your backend to use the MaCo API to communicate MaKo (Market Communication) messages into the market and receive results from the market.

## 🤖 AI Agent Context (Git-Based + BMAD-METHOD Structure)

This workspace includes an **Agentic Context** that enables AI assistants (like Cursor) to understand MaKo processes, dependencies, and implementation patterns. The context is organized using **BMAD-METHOD's subdirectory structure** for scalability and specialization.

**Setup**: When you clone this repository, Cursor will automatically load the agent rules. No additional configuration needed!

**Rule Structure** (in `.cursor/rules/`):
- **Global Rules** (`global-rules/`): Always applied core context
- **Domain Rules** (`domain-rules/`): Business discovery & technical implementation workflows
- **Validation Rules** (`validation-rules/`): Message validation & building agents
- **Visualization Rules** (`visualization-rules/`): Mandatory Mermaid diagram requirements

**Key Features**:
- ✅ **Mandatory Visualizations**: Always creates Mermaid diagrams for processes (sequences, flows, fields)
- ✅ **Validation Agent**: Validates messages against schemas, business rules, and backend capabilities
- ✅ **Builder Agent**: Pre-creates messages from database entries, prepares for Conuti testing
- ✅ **Future-Ready**: Structured for database integration and Conuti API testing

**What's Included**:
- Entry point documentation (`docs/entry-points/`):
  - Process dependency graph (`PROCESS_GRAPH.json`)
  - Business process mapping (`BUSINESS_PROCESS_MAP.md`)
  - Technical setup guide (`AI_AGENT_SETUP.md`)
- Documentation index (`docs/llm.txt`)
- 232 offline documentation files (`docs-offline/`)
- 2,549 EDI test files (`maco-edi-testfiles/`)
- Sync system (`scripts/sync/`) for tracking external repo changes

**For Teams**: 
- Rules are version-controlled and shared automatically via Git
- Organized by category for easy maintenance and discovery
- Scalable structure supports adding specialized agents
- See [`.cursor/README.md`](.cursor/README.md) for detailed documentation

## 🎯 Goal

**Enable your backend to:**
- Send MaKo messages to the market via Conuti MaCo API (outbound)
- Receive results/responses from the market via webhooks (inbound)
- Handle both business-driven scenarios and specific message types

## 🚀 Getting Started

### Prerequisites

- **Cursor IDE** (version 0.45+) - For AI agent support
- **Git** - To clone and sync the repository
- **Python 3** - For sync scripts (optional, only if updating documentation)
- **jq** and **npx** - For schema rebuilding (optional, only if updating schemas)

### Initial Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd maco_agent_workspace
   ```

2. **Open in Cursor**:
   - Open the workspace folder in Cursor IDE
   - Cursor will automatically load the AI agent rules (no configuration needed!)
   - If rules don't load, restart Cursor

3. **Verify setup** (optional):
   ```bash
   # Check that key files exist
   ls docs/entry-points/BUSINESS_PROCESS_MAP.md
   ls docs/entry-points/AI_AGENT_SETUP.md
   ls docs/entry-points/PROCESS_GRAPH.json
   ```

### Quick Start Examples

#### Example 1: Using AI Agent (Recommended)

**With Cursor AI Agent**:
1. Open Cursor chat (Cmd/Ctrl+L) or use Cmd/Ctrl+K
2. Ask: *"I want to register a new customer, what processes do I need?"*
   - The AI agent will reference `BUSINESS_PROCESS_MAP.md` and show you the workflow
3. Ask: *"Show me the sequence diagram for process 55077"*
   - The AI agent will create Mermaid visualizations automatically
4. Ask: *"What fields are required for START_LIEFERBEGINN?"*
   - The AI agent will check schemas and business rules for you

**Benefits**: The AI agent automatically:
- ✅ Reads documentation files before answering
- ✅ Creates visualizations (Mermaid diagrams)
- ✅ Validates against schemas and business rules
- ✅ Cites source files

#### Example 2: Manual Discovery

**For Business Goals**:
1. Read [`docs/entry-points/BUSINESS_PROCESS_MAP.md`](docs/entry-points/BUSINESS_PROCESS_MAP.md)
2. Find your business scenario (e.g., "New Customer Signs Up")
3. Follow the workflow steps
4. Use `docs/llm.txt` to find specific documentation files
5. Check example messages in `maco-edi-testfiles/`

**For Specific Messages**:
1. Read [`docs/entry-points/AI_AGENT_SETUP.md`](docs/entry-points/AI_AGENT_SETUP.md)
2. Find your BDEW process ID (e.g., "55077")
3. Check schema: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55077.yml`
4. Check business rules: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55077.yaml`
5. Review example: `maco-edi-testfiles/outbound/v202510/utilmd/55077/1.json` (⚠️ Always use v202510)

### Understanding the Workspace

**Key Concepts**:
- **Role**: You are a **Lieferant (LF)** - electricity supplier
- **Direction**: 
  - **Outbound**: Your backend → Conuti API (triggers, requests) - BO4E JSON format
  - **Inbound**: Conuti → Your backend (webhooks, responses) - EDIFACT format
- **Process IDs**: BDEW Prüfidentifikatoren (5-digit numbers like "55077")
- **Message Formats**:
  - **Outbound**: `maco-edi-testfiles/outbound/v202510/` (JSON format)
  - **Inbound**: `maco-edi-testfiles/inbound/v202510/` (EDI format)
  - ⚠️ **Always use v202510** version directory, never v202404 (outdated)

### Verification Steps

**Test AI Agent Setup**:
1. Open Cursor chat
2. Ask: *"What is the workspace role?"*
   - Should mention: Lieferant (LF), MaCo API, MaKo messages
3. Ask: *"Show me process 55077"*
   - Should create sequence diagram and flowchart
4. Ask: *"What fields are required for START_LIEFERBEGINN?"*
   - Should reference schemas and business rules

**Test Documentation Access**:
```bash
# Check entry points exist
ls docs/entry-points/*.md

# Check schemas exist
ls maco-api-documentation/_build/*.min.json

# Check example files exist
ls maco-edi-testfiles/outbound/v202510/utilmd/55077/
```

### Next Steps

1. **Choose your entry point**:
   - Business goal? → Start with [`BUSINESS_PROCESS_MAP.md`](docs/entry-points/BUSINESS_PROCESS_MAP.md)
   - Specific message? → Start with [`AI_AGENT_SETUP.md`](docs/entry-points/AI_AGENT_SETUP.md)

2. **Explore the documentation**:
   - Use `docs/llm.txt` to find relevant documentation files
   - Read process documentation in `docs-offline/`
   - Check example messages in `maco-edi-testfiles/`

3. **Implement your backend**:
   - Follow the workflows in the entry point guides
   - Use schemas and business rules to build payloads
   - Reference example messages for structure

4. **Keep documentation updated** (optional):
   - See [`scripts/sync/README.md`](scripts/sync/README.md) for syncing external repos
   - Run `./scripts/sync/check-changes.sh` to check for updates

### Troubleshooting

**AI Agent Rules Not Loading**:
- Ensure Cursor version is 0.45+
- Restart Cursor after cloning
- Check `.cursor/rules/` directory exists
- See [`.cursor/SETUP.md`](.cursor/SETUP.md) for detailed troubleshooting

**Documentation Not Found**:
- Ensure you cloned the full repository (including submodules if any)
- Check that `docs-offline/` and `maco-api-documentation/` directories exist
- Run `./scripts/download-docs.sh` if documentation is missing

**Example Files Not Found**:
- ⚠️ Always use `v202510` directory (see [Understanding the Workspace](#understanding-the-workspace) above)
- Check `maco-edi-testfiles/outbound/v202510/` for outbound examples (JSON)
- Check `maco-edi-testfiles/inbound/v202510/` for inbound examples (EDI)

## 🚀 Two Entry Points

> **💡 Tip**: See [Getting Started](#-getting-started) above for detailed setup instructions and examples.

### Entry Point 1: Business Goal → Implementation
**When**: You have a business goal (e.g., "register new customer", "cancel contract")  
**Start Here**: [`BUSINESS_PROCESS_MAP.md`](docs/entry-points/BUSINESS_PROCESS_MAP.md)  
**See**: [Getting Started - Quick Start Examples](#quick-start-examples) for step-by-step guide

### Entry Point 2: Specific MaKo Message → Implementation
**When**: You have a specific BDEW process ID or MaKo message (e.g., "55078", "START_LIEFERBEGINN")  
**Start Here**: [`AI_AGENT_SETUP.md`](docs/entry-points/AI_AGENT_SETUP.md)  
**See**: [Getting Started - Quick Start Examples](#quick-start-examples) for step-by-step guide

## 📁 Key Files

| File | Purpose | When to Use |
|------|---------|-------------|
| `BUSINESS_PROCESS_MAP.md` | Business concept → Process mapping | **Business goal discovery, backend design** |
| `AI_AGENT_SETUP.md` | Technical setup guide | **Technical implementation, specific messages** |
| `llm.txt` | Documentation index (237 entries) | **Find which documentation you need** |
| `docs-offline/` | 232 offline documentation files | **Read workflow docs and process descriptions** |
| `maco-edi-testfiles/` | 2,549 EDI test files | **Real-world message examples (inbound/outbound)** |
| `_build/bo4e-openapi.min.json` | Complete BO4E schemas | **Data structure reference** |
| `yaml_output/[ID].yaml` | Business rules (136 files) | **Mandatory fields, validation** |
| `PIs/PI_[ID].yml` | Process API schemas | **API request/response structure** |

## 🔄 Typical Workflow

> **💡 Tip**: See [Getting Started - Quick Start Examples](#quick-start-examples) for detailed step-by-step instructions.

**From Business Goal** → `BUSINESS_PROCESS_MAP.md` → `llm.txt` → `docs-offline/` → `yaml_output/` + `PIs/` → `maco-edi-testfiles/` → `bo4e-openapi.min.json` → Implement

**From Specific Message** → `AI_AGENT_SETUP.md` → `llm.txt` → `docs-offline/` → `yaml_output/[ID].yaml` → `PIs/PI_[ID].yml` → `maco-edi-testfiles/` → `bo4e-openapi.min.json` → Implement

## 📚 Structure

```
maco_agent_workspace/
├── docs/
│   ├── entry-points/          ⭐ Entry point documentation
│   │   ├── BUSINESS_PROCESS_MAP.md    # Business goal discovery
│   │   ├── AI_AGENT_SETUP.md          # Technical implementation
│   │   └── PROCESS_GRAPH.json         # Process dependency graph
│   └── llm.txt                ⭐ Documentation index
├── .cursor/rules/             ⭐ AI agent rules (BMAD-METHOD structure)
├── scripts/sync/              ⭐ Sync system for external repos
├── maco-api-documentation/    # External repo (tracked)
│   ├── _build/                ⭐ Formatted JSON schemas
│   ├── yaml_output/           ⭐ Business rules (136 files)
│   └── macoapp-schreiben/components/requestBodies/PIs/
│       └── PI_[ID].yml        ⭐ Process schemas
├── docs-offline/              ⭐ 232 offline documentation files
└── maco-edi-testfiles/        ⭐ 2,549 EDI test files (real-world examples)
```

## 🎯 Common Tasks

| Task | Solution |
|------|----------|
| "I want to register a new customer" | `BUSINESS_PROCESS_MAP.md` → Scenario 1: New Customer Signs Up |
| "What data do I need for process 55078?" | `AI_AGENT_SETUP.md` → `yaml_output/55078.yaml` → `bo4e-openapi.min.json` |
| "How do I implement Kündigung workflow?" | `BUSINESS_PROCESS_MAP.md` → Find Kündigung → `llm.txt` → `docs-offline/prozessübersicht-860885m0.md` |
| "I received a specific MaKo message, what do I do?" | `AI_AGENT_SETUP.md` → Find message type → Check schemas → Implement handler |

## 📖 Documentation

- **Offline**: All 232 documentation pages are available in `docs-offline/`
- **Index**: Use `llm.txt` to find which documentation file you need
- **Workflows**: Prozessübersicht files show step-by-step API call sequences
- **Schemas**: All API schemas are in `_build/` directory (formatted JSON)

## 🔧 Backend Requirements

Your backend needs to support:

**Outbound (Your Backend → Conuti MaCo API)**:
- Trigger events (START_LIEFERBEGINN, START_KUENDIGUNG, etc.)
- Send MaloIdent requests
- Store process data

**Inbound (Conuti MaCo API → Your Backend)**:
- Webhook endpoints for MaloIdent responses
- Webhook endpoints for process data updates
- Read operations (if needed)

See `BUSINESS_PROCESS_MAP.md` and `AI_AGENT_SETUP.md` for detailed requirements.
