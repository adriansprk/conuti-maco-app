#!/bin/bash
# Apply workspace-specific patch to build script
# This ensures JSON files are formatted (not minified) for indexing

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BUILD_SCRIPT="$WORKSPACE_ROOT/maco-api-documentation/scripts/build-openapi-json.sh"

if [ ! -f "$BUILD_SCRIPT" ]; then
    echo "⚠️  Build script not found: $BUILD_SCRIPT"
    echo "   Make sure maco-api-documentation submodule is initialized"
    exit 1
fi

echo "🔧 Applying formatting patch to build script..."

# Check if patch is already applied
if grep -q "jq \." "$BUILD_SCRIPT" 2>/dev/null && ! grep -q "jq -c \." "$BUILD_SCRIPT" 2>/dev/null; then
    echo "  ✅ Patch already applied (using jq . for formatting)"
    exit 0
fi

# Create backup
cp "$BUILD_SCRIPT" "${BUILD_SCRIPT}.bak"

# Apply patch: change jq -c to jq . (format instead of minify)
# Use different sed syntax for macOS compatibility
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS sed requires -i '' for in-place editing
    sed -i '' 's/jq -c \./jq ./g' "$BUILD_SCRIPT"
    sed -i '' 's/build_and_minify_openapi/build_and_format_openapi/g' "$BUILD_SCRIPT"
else
    # Linux sed
    sed -i 's/jq -c \./jq ./g' "$BUILD_SCRIPT"
    sed -i 's/build_and_minify_openapi/build_and_format_openapi/g' "$BUILD_SCRIPT"
fi

# Remove backup file
rm -f "${BUILD_SCRIPT}.bak"

echo "  ✅ Patch applied successfully"
echo "  📝 Build script now formats JSON (readable) instead of minifying"
