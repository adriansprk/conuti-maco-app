#!/usr/bin/env python3
"""Regression checks for documentation scope, canonical Prüfis and selection."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))
from documentation_scope import filter_index, is_gas


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load_script("rebuild-documentation-indexes")
finder = load_script("find-documentation")


class DiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads((ROOT / "docs/entry-points/PROCESS_GRAPH.json").read_text(encoding="utf-8"))

    def test_canonical_pruefi_page_is_found(self):
        for pi in ("55016", "55077"):
            for version in ("202604", "202610"):
                matches = finder.search(self.graph, "by_bdew_id", pi, version, "LF")
                self.assertTrue(any(path["path"].endswith(f"/{version}/pruefi/UTILMD/PI_{pi}.md") for path in matches))

    def test_version_and_role_filter(self):
        results = finder.search(self.graph, "by_process_name", "lieferbeginn", "202610", "LF")
        self.assertTrue(results)
        self.assertTrue(all(item["version"] == "202610" and item["role"] == "LF" for item in results))
        self.assertTrue(all("gas" not in item["path"].lower() for item in results))

    def test_gas_sources_are_not_discoverable(self):
        self.assertTrue(is_gas("prozessdoku/202610/LF/geli-gas-2-0-lieferbeginn.md"))
        self.assertFalse(is_gas("prozessdoku/202610/LF/GPKE-Teil2-lieferbeginn.md", "Strom · Sicht LF"))
        self.assertFalse(any(is_gas(path, info["title"]) for path, info in self.graph["indexes"]["by_path"].items()))

    def test_indexes_cover_exact_strom_manifest(self):
        manifest = json.loads((ROOT / "docs-offline/index.json").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest), self.graph["source_files"]["new"])
        self.assertTrue(all((ROOT / "docs-offline" / path).is_file() for path in manifest))
        self.assertTrue(all(not is_gas(path) for path in manifest))

    def test_strom_filter_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "llms-index.txt"
            index.write_text("# Index\n\n- [Strom](https://dokumentation.macoapp.de/prozesse/strom.md)\n- [Gas](https://dokumentation.macoapp.de/prozesse/gas.md)\n", encoding="utf-8")
            self.assertEqual(filter_index(index), {"prozesse/strom.md"})
            first = index.read_bytes()
            self.assertEqual(filter_index(index), {"prozesse/strom.md"})
            self.assertEqual(index.read_bytes(), first)

    def test_content_only_gas_page_is_pruned(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            indexes, mirror = base / "indexes", base / "mirror"
            indexes.mkdir()
            mirror.mkdir()
            listing = "# Index\n- [Neutral](https://dokumentation.macoapp.de/prozessdoku/202610/LF/neutral.md)\n- [Strom](https://dokumentation.macoapp.de/prozessdoku/202610/LF/strom.md)\n"
            for name in ("llms.txt", "llms-index.txt"):
                (indexes / name).write_text(listing, encoding="utf-8")
            page = mirror / "prozessdoku/202610/LF/neutral.md"
            page.parent.mkdir(parents=True)
            page.write_text('# Neutral\n<Kopf rolle="LF" sparte="Gas" />\n', encoding="utf-8")
            (page.parent / "strom.md").write_text('# Strom\n<Kopf rolle="LF" sparte="Strom" />\n', encoding="utf-8")
            subprocess.run([sys.executable, str(SCRIPTS / "documentation_scope.py"),
                            "--index-dir", str(indexes), "--mirror-dir", str(mirror), "--prune"],
                           check=True, capture_output=True, text=True)
            self.assertFalse(page.exists())
            self.assertNotIn("neutral.md", (indexes / "llms-index.txt").read_text(encoding="utf-8"))

    def test_content_only_legacy_gas_page_is_pruned(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            page = base / "neutral.md"
            page.write_text('# Neutral\n<Kopf rolle="LF" sparte="Gas" />\n', encoding="utf-8")
            index = base / "llm.txt"
            index.write_text('# Old\n- [Neutral](https://doc.macoapp.de/neutral.md)\n', encoding="utf-8")
            subprocess.run([sys.executable, str(SCRIPTS / "documentation_scope.py"),
                            "--legacy-index", str(index), "--legacy-dir", str(base)],
                           check=True, capture_output=True, text=True)
            self.assertFalse(page.exists())
            self.assertNotIn("neutral.md", index.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
