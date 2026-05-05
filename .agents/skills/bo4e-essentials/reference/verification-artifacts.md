# Verification artifacts

The BO4E Essentials workflow writes machine-checkable artifacts before the final
markdown is accepted. Store them under:

`your-requests/.runs/<PI>/`

These files are small, structured handoffs from the agent to the deterministic
verifier. They make the run debuggable and keep the main `SKILL.md` from growing
into an overloaded rules file.

## Required files

### `events.jsonl`

Append one JSON object per meaningful step. Required fields:

```json
{"ts":"2026-04-24T21:30:00Z","step":"classification","event":"read_ahb_index","files":["ahb-tables/INDEX.md"]}
```

Use ISO timestamps. Keep event text short. Include `files`, `derived`, `gaps`,
or `decision` fields when useful.

### `tool_trace.jsonl`

Append one JSON object per source-discovery or source-reading tool call. This is
for reproducibility, not for quality scoring.

```json
{
  "ts": "2026-04-24T21:31:00Z",
  "tool": "exec_command",
  "purpose": "read AHB table for requiredness and value pools",
  "command": "python3 - <<'PY' ...",
  "files_read": ["ahb-tables/FV2604/AHB_FV2604_55004.json"],
  "produces": ["claim:edifact:ahb_requiredness:55004"]
}
```

Rules:

- Every concrete source path in `sources_manifest.json` must appear in
  `tool_trace.jsonl`.
- A trace entry should include `produces` when it feeds a claim. The verifier
  does not accept tool use alone as proof of quality; `layer_claims.json` must
  contain the extracted values.

### `classification.json`

```json
{
  "pi": "55004",
  "description": "Lieferende / Abmeldung",
  "direction": "LF → NB",
  "fv": "FV2604",
  "versionsnummer": "2.1",
  "veroeffentlichungsdatum": "2025-12-11"
}
```

### `related_pis.json`

```json
{
  "pi": "55004",
  "request_formats": ["55004"],
  "success_responses": ["55005"],
  "rejection_responses": ["55006"],
  "sibling_requests": [],
  "follow_ups": ["55037"],
  "trigger_proofs": [],
  "notes": ["55037 is a follow-up after 55005, not the direct success response."]
}
```

Use arrays of strings. If a category is empty, write `[]` rather than omitting it.
For paired response PIs, `success_responses` and `rejection_responses` must match
AHB/schema polarity. If process docs use conflicting labels such as `pos/neg`,
`Bestätigung`, or `Ablehnung`, keep the AHB/schema classification and document
the discrepancy in the final markdown.

### `sources_manifest.json`

```json
{
  "pi": "55004",
  "layers": {
    "regulation": [
      {"path": "bdew-docs/bk620160_gpke.md", "purpose": "deadlines"}
    ],
    "process": [
      {"path": "docs-offline/lieferende-nb-lf-rolle-lf-3129676f0.md", "purpose": "role flow"}
    ],
    "architecture": [
      {"status": "missing", "reason": "no PI-specific PNG found"}
    ],
    "validation": [
      {"path": "ebd-diagrams/FV2604/E_0607.json", "purpose": "antwortstatus codes"}
    ],
    "bo4e_schema": [
      {"path": "maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55004.yml"},
      {"path": "maco-api-documentation/pythons/createPiFromTemplater/templater/yaml_output/55004.yaml"}
    ],
    "bo4e_mapping": [
      {"path": "bo4e-mapping/2604/UTILMD_Strom.csv", "purpose": "BO4E field to EDIFACT segment mapping"}
    ],
    "trigger": [
      {"path": "maco-api-documentation/macoapp-trigger/components/schemas/START_LIEFERENDE.yml"}
    ],
    "edifact": [
      {"path": "ahb-tables/FV2604/AHB_FV2604_55004.json"}
    ],
    "examples": [
      {"path": "maco-edi-testfiles/outbound/v202510/utilmd/55004/1.json"}
    ],
    "webhook": [
      {"path": "maco-api-documentation/macoapp-schreiben/components/examples/Strom/55005_eingehend_Testfall1.yaml"}
    ]
  },
  "gaps": [
    {"layer": "architecture", "reason": "no PI-specific PNG found"}
  ]
}
```

Rules:

- Use repo-relative paths.
- Every concrete path must exist.
- Every concrete path must be cited in the final markdown's `## Sources`
  section. Inline mentions elsewhere are useful context, but they do not satisfy
  the source-audit gate.
- For missing optional layers, add an explicit `status: "missing"` entry plus a
  reason. A silent missing layer fails verification because it proves the layer
  was not checked.
- Schema + BO4E mapping + AHB + either trigger or webhook are hard gates. Do not
  write the final doc if any hard gate is missing.

### `layer_claims.json`

This is the key intermediate-check artifact. Each claim says what a source layer
contributed to the unified process picture. The verifier checks that claims point
to files in `sources_manifest.json`, that those files exist, and, during the
final stage, that important `doc_terms` appear in the markdown.

```json
{
  "pi": "55004",
  "claims": [
    {
      "layer": "edifact",
      "claim_type": "ahb_requiredness",
      "path": "ahb-tables/FV2604/AHB_FV2604_55004.json",
      "evidence": "DTM+93 is Muss [11] unless STS+7 uses ZG9/ZH1/ZH2.",
      "claim": "The AHB is authoritative for EDIFACT segment requiredness and conditional rules.",
      "extracted_values": {
        "required_inputs": ["DTM+93"],
        "conditions": ["[11]"],
        "value_pool_codes": ["ZG9", "ZH1", "ZH2"]
      },
      "doc_terms": ["DTM+93", "[11]", "ZG9", "ZH1", "ZH2"]
    },
    {
      "layer": "bo4e_schema",
      "claim_type": "payload_shape",
      "path": "maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55004.yml",
      "evidence": "PI_55004.yml defines transaktionsdaten and stammdaten payload properties.",
      "claim": "The BO4E schema defines the JSON payload shape sent to Conuti.",
      "extracted_values": {
        "objects": ["transaktionsdaten", "stammdaten"],
        "fields": ["vertragsende", "vertragsbeginn", "transaktionsgrund"]
      },
      "doc_terms": ["transaktionsdaten", "stammdaten"]
    },
    {
      "layer": "bo4e_mapping",
      "claim_type": "bo4e_to_edifact",
      "path": "bo4e-mapping/2604/UTILMD_Strom.csv",
      "evidence": "Mapping rows connect BO4E field paths to EDIFACT segments and qualifiers for PI 55004.",
      "claim": "The mapping CSV is the authoritative bridge between BO4E fields and EDIFACT segments.",
      "extracted_values": {
        "mappings": [
          {"bo4e_path": "transaktionsdaten.vertragsende", "edifact": "SG4.IDE+24.DTM+93"}
        ]
      },
      "doc_terms": ["BO4E", "EDIFACT"]
    },
    {
      "layer": "validation",
      "claim_type": "antwortstatus",
      "path": "ebd-diagrams/FV2604/E_0607.json",
      "evidence": "Terminal EBD rows emit A01/A02/.../A11/A27/A99 Antwortstatus codes.",
      "claim": "The EBD tree explains the NB-side validation path and terminal response codes.",
      "extracted_values": {
        "terminal_codes": ["A01", "A02", "A11", "A27", "A99"],
        "validation_steps": ["Vorlauffrist eingehalten?", "Zuordnung vorhanden?"]
      },
      "doc_terms": ["E_0607", "A11", "A27"]
    }
  ]
}
```

Required layers with at least one claim:

- `process`
- `bo4e_schema`
- `bo4e_mapping`
- `edifact`
- one of `trigger` or `webhook`

Optional layers become expected when a concrete source exists in
`sources_manifest.json`: `regulation`, `architecture`, `validation`,
`examples`, `trigger`, `webhook`.

Every concrete source path in `sources_manifest.json` must have at least one
claim. This prevents source-touching without extraction.

Use these claim types so the verifier can catch wrong layer usage:

| Layer | Claim types |
|---|---|
| `regulation` | `deadline`, `time_gate`, `legal_basis`, `regulatory_framing`, `market_rule` |
| `process` | `process_sequence`, `role_direction`, `ref_process`, `follow_up`, `trigger_context` |
| `architecture` | `swimlane`, `format_transformation`, `system_handoff`, `aperak_workflow`, `technical_flow` |
| `validation` | `ebd_tree`, `antwortstatus`, `rejection_code`, `validation_step`, `acceptance_code` |
| `bo4e_schema` | `payload_shape`, `required_field`, `field_type`, `enum`, `auto_generated_field` |
| `bo4e_mapping` | `bo4e_to_edifact`, `edifact_to_bo4e`, `field_mapping`, `qualifier_mapping` |
| `trigger` | `event_name`, `one_of`, `all_of`, `trigger_schema`, `trigger_example` |
| `edifact` | `ahb_requiredness`, `ahb_condition`, `value_pool`, `segment`, `qualifier` |
| `examples` | `outbound_json`, `inbound_edi`, `scenario_fixture`, `wire_example` |
| `webhook` | `webhook_payload`, `response_payload`, `correlation`, `antwortstatus_shape` |

### `doc_coverage.json`

```json
{
  "pi": "55004",
  "ahb_condition_ids": ["11", "313", "577", "UB1"],
  "value_pool_codes": ["ZT5", "Z33", "ZG9", "ZH1", "ZH2"],
  "ebd_terminal_codes": ["A01", "A02", "A11", "A27", "A99"],
  "mapping_column_checks": [
    {
      "pi": "55004",
      "csv_path": "bo4e-mapping/2604/UTILMD_Strom.csv",
      "has_dedicated_column": true,
      "evidence": "Header contains 55004; extracted rows map vertragsende and transaktionsgrund."
    }
  ],
  "field_authority": [
    {
      "field": "transaktionsdaten.transaktionsgrund",
      "authority": "AHB",
      "source": "ahb-tables/FV2604/AHB_FV2604_55004.json"
    },
    {
      "field": "stammdaten.MARKTLOKATION[].marktlokationsId",
      "authority": "Mapping",
      "source": "bo4e-mapping/2604/UTILMD_Strom.csv"
    }
  ],
  "response_polarity_checks": [
    {
      "pi": "55005",
      "expected": "success",
      "ahb_description": "Bestätigung Abmeldung",
      "schema_description": "55005 - ... - Bestätigung Abmeldung",
      "process_label_findings": []
    },
    {
      "pi": "55006",
      "expected": "rejection",
      "ahb_description": "Ablehnung Abmeldung",
      "schema_description": "55006 - ... - Ablehnung Abmeldung",
      "process_label_findings": []
    }
  ]
}
```

This file lists the coverage the final markdown must visibly contain. It does
not need to contain every raw AHB row. Include the IDs and codes that matter for
the documented PI and variants.

`mapping_column_checks` is required for every outbound/request PI with a payload.
It records whether the mapping CSV has a dedicated PI header column. Shared
`RFF+Z13` rows are not enough to mark `has_dedicated_column=true`.

`field_authority` is required for every field included in Minimal Payload or an
Annotated Example. Allowed authority values:

- `AHB` — requiredness/value pool comes from AHB JSON.
- `Mapping` — BO4E path is proven in the mapping CSV for this PI.
- `Schema` — field exists because the trigger or PI schema requires it.
- `Process` — field exists because process docs/processinfo require the step.
- `Fixture` — field appears in a test fixture only; must not be presented as required.
- `Inference` — agent-derived; must be accompanied by a risk note in the doc.

`response_polarity_checks` is required when a doc has paired success/rejection
PIs. Include process label conflicts as findings. The final verifier fails if a
process source contradicts AHB/schema polarity and the final markdown does not
cite that source in a documentation-discrepancy note.

## Verification command

Run before writing the markdown:

```bash
SKILL_DIR="${SKILL_DIR:-.agents/skills/bo4e-essentials}"
python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage sources <PI>
```

For a composite trigger flow, use the flow id as the target and supply the
primary request PI:

```bash
SKILL_DIR="${SKILL_DIR:-.agents/skills/bo4e-essentials}"
python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage sources <FLOW_NAME> --primary-pi <PI>
```

Run after writing the markdown:

```bash
SKILL_DIR="${SKILL_DIR:-.agents/skills/bo4e-essentials}"
python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage final <PI>
"$SKILL_DIR/scripts/lint-essentials.sh" --repo-root "$PWD" <PI>
```

Composite final verification:

```bash
SKILL_DIR="${SKILL_DIR:-.agents/skills/bo4e-essentials}"
python3 "$SKILL_DIR/scripts/verify-bo4e-essentials.py" --repo-root "$PWD" --stage final <FLOW_NAME> --primary-pi <PI> --doc your-requests/<FLOW_NAME>_BO4E_ESSENTIALS.md
"$SKILL_DIR/scripts/lint-essentials.sh" --repo-root "$PWD" your-requests/<FLOW_NAME>_BO4E_ESSENTIALS.md
```

Both commands must exit `0`. Fix artifacts or markdown when verification fails.
Do not loosen the verifier to pass a weak document.
