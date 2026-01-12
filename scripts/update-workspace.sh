#!/bin/bash
# Update workspace script
# Checks for new submodule versions, updates them, then reruns setup

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🔄 Updating MaCo Agent Workspace..."
echo ""

# Step 1: Fetch latest from submodule remotes
echo "🔍 Step 1: Checking for updates in submodules..."
HAS_UPDATES=false

if [ -f "$WORKSPACE_ROOT/.gitmodules" ]; then
    # Fetch latest from all submodule remotes
    echo "  Fetching latest from submodule remotes..."
    git submodule foreach --recursive 'git fetch origin 2>/dev/null || true' || true
    
    # Check each submodule for updates
    while IFS= read -r submodule_path; do
        if [ -n "$submodule_path" ] && [ -d "$WORKSPACE_ROOT/$submodule_path" ]; then
            cd "$WORKSPACE_ROOT/$submodule_path"
            
            # Get current commit and remote branch
            CURRENT=$(git rev-parse HEAD 2>/dev/null || echo "")
            BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
            
            # Try to get remote branch (fallback to origin/main or origin/master)
            REMOTE=""
            if git rev-parse "origin/$BRANCH" >/dev/null 2>&1; then
                REMOTE=$(git rev-parse "origin/$BRANCH" 2>/dev/null || echo "")
            elif git rev-parse "origin/main" >/dev/null 2>&1; then
                REMOTE=$(git rev-parse "origin/main" 2>/dev/null || echo "")
            elif git rev-parse "origin/master" >/dev/null 2>&1; then
                REMOTE=$(git rev-parse "origin/master" 2>/dev/null || echo "")
            fi
            
            if [ -n "$CURRENT" ] && [ -n "$REMOTE" ] && [ "$CURRENT" != "$REMOTE" ]; then
                echo "  📦 $submodule_path: Update available"
                echo "     Current: $(git rev-parse --short HEAD 2>/dev/null)"
                echo "     Remote:  $(git rev-parse --short "$REMOTE" 2>/dev/null)"
                HAS_UPDATES=true
            else
                echo "  ✅ $submodule_path: Up to date"
            fi
        fi
    done < <(git config --file .gitmodules --get-regexp path | awk '{print $2}')
    
    cd "$WORKSPACE_ROOT"
else
    echo "  ⚠️  No .gitmodules found"
fi

echo ""

# Step 2: Update submodules if updates available
if [ "$HAS_UPDATES" = true ]; then
    echo "📥 Step 2: Updating submodules to latest versions..."
    git submodule update --remote --recursive || {
        echo "  ⚠️  Some submodules failed to update - continuing anyway"
    }
    echo "  ✅ Submodules updated"
else
    echo "📥 Step 2: No submodule updates available - skipping update"
fi

echo ""

# Step 3: Run full setup to rebuild everything with new versions
echo "🔨 Step 3: Rebuilding workspace..."
echo "  (This will rebuild schemas, re-download docs, regenerate index)"
echo ""

"$WORKSPACE_ROOT/scripts/setup-workspace.sh"

echo ""
echo "✅ Workspace update complete!"
