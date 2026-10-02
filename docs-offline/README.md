# New Conuti documentation mirror

This directory mirrors 3,447 Strom and shared Markdown pages from `https://dokumentation.macoapp.de/llms-index.txt`. Gas-specific pages are excluded. Page paths preserve the site path; for example, `prozessdoku/202604/LF--LFN/GPKE-Teil2-lieferbeginn.md` corresponds to the same path on the site.

Use `docs/dokumentation/llms.txt` for a curated overview, `docs/dokumentation/llms-index.txt` for every page, or `index.json` for exact local path to URL lookup. `enhanced-index.json` offers Prüfi, trigger, and process-name lookup. The site's versioned trigger OpenAPI files are mirrored under `apis/`. `docs/entry-points/PROCESS_GRAPH.json` combines this mirror with `docs-supplemental/`.

These pages contain MDX components and, for process pages, embedded SVG system diagrams. A `.md` twin is an offline source document, not plain Markdown rendering. The SVGs must not be treated as evidence of conditional process order unless the conditions are also stated in text or regulation.

Refresh with `./scripts/download-dokumentation.sh`, then rebuild indexes with `python3 scripts/rebuild-documentation-indexes.py`.
