#!/usr/bin/env python3
"""
CS2 site data emitter.

Reads the same CS2OpenDev-SchemaTracker artifact set generate_docs.py reads
and writes one JSON file per content family under docs/generated/data/, for
the Astro site to render. Writes no Markdown and does not touch anything
generate_docs.py owns; the entity/proto schema itself is already covered by
downstream-codegen-schemas/cs2_schema.json and is not re-emitted here.

Usage:
    python3 docs/site_data.py --repo-root . \\
        --artifacts-root ./upstream/schema-tracker/artifacts \\
        --build latest --platform windows-x86_64 --output docs

Importable:
    from site_data import emit_site_data
    emit_site_data(repo_root=".", build="latest", platform="windows-x86_64",
                    output="docs")

Dependencies: pip install pyyaml protobuf (same as generate_docs.py).
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_docs as gd  # noqa: E402  (path insert must run first)

DATA_SUBDIR = ("generated", "data")

# ---------------------------------------------------------------------------
# Small shared helpers
# ---------------------------------------------------------------------------

def _write_json(path: Path, obj: Any) -> int:
    """Write *obj* as deterministic pretty JSON. Returns bytes written.

    sort_keys handles dict ordering; every list built from a set iteration
    must already be sorted by the caller, or two runs on the same input can
    differ in list order even with sort_keys=True.
    """
    text = json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return len(text.encode("utf-8"))


def _overlay_text(v: Any) -> str:
    """Overlay block scalars end in a trailing newline; strip that only."""
    if not v:
        return ""
    return str(v).rstrip("\n")


def _prefix_of(name: str) -> str:
    """Text before the first underscore; the whole name if there is none."""
    return name.split("_", 1)[0] if "_" in name else name


def _iter_entity_variants(entities: dict[str, dict]):
    """Yield every entity record: top-level plus client/server twin duplicates.

    load_entity_schema keys by bare name and parks same-name records from a
    different module under duplicates[]; per-module totals need both.
    """
    for e in entities.values():
        yield e
        for d in e.get("duplicates", []) or []:
            yield d


# ---------------------------------------------------------------------------
# protobufs.json
# ---------------------------------------------------------------------------
#
# Qualified names are plain dotted paths (Outer.Nested.Deeper): the build's
# 40 proto files carry no `package`, so a field's type string is either a
# bare simple name (a top-level type, same file or another file) or a
# same-file dotted path down to a nested type -- verified against this
# build's descriptorset (no field references a nested type by bare name from
# outside its own message, and only one bare top-level name collides across
# files: CMsgProtoBufHeader, in two Steam-side files neither CS2 wire
# message references).

def _build_type_indexes(protos: list[dict]) -> tuple[dict, dict]:
    """Return (qualified_index, top_index).

    qualified_index: dotted qualified name -> {"kind", "file"}, every
    message/enum in the descriptor set, nested included.
    top_index: bare simple name -> list of (qualified_name, file), top-level
    types only (what a same-file or cross-file bare reference resolves
    against).
    """
    qualified_index: dict[str, dict] = {}
    top_index: dict[str, list[tuple[str, str]]] = defaultdict(list)

    def index_enum(e: dict, file_name: str, parent_qn: str | None) -> None:
        qn = f"{parent_qn}.{e['name']}" if parent_qn else e["name"]
        qualified_index.setdefault(qn, {"kind": "enum", "file": file_name})
        if parent_qn is None:
            top_index[e["name"]].append((qn, file_name))

    def index_msg(m: dict, file_name: str, parent_qn: str | None) -> None:
        qn = f"{parent_qn}.{m['name']}" if parent_qn else m["name"]
        qualified_index.setdefault(qn, {"kind": "message", "file": file_name})
        if parent_qn is None:
            top_index[m["name"]].append((qn, file_name))
        for nm in m.get("nested", []):
            index_msg(nm, file_name, qn)
        for ne in m.get("enums", []):
            index_enum(ne, file_name, qn)

    for p in protos:
        for m in p.get("messages", []):
            index_msg(m, p["filename"], None)
        for e in p.get("enums", []):
            index_enum(e, p["filename"], None)

    return qualified_index, dict(top_index)


def _resolve_field_type(
    raw: str, current_file: str, qualified_index: dict, top_index: dict
) -> tuple[str, str, str | None]:
    """Return (type_kind, type, type_file) for a field's raw type string.

    type_kind is "scalar", "message", "enum", or "unknown" (a name outside
    this build's descriptor set -- none observed on this build, kept as a
    safety net for future builds).
    """
    if raw in gd._PROTO_PRIMITIVES:
        return "scalar", raw, None
    if "." in raw:
        hit = qualified_index.get(raw)
        if hit:
            return hit["kind"], raw, hit["file"]
        return "unknown", raw, None
    cands = top_index.get(raw)
    if not cands:
        return "unknown", raw, None
    for qn, f in cands:
        if f == current_file:
            return qualified_index[qn]["kind"], qn, f
    qn, f = sorted(cands)[0]  # deterministic tie-break on the one known collision
    return qualified_index[qn]["kind"], qn, f


# Wire-id join rules: enum constant name -> candidate protobuf message name.
# Verified against this build's descriptorset (see A3 summary for the
# per-enum hit rates). Enums outside this list were checked with a generic
# prefix-strip + "C"/"CMsg" fallback and produced zero matches -- they are
# Steam/GC-internal message tables whose naming isn't derivable from this
# repo's data, so they are deliberately left unjoined rather than guessed.
_WIRE_ID_RULES: dict[str, tuple[str, Any, set[str]]] = {
    "NET_Messages":           ("net_",   lambda s: "CNETMsg_" + s, set()),
    "CLC_Messages":           ("clc_",   lambda s: "CCLCMsg_" + s, set()),
    "SVC_Messages":           ("svc_",   lambda s: "CSVCMsg_" + s, set()),
    "EBaseUserMessages":      ("UM_",    lambda s: "CUserMessage" + s, set()),
    "ECstrike15UserMessages": ("CS_UM_", lambda s: "CCSUsrMsg_" + s, set()),
    # DEM_Error/-Max/-IsCompressed are sentinel/flag values, not message ids.
    "EDemoCommands":          ("DEM_",   lambda s: "CDemo" + s, {"Error", "Max", "IsCompressed"}),
    "ETEProtobufIds":         ("TE_",    lambda s: "CMsgTE" + (s[:-2] if s.endswith("Id") else s), set()),
    "EBaseGameEvents":        ("GE_",    lambda s: "CMsg" + s, set()),
    "ECsgoGameEvents":        ("GE_",    lambda s: "CMsg" + (s[:-2] if s.endswith("Id") else s), set()),
}


def _wire_id_rows(protos: list[dict]) -> list[dict]:
    """Every (enum, constant, value, candidate message name) from the rules
    above, whether or not the candidate exists in this build's messages --
    callers decide what "unresolved" means for their output."""
    out: list[dict] = []
    for p in protos:
        for e in p.get("enums", []):
            rule = _WIRE_ID_RULES.get(e["name"])
            if not rule:
                continue
            prefix, transform, skip = rule
            for v in e["values"]:
                const = v["name"]
                if not const.startswith(prefix):
                    continue
                stem = const[len(prefix):]
                if stem in skip:
                    continue
                out.append({
                    "enum": e["name"],
                    "constant": const,
                    "value": int(v["number"]),
                    "candidate": transform(stem),
                })
    return out


def build_protobufs(protos: list[dict], overlays: dict[str, dict]) -> dict:
    qualified_index, top_index = _build_type_indexes(protos)
    top_level_message_names = {m["name"] for p in protos for m in p.get("messages", [])}

    wire_hits: dict[str, list[dict]] = defaultdict(list)
    for row in _wire_id_rows(protos):
        if row["candidate"] in top_level_message_names:
            wire_hits[row["candidate"]].append({
                "enum": row["enum"], "constant": row["constant"], "value": row["value"],
            })

    referenced_by: dict[str, set[str]] = defaultdict(set)
    files_out: list[dict] = []

    for p in protos:
        stem = Path(p["filename"]).stem
        overlay = overlays.get(f"protobufs/{stem}", {}) or {}
        overlay_msgs = overlay.get("messages", {}) if isinstance(overlay.get("messages"), dict) else {}

        file_messages: list[dict] = []
        file_enums: list[dict] = []

        def emit_enum(e: dict, parent_qn: str | None) -> None:
            qn = f"{parent_qn}.{e['name']}" if parent_qn else e["name"]
            file_enums.append({
                "name": e["name"],
                "qualified": qn,
                "parent": parent_qn,
                "values": [
                    {"name": v["name"], "number": int(v["number"])}
                    for v in e.get("values", [])
                ],
            })

        def emit_msg(m: dict, parent_qn: str | None) -> None:
            qn = f"{parent_qn}.{m['name']}" if parent_qn else m["name"]
            # A nested message is keyed by its dotted path; a bare name only
            # addresses a top-level message.
            mover = overlay_msgs.get(qn)
            if not isinstance(mover, dict) and parent_qn is None:
                mover = overlay_msgs.get(m["name"])
            mover = mover if isinstance(mover, dict) else {}
            overlay_flds = mover.get("fields", {}) if isinstance(mover.get("fields"), dict) else {}

            fields_out = []
            for fld in sorted(m.get("fields", []), key=lambda f: int(f.get("number", "0"))):
                kind, resolved, tfile = _resolve_field_type(fld["type"], p["filename"], qualified_index, top_index)
                fov = overlay_flds.get(fld["name"], {})
                fov = fov if isinstance(fov, dict) else {}
                description = fov.get("description") or fld.get("comment", "") or ""
                fields_out.append({
                    "name": fld["name"],
                    "number": int(fld["number"]),
                    "label": fld.get("label", "optional"),
                    "type_kind": kind,
                    "type": resolved,
                    "type_file": tfile,
                    "default": fld.get("default", ""),
                    "description": _overlay_text(description) if fov.get("description") else description,
                    # Not populated by any current overlay (only message-level
                    # `notes` exist today); kept for forward compatibility.
                    "notes": _overlay_text(fov.get("notes")),
                })
                if kind in ("message", "enum"):
                    referenced_by[resolved].add(qn)

            file_messages.append({
                "name": m["name"],
                "qualified": qn,
                "parent": parent_qn,
                "fields": fields_out,
                "nested_messages": [f"{qn}.{nm['name']}" for nm in m.get("nested", [])],
                "nested_enums": [f"{qn}.{ne['name']}" for ne in m.get("enums", [])],
                "oneofs": m.get("oneofs", []),
                "description": _overlay_text(mover.get("description")),
                "notes": _overlay_text(mover.get("notes")),
                "wire_ids": wire_hits.get(qn, []) if parent_qn is None else [],
            })
            for nm in m.get("nested", []):
                emit_msg(nm, qn)
            for ne in m.get("enums", []):
                emit_enum(ne, qn)

        for m in p.get("messages", []):
            emit_msg(m, None)
        for e in p.get("enums", []):
            emit_enum(e, None)

        files_out.append({
            "name": p["filename"],
            "stem": stem,
            "package": p.get("package"),
            "imports": list(p.get("imports", [])),
            "description": _overlay_text(overlay.get("description")),
            "notes": _overlay_text(overlay.get("notes")),
            "messages": file_messages,
            "enums": file_enums,
        })

    types_map = {qn: info["file"] for qn, info in qualified_index.items()}
    referenced_by_out = {k: sorted(v) for k, v in referenced_by.items()}

    return {"files": files_out, "types": types_map, "referenced_by": referenced_by_out}


# ---------------------------------------------------------------------------
# convars.json / commands.json
# ---------------------------------------------------------------------------

# Problems found during the last emit_site_data call. WARNINGS are authoring
# errors: the generator prints them and fails under --strict. INFOS are
# upstream facts worth a log line and never fatal.
WARNINGS: list[str] = []
INFOS: list[str] = []


def _build_flags_legend(overlays: dict[str, dict], convars: list[dict], commands: list[dict]) -> list[dict]:
    convar_counts = Counter(f for cv in convars for f in cv["flags"])
    command_counts = Counter(f for cmd in commands for f in cmd["flags"])
    seen_flags = sorted(set(convar_counts) | set(command_counts))

    legend_overlay = overlays.get("convar_flags", {}) or {}
    descriptions = legend_overlay.get("flags", {}) if isinstance(legend_overlay.get("flags"), dict) else {}
    if not descriptions:
        WARNINGS.append("docs/overlays/convar_flags.yml did not load; flag legend has no descriptions")
    missing = [f for f in seen_flags if f not in descriptions]
    if missing:
        # A flag upstream added is not an authoring error; it renders under
        # its raw name until the overlay names it.
        INFOS.append(
            "docs/overlays/convar_flags.yml has no entry for flag(s) seen on this "
            "build, shipped with a blank description: " + ", ".join(missing)
        )

    return [
        {
            "name": f,
            "convar_count": convar_counts.get(f, 0),
            "command_count": command_counts.get(f, 0),
            "description": (descriptions.get(f, {}) or {}).get("description", "") or "",
        }
        for f in seen_flags
    ]


def build_convars(convars: list[dict], flags_legend: list[dict]) -> dict:
    out = []
    for cv in convars:
        out.append({
            "name": cv["name"],
            "default": cv["default"],
            "value_type": cv["value_type"],
            "min": gd._bound_number(cv["min_value"]) if cv["has_min"] else None,
            "max": gd._bound_number(cv["max_value"]) if cv["has_max"] else None,
            "flags": sorted(cv["flags"]),
            "help": cv["description"],
            "prefix": _prefix_of(cv["name"]),
        })
    out.sort(key=lambda c: c["name"].lower())
    return {"convars": out, "flags": flags_legend}


def build_commands(commands: list[dict], flags_legend: list[dict]) -> dict:
    out = []
    for cmd in commands:
        out.append({
            "name": cmd["name"],
            "flags": sorted(cmd["flags"]),
            "help": cmd["description"],
            "has_completion_callback": cmd["has_completion_callback"],
            "prefix": _prefix_of(cmd["name"]),
        })
    out.sort(key=lambda c: c["name"].lower())
    return {"commands": out, "flags": flags_legend}


# ---------------------------------------------------------------------------
# gameevents.json
# ---------------------------------------------------------------------------

def _gameevents_type_legend(protos: list[dict]) -> list[dict]:
    """Map each .gameevents field type to CMsgSource1LegacyGameEvent.key_t's
    `type` discriminator, derived from key_t's own field numbers (val_string
    is field 2, so its code is 1; val_uint64 is field 8, code 7; and so on),
    not from a recalled enum -- checkable straight off this build's
    descriptor."""
    key_t = None
    for p in protos:
        if p["filename"] != "gameevents.proto":
            continue
        for m in p["messages"]:
            if m["name"] != "CMsgSource1LegacyGameEvent":
                continue
            for nm in m.get("nested", []):
                if nm["name"] == "key_t":
                    key_t = nm

    codes: dict[str, int] = {}
    if key_t:
        for f in key_t["fields"]:
            if f["name"].startswith("val_"):
                codes[f["name"][len("val_"):]] = int(f["number"]) - 1

    key_t_field = {
        "string": "val_string", "float": "val_float", "long": "val_long",
        "int": "val_long", "short": "val_short", "byte": "val_byte",
        "bool": "val_bool", "uint64": "val_uint64",
    }

    legend = []
    for tname, tinfo in sorted(gd._GAMEEVENTS_TYPE_MAP.items()):
        code = None
        note = ""
        kf = key_t_field.get(tname)
        if kf:
            code = codes.get(kf[len("val_"):])
        if tname in ("none", "local"):
            code = 0
            note = "Not carried in the key_t union; type 0 means no value is sent."
        elif tname == "player_controller_and_pawn":
            note = (
                "Packs two indices into one integer: controller id in the low "
                "byte, pawn index in the bytes above it. Decode as "
                "controller_id = value & 0xFF, pawn_index = value >> 8. Not a "
                "distinct key_t code on its own."
            )
        elif tname in ("player_controller", "player_pawn", "ehandle"):
            code = codes.get("long")
            note = "Sent as a plain integer, wire-coded the same as key_t.type 3 (long)."
        legend.append({
            "type": tname,
            "description": tinfo["description"],
            "key_t_type_code": code,
            "note": note,
        })
    return legend


def build_gameevents(gameevents: list[dict], overlays: dict[str, dict], protos: list[dict]) -> dict:
    overlay = overlays.get("gameevents", {}) or {}
    overlay_events = overlay.get("events", {}) if isinstance(overlay.get("events"), dict) else {}

    name_counts = Counter(e["name"] for e in gameevents)
    duplicates: dict[str, list[str]] = defaultdict(list)
    for e in gameevents:
        if name_counts[e["name"]] > 1:
            duplicates[e["name"]].append(e["source"])

    events_out = []
    for e in gameevents:
        multi = name_counts[e["name"]] > 1
        src_stem = e["source"][: -len(".gameevents")] if e["source"].endswith(".gameevents") else e["source"]
        anchor = e["name"] if not multi else f"{e['name']}-{src_stem}"

        eov = overlay_events.get(e["name"], {})
        eov = eov if isinstance(eov, dict) else {}
        description = _overlay_text(eov.get("description")) or e["comment"]
        overlay_flds = eov.get("fields", {}) if isinstance(eov.get("fields"), dict) else {}

        fields_out = []
        for f in e["fields"]:
            fov = overlay_flds.get(f["name"], {})
            fov = fov if isinstance(fov, dict) else {}
            fdesc = _overlay_text(fov.get("description")) or f["comment"]
            fields_out.append({"name": f["name"], "type": f["type"], "description": fdesc})

        events_out.append({
            "name": e["name"],
            "source": e["source"],
            "anchor": anchor,
            "description": description,
            "notes": _overlay_text(eov.get("notes")),
            "warning": _overlay_text(eov.get("warning")),
            "properties": e["properties"],
            "fields": fields_out,
        })
    events_out.sort(key=lambda e: (e["name"].lower(), e["source"]))

    return {
        "events": events_out,
        "sources": sorted({e["source"] for e in gameevents}),
        "type_legend": _gameevents_type_legend(protos),
        "duplicates": {k: sorted(v) for k, v in duplicates.items()},
    }


# ---------------------------------------------------------------------------
# items.json / paint_kits.json / sticker_kits.json / music_kits.json
# ---------------------------------------------------------------------------

_ITEM_DISPLAY_FIELDS = ("classname", "nameToken", "itemTypeName", "itemSlot", "descriptionToken")


def _prefab_chain(item: dict, prefabs_by_id: dict[str, dict], max_depth: int = 25) -> list[dict]:
    """Depth-first walk of an item's prefab tree. `prefab` can hold several
    space-separated ids (items_game.txt's multiple-inheritance form, e.g.
    "weapon_base weapon_supports_stickers weapon_supports_keychains"); each
    is walked in order, first occurrence wins, cycles are cut by `visited`.
    """
    chain: list[dict] = []
    visited: set[str] = set()

    def walk(prefab_field: str, depth: int) -> None:
        if depth > max_depth or not prefab_field:
            return
        for pid in prefab_field.split():
            if pid in visited:
                continue
            visited.add(pid)
            p = prefabs_by_id.get(pid)
            if not p:
                continue
            chain.append(p)
            walk(p.get("prefab", ""), depth + 1)

    walk(item.get("prefab", ""), 0)
    return chain


def _resolve_display_field(item: dict, chain: list[dict], field: str) -> tuple[str, str]:
    own = item.get(field, "") or ""
    if own:
        return own, "own"
    for p in chain:
        v = p.get(field, "") or ""
        if v:
            return v, f"prefab:{p.get('id', '')}"
    return "", "unresolved"


def build_items(data: dict) -> dict:
    prefabs = data.get("prefabs", [])
    prefabs_by_id = {p["id"]: p for p in prefabs}

    items_out = []
    for it in data.get("items", []):
        chain = _prefab_chain(it, prefabs_by_id)
        resolved: dict[str, str] = {}
        resolution: dict[str, str] = {}
        for field in _ITEM_DISPLAY_FIELDS:
            v, how = _resolve_display_field(it, chain, field)
            resolved[field] = v
            resolution[field] = how
        items_out.append({
            "def_index": it.get("defIndex"),
            "name": it.get("name", ""),
            "classname": resolved["classname"],
            "name_token": resolved["nameToken"],
            "item_type_name": resolved["itemTypeName"],
            "item_slot": resolved["itemSlot"],
            "description_token": resolved["descriptionToken"],
            "is_default": bool(it.get("isDefault", False)),
            "prefab_id": it.get("prefab", ""),
            "resolution": resolution,
        })
    items_out.sort(key=lambda i: ((i["name"] or "").lower(), i["def_index"]))

    prefabs_out = [
        {
            "id": p.get("id", ""),
            "parent_prefab": p.get("prefab", ""),
            "classname": p.get("classname", ""),
            "name_token": p.get("nameToken", ""),
            "item_type_name": p.get("itemTypeName", ""),
            "item_slot": p.get("itemSlot", ""),
        }
        for p in prefabs
    ]
    rarities = [
        {"id": r.get("id", ""), "value": r.get("value"), "loc_key": r.get("locKey", ""),
         "loc_key_weapon": r.get("locKeyWeapon", "")}
        for r in data.get("rarities", [])
    ]
    qualities = [{"id": q.get("id", ""), "value": q.get("value")} for q in data.get("qualities", [])]

    return {
        "items": items_out,
        "prefabs": prefabs_out,
        "rarities": rarities,
        "qualities": qualities,
        "note": (
            "item_definitions.json carries no per-item rarity or quality link "
            "upstream; only the rarities and qualities enumeration tables "
            "exist, so items[] has no rarity or quality field."
        ),
    }


def build_paint_kits(data: dict) -> dict:
    return {
        "paint_kits": [
            {"def_index": pk.get("defIndex"), "name": pk.get("name", ""),
             "description_tag": pk.get("descriptionTag", "")}
            for pk in data.get("paintKits", [])
        ]
    }


def build_sticker_kits(data: dict) -> dict:
    return {
        "sticker_kits": [
            {"def_index": sk.get("defIndex"), "name": sk.get("name", ""),
             "item_name_token": sk.get("itemName", ""), "description": sk.get("descriptionString", "")}
            for sk in data.get("stickerKits", [])
        ]
    }


def build_music_kits(data: dict) -> dict:
    return {
        "music_kits": [
            {"def_index": m.get("defIndex"), "name": m.get("name", ""), "loc_name": m.get("locName", "")}
            for m in data.get("musicDefinitions", [])
        ]
    }


# ---------------------------------------------------------------------------
# network.json
# ---------------------------------------------------------------------------

_ENUM_GROUP = {
    "NET_Messages": "NetMessages",
    "CLC_Messages": "ClcMessages",
    "SVC_Messages": "SvcMessages",
    "EBaseUserMessages": "UserMessages",
    "ECstrike15UserMessages": "UserMessages",
    "EDemoCommands": "Demo stream",
    "ETEProtobufIds": "TempEntities",
}

# Best-effort, from the Source engine's own channel naming convention, not
# verified per message against a packet capture.
_DIRECTION_BY_GROUP = {
    "ClcMessages": "client_to_server",
    "SvcMessages": "server_to_client",
    "NetMessages": "bidirectional",
    "UserMessages": "server_to_client",
    "TempEntities": "server_to_client",
    "Decals": "server_to_client",
    "Sounds": "server_to_client",
    "GameEvents": "server_to_client",
    "Source1Legacy": "server_to_client",
    "Bidirectional": "bidirectional",
    "ClientMessages": "client_to_server",
    "PeerToPeer": "peer_to_peer",
    "Demo stream": None,
}


def _game_event_group(id_: int) -> str:
    if 201 <= id_ <= 204:
        return "Decals"
    if 205 <= id_ <= 207:
        return "Source1Legacy"
    if 208 <= id_ <= 212:
        return "Sounds"
    return "GameEvents"


def build_network(
    netmsgs: dict | None, demomsgs: dict | None, wire_rows: list[dict], top_level_message_names: set[str]
) -> dict:
    rows: dict[tuple[str, int, str], dict] = {}

    def add(id_: int, name: str, group: str, binding: str, enum: str | None = None, constant: str | None = None) -> None:
        key = (group, id_, name)
        row = rows.get(key)
        if row is None:
            row = {
                "id": id_, "name": name, "group": group,
                "enum": enum, "constant": constant,
                "direction": _DIRECTION_BY_GROUP.get(group),
                "binding": binding,
            }
            rows[key] = row
            return
        if row["binding"] != binding:
            row["binding"] = "both"
        if enum:
            row["enum"] = enum
        if constant:
            row["constant"] = constant

    if netmsgs:
        for ch in netmsgs.get("channels", []):
            for m in ch.get("messages", []):
                add(m["id"], m["protoMessageType"], ch.get("name", ""), "rtti")
    if demomsgs:
        for m in demomsgs.get("messages", []):
            add(m["id"], m["protoMessageType"], "Demo stream", "rtti")

    for wr in wire_rows:
        group = _ENUM_GROUP.get(wr["enum"]) or _game_event_group(wr["value"])
        add(wr["value"], wr["candidate"], group, "enum", enum=wr["enum"], constant=wr["constant"])

    out = list(rows.values())
    for r in out:
        exists = r["name"] in top_level_message_names
        r["type_exists"] = exists
        bits = []
        if r["binding"] == "enum":
            bits.append(f"Declared in {r['enum']}; not present in this build's RTTI-bound message table.")
        if not exists:
            bits.append("No matching message in this build's descriptor set.")
        r["description"] = " ".join(bits)
    out.sort(key=lambda r: (r["group"], r["id"], r["name"]))
    return {"rows": out}


# ---------------------------------------------------------------------------
# game_modes.json, changelog.json, maps.json, surfaces.json, props.json,
# modules.json
# ---------------------------------------------------------------------------

def build_gamemodes(data: dict) -> dict:
    game_types = []
    for gt in data.get("gameTypes", []):
        modes = []
        for gm in gt.get("gameModes", []):
            modes.append({
                "id": gm.get("id", ""),
                "game_type": gm.get("gameType"),
                "game_mode": gm.get("gameMode"),
                "name_token": gm.get("nameId", ""),
                "description_token": gm.get("descriptionId", ""),
                "display_name": gm.get("displayName", ""),
                "max_players": gm.get("maxPlayers"),
                "map_groups": gm.get("mapGroupsMp", []),
                "type_flags": gm.get("typeFlags"),
                "exhibit_game_type": gm.get("exhibitGameType", ""),
                "convars": gm.get("convars", []),
                "has_convar_overrides": bool(gm.get("convars")),
            })
        game_types.append({"id": gt.get("id", ""), "index": gt.get("index"), "modes": modes})
    map_groups = [{"id": g.get("id", ""), "maps": g.get("maps", [])} for g in data.get("mapGroups", [])]
    return {
        "game_types": game_types,
        "map_groups": map_groups,
        "note": (
            "game_type/game_mode are the numeric ids this build's gamemodes.txt "
            "carries per mode; every mode's convars list is empty upstream on "
            "this build, so has_convar_overrides is false throughout."
        ),
    }


_CHANGELOG_LIST_CAP = 2000


def build_changelog(data: dict) -> dict:
    families = []
    total = 0
    for fam in data.get("families", []):
        added, removed, changed = fam.get("added", []), fam.get("removed", []), fam.get("changed", [])
        total += len(added) + len(removed) + len(changed)
        families.append({
            "family": fam.get("family", ""),
            "added_count": len(added),
            "removed_count": len(removed),
            "changed_count": len(changed),
            "added": added[:_CHANGELOG_LIST_CAP],
            "removed": removed[:_CHANGELOG_LIST_CAP],
            "changed": [
                {
                    "name": c.get("name", ""),
                    "field_changes": [
                        {"field": fc.get("field", ""), "old_value": fc.get("oldValue", ""),
                         "new_value": fc.get("newValue", "")}
                        for fc in c.get("fields", [])
                    ],
                }
                for c in changed[:_CHANGELOG_LIST_CAP]
            ],
            "truncated": max(len(added), len(removed), len(changed)) > _CHANGELOG_LIST_CAP,
        })
    from_build, to_build = data.get("fromBuild", ""), data.get("toBuild", "")
    return {
        "from_build": from_build,
        "to_build": to_build,
        "platform": data.get("platform", ""),
        "families": families,
        "no_changes": total == 0,
        "schema_history_anchor": f"{from_build}-{to_build}",
    }


def build_maps(data: dict) -> dict:
    return {
        "map_names": list(data.get("mapNames", [])),
        "maps": data.get("maps", []),
        "note": "This is the set of maps that ship a radar overview definition, not the game's full map list.",
    }


def build_surfaces(data: dict) -> dict:
    order: list[str] = []
    groups: dict[str, list[dict]] = {}
    for s in data.get("surfaces", []):
        name = s.get("name", "")
        if name not in groups:
            groups[name] = []
            order.append(name)
        groups[name].append({
            "scope": s.get("scope", ""),
            "source_file": s.get("sourceFile", ""),
            "properties": [{"name": p.get("name", ""), "value": p.get("value", "")} for p in s.get("properties", [])],
        })
    return {"materials": [{"name": n, "rows": groups[n]} for n in order]}


def build_props(data: dict) -> dict:
    prop_classes = [
        {"id": pc.get("id", ""),
         "properties": [{"name": p.get("name", ""), "value": p.get("value", "")} for p in pc.get("properties", [])]}
        for pc in data.get("propClasses", [])
    ]
    collision_groups = [
        {
            "type": g.get("collisionGroup", ""),
            "name": g.get("name", ""),
            "description": g.get("description", ""),
            "interact_as": g.get("interactAs", []),
            "interact_with": g.get("interactWith", []),
            "interact_exclude": g.get("interactExclude", []),
        }
        for g in data.get("collisionGroups", [])
    ]
    breakable_models = [{"id": b.get("id", ""), "models": b.get("models", [])} for b in data.get("breakableModels", [])]
    return {"prop_classes": prop_classes, "collision_groups": collision_groups, "breakable_models": breakable_models}


def build_modules(data: dict, schema_modules: set[str]) -> dict:
    out = []
    for m in data.get("modules", []):
        path = m.get("path", "")
        stem = Path(path).stem
        out.append({
            "path": path,
            "stem": stem,
            "file_size": m.get("fileSize", ""),
            "sha256": m.get("sha256", ""),
            "export_count": m.get("exportCount"),
            "schema_registration_count": m.get("schemaRegistrationCount"),
            "resolved_interfaces": m.get("resolvedInterfaces", []),
            "schema_module": stem if stem in schema_modules else None,
        })
    out.sort(key=lambda m: m["path"].lower())
    return {"modules": out}


# ---------------------------------------------------------------------------
# schema-history.json
# ---------------------------------------------------------------------------

def build_schema_history(evolution: dict, lens_overlay: dict, source_info: dict) -> dict:
    transitions_raw = evolution.get("transitions", [])
    summarised = [(tr, gd._transition_counts(tr)) for tr in transitions_raw]

    transitions_out = []
    for tr, c in summarised:
        transitions_out.append({
            "from_build": tr.get("fromBuild", ""),
            "to_build": tr.get("toBuild", ""),
            "from_date": (tr.get("fromManifestCreatedUtc", "") or "")[:10],
            "to_date": (tr.get("toManifestCreatedUtc", "") or "")[:10],
            "anchor": f"{tr.get('fromBuild', '')}-{tr.get('toBuild', '')}",
            "counts": c,
            "is_empty": gd._transition_is_empty(c),
        })

    non_empty = [(tr, c) for tr, c in summarised if not gd._transition_is_empty(c)]
    rename_idx = gd._confirmed_rename_index(lens_overlay)
    detail_cap_tr = gd._HISTORY_DETAIL_TRANSITIONS
    detail_cap_cls = gd._HISTORY_DETAIL_CLASS_CAP

    detail_out = []
    for tr, _c in list(reversed(non_empty))[:detail_cap_tr]:
        changed = tr.get("classChanged", [])
        classes_out = []
        for cd in changed[:detail_cap_cls]:
            kinds: dict[str, int] = {}
            for op in cd.get("fieldOps", []):
                kinds[op.get("kind", "")] = kinds.get(op.get("kind", ""), 0) + 1
            structural = {k for k in kinds if k != "META_CHANGE"}
            cls_name = cd.get("name", "")
            confirmed = {id(r) for (cn, _fld), r in rename_idx.items() if cn == cls_name}
            classes_out.append({
                "name": cls_name,
                "field_ops": kinds,
                "metadata_only": bool(kinds) and not structural,
                "static_field_ops": len(cd.get("staticFieldOps", [])),
                "meta_ops": len(cd.get("metaOps", [])),
                "paired_evidence": len(cd.get("pairedEvidence", [])),
                "pair_candidates": len(cd.get("pairCandidates", [])),
                "resize": cd.get("resize"),
                "realign": bool(cd.get("realign")),
                "reparent": bool(cd.get("reparent")),
                "flags_changed": bool(cd.get("flags")),
                "confirmed_rename_count": len(confirmed),
            })
        detail_out.append({
            "from_build": tr.get("fromBuild", ""),
            "to_build": tr.get("toBuild", ""),
            "anchor": f"{tr.get('fromBuild', '')}-{tr.get('toBuild', '')}",
            "from_date": (tr.get("fromManifestCreatedUtc", "") or "")[:10],
            "to_date": (tr.get("toManifestCreatedUtc", "") or "")[:10],
            "classes_added": tr.get("classAdded", []),
            "classes_removed": tr.get("classRemoved", []),
            "classes_changed": classes_out,
            "classes_changed_total": len(changed),
            "classes_changed_truncated": len(changed) > detail_cap_cls,
            "class_pair_candidates_count": len(tr.get("classPairCandidates", [])),
            "field_move_candidates_count": len(tr.get("fieldMoveCandidates", [])),
        })

    return {
        "baseline_build": evolution.get("baselineBuild", ""),
        "latest_build": evolution.get("latestBuild", ""),
        "platform": evolution.get("platform", source_info.get("platform", "")),
        "schema_version": evolution.get("schemaVersion", ""),
        "transitions": transitions_out,
        "detail": detail_out,
        "breaking": list(lens_overlay.get("breaking", []) or []),
    }


# ---------------------------------------------------------------------------
# meta.json
# ---------------------------------------------------------------------------

def build_meta(source_info: dict, entities: dict[str, dict], counts: dict[str, int]) -> dict:
    mod_classes: dict[str, int] = defaultdict(int)
    mod_enums: dict[str, int] = defaultdict(int)
    class_names = set()
    enum_names = set()
    declared_fields = 0
    for v in _iter_entity_variants(entities):
        if v["kind"] == "class":
            mod_classes[v["module"]] += 1
            declared_fields += len(v["fields"])
        else:
            mod_enums[v["module"]] += 1
    for name, e in entities.items():
        (class_names if e["kind"] == "class" else enum_names).add(name)

    modules_list = [
        {"module": m, "classes": mod_classes.get(m, 0), "enums": mod_enums.get(m, 0)}
        for m in sorted(set(mod_classes) | set(mod_enums))
    ]

    all_counts = {
        "classes": len(class_names),
        "enums": len(enum_names),
        "fields": declared_fields,
    }
    all_counts.update(counts)

    return {
        "build_id": source_info.get("build_id", ""),
        "steam_date": source_info.get("version_date", ""),
        "steam_manifest_utc": source_info.get("version_time", ""),
        "platform": source_info.get("platform", ""),
        "schema_version": source_info.get("schema_version", ""),
        "tool_version": source_info.get("tool_version", ""),
        "tool_commit": source_info.get("tool_commit", ""),
        "counts": all_counts,
        "modules": modules_list,
        "note": (
            "classes/enums/fields count distinct top-level entity names and "
            "their own declared fields; the modules[] list additionally "
            "counts client/server twin records (duplicates), so summing its "
            "per-module classes/enums can exceed the top-level totals above."
        ),
    }


# ---------------------------------------------------------------------------
# README.md
# ---------------------------------------------------------------------------

def _build_readme(sizes: dict[str, int], facts: dict[str, int]) -> str:
    """*facts* carries the build-specific counts the prose quotes, so the
    text never goes stale against the data next to it."""
    def kb(name: str) -> str:
        n = sizes.get(name)
        return f"{n / 1024:.1f} KB" if n is not None else "not generated this build"

    return f"""# docs/generated/data/

Generated by `docs/site_data.py`. Every file here is overwritten on the next
run -- do not hand-edit. The entity/proto schema itself is not duplicated
here; it lives in `../downstream-codegen-schemas/cs2_schema.json`.

All files are UTF-8, pretty-printed JSON with 2-space indent and sorted
object keys. Where key order would carry meaning (e.g. `imports`, which
preserves the descriptor's own dependency order) it is left as upstream
gives it; every other list is explicitly sorted so two runs on the same
input are byte-identical.

## meta.json ({kb('meta.json')})

Build identity (`build_id`, `steam_date`, `steam_manifest_utc` and
`platform` from the build's own `provenance.json`, `schema_version`,
`tool_version`), a `counts` object per family, and a `modules` list of
`{{module, classes, enums}}`. `classes`/`enums`/`fields` in `counts` are
distinct top-level entity names (matching what a reader would call
"{facts['classes']:,} classes"); the per-module `modules[]` counts
additionally include client/server twin duplicate records, so they can sum
to more than the top-level totals -- see the `note` field on the object.
`counts.messages` is `protobufs.json`'s flattened total (top-level plus
nested, {facts['messages']:,} on this build); `counts.surfaces` is the
upstream record count from `surface_properties.json`
({facts['surfaces']:,} on this build), not the number of distinct
materials in `surfaces.json`'s `materials[]` (which is smaller, since the
same material can have several rows).

## protobufs.json ({kb('protobufs.json')})

`files[]`: one entry per `.proto` file (`name`, `stem`, `package`, `imports`,
overlay `description`/`notes`). `messages[]` and `enums[]` on each file are
**flattened recursively** -- every nested message and enum appears as its
own entry, tagged with `qualified` (dotted `Parent.Nested` path) and
`parent` (the parent's qualified name, or `null` for a top-level type).
`nested_messages`/`nested_enums` on a message are the qualified names of its
*direct* children only. A message's `description`/`notes` come from the
overlay entry keyed by its qualified name (`CDemoClassInfo.class_t` for a
nested type); a bare name addresses a top-level message only. Enum
`values[]` carry `name` and `number`; the overlay format has no slot for a
proto enum value's prose.

Field type resolution (`type_kind`, `type`, `type_file`): this build's
{facts['proto_files']} proto files carry no `package`, so a field's raw type is either a bare
simple name (a top-level type, in this file or another) or a same-file
dotted path to a nested type. Resolution: dotted raw values are looked up
directly against the qualified-name index; bare raw values are looked up
against every file's top-level type names, preferring a match in the
field's own file when more than one file defines that name (only one such
collision exists in this build: `CMsgProtoBufHeader`, defined identically
in two Steam-side files neither CS2 wire message references). `type_kind`
is `scalar`, `message`, or `enum`; `unknown` is reserved for a name outside
the descriptor set, not observed on this build.

Top-level `types` maps every qualified name (message or enum, nested
included) to its defining file. Top-level `referenced_by` maps a qualified
type name to the sorted list of qualified messages that have a field of
that type.

`wire_ids` on a (top-level only) message is the list of `{{enum, constant,
value}}` entries whose enum constant name maps to that message's name by
the join rule below. A message can have zero, one, or more than one.

### Wire-id join rule

Each row's `enum`/`constant` comes from scanning a fixed set of descriptor
enums whose constants are known to be message-id tables, transforming each
constant's name by a rule verified against this build's actual message
names (not guessed):

| Enum | Constant prefix | Message name rule | Notes |
|---|---|---|---|
| `NET_Messages` | `net_X` | `CNETMsg_X` | |
| `CLC_Messages` | `clc_X` | `CCLCMsg_X` | |
| `SVC_Messages` | `svc_X` | `CSVCMsg_X` | |
| `EBaseUserMessages` | `UM_X` | `CUserMessageX` (no separator) | |
| `ECstrike15UserMessages` | `CS_UM_X` | `CCSUsrMsg_X` | |
| `EDemoCommands` | `DEM_X` | `CDemoX` (no separator) | `Error`/`Max`/`IsCompressed` are flag/sentinel values, skipped |
| `ETEProtobufIds` | `TE_XId` | `CMsgTEX` (trailing `Id` stripped) | |
| `EBaseGameEvents` | `GE_X` | `CMsgX` | |
| `ECsgoGameEvents` | `GE_XId` | `CMsgX` (trailing `Id` stripped) | |

Every other enum in the descriptor set (Steam/GC message tables such as
`EGCItemMsg`, `EMsg`, `EGCSystemMsg`, ...) was checked with the same
strip-prefix-then-`CMsg`/`C`-prepend heuristic and produced zero matches
against this build's actual message names, so it is left unjoined rather
than guessed at.

`network.json` performs a second, separate join using these same rules
against the RTTI-recovered id tables -- see below.

## convars.json ({kb('convars.json')}) / commands.json ({kb('commands.json')})

`convars[]`/`commands[]`: `name`, `default` (convars only), `value_type`
(convars only, e.g. `Float32`/`Int32`/`Bool`/`String`), `min`/`max` (convars
only, `null` when upstream has no bound), `flags[]` (sorted), `help` (the
raw upstream description, newlines preserved -- render, don't `\\n`-collapse
it), `prefix` (text before the first underscore, or the whole name if there
is none), and `has_completion_callback` (commands only). Sorted
case-insensitively by name.

Both files carry the same `flags` legend array
(`{{name, convar_count, command_count, description}}`), loaded from
`docs/overlays/convar_flags.yml`. A flag this build uses that has no overlay
entry is logged as an `INFO` line and shipped with an empty `description`,
so a new upstream flag never blocks a regeneration; add it to the overlay to
name it.

## gameevents.json ({kb('gameevents.json')})

`events[]`: `name`, `source` (originating `.gameevents` file), `anchor`,
`description` (overlay first, else the upstream inline comment), `notes`,
`warning`, `properties`, `fields[]` (`name`, `type`, `description`).

Anchor rule: a name unique across all sources uses itself as the anchor; a
name that appears in more than one source gets `<name>-<source-stem>`
(source with the `.gameevents` suffix removed, e.g. `round_end-mod`), so
every event has a distinct, stable anchor even when the name repeats.
{facts['duplicate_event_names']} names repeat on this build (`round_end`,
for one, is declared in every `.gameevents` file).
`duplicates` maps each such name to its list of sources.

`type_legend` maps each field type to its description and, where derivable,
the numeric `type` code `CMsgSource1LegacyGameEvent.key_t` (the carrier of
every game event on the wire) would use for it. The code is read off
`key_t`'s own field numbers on this build (`val_string` is field 2, so its
code is 1; `val_uint64` is field 8, so its code is 7), not recalled from an
external header. `player_controller_and_pawn` has no single code: its
`note` explains the bit-packing (controller id in the low byte, pawn index
above it).

## items.json ({kb('items.json')}) / paint_kits.json ({kb('paint_kits.json')}) / sticker_kits.json ({kb('sticker_kits.json')}) / music_kits.json ({kb('music_kits.json')})

`items[]`: `def_index`, `name` (upstream's own identifying `name` field,
e.g. `weapon_ak47` -- previously dropped by the Markdown generator),
`classname`/`name_token`/`item_type_name`/`item_slot`/`description_token`
resolved through the prefab chain when the item's own value is empty (see
below), `is_default`, `prefab_id`, and a `resolution` object naming, per
resolved field, whether the value came from the item itself (`"own"`), a
prefab in the chain (`"prefab:<id>"`), or was left unresolved (`""`).
There is no per-item `rarity`/`quality`: upstream `item_definitions.json`
carries no link from an item to the `rarities`/`qualities` enumeration
tables (also emitted here) -- see the `note` field on the object.

Prefab resolution: an item's (or prefab's) own `prefab` field can hold
several space-separated prefab ids (items_game.txt's multiple-inheritance
form). Each is walked depth-first in order, first non-empty value for a
given display field wins, and a visited-id set cuts cycles. Verified
against `weapon_ak47`: its own fields are all empty except `prefab`, whose
chain (`weapon_ak47_prefab` -> `rifle` -> `primary`) supplies `classname`
and `name_token` from the first link and `item_type_name` from the second.

`sticker_kits.json` is a single file; at this build's size it stays under
the 5 MB cap without a defIndex-thousand split (see `meta.json` for the
current sticker kit count).

## maps.json ({kb('maps.json')})

All upstream per-map fields, bomb site coordinates (`bombAX`/`bombAY`/
`bombBX`/`bombBY`), `rotate`, `zoom`, and `blockName` included verbatim
(previously dropped). `note` states plainly that this is the set of maps
shipping a radar overview, not the game's full map list.

## game_modes.json ({kb('game_modes.json')})

Each mode carries upstream's numeric `game_type`/`game_mode` ids alongside
the string `id` (previously dropped). `has_convar_overrides` reflects
upstream `convars[]`; on this build every mode's list is empty, so it is
`false` throughout -- the `note` field says so rather than letting the
zeroes look like a bug in this emitter.

## props.json ({kb('props.json')})

`collision_groups[]` carries both `type` (upstream's `collisionGroup`
enum-like value, e.g. `ConditionallySolid`) and `name` (upstream's actual
name, e.g. `clip` -- previously the Markdown page showed only `type`, so
distinct groups sharing a type looked like duplicates), plus
`interact_exclude` (previously dropped).

## surfaces.json ({kb('surfaces.json')})

Grouped by material: `materials[]` is `{{name, rows[]}}`, each row one
upstream record's `scope`/`source_file`/`properties` -- the same material
that appeared as several disconnected table rows in the Markdown page is
now one entry with several rows underneath it.

## modules.json ({kb('modules.json')})

Each binary carries its upstream `sha256` (previously dropped) and
`schema_module`: the binary's path stem (e.g. `server` from
`game/csgo/bin/win64/server.dll`) when that name matches one of the schema
modules seen in `entity_schema.json` (SchemaTracker's `projectName`
grouping), else `null`.

## network.json ({kb('network.json')})

`rows[]`: `{{id, name, group, enum, constant, direction, binding,
type_exists, description}}`. This is the union of two sources: the
RTTI-recovered id tables (`network_messages.json`'s channels plus
`demo_messages.json`, `binding: "rtti"`) and the same wire-id join rules
documented under `protobufs.json` above, applied here to attempt a message
name for every enum constant whether or not it appears in the RTTI table
(`binding: "enum"`). A row present in both is `binding: "both"`. Rows are
keyed by `(group, id, name)`, not `id` alone: ids are only unique within
their `group` (e.g. `NetMessages` id 0 and `SvcMessages` id 40 are
unrelated), and a single `(group, id)` can legitimately carry more than one
message (`CDemoSpawnGroups` and `CDemoSpawnGroupsHLTVBroadcast` both bind
demo id 15).

`group` is the upstream channel name for `rtti` rows; for `enum`-only rows
it is the channel a message with that enum would land in (see the id-range
table below for the game-event enums, which split across four channels).
`type_exists` is `false` when the joined/looked-up name has no matching
message in this build's descriptor set at all -- distinguishing a genuinely
dead id from one that is merely not (yet) bound via RTTI, which the
Markdown page could not do.

`direction` is inferred from the Source engine's channel-naming convention
(`Svc`/`Clc`/etc.), not verified per message against a packet capture; it
is `null` where no convention is known (the demo stream is a recorded
format, not a live direction).

Which enum feeds which channel/id range:

| Channel (`group`) | Id range on this build | Source enum(s) |
|---|---|---|
| `NetMessages` | 0-15 | `NET_Messages` |
| `ClcMessages` | 20-75 | `CLC_Messages` |
| `SvcMessages` | 40-77 | `SVC_Messages` |
| `UserMessages` | 101-390 | `EBaseUserMessages` (101-200), `ECstrike15UserMessages` (301-390) |
| `TempEntities` | 400-452 | `ETEProtobufIds` |
| `Decals` | 201-204 | `EBaseGameEvents` |
| `Sounds` | 208-212 | `EBaseGameEvents` |
| `Source1Legacy` | 205-207 | `EBaseGameEvents` |
| `GameEvents` | 200, 213-214, 450-453 | `EBaseGameEvents`, `ECsgoGameEvents` |
| `Demo stream` | 0-19, 64 | `EDemoCommands` |

## changelog.json ({kb('changelog.json')})

For the one build-pair transition the current artifact set carries: every
family is always listed (with `added_count`/`removed_count`/`changed_count`,
even when all are zero), `no_changes` is `true` when every family is empty
across the whole transition (which it is on this build), and
`schema_history_anchor` links to the matching transition's anchor in
`schema-history.json`.

## schema-history.json ({kb('schema-history.json') if 'schema-history.json' in sizes else 'not generated -- no schema_evolution.json for this platform'})

`transitions[]`: every recorded transition (from/to build, dates, op
counts, `anchor`, `is_empty`). `detail[]`: full per-class field-op detail
for the three most recent transitions with structural changes, each changed
class flagged `metadata_only: true` when every one of its field ops is
`META_CHANGE` (a metadata-only churn class, previously shown identically to
a real structural change). `breaking[]` is `docs/overlays/schema-lens.yml`'s
`breaking:` list, passed through as-is.

## Fields with no page yet

Emitted for completeness but rendered by no site page on this build:
`maps.json`'s `map_names` list and each map's `properties` array, and
`game_modes.json`'s per-mode `convars` list (empty upstream on this build).

## Regenerating

```
python3 docs/site_data.py --repo-root . \\
    --artifacts-root ./upstream/schema-tracker/artifacts \\
    --build latest --platform windows-x86_64 --output docs
```
"""


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def emit_site_data(
    repo_root: str | Path,
    artifacts_root: str | Path | None = None,
    build: str = "latest",
    platform: str = "windows-x86_64",
    output: str | Path = "docs",
) -> dict[str, int]:
    """Load one SchemaTracker build and write docs/generated/data/*.json.

    Self-contained: resolves the build and loads every artifact itself, so
    it can be called independently of generate_docs.main()'s internal
    state. Returns {filename: bytes_written} for the files actually
    produced (schema-history.json is omitted when no schema_evolution.json
    exists for this platform).
    """
    WARNINGS.clear()
    INFOS.clear()
    repo_root = Path(repo_root).resolve()
    artifacts_root = (
        Path(artifacts_root).resolve() if artifacts_root
        else repo_root / "upstream" / "schema-tracker" / "artifacts"
    )
    out_dir = Path(output).resolve()
    data_dir = out_dir / Path(*DATA_SUBDIR)
    data_dir.mkdir(parents=True, exist_ok=True)

    overlays = gd.load_overlays(repo_root / "docs" / "overlays")

    build_dir = gd.resolve_build_dir(artifacts_root, build, platform)
    if build_dir is None:
        raise RuntimeError(
            f"could not resolve a SchemaTracker build under {artifacts_root} "
            f"(build={build!r}, platform={platform!r})"
        )

    source_info = gd.build_source_info(build_dir, platform)

    entities = gd.load_entity_schema(build_dir)
    protos = gd.load_proto_descriptors(build_dir / "protos.descriptorset")
    convars = gd.load_convars_json(build_dir / "convars.json")
    commands = gd.load_commands_json(build_dir / "commands.json")
    gameevents = gd.load_gameevents_json(build_dir / "gameevents.json")

    protobufs_data = build_protobufs(protos, overlays)

    flags_legend = _build_flags_legend(overlays, convars, commands)
    convars_data = build_convars(convars, flags_legend)
    commands_data = build_commands(commands, flags_legend)

    gameevents_data = build_gameevents(gameevents, overlays, protos)

    items_json = gd._load_content_json(build_dir, "item_definitions.json") or {}
    items_data = build_items(items_json)
    paint_kits_data = build_paint_kits(items_json)
    sticker_kits_data = build_sticker_kits(items_json)
    music_kits_data = build_music_kits(items_json)

    netmsgs = gd._load_content_json(build_dir, "network_messages.json")
    demomsgs = gd._load_content_json(build_dir, "demo_messages.json")
    top_level_message_names = {m["name"] for p in protos for m in p.get("messages", [])}
    network_data = build_network(netmsgs, demomsgs, _wire_id_rows(protos), top_level_message_names)

    gamemodes_data = build_gamemodes(gd._load_content_json(build_dir, "game_modes.json") or {})
    changelog_data = build_changelog(gd._load_content_json(build_dir, "changelog.json") or {})
    maps_data = build_maps(gd._load_content_json(build_dir, "map_overviews.json") or {})
    surfaces_data = build_surfaces(gd._load_content_json(build_dir, "surface_properties.json") or {})
    props_data = build_props(gd._load_content_json(build_dir, "prop_data.json") or {})

    schema_modules = {v["module"] for v in _iter_entity_variants(entities)}
    modules_data = build_modules(gd._load_content_json(build_dir, "modules.json") or {}, schema_modules)

    evolution = gd.load_schema_evolution(artifacts_root, platform)
    schema_history_data = None
    if evolution:
        lens_overlay = overlays.get("schema-lens", {}) or {}
        schema_history_data = build_schema_history(evolution, lens_overlay, source_info)

    n_messages = sum(len(f["messages"]) for f in protobufs_data["files"])
    counts = {
        "proto_files": len(protobufs_data["files"]),
        "messages": n_messages,
        "convars": len(convars_data["convars"]),
        "commands": len(commands_data["commands"]),
        "events": len(gameevents_data["events"]),
        "items": len(items_data["items"]),
        "sticker_kits": len(sticker_kits_data["sticker_kits"]),
        "paint_kits": len(paint_kits_data["paint_kits"]),
        "music_kits": len(music_kits_data["music_kits"]),
        "maps": len(maps_data["maps"]),
        "game_modes": sum(len(gt["modes"]) for gt in gamemodes_data["game_types"]),
        "surfaces": sum(len(m["rows"]) for m in surfaces_data["materials"]),
        "modules": len(modules_data["modules"]),
    }
    meta_data = build_meta(source_info, entities, counts)

    sizes: dict[str, int] = {}

    def emit(name: str, obj: Any) -> None:
        sizes[name] = _write_json(data_dir / name, obj)

    emit("meta.json", meta_data)
    emit("protobufs.json", protobufs_data)
    emit("convars.json", convars_data)
    emit("commands.json", commands_data)
    emit("gameevents.json", gameevents_data)
    emit("items.json", items_data)
    emit("paint_kits.json", paint_kits_data)
    emit("sticker_kits.json", sticker_kits_data)
    emit("music_kits.json", music_kits_data)
    emit("maps.json", maps_data)
    emit("game_modes.json", gamemodes_data)
    emit("props.json", props_data)
    emit("surfaces.json", surfaces_data)
    emit("modules.json", modules_data)
    emit("network.json", network_data)
    emit("changelog.json", changelog_data)
    if schema_history_data is not None:
        emit("schema-history.json", schema_history_data)

    facts = {
        "classes": meta_data["counts"]["classes"],
        "messages": counts["messages"],
        "surfaces": counts["surfaces"],
        "proto_files": counts["proto_files"],
        "duplicate_event_names": len(gameevents_data["duplicates"]),
    }
    readme_path = data_dir / "README.md"
    readme_text = _build_readme(sizes, facts)
    with readme_path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(readme_text)

    return sizes


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Emit docs/generated/data/*.json for the Astro site.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--artifacts-root", default=None)
    parser.add_argument("--build", default="latest")
    parser.add_argument("--platform", default="windows-x86_64", choices=["windows-x86_64", "linux-x86_64"])
    parser.add_argument("--output", default="docs")
    args = parser.parse_args(argv)

    try:
        sizes = emit_site_data(
            repo_root=args.repo_root,
            artifacts_root=args.artifacts_root,
            build=args.build,
            platform=args.platform,
            output=args.output,
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    for i in INFOS:
        print(f"INFO: {i}")
    for w in WARNINGS:
        print(f"WARNING: {w}", file=sys.stderr)
    total = sum(sizes.values())
    print(f"Wrote {len(sizes)} file(s), {total / 1024:.1f} KB total, to "
          f"{Path(args.output).resolve() / Path(*DATA_SUBDIR)}")
    for name in sorted(sizes):
        print(f"  {name}: {sizes[name] / 1024:.1f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
