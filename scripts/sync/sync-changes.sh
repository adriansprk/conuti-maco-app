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
    
    if [ -d ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        
        # Update version tracker
        jq ".external_repos.maco-api-documentation.last_synced = \"$TIMESTAMP\" | .external_repos.maco-api-documentation.last_commit_hash = \"$CURRENT_HASH\"" \
           "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
        
        echo "  ✅ Updated version tracker"
        echo "  📝 Commit: $CURRENT_HASH"
        
        # Check for build script changes
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
        
        # Note: llm.txt is manually downloaded from doc.macoapp.de, not part of this repo
    fi
fi

echo ""

# Update docs-offline tracking
if [ -d "$WORKSPACE_ROOT/docs-offline" ]; then
    echo "📚 Processing docs-offline..."
    
    FILE_COUNT=$(find "$WORKSPACE_ROOT/docs-offline" -name "*.md" | wc -l | tr -d ' ')
    
    jq ".external_repos.docs-offline.last_synced = \"$TIMESTAMP\" | .external_repos.docs-offline.file_count = $FILE_COUNT" \
       "$VERSION_TRACKER" > "$VERSION_TRACKER.tmp" && mv "$VERSION_TRACKER.tmp" "$VERSION_TRACKER"
    
    echo "  ✅ Updated version tracker"
    echo "  📝 File count: $FILE_COUNT"
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
