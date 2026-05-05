#!/usr/bin/env python3
"""Deterministic verification gate for BO4E Essentials runs.

This complements scripts/lint-essentials.sh. The shell linter checks the final
markdown shape; this verifier checks the run evidence the skill leaves behind.
It is intentionally stdlib-only so it can run in every local agent setup.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path.cwd().resolve()

REQUIRED_SECTIONS = [
    "Flow Summary",
    "Validation Notes",
    "Sources",
    "PM Summary",
    "Ops Runbook",
    "Ticket Breakdown",
]

SOURCE_LAYERS = [
    "regulation",
    "process",
    "architecture",
    "validation",
    "bo4e_schema",
    "bo4e_mapping",
    "trigger",
    "edifact",
    "examples",
    "webhook",
]

LAYER_ALIASES = {
    "schema": "bo4e_schema",
    "bo4e": "bo4e_schema",
    "mapping": "bo4e_mapping",
    "bo4e_edifact_mapping": "bo4e_mapping",
    "bo4e_mapping_csv": "bo4e_mapping",
    "ahb": "edifact",
    "edi": "edifact",
    "edifact_ahb": "edifact",
    "png": "architecture",
    "ebd": "validation",
    "conuti_webhook_json": "webhook",
    "webhook_examples": "webhook",
}

REQUIRED_CLAIM_LAYERS = {"process", "bo4e_schema", "bo4e_mapping", "edifact"}
OPTIONAL_CLAIM_LAYERS = {"regulation", "architecture", "validation", "examples", "trigger", "webhook"}

CLAIM_TYPE_HINTS = {
    "regulation": {
        "deadline",
        "time_gate",
        "legal_basis",
        "regulatory_framing",
        "market_rule",
    },
    "process": {
        "process_sequence",
        "role_direction",
        "ref_process",
        "follow_up",
        "trigger_context",
    },
    "architecture": {
        "swimlane",
        "format_transformation",
        "system_handoff",
        "aperak_workflow",
        "technical_flow",
    },
    "validation": {
        "ebd_tree",
        "antwortstatus",
        "rejection_code",
        "validation_step",
        "acceptance_code",
    },
    "bo4e_schema": {
        "payload_shape",
        "required_field",
        "field_type",
        "enum",
        "auto_generated_field",
    },
    "bo4e_mapping": {
        "bo4e_to_edifact",
        "edifact_to_bo4e",
        "field_mapping",
        "qualifier_mapping",
    },
    "trigger": {
        "event_name",
        "one_of",
        "all_of",
        "trigger_schema",
        "trigger_example",
    },
    "edifact": {
        "ahb_requiredness",
        "ahb_condition",
        "value_pool",
        "segment",
        "qualifier",
    },
    "examples": {
        "outbound_json",
        "inbound_edi",
        "scenario_fixture",
        "wire_example",
    },
    "webhook": {
        "webhook_payload",
        "response_payload",
        "correlation",
        "antwortstatus_shape",
    },
}

EXTRACTED_VALUE_HINTS = {
    "ahb_requiredness": {"required_inputs", "conditions", "segments", "fields"},
    "ahb_condition": {"conditions", "condition_ids"},
    "value_pool": {"value_pool_codes", "codes"},
    "segment": {"segments"},
    "qualifier": {"qualifiers"},
    "payload_shape": {"fields", "required_fields", "objects"},
    "required_field": {"required_fields", "fields"},
    "field_type": {"fields", "types"},
    "enum": {"enums", "values"},
    "auto_generated_field": {"auto_generated_fields", "fields"},
    "bo4e_to_edifact": {"mappings", "field_mappings"},
    "edifact_to_bo4e": {"mappings", "field_mappings"},
    "field_mapping": {"mappings", "field_mappings"},
    "qualifier_mapping": {"mappings", "qualifiers"},
    "ebd_tree": {"validation_steps", "terminal_codes", "antwortstatus_codes"},
    "antwortstatus": {"antwortstatus_codes", "terminal_codes"},
    "rejection_code": {"rejection_codes", "terminal_codes"},
    "validation_step": {"validation_steps"},
    "acceptance_code": {"acceptance_codes", "terminal_codes"},
    "process_sequence": {"process_steps", "messages"},
    "role_direction": {"directions", "roles"},
    "ref_process": {"ref_processes", "follow_ups"},
    "follow_up": {"follow_ups", "messages"},
    "trigger_context": {"triggers", "events"},
    "event_name": {"events", "triggers"},
    "one_of": {"request_formats", "schemas"},
    "all_of": {"request_formats", "schemas"},
    "trigger_schema": {"triggers", "fields"},
    "trigger_example": {"examples", "fields"},
    "deadline": {"deadlines", "rules"},
    "time_gate": {"time_gates", "rules"},
    "legal_basis": {"legal_references", "rules"},
    "regulatory_framing": {"rules", "business_context"},
    "market_rule": {"rules"},
    "swimlane": {"swimlanes", "systems"},
    "format_transformation": {"transformations", "systems"},
    "system_handoff": {"handoffs", "systems"},
    "aperak_workflow": {"aperak_steps", "decisions"},
    "technical_flow": {"technical_steps", "systems"},
    "outbound_json": {"examples", "fields"},
    "inbound_edi": {"examples", "segments"},
    "scenario_fixture": {"scenarios", "examples"},
    "wire_example": {"examples", "fields", "segments"},
    "webhook_payload": {"fields", "payloads"},
    "response_payload": {"fields", "payloads"},
    "correlation": {"correlation_keys", "fields"},
    "antwortstatus_shape": {"antwortstatus_codes", "fields"},
}

KNOWN_RESPONSE_PATTERNS = {
    "55001": {"success_responses": ["55002"], "rejection_responses": ["55003"]},
    "55004": {
        "success_responses": ["55005"],
        "rejection_responses": ["55006"],
        "follow_ups": ["55037"],
    },
    "55007": {"success_responses": ["55008"], "rejection_responses": ["55009"]},
    "55077": {"success_responses": ["55078"], "rejection_responses": ["55080"]},
    "55600": {"success_responses": ["55602"], "rejection_responses": ["55604"]},
    "55601": {"success_responses": ["55603"], "rejection_responses": ["55605"]},
}

ALLOWED_FIELD_AUTHORITIES = {"AHB", "Mapping", "Schema", "Process", "Fixture", "Inference"}
POSITIVE_RESPONSE_TERMS = {
    "bestätigung",
    "bestaetigung",
    "zustimmung",
    "zustimmen",
    "positiv",
    "pos.",
    "angenommen",
    "akzeptiert",
}
NEGATIVE_RESPONSE_TERMS = {
    "ablehnung",
    "ablehnen",
    "negativ",
    "neg.",
    "abgelehnt",
    "rejection",
}


class Reporter:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.passes = 0

    def pass_(self, message: str) -> None:
        self.passes += 1
        print(f"PASS: {message}")

    def warn(self, message: str) -> None:
        self.warnings.append(message)
        print(f"WARN: {message}")

    def fail(self, message: str) -> None:
        self.failures.append(message)
        print(f"FAIL: {message}")


def load_json(path: Path, reporter: Reporter, required: bool = True) -> Any | None:
    if not path.exists():
        if required:
            reporter.fail(f"required artifact missing: {rel(path)}")
        return None
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        reporter.fail(f"{rel(path)} is not valid JSON: {exc}")
        return None


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def normalize_layer(name: str) -> str:
    key = name.strip().lower().replace("-", "_").replace(" ", "_")
    return LAYER_ALIASES.get(key, key)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def artifact_pi(data: Any) -> str | None:
    if not isinstance(data, dict):
        return None
    value = data.get("pi") or data.get("pruefidentifikator")
    return str(value) if value is not None else None


def collect_source_entries(manifest: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    raw_layers = manifest.get("layers", manifest.get("sources", {}))
    if not isinstance(raw_layers, dict):
        return {}

    layers: dict[str, list[dict[str, Any]]] = {name: [] for name in SOURCE_LAYERS}
    for raw_name, raw_entries in raw_layers.items():
        layer = normalize_layer(str(raw_name))
        if layer not in layers:
            layers[layer] = []
        for entry in as_list(raw_entries):
            if isinstance(entry, str):
                layers[layer].append({"path": entry})
            elif isinstance(entry, dict):
                if "paths" in entry and "path" not in entry:
                    for path in as_list(entry.get("paths")):
                        layers[layer].append({**entry, "path": path})
                else:
                    layers[layer].append(entry)
            else:
                layers[layer].append({"value": entry})
    return layers


def entry_path(entry: dict[str, Any]) -> str | None:
    value = entry.get("path") or entry.get("file")
    if value is None:
        return None
    return str(value)


def entry_is_missing(entry: dict[str, Any]) -> bool:
    status = str(entry.get("status", "")).lower()
    reason = str(entry.get("reason", entry.get("note", ""))).lower()
    path = entry_path(entry)
    return (
        status in {"missing", "none", "not_found", "not-applicable", "not_applicable", "n/a"}
        or path is None
        or path.strip().lower() in {"", "none", "none found", "no png for this pi", "inbound-only"}
        or "none found" in reason
        or "no " in reason and " for this pi" in reason
    )


def concrete_paths(entries: list[dict[str, Any]]) -> list[str]:
    paths: list[str] = []
    for entry in entries:
        path = entry_path(entry)
        if path and not entry_is_missing(entry):
            paths.append(path)
    return paths


def concrete_manifest_paths(layers: dict[str, list[dict[str, Any]]]) -> dict[str, set[str]]:
    return {layer: set(concrete_paths(entries)) for layer, entries in layers.items()}


def repo_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


def load_ahb_index() -> dict[str, dict[str, Any]]:
    index_path = ROOT / "ahb-tables" / "INDEX.json"
    if not index_path.exists():
        return {}
    data = json.loads(index_path.read_text(encoding="utf-8"))
    by_version = data.get("by_version", {})
    latest = "FV2604" if "FV2604" in by_version else (data.get("versions") or [""])[-1]
    rows = by_version.get(latest, [])
    return {str(row.get("pruefidentifikator")): row for row in rows}


def find_section(text: str, title: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(title)}\b(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body") if match else ""


def flatten_related(related: dict[str, Any]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for key, value in related.items():
        if key in {"pi", "pruefidentifikator", "notes"}:
            continue
        values: list[str] = []
        for item in as_list(value):
            if isinstance(item, dict):
                pi = item.get("pi") or item.get("pruefidentifikator")
            else:
                pi = item
            if pi is not None:
                values.append(str(pi))
        result[key] = values
    return result


def coverage_ids(data: dict[str, Any], key: str) -> list[str]:
    values: list[str] = []
    for item in as_list(data.get(key)):
        if isinstance(item, dict):
            value = item.get("id") or item.get("code") or item.get("value")
        else:
            value = item
        if value is not None:
            values.append(str(value))
    return values


def claim_path(claim: dict[str, Any]) -> str | None:
    for key in ("path", "source_path", "file"):
        if claim.get(key):
            return str(claim[key])
    sources = claim.get("sources")
    if isinstance(sources, list) and sources:
        first = sources[0]
        if isinstance(first, str):
            return first
        if isinstance(first, dict):
            return entry_path(first)
    return None


def value_is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def validate_tool_trace(
    path: Path,
    manifest: dict[str, Any] | None,
    reporter: Reporter,
) -> None:
    if not path.exists():
        reporter.fail(f"tool trace missing: {rel(path)}")
        return

    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        reporter.fail(f"tool trace is empty: {rel(path)}")
        return

    touched_paths: set[str] = set()
    produced_outputs = 0
    for number, line in enumerate(lines, start=1):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as exc:
            reporter.fail(f"{rel(path)} line {number} is not valid JSON: {exc}")
            return

        for field in ("ts", "tool", "purpose"):
            if not entry.get(field):
                reporter.fail(f"{rel(path)} line {number} missing field '{field}'")
                return

        files = as_list(entry.get("files_read") or entry.get("files") or entry.get("paths"))
        outputs = as_list(entry.get("produces") or entry.get("outputs") or entry.get("extraction_ids"))
        if not files and not outputs:
            reporter.fail(f"{rel(path)} line {number} must include files_read and/or produces")
            return
        for file_path in files:
            if file_path:
                touched_paths.add(str(file_path))
        if outputs:
            produced_outputs += len(outputs)

    if manifest:
        manifest_layers = collect_source_entries(manifest)
        for layer, paths in concrete_manifest_paths(manifest_layers).items():
            for source_path in paths:
                if source_path not in touched_paths:
                    reporter.fail(f"source in manifest was not recorded in tool_trace.jsonl: {source_path}")

    if produced_outputs:
        reporter.pass_(f"tool trace valid with {len(lines)} entries and {produced_outputs} produced extraction reference(s)")
    else:
        reporter.warn("tool trace has no produced extraction references; claims must still carry extracted_values")


def validate_event_log(path: Path, reporter: Reporter) -> None:
    if not path.exists():
        reporter.fail(f"event log missing: {rel(path)}")
        return
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        reporter.fail(f"event log is empty: {rel(path)}")
        return
    for number, line in enumerate(lines, start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            reporter.fail(f"{rel(path)} line {number} is not valid JSON: {exc}")
            return
        for field in ("ts", "step", "event"):
            if field not in event:
                reporter.fail(f"{rel(path)} line {number} missing field '{field}'")
                return
    reporter.pass_(f"event log valid with {len(lines)} entries")


def validate_classification(
    pi: str, classification: dict[str, Any], ahb_rows: dict[str, dict[str, Any]], reporter: Reporter
) -> None:
    if artifact_pi(classification) != pi:
        reporter.fail("classification.json PI does not match requested PI")
    else:
        reporter.pass_("classification PI matches")

    for field in ("description", "direction", "fv"):
        if classification.get(field):
            reporter.pass_(f"classification contains {field}")
        else:
            reporter.fail(f"classification missing {field}")

    fv = str(classification.get("fv", ""))
    if fv != "FV2604":
        reporter.warn(f"classification uses {fv or 'no FV'}; FV2604 is preferred when present")

    if pi in ahb_rows:
        row = ahb_rows[pi]
        description = str(classification.get("description", "")).lower()
        expected = str(row.get("description", "")).lower()
        if expected and expected not in description and description not in expected:
            reporter.warn("classification description differs from ahb-tables/INDEX.json")
        else:
            reporter.pass_("classification aligns with AHB index")
    else:
        reporter.warn(f"PI {pi} not found in latest AHB index")


def validate_related(
    pi: str,
    related: dict[str, Any],
    ahb_rows: dict[str, dict[str, Any]],
    doc_text: str,
    final_stage: bool,
    reporter: Reporter,
) -> None:
    if artifact_pi(related) != pi:
        reporter.fail("related_pis.json PI does not match requested PI")
    else:
        reporter.pass_("related PI artifact matches")

    flattened = flatten_related(related)
    for category, expected in KNOWN_RESPONSE_PATTERNS.get(pi, {}).items():
        actual = set(flattened.get(category, []))
        for expected_pi in expected:
            if expected_pi in actual:
                reporter.pass_(f"related {category} includes {expected_pi}")
            else:
                reporter.fail(f"related {category} missing expected PI {expected_pi}")

    all_related = sorted({value for values in flattened.values() for value in values})
    if not all_related:
        reporter.warn("related_pis.json has no related Prüfis")
    for related_pi in all_related:
        if related_pi not in ahb_rows:
            reporter.warn(f"related PI {related_pi} not found in latest AHB index")
        if final_stage and related_pi not in doc_text:
            reporter.fail(f"related PI {related_pi} is missing from final markdown")
    if all_related:
        if final_stage:
            reporter.pass_(f"final markdown mentions {len(all_related)} related Prüfi references")
        else:
            reporter.pass_(f"related_pis contains {len(all_related)} related Prüfi references")


def validate_manifest(pi: str, manifest: dict[str, Any], doc_text: str, final_stage: bool, reporter: Reporter) -> None:
    if artifact_pi(manifest) not in {None, pi}:
        reporter.fail("sources_manifest.json PI does not match requested PI")

    layers = collect_source_entries(manifest)
    sources_section = find_section(doc_text, "Sources")
    if not layers:
        reporter.fail("sources_manifest.json has no layers object")
        return

    for layer in SOURCE_LAYERS:
        entries = layers.get(layer, [])
        paths = concrete_paths(entries)
        has_missing_entry = any(entry_is_missing(entry) for entry in entries)
        if paths:
            reporter.pass_(f"{layer} layer has {len(paths)} source path(s)")
        elif layer in {"architecture", "validation", "regulation", "process", "examples", "webhook", "trigger"} and has_missing_entry:
            reporter.warn(f"{layer} layer is explicitly marked missing/not applicable")
        elif layer in {"bo4e_schema", "bo4e_mapping", "edifact"}:
            reporter.fail(f"{layer} layer has no concrete source path")
        else:
            reporter.fail(f"{layer} layer has no source path or explicit gap")

    if not concrete_paths(layers.get("bo4e_schema", [])):
        reporter.fail("hard gate missing: BO4E schema")
    if not concrete_paths(layers.get("bo4e_mapping", [])):
        reporter.fail("hard gate missing: BO4E mapping")
    if not concrete_paths(layers.get("edifact", [])):
        reporter.fail("hard gate missing: AHB/EDIFACT")
    if not (concrete_paths(layers.get("trigger", [])) or concrete_paths(layers.get("webhook", []))):
        reporter.fail("hard gate missing: trigger schema or webhook example")
    else:
        reporter.pass_("hard gate present: trigger schema or webhook example")

    for layer, entries in layers.items():
        for path in concrete_paths(entries):
            if path.startswith(("http://", "https://")):
                continue
            full_path = repo_path(path)
            if full_path.exists():
                reporter.pass_(f"source exists: {path}")
            else:
                reporter.fail(f"source path does not exist: {path}")
            if final_stage and layer in {
                "bo4e_schema",
                "bo4e_mapping",
                "edifact",
                "trigger",
                "webhook",
                "validation",
                "process",
                "regulation",
                "examples",
                "architecture",
            }:
                if path in sources_section:
                    reporter.pass_(f"source cited in Sources: {path}")
                elif path in doc_text:
                    reporter.fail(f"source path is used but not cited in ## Sources: {path}")
                else:
                    reporter.fail(f"source path from {layer} manifest is not cited in final markdown: {path}")


def validate_doc(target: str, primary_pi: str, path: Path, text: str, reporter: Reporter) -> None:
    if re.search(rf"^#\s+.*{re.escape(target)}", text, re.MULTILINE):
        reporter.pass_("H1 mentions verification target")
    elif re.search(rf"^#\s+.*{re.escape(primary_pi)}", text, re.MULTILINE):
        reporter.pass_("H1 mentions primary PI")
    else:
        reporter.fail("H1 does not mention verification target or primary PI")

    for section in REQUIRED_SECTIONS:
        if re.search(rf"^##\s+{re.escape(section)}\b", text, re.MULTILINE):
            reporter.pass_(f"section present: {section}")
        else:
            reporter.fail(f"section missing: {section}")

    if "```mermaid" in text:
        reporter.pass_("Mermaid block present")
    else:
        reporter.fail("Mermaid block missing")

    if "v202404" in text:
        reporter.fail("forbidden test fixture version v202404 found")
    else:
        reporter.pass_("no forbidden v202404 reference")

    sources = find_section(text, "Sources")
    if "PROCESS_GRAPH.json" in sources:
        reporter.fail("PROCESS_GRAPH.json is cited in Sources; cite source files instead")
    else:
        reporter.pass_("PROCESS_GRAPH.json not cited in Sources")

    if re.search(r"ahb-tables/FV\d+/AHB_FV\d+_\d+\.json", text):
        reporter.pass_("AHB source path present in markdown")
    else:
        reporter.fail("missing AHB source path in markdown")

    if re.search(r"(PI_\d+\.yml|yaml_output/\d+\.yaml)", text):
        reporter.pass_("schema source path present in markdown")
    else:
        reporter.fail("missing schema source path in markdown")

    has_payload = bool(
        re.search(r"^##\s+Minimal (Valid )?Payload", text, re.MULTILINE)
        or re.search(r"^##\s+Annotated Example", text, re.MULTILINE)
    )
    if has_payload:
        if re.search(r"^##\s+AHB / Mapping Recheck\b", text, re.MULTILINE):
            reporter.pass_("AHB / Mapping Recheck section present for payload doc")
        else:
            reporter.fail("payload doc missing AHB / Mapping Recheck section")
        if any(authority in text for authority in ALLOWED_FIELD_AUTHORITIES):
            reporter.pass_("field authority vocabulary present")
        else:
            reporter.fail("payload doc missing field authority tags")


def _contains_any(text: str, terms: set[str]) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in terms)


def _response_expectations(related: dict[str, Any]) -> dict[str, str]:
    expectations: dict[str, str] = {}
    for pi in flatten_related({"success_responses": related.get("success_responses", [])}).get("success_responses", []):
        expectations[pi] = "success"
    for pi in flatten_related({"rejection_responses": related.get("rejection_responses", [])}).get("rejection_responses", []):
        expectations[pi] = "rejection"
    return expectations


def validate_response_polarity(
    related: dict[str, Any] | None,
    manifest: dict[str, Any] | None,
    ahb_rows: dict[str, dict[str, Any]],
    doc_text: str,
    final_stage: bool,
    reporter: Reporter,
) -> None:
    if not isinstance(related, dict):
        return

    expectations = _response_expectations(related)
    if not expectations:
        return

    authoritative_conflicts: list[str] = []
    for response_pi, expected in sorted(expectations.items()):
        description = str(ahb_rows.get(response_pi, {}).get("description", ""))
        if not description:
            reporter.warn(f"cannot verify response polarity for {response_pi}: not found in latest AHB index")
            continue
        if expected == "success":
            if _contains_any(description, NEGATIVE_RESPONSE_TERMS):
                authoritative_conflicts.append(f"{response_pi} is listed as success but AHB says '{description}'")
            else:
                reporter.pass_(f"AHB polarity agrees for success response {response_pi}")
            if not _contains_any(description, POSITIVE_RESPONSE_TERMS):
                reporter.warn(f"success response {response_pi} has no obvious positive term in AHB description: {description}")
        else:
            if _contains_any(description, POSITIVE_RESPONSE_TERMS):
                authoritative_conflicts.append(f"{response_pi} is listed as rejection but AHB says '{description}'")
            else:
                reporter.pass_(f"AHB polarity agrees for rejection response {response_pi}")
            if not _contains_any(description, NEGATIVE_RESPONSE_TERMS):
                reporter.warn(f"rejection response {response_pi} has no obvious negative term in AHB description: {description}")

    for conflict in authoritative_conflicts:
        reporter.fail(conflict)

    if not isinstance(manifest, dict):
        return

    layers = collect_source_entries(manifest)
    process_paths = concrete_paths(layers.get("process", []))
    if not process_paths:
        return

    process_conflicts: list[str] = []
    for source_path in process_paths:
        full_path = repo_path(source_path)
        if not full_path.exists() or full_path.suffix.lower() not in {".md", ".txt"}:
            continue
        lines = full_path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            for response_pi, expected in expectations.items():
                if f"PI_{response_pi}" not in line and not re.search(rf"title=.*\b{re.escape(response_pi)}\b", line):
                    continue
                context = " ".join(lines[max(0, index - 1) : index + 1]).strip()
                if expected == "success" and _contains_any(context, NEGATIVE_RESPONSE_TERMS):
                    process_conflicts.append(f"{source_path}:{index + 1}: {context}")
                if expected == "rejection" and _contains_any(context, POSITIVE_RESPONSE_TERMS):
                    process_conflicts.append(f"{source_path}:{index + 1}: {context}")

    if not process_conflicts:
        reporter.pass_("process docs do not contradict response polarity labels")
        return

    if final_stage:
        missing_documentation = [
            conflict
            for conflict in process_conflicts
            if conflict.split(":", 1)[0] not in doc_text
        ]
        has_discrepancy_section = re.search(
            r"documentation discrepancy|doc(?:umentation)? inconsistency|dokumentations.*(?:abweichung|inkonsistenz)",
            doc_text,
            re.IGNORECASE,
        )
        if has_discrepancy_section and not missing_documentation:
            reporter.pass_(f"documented {len(process_conflicts)} process response-polarity inconsistency/ies")
        else:
            if not has_discrepancy_section:
                reporter.fail("process docs contradict response polarity but final markdown lacks a documentation-discrepancy note")
            for conflict in missing_documentation:
                reporter.fail(f"undocumented process response-polarity inconsistency: {conflict}")
    else:
        reporter.warn("process docs contain response-polarity inconsistencies: " + "; ".join(process_conflicts))


def validate_response_polarity_coverage(
    related: dict[str, Any] | None,
    coverage: dict[str, Any] | None,
    reporter: Reporter,
) -> None:
    if not isinstance(related, dict) or not isinstance(coverage, dict):
        return
    expectations = _response_expectations(related)
    if not expectations:
        return

    checks = as_list(coverage.get("response_polarity_checks"))
    if not checks:
        reporter.fail("doc_coverage.json missing response_polarity_checks for paired response PIs")
        return

    by_pi: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(checks, start=1):
        if not isinstance(item, dict):
            reporter.fail(f"response_polarity_checks item {index} is not an object")
            continue
        pi_value = str(item.get("pi", ""))
        if not pi_value:
            reporter.fail(f"response_polarity_checks item {index} missing pi")
            continue
        by_pi[pi_value] = item
        if item.get("expected") not in {"success", "rejection"}:
            reporter.fail(f"response_polarity_checks item {index} has invalid expected value")
        for field in ("ahb_description", "schema_description", "process_label_findings"):
            if field not in item:
                reporter.fail(f"response_polarity_checks item {index} missing {field}")

    for pi_value, expected in sorted(expectations.items()):
        item = by_pi.get(pi_value)
        if not item:
            reporter.fail(f"response_polarity_checks missing response PI {pi_value}")
            continue
        if item.get("expected") != expected:
            reporter.fail(f"response_polarity_checks for {pi_value} expected {item.get('expected')}, should be {expected}")
    reporter.pass_(f"validated {len(by_pi)} response polarity coverage item(s)")


def validate_coverage(coverage: dict[str, Any], doc_text: str, reporter: Reporter) -> None:
    for key, label in [
        ("ahb_condition_ids", "AHB condition ID"),
        ("value_pool_codes", "value-pool code"),
        ("ebd_terminal_codes", "EBD terminal code"),
    ]:
        values = coverage_ids(coverage, key)
        if not values:
            reporter.warn(f"doc_coverage.json has no {key}")
            continue
        missing = [value for value in values if value not in doc_text]
        if missing:
            reporter.fail(f"final markdown missing {label}(s): {', '.join(missing)}")
        else:
            reporter.pass_(f"final markdown covers {len(values)} {label}(s)")

    condition_ids = sorted(set(re.findall(r"\[(UB\d+|\d{1,4})\]", doc_text)))
    weak: list[str] = []
    for condition_id in condition_ids:
        match = re.search(rf"\[{re.escape(condition_id)}\](.{{0,180}})", doc_text, re.DOTALL)
        if not match:
            continue
        tail = re.sub(r"[`*_#\[\]()+/.,:;=<>|-]", " ", match.group(1))
        words = re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", tail)
        if len(words) < 3:
            weak.append(condition_id)
    if weak:
        reporter.warn("condition IDs may lack nearby plain-English explanation: " + ", ".join(weak))
    elif condition_ids:
        reporter.pass_(f"{len(condition_ids)} condition IDs have nearby explanatory text")

    mapping_checks = as_list(coverage.get("mapping_column_checks"))
    has_payload = bool(
        re.search(r"^##\s+Minimal (Valid )?Payload", doc_text, re.MULTILINE)
        or re.search(r"^##\s+Annotated Example", doc_text, re.MULTILINE)
    )
    if has_payload:
        if not mapping_checks:
            reporter.fail("payload doc missing mapping_column_checks in doc_coverage.json")
        else:
            for index, item in enumerate(mapping_checks, start=1):
                if not isinstance(item, dict):
                    reporter.fail(f"mapping_column_checks item {index} is not an object")
                    continue
                for field in ("pi", "csv_path", "has_dedicated_column", "evidence"):
                    if field not in item:
                        reporter.fail(f"mapping_column_checks item {index} missing {field}")
                csv_path = item.get("csv_path")
                if isinstance(csv_path, str):
                    if repo_path(csv_path).exists():
                        reporter.pass_(f"mapping CSV exists for coverage check: {csv_path}")
                    else:
                        reporter.fail(f"mapping CSV in coverage check does not exist: {csv_path}")
                    if csv_path not in doc_text:
                        reporter.fail(f"mapping CSV from coverage check not cited in final markdown: {csv_path}")
                pi_value = str(item.get("pi", ""))
                if pi_value and pi_value not in doc_text:
                    reporter.fail(f"mapping_column_checks PI {pi_value} missing from final markdown")
                if item.get("has_dedicated_column") is False:
                    phrase = f"no dedicated {pi_value}"
                    if pi_value and phrase.lower() not in doc_text.lower():
                        reporter.fail(f"final markdown must state no dedicated mapping column for {pi_value}")
            reporter.pass_(f"validated {len(mapping_checks)} mapping column check(s)")

        field_authority = as_list(coverage.get("field_authority"))
        if not field_authority:
            reporter.fail("payload doc missing field_authority in doc_coverage.json")
        else:
            for index, item in enumerate(field_authority, start=1):
                if not isinstance(item, dict):
                    reporter.fail(f"field_authority item {index} is not an object")
                    continue
                field_name = str(item.get("field", ""))
                authority = str(item.get("authority", ""))
                source = str(item.get("source", ""))
                if not field_name:
                    reporter.fail(f"field_authority item {index} missing field")
                elif field_name not in doc_text:
                    reporter.fail(f"field_authority field not mentioned in final markdown: {field_name}")
                if authority not in ALLOWED_FIELD_AUTHORITIES:
                    reporter.fail(f"field_authority item {index} has invalid authority '{authority}'")
                elif authority not in doc_text:
                    reporter.fail(f"field_authority authority '{authority}' not visible in final markdown")
                if not source:
                    reporter.fail(f"field_authority item {index} missing source")
            reporter.pass_(f"validated {len(field_authority)} field authority item(s)")


def validate_layer_claims(
    claims_data: dict[str, Any],
    manifest: dict[str, Any] | None,
    doc_text: str,
    final_stage: bool,
    reporter: Reporter,
) -> None:
    if not isinstance(claims_data, dict):
        reporter.fail("layer_claims.json must be a JSON object")
        return

    raw_claims = claims_data.get("claims")
    if not isinstance(raw_claims, list):
        reporter.fail("layer_claims.json missing claims array")
        return

    manifest_layers = collect_source_entries(manifest or {})
    manifest_paths = concrete_manifest_paths(manifest_layers)
    claims_by_layer: dict[str, list[dict[str, Any]]] = {}

    for index, raw_claim in enumerate(raw_claims, start=1):
        if not isinstance(raw_claim, dict):
            reporter.fail(f"layer_claims.json claim {index} is not an object")
            continue

        layer = normalize_layer(str(raw_claim.get("layer", "")))
        if layer not in SOURCE_LAYERS:
            reporter.fail(f"layer_claims.json claim {index} has unknown layer '{raw_claim.get('layer')}'")
            continue
        claims_by_layer.setdefault(layer, []).append(raw_claim)

        ctype = str(raw_claim.get("claim_type", ""))
        if not ctype:
            reporter.fail(f"{layer} claim {index} missing claim_type")
        elif ctype not in CLAIM_TYPE_HINTS.get(layer, set()):
            reporter.warn(f"{layer} claim {index} uses non-standard claim_type '{ctype}'")

        text = str(raw_claim.get("claim", "")).strip()
        if len(text) < 12:
            reporter.fail(f"{layer} claim {index} has no useful claim text")

        evidence = raw_claim.get("evidence")
        if not evidence:
            reporter.fail(f"{layer} claim {index} missing evidence")

        path = claim_path(raw_claim)
        if not path:
            reporter.fail(f"{layer} claim {index} missing source path")
        else:
            if path not in manifest_paths.get(layer, set()):
                reporter.fail(f"{layer} claim {index} source path is not listed under the same layer in sources_manifest.json: {path}")
            if not path.startswith(("http://", "https://")) and not repo_path(path).exists():
                reporter.fail(f"{layer} claim {index} source path does not exist: {path}")

        extracted_values = raw_claim.get("extracted_values")
        if not isinstance(extracted_values, dict) or not extracted_values:
            reporter.fail(f"{layer} claim {index} missing structured extracted_values")
        else:
            non_empty_keys = {key for key, value in extracted_values.items() if value_is_non_empty(value)}
            if not non_empty_keys:
                reporter.fail(f"{layer} claim {index} extracted_values are empty")
            expected_keys = EXTRACTED_VALUE_HINTS.get(ctype, set())
            if expected_keys and not (non_empty_keys & expected_keys):
                reporter.warn(
                    f"{layer} claim {index} extracted_values do not use expected key(s) for {ctype}: "
                    + ", ".join(sorted(expected_keys))
                )

        doc_terms = [str(term) for term in as_list(raw_claim.get("doc_terms")) if term]
        if final_stage and doc_terms:
            missing_terms = [term for term in doc_terms if term not in doc_text]
            if missing_terms:
                reporter.fail(
                    f"{layer} claim {index} doc_terms missing from final markdown: {', '.join(missing_terms)}"
                )

    for layer in REQUIRED_CLAIM_LAYERS:
        if claims_by_layer.get(layer):
            reporter.pass_(f"layer_claims contains {layer} claim(s)")
        else:
            reporter.fail(f"layer_claims missing required {layer} claim")

    if claims_by_layer.get("trigger") or claims_by_layer.get("webhook"):
        reporter.pass_("layer_claims contains trigger or webhook claim(s)")
    else:
        reporter.fail("layer_claims missing trigger or webhook claim")

    for layer in OPTIONAL_CLAIM_LAYERS:
        if manifest_paths.get(layer) and not claims_by_layer.get(layer):
            reporter.warn(f"{layer} source exists but layer_claims has no {layer} claim")

    if claims_by_layer:
        reporter.pass_(f"validated {sum(len(v) for v in claims_by_layer.values())} source-layer claim(s)")

    if manifest:
        claimed_paths = {claim_path(claim) for claim in raw_claims if isinstance(claim, dict)}
        claimed_paths.discard(None)
        for layer, paths in manifest_paths.items():
            for source_path in paths:
                if source_path not in claimed_paths:
                    reporter.fail(f"source path has no extracted claim in layer_claims.json: {source_path}")


def main() -> int:
    global ROOT

    parser = argparse.ArgumentParser(description="Verify BO4E Essentials run evidence and markdown.")
    parser.add_argument("target", help="Prüfidentifikator or composite flow id, e.g. 55004 or START_VERSAND_ANF_STORNO")
    parser.add_argument(
        "--stage",
        choices=("sources", "final", "all"),
        default="all",
        help="sources = pre-write evidence gate; final/all = include markdown coverage checks",
    )
    parser.add_argument(
        "--doc",
        type=Path,
        help="Final markdown path. Defaults to your-requests/<PI>_BO4E_ESSENTIALS.md",
    )
    parser.add_argument(
        "--run-dir",
        type=Path,
        help="Run artifact directory. Defaults to your-requests/.runs/<PI>",
    )
    parser.add_argument(
        "--primary-pi",
        help="Primary request Prüfi for composite flow ids. Optional for numeric targets.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository/workspace root. Defaults to the current working directory.",
    )
    args = parser.parse_args()

    ROOT = args.repo_root.resolve()

    target = str(args.target)
    numeric_target = bool(re.fullmatch(r"\d+", target))
    doc_path = args.doc or ROOT / "your-requests" / f"{target}_BO4E_ESSENTIALS.md"
    run_dir = args.run_dir or ROOT / "your-requests" / ".runs" / target
    if not doc_path.is_absolute():
        doc_path = ROOT / doc_path
    if not run_dir.is_absolute():
        run_dir = ROOT / run_dir

    reporter = Reporter()
    final_stage = args.stage in {"final", "all"}
    classification = load_json(run_dir / "classification.json", reporter)
    pi = str(args.primary_pi or (target if numeric_target else artifact_pi(classification) or target))
    if not re.fullmatch(r"\d+", pi):
        reporter.fail("primary PI is required for composite flow verification; pass --primary-pi <NNNNN> or set classification.json pi")

    print(f"Verifying target {target}")
    print(f"primary_pi: {pi}")
    print(f"stage: {args.stage}")
    print(f"doc: {rel(doc_path)}")
    print(f"run_dir: {rel(run_dir)}")

    if final_stage:
        if not doc_path.exists():
            reporter.fail(f"final markdown missing: {rel(doc_path)}")
            doc_text = ""
        else:
            doc_text = doc_path.read_text(encoding="utf-8")
            validate_doc(target, pi, doc_path, doc_text, reporter)
    else:
        doc_text = ""

    related = load_json(run_dir / "related_pis.json", reporter)
    manifest = load_json(run_dir / "sources_manifest.json", reporter)
    claims = load_json(run_dir / "layer_claims.json", reporter)
    coverage = load_json(run_dir / "doc_coverage.json", reporter, required=final_stage)
    validate_event_log(run_dir / "events.jsonl", reporter)
    validate_tool_trace(run_dir / "tool_trace.jsonl", manifest if isinstance(manifest, dict) else None, reporter)

    ahb_rows = load_ahb_index()

    if isinstance(classification, dict):
        validate_classification(pi, classification, ahb_rows, reporter)
    if isinstance(related, dict):
        validate_related(pi, related, ahb_rows, doc_text, final_stage, reporter)
    if isinstance(manifest, dict):
        validate_manifest(pi, manifest, doc_text, final_stage, reporter)
    validate_response_polarity(
        related if isinstance(related, dict) else None,
        manifest if isinstance(manifest, dict) else None,
        ahb_rows,
        doc_text,
        final_stage,
        reporter,
    )
    validate_response_polarity_coverage(
        related if isinstance(related, dict) else None,
        coverage if isinstance(coverage, dict) else None,
        reporter,
    )
    if isinstance(claims, dict):
        validate_layer_claims(
            claims,
            manifest if isinstance(manifest, dict) else None,
            doc_text,
            final_stage,
            reporter,
        )
    if final_stage and isinstance(coverage, dict):
        validate_coverage(coverage, doc_text, reporter)

    print("---")
    print(f"passed: {reporter.passes}")
    print(f"warnings: {len(reporter.warnings)}")
    print(f"failures: {len(reporter.failures)}")

    if reporter.failures:
        print("VERIFY FAILED")
        return 1
    print("VERIFY OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
