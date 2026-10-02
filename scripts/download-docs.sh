#!/bin/bash
# download-docs.sh - Download all documentation from llm.txt
# Makes Prozessübersicht documentation available offline for AI agents

# Don't exit on error - continue downloading other files even if one fails
set +e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="docs-supplemental"
INDEX_FILE="$OUTPUT_DIR/index.json"
LOG_FILE="$OUTPUT_DIR/download.log"
PARALLEL_JOBS="${PARALLEL_JOBS:-3}"
MAX_RETRIES="${MAX_RETRIES:-3}"

echo "📥 Downloading MaCo API Documentation..."
echo "Output directory: $OUTPUT_DIR"
echo "Log file: $LOG_FILE"
echo "Parallel jobs: $PARALLEL_JOBS (override with PARALLEL_JOBS=N)"
echo "Max retries per URL: $MAX_RETRIES"
mkdir -p "$OUTPUT_DIR"
: > "$LOG_FILE"

# By default, refresh docs-supplemental/llm.txt from the old portal.
# Set SKIP_LLM_FETCH=1 to use the committed supplemental index (offline / reproducible).
if [ "${SKIP_LLM_FETCH:-}" != "1" ]; then
    echo "📄 Refreshing docs-supplemental/llm.txt from doc.macoapp.de ..."
    if "$SCRIPT_DIR/fetch-llm-index.sh"; then
        echo ""
    else
        echo "  ⚠️  fetch-llm-index.sh failed — continuing with existing docs-supplemental/llm.txt"
        echo ""
    fi
else
    echo "📄 SKIP_LLM_FETCH=1 — using existing docs-supplemental/llm.txt"
    echo ""
fi

# Extract old portal URLs from its separate index.
echo "Extracting URLs from docs-supplemental/llm.txt..."
URLS=$(grep -o 'https://doc\.macoapp\.de/[^)]*' docs-supplemental/llm.txt | sort -u)

URL_COUNT=$(echo "$URLS" | grep -c . || true)
echo "Found $URL_COUNT unique documentation URLs"
echo "Starting download at $(date)"
echo ""

STATUS_DIR=$(mktemp -d)
trap 'rm -rf "$STATUS_DIR"' EXIT

is_valid_doc_file() {
    local file="$1"
    if [ ! -s "$file" ]; then
        return 1
    fi
    if head -c 20 "$file" | grep -q '<!DOCTYPE html>'; then
        return 1
    fi
    if grep -q 'An abnormal error occurred' "$file" 2>/dev/null; then
        return 1
    fi
    return 0
}

download_one() {
    local url="$1"
    if [ -z "$url" ]; then
        return 0
    fi

    local filename
    filename=$(basename "$url")
    # Decode URL encoding (basic)
    filename=$(echo "$filename" | sed 's/%C3%BC/ü/g' | sed 's/%C3%A4/ä/g' | sed 's/%C3%B6/ö/g' | sed 's/%C3%9C/Ü/g' | sed 's/%C3%84/Ä/g' | sed 's/%C3%96/Ö/g' | sed 's/%C3%9F/ß/g')

    local output_path="$OUTPUT_DIR/$filename"
    local attempt=1

    while [ "$attempt" -le "$MAX_RETRIES" ]; do
        if curl -s -f -L "$url" -o "$output_path" --max-time 60 --connect-timeout 30 2>>"$LOG_FILE"; then
            if is_valid_doc_file "$output_path"; then
                echo "ok" >> "$STATUS_DIR/success.list"
                echo "✅ Downloaded: $filename"
                return 0
            fi
            echo "invalid HTML/rate-limit response for $filename (attempt $attempt/$MAX_RETRIES)" >>"$LOG_FILE"
            rm -f "$output_path"
        else
            echo "curl failed for $filename (attempt $attempt/$MAX_RETRIES)" >>"$LOG_FILE"
            rm -f "$output_path"
        fi

        if [ "$attempt" -lt "$MAX_RETRIES" ]; then
            sleep $((attempt * 2))
        fi
        attempt=$((attempt + 1))
    done

    echo "fail" >> "$STATUS_DIR/fail.list"
    echo "❌ Failed: $filename (check $LOG_FILE for details)"
}

export OUTPUT_DIR LOG_FILE STATUS_DIR MAX_RETRIES
export -f download_one is_valid_doc_file

if [ "$URL_COUNT" -gt 0 ]; then
    echo "$URLS" | xargs -n 1 -P "$PARALLEL_JOBS" -I {} bash -c 'download_one "$1"' _ {}
fi

SUCCESS_COUNT=0
FAIL_COUNT=0
if [ -f "$STATUS_DIR/success.list" ]; then
    SUCCESS_COUNT=$(wc -l < "$STATUS_DIR/success.list" | tr -d ' ')
fi
if [ -f "$STATUS_DIR/fail.list" ]; then
    FAIL_COUNT=$(wc -l < "$STATUS_DIR/fail.list" | tr -d ' ')
fi

INVALID_COUNT=0
if command -v rg >/dev/null 2>&1; then
    INVALID_COUNT=$(rg -l '^<!DOCTYPE html>' "$OUTPUT_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
fi

# Rebuild both source indexes after refreshing the older portal.
python3 "$SCRIPT_DIR/documentation_scope.py" --legacy-index "$OUTPUT_DIR/llm.txt" --legacy-dir "$OUTPUT_DIR"
if [ -f "$SCRIPT_DIR/rebuild-documentation-indexes.py" ]; then
    echo ""
    echo "📋 Rebuilding documentation indexes..."
    python3 "$SCRIPT_DIR/rebuild-documentation-indexes.py" || echo "  ⚠️  Index rebuild failed"
fi

echo ""
echo "Completed at $(date)"
echo "📊 Summary:"
echo "  ✅ Successfully downloaded: $SUCCESS_COUNT"
echo "  ❌ Failed: $FAIL_COUNT"
if [ "$INVALID_COUNT" -gt 0 ]; then
    echo "  ⚠️  Invalid HTML responses still on disk: $INVALID_COUNT (re-run with lower PARALLEL_JOBS)"
fi
echo "  📁 Files saved to: $OUTPUT_DIR"
echo "  📋 Index created: $INDEX_FILE"
if [ -f "$LOG_FILE" ] && [ -s "$LOG_FILE" ]; then
    echo "  📝 Error log: $LOG_FILE"
fi
