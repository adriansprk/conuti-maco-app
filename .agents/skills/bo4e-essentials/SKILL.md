---
name: bo4e-essentials
description: Produce a ticket-ready "BO4E Essentials" markdown doc for a specific BDEW Prüfidentifikator (e.g. 55007, 17133, 13016) or composite Conuti trigger flow (e.g. START_VERSAND_ANF_STORNO) in a MaCo workspace checkout, cross-validated against regulatory bdew-docs, docs-offline, PNG, EBD, PI_xxx.yml/yaml_output, trigger, AHB, bo4e-mapping, and maco-edi-testfiles v202510 layers. Use when the user asks "/bo4e-essentials NNNNN", "create an overview / essentials doc / BO4E payload doc for Prüfi NNNNN", "document the flow for NNNNN/START_* so I can create tickets", or "validate NNNNN against AHB and write it up". Output defaults to your-requests/NNNNN_BO4E_ESSENTIALS.md or your-requests/FLOW_NAME_BO4E_ESSENTIALS.md; the doc must pass this skill's bundled lint and verification scripts. Do NOT use for general BO4E questions, reading existing docs, or quick single-field answers.
---

# BO4E Essentials — skill

Orchestrator. Produces `your-requests/<PI>_BO4E_ESSENTIALS.md` or `your-requests/<FLOW_NAME>_BO4E_ESSENTIALS.md` by walking a fixed source-layer gathering pass, emitting a verification checkpoint, then writing in the house format. Tool-agnostic: the same workflow applies whether invoked by Claude Code, Codex, or Cursor.

Run from the workspace root: the directory containing source folders such as `ahb-tables/`, `bdew-docs/`, `bo4e-mapping/`, `docs-offline/`, `maco-api-documentation/`, and `maco-edi-testfiles/`. Do not assume an absolute local path. Resolve `SKILL_DIR` to this skill folder, for example:

```bash
SKILL_DIR="${SKILL_DIR:-.agents/skills/bo4e-essentials}"
```

## Trust contract

The doc is not trusted because it has examples or because it passes shape lint. It is trusted only when every payload recommendation is tied to this authority order:

1. **AHB JSON** (`ahb-tables/FV<latest>/AHB_*.json`) — authoritative for EDIFACT requiredness, value pools, condition IDs, and scenario-specific rules.
2. **BO4E mapping CSV** (`bo4e-mapping/<FV>/<message>.csv`) — authoritative for BO4E field path ↔ EDIFACT segment/qualifier mapping, but only when the target PI has a dedicated column or the doc explicitly marks that the evidence is shared-only.
3. **Trigger / request schema** — authoritative for Conuti envelope and generic JSON shape, but not sufficient for PI-specific value-pool restrictions.
4. **Process docs / processinfo** — authoritative for lifecycle sequence, role direction, and related PIs.
5. **Fixtures** (`maco-edi-testfiles`) — examples only. Fixtures may show plausible payloads but do **not** establish requiredness, completeness, legal value pools, or production-safe product codes.

Every outbound doc with a payload must include an `## AHB / Mapping Recheck` section and a field-authority table. Each payload field must be classified as `AHB`, `Mapping`, `Schema`, `Process`, `Fixture`, or `Inference`. `Fixture` and `Inference` fields must be explicitly labelled as non-authoritative and must not be presented as required unless AHB/mapping also proves them.

## Composite-flow mode

The default output remains one doc per PI. If the user asks for a business process that spans multiple PIs (for example, "already running delivery -> configure Module 3"), create a composite doc:

- Output path: `your-requests/<FLOW_NAME>_BO4E_ESSENTIALS.md`
- Run evidence:
  - `your-requests/.runs/<FLOW_NAME>/` for the cross-process summary and the primary request PI.
  - Use extra `your-requests/.runs/<PI>/` directories only when there are multiple independent primary outbound/request PIs with their own payload builders.
- Verification:
  - Run `"$SKILL_DIR/scripts/lint-essentials.sh" --repo-root "$PWD" <path-to-composite-doc>`.
  - Run `python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage final <FLOW_NAME> --primary-pi <PI> --doc <path-to-composite-doc>` for the composite run directory.
  - For legacy compatibility, `python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage final <PI> --doc <path-to-composite-doc> --run-dir your-requests/.runs/<FLOW_NAME>` is also acceptable.

Do **not** force a composite flow into one arbitrary PI. Do **not** pretend a fixture-backed follow-up is the direct response to the primary PI. The doc must separate prerequisites, direct responses, follow-ups, and parallel inbound messages.

## Authoritative rules (read when present)

These workspace rule files govern the doc's content and style when the checkout includes them. Read them when present. If a consuming checkout does not include `.cursor/rules/`, apply the summarized requirement after each path and continue:

- `.cursor/rules/global-rules/anti-hallucination-mandatory-always.mdc` — cite source files, never guess.
- `.cursor/rules/global-rules/maco-workspace-context-always.mdc` — source-file taxonomy (the six source layers this skill walks).
- `.cursor/rules/global-rules/pm-ops-summary-mandatory-always.mdc` — mandatory PM Summary + Ops Runbook on output.
- `.cursor/rules/validation-rules/pruefidentifikator-verification-mandatory-always.mdc` — find ALL request formats + ALL response PIs.
- `.cursor/rules/visualization-rules/process-visualization-mandatory-always.mdc` — mandatory Mermaid sequence + flow + field table.

## Skill-local references

Load on demand during the workflow:

- `reference/pruefi-patterns.md` — numbering patterns (XX001→XX002/XX003, XX077→XX078/XX080, XX600→XX602/XX603) + derivation recipe.
- `reference/project-static-values.md` — workspace-specific MP-ID / Bilanzkreis / product codes when present, date conventions, known time-gates.
- `reference/output-template.md` — fixed section order + mandatory-section table + PM Summary / Ops Runbook boilerplate.
- `reference/verification-artifacts.md` — structured handoff JSON files, event log, verifier contract, and source-citation rules.
- `scripts/lint-essentials.sh` — bundled markdown shape linter; run from any workspace root with `--repo-root`.
- `scripts/verify-bo4e-essentials.py` — bundled deterministic evidence verifier; run from any workspace root with `--repo-root`.

## Template exemplars

- `your-requests/55001_BO4E_ESSENTIALS.md` — outbound, parent flow with paired responses.
- `your-requests/55004_BO4E_ESSENTIALS.md` — outbound with EBD response codes + ticket breakdown.

*Note: both exemplars predate the PM Summary / Ops Runbook mandate. New docs include those sections; the linter enforces it. Regenerate existing docs through this skill to bring them into compliance.*

## Workflow (deterministic)

### Step 0 — Open a run evidence directory

Create `your-requests/.runs/<PI>/` before source gathering. Treat it as the run's structured handoff area, not as final user documentation.

Write these files during the workflow, following `reference/verification-artifacts.md`:

- `events.jsonl` — append every meaningful file read, derivation, gap, and decision.
- `tool_trace.jsonl` — append every tool call used for source discovery/reading, with files read and produced extraction IDs.
- `classification.json` — PI metadata from `ahb-tables/INDEX.md` / `INDEX.json`.
- `related_pis.json` — request formats, success responses, rejection responses, sibling requests, follow-ups.
- `sources_manifest.json` — every source file actually read, grouped by layer, with explicit missing entries for optional gaps.
- `layer_claims.json` — what each authoritative source layer contributed to the unified process picture.
- `doc_coverage.json` — AHB condition IDs, value-pool codes, and EBD terminal codes the final markdown must cover.

These artifacts are the deterministic "sensor" layer: Python verifies them before the markdown is accepted. Keep them compact and factual; do not write prose summaries there.

`tool_trace.jsonl` is not a quality signal by itself. It is only a reproducibility trace. Every traced source read must lead to a concrete `layer_claims.json` claim with structured `extracted_values`, or the source read is considered unused.

### Step 1 — Classify the PI

Read `ahb-tables/INDEX.md`. Capture:
- `description` (e.g. "Anmeldung verb. MaLo", "Abmeldung")
- `direction` (`LF → NB`, `NB → LF`, etc.)
- `versionsnummer` + `veroeffentlichungsdatum` + which FV directory to use (latest wins — prefer `FV2604`).

Write the result to `your-requests/.runs/<PI>/classification.json` and append an `events.jsonl` entry with the index files read.

**Direction decides framing:**
- Outbound (`LF → *`): full doc with annotated example + variants + payload builder guidance.
- Inbound (`* → LF`): webhook-handler doc focused on `antwortstatus` / `freitext` parsing + `prozessId` correlation. Still needs PM Summary, Ops Runbook, Sources, Ticket Breakdown.

### Step 2 — Derive all related Prüfis

Apply `reference/pruefi-patterns.md`:
1. For the whitelisted known patterns in `reference/pruefi-patterns.md`, compute paired response PIs and then **verify each exists** in `ahb-tables/INDEX.md`.
2. For every other flow, especially ORDERS/ORDRSP/IFTSTA, derive relationships from `processinfo.json`, `docs-offline/*`, AHB, and fixtures. Do **not** use `PI+1` / `PI+2` as evidence.
2. Check the trigger schema (`maco-api-documentation/macoapp-trigger/components/schemas/START_*.yml`) for `oneOf` / `allOf` — find sibling request PIs sharing the trigger (e.g. 55001 + 55077 both under `START_LIEFERBEGINN`).
3. Cross-verify on the NB side: `grep -r "Übergabe der erzeugten Rückmeldung" docs-offline/` — explicit list of which PIs the NB generates.
4. List any follow-up PIs (e.g. 55037 after a successful 55005) — include them in Flow Summary; flag as follow-ups, not direct responses.
5. **Response polarity check:** for every `success_responses` / `rejection_responses` entry, cross-check AHB `meta.description`, `PI_<N>.yml` description, and any process overview/tab labels. If process docs say "pos/neg", "Bestätigung", or "Ablehnung" in conflict with AHB/schema, keep AHB/schema as authority and add a "Documentation discrepancy" note with exact file paths and lines. Do not silently normalize swapped labels.

Write all derived and verified related PIs to `your-requests/.runs/<PI>/related_pis.json`. The final doc must mention every PI listed there.

### Step 2.5 — Trigger ↔ Prüfi disambiguation (mandatory)

A near-namesake trigger does **not** imply the same Prüfi. Concretely: `START_AUFHEBUNG_ZUK_ZUORDNUNG_LF` generates **PI_55038**, NOT 55004. `START_LIEFERENDE` (LF side) generates 55004; `START_LIEFERENDE` (NB side, via the `oneOf` arm) generates 55007. Conflating these has produced wrong docs in the past.

For every candidate trigger surfaced in Step 2, **prove the trigger → Prüfi mapping** before listing it as a trigger for this PI:

1. Open `docs-offline/trigger-events-14016919e0.md` and grep for the trigger name. The OpenAPI block exposes the schema `[LF] START_X` / `[NB] START_X` arms with `allOf $ref: PI_NNNNN` — the referenced PI is what that trigger actually generates.
2. Or open the trigger schema directly (`macoapp-trigger/components/schemas/START_*.yml`) and locate the `allOf $ref` to the `PI_NNNNN` schema.
3. List in `your-requests/.runs/<PI>/related_pis.json` only triggers whose mapping you've proven points at this PI. Add a `trigger_proofs` array with `{trigger, role, generates_pi, source_path, line_or_excerpt}` per row.
4. If a trigger looks topically related but generates a different PI, list it in the doc's `## Trigger scope` section as a *do-not-confuse* row, not as a trigger for this PI.

Pitfall this guards against: copying the trigger list from a sibling doc / prior agent output without re-verifying.

### Step 3 — Source gathering (one read per layer)

Use `docs/entry-points/PROCESS_GRAPH.json` indexes (`by_bdew_id`, `by_trigger`, `by_process_name`) for discovery, then read source files. Don't cite the index — cite the source files.

For PI `N`, collect at least one artifact from **each applicable layer**:

| Layer | Path pattern | Read purpose | Mandatory? |
|---|---|---|---|
| **Regulation (WHY by law)** | `bdew-docs/bk620160_gpke.md` (Use-Case + SD + Vorlauffrist + counter-party SLA), `bdew-docs/BDEW_AWH_LFW24_V1_7_*.md` (LFW Fristen, time-gated codes, stilllegung), `bdew-docs/BDEW_AWH_Netzbetreiberwechselprozesse_*.md` (NBA↔NBN routing if MP-ID lookup is involved), `bdew-docs/UTILMD_MIG_Strom_S2_1_*.md` (MIG code catalogue confirmations) | Extract the **Regulation Anchors** for the doc: Vorlauffristen by scenario, counter-party response SLA, retroactive windows, NB-Wechsel routing rule, time-gated codes. **Quote, don't paraphrase**, with line numbers. | **Mandatory** for outbound LF→NB / LF→MSB Prüfis. Inbound-only docs may legitimately skip if no LF-side timing decisions exist. |
| Process (WHY by design) | `docs-offline/<flow>-*.md` (match by flow name / role) | Mermaid flow, role narrative, "ref" references | Always read at least the LF-role and NB-role variants if they exist |
| Architecture (HOW) | `docs-offline/prozessdiagramme-png/INDEX.md` → `<flow>.png` | Swimlanes, BO4E↔EDI transform points | If exists |
| Validation (WHAT) | `ebd-diagrams/FV<latest>/E_<code>.json` (find code via "Entscheidungsbaum E_" grep in process docs OR via the EBD's `metadata.section` linking back to the GPKE chapter) | Decision tree + antwortstatus codes; **also extract any time-gated result codes** (e.g. `A99` sunset dates) from the JSON `note` fields | If a paired response carries an EBD |
| BO4E schema | `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_<N>.yml` + `pythons/createPiFromTemplater/templater/yaml_output/<N>.yaml` | Field schema (+ diff if they disagree) | **Mandatory** — gate |
| **BO4E→EDIFACT mapping** | `bo4e-mapping/<FV>/UTILMD_Strom.csv` (or `UTILMD_Gas.csv` / message-specific CSV); the column header for this PI carries the directional + Muss/Kann marker | Concrete BO4E field path ↔ EDIFACT segment/qualifier bridge; pulls out facts schema can't show (e.g. `energierichtung` ↔ `Z06/Z07`). You must prove whether the PI has a dedicated column. If not, mark mapping support as `shared-only` or `missing` and fall back to AHB for requiredness. | **Mandatory** — gate |
| Trigger | `macoapp-trigger/components/schemas/START_*.yml` + matching `examples/*.yml` + `docs-offline/trigger-events-14016919e0.md` (the trigger ↔ PI proof source) | Outbound envelope, variant examples, **trigger ↔ PI mapping** for Step 2.5 | Mandatory for outbound |
| EDIFACT | `ahb-tables/FV<latest>/AHB_FV<latest>_<N>.json` | `Muss`/`Kann`, value pools (DE9013 etc.), conditional rule IDs | **Mandatory** — gate |
| Examples | `maco-edi-testfiles/outbound/v202510/<message>/<N>/*.json`, `inbound/v202510/<message>/<N>/*.edi` | Scenario fixtures. Use them to confirm shape and wire examples, never to infer requiredness or valid value pools. **At least one inbound `.edi` for a response PI must be quoted** when wire-level response shape matters. | Mandatory if wire-level snippet expected |
| Conuti webhook JSON | `maco-api-documentation/macoapp-schreiben/components/examples/Strom/<N>_eingehend_Testfall*.yaml` | BO4E shape delivered to your webhook | If exists |

**Missing sources are information.** If a layer has no artifact for this PI (e.g. no PNG for a niche PI, no EBD for a non-response PI), note it explicitly in the Validation Notes — don't fabricate paths. **A missing `bdew-docs/` regulation anchor for an outbound Prüfi is a red flag** — go look harder before declaring it absent.

### Step 3.5 — Time-gate awareness check (mandatory)

Today's date matters. For each time-gated code identified in the AHB / LFW24 / EBD, compare to today (`date +%Y-%m-%d`):

- **Already in the past** → document as "live since <date>", remove "future" framing, ensure the variant has a Variants block, add a one-time *cleanup* ticket if the code has a sunset.
- **In the future** → document as "valid from <date>", add a one-time *enable* ticket pinned to that date, mark the corresponding Variants block as "not yet enabled".

Examples (re-verify per PI):
- `ZZB` Stilllegung incl. Stilllegung MaLo: live since `2026-04-01` → should appear as a regular ergaenzung row.
- `ZZD` Übergangsversorgung condition `[313]`: live since `2026-03-31 22:00 UTC`.
- `A99` on E_0607: retires `2026-10-01` → cleanup ticket.

Also write `your-requests/.runs/<PI>/sources_manifest.json` while gathering. Use repo-relative paths, and mark optional missing layers explicitly with `{"status": "missing", "reason": "..."}`. Do this for every layer, even when the result is "none found"; a silent missing layer fails verification. Schema + BO4E mapping + AHB + either trigger or webhook example are hard gates.

Write `your-requests/.runs/<PI>/layer_claims.json` as you read each layer. Use one claim per important contribution:

- `regulation`: deadlines, time-gates, legal framing from BDEW/GPKE/LFW/WiM docs.
- `process`: sequence, role direction, `ref` processes, follow-ups from `docs-offline/*.md`.
- `architecture`: swimlane/system handoff/format transformation facts from PNG diagrams.
- `validation`: EBD decision paths, terminal `antwortstatus`, acceptance/rejection codes.
- `bo4e_schema`: payload shape, required fields, types, enums, generated-field discrepancies.
- `bo4e_mapping`: concrete BO4E path ↔ EDIFACT segment/qualifier mappings.
- `bo4e_mapping`: concrete BO4E path ↔ EDIFACT segment/qualifier mappings, plus `mapping_column_checks` stating `{pi, csv_path, has_dedicated_column, evidence}`.
- `edifact`: AHB `Muss`/`Kann`, condition IDs, value pools, segment rules.
- `examples`: scenario fixtures and wire-level examples, always `v202510`.
- `trigger` / `webhook`: outbound event shape or inbound response shape.

Every claim must point to a path listed under the same layer in `sources_manifest.json`, include short evidence text, and list `doc_terms` that must appear in the final markdown.

Every claim must also include `extracted_values`. Examples:

- AHB claim: `{"required_inputs": [...], "conditions": [...], "value_pool_codes": [...]}`
- BO4E schema claim: `{"fields": [...], "required_fields": [...], "objects": [...]}`
- BO4E mapping claim: `{"mappings": [{"bo4e_path": "...", "edifact": "..."}]}`
- EBD claim: `{"validation_steps": [...], "terminal_codes": [...]}`
- Process/offline-doc claim: `{"process_steps": [...], "follow_ups": [...], "ref_processes": [...]}`
- PNG claim: `{"swimlanes": [...], "transformations": [...], "handoffs": [...]}`

Write `your-requests/.runs/<PI>/doc_coverage.json` from the gathered source facts:

- `ahb_condition_ids`: every important `[N]` / `[UBn]` condition the final doc must explain.
- `value_pool_codes`: every transaktionsgrund / DE9013 / scenario code covered in the value-pool tables.
- `ebd_terminal_codes`: every terminal Antwortstatus code covered from paired EBD trees.
- `mapping_column_checks`: every message CSV checked, including whether the PI has a dedicated header column. If `has_dedicated_column=false`, the final doc must say so.
- `field_authority`: every field in the Minimal Payload / Annotated Example, with `{field, authority, source}` where authority is one of `AHB`, `Mapping`, `Schema`, `Process`, `Fixture`, `Inference`.
- `response_polarity_checks` when paired responses exist, with `{pi, expected: "success"|"rejection", ahb_description, schema_description, process_label_findings}`. If any process label conflicts with AHB/schema, the final markdown must include a documentation-discrepancy note citing the offending source path(s).

### Step 4 — Pre-write checkpoint (mandatory)

Before writing the output file, make sure the run artifacts exist and run:

```bash
python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage sources <N>
```

For composite trigger-flow docs, run the same gate with the flow id and primary request PI:

```bash
python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage sources <FLOW_NAME> --primary-pi <N>
```

This is the deterministic source-evidence gate. It must pass before writing the final markdown.

Then emit a verification block in the chat (not in the output file) listing every file actually read, grouped by layer, **plus the trigger ↔ Prüfi proofs and the regulation anchors extracted**. This is the "halt and prove you did the work" checkpoint. Template:

```
Checkpoint for PI <N>:
- Classification: <description> / <direction> / <FV>
- Triggers proven (Step 2.5): {<trigger>: <generates_pi> via <source_path>}
  Do-not-confuse: {<trigger>: <generates_pi> (NOT this one)}
- Related PIs (derived): request formats [...], successes [...], rejections [...], follow-ups [...]
- Regulation Anchors extracted from bdew-docs:
  - LF Vorlauffrist (LFW): <value> — <source path:line>
  - LF Vorlauffrist (Stilllegung): <value> — <source path:line>
  - LF Vorlauffrist (Tranche/erzeugend): <value> — <source path:line>
  - Counter-party response SLA: <value> — <source path:line>
  - Retroactive window: <value or n/a> — <source path:line>
  - NB-Wechsel routing: <applies?> — <source path:line>
- Time-gates checked against today (<YYYY-MM-DD>):
  - <code>: <gate-date> → <live | future-pending>
- Sources read:
  - Regulation: <bdew-docs path(s) or "none — flag if outbound">
  - Process: <path(s)>
  - Architecture: <path or "no PNG for this PI">
  - Validation: <EBD path or "no paired EBD">
  - BO4E schema: <path>
  - BO4E mapping: <bo4e-mapping CSV path + column index>
  - Trigger: <path(s) or "inbound-only">
  - EDIFACT: <AHB path>
  - Examples: <path(s)>
- Gaps flagged: [...]
```

Proceed only if at least schema + AHB + BO4E mapping + (trigger-or-webhook-example) are present **and** for outbound LF→NB / LF→MSB Prüfis at least one regulation anchor from `bdew-docs/` was extracted. If any hard gate is missing, stop and tell the user — don't guess.

Additional outbound payload gate: before writing, explicitly compare the payload skeleton against AHB and BO4E mapping. The checkpoint must state:

- AHB-required segments/value-pool codes that drive each payload field.
- BO4E mapping CSV path, whether the PI has a dedicated column, and which BO4E paths are marked for that PI.
- Fixture-only fields removed or demoted to example-only.
- Any field still listed as `Inference`, with a risk note.

### Step 5 — Write output

Write `your-requests/<N>_BO4E_ESSENTIALS.md` using the section order in `reference/output-template.md`. The output table in that reference tells you which sections apply for request / success / rejection / inbound-only PIs. PM Summary, Ops Runbook, Sources, Ticket Breakdown, and a Mermaid diagram are **always required** (enforced by the linter).

Apply `pruefidentifikator-verification-mandatory-always.mdc`: every related PI goes into Flow Summary with its direction + purpose + trigger.

Translate every AHB condition ID (e.g. `[11]`, `[313]`, `[577]`, `[UB1]`) into plain English in Validation Notes — don't leave the bracketed IDs unexplained.

Use project static values from `reference/project-static-values.md` verbatim when this workspace supplies them. If a consuming repo has no equivalent static values, mark them as a configuration gap and use obvious placeholders in examples. Date format per the same reference.

For outbound payloads, write `## AHB / Mapping Recheck` before `## Minimal Valid Payload`. This section must be the source-of-truth bridge from AHB/mapping to the payload. If a mapping CSV has no dedicated PI column, say that directly and treat any fixture-derived fields as lower confidence.

### Step 6 — Verify and lint

Run both bundled commands from the workspace root:

```bash
SKILL_DIR="${SKILL_DIR:-.agents/skills/bo4e-essentials}"
python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage final <N>
"$SKILL_DIR/scripts/lint-essentials.sh" --repo-root "$PWD" <N>
```

Both must exit 0. If either fails, fix the artifacts or output; don't disable the verifier or linter. Every concrete path in `sources_manifest.json` must exist and be cited in the final `## Sources` section.

Warnings (non-failing) are expected for inbound-only PIs that legitimately omit Minimal Payload / Annotated Example — acknowledge them in your end-of-turn summary rather than silencing them.

## Pitfalls (don't repeat these)

- **Don't cite `PROCESS_GRAPH.json` as a source.** It's a discovery index; cite the files it points to.
- **Don't copy enriched outbound test files as if user-supplied.** Strip `datenaustauschreferenz`, `vorgangsnummer`, `pruefidentifikator`, `dokumentennummer`, `nachrichtendatum`, `nachrichtenreferenznummer` — Conuti generates these.
- **Don't conflate direct responses with follow-ups.** E.g. 55037 (*Informationsmeldung zur Beendigung der Zuordnung*) follows a successful 55005; it is **not** the success response to 55004.
- **Don't conflate near-namesake triggers.** `START_AUFHEBUNG_ZUK_ZUORDNUNG_LF` generates **PI_55038**, NOT 55004. Always verify trigger → PI via `docs-offline/trigger-events-14016919e0.md` (Step 2.5).
- **Don't leave AHB condition IDs unexplained.** Every `[N]` / `[UBn]` encodes a real rule — translate it.
- **Don't skip variants.** Every `transaktionsgrundergaenzung` / scenario branch in the AHB value pool needs coverage (full example or diff block). Time-gated codes (`ZZB`, `ZZD`) need their gate-date mentioned.
- **Don't invent paths.** If a file doesn't exist for this PI, say so — don't link a dead path.
- **Don't merge PIs.** One doc per PI. Paired responses are documented inside the parent request's doc; each can also have its own file if asked.
- **Don't re-read files read earlier in the session.** Cache in conversation state.
- **Don't use `v202404`.** Always `v202510` (outbound JSON, inbound EDI).
- **Don't write PM Summary / Ops Runbook from imagination.** Ground every bullet in a verified source (schema requirement, EBD path, regulatory deadline).
- **Don't skip the `bdew-docs/` regulation anchors for outbound Prüfis.** "I cited the file in Sources" is not enough — the doc must contain the extracted Vorlauffrist value and counter-party SLA. Wrong-by-default failure mode: assuming "1 Monat" when GPKE actually says "6 WT" for the LFW case.
- **Don't trust the `PI_*.yml` schema enums alone.** They inherit generic enums (e.g. `kategorie` with 40+ values when only `E02` is valid). The AHB JSON is authoritative for value-pool restrictions.
- **Don't omit `bo4e-mapping/<FV>/<message>.csv`.** It encodes BO4E↔EDI mappings (e.g. `energierichtung Z06/Z07`) that the schema doesn't expose. If the doc has no mapping-row citation, you skipped the layer.
- **Don't claim mapping support from a shared `RFF+Z13` list.** First prove whether the PI has a dedicated mapping column. If it does not, document the gap and let AHB carry requiredness.
- **Don't let fixtures define Minimal Payload.** Fixtures can seed examples only after AHB and mapping prove the fields.
- **Don't use numeric response derivation outside whitelisted families.** ORDERS/ORDRSP/IFTSTA relationships must come from process sources.
- **Don't collapse composite flows into one PI.** Use composite-flow mode and verify each primary PI separately.
- **Don't skip the trigger schema's required fields.** Test fixtures may omit fields the trigger schema declares required (e.g. `energierichtung`, `marktlokationsTyp.typ`). The Annotated Example must include them.
- **Don't ignore today's date.** Time-gated codes flip from "future" to "live" without anyone updating the docs. Run Step 3.5 every time.
- **Don't use a stale A99 sunset date from memory.** EBD JSON's `note` field is authoritative; re-check.
- **Don't skip run artifacts.** `verify-bo4e-essentials.py` is the deterministic feedback gate; a markdown-only run is not ticket-ready.
- **Don't make the LLM verify its own checklist.** Put coverage claims in `doc_coverage.json` and let Python check the final markdown mechanically.
