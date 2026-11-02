#!/usr/bin/env python3
"""Propose classname -> schema class pairs for docs/overlays/entity_classnames.yml.

Hammer classnames (``func_button``) and server schema classes (``CBaseButton``)
are joined in the game by ``CEntityClass::m_designerName``, which no artifact
carries yet (SchemaTracker issue #35).  Until it does, the overlay is curated by
hand, and this script does the first pass: for every placeable FGD class it
tries a fixed list of spellings against the server classes that descend from
``CBaseEntity`` and prints the hits as YAML for a human to review.

It never writes the overlay itself and nothing in the generator calls it.

    python3 docs/tools/seed_entity_classnames.py \
      --artifacts-root ./upstream/schema-tracker/artifacts > candidates.yml
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_docs as gd  # noqa: E402


def _server_entity_classes(entities: dict[str, dict]) -> dict[str, str]:
    """Lower-cased name -> name for server classes that descend from CBaseEntity."""
    server: dict[str, dict] = {}
    for name in entities:
        for v in gd._all_variants(name, entities):
            if v.get("module") == "server" and v.get("kind") == "class":
                server[name] = v
    memo: dict[str, bool] = {}

    def is_entity(name: str, depth: int = 0) -> bool:
        if name == "CBaseEntity":
            return True
        if name in memo:
            return memo[name]
        memo[name] = False
        v = server.get(name)
        if v is None or depth > 64:
            return False
        memo[name] = any(is_entity(b, depth + 1) for b in v.get("bases") or [])
        return memo[name]

    return {n.lower(): n for n in server if is_entity(n)}


def _candidates(classname: str) -> list[tuple[str, str]]:
    """(rule, lower-cased spelling) pairs, most specific first."""
    tokens = [t for t in classname.lower().split("_") if t]
    whole = "".join(tokens)
    rest = "".join(tokens[1:])
    out = [
        ("C+name", "c" + whole),
        ("CCS+name", "ccs" + whole),
        ("C+name+Entity", "c" + whole + "entity"),
        ("CCS+name+Entity", "ccs" + whole + "entity"),
    ]
    if len(tokens) == 2:
        out.append(("C+reversed", "c" + tokens[1] + tokens[0]))
    if rest:
        out += [
            ("C+rest", "c" + rest),
            ("CCS+rest", "ccs" + rest),
            ("CBase+rest", "cbase" + rest),
        ]
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--artifacts-root", required=True)
    ap.add_argument("--build", default="latest")
    ap.add_argument("--platform", default="windows-x86_64")
    args = ap.parse_args(argv)

    build_dir = gd.resolve_build_dir(Path(args.artifacts_root), args.build, args.platform)
    if build_dir is None:
        print("ERROR: no build found", file=sys.stderr)
        return 2
    entity_io = gd._load_content_json(build_dir, "entity_io.json")
    if not entity_io:
        print(f"ERROR: {build_dir} has no entity_io.json", file=sys.stderr)
        return 2
    by_lower = _server_entity_classes(gd.load_entity_schema(build_dir))

    hits: list[tuple[str, str, str]] = []
    misses: list[str] = []
    for cls in entity_io.get("classes", []):
        if cls.get("isBase"):
            continue
        name = cls["name"]
        for rule, spelling in _candidates(name):
            if spelling in by_lower:
                hits.append((name, by_lower[spelling], rule))
                break
        else:
            misses.append(name)

    print(f"# {len(hits)} candidate(s), {len(misses)} classname(s) with no match.")
    print("# Review every line before copying it into docs/overlays/entity_classnames.yml.")
    print("classnames:")
    for name, cls, rule in hits:
        print(f"  {name}: {{class: {cls}, module: server}}  # {rule}")
    print("# No candidate:")
    for name in misses:
        print(f"#   {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
