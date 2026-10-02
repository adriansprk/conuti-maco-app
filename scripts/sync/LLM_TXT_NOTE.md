# Documentation index sources

The new and older portals have separate indexes:

| Portal | Local index | Offline pages | Refresh |
|---|---|---|---|
| `dokumentation.macoapp.de` | `docs/dokumentation/llms.txt`, `llms-index.txt` | `docs-offline/<site-path>.md` | `./scripts/download-dokumentation.sh` |
| `doc.macoapp.de` | `docs-supplemental/llm.txt` | `docs-supplemental/*.md` | `./scripts/download-docs.sh` |

The locally scoped new-site index lists 3,447 Strom/shared Markdown twins in two format versions. The mirror preserves each URL path and excludes Gas-specific pages. The old site's `llm.txt` remains separate because its Mermaid and operational content is supplementary. `./scripts/fetch-llm-index.sh` refreshes only the old Strom-scoped index.

After either source changes, run `python3 scripts/rebuild-documentation-indexes.py`. This rebuilds both local indexes and the combined `docs/entry-points/PROCESS_GRAPH.json`. The graph only points to sources; it never reconstructs branches from SVG layout.
