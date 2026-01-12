#!/bin/bash
# download-docs.sh - Download all documentation from llm.txt
# Makes Prozessübersicht documentation available offline for AI agents

# Don't exit on error - continue downloading other files even if one fails
set +e

OUTPUT_DIR="docs-offline"
INDEX_FILE="$OUTPUT_DIR/index.json"
LOG_FILE="$OUTPUT_DIR/download.log"

echo "📥 Downloading MaCo API Documentation..."
echo "Output directory: $OUTPUT_DIR"
echo "Log file: $LOG_FILE"
mkdir -p "$OUTPUT_DIR"

# Extract all doc.macoapp.de URLs from llm.txt
echo "Extracting URLs from docs/llm.txt..."
URLS=$(grep -o 'https://doc\.macoapp\.de/[^)]*' docs/llm.txt | sort -u)

URL_COUNT=$(echo "$URLS" | wc -l | tr -d ' ')
echo "Found $URL_COUNT unique documentation URLs"
echo "Starting download at $(date)"
echo ""

# Create index structure
echo "{" > "$INDEX_FILE"
FIRST=true

SUCCESS_COUNT=0
FAIL_COUNT=0
CURRENT=0

while IFS= read -r url; do
    if [ -z "$url" ]; then
        continue
    fi
    
    CURRENT=$((CURRENT + 1))
    
    # Extract filename from URL
    filename=$(basename "$url")
    # Decode URL encoding (basic)
    filename=$(echo "$filename" | sed 's/%C3%BC/ü/g' | sed 's/%C3%A4/ä/g' | sed 's/%C3%B6/ö/g' | sed 's/%C3%9C/Ü/g' | sed 's/%C3%84/Ä/g' | sed 's/%C3%96/Ö/g' | sed 's/%C3%9F/ß/g')
    
    output_path="$OUTPUT_DIR/$filename"
    
    # Show progress
    printf "[%3d/%3d] " "$CURRENT" "$URL_COUNT"
    
    # Download the file with increased timeout (60 seconds)
    if curl -s -f -L "$url" -o "$output_path" --max-time 60 --connect-timeout 30 2>>"$LOG_FILE"; then
        echo "✅ Downloaded: $filename"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        
        # Add to index
        if [ "$FIRST" = false ]; then
            echo "," >> "$INDEX_FILE"
        fi
        echo "  \"$filename\": \"$url\"" | tr -d '\n' >> "$INDEX_FILE"
        FIRST=false
    else
        echo "❌ Failed: $filename (check $LOG_FILE for details)"
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
    
    # Small delay to be respectful
    sleep 0.3
done <<< "$URLS"

echo "}" >> "$INDEX_FILE"

echo ""
echo "Completed at $(date)"
echo "📊 Summary:"
echo "  ✅ Successfully downloaded: $SUCCESS_COUNT"
echo "  ❌ Failed: $FAIL_COUNT"
echo "  📁 Files saved to: $OUTPUT_DIR"
echo "  📋 Index created: $INDEX_FILE"
if [ -f "$LOG_FILE" ] && [ -s "$LOG_FILE" ]; then
    echo "  📝 Error log: $LOG_FILE"
fi

