#!/usr/bin/env python3
"""Compatibility entry point; all indexes use the canonical builder."""

import runpy
from pathlib import Path
import sys

scripts_dir = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(scripts_dir))
runpy.run_path(str(scripts_dir / "rebuild-documentation-indexes.py"), run_name="__main__")
