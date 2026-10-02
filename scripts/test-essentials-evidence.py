#!/usr/bin/env python3
"""Focused tests for the deterministic Essentials evidence gate."""

import hashlib
import importlib.util
import contextlib
import io
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/bo4e-essentials/scripts/verify-bo4e-essentials.py"
spec = importlib.util.spec_from_file_location("essentials_verifier", SCRIPT)
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class EvidenceTests(unittest.TestCase):
    def test_source_hash_and_exact_excerpt(self):
        with tempfile.TemporaryDirectory() as directory:
            old_root = verifier.ROOT
            verifier.ROOT = Path(directory)
            try:
                source = Path(directory) / "source.md"
                source.write_text("55016 request leads to 55017 response.\n", encoding="utf-8")
                proof = {"source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                         "source_excerpt": "55016 request leads to 55017 response."}
                reporter = verifier.Reporter()
                with contextlib.redirect_stdout(io.StringIO()):
                    verifier.check_source_proof(proof, "source.md", "test", reporter)
                self.assertFalse(reporter.failures)
                source.write_text("55016 request leads to 55018 response.\n", encoding="utf-8")
                changed = verifier.Reporter()
                with contextlib.redirect_stdout(io.StringIO()):
                    verifier.check_source_proof(proof, "source.md", "test", changed)
                self.assertTrue(any("hash changed" in item for item in changed.failures))
                self.assertTrue(any("excerpt does not occur" in item for item in changed.failures))
            finally:
                verifier.ROOT = old_root

    def test_format_version_extraction(self):
        self.assertEqual(verifier.source_version("ahb-tables/FV2610/AHB_FV2610_55016.json"), "202610")
        self.assertEqual(verifier.source_version("bo4e-mapping/2604/UTILMD_Strom.csv"), "202604")
        self.assertEqual(verifier.source_version("docs-offline/prozessdoku/202610/LF/thing.md"), "202610")


if __name__ == "__main__":
    unittest.main()
