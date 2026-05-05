#!/bin/bash
# Initial workspace setup script
# Clones submodules, applies patches, builds JSON schemas, downloads docs, creates index

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🚀 Setting up MaCo Agent Workspace..."
echo ""

# Step 1: Initialize submodules (if not already done)
echo "📦 Step 1: Initializing Git submodules..."
if [ -f "$WORKSPACE_ROOT/.gitmodules" ]; then
    git submodule update --init --recursive 2>/dev/null || {
        echo "  ℹ️  Submodules already initialized or updating..."
    }
    echo "  ✅ Submodules ready"
else
    echo "  ⚠️  No .gitmodules found - submodules may need manual setup"
fi

echo ""

# Step 2: Apply build script patch
echo "🔧 Step 2: Applying workspace-specific patches..."
if [ -f "$WORKSPACE_ROOT/scripts/apply-build-script-patch.sh" ]; then
    "$WORKSPACE_ROOT/scripts/apply-build-script-patch.sh"
else
    echo "  ⚠️  Patch script not found - skipping"
fi

echo ""

# Step 3: Download documentation files
echo "📚 Step 3: Downloading documentation files..."
if [ "${SKIP_LLM_FETCH:-}" = "1" ]; then
    echo "  (SKIP_LLM_FETCH=1 — docs download will use committed docs/llm.txt without fetching llms.txt)"
fi
if [ -f "$WORKSPACE_ROOT/scripts/download-docs.sh" ]; then
    echo "  Downloading from doc.macoapp.de..."
    "$WORKSPACE_ROOT/scripts/download-docs.sh" || {
        echo "  ⚠️  Documentation download had issues - check output above"
    }
else
    echo "  ⚠️  download-docs.sh not found - skipping"
fi

echo ""

# Step 4: Build schemas (formatted JSON, not minified)
echo "🔨 Step 4: Building JSON schemas (formatted for indexing)..."
if [ -f "$WORKSPACE_ROOT/scripts/sync/rebuild-schemas.sh" ]; then
    "$WORKSPACE_ROOT/scripts/sync/rebuild-schemas.sh"
else
    echo "  ⚠️  rebuild-schemas.sh not found - skipping"
fi

echo ""

# Step 5: Generate PROCESS_GRAPH.json index
echo "📊 Step 5: Generating PROCESS_GRAPH.json index..."
if command -v python3 &> /dev/null; then
    if [ -f "$WORKSPACE_ROOT/scripts/sync/update-process-graph-minimal.py" ]; then
        python3 "$WORKSPACE_ROOT/scripts/sync/update-process-graph-minimal.py"
    else
        echo "  ⚠️  update-process-graph-minimal.py not found - skipping"
    fi
else
    echo "  ⚠️  python3 not found - install Python 3 to generate index"
fi

echo ""
echo "✅ Workspace setup complete!"
echo ""
echo "📋 Generated files:"
echo "  - JSON schemas: maco-api-documentation/_build/*.min.json (formatted, not minified)"
echo "  - Documentation: docs-offline/*.md"
echo "  - Process index: docs/entry-points/PROCESS_GRAPH.json"
echo ""
echo "💡 Next steps:"
echo "  1. Open workspace in Cursor IDE"
echo "  2. Start using AI agents with MaKo processes"
echo ""
echo "🔄 To update later: Run ./scripts/update-workspace.sh"
