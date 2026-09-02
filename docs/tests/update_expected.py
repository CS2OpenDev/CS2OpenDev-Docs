#!/usr/bin/env python3
"""Rewrite docs/tests/expected/ from the committed fixture.

Run after an intentional change to the generator's output, then read the diff
before committing it: that diff is the review surface for every rendering
change.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _gen import EXPECTED, FIXTURE, gd  # noqa: E402


def main() -> int:
    if EXPECTED.is_dir():
        shutil.rmtree(EXPECTED)
    EXPECTED.mkdir(parents=True)
    code = gd.main([
        "--repo-root", str(FIXTURE),
        "--artifacts-root", str(FIXTURE / "artifacts"),
        "--build", "9000001",
        "--platform", "windows-x86_64",
        "--output", str(EXPECTED),
    ])
    if code != 0:
        print(f"generator exited {code}; expected/ may be incomplete", file=sys.stderr)
        return code
    files = sum(1 for p in EXPECTED.rglob("*") if p.is_file())
    total = sum(p.stat().st_size for p in EXPECTED.rglob("*") if p.is_file())
    print(f"wrote {files} files ({total // 1024} KiB) to {EXPECTED}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
