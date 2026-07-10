#!/bin/bash
# Initialize and pull all git submodules to their tracked upstream branches.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
GITMODULES="$WORKSPACE_ROOT/.gitmodules"

SUBMODULES=(
  bo4e-schema
  cdoc-schema
  maco-api-documentation
  maco-edi-testfiles
  ebd-diagrams
)

echo "🔄 Updating git submodules..."
echo "Workspace: $WORKSPACE_ROOT"
echo ""

cd "$WORKSPACE_ROOT"
git submodule update --init --recursive "${SUBMODULES[@]}"

for sub in "${SUBMODULES[@]}"; do
  path="$WORKSPACE_ROOT/$sub"
  if [ ! -d "$path" ]; then
    echo "⚠️  Skipping $sub (path not found)"
    continue
  fi

  branch="$(git config -f "$GITMODULES" "submodule.$sub.branch" || true)"
  if [ -z "$branch" ]; then
    branch="main"
  fi

  echo "📦 $sub (branch: $branch)"
  cd "$path"

  if [ ! -d ".git" ] && [ ! -f ".git" ]; then
    echo "  ⚠️  Not a git repository"
    continue
  fi

  git fetch origin

  if git show-ref --verify --quiet "refs/remotes/origin/$branch"; then
    if ! git checkout "$branch" 2>/dev/null; then
      git checkout -B "$branch" "origin/$branch"
    fi
    git pull --ff-only origin "$branch"
  else
    echo "  ⚠️  origin/$branch not found; leaving current checkout in place"
  fi

  echo "  ✅ $(git rev-parse --short HEAD) ($(git log -1 --format='%s' | head -c 80))"
  echo ""
done

echo "✅ Submodule update complete."
echo "Next: ./scripts/sync/sync-changes.sh"
