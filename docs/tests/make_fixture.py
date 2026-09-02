#!/usr/bin/env python3
"""Cut docs/tests/fixture/ out of a real SchemaTracker artifact set.

The fixture is committed, so this only has to run when the cases it covers
change.  It keeps, deliberately:

* both variants of every class on the ``CCSPlayerPawn`` / ``C_CSPlayerPawn``
  primary-parent spines down to ``CEntityInstance`` (the twin resolution case)
* one nested ``A::B`` class (link regex, mermaid quoting, filename mapping)
* one enum with overlay member annotations and one with a negative value under
  an unsigned underlying type
* three proto files, one of which (``demo.proto``) has nested messages and
  nested enums, plus one import that is *not* in the set
* five game events including a name that occurs in two sources
* convars and commands whose descriptions carry newlines, pipes and
  ``<placeholder>`` tokens
* the overlay entries that apply, including two keys that resolve to nothing

Usage:
    python3 docs/tests/make_fixture.py \\
        --artifacts-root ./upstream/schema-tracker/artifacts \\
        --build 25000182 --platform windows-x86_64
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixture"
BUILD_ID = "9000001"
PLATFORM = "windows-x86_64"

SPINE_ROOTS = ["CCSPlayerPawn", "C_CSPlayerPawn"]
EXTRA_CLASSES = [
    "CBoneConstraintPoseSpaceBone",          # nested type parent
    "CBoneConstraintPoseSpaceBone::Input_t",  # the A::B name itself
    "CGameSceneNode",                         # a run of bitfields at one offset
]
KEEP_ENUMS = ["SolidType_t", "MoveType_t", "LifeState_t", "BloodType",
              "AnimScriptType"]  # BloodType: negative value under uint32_t
KEEP_PROTOS = ["demo.proto", "gameevents.proto", "networkbasetypes.proto"]
KEEP_EVENTS = ["player_death", "round_end", "bomb_planted", "weapon_fire", "player_jump"]
KEEP_CONVARS = [
    "bot_prefix", "mp_roundtime", "sv_cheats", "mp_friendlyfire",
    "cl_showfps", "mp_maxrounds", "host_timescale", "sv_gravity",
]
KEEP_COMMANDS = ["bind", "kick", "map", "changelevel", "bot_stop", "help"]


def _closure(by_name: dict[str, list[dict]], roots: list[str]) -> set[str]:
    """All class names reachable from *roots* through every variant's parents."""
    seen: set[str] = set()
    stack = list(roots)
    while stack:
        name = stack.pop()
        if name in seen:
            continue
        seen.add(name)
        for rec in by_name.get(name, []):
            for parent in rec.get("parents", []):
                pname = parent.get("name", "")
                if pname and pname not in seen:
                    stack.append(pname)
    return seen


def build_entity_schema(src: Path, dst: Path) -> dict[str, list[str]]:
    data = json.loads(src.read_text(encoding="utf-8"))
    by_name: dict[str, list[dict]] = {}
    for c in data.get("classes", []):
        by_name.setdefault(c["name"], []).append(c)

    keep = _closure(by_name, SPINE_ROOTS)
    keep |= {n for n in EXTRA_CLASSES if n in by_name}
    keep |= _closure(by_name, [n for n in EXTRA_CLASSES if n in by_name])

    classes = [c for c in data.get("classes", []) if c["name"] in keep]
    enums = [e for e in data.get("enums", []) if e["name"] in KEEP_ENUMS]
    out = {"classes": classes, "enums": enums}
    for extra in ("schemaVersion", "buildId"):
        if extra in data:
            out[extra] = data[extra]
    dst.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    return {"classes": sorted(keep), "enums": [e["name"] for e in enums]}


def build_descriptorset(src: Path, dst: Path) -> None:
    from google.protobuf import descriptor_pb2

    fds = descriptor_pb2.FileDescriptorSet.FromString(src.read_bytes())
    out = descriptor_pb2.FileDescriptorSet()
    for f in fds.file:
        if f.name in KEEP_PROTOS:
            out.file.add().CopyFrom(f)
    dst.write_bytes(out.SerializeToString())


def _pick(records: list[dict], names: list[str], key: str = "name") -> list[dict]:
    index = {r.get(key): r for r in records}
    return [index[n] for n in names if n in index]


def build_convars(src: Path, dst: Path) -> None:
    data = json.loads(src.read_text(encoding="utf-8"))
    picked = _pick(data.get("convars", []), KEEP_CONVARS)
    # One convar whose default carries a pipe, so the code-span escape is
    # exercised even if the named ones stop having one.
    for cv in data.get("convars", []):
        if "|" in (cv.get("default") or "") and cv not in picked:
            picked.append(cv)
            break
    dst.write_text(json.dumps({"convars": picked}, indent=1) + "\n", encoding="utf-8")


def build_commands(src: Path, dst: Path) -> None:
    data = json.loads(src.read_text(encoding="utf-8"))
    picked = _pick(data.get("commands", []), KEEP_COMMANDS)
    for cmd in data.get("commands", []):
        if "\n" in (cmd.get("description") or "") and cmd not in picked:
            picked.append(cmd)
            break
    dst.write_text(json.dumps({"commands": picked}, indent=1) + "\n", encoding="utf-8")


def build_gameevents(src: Path, dst: Path) -> None:
    data = json.loads(src.read_text(encoding="utf-8"))
    picked = [e for e in data.get("events", []) if e.get("name") in KEEP_EVENTS]
    dst.write_text(json.dumps({"events": picked}, indent=1) + "\n", encoding="utf-8")


def build_provenance(src: Path, dst: Path) -> None:
    prov = json.loads(src.read_text(encoding="utf-8"))
    out = {
        "buildId": BUILD_ID,
        "schemaVersion": prov.get("schemaVersion", ""),
        "cs2Build": {"schemaRevision": prov.get("cs2Build", {}).get("schemaRevision", "")},
        "steam": {"manifestCreatedUtc": "2026-08-28T00:00:00Z"},
        "tool": prov.get("tool", {}),
    }
    dst.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")


def build_content(build_dir: Path, dst_dir: Path) -> None:
    """Trimmed copies of the content-gated artifacts, a few rows each."""
    def head(data, key, n):
        if isinstance(data, dict) and isinstance(data.get(key), list):
            data[key] = data[key][:n]
        return data

    items = json.loads((build_dir / "item_definitions.json").read_text(encoding="utf-8"))
    for key, n in (("items", 6), ("paintKits", 3), ("stickerKits", 3),
                   ("musicDefinitions", 2), ("prefabs", 4), ("rarities", 3),
                   ("qualities", 3)):
        head(items, key, n)
    (dst_dir / "item_definitions.json").write_text(
        json.dumps(items, indent=1) + "\n", encoding="utf-8")

    net = json.loads((build_dir / "network_messages.json").read_text(encoding="utf-8"))
    for ch in net.get("channels", []):
        ch["messages"] = ch.get("messages", [])[:4]
    net["channels"] = net.get("channels", [])[:3]
    (dst_dir / "network_messages.json").write_text(
        json.dumps(net, indent=1) + "\n", encoding="utf-8")

    demo = json.loads((build_dir / "demo_messages.json").read_text(encoding="utf-8"))
    head(demo, "messages", 6)
    (dst_dir / "demo_messages.json").write_text(
        json.dumps(demo, indent=1) + "\n", encoding="utf-8")

    modes = json.loads((build_dir / "game_modes.json").read_text(encoding="utf-8"))
    modes["gameTypes"] = modes.get("gameTypes", [])[:1]
    modes["mapGroups"] = modes.get("mapGroups", [])[:3]
    (dst_dir / "game_modes.json").write_text(
        json.dumps(modes, indent=1) + "\n", encoding="utf-8")

    # changelog.json is kept with all-zero families: the "no changes" sentence
    # is the case that used to render a blank page.
    changelog = json.loads((build_dir / "changelog.json").read_text(encoding="utf-8"))
    (dst_dir / "changelog.json").write_text(
        json.dumps(changelog, indent=1) + "\n", encoding="utf-8")

    maps = json.loads((build_dir / "map_overviews.json").read_text(encoding="utf-8"))
    head(maps, "maps", 3)
    maps["mapNames"] = maps.get("mapNames", [])[:5]
    (dst_dir / "map_overviews.json").write_text(
        json.dumps(maps, indent=1) + "\n", encoding="utf-8")

    surf = json.loads((build_dir / "surface_properties.json").read_text(encoding="utf-8"))
    head(surf, "surfaces", 4)
    (dst_dir / "surface_properties.json").write_text(
        json.dumps(surf, indent=1) + "\n", encoding="utf-8")

    props = json.loads((build_dir / "prop_data.json").read_text(encoding="utf-8"))
    head(props, "propClasses", 3)
    head(props, "collisionGroups", 4)
    head(props, "breakableModels", 2)
    (dst_dir / "prop_data.json").write_text(
        json.dumps(props, indent=1) + "\n", encoding="utf-8")

    mods = json.loads((build_dir / "modules.json").read_text(encoding="utf-8"))
    head(mods, "modules", 4)
    (dst_dir / "modules.json").write_text(
        json.dumps(mods, indent=1) + "\n", encoding="utf-8")


def build_schema_evolution(dst: Path, classes: list[str]) -> None:
    """A small synthetic evolution artifact covering the fixture's classes."""
    a, b = classes[0], classes[1] if len(classes) > 1 else classes[0]
    evolution = {
        "platform": PLATFORM,
        "schemaVersion": "0.8.0",
        "baselineBuild": "8999999",
        "latestBuild": BUILD_ID,
        "transitions": [
            {
                "fromBuild": "8999999",
                "toBuild": "9000000",
                "fromManifestCreatedUtc": "2026-08-01T00:00:00Z",
                "toManifestCreatedUtc": "2026-08-14T00:00:00Z",
                "classAdded": [a],
                "classRemoved": [],
                "classChanged": [
                    {
                        "name": b,
                        "fieldOps": [
                            {"kind": "ADD", "field": "m_flFixtureOne"},
                            {"kind": "OFFSET_CHANGE", "field": "m_iHealth"},
                        ],
                        "resize": {"from": "1000", "to": "1008"},
                    }
                ],
                "classPairCandidates": [],
                "fieldMoveCandidates": [],
            },
            {
                "fromBuild": "9000000",
                "toBuild": BUILD_ID,
                "fromManifestCreatedUtc": "2026-08-14T00:00:00Z",
                "toManifestCreatedUtc": "2026-08-28T00:00:00Z",
                "classAdded": [],
                "classRemoved": [],
                "classChanged": [],
            },
        ],
        "fieldHistory": [
            {
                "className": b,
                "field": "m_iHealth",
                "firstSeenBuild": "8999999",
                "lastSeenBuild": BUILD_ID,
                "typeHistory": [{"build": "8999999", "type": "int32"}],
            }
        ],
        "enumHistory": [
            {
                "enumName": "SolidType_t",
                "firstSeenBuild": "8999999",
                "lastSeenBuild": BUILD_ID,
            }
        ],
    }
    dst.write_text(json.dumps(evolution, indent=1) + "\n", encoding="utf-8")


def build_overlays(repo_root: Path, dst_dir: Path, kept: dict[str, list[str]]) -> None:
    import yaml

    src = repo_root / "docs" / "overlays"
    keep_names = set(kept["classes"]) | set(kept["enums"])

    server = yaml.safe_load((src / "server.yml").read_text(encoding="utf-8")) or {}
    trimmed = {k: v for k, v in server.items() if k in keep_names}
    # One entry that resolves to nothing, so the validator has something to
    # report in the tests.
    trimmed["CClassThatWasRemoved"] = {"description": "Gone from this build."}
    (dst_dir / "server.yml").write_text(
        yaml.safe_dump(trimmed, sort_keys=True, allow_unicode=True, width=100),
        encoding="utf-8",
    )

    gt = yaml.safe_load((src / "globaltypes.yml").read_text(encoding="utf-8")) or {}
    (dst_dir / "globaltypes.yml").write_text(
        yaml.safe_dump({k: v for k, v in gt.items() if k in keep_names},
                       sort_keys=True, allow_unicode=True, width=100),
        encoding="utf-8",
    )

    ge = yaml.safe_load((src / "gameevents.yml").read_text(encoding="utf-8")) or {}
    events = {k: v for k, v in (ge.get("events") or {}).items() if k in KEEP_EVENTS}
    (dst_dir / "gameevents.yml").write_text(
        yaml.safe_dump({"description": ge.get("description", ""), "events": events},
                       sort_keys=True, allow_unicode=True, width=100),
        encoding="utf-8",
    )

    wkc = yaml.safe_load(
        (src / "well_known_constants.yml").read_text(encoding="utf-8")
    ) or {}
    (dst_dir / "well_known_constants.yml").write_text(
        yaml.safe_dump({"constants": (wkc.get("constants") or [])[:2]},
                       sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )

    (dst_dir / "schema-lens.yml").write_text(
        "description: Fixture schema-lens overlay.\n"
        "notes: |\n"
        "  Two lines, so the blockquote continuation is covered.\n"
        "  Second line.\n"
        "confirmed_renames:\n"
        "  - class: CBaseEntity\n"
        "    from: m_iOldHealth\n"
        "    to: m_iHealth\n"
        "    note: Renamed in the fixture's synthetic transition.\n",
        encoding="utf-8",
    )

    proto_dst = dst_dir / "protobufs"
    proto_dst.mkdir(parents=True, exist_ok=True)
    for stem in (p.removesuffix(".proto") for p in KEEP_PROTOS):
        cand = src / "protobufs" / f"{stem}.yml"
        if cand.is_file():
            shutil.copy2(cand, proto_dst / cand.name)
    if not any(proto_dst.iterdir()):
        (proto_dst / "demo.yml").write_text(
            "description: Demo-file container messages.\n"
            "messages:\n"
            "  CDemoClassInfo:\n"
            "    description: Class id to network-class-name table.\n"
            "    fields:\n"
            "      classes:\n"
            "        description: One entry per network class.\n"
            "      no_such_field:\n"
            "        description: Deliberately stale, for the validator test.\n",
            encoding="utf-8",
        )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--artifacts-root", required=True)
    ap.add_argument("--build", required=True)
    ap.add_argument("--platform", default=PLATFORM)
    ap.add_argument("--repo-root", default=".")
    args = ap.parse_args(argv)

    build_dir = Path(args.artifacts_root).resolve() / args.build / args.platform
    if not (build_dir / "entity_schema.json").is_file():
        print(f"no artifact set at {build_dir}", file=sys.stderr)
        return 2

    if FIXTURE.is_dir():
        shutil.rmtree(FIXTURE)
    out_build = FIXTURE / "artifacts" / BUILD_ID / PLATFORM
    out_build.mkdir(parents=True)
    (FIXTURE / "artifacts" / "schema_evolution").mkdir(parents=True)
    overlays_dir = FIXTURE / "docs" / "overlays"
    overlays_dir.mkdir(parents=True)

    kept = build_entity_schema(
        build_dir / "entity_schema.json", out_build / "entity_schema.json"
    )
    build_descriptorset(
        build_dir / "protos.descriptorset", out_build / "protos.descriptorset"
    )
    proto_src = build_dir / "protos"
    proto_dst = out_build / "protos"
    proto_dst.mkdir()
    for name in KEEP_PROTOS:
        if (proto_src / name).is_file():
            shutil.copy2(proto_src / name, proto_dst / name)
    build_convars(build_dir / "convars.json", out_build / "convars.json")
    build_commands(build_dir / "commands.json", out_build / "commands.json")
    build_gameevents(build_dir / "gameevents.json", out_build / "gameevents.json")
    build_provenance(build_dir / "provenance.json", out_build / "provenance.json")
    build_content(build_dir, out_build)
    build_schema_evolution(
        FIXTURE / "artifacts" / "schema_evolution" / f"{PLATFORM}.json",
        kept["classes"],
    )
    build_overlays(Path(args.repo_root).resolve(), overlays_dir, kept)

    total = sum(p.stat().st_size for p in FIXTURE.rglob("*") if p.is_file())
    print(f"fixture written to {FIXTURE} "
          f"({len(kept['classes'])} classes, {len(kept['enums'])} enums, "
          f"{total // 1024} KiB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
