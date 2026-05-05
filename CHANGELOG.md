# Changelog

## v0.2.0 - 2026-05-05

This release turns the workspace from a documentation bundle into a verifiable
MaCo investigation toolkit for BO4E implementation work.

### Added

- Parsed BDEW source documents in `bdew-docs/`, including GPKE, WiM, LFW24,
  APERAK, UTILMD/MSCONS/INVOIC/ORDERS MIGs, MSCONS AHB, and OBIS/media code
  lists.
- BO4E mapping CSVs in `bo4e-mapping/` for format versions `2510` and `2604`,
  covering EDIFACT message families such as UTILMD, MSCONS, ORDERS, INVOIC,
  APERAK, CONTRL, MaLoIdent, and related message types.
- AHB table JSONs under `ahb-tables/` for Pruefidentifikator-level mandatory
  fields, conditional rules, value pools, and EDIFACT evidence.
- The `bo4e-essentials` agent skill under `.agents/skills/bo4e-essentials/`.
  It produces ticket-ready BO4E Essentials docs for a Pruefidentifikator or
  composite `START_*` flow.
- Deterministic verification scripts bundled with the skill:
  - `scripts/verify-bo4e-essentials.py` checks source evidence artifacts,
    source manifests, extracted layer claims, related PIs, response polarity,
    mapping-column checks, and field-authority coverage.
  - `scripts/lint-essentials.sh` checks the final markdown structure, required
    sections, source citations, Mermaid diagrams, schema/AHB references, and
    payload trust sections such as `AHB / Mapping Recheck`.

### Investigation Model

The release standardizes the evidence chain for BO4E implementation questions:

1. Trigger starts the process.
2. Process docs show the flow.
3. GPKE says when the flow is allowed.
4. AHB says what is mandatory.
5. Schema says the JSON shape.
6. Mapping proves JSON-to-EDIFACT.

Fixtures remain examples only. They can confirm shape and wire examples, but
they do not establish requiredness, legal value pools, or production-safe
payload fields.

### Why It Matters

The BO4E Essentials workflow no longer relies on an LLM to self-police a long
checklist. The agent must leave structured run artifacts in
`your-requests/.runs/<PI>/`, and the bundled Python verifier checks those
artifacts before the final markdown is accepted. The shell linter then checks
that the final doc exposes the required source-backed sections.

A BO4E Essentials doc is ticket-ready only when both deterministic gates pass.
