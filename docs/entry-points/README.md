# Entry points

- `BUSINESS_PROCESS_MAP.md`: find a MaKo process from a business goal.
- `AI_AGENT_SETUP.md`: implement a known Prüfi or trigger.
- `PROCESS_GRAPH.json`: source discovery by `indexes.by_bdew_id`, `by_trigger`, `by_process_name`, and `by_path`. Its paths point to both the new `docs-offline/` mirror and `docs-supplemental/`. It contains no inferred process branches.

Start with the new versioned process view in `docs-offline/prozessdoku/<format-version>/`. Read a matching old Mermaid page in `docs-supplemental/` for conditional or parallel flow when available. Verify implementation fields with the API schema, AHB and test files for the same applicable format version.

The source indexes are `docs/dokumentation/llms.txt` and `docs/dokumentation/llms-index.txt` for the new site, and `docs-supplemental/llm.txt` for the older site. Rebuild all local lookup indexes with `python3 scripts/rebuild-documentation-indexes.py`.
