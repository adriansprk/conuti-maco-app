# Business Process Discovery Guide

This guide helps you discover which market processes and APIs you need based on **business goals** rather than technical process IDs.

**Entry Point**: Use this guide when you start with a **business goal** (e.g., "register customer", "cancel contract").
**Alternative Entry Point**: If you have a specific MaKo message/BDEW ID, start with [`AI_AGENT_SETUP.md`](./AI_AGENT_SETUP.md) instead.

**Machine-Readable Version**: See [`PROCESS_GRAPH.json`](./PROCESS_GRAPH.json) for structured process dependencies, sequences, and business scenarios optimized for programmatic access.

## 🎯 Common Business Scenarios

### Scenario 1: New Customer Signs Up for Electricity Contract

**Business Goal**: Register a new customer who wants to receive electricity from us

**Required Processes**:
1. **MaloIdent (Market Location Identification)**
   - **Trigger**: `START_MALOIDENT` (outbound)
   - **Purpose**: Identify the market location (MaLo) if customer doesn't know their MaLo-ID
   - **Your Role**: Lieferant (LF)
   - **Documentation**: `llm.txt` → "Lieferant [Malo-Ident (Rolle LF)]"
   - **API**: `maloident-macoapp/maloident-macoapp.yaml` → Send request
   - **Webhook**: `maloident-lieferant/maloident-lieferant.yaml` → Receive response
   - **Expected Response**: MaLo-ID and location data (via webhook)
   - **Note**: You must implement webhook endpoints to receive the response asynchronously

2. **Lieferbeginn (Supply Start)**
   - **Trigger**: `START_LIEFERBEGINN`
   - **Purpose**: Register the customer's supply contract with the network operator
   - **Your Role**: Lieferant (LF)
   - **Documentation**: `llm.txt` → "Lieferant [Lieferbeginn (Rolle LFN)]"
   - **API**: `events/events-openapi.yaml` → START_LIEFERBEGINN
   - **Required Data**: 
     - Customer information (Geschaeftspartner)
     - Market location (Marktlokation)
     - Contract details (Energieliefervertrag)
     - Supply start date
   - **Expected Responses**:
     - From Network Operator (NB): Confirmation, configuration requirements
     - From Meter Operator (MSB): Meter configuration details

3. **Configuration Setup** (if needed)
   - **Trigger**: `START_EINRICHTUNG_KONFIG` (triggered by NB after Lieferbeginn)
   - **Purpose**: Set up meter configuration
   - **Your Role**: Receiving from NB, may need to coordinate with MSB
   - **Documentation**: `llm.txt` → "Netzbetreiber [Einrichtung der Konfiguration...]"

**Workflow**:
```
Customer Signs Up
    ↓
1. START_MALOIDENT (if MaLo-ID unknown)
   → Your backend calls Conuti API (outbound)
   → Conuti calls your webhook with response (inbound)
    ↓
2. START_LIEFERBEGINN (register supply)
   → Your backend calls Conuti API (outbound)
    ↓
3. Receive responses from NB/MSB
   → Via webhooks/read operations (inbound)
    ↓
4. Handle configuration setup (if required)
```

**Backend Requirements**:
- **Outbound APIs**: Call Conuti APIs (START_MALOIDENT, START_LIEFERBEGINN)
- **Inbound Webhooks**: Implement endpoints for MaloIdent responses (`maloident-lieferant`)
- **Data Storage**: 
  - Store customer data (Geschaeftspartner)
  - Store market location data (Marktlokation)
  - Store contract data (Energieliefervertrag)
- **Response Handling**: Handle asynchronous responses from NB/MSB
- **Process Tracking**: Track process status and correlate requests/responses

---

### Scenario 2: Customer Cancels Contract

**Business Goal**: Customer wants to end their electricity contract

**Required Processes**:
1. **Kündigung (Cancellation)**
   - **Trigger**: `START_KUENDIGUNG`
   - **Purpose**: Notify network operator of contract termination
   - **Your Role**: Lieferant (LF)
   - **Documentation**: `llm.txt` → "Lieferant [Kündigung LFA]" or "Kündigung LFN"
   - **API**: `events/events-openapi.yaml` → START_KUENDIGUNG
   - **Required Data**: Contract end date, reason

2. **Lieferende (Supply End)**
   - **Trigger**: `START_LIEFERENDE`
   - **Purpose**: Finalize supply termination
   - **Your Role**: Lieferant (LF)
   - **Documentation**: `llm.txt` → "Lieferant [Lieferende LF -> NB]"

---

### Scenario 3: Customer Changes Address or Contract Details

**Business Goal**: Update customer information or contract terms

**Required Processes**:
1. **Stammdatenänderung (Master Data Change)**
   - **Trigger**: `START_VERSAND_SDAE`
   - **Purpose**: Update master data (customer info, location, etc.)
   - **Your Role**: Lieferant (LF) - if you're responsible
   - **Documentation**: `llm.txt` → "Lieferant [Stammdatenänderung...]"
   - **API**: `events/events-openapi.yaml` → START_VERSAND_SDAE

---

## 🔍 Discovery Workflow

### Step 1: Identify Your Business Goal
- "Register new customer"
- "Cancel contract"
- "Change customer data"
- "Handle billing"
- etc.

### Step 1b: Check PROCESS_GRAPH.json for Pre-built Scenarios
```javascript
// Available business scenarios in PROCESS_GRAPH.json:
PROCESS_GRAPH.business_scenarios.NEW_CUSTOMER_SIGNUP
PROCESS_GRAPH.business_scenarios.SUPPLIER_SWITCH_AS_NEW
PROCESS_GRAPH.business_scenarios.SUPPLIER_SWITCH_AS_OLD
PROCESS_GRAPH.business_scenarios.CUSTOMER_CANCELLATION
PROCESS_GRAPH.business_scenarios.HANDLE_FORCED_TERMINATION
PROCESS_GRAPH.business_scenarios.HANDLE_EG_ASSIGNMENT
PROCESS_GRAPH.business_scenarios.MASTER_DATA_UPDATE
PROCESS_GRAPH.business_scenarios.CANCEL_PREVIOUS_MESSAGE
```

Each scenario includes:
- Step-by-step process sequence
- Prerequisites and dependencies
- Expected responses
- Backend requirements

### Step 2: Find Related Processes in `llm.txt`
Search for business terms:
- **"Lieferbeginn"** = Supply start / New customer registration
- **"Kündigung"** = Cancellation
- **"Stammdatenänderung"** = Master data change
- **"Abrechnung"** = Billing
- **"Malo-Ident"** = Location identification

### Step 3: Understand the Process Flow
1. Check the process overview documentation (linked in `llm.txt`)
2. Identify which market participants are involved:
   - **LF** (Lieferant) = You (supplier)
   - **NB** (Netzbetreiber) = Network operator
   - **MSB** (Messstellenbetreiber) = Meter operator

### Step 4: Identify Required Data
1. Check the **business rule YAML**: `yaml_output/[PROCESS_ID].yaml`
   - Lists mandatory fields
   - Shows validation rules
   - Indicates conditional fields

2. Check the **process schema**: `PIs/PI_[PROCESS_ID].yml`
   - Shows exact API structure
   - Request/response formats

3. Cross-reference with **BO4E schema**: `bo4e-openapi.min.json`
   - Understand data types
   - See object relationships
   - Find enum values

### Step 5: Map to Backend Services
- **What data do you need to collect?**
  - Customer information
  - Location data
  - Contract details
  - Dates/times

- **What APIs do you need to call?** (Outbound)
  - Trigger events (`macoapp-trigger`, `events-openapi`)
  - MaloIdent requests (`maloident-macoapp`)
  - Write operations (`macoapp-schreiben`)

- **What webhooks do you need to implement?** (Inbound)
  - MaloIdent responses (`maloident-lieferant`)
  - Read operations (`macoapp-lesen`)
  - Process data updates

- **What responses do you need to handle?**
  - Confirmations
  - Rejections
  - Status updates
  - Data requests

---

## 📋 Process Categories

### Customer Onboarding
- **MaloIdent**: Identify market location
- **Lieferbeginn**: Start supply contract
- **Configuration Setup**: Set up meters/configurations

### Contract Management
- **Kündigung**: Cancel contract
- **Lieferende**: End supply
- **Stammdatenänderung**: Update master data

### Billing & Settlement
- **Abrechnungsdaten**: Billing data
- **Netznutzungsabrechnung**: Network usage billing
- **Bilanzkreisabrechnung**: Balance group settlement

### Metering & Values
- **Zählerstand**: Meter readings
- **Lastgang**: Load profiles
- **Energiemengen**: Energy quantities

---

## 🤖 AI Agent Prompt for Discovery

```
I want to [BUSINESS GOAL, e.g., "register a new customer for electricity supply"].

Help me discover:
1. Which market processes are required?
2. What data do I need to collect from the customer?
3. What APIs do I need to call (as Lieferant)?
4. What responses should I expect from other market participants?
5. What backend services do I need to build?

Use the following resources:
- PROCESS_GRAPH.json: Check business_scenarios for pre-built workflows, check dependencies
- BUSINESS_PROCESS_MAP.md: Find business scenarios matching your goal
- llm.txt: Find processes related to [business goal] (index to find docs)
- docs-offline/: Read workflow documentation (Prozessübersicht) and process descriptions
- yaml_output/: Check mandatory fields for each process
- PIs/: Understand API structure
- _build/bo4e-openapi.min.json: Understand data types
- _build/maloident-macoapp.min.json: MaloIdent request structure (outbound)
- _build/maloident-lieferant.min.json: MaloIdent response structure (inbound webhook)
- _build/macoapp-trigger.min.json: Trigger event structures (outbound)
```

---

## 💡 Tips

1. **Start with `PROCESS_GRAPH.json`** - Contains pre-built business scenarios with step-by-step sequences
2. **Check dependencies** - Use `processes.[ID].prerequisites` and `triggers_processes` in PROCESS_GRAPH.json
3. **Use `llm.txt`** - It's organized by business processes for finding documentation
4. **Follow the workflow** - Processes often have dependencies (e.g., MaloIdent before Lieferbeginn)
5. **Check your role** - You're likely "Lieferant" (LF), so focus on LF processes (see `indexes.by_role.LF`)
6. **Understand responses** - You'll receive responses from NB and MSB, prepare handlers
7. **Use processinfo.json** - Contains detailed process descriptions (technical but comprehensive)

---

## 🔗 Quick Reference

| Business Goal | Main Process | Trigger Event | Documentation Link |
|--------------|-------------|---------------|-------------------|
| Register new customer | Lieferbeginn | START_LIEFERBEGINN | Lieferant > Lieferbeginn |
| Cancel contract | Kündigung | START_KUENDIGUNG | Lieferant > Kündigung |
| Identify location | MaloIdent | START_MALOIDENT | Lieferant > Malo-Ident |
| Update customer data | Stammdatenänderung | START_VERSAND_SDAE | Lieferant > Stammdatenänderung |
| Handle billing | Abrechnungsdaten | START_ABR_NN | Lieferant > Abrechnungsdaten |

