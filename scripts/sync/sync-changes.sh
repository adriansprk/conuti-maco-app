#!/bin/bash
# Sync changes from external repositories and update PROCESS_GRAPH.json

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VERSION_TRACKER="$SCRIPT_DIR/version-tracker.json"
PROCESS_GRAPH="$WORKSPACE_ROOT/docs/entry-points/PROCESS_GRAPH.json"

echo "🔄 Syncing changes from external repositories..."
echo ""

# Update version tracker timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Check maco-api-documentation
if [ -d "$WORKSPACE_ROOT/maco-api-documentation" ]; then
    echo "📦 Processing maco-api-documentation..."
    
    cd "$WORKSPACE_ROOT/maco-api-documentation"
    
    # Check if it's a git repo (regular repo or submodule)
    if [ -d ".git" ] || [ -f ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        
        # Get last tracked hash from version tracker
        LAST_HASH=$(jq -r '."external_repos"."maco-api-documentation".last_commit_hash' "$VERSION_TRACKER" 2>/dev/null || echo "")
        
        # Update version tracker
        jq ".\"external_repos\".\"maco-api-documentation\".last_synced = \"$TIMESTAMP\" | .\"external_repos\".\"maco-api-documentation\".last_commit_hash = \"$CURRENT_HASH\"" \
           "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
        
        echo "  ✅ Updated version tracker"
        echo "  📝 Commit: $CURRENT_HASH"
        
        # Check for build script changes (only if we have a previous hash to compare)
        if [ -n "$LAST_HASH" ] && [ "$LAST_HASH" != "null" ] && [ "$LAST_HASH" != "$CURRENT_HASH" ]; then
            if git diff --name-only "$LAST_HASH" HEAD 2>/dev/null | grep -q "scripts/build-openapi-json.sh"; then
                echo ""
                echo "  🚨 CRITICAL: Build script changed!"
                echo "  ⚠️  Schema formatting may have changed"
                echo "  💡 You should re-run the build script:"
                echo "     cd maco-api-documentation && ./scripts/build-openapi-json.sh"
                echo ""
                read -p "  Re-run build script now? (y/n) " -n 1 -r
                echo
                if [[ $REPLY =~ ^[Yy]$ ]]; then
                    echo "  🔨 Running build script..."
                    ./scripts/build-openapi-json.sh
                    echo "  ✅ Build complete"
                else
                    echo "  ⚠️  Skipped - remember to rebuild schemas manually"
                fi
            fi
        fi
        
        # Check for schema changes
        SCHEMA_CHANGED=false
        if [ -f "_build/bo4e-openapi.min.json" ]; then
            SCHEMA_CHANGED=true
            echo "  📋 Schemas found - will update PROCESS_GRAPH.json"
            
            # Verify schemas are formatted (not minified)
            if command -v jq &> /dev/null; then
                FIRST_LINE=$(head -1 "_build/bo4e-openapi.min.json")
                if [[ "$FIRST_LINE" == "{" ]]; then
                    echo "  ✅ Schemas appear to be formatted (readable)"
                else
                    echo "  ⚠️  Schemas may not be formatted - consider rebuilding"
                fi
            fi
        fi
        
        # Check for business rules changes
        if [ -d "pythons/createPiFromTemplater/templater/yaml_output" ]; then
            YAML_COUNT=$(find "pythons/createPiFromTemplater/templater/yaml_output" -name "*.yaml" | wc -l | tr -d ' ')
            echo "  📋 Found $YAML_COUNT business rule files"
        fi
        
        # Note: the older portal index is in docs-supplemental/llm.txt; the new indexes are in docs/dokumentation/.
    fi
fi

echo ""

# Update bo4e-schema tracking
if [ -d "$WORKSPACE_ROOT/bo4e-schema" ]; then
    echo "📦 Processing bo4e-schema..."
    cd "$WORKSPACE_ROOT/bo4e-schema"
    if [ -d ".git" ] || [ -f ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        jq ".external_repos.\"bo4e-schema\".last_synced = \"$TIMESTAMP\" | .external_repos.\"bo4e-schema\".last_commit_hash = \"$CURRENT_HASH\"" \
           "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
        echo "  ✅ Updated version tracker"
        echo "  📝 Commit: $CURRENT_HASH"
    fi
fi

echo ""

# Update cdoc-schema tracking
if [ -d "$WORKSPACE_ROOT/cdoc-schema" ]; then
    echo "📦 Processing cdoc-schema..."
    cd "$WORKSPACE_ROOT/cdoc-schema"
    if [ -d ".git" ] || [ -f ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        jq ".external_repos.\"cdoc-schema\".last_synced = \"$TIMESTAMP\" | .external_repos.\"cdoc-schema\".last_commit_hash = \"$CURRENT_HASH\"" \
           "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
        echo "  ✅ Updated version tracker"
        echo "  📝 Commit: $CURRENT_HASH"
    fi
fi

echo ""

# Update docs-offline tracking
if [ -d "$WORKSPACE_ROOT/docs-offline" ]; then
    echo "📚 Processing docs-offline..."
    
    FILE_COUNT=$(find "$WORKSPACE_ROOT/docs-offline" -name "*.md" | wc -l | tr -d ' ')
    
    jq ".\"external_repos\".\"docs-offline\".last_synced = \"$TIMESTAMP\" | .\"external_repos\".\"docs-offline\".file_count = $FILE_COUNT" \
       "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
    
    echo "  ✅ Updated version tracker"
    echo "  📝 File count: $FILE_COUNT"
fi

echo ""

if [ -d "$WORKSPACE_ROOT/docs-supplemental" ]; then
    echo "📚 Processing docs-supplemental..."
    FILE_COUNT=$(find "$WORKSPACE_ROOT/docs-supplemental" -maxdepth 1 -name "*.md" | wc -l | tr -d ' ')
    jq ".\"external_repos\".\"docs-supplemental\".last_synced = \"$TIMESTAMP\" | .\"external_repos\".\"docs-supplemental\".file_count = $FILE_COUNT" \
       "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
    echo "  ✅ Updated supplemental tracker: $FILE_COUNT files"
fi

echo ""

# Update maco-edi-testfiles tracking
if [ -d "$WORKSPACE_ROOT/maco-edi-testfiles" ]; then
    echo "📦 Processing maco-edi-testfiles..."
    
    cd "$WORKSPACE_ROOT/maco-edi-testfiles"
    
    # Check if it's a git repo (regular repo or submodule)
    if [ -d ".git" ] || [ -f ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        
        # Update version tracker
        jq ".external_repos.\"maco-edi-testfiles\".last_synced = \"$TIMESTAMP\" | .external_repos.\"maco-edi-testfiles\".last_commit_hash = \"$CURRENT_HASH\"" \
           "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
        
        echo "  ✅ Updated version tracker"
        echo "  📝 Commit: $CURRENT_HASH"
        
        # Count test files
        EDI_COUNT=$(find . -name "*.edi" | wc -l | tr -d ' ')
        JSON_COUNT=$(find . -name "*.json" | wc -l | tr -d ' ')
        echo "  📋 Test files: $EDI_COUNT EDI, $JSON_COUNT JSON"
        
        # Check for version directories
        VERSION_DIRS=$(find . -type d -name "v[0-9]*" | grep -E "(inbound|outbound)" | sed 's|^\./||' | sort -u)
        if [ -n "$VERSION_DIRS" ]; then
            echo "  📋 Version directories found:"
            echo "$VERSION_DIRS" | head -5 | sed 's/^/    /'
            VERSION_COUNT=$(echo "$VERSION_DIRS" | wc -l | tr -d ' ')
            if [ "$VERSION_COUNT" -gt 5 ]; then
                echo "    ... and $((VERSION_COUNT - 5)) more"
            fi
        fi
    else
        echo "  ⚠️  Not a git repository - cannot track changes"
    fi
else
    echo "  ⚠️  maco-edi-testfiles not found"
fi

echo ""

# Update ebd-diagrams tracking
if [ -d "$WORKSPACE_ROOT/ebd-diagrams" ]; then
    echo "📊 Processing ebd-diagrams..."

    cd "$WORKSPACE_ROOT/ebd-diagrams"

    if [ -d ".git" ] || [ -f ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        REF_SNAPSHOT=$(python3 "$SCRIPT_DIR/reference-data-status.py" snapshot)
        LATEST_FV=$(echo "$REF_SNAPSHOT" | jq -r '.ebd_diagrams.latest_format_version // ""')
        EBD_COUNT=$(echo "$REF_SNAPSHOT" | jq -r '.ebd_diagrams.ebd_count_latest // 0')
        FV_LIST=$(echo "$REF_SNAPSHOT" | jq -c '.ebd_diagrams.format_versions // []')

        jq \
          ".external_repos.\"ebd-diagrams\".last_synced = \"$TIMESTAMP\" |
           .external_repos.\"ebd-diagrams\".last_commit_hash = \"$CURRENT_HASH\" |
           .external_repos.\"ebd-diagrams\".latest_format_version = $(echo "$LATEST_FV" | jq -R .) |
           .external_repos.\"ebd-diagrams\".ebd_count_latest = $EBD_COUNT |
           .external_repos.\"ebd-diagrams\".format_versions = $FV_LIST" \
           "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"

        echo "  ✅ Updated version tracker"
        echo "  📝 Commit: $CURRENT_HASH"
        echo "  📋 Latest format version: ${LATEST_FV:-unknown} ($EBD_COUNT EBD JSON files)"
    else
        echo "  ⚠️  Not a git repository - cannot track changes"
    fi
else
    echo "  ⚠️  ebd-diagrams not found"
fi

echo ""

# Update ahb-tables tracking
if [ -d "$WORKSPACE_ROOT/ahb-tables" ]; then
    echo "📋 Processing ahb-tables..."

    REF_SNAPSHOT=$(python3 "$SCRIPT_DIR/reference-data-status.py" snapshot)
    AHB_VERSIONS=$(echo "$REF_SNAPSHOT" | jq -c '.ahb_tables.versions // []')
    AHB_COUNTS=$(echo "$REF_SNAPSHOT" | jq -c '.ahb_tables.version_counts // {}')

    jq \
      ".external_repos.\"ahb-tables\".last_synced = \"$TIMESTAMP\" |
       .external_repos.\"ahb-tables\".versions = $AHB_VERSIONS |
       .external_repos.\"ahb-tables\".version_counts = $AHB_COUNTS" \
       "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"

    echo "  ✅ Updated version tracker"
    echo "$REF_SNAPSHOT" | jq -r '.ahb_tables.version_counts | to_entries[] | "  📝 \(.key): \(.value) Prüfidentifikatoren"'
else
    echo "  ⚠️  ahb-tables not found"
fi

echo ""

# Update PROCESS_GRAPH.json metadata
if [ -f "$PROCESS_GRAPH" ]; then
    echo "📊 Updating PROCESS_GRAPH.json metadata..."
    
    # Update timestamp only (preserve version from minimal script)
    jq ".generated = \"$TIMESTAMP\"" \
       "$PROCESS_GRAPH" > "$PROCESS_GRAPH.tmp" && mv "$PROCESS_GRAPH.tmp" "$PROCESS_GRAPH"
    
    echo "  ✅ Updated generation timestamp"
else
    echo "  ⚠️  PROCESS_GRAPH.json not found at $PROCESS_GRAPH"
    echo "  💡 You may need to regenerate it"
fi

echo ""
echo "✅ Sync complete!"
echo ""
echo "⚠️  Note: This script updates tracking metadata."
echo "   To regenerate PROCESS_GRAPH.json from source files, run:"
echo "   python3 scripts/sync/update-process-graph-minimal.py"
echo ""
echo "📋 Next steps:"
echo "   1. Review changes in external repos"
echo "   2. Run update-process-graph-minimal.py if docs changed"
echo "   3. Test updated PROCESS_GRAPH.json"
echo "   4. Commit changes"
