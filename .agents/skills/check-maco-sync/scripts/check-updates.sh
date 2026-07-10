#!/bin/bash
# Full MaCo workspace update check: version tracker, remote git, docs-offline, llm.txt.
# Run from workspace root or any directory (script resolves paths).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_ROOT="$(cd "$SKILL_DIR/../../.." && pwd)"
SYNC_DIR="$WORKSPACE_ROOT/scripts/sync"
VERSION_TRACKER="$SYNC_DIR/version-tracker.json"
LLM_LOCAL="$WORKSPACE_ROOT/docs/llm.txt"
LLM_URL="${MACO_DOC_INDEX_URL:-https://doc.macoapp.de/llms.txt}"

UPDATES_AVAILABLE=0
WARNINGS=0

section() {
    echo ""
    echo "━━━ $1 ━━━"
}

status_ok() { echo "  ✅ $1"; }
status_warn() { echo "  ⚠️  $1"; UPDATES_AVAILABLE=1; }
status_info() { echo "  ℹ️  $1"; }
status_crit() { echo "  🚨 $1"; UPDATES_AVAILABLE=1; }

check_git_repo() {
    local name="$1"
    local path="$WORKSPACE_ROOT/$1"

    if [ ! -d "$path" ]; then
        status_warn "$name not found at $path"
        return
    fi

    cd "$path"
    if [ ! -d ".git" ] && [ ! -f ".git" ]; then
        status_warn "$name is not a git repository"
        return
    fi

    local branch upstream behind dirty
    branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"
    upstream="$(git rev-parse --abbrev-ref "@{upstream}" 2>/dev/null || true)"
    if [ -z "$upstream" ]; then
        upstream="origin/main"
        git rev-parse --verify "$upstream" >/dev/null 2>&1 || upstream="origin/master"
    fi

    if git fetch origin --quiet 2>/dev/null; then
        status_ok "$name: fetched origin"
    else
        status_warn "$name: could not fetch origin (network or auth?)"
        WARNINGS=1
    fi

    behind="$(git rev-list --count "HEAD..$upstream" 2>/dev/null || echo "?")"
    local current_hash tracked_hash last_synced
    current_hash="$(git rev-parse HEAD)"
    tracked_hash="$(jq -r --arg n "$name" '.external_repos[$n].last_commit_hash // "null"' "$VERSION_TRACKER" 2>/dev/null || echo "null")"
    last_synced="$(jq -r --arg n "$name" '.external_repos[$n].last_synced // "unknown"' "$VERSION_TRACKER" 2>/dev/null || echo "unknown")"

    echo "  Branch: $branch ($upstream)"
    echo "  HEAD:   $current_hash"
    echo "  Tracker last synced: $last_synced"
    echo "  Tracker commit:      $tracked_hash"

    if [ "$behind" = "?" ]; then
        status_warn "$name: could not compute commits behind $upstream"
    elif [ "$behind" -gt 0 ]; then
        status_warn "$name: $behind commit(s) behind $upstream — run: cd $name && git pull"
        echo "  Incoming commits:"
        git log --oneline "HEAD..$upstream" | head -5 | sed 's/^/    /'
        local more=$((behind - 5))
        if [ "$more" -gt 0 ]; then
            echo "    ... and $more more"
        fi
    else
        status_ok "$name: up to date with remote"
    fi

    if [ "$tracked_hash" != "null" ] && [ "$current_hash" != "$tracked_hash" ]; then
        status_warn "$name: local HEAD differs from version-tracker (pulled but not synced?)"
        echo "  Changed since last sync:"
        git diff --name-only "$tracked_hash" HEAD | head -15 | sed 's/^/    /'
        local changed_count
        changed_count="$(git diff --name-only "$tracked_hash" HEAD | wc -l | tr -d ' ')"
        if [ "$changed_count" -gt 15 ]; then
            echo "    ... and $((changed_count - 15)) more"
        fi
        if [ "$name" = "maco-api-documentation" ]; then
            if git diff --name-only "$tracked_hash" HEAD | grep -q "scripts/build-openapi-json.sh"; then
                status_crit "$name: build script changed — run ./scripts/sync/rebuild-schemas.sh after pull"
            fi
        fi
    elif [ "$tracked_hash" = "null" ] || [ -z "$tracked_hash" ]; then
        status_info "$name: no prior commit recorded in version-tracker (first run)"
    else
        status_ok "$name: matches version-tracker commit"
    fi

    dirty="$(git status --porcelain)"
    if [ -n "$dirty" ]; then
        status_info "$name: local modifications present (workspace patches, not remote updates)"
        echo "$dirty" | head -10 | sed 's/^/    /'
        local dirty_count
        dirty_count="$(echo "$dirty" | wc -l | tr -d ' ')"
        if [ "$dirty_count" -gt 10 ]; then
            echo "    ... and $((dirty_count - 10)) more"
        fi
    fi
}

check_docs_offline() {
    local file_count last_count last_synced
    if [ ! -d "$WORKSPACE_ROOT/docs-offline" ]; then
        status_warn "docs-offline not found"
        return
    fi

    file_count="$(find "$WORKSPACE_ROOT/docs-offline" -name "*.md" | wc -l | tr -d ' ')"
    last_count="$(jq -r '."external_repos"."docs-offline".file_count // 0' "$VERSION_TRACKER" 2>/dev/null || echo "0")"
    last_synced="$(jq -r '."external_repos"."docs-offline".last_synced // "unknown"' "$VERSION_TRACKER" 2>/dev/null || echo "unknown")"

    echo "  Markdown files: $file_count (tracker: $last_count)"
    echo "  Tracker last synced: $last_synced"

    if [ "$file_count" != "$last_count" ]; then
        status_warn "docs-offline file count changed — re-run download-docs + sync-changes"
    else
        status_ok "docs-offline file count matches tracker"
    fi
}

check_llm_txt() {
    local tmp
    tmp="$(mktemp)"
    trap 'rm -f "$tmp"' RETURN

    echo "  Remote URL: $LLM_URL"
    echo "  Local file: $LLM_LOCAL"

    if [ ! -f "$LLM_LOCAL" ]; then
        status_warn "docs/llm.txt missing — run ./scripts/fetch-llm-index.sh"
        return
    fi

    if ! curl -s -f -L "$LLM_URL" -o "$tmp" --max-time 120 --connect-timeout 30; then
        status_warn "could not fetch remote llms.txt"
        WARNINGS=1
        return
    fi

    local local_lines remote_lines local_hash remote_hash
    local_lines="$(wc -l < "$LLM_LOCAL" | tr -d ' ')"
    remote_lines="$(wc -l < "$tmp" | tr -d ' ')"
    local_hash="$(shasum -a 256 "$LLM_LOCAL" | awk '{print $1}')"
    remote_hash="$(shasum -a 256 "$tmp" | awk '{print $1}')"

    echo "  Lines: local=$local_lines remote=$remote_lines"
    echo "  SHA-256 local:  $local_hash"
    echo "  SHA-256 remote: $remote_hash"

    if cmp -s "$LLM_LOCAL" "$tmp"; then
        status_ok "docs/llm.txt matches remote llms.txt"
    else
        status_warn "docs/llm.txt differs from remote — run ./scripts/fetch-llm-index.sh"
        echo "  Diff preview (first 20 lines):"
        diff "$LLM_LOCAL" "$tmp" | head -20 | sed 's/^/    /' || true
    fi
}

echo "🔍 MaCo workspace update check"
echo "Workspace: $WORKSPACE_ROOT"

section "Version tracker"
if [ -f "$VERSION_TRACKER" ]; then
    jq -r '.external_repos | to_entries[] | "  \(.key): last_synced=\(.value.last_synced // "n/a")"' "$VERSION_TRACKER"
else
    status_warn "version-tracker.json not found at $VERSION_TRACKER"
fi

section "Git submodules / external repos"
check_git_repo "maco-api-documentation"
check_git_repo "maco-edi-testfiles"
check_git_repo "ebd-diagrams"

section "Reference data (AHB + EBD)"
if [ -d "$WORKSPACE_ROOT/ahb-tables" ] || [ -d "$WORKSPACE_ROOT/ebd-diagrams" ]; then
    if python3 "$SYNC_DIR/reference-data-status.py" check; then
        status_ok "ahb-tables and ebd-diagrams reference data look current"
    else
        status_warn "ahb-tables and/or ebd-diagrams need refresh — see output above"
    fi
else
    status_warn "ahb-tables/ and/or ebd-diagrams/ not found"
fi

section "docs-offline"
check_docs_offline

section "docs/llm.txt (portal index)"
check_llm_txt

section "Summary"
if [ "$UPDATES_AVAILABLE" -eq 0 ] && [ "$WARNINGS" -eq 0 ]; then
    echo "  ✅ Everything checked is up to date."
    echo ""
    echo "Apply workflow (only if you pull or fetch changes later):"
    echo "  ./scripts/sync/sync-changes.sh"
    echo "  python3 scripts/sync/update-process-graph-minimal.py"
    exit 0
fi

if [ "$UPDATES_AVAILABLE" -gt 0 ]; then
    echo "  ⚠️  Updates or drift detected — see sections above."
fi
if [ "$WARNINGS" -gt 0 ]; then
    echo "  ⚠️  Some checks could not complete (network/auth)."
fi
echo ""
echo "Typical apply sequence:"
echo "  cd maco-api-documentation && git pull && cd .."
echo "  cd maco-edi-testfiles && git pull && cd .."
echo "  cd ebd-diagrams && git pull && cd .."
echo "  python3 scripts/download-ahb-tables.py && python3 scripts/generate-ahb-index.py  # if AHB drift"
echo "  ./scripts/fetch-llm-index.sh          # if llm.txt differed"
echo "  ./scripts/download-docs.sh            # if llm.txt or docs-offline need refresh"
echo "  ./scripts/sync/rebuild-schemas.sh     # if maco-api build script changed"
echo "  python3 scripts/sync/update-process-graph-minimal.py"
echo "  ./scripts/sync/sync-changes.sh"
exit 1
