"""Put this directory on sys.path so ``from _gen import gd`` works under
pytest regardless of the import mode and the working directory."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
