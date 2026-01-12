#!/bin/bash
# Rebuild formatted JSON schemas from source YAML files
# Use this when build script changes or schemas need regeneration

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
MACO_API_DOC="$WORKSPACE_ROOT/maco-api-documentation"

if [ ! -d "$MACO_API_DOC" ]; then
    echo "❌ maco-api-documentation directory not found at $MACO_API_DOC"
    exit 1
fi

echo "🔨 Rebuilding formatted JSON schemas..."
echo ""

cd "$MACO_API_DOC"

# Check if build script exists
if [ ! -f "scripts/build-openapi-json.sh" ]; then
    echo "❌ Build script not found at scripts/build-openapi-json.sh"
    exit 1
fi

# Check dependencies
echo "📋 Checking dependencies..."

if ! command -v jq &> /dev/null; then
    echo "❌ jq not found - required for JSON formatting"
    echo "   Install with: brew install jq (macOS) or apt-get install jq (Linux)"
    exit 1
fi
echo "  ✅ jq found"

if ! command -v npx &> /dev/null; then
    echo "❌ npx not found - required for @redocly/openapi-cli"
    echo "   Install Node.js to get npx"
    exit 1
fi
echo "  ✅ npx found"

echo ""
echo "🔧 Applying workspace-specific build script patch..."
echo "   (Ensures JSON files are formatted for indexing, not minified)"
"$WORKSPACE_ROOT/scripts/apply-build-script-patch.sh"

echo ""
echo "🚀 Running build script..."
echo ""

# Run the build script
./scripts/build-openapi-json.sh

echo ""
echo "✅ Schema rebuild complete!"
echo ""
echo "📋 Generated files in _build/:"
ls -lh _build/*.min.json 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'

echo ""
echo "💡 Next steps:"
echo "   1. Verify schemas are formatted (readable, not minified)"
echo "   2. Run: ./scripts/sync/sync-changes.sh to update tracking"
echo "   3. Regenerate PROCESS_GRAPH.json if needed: python3 scripts/sync/update-process-graph-minimal.py"
echo "   4. Test with your application"
