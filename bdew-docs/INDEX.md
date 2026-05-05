# BDEW Documents Index

This index helps agents choose the right BDEW source document before answering MaKo questions. It is a navigation aid only: always open and read the linked source document before making process, deadline, field, or EDIFACT claims.

## Quick Routing

| Question type | Start with | Why |
|---|---|---|
| Supplier switching, cancellation, Lieferbeginn, Lieferende, Ersatz-/Grundversorgung, net usage billing, master data exchange | [`bk620160_gpke.md`](./bk620160_gpke.md) | Core GPKE process description for electricity customer supply processes. |
| 24h supplier switching details, timing, follow-up data after Lieferbeginn, BGM+E03 changes, iMS configuration, §14a, shutdown examples | [`BDEW_AWH_LFW24_V1_7_20251208.md`](./BDEW_AWH_LFW24_V1_7_20251208.md) | BDEW application help for Lieferantenwechsel 24 Stunden, with worked examples and clarification scenarios. |
| Metering operator processes: MSB cancellation/start/end, device changes, iMS/mME installation, MSB billing, MSB price sheets | [`BK6-24-174_WiM_Teil1_Lesefassung.md`](./BK6-24-174_WiM_Teil1_Lesefassung.md) | WiM Teil 1 covers metering base processes and MSB commercial processes. |
| Meter readings, measured values, value requests, reclamations, cancellations, values after Typ 2, ESA value access | [`BK6-24-174_WiM_Teil2_Lesefassung.md`](./BK6-24-174_WiM_Teil2_Lesefassung.md) | WiM Teil 2 covers collection, preparation, request, transmission, reclamation, and cancellation of values. |
| Network operator change, old/new NB handover, package ID, affected locations, data transfer to LF/MSB/ÜNB | [`BDEW_AWH_Netzbetreiberwechselprozesse_Strom_V1_2_20251030.md`](./BDEW_AWH_Netzbetreiberwechselprozesse_Strom_V1_2_20251030.md) | Application help for market processes when a location changes responsible NB MP-ID. |
| APERAK/CONTRL handling, syntax vs processing errors, acknowledgement messages, ERC error codes, APERAK deadlines | [`APERAK_AHB_1_1_Konsultationsfassung_20260202.md`](./APERAK_AHB_1_1_Konsultationsfassung_20260202.md) | APERAK Anwendungshandbuch for market communication feedback and error handling. |
| UTILMD EDIFACT segment structure, segment groups, fields, cardinalities, DTM/LOC/NAD/RFF layout | [`UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.md`](./UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.md) | UTILMD Message Implementation Guide for Strom, version S2.1. |
| MSCONS EDIFACT segment structure and generic MSCONS layout | [`MSCONS_MIG_2_4c_außerordentliche_20240726.md`](./MSCONS_MIG_2_4c_außerordentliche_20240726.md) | MSCONS Message Implementation Guide, version 2.4c. |
| MSCONS business usage, Prüfi-specific value scenarios, zählerstände, energiemengen, Lastgänge, MaBiS/Redispatch values, corrections | [`MSCONS_AHB_3_1f_Fehlerkorrektur_20250930.md`](./MSCONS_AHB_3_1f_Fehlerkorrektur_20250930.md) | MSCONS Anwendungshandbuch explains when and how MSCONS structures are used. |
| Invoice EDIFACT structure, invoice header/positions/taxes/amounts/payment terms | [`INVOIC_MIG_2.8e_20250401.md`](./INVOIC_MIG_2.8e_20250401.md) | INVOIC Message Implementation Guide, version 2.8e. |
| Order EDIFACT structure, requests/orders, product descriptions, references, locations, participants | [`ORDERS_MIG_1_4b_20250401.md`](./ORDERS_MIG_1_4b_20250401.md) | ORDERS Message Implementation Guide, version 1.4b. |
| OBIS codes, media codes, allowed OBIS for MSCONS/UTILMD, electricity/gas measuring identifiers | [`Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md`](./Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md) | External codelist for OBIS/media syntax and AHB checks. |

## How To Choose

1. If the question is about **what market process should happen and in which order**, start with GPKE, WiM, LFW24, or Netzbetreiberwechsel.
2. If the question is about **how an EDIFACT message is physically structured**, start with the matching MIG.
3. If the question is about **APERAK or CONTRL feedback, syntax errors, processing errors, acknowledgements, or ERC codes**, start with the APERAK AHB.
4. If the question is about **which MSCONS variant is allowed for a value scenario**, start with the MSCONS AHB, then check the MSCONS MIG for segment placement.
5. If the question is about **OBIS codes or media identifiers**, start with the OBIS/media codelist.
6. If the question is about **BO4E API fields, Conuti schemas, or trigger payloads**, do not rely on this folder alone. Use the repo schema sources in `maco-api-documentation/` after reading the relevant BDEW process context.

## Document Groups

### Process And Regulatory Context

- [`bk620160_gpke.md`](./bk620160_gpke.md) - GPKE customer supply processes.
  - Use for Kündigung, Lieferende, Lieferbeginn, Ersatz-/Grundversorgung, Netznutzungsabrechnung, Preisblatt NB, Sperren/Entsperren, Stammdatenaustausch, Geschäfts- und Kommunikationsdaten.
  - This is the broad process baseline for electricity supplier responsibilities.

- [`BDEW_AWH_LFW24_V1_7_20251208.md`](./BDEW_AWH_LFW24_V1_7_20251208.md) - 24h supplier switching application help.
  - Use for LFW24-specific interpretation, especially changes to billing/master data, Lieferbeginn follow-up data, configuration setup, iMS/§14a examples, Lieferende deadline examples, and Marktlokation shutdown cases.
  - Good companion to GPKE when GPKE gives the process but not enough operational nuance.

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

### Code Lists

- [`Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md`](./Codeliste-OBIS-Kennzahlen_Medien_2_5c_Konsultationsfassung_20250801.md) - OBIS and media codelist.
  - Use for OBIS syntax, electricity/thermal-energy value groups, allowed OBIS codes in market communication, usage restrictions by MSCONS Prüfidentifikator, UTILMD master-data OBIS usage, media identifiers, and examples.
  - Note that this file is marked as a consultation version.

## Agent Guardrails

- Do not cite this index as the authority for a process or field. Cite the linked source document after reading it.
- For BDEW process questions, verify the process source here and then cross-check repo sources such as `docs-offline/`, `ebd-diagrams/`, `maco-api-documentation/`, `ahb-tables/`, and `maco-edi-testfiles/` as required by the workspace rules.
- MIG documents answer EDIFACT structure questions. They do not replace process descriptions, BO4E schemas, or Prüfi-specific business validation.
- The APERAK AHB answers feedback/error-handling questions after EDIFACT communication. It does not replace the process-specific response rules in GPKE/WiM or Conuti webhook schemas.
- The MSCONS AHB answers applied MSCONS usage questions. The UTILMD/INVOIC/ORDERS files in this folder are MIGs, not full process descriptions.
- For OBIS validity, use the codelist together with the relevant AHB/MIG and the concrete Prüfidentifikator context.

