"""Import ``docs/generate_docs.py`` as the module ``gd``.

The generator is a script, not a package, and lives one directory up.  Loading
it by path keeps the tests runnable from any working directory and under both
pytest and ``python3 -m unittest``.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

GENERATOR = Path(__file__).resolve().parent.parent / "generate_docs.py"
FIXTURE = Path(__file__).resolve().parent / "fixture"
EXPECTED = Path(__file__).resolve().parent / "expected"

_spec = importlib.util.spec_from_file_location("cs2docs_generator", GENERATOR)
assert _spec and _spec.loader
gd = importlib.util.module_from_spec(_spec)
sys.modules["cs2docs_generator"] = gd
_spec.loader.exec_module(gd)
