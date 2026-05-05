#!/usr/bin/env bash
# lint-essentials.sh — verify a BO4E essentials doc has the mandatory sections.
# Tool-agnostic: pure bash + grep. Runs anywhere.
#
# Usage:
#   scripts/lint-essentials.sh NNNNN                       # lint your-requests/NNNNN_BO4E_ESSENTIALS.md
#   scripts/lint-essentials.sh path/to/file.md             # lint an explicit file
#   scripts/lint-essentials.sh --repo-root /repo NNNNN      # lint from a specific workspace root
#
# Exit code: 0 = pass, 1 = fail (missing required content).

set -euo pipefail

repo_root="$PWD"
if [[ "${1:-}" == "--repo-root" ]]; then
  repo_root="${2:?usage: lint-essentials.sh [--repo-root <path>] <PI-number-or-path>}"
  shift 2
fi

arg="${1:?usage: lint-essentials.sh [--repo-root <path>] <PI-number-or-path>}"
cd "$repo_root"

if [[ -f "$arg" ]]; then
  f="$arg"
  pi="$(basename "$f" | grep -oE '^[0-9]+' || echo "")"
else
  pi="$arg"
  f="your-requests/${pi}_BO4E_ESSENTIALS.md"
fi

[[ -f "$f" ]] || { echo "FAIL: $f not found"; exit 1; }

fail=0
pass_count=0

check() {
  local label="$1"
  local pattern="$2"
  local mode="${3:-regex}"  # regex | fixed
  local found
  if [[ "$mode" == "fixed" ]]; then
    grep -qF -- "$pattern" "$f" && found=1 || found=0
  else
    grep -qE -- "$pattern" "$f" && found=1 || found=0
  fi
  if (( found )); then
    pass_count=$((pass_count+1))
  else
    echo "MISSING: $label  (looked for: $pattern)"
    fail=1
  fi
}

# --- Required sections (applies to every essentials doc) ---
check "H1 title mentioning PI" "^#[[:space:]].*${pi:-[0-9]+}" regex
check "Flow Summary section"   "^##[[:space:]]+Flow Summary"
check "Validation Notes"       "^##[[:space:]]+Validation Notes"
check "Sources"                "^##[[:space:]]+Sources"
check "Ticket Breakdown"       "^##[[:space:]]+Ticket Breakdown"

# --- Cursor PM/Ops layer (per pm-ops-summary-mandatory-always.mdc) ---
check "PM Summary"             "^##[[:space:]]+PM Summary"
check "Ops Runbook"            "^##[[:space:]]+Ops Runbook"

# --- Visualization (per process-visualization-mandatory-always.mdc) ---
check "Mermaid diagram"        '```mermaid' fixed

# --- Anti-hallucination (per anti-hallucination-mandatory-always.mdc) ---
# At least one concrete source path in "Sources" — look for known roots
check "Source: AHB table"      "ahb-tables/FV[0-9]+/AHB_FV[0-9]+_[0-9]+\.json"
check "Source: schema (PI_xxx.yml) OR yaml_output" "(PI_[0-9]+\.yml|yaml_output/[0-9]+\.yaml)"

# --- Never-use: v202404 ---
if grep -qE "v202404" "$f"; then
  echo "FORBIDDEN: references v202404 (must use v202510 per maco-workspace-context rule)"
  fail=1
fi

# --- Warn (not fail) ---
warn_count=0
warn() { echo "WARN: $1"; warn_count=$((warn_count+1)); }

grep -qE "^##[[:space:]]+Minimal (Valid )?Payload" "$f" || warn "no Minimal Payload section (expected for outbound PIs)"
grep -qE "^##[[:space:]]+(Annotated Example|Variants)" "$f" || warn "no Annotated Example or Variants section"
grep -qE "antwortstatus|E_0[0-9]+" "$f" || warn "no antwortstatus / EBD code reference (expected when documenting response PIs)"

if grep -qE "^##[[:space:]]+Minimal (Valid )?Payload" "$f" || grep -qE "^##[[:space:]]+Annotated Example" "$f"; then
  check "AHB / Mapping Recheck" "^##[[:space:]]+AHB / Mapping Recheck"
  grep -qE "AHB|Mapping|Schema|Process|Fixture|Inference" "$f" || {
    echo "MISSING: field authority tags (expected one of AHB, Mapping, Schema, Process, Fixture, Inference)"
    fail=1
  }
fi

grep -qE "PROCESS_GRAPH\.json[^a-zA-Z]" "$f" && grep -qE "cite|Sources" "$f" && {
  # cheap heuristic: doc mentions PROCESS_GRAPH.json in Sources — that's the index, not a source
  if grep -A 20 "^## Sources" "$f" 2>/dev/null | grep -qE "PROCESS_GRAPH\.json"; then
    warn "PROCESS_GRAPH.json cited as a source — it is an index; cite the source files it points to"
  fi
}

echo "---"
echo "checked: $f"
echo "passed: $pass_count  warnings: $warn_count"
if (( fail )); then
  echo "LINT FAILED"
  exit 1
fi
echo "LINT OK"
