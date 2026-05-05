#!/bin/bash
# Fetch MaCo's canonical documentation index from doc.macoapp.de → docs/llm.txt
#
# Remote filename is llms.txt; the workspace keeps using docs/llm.txt for all tooling.
#
# Usage:
#   ./scripts/fetch-llm-index.sh
#   MACO_DOC_INDEX_URL=https://doc.macoapp.de/llms.txt ./scripts/fetch-llm-index.sh
#
# Invoked automatically by download-docs.sh unless SKIP_LLM_FETCH=1.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
URL="${MACO_DOC_INDEX_URL:-https://doc.macoapp.de/llms.txt}"
OUT="$WORKSPACE_ROOT/docs/llm.txt"

echo "📄 Fetching MaCo documentation index..."
echo "   URL:  $URL"
echo "   Dest: $OUT"

mkdir -p "$(dirname "$OUT")"
TMP="${OUT}.tmp.$$"
if curl -s -f -L "$URL" -o "$TMP" --max-time 120 --connect-timeout 30; then
    mv "$TMP" "$OUT"
    echo "   ✅ Wrote $(wc -l < "$OUT" | tr -d ' ') lines"
else
    rm -f "$TMP"
    echo "   ❌ Failed to fetch index (curl exited non-zero)" >&2
    exit 1
fi
