---
name: check-maco-sync
description: >
  Check whether the MaCo workspace has upstream updates to pull or sync — git submodules
  (maco-api-documentation, maco-edi-testfiles), docs-offline drift, and docs/llm.txt against
  https://doc.macoapp.de/llms.txt. Use when the user asks to check sync status, whether there
  are updates to get, if external repos are current, or if llm.txt is stale. Runs the bundled
  check script and reports a structured verdict with apply steps. Do NOT use for applying updates
  unless the user explicitly asks to pull/sync.
triggers:
  - check sync updates
  - are there updates to get
  - is the workspace up to date
  - check maco sync
  - is llm.txt current
  - check external repos
---

# Check MaCo Sync

Read-only health check for the MaCo workspace's external inputs. Answers: **can I pull anything new, and is local tracking stale?**

Run from the workspace root (directory containing `maco-api-documentation/`, `docs/llm.txt`, `scripts/sync/`).

```bash
SKILL_DIR="${SKILL_DIR:-.agents/skills/check-maco-sync}"
"$SKILL_DIR/scripts/check-updates.sh"
```

Exit code: **0** = all checks pass; **1** = updates or drift detected.

## What gets checked

| Source | Check | Not covered by `check-changes.sh` alone |
|--------|-------|----------------------------------------|
| `maco-api-documentation` | `git fetch`, commits behind `origin`, HEAD vs `version-tracker.json`, local dirty tree | Remote behind count |
| `maco-edi-testfiles` | Same as above | Remote behind count |
| `docs-offline/` | `.md` file count vs tracker | — |
| `docs/llm.txt` | Fetch `llms.txt`, SHA-256 + byte compare | **Yes — always network-fetch** |

`scripts/sync/check-changes.sh` only compares **already-local** git state to the tracker. This skill's script also probes **remote** git and **live** `llms.txt`.

## Workflow

### Step 1 — Run the check script

```bash
.agents/skills/check-maco-sync/scripts/check-updates.sh
```

Requires: `curl`, `jq`, `git`, network access to `origin` and `doc.macoapp.de`.

### Step 2 — Interpret the report

Report sections appear in this order: version tracker → git repos → docs-offline → llm.txt → summary.

| Signal | Meaning | User action |
|--------|---------|-------------|
| `N commit(s) behind origin` | Remote has unpulled commits | `git pull` in that repo |
| `local HEAD differs from version-tracker` | Pulled but `sync-changes.sh` not run | Run sync + regenerate index |
| `build script changed` | Critical — schema build may differ | `./scripts/sync/rebuild-schemas.sh` |
| `local modifications present` | Workspace patches (expected on `maco-api-documentation`) | Informational — not an upstream update |
| `docs-offline file count changed` | Offline docs out of sync with tracker | `./scripts/download-docs.sh` then sync |
| `docs/llm.txt differs from remote` | Portal index updated online | `./scripts/fetch-llm-index.sh` |

### Step 3 — Respond to the user

Structure the answer as:

1. **Verdict** — up to date / updates available / partial (network failure)
2. **Per-source table** — repo, remote behind, tracker match, llm.txt match
3. **Apply steps** — only list commands for sources that actually need action
4. **Do not pull or overwrite** unless the user explicitly asks to apply updates

### Step 4 — Apply updates (only when requested)

Full refresh sequence after pulls:

```bash
cd maco-api-documentation && git pull && cd ..
cd maco-edi-testfiles && git pull && cd ..
./scripts/fetch-llm-index.sh
./scripts/download-docs.sh
./scripts/sync/rebuild-schemas.sh    # only if build script changed
python3 scripts/sync/update-process-graph-minimal.py
./scripts/sync/sync-changes.sh
```

Use `SKIP_LLM_FETCH=1 ./scripts/download-docs.sh` only when the index must stay pinned offline.

## Supporting files

| File | What it contains | When to load |
|------|------------------|--------------|
| `scripts/check-updates.sh` | Bundled check (remote git + llm.txt + tracker) | **Always — run in Step 1** |
| `scripts/sync/README.md` | Sync script catalogue and typical workflow | When user asks how to apply updates |
| `scripts/sync/LLM_TXT_NOTE.md` | llm.txt fetch behaviour and `SKIP_LLM_FETCH` | When llm.txt section needs detail |

Paths under `scripts/sync/` are relative to workspace root, not the skill folder.

## Exit criteria

Stop when:

- The check script has run successfully (or network failures are reported honestly)
- The user has a clear verdict and targeted next steps
- No `git pull`, `fetch-llm-index.sh`, or `download-docs.sh` was run unless explicitly requested
