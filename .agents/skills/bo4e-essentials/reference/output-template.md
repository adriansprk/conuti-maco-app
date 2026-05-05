# Output template — section order and boilerplate

Fixed section order for `your-requests/<PI>_BO4E_ESSENTIALS.md`. Skip sections that don't apply (see "When each section applies" below), but don't reorder.

The bundled `scripts/lint-essentials.sh` enforces the mandatory subset. Run it
from the workspace root with `--repo-root "$PWD"`.

## Section order

1. **Title header** — `# NNNNN BO4E Essentials - <AHB description>` + the 4-line block: `Prüfidentifikator`, `Direction`, `Triggers`, `Process` (one-sentence summary).
2. **Trigger scope (disambiguation)** — small table mapping each candidate trigger to the Prüfi it actually generates. Required when the same `START_*` family covers multiple PIs, when there are siblings (e.g. `START_LIEFERBEGINN` → 55001 *and* 55077), or when a near-namesake trigger generates a different PI (e.g. `START_AUFHEBUNG_ZUK_ZUORDNUNG_LF` → **55038**, NOT 55004). Verify each row via `docs-offline/trigger-events-14016919e0.md` or the `allOf $ref: PI_NNNNN` in the schema. Skip if there is unambiguously one trigger and no siblings.
3. **Flow Summary** — table of all related PIs (request + success + rejection + follow-ups) + Mermaid `sequenceDiagram`.
4. **Regulation Anchors** — required for outbound LF→NB / LF→MSB Prüfis. Quote (don't paraphrase) the regulatory deadlines and gates with source file + line number: Vorlauffrist by scenario, counter-party response SLA, retroactive window, NB-Wechsel routing, time-gated codes (e.g. `ZZD`, `ZZB`, `A99` sunset). See `reference/project-static-values.md` § "Regulation anchors". Skip for inbound-only PIs that have no LF-side timing decisions.
5. **Prerequisites** — OAuth (reference `55001_BO4E_ESSENTIALS.md`'s snippet, don't re-document) + any lookup endpoints specifically needed for this PI. **If the flow resolves a counter-party MP-ID, include the NB-Wechsel routing warning** (lookup must use today's send date, not `vertragsende`/`vertragsbeginn`).
6. **How to Send / How to Handle** — HTTP verb, URL, response codes table. For inbound PIs: webhook handler shape instead.
7. **Annotated Example** — every field tagged `// static | dynamic | scenario-dependent | conditional`. Outbound only. **Required fields from the trigger schema** (e.g. `energierichtung`, `marktlokationsTyp.typ`) must be present — don't only reproduce what the test fixtures show.
8. **Validation Notes** — numbered list cross-checked against AHB `Muss`/`Kann`/conditional rules (with condition IDs translated), schema, trigger examples, test files, EBD, **and `bo4e-mapping/<FV>/<message>.csv`** (specifically the column for this PI, or an explicit "no dedicated column" gap). Always include: (a) "Fields Conuti auto-generates — do NOT send", (b) every AHB condition ID that matters (e.g. `[11]`, `[313]`, `[577]`, `[UB1]`), (c) any documentation discrepancy flagged explicitly, (d) schema-vs-test-file gaps (fields present in test but not in `PI_*.yml` or vice versa), (e) BO4E↔EDI mapping facts pulled from the CSV that aren't visible from schema alone (e.g. `energierichtung` ↔ `Z06/Z07`).
9. **AHB / Mapping Recheck** — outbound payload trust gate. Required whenever the doc has a Minimal Payload or Annotated Example. Include a table with: `Field / payload area`, `AHB evidence`, `BO4E mapping evidence`, `Authority`, `Payload implication`. State whether each mapping CSV has a dedicated PI column. Fixture-only or inferred fields must be labelled as lower authority.
10. **Value Pool / Transaktionsgrund tables** — every DE9013 code + meaning + scenario + DTM rule. One row per code from the AHB JSON. **Mark time-gated codes** (validity start date) with the source file/line.
11. **Minimal Valid Payload** — bare-minimum JSON the builder must emit. No comments inside JSON. Immediately before or after the JSON, include a field-authority table for every included field using one of: `AHB`, `Mapping`, `Schema`, `Process`, `Fixture`, `Inference`.
12. **Variants** — each scenario (Tranche, ruhende MaLo, future-cancellation, business customer, fixed-term, EnFG, time-gated codes like `ZZB`, etc.) as a diff block or replacement block.
13. **Response Format** — shape per paired response PI (55002/55003, 55005/55006…). Include `prozessId` correlation rule. Include at least one **EDIFACT wire-level snippet** for at least one paired response (extracted from `maco-edi-testfiles/inbound/v202510/<message>/<RESP>/*.edi`) — wire shape often disambiguates fields the schema leaves abstract. Inbound-only docs start here.
14. **EBD Antwortstatus Codes** — one table per decision path (standard vs Tranche vs MaLo etc.) when an EBD is paired with this flow. Pull every terminal code, including `A99` and any other catch-all. Note time-gates on result codes (e.g. A99 sunset).
15. **Field Classification Summary + Dynamic Fields Checklist** — dev-facing tables.
16. **Static Values Reference** — subset relevant to this PI, from `reference/project-static-values.md`. If the workspace does not provide concrete supplier/static values, mark them as a project configuration gap and keep examples placeholder-based.
17. **Quick Reference Card** — path-to-example table for lookup.
18. **Date Format** — one paragraph, from `reference/project-static-values.md`.
19. **PM Summary** — required (see boilerplate below).
20. **Ops Runbook** — required (see boilerplate below).
21. **Ticket Breakdown Suggestion** — 5–12 one-sentence tickets covering: outbound core, variants, business-logic mapping, inbound handlers per response PI, observability, **every time-gated code** (one ticket per gate: enable on activation date or remove on sunset date), NB-Wechsel routing if applicable, any regulatory deadline (LFW24, GPKE 6WT).
22. **Sources** — grouped by layer (Schema / Trigger / Tests / AHB / EBD / PNG / Offline / **BDEW** / **BO4E mapping**). Cite actual files, not `PROCESS_GRAPH.json`. BDEW citations must include the specific document name (`bk620160_gpke.md`, `BDEW_AWH_LFW24_*.md`, `BDEW_AWH_Netzbetreiberwechsel*.md`, `UTILMD_MIG_Strom_*.md`); the BO4E mapping citation must include the column reference and whether the PI has a dedicated column.

## When each section applies

| Section | Outbound request PI | Paired success PI | Paired rejection PI | Inbound-only / follow-up |
|---|---|---|---|---|
| Trigger scope | **required when ambiguous** (multi-PI trigger family or near-namesake) | n/a | n/a | n/a |
| Regulation Anchors | **required** | required if the success carries a downstream SLA | required if the rejection encodes a regulatory rule (e.g. Vorlauffrist) | required if the inbound message itself starts a counted timer |
| Annotated Example | **required** | skip (use the paired request's) | skip | required if user acts on it |
| AHB / Mapping Recheck | **required** | required if payload/handler fields are recommended | required if payload/handler fields are recommended | required if user acts on mapped payload fields |
| Minimal Valid Payload | **required** | skip | skip | skip |
| Variants | **required** | skip | skip | skip |
| Response Format | required | — | — | — |
| EBD Antwortstatus | **required** when response PI has EBD | **required** | **required** | n/a |
| PM Summary, Ops Runbook, Ticket Breakdown, Visualization, Sources | **always** | **always** | **always** | **always** |

## Mermaid sequence diagram — required shape

Participants at minimum: `Backend`, `Conuti`, `NB` (or `MSB`). Show: the outbound call, the EDIFACT hop, the async wait note, both response branches (success + rejection), any follow-up message.

## PM Summary — boilerplate structure

Source: `.cursor/rules/global-rules/pm-ops-summary-mandatory-always.mdc`. Fill each subsection from verified docs; never invent.

```markdown
## PM Summary

### Business Outcome (Definition of Done)
- [What success means from a business perspective]
- [What must be true in the LF system when this flow completes]
- [Whether follow-up processes must be received first]

### Supplier Responsibilities (LF)
- **Active**: [outbound messages, retries, triggers — per AHB + schema]
- **Passive**: [webhook handlers, persistence, monitoring — per response PIs]

### Customer Impact
- [What the customer experiences, if anything]
- [Timing: immediate vs asynchronous]
- [Communication implications on delay / rejection]

### Build Checklist
- Outbound triggers/APIs: [list]
- Inbound webhook handlers: [list by Prüfi]
- Persistence: [BO4E objects + states]
- Idempotency: [correlation keys, duplicate handling]
- Observability: [logs, metrics, alerts]
```

## Ops Runbook — boilerplate structure

```markdown
## Ops Runbook

### Operational Risk Points
- [Where failures can occur: validation, timing, partner, transport]
- [Which actor originates each error: LF / Conuti / NB / MSB]

### Retry Strategy
- Automatic: [what can be retried without human]
- Manual: [what needs human review first]
- Never: [what must not be retried — e.g. after confirmed 55002/55005]

### Escalation Policy
- To engineering: [triggers]
- To Conuti: [triggers + required artifacts]
- To NB / MSB: [triggers + required artifacts]
- Minimum data for ticket: prozessId, MaLo/Tranche ID, vertragsbeginn/ende, NB MP-ID, webhook PI, antwortstatus, freitext, raw EDI or BO4E payload.

### Runbook Artifacts
- Schemas: PI_<ID>.yml, yaml_output/<ID>.yaml
- Test files: maco-edi-testfiles/outbound/v202510/utilmd/<ID>/*.json (JSON outbound), inbound/v202510/utilmd/<ID>/*.edi (EDI inbound)
- EBD: ebd-diagrams/FV<latest>/E_<code>.{json,svg}
- PNG (if exists): docs-offline/prozessdiagramme-png/<name>.png
```

## Anti-patterns (fail the lint)

- No `## Flow Summary` / `## Validation Notes` / `## Sources` / `## PM Summary` / `## Ops Runbook` / `## Ticket Breakdown` section.
- Outbound payload doc has no `## AHB / Mapping Recheck` section.
- No ` ```mermaid ` block.
- References to `v202404` (must be `v202510`).
- `PROCESS_GRAPH.json` cited in `## Sources` (it's an index, cite the files it points to).
- Annotated fields without a classification tag.
- AHB condition IDs (`[11]`, `[313]`, `[UB1]`, etc.) mentioned but not translated to plain English.
- Minimal Payload fields without authority tags (`AHB`, `Mapping`, `Schema`, `Process`, `Fixture`, `Inference`) in the adjacent field-authority table.
