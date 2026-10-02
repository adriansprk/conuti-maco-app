# Older documentation supplement

This is the preserved offline snapshot of `doc.macoapp.de`. It is a comparison and supplement to the primary `dokumentation.macoapp.de` mirror in `docs-offline/`.

The old snapshot remains because its Mermaid sequence diagrams explicitly express optional, alternative, and parallel branches that the new process system diagrams do not necessarily encode. The `prozessdiagramme-png/` directory records implementation architecture. This snapshot also contains interface change history, authentication and error guidance, and format-change comparisons. Other old pages remain available until their equivalence to the new site has been checked; their presence here does not make them the current authority.

At migration, this folder holds 363 Markdown pages: 69 contain Mermaid and 79 contain embedded OpenAPI (these groups overlap), plus 54 architecture PNGs. The full prior snapshot is retained to avoid deleting a unique detail based on a title match alone. Page-level deduplication can follow a source comparison; the primary indexes already rank new process views first.

Use `llm.txt` to browse this source and `index.json` or `enhanced-index.json` for local lookup. The combined `docs/entry-points/PROCESS_GRAPH.json` labels these pages `supplemental`. Check the format version of any claim before using it for implementation.

Refresh only this supplement with `./scripts/download-docs.sh` and rebuild all indexes with `python3 scripts/rebuild-documentation-indexes.py`.
