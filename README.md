# MaCo API Documentation Workspace

This workspace helps you enable your backend to use the MaCo API to communicate MaKo (Market Communication) messages into the market and receive results from the market.

## 🎯 Goal

**Enable your backend to:**
- Send MaKo messages to the market via Conuti MaCo API (outbound)
- Receive results/responses from the market via webhooks (inbound)
- Handle both business-driven scenarios and specific message types

## 🚀 Two Entry Points

### Entry Point 1: Business Goal → Implementation
**When**: You have a business goal (e.g., "register new customer", "cancel contract")

**Start Here**: [`BUSINESS_PROCESS_MAP.md`](./BUSINESS_PROCESS_MAP.md)
- Maps business goals to market processes
- Shows required workflows and dependencies
- Identifies what data to collect and what services to build

**Example**: "I want to register a new customer"
→ Read BUSINESS_PROCESS_MAP.md → Find MaloIdent → Lieferbeginn workflow → Implement

### Entry Point 2: Specific MaKo Message → Implementation
**When**: You have a specific BDEW process ID or MaKo message (e.g., "55078", "START_LIEFERBEGINN")

**Start Here**: [`AI_AGENT_SETUP.md`](./AI_AGENT_SETUP.md)
- Technical setup and schema reference
- API structure, data types, payload building
- Process-specific implementation details

**Example**: "I need to implement process 55078"
→ Read AI_AGENT_SETUP.md → Check schemas → Build payload → Implement

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

### From Business Goal:
```
Business Goal (e.g., "register customer")
    ↓
BUSINESS_PROCESS_MAP.md → Find processes needed
    ↓
llm.txt → Find documentation for each process
    ↓
docs-offline/ → Read workflow documentation (Prozessübersicht)
    ↓
yaml_output/ + PIs/ → Check mandatory fields and API structure
    ↓
maco-edi-testfiles/ → Check real-world examples
    ↓
_build/bo4e-openapi.min.json → Understand data types
    ↓
Implement backend services
```

### From Specific Message:
```
Specific BDEW ID or Message (e.g., "55078", "START_LIEFERBEGINN")
    ↓
AI_AGENT_SETUP.md → Understand technical requirements
    ↓
llm.txt → Find documentation for this process
    ↓
docs-offline/ → Read process documentation
    ↓
yaml_output/[ID].yaml → Check business rules
    ↓
PIs/PI_[ID].yml → Check API schema
    ↓
maco-edi-testfiles/ → Check example messages
    ↓
_build/bo4e-openapi.min.json → Understand data types
    ↓
Build payload and implement
```

## 📚 Structure

```
maco_agent_workspace/
├── BUSINESS_PROCESS_MAP.md    ⭐ Business goal discovery
├── AI_AGENT_SETUP.md          ⭐ Technical implementation
├── llm.txt                    ⭐ Documentation index
├── maco-api-documentation/
│   ├── docs-offline/          ⭐ 232 offline documentation files
│   ├── _build/                ⭐ Formatted JSON schemas
│   ├── yaml_output/           ⭐ Business rules (136 files)
│   └── macoapp-schreiben/components/requestBodies/PIs/
│       └── PI_[ID].yml        ⭐ Process schemas
├── maco-edi-testfiles/        ⭐ 2,549 EDI test files (real-world examples)
```

## 🎯 Common Tasks

### "I want to register a new customer"
→ Read `BUSINESS_PROCESS_MAP.md` → Scenario 1: New Customer Signs Up

### "What data do I need for process 55078?"
→ Read `AI_AGENT_SETUP.md` → Check `yaml_output/55078.yaml` → Reference `bo4e-openapi.min.json`

### "How do I implement Kündigung workflow?"
→ Read `BUSINESS_PROCESS_MAP.md` → Find Kündigung → Use `llm.txt` → Read `docs-offline/prozessübersicht-860885m0.md`

### "I received a specific MaKo message, what do I do?"
→ Read `AI_AGENT_SETUP.md` → Find message type → Check schemas → Implement handler

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
