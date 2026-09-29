# BDEW Documents Index

This index helps agents choose the right BDEW source document before answering MaKo questions. It is a navigation aid only: always open and read the linked source document before making process, deadline, field, or EDIFACT claims.

## Quick Routing

| Question type | Start with | Why |
|---|---|---|
| Zuordnungsprozesse under BK6-24-174: MaLo-ID Ermittlung, Kündigung, Lieferbeginn, Neuanlage, Ersatz-/Grundversorgung, 100 % LF-Zuordnung (erzeugend), Lieferende, Abrechnungsdaten, Netznutzungsabrechnung, NB-Preisblätter, Sperren/Entsperren | [`BK6-24-174_GPKE_Teil2_Lesefassung.md`](./BK6-24-174_GPKE_Teil2_Lesefassung.md) | GPKE Teil 2 Lesefassung (BK6-24-174): UC/SD sequences and deadlines for supplier–NB assignment processes. |
| Foundational GPKE rules (Fristenberechnung, Identifikation, Objektmodell), or text tied to Festlegung **BK6-20-160** (gültig ab 01.04.2022) | [`bk620160_gpke.md`](./bk620160_gpke.md) | Older consolidated GPKE festlegung; still cited in many internal docs. Cross-check Teil 2 when the question is BK6-24-174 scope. |
| 24h supplier switching details, timing, follow-up data after Lieferbeginn, BGM+E03 changes, iMS configuration, §14a, shutdown examples | [`BDEW_AWH_LFW24_V1_7_20251208.md`](./BDEW_AWH_LFW24_V1_7_20251208.md) | BDEW application help for Lieferantenwechsel 24 Stunden; use after GPKE Teil 2 UC/SD for process law. Worked examples and clarification scenarios. |
| LFW24 go-live (06.06.2025), cutover from Universalbestellprozess, async→sync billing, GPKE/GeLi Gas holiday, migration send windows, transitional correction examples | [`AWH_Einführungsszenario_LFW24_Version_1.2.md`](./AWH_Einführungsszenario_LFW24_Version_1.2.md) | BDEW introduction scenario for BK6-22-024 rollout: cutover rules, end of Asynchronmodell, and worked examples A–G for Netznutzungs-/Bilanzierungswechsel around 06.06.2025. |
| Metering operator processes: MSB cancellation/start/end, device changes, iMS/mME installation, MSB billing, MSB price sheets | [`BK6-24-174_WiM_Teil1_Lesefassung.md`](./BK6-24-174_WiM_Teil1_Lesefassung.md) | WiM Teil 1 covers metering base processes and MSB commercial processes. |
| Meter readings, measured values, value requests, reclamations, cancellations, values after Typ 2, ESA value access | [`BK6-24-174_WiM_Teil2_Lesefassung.md`](./BK6-24-174_WiM_Teil2_Lesefassung.md) | WiM Teil 2 covers collection, preparation, request, transmission, reclamation, and cancellation of values. |
| Network operator change, old/new NB handover, package ID, affected locations, data transfer to LF/MSB/ÜNB | [`BDEW_AWH_Netzbetreiberwechselprozesse_Strom_V1_2_20251030.md`](./BDEW_AWH_Netzbetreiberwechselprozesse_Strom_V1_2_20251030.md) | Application help for market processes when a location changes responsible NB MP-ID. |
| APERAK/CONTRL handling, syntax vs processing errors, acknowledgement messages, ERC error codes, APERAK deadlines | [`APERAK_AHB_1_1_Konsultationsfassung_20260202.md`](./APERAK_AHB_1_1_Konsultationsfassung_20260202.md) | APERAK Anwendungshandbuch for market communication feedback and error handling. |
| UTILMD EDIFACT segment structure, segment groups, fields, cardinalities, DTM/LOC/NAD/RFF layout | [`UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.md`](./UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.md) | UTILMD Message Implementation Guide for Strom, version S2.1. |
| MSCONS EDIFACT segment structure and generic MSCONS layout | [`MSCONS_MIG_2_4c_außerordentliche_20240726.md`](./MSCONS_MIG_2_4c_außerordentliche_20240726.md) | MSCONS Message Implementation Guide, version 2.4c. |
| MSCONS business usage, Prüfi-specific value scenarios, zählerstände, energiemengen, Lastgänge, MaBiS/Redispatch values, corrections | [`MSCONS_AHB_3_1f_Fehlerkorrektur_20250930.md`](./MSCONS_AHB_3_1f_Fehlerkorrektur_20250930.md) | MSCONS Anwendungshandbuch explains when and how MSCONS structures are used. Prose is 3.1f; the newer 3.1g exists only as XML (`xml-docs/`). For Prüfi requiredness use `ahb-tables/`. |
| Invoice EDIFACT structure, invoice header/positions/taxes/amounts/payment terms | [`INVOIC_MIG_2.8e_20250401.md`](./INVOIC_MIG_2.8e_20250401.md) | INVOIC Message Implementation Guide, version 2.8e. |
| Order EDIFACT structure, requests/orders, product descriptions, references, locations, participants | [`ORDERS_MIG_1_4b_20250401.md`](./ORDERS_MIG_1_4b_20250401.md) | ORDERS Message Implementation Guide, version 1.4b. |
| PRICAT EDIFACT structure, price-sheet message layout, BGM document types | [`PRICAT_MIG_2_0e_Fehlerkorrektur_20250930.md`](./PRICAT_MIG_2_0e_Fehlerkorrektur_20250930.md) | PRICAT Message Implementation Guide, version 2.0e. |
| PRICAT business usage: NB/MSB price sheets (Netznutzung, Messstellenbetrieb, Konfigurationen, Technik), catalog scenarios | [`PRICAT_AHB_2_0f_Fehlerkorrektur_20251211.md`](./PRICAT_AHB_2_0f_Fehlerkorrektur_20251211.md) | PRICAT Anwendungshandbuch; read before the PRICAT MIG when the question is semantic. |
| OBIS codes, media codes, allowed OBIS for MSCONS/UTILMD, electricity/gas measuring identifiers | [`Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md`](./Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md) | External codelist for OBIS/media syntax and AHB checks. |
| Artikelnummern, Gruppenartikel-ID / Artikel-ID, INVOIC/UTILMD/PRICAT code columns, MSB billing article codes | [`Codeliste_Artikelnummern und Artikel-ID_5_6_Fehlerkorrektur_20250930.md`](./Codeliste_Artikelnummern%20und%20Artikel-ID_5_6_Fehlerkorrektur_20250930.md) | EDI@Energy codelist referenced from many AHB conditions (e.g. condition [40]). |
| Prüfi-specific requiredness: which segments/DEs/codes are Muss/Soll/Kann/X for Prüfi N, conditions, packages | [`../ahb-tables/FVxxxx/AHB_FVxxxx_{Prüfi}.json`](../ahb-tables/INDEX.md) | Per-Prüfi, per-format-version AHB rows with inlined condition text. Not in this folder; pick the FV valid for the process date. |
| IFTSTA or REMADV EDIFACT segment structure | [`xml-docs/IFTSTA_MIG_2_0g_20250401 1.xml`](./xml-docs/IFTSTA_MIG_2_0g_20250401%201.xml), [`xml-docs/REMADV_MIG_2_9e_20251001.xml`](./xml-docs/REMADV_MIG_2_9e_20251001.xml) | Only MIG source for these message types — no Markdown version exists. |
| An `ahb-tables` row looks wrong, or a Fehlerkorrektur may not be in the Hochfrequenz snapshot yet | Matching `xml-docs/*_AHB_*.xml` | BDEW-published original; tie-breaker, not the default lookup. See [BDEW XML Originals](#bdew-xml-originals-xml-docs). |
| Messprodukt-/Konfigurationsprodukt-Codes (9991…), Standard-Messprodukte Strom/Gas Typ 1, Typ 2 SMGW/Backend/ESA, Schaltzeit-/Leistungskurven-/Ad-Hoc-Steuerkanal config, Mindestumfang Messprodukte in UTILMD, Bestell-/Änderungsprodukte (UTILMD/ORDERS) | [`Codeliste-Konfigurationen_1_3c_Fehlerkorrektur_20251211.md`](./Codeliste-Konfigurationen_1_3c_Fehlerkorrektur_20251211.md) | Codelist of measurement/configuration products ordered between MSB and NB/LF/MSB/ESA. |

## How To Choose

1. If the question is about **what market process should happen and in which order**, start with **GPKE Teil 2** for BK6-24-174 Zuordnungs- and ergänzende Prozesse; use **`bk620160_gpke.md`** for BK6-20-160 baseline or introductory GPKE chapters (Fristen, Identifikation). Then use WiM, LFW24, or Netzbetreiberwechsel as needed. For **LFW24 go-live cutover, 06.06.2025 migration windows, or transitional async→sync billing corrections**, start with the LFW24 Einführungsszenario before the operational LFW24 AWH.
2. If the question is about **how an EDIFACT message is physically structured**, start with the matching MIG. For IFTSTA and REMADV the MIG exists only as XML in `xml-docs/`.
3. If the question is about **which segments, data elements, or codes are required for a specific Prüfidentifikator**, use `../ahb-tables/FVxxxx/AHB_FVxxxx_{Prüfi}.json` for the format version valid at the process date. Use this folder's AHB Markdown only for the surrounding prose, and `xml-docs/*_AHB_*.xml` only to verify a suspicious row.
4. If the question is about **APERAK or CONTRL feedback, syntax errors, processing errors, acknowledgements, or ERC codes**, start with the APERAK AHB.
5. If the question is about **which MSCONS variant is allowed for a value scenario**, start with the MSCONS AHB, then check the MSCONS MIG for segment placement.
6. If the question is about **OBIS codes or media identifiers**, start with the OBIS/media codelist.
7. If the question is about **which Messprodukt-/Konfigurationsprodukt-Code (9991…) to order, what a product code means, or the Mindestumfang of products in a UTILMD/ORDERS message**, start with the Codeliste der Konfigurationen.
8. If the question is about **Artikelnummern or Gruppenartikel-ID / Artikel-ID** (INVOIC lines, UTILMD PIA, PRICAT catalog entries, MSB Abrechnung), start with the Codeliste der Artikelnummern und Artikel-ID; pair with the PRICAT AHB for price-sheet document types.
9. If the question is about **PRICAT price sheets or catalog messages**, start with the PRICAT AHB, then the PRICAT MIG for segment placement.
10. If the question is about **BO4E API fields, Conuti schemas, or trigger payloads**, do not rely on this folder alone. Use the repo schema sources in `maco-api-documentation/` after reading the relevant BDEW process context.

## Document Groups

### Process And Regulatory Context

- [`BK6-24-174_GPKE_Teil2_Lesefassung.md`](./BK6-24-174_GPKE_Teil2_Lesefassung.md) - GPKE Teil 2 (BK6-24-174 Lesefassung), focus Zuordnungsprozesse.
  - Use for current Lesefassung UC/SD: Ermittlung MaLo-ID, Kündigung, Lieferbeginn (incl. EEG/Tranche Fristen), Neuanlage, Ersatz-/Grundversorgung, 100 % LF-Zuordnung zu erzeugenden Marktlokationen, Lieferende LF↔NB, Abrechnungsdaten (Netznutzung/Bilanzkreis/Änderungsbestellung), Übermittlung gemessener Werte und Lieferschein, Netznutzungsabrechnung, NB-Preisblätter, Sperren/Entsperren und Wiederherstellung bei Lieferbeginn.
  - Prefer this over `bk620160_gpke.md` when the question is explicitly BK6-24-174 / GPKE Teil 2 scope or when UC/SD sequence detail is needed for Zuordnung.

- [`bk620160_gpke.md`](./bk620160_gpke.md) - GPKE Festlegung BK6-20-160 (Konsolidierte Lesefassung, gültig ab 01.04.2022).
  - Use for introductory GPKE chapters (Rollen/Objekte, Fristenberechnung, Identifikation), Basis- and Ergänzungsprozesse under the older festlegung, and where internal docs still cite BK6-20-160 line references.
  - Cross-check [`BK6-24-174_GPKE_Teil2_Lesefassung.md`](./BK6-24-174_GPKE_Teil2_Lesefassung.md) for the same business scenario when implementing against BK6-24-174.

- [`BDEW_AWH_LFW24_V1_7_20251208.md`](./BDEW_AWH_LFW24_V1_7_20251208.md) - 24h supplier switching application help.
  - Use for LFW24-specific interpretation, especially changes to billing/master data, Lieferbeginn follow-up data, configuration setup, iMS/§14a examples, Lieferende deadline examples, and Marktlokation shutdown cases.
  - Good companion to GPKE when GPKE gives the process but not enough operational nuance.

- [`AWH_Einführungsszenario_LFW24_Version_1.2.md`](./AWH_Einführungsszenario_LFW24_Version_1.2.md) - LFW24 introduction / go-live scenario (BK6-22-024).
  - Use for the 06.06.2025 cutover: GPKE/GeLi Gas holiday calendar, migration from Universalbestellprozess, message-version switch date, send windows (05.06./06.06.2025), end of Asynchronmodell (sync Netznutzung + Bilanzierung from 10.06.2025), and worked examples A–G for correcting Netznutzungs-/Bilanzierungswechsel timing mismatches.
  - Covers BK6-24-174 meter-reading transmission cutover in ch. 6; annex references per-process sequence diagrams for GPKE, WiM Strom, MPES.
  - Prefer this over `BDEW_AWH_LFW24_V1_7_20251208.md` for rollout/migration questions; prefer the operational AWH for steady-state LFW24 process interpretation.

- [`BK6-24-174_WiM_Teil1_Lesefassung.md`](./BK6-24-174_WiM_Teil1_Lesefassung.md) - WiM base metering processes.
  - Use for MSB contract/process topics: Kündigung Messstellenbetrieb, Beginn/Ende Messstellenbetrieb, Verpflichtung gMSB, Gerätewechsel, Geräteübernahme, Messlokationsänderung, mME/iMS installation, MSB price sheets, and MSB billing.

- [`BK6-24-174_WiM_Teil2_Lesefassung.md`](./BK6-24-174_WiM_Teil2_Lesefassung.md) - WiM value transmission processes.
  - Use for meter value lifecycle topics: Störungsbehebung, value preparation/transmission, Zwischenablesungswerte, value reclamation, value cancellation, LF/NB zählerstand transmission to MSB, Typ-2 values, and ESA value access.

- [`BDEW_AWH_Netzbetreiberwechselprozesse_Strom_V1_2_20251030.md`](./BDEW_AWH_Netzbetreiberwechselprozesse_Strom_V1_2_20251030.md) - Network operator change application help.
  - Use when the responsible NB MP-ID changes for locations: package ID, NBA/NBN handover, lists of locations, Lokationsbündel data, data to LF/MSB/ÜNB, and follow-up rules for GPKE/WiM assignments.

### EDIFACT Message Implementation

- [`APERAK_AHB_1_1_Konsultationsfassung_20260202.md`](./APERAK_AHB_1_1_Konsultationsfassung_20260202.md) - APERAK Anwendungshandbuch.
  - Use for market communication feedback handling: responsibilities between sender and receiver, CONTRL vs APERAK, syntaxfehlermeldung, verarbeitbarkeitsfehlermeldung, anerkennungsmeldung, APERAK AHB checks, object/business-case assignment checks, Strom/Gas APERAK rules, APERAK deadlines, feedback tables, and ERC error codes.
  - Note that this file is marked as a consultation version.

- [`UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.md`](./UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.md) - UTILMD Strom MIG.
  - Use for UTILMD segment groups and technical EDIFACT placement: UNH/BGM/DTM, sender/receiver NAD, LOC objects, Prüfidentifikator RFF, transaction references, status, dates, contact information, and master-data payload segments.

- [`MSCONS_MIG_2_4c_außerordentliche_20240726.md`](./MSCONS_MIG_2_4c_außerordentliche_20240726.md) - MSCONS MIG.
  - Use for generic MSCONS EDIFACT structure: message header, sender/receiver, delivery/consumption object, bilanzkreis, time periods, device/configuration references, quantities, status, correction reason, and meter/value positions.

- [`MSCONS_AHB_3_1f_Fehlerkorrektur_20250930.md`](./MSCONS_AHB_3_1f_Fehlerkorrektur_20250930.md) - MSCONS AHB.
  - Use for applied MSCONS scenarios: zählerstände, energiemengen, Lastgänge, MaBiS/Redispatch, Gasbeschaffenheit, marktlokationsscharfe lists, Werte nach Typ 2, stornierung/correction, and events that trigger value provision.
  - Read this before the MSCONS MIG when the question is semantic rather than structural.

- [`INVOIC_MIG_2.8e_20250401.md`](./INVOIC_MIG_2.8e_20250401.md) - INVOIC MIG.
  - Use for EDIFACT invoice structure: invoice number, dates, invoice type, references, sender/receiver, service address, line items, quantities, prices, taxes, discounts/surcharges, totals, and payment terms.

- [`ORDERS_MIG_1_4b_20250401.md`](./ORDERS_MIG_1_4b_20250401.md) - ORDERS MIG.
  - Use for EDIFACT order/request structure: order header, execution/start/end dates, product or service description, subscription/order metadata, references, participants, locations, customer/contact data, and configuration references.

- [`PRICAT_MIG_2_0e_Fehlerkorrektur_20250930.md`](./PRICAT_MIG_2_0e_Fehlerkorrektur_20250930.md) - PRICAT MIG.
  - Use for EDIFACT price-catalog structure: message header, sender/receiver, document dates, line items, article IDs, prices, and references. Stand MIG 2.0e (Fehlerkorrektur 30.09.2025).

- [`PRICAT_AHB_2_0f_Fehlerkorrektur_20251211.md`](./PRICAT_AHB_2_0f_Fehlerkorrektur_20251211.md) - PRICAT Anwendungshandbuch.
  - Use for applied PRICAT scenarios: Preisblatt Netznutzung (BGM+Z70), Messstellenbetrieb (Z32), Konfigurationen (Z77), Technik (Z94), MaBiS-related catalogs, and AHB checks on article codes. Stand 2.0f (11.12.2025); pairs with PRICAT MIG 2.0e.

### Code Lists

- [`Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md`](./Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md) - OBIS and media codelist.
  - Use for OBIS syntax, electricity/thermal-energy value groups, allowed OBIS codes in market communication, usage restrictions by MSCONS Prüfidentifikator, UTILMD master-data OBIS usage, media identifiers, and examples.
  - Note that this file is marked as a consultation version.

- [`Codeliste-Konfigurationen_1_3c_Fehlerkorrektur_20251211.md`](./Codeliste-Konfigurationen_1_3c_Fehlerkorrektur_20251211.md) - Codelist of configurations / measurement products (v1.3c).
  - Use for Messprodukt- and Konfigurationsprodukt-Codes (`9991…`): Standard-Messprodukte Strom/Gas für Werte nach Typ 1 (Markt-/Mess-/Netzlokation, Tranche), Konfigurationsprodukte (Schaltzeitdefinition, Leistungskurvendefinition, Ad-Hoc-Steuerkanal), Messprodukte für Werte nach Typ 2 aus SMGW/Backend und für ESA, Art der Werte / Messprodukt-Position-Codes, Mindestumfang der Messprodukte in der UTILMD (Strom/Gas), and Produkte zur Bestellung/Änderung von Daten an Lokationen (UTILMD/ORDERS).
  - Tells you which product codes a given Marktrolle (NB/LF/MSB/ESA) may order against the MSB. Read alongside WiM Teil 2 (value transmission) and the UTILMD/ORDERS/MSCONS MIGs for segment placement; this is a code/value codelist, not a process description.
  - This is a consolidated reading version with error corrections (Stand 11.12.2025).

- [`Codeliste_Artikelnummern und Artikel-ID_5_6_Fehlerkorrektur_20250930.md`](./Codeliste_Artikelnummern%20und%20Artikel-ID_5_6_Fehlerkorrektur_20250930.md) - Artikelnummern und Artikel-ID (v5.6).
  - Use for numeric Artikelnummern and structured Gruppenartikel-ID / Artikel-ID codes: per-Prüfi UTILMD/INVOIC/PRICAT columns, MSB Abrechnung Messstellenbetrieb chapters, and Bildungsvorschriften for article IDs referenced from AHB conditions.
  - Read alongside PRICAT AHB/MIG and INVOIC MIG when validating invoice or price-sheet line items; pair with UTILMD when PIA article codes appear in master-data messages.

### BDEW XML Originals (`xml-docs/`)

Machine-readable AHB/MIG files published by BDEW. They contain no prose: no introductions, no change history, and no referenced tables such as the MESZ/MEZ-to-UTC tables. Never start a process question here.

**Source precedence:** process/prose → Markdown in this folder · Prüfi requiredness → `../ahb-tables/` · MIG structure → Markdown, else XML · disputed or recently corrected row → BDEW XML.

| File | Type | Version | Role |
|---|---|---|---|
| `IFTSTA_MIG_2_0g_20250401 1.xml` | MIG | 2.0g | **Primary**: no Markdown MIG for IFTSTA |
| `REMADV_MIG_2_9e_20251001.xml` | MIG | 2.9e | **Primary**: no Markdown MIG for REMADV |
| `UTILMD_AHB-Strom_2_1_Fehlerkorrektur_20260629.xml` | AHB | 2.1 (Fehlerkorrektur 29.06.2026) | Verification. Same release as `ahb-tables/FV2604` (2.1, 29.06.2026) after the 2026-09-29 refresh; 185 of 187 Prüfis match row-for-row. Does not apply to FV2610 (UTILMD 2.2). |
| `MSCONS_AHB_3_1g_Fehlerkorrektur_20260302 2.xml` | AHB | 3.1g | Verification; newer than the `MSCONS_AHB_3_1f` Markdown |
| `ORDERS_AHB_1_1a_20251001.xml` | AHB | 1.1a | Verification |
| `IFTSTA_AHB_2_0h_Fehlerkorrektur_20250623.xml` | AHB | 2.0h | Verification |
| `REMADV_AHB_1_0a_20251001.xml` | AHB | 1.0a | Verification |
| `PRICAT_AHB_2_0f_Fehlerkorrektur_20251211.xml` | AHB | 2.0f | Verification; same version as [`PRICAT_AHB_2_0f_Fehlerkorrektur_20251211.md`](./PRICAT_AHB_2_0f_Fehlerkorrektur_20251211.md) |
| `UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.xml` | MIG | S2.1 | Duplicate of the Markdown MIG; tie-breaker only |
| `MSCONS_MIG_2_4c_außerordentliche_20240726 2.xml` | MIG | 2.4c | Duplicate of the Markdown MIG; tie-breaker only |
| `ORDERS_MIG_1_4b_20250401 1.xml` | MIG | 1.4b | Duplicate of the Markdown MIG; tie-breaker only |
| `INVOIC_MIG_2.8e__20250401.xml` | MIG | 2.8e | Duplicate of the Markdown MIG; tie-breaker only |
| `PRICAT_MIG_2_0e_Fehlerkorrektur_20250930.xml` | MIG | 2.0e | Duplicate of [`PRICAT_MIG_2_0e_Fehlerkorrektur_20250930.md`](./PRICAT_MIG_2_0e_Fehlerkorrektur_20250930.md); tie-breaker only |

Reading tip: each AHB file holds one `<AWF Pruefidentifikator="…">` block per Prüfi, with `<Bedingungen>`, `<UB_Bedingungen>`, and `<Pakete>` at the end of the file. Pull out only the `AWF` block you need plus the conditions it references. The UTILMD AHB is ~4 MB, so don't read the whole file.

## Agent Guardrails

- When `ahb-tables/` and a BDEW XML AHB of the same version disagree, the BDEW XML wins. State the discrepancy instead of silently picking one. First compare the XML's `Veroeffentlichungsdatum` with `meta.veroeffentlichungsdatum` in ahb-tables: a different date usually means a Fehlerkorrektur.

- Do not cite this index as the authority for a process or field. Cite the linked source document after reading it.
- For BDEW process questions, verify the process source here and then cross-check repo sources such as `docs-offline/`, `ebd-diagrams/`, `maco-api-documentation/`, `ahb-tables/`, and `maco-edi-testfiles/` as required by the workspace rules.
- MIG documents answer EDIFACT structure questions. They do not replace process descriptions, BO4E schemas, or Prüfi-specific business validation.
- The APERAK AHB answers feedback/error-handling questions after EDIFACT communication. It does not replace the process-specific response rules in GPKE/WiM or Conuti webhook schemas.
- The MSCONS AHB answers applied MSCONS usage questions. The UTILMD/INVOIC/ORDERS files in this folder are MIGs, not full process descriptions.
- For OBIS validity, use the codelist together with the relevant AHB/MIG and the concrete Prüfidentifikator context.

