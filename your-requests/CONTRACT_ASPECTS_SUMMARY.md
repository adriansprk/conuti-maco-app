# BO4E Contract (Vertrag) - Complete Aspect Overview

## Overview

A contract in BO4E is defined by **7 main aspect categories** with **20+ individual properties**. Only `boTyp` and `versionStruktur` are required; all other fields are optional but define the contract's characteristics.

---

## 1. Core Identification

**Purpose**: Basic contract identification and metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `boTyp` | enum | ✅ **Yes** | Always "VERTRAG" |
| `versionStruktur` | string | ✅ **Yes** | BO4E structure version (default: "1") |
| `vertragsnummer` | string | No | Unique contract number |
| `beschreibung` | string | No | Free text description of conditions |

---

## 2. Contract Classification

**Purpose**: Categorize the contract by type, status, and sector

| Field | Type | Required | Values |
|-------|------|----------|--------|
| `vertragsart` | enum | No | ENERGIELIEFERVERTRAG, NETZNUTZUNGSVERTRAG, BILANZIERUNGSVERTRAG, MESSSTELLENBETRIEBSVERTRAG, BUENDELVERTRAG |
| `vertragsstatus` | enum | No | IN_ARBEIT, UEBERMITTELT, ANGENOMMEN, AKTIV, ABGELEHNT, WIDERRUFEN, STORNIERT, GEKUENDIGT, BEENDET |
| `sparte` | enum | No | STROM, GAS, FERNWAERME, NAHWAERME, WASSER, ABWASSER |

---

## 3. Location Binding

**Purpose**: Link contract to a specific location

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `lokationsId` | string | No | ID of the location (MaLo, MeLo, NeLo, etc.) |
| `lokationsTyp` | enum | No | MALO, MELO, NELO, TECHNISCHE_RESSOURCE, STEUERBARE_RESSOURCE, TRANCHE |

---

## 4. Temporal Aspects

**Purpose**: Define contract timing and validity periods

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vertragsbeginn` | date-time | No | Contract start date/time |
| `vertragsende` | date-time | No | Contract end date/time (planned or actual) |
| `gueltigkeitszeitraum` | Zeitraum | No | Validity period object with start/end dates, duration, etc. |

**Zeitraum Object Properties**:
- `zeiteinheit` - Time unit enum
- `dauer` - Duration (integer)
- `startdatum` - Start date-time
- `enddatum` - End date-time
- `einheit` - Unit enum
- `ableseZeitraum` - Meter reading period (string)
- `abrechnungsZeitraum` - Billing period (string)
- `zeitraumText` - Text description
- `zeitraumId` - Period ID (integer)

---

## 5. Contract Parties

**Purpose**: Identify who is involved in the contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vertragspartner1` | array[Geschaeftspartner] | No | First party (usually issuer) |
| `vertragspartner2` | array[Geschaeftspartner] | No | Second party (usually recipient) |
| `korrespondenzpartner` | Geschaeftspartner | No | Correspondence partner |

**Geschaeftspartner Properties**:
- `boTyp`: "GESCHAEFTSPARTNER"
- `versionStruktur`: "1"
- `name1`, `name2`, `name3`, `name4` - Name parts
- `anrede` - Salutation (Herr, Frau, etc.)
- `partneradresse` - Address object
- `geschaeftspartnerrolle` - Business partner roles (KUNDE, LIEFERANT, etc.)
- `umsatzsteuerId` - VAT ID
- `glaeubigerId` - Creditor ID
- `emailAdresse`, `website` - Contact information
- `gewerbekennzeichnung` - Business/private flag
- `hrnummer`, `amtsgericht` - Commercial register info
- `externeKundenummerLieferant` - External customer number
- `externeReferenzen` - External references

---

## 6. Contract Conditions (vertragskonditionen)

**Purpose**: Detailed terms, billing, cancellation, and operational conditions

This is the **most complex aspect** with **20+ sub-properties**:

### 6.1 Network Usage Billing

| Field | Type | Description |
|-------|------|-------------|
| `netznutzungszahler` | enum | Who pays for network usage |
| `netznutzungsvertrag` | enum | Type of network usage contract |
| `netznutzungsabrechnung` | Zeitraum | Network usage billing period |
| `beinhaltetSingulaerGenutzteBetriebsmittel` | boolean | Whether singularly used equipment included |
| `netznutzungsabrechnungsgrundlage` | enum | Basis for network usage billing |
| `netznutzungsabrechnungsvariante` | enum | Variant of network usage billing |
| `abrechnungUeberNna` | boolean | Billing via network usage billing |
| `startAbrechnungsjahr` | date-time | Start of billing year |
| `naechstenetznutzungsabrechnung` | string | Next network usage billing |
| `abrechnungsintervall` | integer | Billing interval |
| `netznutzungsabrechnungIntervall` | integer | Network usage billing interval |

### 6.2 Customer Classification

| Field | Type | Description |
|-------|------|-------------|
| `haushaltskunde` | boolean | Household customer flag |

### 6.3 Discounts

| Field | Type | Description |
|-------|------|-------------|
| `gemeinderabatt` | Gemeinderabatt | Municipal discount object |
| | | - `wert`: number (discount value) |
| | | - `einheit`: string (unit) |
| | | - `typ`: string (type) |
| | | - `bemessungsgrundlage`: number (basis) |

### 6.4 Meter Reading

| Field | Type | Description |
|-------|------|-------------|
| `geplanteTurnusablesung` | Zeitraum | Planned periodic meter reading |
| `beauftragungMsb` | enum | MSB (Meter Operator) assignment |

### 6.5 Contract Duration & Cancellation

| Field | Type | Description |
|-------|------|-------------|
| `vertragslaufzeit` | Zeitraum | Contract duration period |
| `kuendigungsfrist` | Zeitraum | Cancellation notice period |
| `kuendigungstermin` | string | Cancellation deadline |
| `vertragsverlaengerung` | Zeitraum | Automatic extension period if not cancelled |

### 6.6 Payment Terms

| Field | Type | Description |
|-------|------|-------------|
| `abschlagszyklus` | Zeitraum | Advance payment cycle |
| `anzahl_abschlaege` | number | Number of advance payments per year (e.g., 12) |

### 6.7 Additional

| Field | Type | Description |
|-------|------|-------------|
| `beschreibung` | string | Free text description of conditions |

---

## 7. Billing Aspects

**Purpose**: High-level billing configuration

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `abrechnungUeberNna` | boolean | No | Whether billing is done via network usage billing |
| `gemeinderabatt` | integer | No | Municipal discount (for EDIFACT mapping) |

---

## 8. Data Quality

**Purpose**: Indicate data quality/reliability

| Field | Type | Required | Values |
|-------|------|----------|--------|
| `datenqualitaet` | enum | No | ERWARTETE_DATEN, IM_SYSTEM_VORHANDENE_DATEN, INFORMATIVE_DATEN, GUELTIGE_DATEN, KEINE_DATEN, IM_SYSTEM_KEINE_DATEN_VORHANDEN, KEINE_DATEN_ERWARTET, DIFFERENZ_DATEN, DIFFERENZ_ERWARTETE_DATEN, DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN |

---

## 9. Additional Aspects

**Purpose**: Special regulatory and legal information

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `enFG` | array[EnFG] | No | Energy Industry Act (Energiewirtschaftsgesetz) information |
| | | | - `grundlageVerringerungUmlagen`: enum |
| | | | - `grund`: array of enum (reasons for levy reduction) |

---

## Contract Type Overview

### ENERGIELIEFERVERTRAG (Energy Supply Contract)
- **Between**: Supplier (LF) ↔ Customer
- **Purpose**: Supply of energy to customer
- **Typical Fields**: `vertragspartner2` (customer), `vertragsbeginn`, `vertragsende`

### NETZNUTZUNGSVERTRAG (Network Usage Contract)
- **Between**: Network Operator (NB) ↔ Customer/Supplier
- **Purpose**: Use of network infrastructure
- **Typical Fields**: `lokationsId` (MaLo), `vertragskonditionen.netznutzungsabrechnung`

### MESSSTELLENBETRIEBSVERTRAG (Meter Operation Contract)
- **Between**: Meter Operator (MSB) ↔ Customer/Supplier
- **Purpose**: Meter operation and reading
- **Typical Fields**: `lokationsId` (MeLo), `vertragskonditionen.geplanteTurnusablesung`

### BILANZIERUNGSVERTRAG (Balancing Contract)
- **Between**: Balance Group Manager ↔ Balance Group Member
- **Purpose**: Balance group management
- **Typical Fields**: Balance group related fields

### BUENDELVERTRAG (Bundle Contract)
- **Between**: Service Provider ↔ Customer
- **Purpose**: Combined contract for multiple services
- **Typical Fields**: Multiple service aspects

---

## Summary: What Makes a Contract?

A contract in BO4E is defined by:

1. **Identity** (boTyp, versionStruktur, vertragsnummer)
2. **Type & Status** (vertragsart, vertragsstatus, sparte)
3. **Location** (lokationsId, lokationsTyp)
4. **Time** (vertragsbeginn, vertragsende, gueltigkeitszeitraum)
5. **Parties** (vertragspartner1, vertragspartner2, korrespondenzpartner)
6. **Conditions** (vertragskonditionen - 20+ sub-properties)
7. **Billing** (abrechnungUeberNna, gemeinderabatt)
8. **Data Quality** (datenqualitaet)
9. **Regulatory** (enFG)

**Total Properties**: 20+ direct properties + nested objects (Geschaeftspartner, Vertragskonditionen, Zeitraum, etc.)

**Required Fields**: Only `boTyp` and `versionStruktur` are mandatory. All other fields are optional but define the contract's characteristics.

---

## Schema References

- **Main Schema**: `bo4e-schema/schemas/v1/bo/Vertrag.schema.json`
- **Conditions Schema**: `bo4e-schema/schemas/v1/com/Vertragskonditionen.schema.json`
- **Partner Schema**: `bo4e-schema/schemas/v1/bo/Geschaeftspartner.schema.json`
- **Period Schema**: `bo4e-schema/schemas/v1/com/Zeitraum.schema.json`
- **Example**: `bo4e-schema/docs/examples/bo/Vertrag.json`





