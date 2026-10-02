# Documentation sources

The Strom-scoped Conuti documentation mirror is the primary process and interface reference. Gas-specific pages are excluded from the new mirror, both local indexes, and the older supplemental snapshot. The older `doc.macoapp.de` export is retained separately for applicable diagrams, historical material, and comparison.

| Source | Index | Offline pages | Use |
|---|---|---|---|
| New site | `docs/dokumentation/llms.txt` (curated) and `llms-index.txt` (Strom/shared pages) | `docs-offline/<site-path>.md` | Versioned process views, Prüfis, EBDs, trigger events, BO4E reference |
| Older site | `docs-supplemental/llm.txt` | `docs-supplemental/*.md` | Mermaid branches, PNG architecture diagrams, operational and historical pages |

For a process, use `python3 scripts/find-documentation.py --process lieferbeginn --version 202610 --role LF` (or `--pi` / `--trigger`). Use `--perspective LFN` or `LFA` to narrow supplier views and `--include-supplemental` when older branch detail is needed. The graph's indexes contain paths to both sources; each `by_path` entry records source, format version, industry, role, participant view, and document type. Read the source page before describing a process.

The new site's system diagrams are embedded SVGs. They show actors and operations but do not reliably encode all regulatory `opt`, `alt`, or `par` conditions. Keep the legacy Mermaid sequence diagrams available for those conditions and check the BDEW source when interpreting them. SVG-to-Mermaid conversion is a separate, source-verified job.

Refresh and rebuild:

```bash
./scripts/download-dokumentation.sh
python3 scripts/rebuild-documentation-indexes.py
python3 scripts/rebuild-documentation-indexes.py --check
python3 scripts/test-documentation-discovery.py
```

The older portal can still be refreshed with `./scripts/download-docs.sh`; it writes only to `docs-supplemental/`. Its index remains separate from the new site's indexes.
