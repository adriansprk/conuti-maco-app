#!/usr/bin/env bash
# Deterministic local gate for documentation discovery and evidence scripts.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

python3 scripts/rebuild-documentation-indexes.py --check
python3 scripts/test-documentation-discovery.py
python3 scripts/test-essentials-evidence.py
bash -n scripts/download-dokumentation.sh scripts/download-docs.sh scripts/fetch-llm-index.sh
echo "Workspace validation OK"
