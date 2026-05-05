# llm.txt Source and Workflow

## Source

**Canonical portal index (live):** `https://doc.macoapp.de/llms.txt` (HTTP 200, stable path).

The workspace copy **`docs/llm.txt`** is the same content saved locally for scripts (`grep`, offline use). It is **not** part of the `maco-api-documentation` submodule.

## Fetch behaviour

**`scripts/download-docs.sh`** runs **`scripts/fetch-llm-index.sh`** first by default (downloads **`llms.txt`** → **`docs/llm.txt`**), then crawls every linked `.md` URL.

**Offline / pinned index:** set **`SKIP_LLM_FETCH=1`** so the existing committed **`docs/llm.txt`** is used without network:

```bash
SKIP_LLM_FETCH=1 ./scripts/download-docs.sh
```

**Index only** (no page crawl):

```bash
./scripts/fetch-llm-index.sh
```

---

Legacy note: the index could be pasted by hand; **`fetch-llm-index.sh`** is now the normal source.

## Workflow

```
https://doc.macoapp.de/llms.txt (canonical index)
    ↓
scripts/fetch-llm-index.sh  →  docs/llm.txt   (default before download-docs; optional SKIP_LLM_FETCH=1)
    ↓
scripts/download-docs.sh
    ↓
docs-offline/*.md (downloaded markdown files)
    ↓
scripts/sync/update-process-graph-minimal.py
    ↓
PROCESS_GRAPH.json (generated)
```

## Process

1. **`docs/llm.txt`** — refreshed from **`llms.txt`** automatically when you run **`download-docs.sh`**, unless **`SKIP_LLM_FETCH=1`**.
2. **`download-docs.sh`** — extracts URLs from **`docs/llm.txt`**, downloads **`docs-offline/*.md`**.
3. **`PROCESS_GRAPH.json`** — `python3 scripts/sync/update-process-graph-minimal.py` (also from **`setup-workspace.sh`**).

## File Locations

- **`docs/llm.txt`** — copy of the portal index (`llms.txt`), workspace-local
- **`docs-offline/*.md`** — downloaded markdown files
- **`docs/entry-points/PROCESS_GRAPH.json`** — generated from markdown files + schemas

## Updating Workflow

When online documentation updates:

```bash
./scripts/download-docs.sh
python3 scripts/sync/update-process-graph-minimal.py
```

Use **`SKIP_LLM_FETCH=1`** only when you must not hit **`doc.macoapp.de`** for the index.

## Sync System

The sync system now correctly reflects that:

- ✅ `docs/llm.txt` is **NOT** part of `maco-api-documentation` repo
- ✅ It tracks **`https://doc.macoapp.de/llms.txt`** via **`fetch-llm-index.sh`** (default before doc download)
- ✅ `PROCESS_GRAPH.json` is **generated** from `docs-offline/` markdown files

## Notes

- `maco-api-documentation/README.MD` references `../llm.txt` because it expects it in the workspace root (parent directory)
- Default **`download-docs.sh`** **does** fetch the index first; use **`SKIP_LLM_FETCH=1`** for offline-only or frozen-index runs
