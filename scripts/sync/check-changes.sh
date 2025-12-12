#!/bin/bash
# Check for changes in external repositories and report what needs updating

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VERSION_TRACKER="$SCRIPT_DIR/version-tracker.json"

echo "🔍 Checking for changes in external repositories..."
echo ""

# Check maco-api-documentation changes
if [ -d "$WORKSPACE_ROOT/maco-api-documentation" ]; then
    echo "📦 Checking maco-api-documentation..."
    
    cd "$WORKSPACE_ROOT/maco-api-documentation"
    
    # Check if it's a git repo
    if [ -d ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        LAST_HASH=$(jq -r '."external_repos"."maco-api-documentation".last_commit_hash' "$VERSION_TRACKER" 2>/dev/null || echo "null")
        
        if [ "$CURRENT_HASH" != "$LAST_HASH" ] && [ "$LAST_HASH" != "null" ]; then
            echo "  ⚠️  Changes detected!"
            echo "  📝 Last synced: $(jq -r '."external_repos"."maco-api-documentation".last_synced' "$VERSION_TRACKER")"
            echo "  🔄 Current commit: $CURRENT_HASH"
            echo "  📋 Changed files:"
            CHANGED_FILES=$(git diff --name-only "$LAST_HASH" HEAD)
            echo "$CHANGED_FILES" | head -20
            
            # Check for critical build script changes
            if echo "$CHANGED_FILES" | grep -q "scripts/build-openapi-json.sh"; then
                echo ""
                echo "  🚨 CRITICAL: Build script changed!"
                echo "  ⚠️  Schema formatting may have changed"
                echo "  💡 Action required: Re-run build script to regenerate _build/*.min.json"
                echo "     cd maco-api-documentation && ./scripts/build-openapi-json.sh"
            fi
            
            # Check for nodemon config changes
            if echo "$CHANGED_FILES" | grep -q "nodemon.json"; then
                echo ""
                echo "  ⚠️  Build configuration changed (nodemon.json)"
                echo "  💡 May affect auto-rebuild behavior"
            fi
            
            # Note: llm.txt is NOT part of maco-api-documentation repo
            # It's manually downloaded from doc.macoapp.de
            # Changes to llm.txt would be in workspace, not repo
            
            echo ""
            echo "  💡 Run: ./scripts/sync/sync-changes.sh to update tracking"
        else
            echo "  ✅ No changes detected (or first run)"
        fi
    else
        echo "  ⚠️  Not a git repository - cannot track changes"
        echo "  💡 Consider adding as git submodule or tracking manually"
    fi
else
    echo "  ⚠️  maco-api-documentation not found"
fi

echo ""

# Check docs-offline changes
if [ -d "$WORKSPACE_ROOT/docs-offline" ]; then
    echo "📚 Checking docs-offline..."
    
    FILE_COUNT=$(find "$WORKSPACE_ROOT/docs-offline" -name "*.md" | wc -l | tr -d ' ')
    LAST_COUNT=$(jq -r '."external_repos"."docs-offline".file_count' "$VERSION_TRACKER" 2>/dev/null || echo "0")
    
    if [ "$FILE_COUNT" != "$LAST_COUNT" ]; then
        echo "  ⚠️  File count changed!"
        echo "  📝 Last count: $LAST_COUNT"
        echo "  🔄 Current count: $FILE_COUNT"
        echo "  💡 Run: ./scripts/sync/sync-changes.sh to update"
    else
        echo "  ✅ No changes detected (or first run)"
    fi
else
    echo "  ⚠️  docs-offline not found"
fi

echo ""

# Check maco-edi-testfiles changes
if [ -d "$WORKSPACE_ROOT/maco-edi-testfiles" ]; then
    echo "📦 Checking maco-edi-testfiles..."
    
    cd "$WORKSPACE_ROOT/maco-edi-testfiles"
    
    # Check if it's a git repo
    if [ -d ".git" ]; then
        CURRENT_HASH=$(git rev-parse HEAD)
        LAST_HASH=$(jq -r '."external_repos"."maco-edi-testfiles".last_commit_hash' "$VERSION_TRACKER" 2>/dev/null || echo "null")
        
        if [ "$CURRENT_HASH" != "$LAST_HASH" ] && [ "$LAST_HASH" != "null" ]; then
            echo "  ⚠️  Changes detected!"
            echo "  📝 Last synced: $(jq -r '."external_repos"."maco-edi-testfiles".last_synced' "$VERSION_TRACKER")"
            echo "  🔄 Current commit: $CURRENT_HASH"
            echo "  📋 Changed files summary:"
            CHANGED_FILES=$(git diff --name-only "$LAST_HASH" HEAD)
            EDI_COUNT=$(echo "$CHANGED_FILES" | grep -c "\.edi$" || echo "0")
            JSON_COUNT=$(echo "$CHANGED_FILES" | grep -c "\.json$" || echo "0")
            echo "    - EDI files: $EDI_COUNT"
            echo "    - JSON files: $JSON_COUNT"
            echo "    - Total files: $(echo "$CHANGED_FILES" | wc -l | tr -d ' ')"
            
            # Show sample of changed files
            echo "  📋 Sample changed files:"
            echo "$CHANGED_FILES" | head -10 | sed 's/^/    /'
            if [ $(echo "$CHANGED_FILES" | wc -l) -gt 10 ]; then
                echo "    ... and $(($(echo "$CHANGED_FILES" | wc -l) - 10)) more"
            fi
            
            # Check for new version directories
            NEW_VERSIONS=$(echo "$CHANGED_FILES" | grep -oE "(inbound|outbound)/v[0-9]+" | sort -u)
            if [ -n "$NEW_VERSIONS" ]; then
                echo ""
                echo "  🆕 New version directories detected:"
                echo "$NEW_VERSIONS" | sed 's/^/    /'
            fi
            
            echo ""
            echo "  💡 Run: ./scripts/sync/sync-changes.sh to update tracking"
        else
            echo "  ✅ No changes detected (or first run)"
        fi
    else
        echo "  ⚠️  Not a git repository - cannot track changes"
        echo "  💡 Consider adding as git submodule or tracking manually"
    fi
else
    echo "  ⚠️  maco-edi-testfiles not found"
fi

echo ""
echo "✅ Change check complete!"
echo ""
echo "To update PROCESS_GRAPH.json after changes:"
echo "  1. Run: ./scripts/sync/sync-changes.sh (updates tracking)"
echo "  2. Run: python3 scripts/sync/update-process-graph-minimal.py (regenerates index)"
