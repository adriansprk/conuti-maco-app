#!/usr/bin/env bash
# Downloads all AHB tables from ahb-tabellen.hochfrequenz.de (public API, no auth required)
# Usage: ./scripts/download-ahb-tables.sh [FV2510 FV2604]
# Default: downloads both FV2510 and FV2604

set -euo pipefail

BASE_URL="https://ahb-tabellen.hochfrequenz.de/api"
TARGET_DIR="$(cd "$(dirname "$0")/.." && pwd)/ahb-tables"
VERSIONS=("${@:-FV2510 FV2604}")
PARALLEL_JOBS=10
DELAY=0.05  # seconds between requests per worker

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log()    { echo -e "${GREEN}[✓]${NC} $*"; }
warn()   { echo -e "${YELLOW}[!]${NC} $*"; }
error()  { echo -e "${RED}[✗]${NC} $*" >&2; }

download_ahb() {
    local fv="$1"
    local prufi="$2"
    local outfile="$3"

    if [[ -f "$outfile" ]]; then
        return 0  # skip if already exists
    fi

    local url="${BASE_URL}/ahb/${fv}/${prufi}"
    local tmp="${outfile}.tmp"

    if curl -sf --max-time 30 -o "$tmp" "$url"; then
        # Validate it's valid JSON with content
        if python3 -c "import sys,json; d=json.load(open('$tmp')); exit(0 if d.get('lines') else 1)" 2>/dev/null; then
            mv "$tmp" "$outfile"
            return 0
        else
            rm -f "$tmp"
            return 1
        fi
    else
        rm -f "$tmp"
        return 2
    fi
}

export -f download_ahb
export BASE_URL

for FV in "${VERSIONS[@]}"; do
    echo ""
    log "=== Processing $FV ==="

    # Get list of all available Prüfidentifikatoren
    PRUFI_JSON=$(curl -sf "${BASE_URL}/pruefidentifikatoren/${FV}")
    TOTAL=$(echo "$PRUFI_JSON" | python3 -c "import sys,json; data=json.load(sys.stdin); print(len(data))")
    log "Found $TOTAL Prüfidentifikatoren in $FV"

    OUTDIR="${TARGET_DIR}/${FV}"
    mkdir -p "$OUTDIR"

    # Count existing files
    EXISTING=$(ls "$OUTDIR"/AHB_${FV}_*.json 2>/dev/null | wc -l | tr -d ' ')
    warn "Already have $EXISTING / $TOTAL files"

    # Build download list
    PRUFI_LIST=$(echo "$PRUFI_JSON" | python3 -c "import sys,json; [print(d['pruefidentifikator']) for d in json.load(sys.stdin)]")

    DOWNLOADED=0
    SKIPPED=0
    FAILED=0
    FAILED_LIST=()

    # Download with parallel workers using xargs
    echo "$PRUFI_LIST" | while read -r PRUFI; do
        OUTFILE="${OUTDIR}/AHB_${FV}_${PRUFI}.json"
        echo "${FV}|${PRUFI}|${OUTFILE}"
    done | xargs -P "$PARALLEL_JOBS" -I{} bash -c '
        IFS="|" read -r FV PRUFI OUTFILE <<< "{}"
        if [[ -f "$OUTFILE" ]]; then
            echo "SKIP|$PRUFI"
            exit 0
        fi
        URL="'"$BASE_URL"'/ahb/${FV}/${PRUFI}"
        TMP="${OUTFILE}.tmp"
        if curl -sf --max-time 30 -o "$TMP" "$URL" 2>/dev/null; then
            if python3 -c "import json; d=json.load(open(\"$TMP\")); exit(0 if d.get(\"lines\") is not None else 1)" 2>/dev/null; then
                mv "$TMP" "$OUTFILE"
                echo "OK|$PRUFI"
            else
                rm -f "$TMP"
                echo "EMPTY|$PRUFI"
            fi
        else
            rm -f "$TMP"
            echo "FAIL|$PRUFI"
        fi
        sleep '"$DELAY"'
    ' | tee /tmp/ahb_download_${FV}.log | while read -r LINE; do
        STATUS="${LINE%%|*}"
        PRUFI="${LINE##*|}"
        case "$STATUS" in
            OK)   echo -ne "${GREEN}.${NC}" ;;
            SKIP) echo -ne "." ;;
            EMPTY) warn "Empty response for $PRUFI" ;;
            FAIL) echo -ne "${RED}F${NC}" ;;
        esac
    done
    echo ""

    # Summary
    OK_COUNT=$(grep -c "^OK|" /tmp/ahb_download_${FV}.log 2>/dev/null || echo 0)
    SKIP_COUNT=$(grep -c "^SKIP|" /tmp/ahb_download_${FV}.log 2>/dev/null || echo 0)
    FAIL_COUNT=$(grep -c "^FAIL\|^EMPTY" /tmp/ahb_download_${FV}.log 2>/dev/null || echo 0)
    FINAL=$(ls "$OUTDIR"/AHB_${FV}_*.json 2>/dev/null | wc -l | tr -d ' ')

    log "$FV complete: $OK_COUNT downloaded, $SKIP_COUNT skipped, $FAIL_COUNT failed → $FINAL total files"

    if [[ "$FAIL_COUNT" -gt 0 ]]; then
        warn "Failed Prüfis:"
        grep "^FAIL\|^EMPTY" /tmp/ahb_download_${FV}.log | sed 's/.*|/  - /'
    fi
done

echo ""
log "All done. Files saved to: $TARGET_DIR"
