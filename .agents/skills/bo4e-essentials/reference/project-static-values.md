# Project static values

Workspace-specific values that do not vary across outbound messages. Use committed
values as-is when this workspace provides them. If a consuming repo does not
provide equivalent values, do not invent replacements; mark the values as a
project configuration gap and keep examples clearly placeholder-based.

| Value | Meaning | Path(s) |
|---|---|---|
| `9979242000006` | Supplier BDEW MP-ID (absender on outbound) | `transaktionsdaten.absender.rollencodenummer` |
| `11X0-0000-0559-B` | Supplier Bilanzkreis ID | `erforderlichesProduktpaket[].produkt[].wertedetails` for Bilanzkreis |
| `9991000002082` | Product code — **Bilanzkreis** | `erforderlichesProduktpaket[].produkt[].produktCode` |
| `9991000002008` | Product code — **Prognosegrundlage / Jahresverbrauchsprognose** | `produkt[].produktCode` |
| `9991000002115` | Eigenschaft — **SLP** (Standard Load Profile) | `produkt[].codeProdukteigenschaft` |
| `9991000002131` | Eigenschaft — **RLM** (Registrierende Leistungsmessung) | `produkt[].codeProdukteigenschaft` |
| `BDEW` | rollencodetyp for all MP-IDs | `absender.rollencodetyp`, `empfaenger.rollencodetyp` |
| `STROM` | Sparte | `transaktionsdaten.sparte`, on each BO-typed object |
| `NETZNUTZUNGSVERTRAG` | vertragsart | `NETZNUTZUNGSVERTRAG[].vertragsart` |
| `ENERGIELIEFERVERTRAG` | vertragsart | `ENERGIELIEFERVERTRAG[].vertragsart` |
| `MALO` | lokationsTyp | `NETZNUTZUNGSVERTRAG[].lokationsTyp` |
| `KUNDE` | geschaeftspartnerrolle | `vertragspartner2[].geschaeftspartnerrolle` |
| `ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR` | Abort if Produktpaket can't be assigned | `erforderlichesProduktpaket[].umsetzungsgradvorgabe` |

## Date conventions

Always ISO 8601 UTC, pointing to German midnight:
- Winter (CET, UTC+1): `23:00:00Z` = 00:00 local
- Summer (CEST, UTC+2): `22:00:00Z` = 00:00 local

For supplier-switch pairs (`vertragsende` on outgoing 55004 + `vertragsbeginn` on incoming new LFN's 55001) the two instants must match exactly — the NB rejects gaps.

## Kategorie conventions

- `E01` = Lieferbeginn / Anmeldung (55001, 55077 etc.)
- `E02` = Lieferende / Abmeldung (55004, 55007 etc.)

Kategorie is derivable from the PI's `Description` in `ahb-tables/INDEX.md` plus its BGM code in the AHB (`BGM+E01` vs `BGM+E02`).

## Time-gates (FV2604 / 2026 calendar)

Several AHB conditions and EBD result codes are time-gated. **Always re-verify the exact date from the source file (AHB JSON / EBD JSON / LFW24 doc) — don't trust memory or this table; the regulation moves under us.** Cite the source path next to the date in the doc.

Compare today's date against each time-gate. If the gate is **already in the past**, document the code as live and remove "future" framing. If the gate is in the future, mark the code as "valid from <date>" and put a Ticket Breakdown item to enable it.

Known examples (re-verify before citing):

| Code / topic | Gate | Source | Direction |
|---|---|---|---|
| `[313]` on STS+7 `ZZD` (Übergangsversorgung) | `DTM+137 ≥ 2026-03-31 22:00 UTC` | `ahb-tables/FV2604/AHB_FV2604_55004.json` (cond `[313]`) | live as of 2026-04 |
| `ZZB` "Stilllegung incl. Stilllegung MaLo" (transaktionsgrundergaenzung) | valid from `2026-04-01` | `bdew-docs/BDEW_AWH_LFW24_V1_7_20251208.md` lines 3202, 3230, 3239 | live as of 2026-04 |
| `DTM+206` Geräteausbaudatum on stilllegung flow | valid from `2026-04-01` | `bdew-docs/BDEW_AWH_LFW24_V1_7_20251208.md` line 3211 | live as of 2026-04 |
| `A99` "Sonstiges" sunset on E_0607 | "Nutzungsmöglichkeit Ende: **01.10.2026 00:00 Uhr**" | `ebd-diagrams/FV2604/E_0607.json` Step 140 / Step 620 | live, retires 2026-10-01 |

When a time-gate is mentioned, the doc must include a Ticket Breakdown item that pins the gate date (either an enable-flag for a future gate or a cleanup ticket for a sunset).

## Regulation anchors (extract verbatim from `bdew-docs/`)

For outbound LF→NB / LF→MSB Prüfis, extract these anchors and put them in a top-level `## Regulation Anchors` section. Don't paraphrase — quote the rule with the source file + line number.

| Anchor | Where to find it | Example value |
|---|---|---|
| **LF Vorlauffrist** by scenario (LFW / Stilllegung / Tranche) | `bdew-docs/bk620160_gpke.md` §3.1.2 + `BDEW_AWH_LFW24_V1_7_20251208.md` §9 | 6 WT (LFW), Tag-vor-letztem-WT (Stilllegung), 1 Monat (Tranche/erzeugend) |
| **NB / counter-party response SLA** | `bdew-docs/bk620160_gpke.md` (per Use-Case SD table) | "spätestens Ablauf 3. WT" |
| **Retroactive window for sonstige Abmeldungen** | `bdew-docs/bk620160_gpke.md` §II.0 Grundregeln | bis 6 Wochen rückwirkend |
| **NB-Wechsel routing** (any flow that resolves NB MP-ID) | `bdew-docs/BDEW_AWH_Netzbetreiberwechselprozesse_Strom_V1_2_20251030.md` | Abmeldungen → NBA bis Änderungszeitpunkt, danach NBN |
| **Code catalogue confirmations** | `bdew-docs/UTILMD_MIG_Strom_S2_1_Fehlerkorrektur_20260302.md` | DE1001 BGM codes (E01/E02/E03/Z14/E35/E44/E40/Z05); RFF+Z13 Prüfi catalogue |

If `bdew-docs/` does not contain a matching anchor for a specific Prüfi (rare — typical for technical-only artifacts like APERAK / DLQ), say so explicitly in `## Regulation Anchors`. A missing anchor for an outbound Prüfi is a red flag.
