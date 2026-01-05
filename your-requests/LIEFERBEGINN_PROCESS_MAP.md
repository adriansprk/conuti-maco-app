# Lieferbeginn Process - Complete Message & Field Mapping

## Overview

**Process**: Lieferbeginn (Supply Start)  
**BDEW Process ID**: 55001 (consuming Marktlokation) / 55077 (generating Marktlokation)  
**Trigger Event**: `START_LIEFERBEGINN`  
**Your Role**: LFN (Neulieferant - New Supplier)  
**API Schema**: `macoapp-trigger.min.json` → `START_LIEFERBEGINN`

---

## Process Flow

```
1. [OUTBOUND] Trigger START_LIEFERBEGINN
   ↓
2. [INBOUND] Receive response from NB (Network Operator)
   - Success: 55002 (consuming) / 55078 (generating)
   - Rejection: 55003 (consuming) / 55080 (generating)
   - Info Existing Assignment: 55036
   ↓
3. [INBOUND] If 55036 → May receive 55010 (Abmeldeanfrage)
   ↓
4. [INBOUND] Follow-up processes triggered by NB:
   - STAMMDATENAENDERUNG_NB (immediate)
   - ABRECHNUNGSDATEN_BK (immediate)
   - ABRECHNUNGSDATEN_NN (immediate, for consuming MaLo)
   - BERECHNUNGSFORMEL (at Zuordnungsbeginn)
   - EINRICHTUNG_KONFIG (at Zuordnungsbeginn)
   - ERSATZ_GRUNDVERSORGUNG (if E/G required)
   - WIEDERHERSTELLUNG_ANSCHLUSS (if blocked MaLo)
```

---

## 1. OUTBOUND: Trigger Event START_LIEFERBEGINN

### API Endpoint
- **Schema**: `macoapp-trigger.min.json`
- **Event**: `START_LIEFERBEGINN`
- **Direction**: Outbound (Your backend → Conuti API)

### Required Fields

#### Root Level
```yaml
required:
  - stammdaten
  - transaktionsdaten
  - zusatzdaten
```

#### stammdaten (Required)
```yaml
stammdaten:
  required:
    - MARKTLOKATION  # At least one Marktlokation required
  
  MARKTLOKATION:  # Array, at least 1 required
    - marktlokationsId: string  # REQUIRED: Market location ID
    - sparte: enum  # REQUIRED: "STROM" or "GAS"
    - energierichtung: enum  # REQUIRED: "AUSSP" (consuming) or "EINSP" (generating)
    - erforderlichesProduktpaket: array  # Optional: Product package requirements
    - marktlokationsTyp: array  # Optional: Location type classifications
  
  ENERGIELIEFERVERTRAG:  # Array, optional
    - vertragsbeginn: date-time  # Contract start date
    - vertragsende: date-time  # Contract end date
    - vertragspartner2: array  # Customer/partner information
      - name1: string  # Name part 1 (company name or surname)
      - name2: string  # Name part 2 (first name or department)
      - name3: string  # Name part 3 (additional name parts)
      - name4: string  # Name part 4
      - anrede: string  # Salutation (e.g., "Herr", "Frau")
      - geschaeftspartnerrolle: enum  # KUNDE, LIEFERANT, etc.
      - partneradresse: object
        - strasse: string
        - hausnummer: string
        - postleitzahl: string
        - ort: string
        - ortsteil: string
        - landescode: enum  # ISO country code (e.g., "DE")
    - korrespondenzpartner: object  # Optional: Correspondence partner
    - vertragskonditionen: object
      - haushaltskunde: boolean  # Household customer flag
  
  NETZNUTZUNGSVERTRAG:  # Array, optional
    - vertragsbeginn: date-time  # Network usage contract start
    - vertragsende: date-time  # Network usage contract end
    - vertragskonditionen: object
      - haushaltskunde: boolean
  
  TRANCHE:  # Array, optional (for generating locations)
    - tranchenId: string
    - bildungTranchengroesse: enum  # PROZENTUAL, AUFTEILUNGSFAKTOR
    - aufteilungsmenge: object
      - wert: number
      - einheit: enum  # W, WH, KW, KWH, etc.
```

#### transaktionsdaten (Required)
```yaml
transaktionsdaten:
  required:
    - ausfuehrungsdatum  # Execution date
    - vorgangsnummer  # Process number (your internal reference)
    - absender  # Sender information
    - empfaenger  # Recipient information
  
  ausfuehrungsdatum: date-time  # REQUIRED: When to execute the process
  vorgangsnummer: string  # REQUIRED: Your internal process reference
  
  absender:  # REQUIRED: Your information
    rollencodetyp: enum  # REQUIRED: BDEW, GS1, GLN, DVGW
    rollencodenummer: string  # REQUIRED: Your role code number
    ansprechpartner: object  # Optional
      - nachname: string
      - eMailAdresse: string
    rufnummern: array  # Optional
      - rufnummer: object
      - nummerntyp: enum  # RUF_ZENTRALE, FAX_ZENTRALE, etc.
  
  empfaenger:  # REQUIRED: Network operator information
    rollencodetyp: enum  # REQUIRED: BDEW, GS1, GLN, DVGW
    rollencodenummer: string  # REQUIRED: NB role code number
  
  transaktionsgrund: string  # Optional: Transaction reason
  transaktionsgrundergaenzung: string  # Optional: Additional transaction reason
  transaktionsgrundergaenzungBefristeteAnmeldung: string  # Optional: For time-limited registrations
```

#### zusatzdaten (Required)
```yaml
zusatzdaten:
  required:
    - prozessId  # REQUIRED: Your internal process/document ID (UUID format recommended)
    - eventname  # REQUIRED: "START_LIEFERBEGINN"
  
  prozessId: string  # REQUIRED: Unique ID to correlate responses (e.g., UUID)
  eventname: "START_LIEFERBEGINN"  # REQUIRED: Must be exactly this value
```

### YAML File Reference
- **Location**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55001.yaml` (consuming)
- **Location**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55077.yaml` (generating)

---

## 2. INBOUND: Success Response Messages

### 2.1 Success - Consuming Marktlokation (55002)

**BDEW ID**: 55002  
**Description**: Zuordnung des LFN zur Marktlokation bzw. Tranche (consuming)  
**Direction**: Inbound (NB → Your backend via webhook)

#### Required Fields (You Receive)
```yaml
required:
  - stammdaten
  - transaktionsdaten

stammdaten:
  MARKTLOKATION: array  # Confirmed market location
    - marktlokationsId: string
    - marktrollen: array  # Market roles assigned
      - marktrolle: enum  # NB, LF, MSB, etc.
      - rollencodenummer: string
      - messstellenbetreiberEigenschaft: enum  # If MSB role
      - weiterverpflichtet: boolean
  
  MESSLOKATION: array  # Meter locations
    - messlokationsId: string
    - marktrollen: array
  
  NETZNUTZUNGSVERTRAG: array
    - vertragsbeginn: date-time
    - vertragsende: date-time
  
  NETZLOKATION: array  # Network locations
    - netzlokationsId: string
    - marktrollen: array
  
  STEUERBARE_RESSOURCE: array  # Controllable resources
  TECHNISCHE_RESSOURCE: array  # Technical resources

transaktionsdaten:
  pruefidentifikator: "55002"  # Confirms this is success message
  dokumentennummer: string  # Reference from BGM segment
  anfragereferenznummer: string  # Your vorgangsnummer echoed back
  antwortstatus: string  # Response status
  antwortstatusCodeliste: string
  geplantesProduktpaket: integer  # Planned product package (informative)
  vertragsbeginn: date-time  # Confirmed contract start
```

#### Key Fields to Extract
- `pruefidentifikator` = "55002" → **SUCCESS**
- `anfragereferenznummer` → Correlate with your `prozessId`
- `vertragsbeginn` → Confirmed start date
- `marktlokationsId` → Confirmed market location
- `marktrollen` → Assigned market roles

**YAML File**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55002.yaml`

---

### 2.2 Success - Generating Marktlokation (55078)

**BDEW ID**: 55078  
**Description**: Zuordnung des LFN zur Marktlokation bzw. Tranche (generating)  
**Direction**: Inbound (NB → Your backend via webhook)

#### Required Fields (You Receive)
```yaml
required:
  - stammdaten
  - transaktionsdaten

stammdaten:
  MARKTLOKATION: array
    - marktlokationsId: string
    - marktrollen: array
  
  TRANCHE: array  # Tranche information for generating locations
    - tranchenId: string
    - bildungTranchengroesse: enum
    - aufteilungsmenge: object
  
  NETZNUTZUNGSVERTRAG: array
    - vertragsbeginn: date-time
  
  STEUERBARE_RESSOURCE: array
  TECHNISCHE_RESSOURCE: array

transaktionsdaten:
  pruefidentifikator: "55078"  # Confirms this is success message (generating)
  # ... same structure as 55002
```

**YAML File**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55078.yaml`

---

## 3. INBOUND: Rejection Response Messages

### 3.1 Rejection - Consuming Marktlokation (55003)

**BDEW ID**: 55003  
**Description**: Ablehnung der Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche (consuming)  
**Direction**: Inbound (NB → Your backend via webhook)  
**EBD Error Codes**: E_0621, E_0622, E_0623

#### Required Fields (You Receive)
```yaml
required:
  - transaktionsdaten  # Only transaktionsdaten required for rejection

transaktionsdaten:
  pruefidentifikator: "55003"  # Confirms this is rejection message
  dokumentennummer: string
  anfragereferenznummer: string  # Your vorgangsnummer echoed back
  antwortstatus: string  # Rejection status
  antwortstatusCodeliste: string
  antwortstatusdritter: string  # Third-party response status (if applicable)
  antwortstatusdritterCodeliste: string
  antwortstatusdritterBetroffeneLokation: string
  antwortstatusdritterReferenz: string
  freitext: object  # Free text with rejection reason
    - freitext1: string
    - freitext2: string
    - freitext3: string
    - freitext4: string
    - freitext5: string
  lieferbeginndatuminbearbeitung: date-time  # Date in processing (if applicable)
  naechsteBearbeitung: date-time  # Next processing date (if applicable)
  beteiligterMarktpartner: object  # Involved market partner (if applicable)
    - rollencodenummer: string
    - rollencodetyp: enum
```

#### Key Fields to Extract
- `pruefidentifikator` = "55003" → **REJECTION**
- `anfragereferenznummer` → Correlate with your `prozessId`
- `freitext` → **Read rejection reason here**
- `antwortstatus` → Detailed rejection status
- `naechsteBearbeitung` → When you can retry (if provided)

**YAML File**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55003.yaml`

---

### 3.2 Rejection - Generating Marktlokation (55080)

**BDEW ID**: 55080  
**Description**: Ablehnung der Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche (generating)  
**Direction**: Inbound (NB → Your backend via webhook)  
**EBD Error Codes**: E_0621, E_0622, E_0623

#### Required Fields (You Receive)
Same structure as 55003, but:
- `pruefidentifikator` = "55080" → **REJECTION (generating)**

**YAML File**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55080.yaml`

---

## 4. INBOUND: Info Message - Existing Assignment (55036)

**BDEW ID**: 55036  
**Description**: Info existierende Zuordnung (Information about existing assignment)  
**Direction**: Inbound (NB → Your backend via webhook)  
**When**: NB informs you about existing LFA (old supplier) assignment

#### Required Fields (You Receive)
```yaml
required:
  - transaktionsdaten

transaktionsdaten:
  pruefidentifikator: "55036"  # Confirms this is info message
  dokumentennummer: string
  anfragereferenznummer: string  # Your vorgangsnummer echoed back
  kategorie: enum  # Category of the message
  absender: object  # NB information
  empfaenger: object  # Your information
  nachrichtendatum: date-time
  nachrichtenreferenznummer: string
```

#### What Happens Next
If you receive **55036**, the NB will:
1. Send **55010** (Abmeldeanfrage) to the old supplier (LFA)
2. Wait for LFA response (55011 = accept, 55012 = reject)
3. If LFA accepts → Send **55037** (Beendigung Zuordnung LFA)
4. Then send you **55002** or **55078** (success)

**YAML File**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55036.yaml`

---

## 5. INBOUND: Abmeldeanfrage (55010) - For Your Reference

**BDEW ID**: 55010  
**Description**: Anfrage zur Beendigung der Zuordnung (Request to end assignment)  
**Direction**: Inbound (NB → LFA, not you)  
**Note**: You don't receive this, but it's part of the process flow when 55036 is sent

**YAML File**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55010.yaml`

---

## Outcome Scenarios Summary

### Scenario 1: Direct Success
```
START_LIEFERBEGINN (55001/55077)
  ↓
55002 (consuming) or 55078 (generating) ← SUCCESS
```

**Required Fields to Handle**:
- `pruefidentifikator` = "55002" or "55078"
- `anfragereferenznummer` (correlate with your `prozessId`)
- `vertragsbeginn` (confirmed start date)
- `marktlokationsId` (confirmed location)
- `marktrollen` (assigned roles)

---

### Scenario 2: Direct Rejection
```
START_LIEFERBEGINN (55001/55077)
  ↓
55003 (consuming) or 55080 (generating) ← REJECTION
```

**Required Fields to Handle**:
- `pruefidentifikator` = "55003" or "55080"
- `anfragereferenznummer` (correlate with your `prozessId`)
- `freitext` (rejection reason) ← **CRITICAL**
- `antwortstatus` (detailed status)
- `naechsteBearbeitung` (retry date, if provided)

**EBD Error Codes**: E_0621, E_0622, E_0623

---

### Scenario 3: Existing Assignment Flow
```
START_LIEFERBEGINN (55001/55077)
  ↓
55036 ← Info about existing LFA assignment
  ↓
NB sends 55010 to LFA
  ↓
LFA responds: 55011 (accept) or 55012 (reject)
  ↓
If 55011: NB sends 55037 to LFA (termination)
  ↓
55002 or 55078 ← SUCCESS (after LFA termination)
```

**Required Fields to Handle**:
- `pruefidentifikator` = "55036" → **Wait for follow-up**
- `anfragereferenznummer` (correlate with your `prozessId`)
- **Monitor for**: 55002/55078 (success) or 55003/55080 (rejection)

---

## Follow-Up Processes (Triggered by NB After Success)

After receiving **55002** or **55078**, you will receive these follow-up messages:

### Immediate Follow-ups (from NB)

1. **STAMMDATENAENDERUNG_NB** (Prüfi: 55615, 55620, 55175, 55225, 55616, 55617, 55618, 55619, 55691)
   - Master data changes from network operator
   - **Timing**: Immediate

2. **ABRECHNUNGSDATEN_BK** (Prüfi: 55126)
   - Balance group billing data
   - **Timing**: Immediate
   - **Always sent**

3. **ABRECHNUNGSDATEN_NN** (Prüfi: 55218)
   - Network usage billing data
   - **Timing**: Immediate
   - **Only for consuming Marktlokation**

### Follow-ups at Zuordnungsbeginn (from NB)

4. **BERECHNUNGSFORMEL** (Prüfi: 25001)
   - Calculation formula
   - **Timing**: At Zuordnungsbeginn (contract start date)

5. **EINRICHTUNG_KONFIG** (Prüfi: 17134)
   - Configuration setup
   - **Timing**: At Zuordnungsbeginn

6. **ERSATZ_GRUNDVERSORGUNG** (Prüfi: 55013)
   - Fallback/basic supply assignment
   - **Timing**: At Zuordnungsbeginn
   - **Only for consuming Marktlokation when E/G required**

7. **WIEDERHERSTELLUNG_ANSCHLUSS** (Prüfi: 21040, 21039)
   - Reconnection/unblocking
   - **Timing**: At Zuordnungsbeginn
   - **Only for blocked Marktlokation**

---

## Backend Implementation Checklist

### Outbound API (Trigger)
- [ ] Implement `START_LIEFERBEGINN` trigger call
- [ ] Collect required fields:
  - [ ] `marktlokationsId` (or trigger MALOIDENT first if unknown)
  - [ ] `vertragsbeginn` (contract start date)
  - [ ] `vertragsende` (contract end date, if applicable)
  - [ ] Customer information (ENERGIELIEFERVERTRAG)
  - [ ] `prozessId` (your internal UUID)
  - [ ] `vorgangsnummer` (your internal reference)
  - [ ] `absender` (your role code)
  - [ ] `empfaenger` (NB role code)

### Inbound Webhooks (Responses)
- [ ] Implement webhook endpoint for `macoapp-schreiben` (receives all responses)
- [ ] Handle message correlation:
  - [ ] Extract `anfragereferenznummer` or `pruefidentifikator`
  - [ ] Match with your `prozessId` or `vorgangsnummer`
- [ ] Handle success (55002/55078):
  - [ ] Store confirmed `vertragsbeginn`
  - [ ] Store confirmed `marktlokationsId`
  - [ ] Store `marktrollen` assignments
  - [ ] Update process status to "SUCCESS"
- [ ] Handle rejection (55003/55080):
  - [ ] Extract `freitext` (rejection reason)
  - [ ] Extract `antwortstatus` (detailed status)
  - [ ] Check `naechsteBearbeitung` (retry date)
  - [ ] Update process status to "REJECTED"
  - [ ] Log EBD error codes (E_0621, E_0622, E_0623)
- [ ] Handle info (55036):
  - [ ] Update process status to "PENDING_LFA_CONFIRMATION"
  - [ ] Monitor for follow-up messages (55002/55078 or 55003/55080)

### Follow-up Process Handlers
- [ ] Implement handlers for:
  - [ ] STAMMDATENAENDERUNG_NB (multiple Prüfis)
  - [ ] ABRECHNUNGSDATEN_BK (55126)
  - [ ] ABRECHNUNGSDATEN_NN (55218) - if consuming
  - [ ] BERECHNUNGSFORMEL (25001)
  - [ ] EINRICHTUNG_KONFIG (17134)
  - [ ] ERSATZ_GRUNDVERSORGUNG (55013) - if applicable
  - [ ] WIEDERHERSTELLUNG_ANSCHLUSS (21040, 21039) - if applicable

### Data Storage
- [ ] Store process data:
  - [ ] `prozessId` (correlation key)
  - [ ] `vorgangsnummer` (your reference)
  - [ ] `marktlokationsId`
  - [ ] `vertragsbeginn` / `vertragsende`
  - [ ] Process status (PENDING, SUCCESS, REJECTED, PENDING_LFA_CONFIRMATION)
  - [ ] Response messages received
  - [ ] Rejection reasons (if rejected)

---

## Key Files Reference

### YAML Business Rules (Mandatory Fields)
- **55001**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55001.yaml`
- **55077**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55077.yaml`
- **55002**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55002.yaml`
- **55078**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55078.yaml`
- **55003**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55003.yaml`
- **55080**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55080.yaml`
- **55036**: `maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55036.yaml`

### API Schemas
- **Trigger**: `maco-api-documentation/_build/macoapp-trigger.min.json` → `START_LIEFERBEGINN`
- **Responses**: `maco-api-documentation/_build/macoapp-schreiben.min.json` → `PI_55001`, `PI_55002`, etc.

### Process Schemas
- **PI_55001**: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55001.yml`
- **PI_55077**: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55077.yml`
- **PI_55002**: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55002.yml`
- **PI_55078**: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55078.yml`
- **PI_55003**: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55003.yml`
- **PI_55080**: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55080.yml`

### Test Files (Examples)
- **55001**: `maco-edi-testfiles/inbound/v202404/UTILMD/Strom/55001_eingehend_Testfall1.json`
- **55002**: `maco-edi-testfiles/inbound/v202404/UTILMD/Strom/55002_eingehend_Testfall1.json`
- **55003**: `maco-edi-testfiles/inbound/v202404/UTILMD/Strom/55003_eingehend_Testfall1.json`

### Documentation
- **Process Overview**: `docs-offline/prozessübersicht-853953m0.md`
- **Process Description**: `docs-offline/lieferbeginn.md`
- **Process Graph**: `PROCESS_GRAPH.json` → `processes.LIEFERBEGINN`

---

## Important Notes

1. **Correlation**: Always use `prozessId` (from `zusatzdaten`) to correlate responses. The NB will echo back `anfragereferenznummer` which should match your `vorgangsnummer`.

2. **Asynchronous**: All responses are asynchronous. You trigger the event and receive responses via webhooks later.

3. **Prüfidentifikator**: Always check `pruefidentifikator` in responses to determine message type:
   - "55001" = Your request (consuming)
   - "55077" = Your request (generating)
   - "55002" = Success (consuming)
   - "55078" = Success (generating)
   - "55003" = Rejection (consuming)
   - "55080" = Rejection (generating)
   - "55036" = Info existing assignment

4. **Error Handling**: For rejections, always read `freitext` fields for human-readable rejection reasons.

5. **Follow-ups**: After success, prepare handlers for all follow-up processes. They will arrive asynchronously.

6. **Timing**: Follow-up processes arrive at different times:
   - Immediate: STAMMDATENAENDERUNG_NB, ABRECHNUNGSDATEN_BK, ABRECHNUNGSDATEN_NN
   - At Zuordnungsbeginn: BERECHNUNGSFORMEL, EINRICHTUNG_KONFIG, ERSATZ_GRUNDVERSORGUNG, WIEDERHERSTELLUNG_ANSCHLUSS

---

## Quick Reference: Message Types

| Prüfi | Direction | Type | Description |
|-------|-----------|------|-------------|
| 55001 | Outbound | Request | Lieferbeginn request (consuming) |
| 55077 | Outbound | Request | Lieferbeginn request (generating) |
| 55002 | Inbound | Success | Success response (consuming) |
| 55078 | Inbound | Success | Success response (generating) |
| 55003 | Inbound | Rejection | Rejection response (consuming) |
| 55080 | Inbound | Rejection | Rejection response (generating) |
| 55036 | Inbound | Info | Info existing assignment |

---

*Last Updated: Based on PROCESS_GRAPH.json and YAML schemas*
