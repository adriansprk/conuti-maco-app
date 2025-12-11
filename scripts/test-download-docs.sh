#!/bin/bash
# test-download-docs.sh - Test downloading first 10 documentation URLs

set -e

OUTPUT_DIR="maco-api-documentation/docs-offline-test"
INDEX_FILE="$OUTPUT_DIR/index.json"

echo "🧪 Testing Documentation Download (First 10 URLs)..."
echo "Output directory: $OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Extract first 10 unique URLs from llm.txt
echo "Extracting first 10 URLs from llm.txt..."
URLS=$(grep -o 'https://doc\.macoapp\.de/[^)]*' llm.txt | sort -u | head -10)

echo "URLs to download:"
echo "$URLS"
echo ""

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
    
    echo "📥 Downloading: $filename"
    echo "   URL: $url"
    
    # Download the file
    if curl -s -f -L "$url" -o "$output_path" --max-time 30; then
        # Check if file has content
        if [ -s "$output_path" ]; then
            file_size=$(wc -c < "$output_path" | tr -d ' ')
            echo "   ✅ Success: $file_size bytes"
            SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
            
            # Add to index
            if [ "$FIRST" = false ]; then
                echo "," >> "$INDEX_FILE"
            fi
            echo "  \"$filename\": \"$url\"" | tr -d '\n' >> "$INDEX_FILE"
            FIRST=false
        else
            echo "   ⚠️  Warning: File is empty"
            rm "$output_path"
            FAIL_COUNT=$((FAIL_COUNT + 1))
        fi
    else
        echo "   ❌ Failed to download"
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
    
    echo ""
    
    # Small delay to be respectful
    sleep 0.5
done <<< "$URLS"

echo "}" >> "$INDEX_FILE"

echo "📊 Test Summary:"
echo "  ✅ Successfully downloaded: $SUCCESS_COUNT"
echo "  ❌ Failed: $FAIL_COUNT"
echo "  📁 Files saved to: $OUTPUT_DIR"
echo "  📋 Index created: $INDEX_FILE"
echo ""

if [ $SUCCESS_COUNT -gt 0 ]; then
    echo "📄 Sample file preview (first downloaded file):"
    FIRST_FILE=$(ls -t "$OUTPUT_DIR"/*.md 2>/dev/null | head -1)
    if [ -n "$FIRST_FILE" ]; then
        echo "File: $(basename "$FIRST_FILE")"
        echo "---"
        head -20 "$FIRST_FILE"
        echo "..."
    fi
fi

