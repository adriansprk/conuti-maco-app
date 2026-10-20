# MaCo workspace instructions

This workspace supports **Strom** supplier work. Gas-specific documentation is out of scope. Unless the user explicitly requests another format version, use **FV 202610** as the current/default version, including BO4E mappings from `bo4e-mapping/2610/`. State the applicable format version before combining process, AHB, EBD, trigger, mapping, and example evidence. If a task explicitly targets another version, use that version's matching mapping when available; never substitute `2610` for a different version or present mixed-version evidence as validated.

## Find sources

Use `python3 scripts/find-documentation.py --pi 55016 --version 202610 --role LF` for a Prüfi; replace `--pi 55016` with `--process lieferbeginn` or `--trigger START_LIEFERBEGINN` as needed. Always select a format version; default to `202610` when the user has not specified one. For FV 202610, use BO4E mappings under `bo4e-mapping/2610/`. Read the returned source pages; `docs/entry-points/PROCESS_GRAPH.json` is an index, not a source of process relationships. The new `docs-offline/` pages are the current process and interface reference. Use `--include-supplemental` only for branch details or architecture absent from the new pages, and check that the older material still applies to the selected version.

For payload requirements use the matching AHB and BO4E mapping plus PI request schema. For EBD decisions use the matching format version in `ebd-diagrams/`. Test files are examples for their own version, never proof of required fields or current behavior. Cite actual source files and mark unresolved conflicts or gaps.

## Workflows

- For a ticket-ready Prüfi brief, use `.agents/skills/bo4e-essentials/SKILL.md` and its bundled lint and evidence verifier.
- For sync checks, use `.agents/skills/check-maco-sync/SKILL.md`.
- Provide PM/Ops sections, diagrams, and field tables when the user asks for a full process or implementation brief. For a narrow lookup, answer directly with source evidence.

## Validation

After changing documentation discovery, run `python3 scripts/rebuild-documentation-indexes.py` and `bash scripts/validate-workspace.sh`. The validator checks generated indexes, Strom-only discovery, canonical Prüfi lookup, and evidence proof checks. Run it in CI to detect stale generated indexes.
