#!/bin/bash
# download-docs.sh - Download all documentation from llm.txt
# Makes Prozessübersicht documentation available offline for AI agents

set -e

OUTPUT_DIR="maco-api-documentation/docs-offline"
INDEX_FILE="$OUTPUT_DIR/index.json"

echo "📥 Downloading MaCo API Documentation..."
echo "Output directory: $OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Extract all doc.macoapp.de URLs from llm.txt
echo "Extracting URLs from llm.txt..."
URLS=$(grep -o 'https://doc\.macoapp\.de/[^)]*' llm.txt | sort -u)

URL_COUNT=$(echo "$URLS" | wc -l | tr -d ' ')
echo "Found $URL_COUNT unique documentation URLs"

# Create index structure
echo "{" > "$INDEX_FILE"
FIRST=true

SUCCESS_COUNT=0
FAIL_COUNT=0

while IFS= read -r url; do
    if [ -z "$url" ]; then
        continue
    fi
    
    # Extract filename from URL
    filename=$(basename "$url")
    # Decode URL encoding (basic)
    filename=$(echo "$filename" | sed 's/%C3%BC/ü/g' | sed 's/%C3%A4/ä/g' | sed 's/%C3%B6/ö/g' | sed 's/%C3%9C/Ü/g' | sed 's/%C3%84/Ä/g' | sed 's/%C3%96/Ö/g' | sed 's/%C3%9F/ß/g')
    
    output_path="$OUTPUT_DIR/$filename"
    
    # Download the file
    if curl -s -f -L "$url" -o "$output_path" --max-time 30; then
        echo "✅ Downloaded: $filename"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        
        # Add to index
        if [ "$FIRST" = false ]; then
            echo "," >> "$INDEX_FILE"
        fi
        echo "  \"$filename\": \"$url\"" | tr -d '\n' >> "$INDEX_FILE"
        FIRST=false
    else
        echo "❌ Failed: $filename"
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
    
    # Small delay to be respectful
    sleep 0.5
done <<< "$URLS"

echo "}" >> "$INDEX_FILE"

echo ""
echo "📊 Summary:"
echo "  ✅ Successfully downloaded: $SUCCESS_COUNT"
echo "  ❌ Failed: $FAIL_COUNT"
echo "  📁 Files saved to: $OUTPUT_DIR"
echo "  📋 Index created: $INDEX_FILE"

