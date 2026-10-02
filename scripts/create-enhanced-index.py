#!/usr/bin/env python3
"""Compatibility entry point; all indexes use the canonical builder."""

import runpy
from pathlib import Path

runpy.run_path(str(Path(__file__).with_name("rebuild-documentation-indexes.py")), run_name="__main__")
