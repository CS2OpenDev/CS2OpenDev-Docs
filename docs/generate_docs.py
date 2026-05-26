#!/usr/bin/env python3
"""
CS2 Documentation Generator

Parses CS2 schema dumps (entity classes, enums), Protobuf definitions,
convars, and commands, then generates structured static-HTML documentation
with Mermaid UML diagrams.

Community annotations can be added by placing YAML overlay files under
docs/overlays/{module}/{EntityName}.yml  (see docs/overlays/README.md).

Usage:
    python3 docs/generate_docs.py [--repo-root PATH] [--output PATH]
                                  [--data-root PATH]

    --repo-root  Root of the repository that contains docs/, overlays/, etc.
                 (default: current directory)
    --data-root  Root of the CS2OpenDev-Docs data tree that contains
                 DumpSource2/ and Protobufs/.  Defaults to --repo-root, which
                 is the right value when running inside this repository.  Set
                 this to a submodule or sibling checkout path when running
                 from a standalone documentation repository.

Dependencies (all in the Python 3 stdlib except PyYAML):
    pip install pyyaml
"""

from __future__ import annotations

import argparse
import copy
import gzip
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Version of the JSON shape emitted under docs/generated/downstream-codegen-schemas/.
# Bump the major when a field is removed or renamed; the minor when a field is added.
# Additive `annotations` blocks do not require a bump — they were part of 1.0.
SCHEMA_FORMAT_VERSION = "1.1"

# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def _format_metadata(meta: dict[str, Any]) -> str:
    """Render one structured metadata entry as a human-readable string
    for Markdown output.

    Examples:
        {"name": "MNotSaved"}                       -> "MNotSaved"
        {"name": "MPropertyDescription",
         "value": "\"text\""}                       -> "MPropertyDescription \"text\""

    The structured form is what we keep on the entity dict — this helper
    only converts at *render* time so codegen consumers reading
    `x-cs2-metadata` from cs2_schema.json get the {name, value} split.
    """
    if not isinstance(meta, dict):
        # Defensive: some legacy callers may still pass strings.
        return str(meta)
    name = meta.get("name", "")
    value = meta.get("value")
    if value is None or value == "":
        return name
    return f"{name} {value}"


def _metadata_friendly_text(metas: list[dict[str, Any]] | None) -> str:
    """Pull a friendly-name + description out of a structured-metadata
    list (best-effort), suitable for the human-readable column of an
    enum/field value table.

    `MPropertyFriendlyName` and `MPropertyDescription` are the conventions
    DumpSource2 uses on enum members and field overrides; values are
    quoted strings, so we strip surrounding quotes before returning.
    """
    if not metas:
        return ""
    friendly = ""
    desc = ""
    for m in metas:
        if not isinstance(m, dict):
            continue
        n, v = m.get("name", ""), m.get("value", "") or ""
        v = v.strip().strip('"')
        if n == "MPropertyFriendlyName" and not friendly:
            friendly = v
        elif n == "MPropertyDescription" and not desc:
            desc = v
    if friendly and desc and friendly != desc:
        return f"{friendly} — {desc}"
    return friendly or desc


def _stringify_type(t: dict[str, Any]) -> str:
    """Convert a structured cs2.json type node into the legacy string form
    that the rest of the generator (`_extract_type_refs`, Mermaid
    renderers, Markdown tables) understands.

    Mapping:
      builtin / declared_class / declared_enum  -> name
      atomic                                    -> name [ '<' inner [ ',' inner2 ] '>' ]
      ptr                                       -> inner '*'
      fixed_array                               -> inner '[' count ']'
      bitfield                                  -> 'bitfield:' count
    """
    cat = t.get("category")
    if cat in ("builtin", "declared_class", "declared_enum"):
        return t.get("name", "?")
    if cat == "atomic":
        name = t.get("name", "?")
        args: list[str] = []
        if "inner" in t:
            args.append(_stringify_type(t["inner"]))
        if "inner2" in t:
            args.append(_stringify_type(t["inner2"]))
        if "inner3" in t:
            args.append(_stringify_type(t["inner3"]))
        if args:
            return f"{name}<{','.join(args)}>"
        return name
    if cat == "ptr":
        inner = t.get("inner", {})
        return _stringify_type(inner) + "*"
    if cat == "fixed_array":
        inner = t.get("inner", {})
        count = t.get("count", "")
        return f"{_stringify_type(inner)}[{count}]"
    if cat == "bitfield":
        return f"bitfield:{t.get('count', 0)}"
    return t.get("name", "?")


def _innermost_declared_module(t: dict[str, Any]) -> str | None:
    """Walk a structured type tree and return the module of the innermost
    declared class or enum, or None if the type isn't ultimately a
    reference to another entity.

    Handles wrapper categories that nest a target (``ptr``, ``fixed_array``,
    ``atomic`` like ``CHandle<X>`` / ``CUtlVector<X>`` / ``CUtlOrderedMap<K,V>``).
    For multi-arg atomic templates we return the first inner's module — the
    primary referenced type.
    """
    if not isinstance(t, dict):
        return None
    cat = t.get("category")
    if cat in ("declared_class", "declared_enum"):
        return t.get("module")
    for inner_key in ("inner", "inner2", "inner3"):
        if inner_key in t:
            mod = _innermost_declared_module(t[inner_key])
            if mod:
                return mod
    return None


def _convert_class(cls: dict[str, Any]) -> dict[str, Any]:
    """Convert one cs2.json class entry into the entity dict shape used by
    the rest of the generator.

    Metadata is preserved as ``[{name, value}]`` (cs2.json's native shape)
    rather than the legacy stringified form — codegen consumers want the
    split.  Type and parent module hints are propagated so cross-module
    references can be disambiguated downstream.
    """
    fields: list[dict[str, Any]] = []
    for f in cls.get("fields", []):
        ftype = f.get("type", {})
        out: dict[str, Any] = {
            "name": f.get("name", ""),
            "type": _stringify_type(ftype),
            "offset": f.get("offset"),
            "annotations": list(f.get("metadata", [])),
        }
        # When the field references another declared class/enum, cs2.json
        # tells us which module that target lives in — keep the hint so
        # the JSON Schema can disambiguate cross-module references.  This
        # recurses through pointers / arrays / templates so
        # ``CHandle<CCSPlayerController>`` and ``CCSPlayerPawn*`` both get
        # the inner target's module surfaced.
        type_module = _innermost_declared_module(ftype)
        if type_module:
            out["type_module"] = type_module
        fields.append(out)

    parents = cls.get("parents", [])
    parent_modules = [p.get("module", "") for p in parents]

    return {
        "name": cls["name"],
        "kind": "class",
        "module": cls.get("module", ""),
        "bases": [p.get("name", "") for p in parents],
        "base_modules": parent_modules,
        "fields": fields,
        "metadata": list(cls.get("metadata", [])),
        "enum_underlying": None,
        "size": cls.get("size"),
        # Original upstream record preserved verbatim so the generated
        # cs2_schema.json can echo cs2.json.gz's exact shape with overlay
        # annotations layered on top.  See generate_cs2_schema().
        "raw": cls,
    }


def _convert_enum(en: dict[str, Any]) -> dict[str, Any]:
    """Convert one cs2.json enum entry into the entity dict shape used by
    the rest of the generator.

    Per-member metadata (``MPropertyFriendlyName``, ``MPropertyDescription``,
    etc.) is preserved on each value's ``annotations`` list as a structured
    ``[{name, value}]`` array — surfaced both in the Markdown enum table's
    Description column and as ``x-cs2-enum-value-metadata`` in
    cs2_schema.json.
    """
    fields: list[dict[str, Any]] = []
    for m in en.get("members", []):
        v = m.get("value")
        v_str = "" if v is None else str(v)
        fields.append({
            "name": m.get("name", ""),
            "value": v_str,
            "annotations": list(m.get("metadata", [])),
        })
    return {
        "name": en["name"],
        "kind": "enum",
        "module": en.get("module", ""),
        "bases": [],
        "base_modules": [],
        "fields": fields,
        "metadata": list(en.get("metadata", [])),
        "enum_underlying": en.get("alignment"),
        # Original upstream record preserved verbatim — see _convert_class.
        "raw": en,
    }


def _add_entity(entities: dict[str, dict], entity: dict[str, Any]) -> None:
    """Insert *entity* into *entities*, deduplicating on ``(module, name)``.

    DumpSource2's cs2.json sometimes emits the same class definition more
    than once within a single module (e.g. ``CBasePulseGraphInstance``
    appears 12 times under ``pulse_runtime_lib``).  We collapse those into
    one entry.

    When the same name appears in **different** modules — the legitimate
    case, e.g. ``CCSPlayerController`` lives in both ``client`` and
    ``server`` — the additional variant is attached to ``duplicates`` so
    downstream renderers continue to bucket both variants by module.
    """
    name = entity["name"]
    module = entity.get("module", "")
    existing = entities.get(name)
    if existing is None:
        entities[name] = entity
        return
    if existing.get("module") == module:
        return  # exact same (module, name) — drop the redundant entry
    for dup in existing.get("duplicates", []):
        if dup.get("module") == module:
            return
    existing.setdefault("duplicates", []).append(entity)


def _open_schema_json(path: Path):
    """Return a text-mode file handle for *path*, transparently
    decompressing if it is gzipped."""
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8")
    return path.open("r", encoding="utf-8")


def load_schema_json(path: Path) -> tuple[dict[str, dict], dict[str, Any]]:
    """Load DumpSource2's structured ``cs2.json`` (or ``cs2.json.gz``).

    Returns a pair ``(entities, source_info)`` where:

    * ``entities`` is the entity map keyed by name.  This is the
      structured-JSON path that replaced an older regex walk over the
      per-module ``.h`` files in ``DumpSource2/schemas/``; the JSON
      carries inheritance / sizes / offsets / metadata directly, so
      no header parsing is needed any more.
    * ``source_info`` carries the cs2.json header — generator URL, build
      revision, version date/time — so consumers of the generated
      schema files can identify the game build the data corresponds to.
    """
    with _open_schema_json(path) as fh:
        data = json.load(fh)

    entities: dict[str, dict] = {}
    for cls in data.get("classes", []):
        _add_entity(entities, _convert_class(cls))
    for en in data.get("enums", []):
        _add_entity(entities, _convert_enum(en))

    source_info: dict[str, Any] = {
        k: data[k]
        for k in ("generator", "revision", "version_date", "version_time")
        if k in data
    }
    return entities, source_info


def find_schema_json(data_root: Path) -> Path | None:
    """Locate the cs2 schema JSON file.

    Looks first inside ``data_root`` (the GameTracking-CS2 submodule) for a
    cs2.json that DumpSource2 may someday write there, and falls back to a
    sibling ``schema-explorer`` submodule tracking
    ``ValveResourceFormat/SchemaExplorer`` (today's actual source).

    The sibling layout is necessary because ``data_root`` is itself a git
    submodule, so a *nested* ``upstream/data/SchemaExplorer`` submodule would
    be rejected by Git's submodule-of-submodule prohibition.

    Preference order:
      1. <data-root>/DumpSource2/schemas.json[.gz]   (future: DumpSource2
                                                      ships the JSON directly)
      2. <data-root>/../schema-explorer/schemas/cs2.json[.gz]  (current)
    """
    sibling = data_root.parent / "schema-explorer"
    candidates = [
        data_root / "DumpSource2" / "schemas.json.gz",
        data_root / "DumpSource2" / "schemas.json",
        sibling / "schemas" / "cs2.json.gz",
        sibling / "schemas" / "cs2.json",
    ]
    for p in candidates:
        if p.is_file():
            return p
    return None


# ---------------------------------------------------------------------------
# Proto loader (protoc → FileDescriptorSet)
# ---------------------------------------------------------------------------
#
# Proto loading uses protoc, not a regex parser: protoc emits a binary
# FileDescriptorSet for each input file and we walk it via
# google.protobuf.descriptor_pb2.  This gives us oneofs, services,
# default values, source-info comments, and full type resolution for free.
#
# Why per-file rather than one big set: CS2's protobuf dump has cross-file
# enum-value collisions (e.g. ``k_EMsgGCSystemMessage`` appears in both
# ``base_gcmessages.proto`` and ``enums_clientserver.proto`` — protoc treats
# enum values as global siblings under proto2 scoping rules).  Compiling
# without ``--include_imports`` keeps each file isolated; the conflict never
# materialises and downstream consumers (proto codegens) can resolve imports
# themselves at consume time.

# Mapping from FieldDescriptorProto.Type enum to the legacy parser's type-string
# form.  Keyed by the numeric enum value so we don't have to import the proto
# module at module-load time (the import is deferred into the loader).
_PROTO_FIELD_TYPE_NAMES: dict[int, str] = {
    1:  "double",   2:  "float",   3:  "int64",   4:  "uint64",
    5:  "int32",    6:  "fixed64", 7:  "fixed32", 8:  "bool",
    9:  "string",   10: "group",   12: "bytes",   13: "uint32",
    15: "sfixed32", 16: "sfixed64", 17: "sint32",  18: "sint64",
    # 11 (TYPE_MESSAGE) and 14 (TYPE_ENUM) carry a ``type_name`` instead and
    # are resolved by ``_proto_type_string`` below.
}


def _proto_type_string(field_proto: Any) -> str:
    """Render a FieldDescriptorProto's type as the legacy string form
    (e.g. ``int32``, ``CMsgVector``, ``outer.Inner``).

    Matches what the old regex parser produced — leading ``.`` from a
    fully-qualified ``type_name`` is stripped to keep ``_proto_link_type``
    happy.
    """
    t = field_proto.type
    if t in (11, 14):  # TYPE_MESSAGE, TYPE_ENUM
        return field_proto.type_name.lstrip(".")
    return _PROTO_FIELD_TYPE_NAMES.get(t, "?")


def _proto_label_string(field_proto: Any) -> str:
    """LABEL_OPTIONAL=1, LABEL_REQUIRED=2, LABEL_REPEATED=3."""
    if field_proto.label == 3:
        return "repeated"
    if field_proto.label == 2:
        return "required"
    return "optional"


def _proto_collect_comments(file_proto: Any) -> dict[tuple[int, ...], str]:
    """Walk SourceCodeInfo and return a path→comment map.

    Each ``Location`` entry's ``path`` is a sequence of field-number/index
    pairs that uniquely identifies the construct in the file (e.g.
    ``[4, 2, 2, 0]`` = file.message_type[2].field[0]).  We concatenate
    leading + trailing comments, strip ``//``-style noise, and return the
    text trimmed.
    """
    comments: dict[tuple[int, ...], str] = {}
    if not file_proto.HasField("source_code_info"):
        return comments
    for loc in file_proto.source_code_info.location:
        text_parts: list[str] = []
        if loc.leading_comments:
            text_parts.append(loc.leading_comments)
        if loc.trailing_comments:
            text_parts.append(loc.trailing_comments)
        if not text_parts:
            continue
        text = " ".join(text_parts)
        # Normalise whitespace and drop the leading-* asterisks some doc
        # comments use; we want a single-line description for table cells.
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            comments[tuple(loc.path)] = text
    return comments


# Field-number constants from descriptor.proto.  Hardcoded so the SourceCodeInfo
# walker doesn't need to introspect the descriptor module.
_FILE_MESSAGE_TYPE = 4   # FileDescriptorProto.message_type
_FILE_ENUM_TYPE    = 5   # FileDescriptorProto.enum_type
_MSG_FIELD         = 2   # DescriptorProto.field
_MSG_NESTED_TYPE   = 3   # DescriptorProto.nested_type
_MSG_ENUM_TYPE     = 4   # DescriptorProto.enum_type
_ENUM_VALUE        = 2   # EnumDescriptorProto.value


def _proto_field_to_dict(
    field_proto: Any,
    comments: dict[tuple[int, ...], str],
    path: tuple[int, ...],
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "type": _proto_type_string(field_proto),
        "name": field_proto.name,
        "number": str(field_proto.number),
        "label": _proto_label_string(field_proto),
        "comment": comments.get(path, ""),
    }
    if field_proto.HasField("default_value"):
        out["default"] = field_proto.default_value
    # Membership in a `oneof { ... }` group — descriptor stores the index
    # into the parent message's oneof_decl list.  We resolve to the name
    # at the message level where we have access to that list.
    if field_proto.HasField("oneof_index"):
        out["oneof_index"] = field_proto.oneof_index
    # Field-level options that affect wire format / API surface.
    if field_proto.HasField("options"):
        opts = field_proto.options
        if opts.deprecated:
            out["deprecated"] = True
        if opts.HasField("packed"):
            out["packed"] = opts.packed
    return out


def _proto_enum_to_dict(
    enum_proto: Any,
    comments: dict[tuple[int, ...], str],
    path: tuple[int, ...],
) -> dict[str, Any]:
    return {
        "name": enum_proto.name,
        "comments": [comments[path]] if path in comments else [],
        "values": [
            {"name": v.name, "number": str(v.number)}
            for v in enum_proto.value
        ],
    }


def _proto_message_to_dict(
    msg_proto: Any,
    comments: dict[tuple[int, ...], str],
    path: tuple[int, ...],
) -> dict[str, Any]:
    fields = [
        _proto_field_to_dict(f, comments, path + (_MSG_FIELD, i))
        for i, f in enumerate(msg_proto.field)
    ]
    # Resolve oneof group membership: each oneof has a name and groups
    # the fields whose oneof_index points at it.  We expose the name on
    # each grouped field (legacy ``oneof_index`` stays available for
    # consumers that prefer the integer).
    oneof_names = [o.name for o in msg_proto.oneof_decl]
    for fld in fields:
        if "oneof_index" in fld and 0 <= fld["oneof_index"] < len(oneof_names):
            fld["oneof"] = oneof_names[fld["oneof_index"]]
    return {
        "name": msg_proto.name,
        "comments": [comments[path]] if path in comments else [],
        "fields": fields,
        "nested": [
            _proto_message_to_dict(n, comments, path + (_MSG_NESTED_TYPE, i))
            for i, n in enumerate(msg_proto.nested_type)
        ],
        "enums": [
            _proto_enum_to_dict(e, comments, path + (_MSG_ENUM_TYPE, i))
            for i, e in enumerate(msg_proto.enum_type)
        ],
        "oneofs": [
            {"name": o.name, "fields": [f["name"] for f in fields if f.get("oneof") == o.name]}
            for o in msg_proto.oneof_decl
        ],
    }


def _proto_descriptor_to_dict(file_proto: Any) -> dict[str, Any]:
    """Convert a FileDescriptorProto into the legacy proto-summary dict
    (with extras: package, syntax, oneofs, deprecated/packed flags)."""
    comments = _proto_collect_comments(file_proto)
    out = {
        "filename": file_proto.name,
        "imports": list(file_proto.dependency),
        "messages": [
            _proto_message_to_dict(m, comments, (_FILE_MESSAGE_TYPE, i))
            for i, m in enumerate(file_proto.message_type)
        ],
        "enums": [
            _proto_enum_to_dict(e, comments, (_FILE_ENUM_TYPE, i))
            for i, e in enumerate(file_proto.enum_type)
        ],
    }
    # File-level metadata that consumers need for canonical naming and
    # codegen targeting — none of which the regex parser captured.
    if file_proto.package:
        out["package"] = file_proto.package
    if file_proto.syntax:
        out["syntax"] = file_proto.syntax
    return out


def load_proto_descriptors(
    protobufs_root: Path,
    protoc_bin: str = "protoc",
) -> list[dict[str, Any]]:
    """Compile each .proto under *protobufs_root* and return summary dicts.

    Replaces the old regex-based ``parse_proto_file`` walk.  See the
    ``Proto loader`` block comment above for the design rationale.
    """
    if shutil.which(protoc_bin) is None:
        raise RuntimeError(
            f"{protoc_bin!r} not found in PATH.  Install Protocol Buffers "
            "compiler (`brew install protobuf` / "
            "`apt install protobuf-compiler`) or pass --no-protos."
        )
    try:
        from google.protobuf import descriptor_pb2
    except ImportError as exc:
        raise RuntimeError(
            "python protobuf runtime not installed: pip install protobuf"
        ) from exc

    proto_paths = sorted(protobufs_root.glob("*.proto"))
    results: list[dict[str, Any]] = []

    with tempfile.TemporaryDirectory(prefix="cs2-protoset-") as tmp:
        tmp_dir = Path(tmp)
        for proto_path in proto_paths:
            out_pb = tmp_dir / f"{proto_path.stem}.pb"
            cmd = [
                protoc_bin,
                f"--proto_path={protobufs_root}",
                f"--descriptor_set_out={out_pb}",
                "--include_source_info",
                str(proto_path),
            ]
            try:
                subprocess.run(cmd, check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as exc:
                # Per-file, isolated compile.  A genuine syntax error in the
                # upstream dump shouldn't sink the whole run — surface it
                # and continue, matching the legacy parser's tolerance.
                print(
                    f"  WARNING: protoc failed on {proto_path.name}: "
                    f"{exc.stderr.strip()}",
                    file=sys.stderr,
                )
                continue

            with out_pb.open("rb") as fh:
                fds = descriptor_pb2.FileDescriptorSet.FromString(fh.read())

            for fdp in fds.file:
                # We didn't pass --include_imports so the set should contain
                # only the file we asked for, but be paranoid.
                if fdp.name != proto_path.name:
                    continue
                results.append(_proto_descriptor_to_dict(fdp))
    return results


def parse_convars(path: Path) -> list[dict]:
    """Parse DumpSource2/convars.txt.

    Format per entry:
        name value (flag1 flag2 ...)
        \\tdescription text
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    convars: list[dict] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line or line.startswith("\t") or line.startswith(" "):
            i += 1
            continue
        # Header line: name [default_value] (flags)
        m = re.match(r"^(\S+)\s+(.*?)\s*\(([^)]*)\)\s*$", line)
        if m:
            name, default, flags_raw = m.group(1), m.group(2), m.group(3)
            description = ""
            if i + 1 < len(lines) and lines[i + 1].startswith("\t"):
                description = lines[i + 1].strip()
                i += 1
            convars.append({
                "name": name,
                "default": default.strip(),
                "flags": [f.strip() for f in flags_raw.split() if f.strip()],
                "description": description,
            })
        i += 1
    return convars


def parse_commands(path: Path) -> list[dict]:
    """Parse DumpSource2/commands.txt.

    Format per entry:
        name (flag1 flag2 ...)
        \\tdescription text
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    commands: list[dict] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line or line.startswith("\t") or line.startswith(" "):
            i += 1
            continue
        m = re.match(r"^(\S+)\s*\(([^)]*)\)\s*$", line)
        if m:
            name, flags_raw = m.group(1), m.group(2)
            description = ""
            if i + 1 < len(lines) and lines[i + 1].startswith("\t"):
                description = lines[i + 1].strip()
                i += 1
            commands.append({
                "name": name,
                "flags": [f.strip() for f in flags_raw.split() if f.strip()],
                "description": description,
            })
        i += 1
    return commands


# ---------------------------------------------------------------------------
# Game-events parser  (Valve KeyValues1 format)
# ---------------------------------------------------------------------------

# Known field types in .gameevents files and their JSON Schema equivalents.
_GAMEEVENTS_TYPE_MAP: dict[str, dict[str, str]] = {
    "none":                       {"type": "null",    "description": "Value is not networked"},
    "string":                     {"type": "string",  "description": "A zero-terminated string"},
    "bool":                       {"type": "boolean", "description": "Unsigned int, 1 bit"},
    "byte":                       {"type": "integer", "description": "Unsigned int, 8 bit"},
    "short":                      {"type": "integer", "description": "Signed int, 16 bit"},
    "long":                       {"type": "integer", "description": "Signed int, 32 bit"},
    "int":                        {"type": "integer", "description": "Signed integer"},
    "float":                      {"type": "number",  "description": "Float, 32 bit"},
    "uint64":                     {"type": "string",  "description": "Unsigned 64-bit integer (string-encoded)"},
    "local":                      {"type": "string",  "description": "Any data, not networked"},
    "player_controller":          {"type": "integer", "description": "Player controller entity reference"},
    "player_controller_and_pawn": {"type": "integer", "description": "Player controller + pawn entity reference"},
    "player_pawn":                {"type": "integer", "description": "Player pawn entity reference"},
    "ehandle":                    {"type": "integer", "description": "Entity handle"},
}

# These keys inside an event body are event-level metadata, not field defs.
_GAMEEVENTS_META_KEYS = {"local", "reliable"}


def parse_gameevents_file(path: Path) -> list[dict[str, Any]]:
    """Parse a Valve KeyValues1 ``.gameevents`` file.

    Returns a list of event dicts, each with:
        name        – event name
        comment     – trailing ``//`` comment on the event name line
        source      – basename of the originating file (e.g. ``mod.gameevents``)
        properties  – dict of event-level metadata (``local``, ``reliable``)
        fields      – list of ``{name, type, comment}`` dicts
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    source = path.name
    events: list[dict[str, Any]] = []
    lines = text.splitlines()
    i = 0
    total = len(lines)

    def _strip_comment(line: str) -> tuple[str, str]:
        """Return (code_part, comment_text) splitting on the first ``//``."""
        idx = line.find("//")
        if idx == -1:
            return line, ""
        return line[:idx], line[idx + 2:].strip()

    # Skip until the first top-level opening brace (root container).
    while i < total:
        code, _ = _strip_comment(lines[i])
        if "{" in code:
            i += 1
            break
        i += 1

    # Now we're inside the root object.  Each event is:
    #   "event_name"  // optional comment
    #   {
    #       "field" "type"  // optional comment
    #       ...
    #   }
    depth = 0
    pending_name: str | None = None
    pending_comment = ""
    # Collect comments that appear above an event name for group/section context
    section_comments: list[str] = []

    while i < total:
        raw_line = lines[i]
        code, comment = _strip_comment(raw_line)
        stripped = code.strip()
        i += 1

        # Pure comment line — accumulate for section headings
        if not stripped and comment:
            section_comments.append(comment)
            continue

        # Blank line
        if not stripped:
            # Reset section comments on blank non-comment lines only if
            # we haven't started an event yet.
            if pending_name is None:
                section_comments = []
            continue

        # Opening brace for an event body
        if stripped == "{" and depth == 0 and pending_name is not None:
            depth = 1
            event: dict[str, Any] = {
                "name": pending_name,
                "comment": pending_comment,
                "source": source,
                "properties": {},
                "fields": [],
            }
            pending_name = None
            pending_comment = ""
            section_comments = []

            # Parse event body
            while i < total:
                braw = lines[i]
                bcode, bcomment = _strip_comment(braw)
                bstripped = bcode.strip()
                i += 1

                if bstripped == "}":
                    depth = 0
                    break
                if not bstripped:
                    continue

                # Match key-value pairs: "key" "value"
                kv_match = re.match(
                    r'^\s*"([^"]+)"\s+"([^"]*)"', braw
                )
                if kv_match:
                    key = kv_match.group(1)
                    val = kv_match.group(2)
                    if key in _GAMEEVENTS_META_KEYS:
                        event["properties"][key] = val
                    else:
                        event["fields"].append({
                            "name": key,
                            "type": val,
                            "comment": bcomment,
                        })
                # Standalone quoted key with no value (shouldn't normally happen)
                # Skip it gracefully.
            events.append(event)
            continue

        # Closing brace of the root container
        if stripped == "}":
            break

        # Event name line: "event_name" // optional comment
        name_match = re.match(r'^\s*"([^"]+)"', raw_line)
        if name_match:
            pending_name = name_match.group(1)
            pending_comment = comment
            continue

    return events


def parse_all_gameevents(data_root: Path) -> list[dict[str, Any]]:
    """Find and parse all ``.gameevents`` files under the data tree.

    Searches the three known locations and any other ``.gameevents`` files.
    Returns a flat list of event dicts.
    """
    all_events: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    for ge_file in sorted(data_root.rglob("*.gameevents")):
        real = str(ge_file.resolve())
        if real in seen_paths:
            continue
        seen_paths.add(real)
        all_events.extend(parse_gameevents_file(ge_file))
    return all_events


# ---------------------------------------------------------------------------
# Overlay loader
# ---------------------------------------------------------------------------

def load_overlays(overlays_root: Path) -> dict[str, dict]:
    """Walk overlays_root and load all YAML annotation files.

    Supports two formats:

    *Single-entity* (legacy): ``overlays/{module}/{EntityName}.yml``
        The file content is the overlay for exactly one entity.
        Key → ``{module}/{EntityName}``

    *Multi-entity* (module-level): ``overlays/{module}.yml``
        Top-level YAML keys are entity / message names; their values are
        individual overlay dicts.  Each entry expands to key
        ``{module}/{EntityName}``.

        Module-level files are *also* stored raw under the bare module
        key so consumers wanting the wrapped shape (for example
        ``gameevents.yml``'s top-level ``events:`` mapping, which the
        gameevents schema generator reads as a unit) can fetch the
        file content directly via ``overlays[module]``.

    Both formats can coexist.  If the same key appears in both, the
    single-entity file (processed last due to ``sorted``) wins.
    """
    if not HAS_YAML:
        return {}
    overlays: dict[str, dict] = {}
    for yml in sorted(overlays_root.rglob("*.yml")):
        try:
            data = yaml.safe_load(yml.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        rel = yml.relative_to(overlays_root).with_suffix("")
        key = str(rel).replace("\\", "/")
        parts = key.split("/")
        if len(parts) == 1:
            # Module-level multi-entity file: each top-level key is an
            # entity name.  Also keep the raw file content under the
            # bare module key so consumers that want the wrapped shape
            # (e.g. ``gameevents.yml`` with a top-level ``events:``
            # mapping) can retrieve it directly.
            module = parts[0]
            overlays[module] = data
            for entity_name, entity_data in data.items():
                if isinstance(entity_data, dict):
                    overlays[f"{module}/{entity_name}"] = entity_data
        else:
            # Single-entity file (legacy format): use path as-is.
            overlays[key] = data
    return overlays


def get_overlay(overlays: dict[str, dict], module: str, name: str) -> dict:
    """Look up an overlay by module/name; fall back to just name."""
    key = f"{module}/{name}"
    if key in overlays:
        return overlays[key]
    # Also try matching by name alone across any module
    for k, v in overlays.items():
        if k.endswith(f"/{name}"):
            return v
    return {}



# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------



def _extract_type_refs(type_str: str, entities: dict[str, dict]) -> list[str]:
    """Return names of known schema entities referenced in a field type string."""
    seen: list[str] = []
    for m in re.finditer(r"\b[A-Z_]\w+\b", type_str):
        word = m.group(0)
        if word in entities and word not in seen:
            seen.append(word)
    return seen


def _mermaid_safe(name: str) -> str:
    """Make a name safe for Mermaid by quoting if needed."""
    if re.match(r"^[A-Za-z_]\w*$", name):
        return name
    return f'"{name}"'


def _entity_anchor(name: str) -> str:
    """Return the kramdown heading anchor for an entity name.

    Mirrors kramdown's default auto-id algorithm: lowercase, drop everything
    that isn't a word char, space, or hyphen, then turn spaces into hyphens.
    Critical for nested-class names like ``Foo::Bar`` that the cs2.json
    loader produces — kramdown strips the ``:`` characters from the heading
    anchor, so the index link must do the same or it dangles.
    """
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    return slug.strip().replace(" ", "-")


# Proto primitive scalar types that do not get anchor-linked.
_PROTO_PRIMITIVES = {
    "double", "float", "int32", "int64", "uint32", "uint64",
    "sint32", "sint64", "fixed32", "fixed64", "sfixed32", "sfixed64",
    "bool", "string", "bytes",
}


def _proto_anchor(name: str) -> str:
    """Return the GitHub Markdown anchor for a proto section heading like ``### `Name` ``."""
    # GitHub lowercases and strips all chars except word chars (a-z0-9_) and hyphens.
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    return slug.strip().replace(" ", "-")


def _proto_link_type(ftype: str, local_names: set[str]) -> str:
    """Return plain type text for primitives; an anchor link for known local types."""
    raw = ftype.lstrip(".")
    simple = raw.split(".")[-1]
    if simple in _PROTO_PRIMITIVES or simple not in local_names:
        return raw
    return f"[{simple}](#{_proto_anchor(simple)})"


def _md_link_type(
    type_str: str, entities: dict[str, dict], current_module: str = ""
) -> str:
    """Wrap known entity names in a type string with Markdown links (anchor-based).

    When *current_module* is supplied and the referenced entity also exists in
    that module (as a duplicate), the link targets the current-module page so
    readers stay within the same schema page.
    """
    def replace(m: re.Match) -> str:
        word = m.group(0)
        if word in entities:
            e = entities[word]
            mod = e["module"]
            # Prefer a same-module link when the entity exists in current_module
            if current_module and current_module != mod:
                if any(d["module"] == current_module for d in e.get("duplicates", [])):
                    mod = current_module
            return f"[{word}](../schemas/{mod}.md#{_entity_anchor(word)})"
        return word

    return re.sub(r"\b[A-Z_]\w+\b", replace, type_str)


def _md_front_matter(**kwargs: str) -> str:
    """Render a YAML front matter block for Jekyll."""
    lines = ["---"]
    for key, val in kwargs.items():
        # Quote values that might confuse YAML
        if any(c in str(val) for c in (':', '#', '[', ']', '{', '}')):
            lines.append(f'{key}: "{val}"')
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _build_md_relationship_diagram(
    name: str,
    entity: dict,
    entities: dict[str, dict],
) -> list[str]:
    """Build Mermaid classDiagram lines for an entity's relationships."""
    lines: list[str] = []
    seen_edges: set[tuple[str, str]] = set()

    # Walk up inheritance chain (up to 5 levels)
    chain: list[str] = [name]
    current = entity
    for _ in range(5):
        bases = current.get("bases", [])
        if not bases:
            break
        parent = bases[0]
        chain.append(parent)
        current = entities.get(parent, {})
        if not current:
            break

    for i in range(len(chain) - 1):
        child = chain[i]
        parent = chain[i + 1]
        edge = (parent, child)
        if edge not in seen_edges:
            lines.append(f"    {_mermaid_safe(parent)} <|-- {_mermaid_safe(child)}")
            seen_edges.add(edge)

    for e in entities.values():
        if name in e.get("bases", []) and e["name"] != name:
            edge = (name, e["name"])
            if edge not in seen_edges:
                lines.append(f"    {_mermaid_safe(name)} <|-- {_mermaid_safe(e['name'])}")
                seen_edges.add(edge)

    comp_count = 0
    for fld in entity.get("fields", []):
        if comp_count >= 10:
            break
        for ref in _extract_type_refs(fld.get("type", ""), entities):
            if ref == name or comp_count >= 10:
                continue
            edge = (name, ref)
            if edge not in seen_edges:
                ftype = fld.get("type", "")
                arrow = "-->" if ("*" in ftype or "CHandle" in ftype) else "*--"
                lines.append(f"    {_mermaid_safe(name)} {arrow} {_mermaid_safe(ref)}")
                seen_edges.add(edge)
                comp_count += 1

    return lines


def generate_schemas_index_md(
    entities: dict[str, dict],
    overlays: dict[str, dict],
    out_dir: Path,
    diagram_modules: set[str] | None = None,
) -> None:
    """Generate schemas.md (master index) and per-module Markdown pages.

    Entity details are embedded directly in the per-module pages using
    ``### EntityName`` headings (anchor: ``#entityname``) so no separate
    per-entity files are needed.
    """
    by_module: dict[str, list[dict]] = defaultdict(list)
    for entity in entities.values():
        by_module[entity["module"]].append(entity)
        # Also include duplicates (same entity name, different module e.g. client+server)
        for dup in entity.get("duplicates", []):
            by_module[dup["module"]].append(dup)

    # Master schemas.md
    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="Schemas", nav_order="2"))
    lines.append("# Schema Reference\n")
    lines.append("All entities and types extracted from CS2's schema dump, organised by module.\n")
    lines.append("## Modules\n")
    lines.append("| Module | Entities | UML |")
    lines.append("|--------|----------|-----|")
    for mod in sorted(by_module):
        count = len(by_module[mod])
        has_diagram = diagram_modules is None or mod in diagram_modules
        uml_cell = f"[📊 Diagram](diagrams/{mod}.md)" if has_diagram else "—"
        lines.append(
            f"| [{mod}](schemas/{mod}.md) | {count} | {uml_cell} |"
        )
    lines.append("")
    (out_dir / "schemas.md").write_text("\n".join(lines), encoding="utf-8")

    # Per-module pages – entity details embedded with heading anchors
    (out_dir / "schemas").mkdir(exist_ok=True)
    for mod, ents in by_module.items():
        sorted_ents = sorted(ents, key=lambda x: x["name"])
        m_lines: list[str] = []
        m_lines.append(_md_front_matter(
            layout="default",
            title=mod,
            parent="Schemas",
            nav_exclude="true",
        ))
        m_lines.append(f"# Module: {mod}\n")
        if diagram_modules is None or mod in diagram_modules:
            m_lines.append(f"[📊 View UML Diagram](../diagrams/{mod}.md)\n")

        # Quick-reference index table with anchor links
        m_lines.append("| Name | Kind | Bases | Fields |")
        m_lines.append("|------|------|-------|--------|")
        for e in sorted_ents:
            anchor = _entity_anchor(e["name"])
            bases_str = ", ".join(e.get("bases", []))
            field_count = len(e.get("fields", []))
            m_lines.append(
                f"| [{e['name']}](#{anchor}) | {e['kind']} | {bases_str} | {field_count} |"
            )
        m_lines.append("")

        # Full entity detail sections
        m_lines.append("---\n")
        for e in sorted_ents:
            name = e["name"]
            kind = e["kind"]
            overlay = get_overlay(overlays, mod, name)

            m_lines.append(f"### {name}\n")

            if overlay.get("description"):
                m_lines.append(f"{overlay['description']}\n")
            if overlay.get("notes"):
                m_lines.append(f"> 📝 {overlay['notes']}\n")
            if overlay.get("warning"):
                m_lines.append(f"> ⚠️ {overlay['warning']}\n")

            # Bases / derived
            if e.get("bases"):
                base_links = []
                for b in e["bases"]:
                    if b in entities:
                        bmod = entities[b]["module"]
                        # Prefer same-module link when the base also exists in this module
                        if bmod != mod and any(
                            d["module"] == mod for d in entities[b].get("duplicates", [])
                        ):
                            bmod = mod
                        base_links.append(f"[{b}]({bmod}.md#{_entity_anchor(b)})")
                    else:
                        base_links.append(b)
                m_lines.append(f"**Inherits from:** {', '.join(base_links)}\n")

            derived = sorted(
                [d for d in entities.values() if name in d.get("bases", [])],
                key=lambda x: x["name"],
            )
            if derived:
                links = [
                    f"[{d['name']}]({d['module']}.md#{_entity_anchor(d['name'])})"
                    for d in derived
                ]
                m_lines.append(f"**Derived by:** {', '.join(links)}\n")

            # Metadata tags – exclude MNetworkVarNames entries because they
            # only repeat the field name/type already in the Fields table.
            if e.get("metadata"):
                tags = [
                    f"`{_format_metadata(m)}`" for m in e["metadata"]
                    if isinstance(m, dict)
                    and m.get("name")
                    and not m["name"].startswith("MNetworkVarNames")
                ]
                if tags:
                    m_lines.append(f"**Metadata:** {', '.join(tags)}\n")

            # Relationship diagram
            diagram_lines = _build_md_relationship_diagram(name, e, entities)
            if diagram_lines:
                m_lines.append("**Relationships:**\n")
                m_lines.append("```mermaid")
                m_lines.append("classDiagram")
                m_lines.extend(diagram_lines)
                m_lines.append("```\n")

            # Fields / enum values
            if kind == "enum":
                vals = e.get("fields", [])
                if vals:
                    m_lines.append("**Values:**\n")
                    # Description column surfaces upstream-supplied
                    # MPropertyFriendlyName / MPropertyDescription on enum
                    # members — these are the human labels DumpSource2
                    # extracted from runtime reflection and would otherwise
                    # disappear into the JSON (1017 enum members carry
                    # this info).
                    m_lines.append("| Name | Value | Description |")
                    m_lines.append("|------|-------|-------------|")
                    for fld in vals:
                        desc = _metadata_friendly_text(fld.get("annotations"))
                        desc = desc.replace("|", "\\|")
                        m_lines.append(
                            f"| `{fld['name']}` | {fld.get('value', '')} | {desc} |"
                        )
                    m_lines.append("")
            else:
                fields = e.get("fields", [])
                if fields:
                    overlay_fields: dict = overlay.get("fields", {}) or {}
                    m_lines.append("**Fields:**\n")
                    m_lines.append("| Name | Type | Annotations |")
                    m_lines.append("|------|------|-------------|")
                    for fld in fields:
                        fname = fld.get("name", "")
                        ftype = fld.get("type", "")
                        annots = fld.get("annotations", [])
                        fover = overlay_fields.get(fname, {}) if isinstance(overlay_fields, dict) else {}
                        type_linked = _md_link_type(ftype, entities, mod)
                        annot_str = " ".join(
                            f"`{_format_metadata(a)}`"
                            for a in annots
                            if isinstance(a, dict) and a.get("name")
                        )
                        desc_parts = []
                        if fover and isinstance(fover, dict):
                            if fover.get("description"):
                                desc_parts.append(str(fover["description"]))
                            if fover.get("notes"):
                                desc_parts.append(f"*{fover['notes']}*")
                        if annot_str:
                            desc_parts.append(annot_str)
                        m_lines.append(f"| `{fname}` | {type_linked} | {' '.join(desc_parts)} |")
                    m_lines.append("")

        (out_dir / "schemas" / f"{mod}.md").write_text(
            "\n".join(m_lines), encoding="utf-8"
        )


def generate_module_uml_md(entities: dict[str, dict], out_dir: Path) -> set[str]:
    """Generate per-module UML Markdown pages at diagrams/{mod}.md."""
    by_module: dict[str, list[dict]] = defaultdict(list)
    for e in entities.values():
        by_module[e["module"]].append(e)
        # Also include duplicates (same entity name, different module e.g. client+server)
        for dup in e.get("duplicates", []):
            by_module[dup["module"]].append(dup)

    (out_dir / "diagrams").mkdir(exist_ok=True)
    generated: set[str] = set()

    for mod, ents in sorted(by_module.items()):
        ent_names = {e["name"] for e in ents}
        diagram_lines: list[str] = []
        seen_edges: set[tuple[str, str]] = set()

        for e in ents:
            for base in e.get("bases", []):
                edge = (base, e["name"])
                if edge not in seen_edges:
                    diagram_lines.append(
                        f"    {_mermaid_safe(base)} <|-- {_mermaid_safe(e['name'])}"
                    )
                    seen_edges.add(edge)

        for e in ents:
            ename = e["name"]
            for fld in e.get("fields", []):
                for ref in _extract_type_refs(fld.get("type", ""), entities):
                    if ref == ename or ref not in ent_names:
                        continue
                    edge = (ename, ref)
                    if edge not in seen_edges:
                        ftype = fld.get("type", "")
                        arrow = "-->" if ("*" in ftype or "CHandle" in ftype) else "*--"
                        diagram_lines.append(
                            f"    {_mermaid_safe(ename)} {arrow} {_mermaid_safe(ref)}"
                        )
                        seen_edges.add(edge)
            if len(diagram_lines) >= 300:
                break

        if not diagram_lines:
            continue

        cap = 300
        capped = diagram_lines[:cap]
        extra = len(diagram_lines) - cap
        count_note = f" (showing {cap} of {len(diagram_lines)} relationships)" if extra > 0 else ""

        md_lines: list[str] = []
        md_lines.append(_md_front_matter(
            layout="default",
            title=f"UML: {mod}",
            parent="Schemas",
            nav_exclude="true",
        ))
        md_lines.append(f"# UML: {mod}\n")
        md_lines.append(
            f"Class relationships (inheritance and composition) for the `{mod}` module{count_note}.\n"
        )
        md_lines.append(
            "**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer\n"
        )
        md_lines.append("```mermaid")
        md_lines.append("classDiagram")
        md_lines.extend(capped)
        md_lines.append("```\n")

        (out_dir / "diagrams" / f"{mod}.md").write_text(
            "\n".join(md_lines), encoding="utf-8"
        )
        generated.add(mod)

    return generated


def _build_proto_mermaid(proto: dict) -> list[str]:
    """Build Mermaid classDiagram lines for a proto file.

    Returns a list of lines to be embedded inside a ``classDiagram`` block.
    Returns an empty list when there is nothing to diagram.
    """
    _SCALARS = {
        "double", "float", "int32", "int64", "uint32", "uint64",
        "sint32", "sint64", "fixed32", "fixed64", "sfixed32", "sfixed64",
        "bool", "string", "bytes",
    }

    def _flat_msgs(msgs: list) -> list:
        result: list = []
        for m in msgs:
            result.append(m)
            result.extend(_flat_msgs(m.get("nested", [])))
        return result

    all_msgs = _flat_msgs(proto.get("messages", []))
    all_enums = list(proto.get("enums", []))
    for msg in all_msgs:
        all_enums.extend(msg.get("enums", []))

    if not all_msgs and not all_enums:
        return []

    local_names: set[str] = {m["name"] for m in all_msgs} | {e["name"] for e in all_enums}

    lines: list[str] = ["direction LR", ""]

    for msg in all_msgs:
        safe = _mermaid_safe(msg["name"])
        lines.append(f"  class {safe} {{")
        for fld in msg.get("fields", []):
            ftype = fld["type"].lstrip(".")
            type_str = f"List~{ftype}~" if fld.get("label") == "repeated" else ftype
            lines.append(f"    +{type_str} {fld['name']}")
        lines.append("  }")
        lines.append("")

    # Relationship arrows (message-type fields within the same file)
    seen_arrows: set[str] = set()
    for msg in all_msgs:
        src = _mermaid_safe(msg["name"])
        for fld in msg.get("fields", []):
            raw = fld["type"].lstrip(".")
            simple = raw.split(".")[-1]
            if simple not in local_names or simple in _SCALARS:
                continue
            tgt = _mermaid_safe(simple)
            arrow_key = f"{src}-->{tgt}"
            if arrow_key in seen_arrows:
                continue
            seen_arrows.add(arrow_key)
            suffix = "[]" if fld.get("label") == "repeated" else ""
            lines.append(f"  {src} --> {tgt} : {fld['name']}{suffix}")
    if seen_arrows:
        lines.append("")

    for en in all_enums:
        safe = _mermaid_safe(en["name"])
        lines.append(f"  class {safe}{{")
        lines.append("    <<enumeration>>")
        for v in en.get("values", []):
            lines.append(f"    {v['name']}")
        lines.append("  }")
        lines.append("")

    return lines


def generate_protobufs_md_page(
    protos: list[dict],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate protobufs.md and per-file proto Markdown pages."""
    (out_dir / "proto").mkdir(exist_ok=True)

    # Master index
    idx_lines: list[str] = []
    idx_lines.append(_md_front_matter(layout="default", title="Protobufs", nav_order="3"))
    idx_lines.append("# Protobuf Reference\n")
    idx_lines.append("Network message definitions and game event structures from CS2's Protobufs directory.\n")
    idx_lines.append("| File | Messages | Enums |")
    idx_lines.append("|------|----------|-------|")
    for proto in sorted(protos, key=lambda x: x["filename"]):
        fname = proto["filename"]
        stem = fname.removesuffix(".proto")
        msg_count = len(proto.get("messages", []))
        enum_count = len(proto.get("enums", []))
        idx_lines.append(f"| [{fname}](proto/{stem}.md) | {msg_count} | {enum_count} |")
    idx_lines.append("")
    (out_dir / "protobufs.md").write_text("\n".join(idx_lines), encoding="utf-8")

    # Per-file pages
    for proto in protos:
        pfile = proto["filename"]
        stem = pfile.removesuffix(".proto")
        overlay = overlays.get(f"protobufs/{stem}", {})

        p_lines: list[str] = []
        p_lines.append(_md_front_matter(
            layout="default",
            title=pfile,
            parent="Protobufs",
            nav_exclude="true",
        ))
        p_lines.append(f"# `{pfile}`\n")

        # File-level metadata (package + syntax + imports) come from the
        # FileDescriptorProto and matter for codegen consumers.
        meta_bits: list[str] = []
        if proto.get("package"):
            meta_bits.append(f"**Package:** `{proto['package']}`")
        if proto.get("syntax"):
            meta_bits.append(f"**Syntax:** `{proto['syntax']}`")
        if proto.get("imports"):
            meta_bits.append(
                "**Imports:** " + ", ".join(f"`{imp}`" for imp in proto["imports"])
            )
        if meta_bits:
            p_lines.append("  ".join(meta_bits) + "\n")

        if overlay.get("description"):
            p_lines.append(f"{overlay['description']}\n")
        if overlay.get("notes"):
            p_lines.append(f"> 📝 {overlay['notes']}\n")

        # Mermaid class diagram
        diagram = _build_proto_mermaid(proto)
        if diagram:
            p_lines.append("## Diagram\n")
            p_lines.append("```mermaid")
            p_lines.append("classDiagram")
            p_lines.extend(diagram)
            p_lines.append("```\n")

        if proto.get("enums"):
            p_lines.append("## Enums\n")
            for en in proto["enums"]:
                p_lines.append(f"### `{en['name']}`\n")
                p_lines.append("| Name | Value |")
                p_lines.append("|------|-------|")
                for v in en.get("values", []):
                    p_lines.append(f"| `{v['name']}` | {v['number']} |")
                p_lines.append("")

        # Build a set of local type names (messages + enums) for anchor-linking.
        local_names: set[str] = (
            {m["name"] for m in proto.get("messages", [])}
            | {e["name"] for e in proto.get("enums", [])}
        )

        overlay_msgs: dict = overlay.get("messages", {}) or {}
        if proto.get("messages"):
            p_lines.append("## Messages\n")
            for msg in proto["messages"]:
                mname = msg["name"]
                mover = overlay_msgs.get(mname, {}) if isinstance(overlay_msgs, dict) else {}
                p_lines.append(f"### `{mname}`\n")
                if mover and isinstance(mover, dict) and mover.get("description"):
                    p_lines.append(f"{mover['description']}\n")
                if mover and isinstance(mover, dict) and mover.get("notes"):
                    p_lines.append(f"> 📝 {mover['notes']}\n")

                # Surface oneof groups before the fields table so readers
                # know which fields are mutually exclusive.
                if msg.get("oneofs"):
                    nonempty_oneofs = [o for o in msg["oneofs"] if o.get("fields")]
                    if nonempty_oneofs:
                        oneof_bits = ", ".join(
                            f"`{o['name']}` ({', '.join(o['fields'])})"
                            for o in nonempty_oneofs
                        )
                        p_lines.append(f"**Oneofs:** {oneof_bits}\n")

                if msg.get("fields"):
                    overlay_flds: dict = (
                        mover.get("fields", {}) or {}
                        if mover and isinstance(mover, dict) else {}
                    )
                    p_lines.append("| Field | Ordinal | Type | Label | Description |")
                    p_lines.append("|-------|---------|------|-------|-------------|")
                    for fld in sorted(
                        msg["fields"], key=lambda f: int(f.get("number", "0"))
                    ):
                        fname_fld = fld["name"]
                        ftype = fld["type"]
                        label = fld.get("label", "optional")
                        fnum = fld.get("number", "")
                        ftype_display = _proto_link_type(ftype, local_names)
                        # Build description from overlay + proto inline comment + default
                        desc_parts: list[str] = []
                        fover = (
                            overlay_flds.get(fname_fld, {})
                            if isinstance(overlay_flds, dict) else {}
                        )
                        if fover and isinstance(fover, dict) and fover.get("description"):
                            desc_parts.append(str(fover["description"]))
                        comment = fld.get("comment", "")
                        if comment:
                            desc_parts.append(comment)
                        # Field-level descriptor flags worth surfacing.
                        if fld.get("oneof"):
                            desc_parts.append(f"*(oneof: `{fld['oneof']}`)*")
                        if fld.get("deprecated"):
                            desc_parts.append("**deprecated**")
                        if fld.get("packed") is True:
                            desc_parts.append("*(packed)*")
                        default = fld.get("default", "")
                        if default:
                            desc_parts.append(f"*(default: `{default}`)*")
                        desc = " ".join(desc_parts).replace("|", "\\|")
                        p_lines.append(
                            f"| `{fname_fld}` | {fnum} | {ftype_display} | {label} | {desc} |"
                        )
                    p_lines.append("")

        (out_dir / "proto" / f"{stem}.md").write_text("\n".join(p_lines), encoding="utf-8")


def generate_convars_md_page(convars: list[dict], out_dir: Path) -> None:
    """Generate convars.md."""
    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="ConVars", nav_order="4"))
    lines.append("# ConVar Reference\n")
    lines.append("All console variables extracted from CS2.\n")
    lines.append("| Name | Default | Flags | Description |")
    lines.append("|------|---------|-------|-------------|")
    for cv in convars:
        flags = " ".join(f"`{f}`" for f in cv["flags"])
        desc = cv["description"] or ""
        # Escape pipe characters in markdown table cells
        desc = desc.replace("|", "\\|")
        lines.append(f"| `{cv['name']}` | `{cv['default']}` | {flags} | {desc} |")
    lines.append("")
    (out_dir / "convars.md").write_text("\n".join(lines), encoding="utf-8")


def generate_commands_md_page(commands: list[dict], out_dir: Path) -> None:
    """Generate commands.md."""
    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="Commands", nav_order="5"))
    lines.append("# Console Commands\n")
    lines.append("All console commands extracted from CS2.\n")
    lines.append("| Command | Flags | Description |")
    lines.append("|---------|-------|-------------|")
    for cmd in commands:
        flags = " ".join(f"`{f}`" for f in cmd["flags"])
        desc = (cmd["description"] or "").replace("|", "\\|")
        lines.append(f"| `{cmd['name']}` | {flags} | {desc} |")
    lines.append("")
    (out_dir / "commands.md").write_text("\n".join(lines), encoding="utf-8")


def generate_gameevents_md_page(
    gameevents: list[dict[str, Any]],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate gameevents.md – the Game Events documentation page."""
    overlay = overlays.get("gameevents", {})
    overlay_events: dict = overlay.get("events", {}) or {}

    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="Game Events", nav_order="6"))
    lines.append("# Game Events Reference\n")
    lines.append(
        "Game events extracted from CS2's `.gameevents` resource files. "
        "These events are fired by the game engine and server to signal "
        "in-game occurrences such as player actions, round state changes, "
        "and UI notifications.\n"
    )
    if overlay.get("description"):
        lines.append(f"{overlay['description']}\n")
    if overlay.get("notes"):
        lines.append(f"> 📝 {overlay['notes']}\n")

    # Data-type legend
    lines.append("## Field Types\n")
    lines.append("| Type | Description |")
    lines.append("|------|-------------|")
    for tname, tinfo in sorted(_GAMEEVENTS_TYPE_MAP.items()):
        lines.append(f"| `{tname}` | {tinfo['description']} |")
    lines.append("")

    # Group events by source file
    by_source: dict[str, list[dict]] = {}
    for ev in gameevents:
        by_source.setdefault(ev["source"], []).append(ev)

    source_labels: dict[str, str] = {
        "core.gameevents": "Core Engine Events",
        "game.gameevents": "Game Events",
        "mod.gameevents": "CS2 (Counter-Strike) Events",
    }

    # Summary table
    lines.append("## Summary\n")
    lines.append(f"**Total events:** {len(gameevents)}\n")
    lines.append("| Source | Events | Description |")
    lines.append("|--------|--------|-------------|")
    for src in sorted(by_source):
        label = source_labels.get(src, src)
        lines.append(f"| `{src}` | {len(by_source[src])} | {label} |")
    lines.append("")

    # Quick-reference index
    lines.append("## Event Index\n")
    lines.append("| Event | Source | Fields | Description |")
    lines.append("|-------|--------|--------|-------------|")
    for ev in gameevents:
        anchor = ev["name"].lower().replace(" ", "-")
        eov = overlay_events.get(ev["name"], {}) if isinstance(overlay_events, dict) else {}
        desc = ""
        if eov and isinstance(eov, dict) and eov.get("description"):
            desc = str(eov["description"])
        elif ev["comment"]:
            desc = ev["comment"]
        desc = desc.replace("|", "\\|")
        lines.append(
            f"| [{ev['name']}](#{anchor}) | `{ev['source']}` | {len(ev['fields'])} | {desc} |"
        )
    lines.append("")

    # Detailed event sections grouped by source
    lines.append("---\n")
    for src in sorted(by_source):
        label = source_labels.get(src, src)
        lines.append(f"## {label}\n")
        lines.append(f"*Source: `{src}`*\n")

        for ev in by_source[src]:
            ename = ev["name"]
            eov = overlay_events.get(ename, {}) if isinstance(overlay_events, dict) else {}

            lines.append(f"### {ename}\n")

            # Description from overlay, then from inline comment
            if eov and isinstance(eov, dict) and eov.get("description"):
                lines.append(f"{eov['description']}\n")
            elif ev["comment"]:
                lines.append(f"{ev['comment']}\n")

            if eov and isinstance(eov, dict) and eov.get("notes"):
                lines.append(f"> 📝 {eov['notes']}\n")
            if eov and isinstance(eov, dict) and eov.get("warning"):
                lines.append(f"> ⚠️ {eov['warning']}\n")

            # Event-level properties
            if ev["properties"]:
                props = ", ".join(f"`{k}={v}`" for k, v in ev["properties"].items())
                lines.append(f"**Properties:** {props}\n")

            if ev["fields"]:
                overlay_flds: dict = (
                    eov.get("fields", {}) or {}
                    if eov and isinstance(eov, dict) else {}
                )
                lines.append("| Field | Type | Description |")
                lines.append("|-------|------|-------------|")
                for fld in ev["fields"]:
                    fname = fld["name"]
                    ftype = fld["type"]
                    fov = overlay_flds.get(fname, {}) if isinstance(overlay_flds, dict) else {}
                    desc_parts: list[str] = []
                    if fov and isinstance(fov, dict) and fov.get("description"):
                        desc_parts.append(str(fov["description"]))
                    if fld["comment"]:
                        desc_parts.append(fld["comment"])
                    if fov and isinstance(fov, dict) and fov.get("notes"):
                        desc_parts.append(f"*{fov['notes']}*")
                    desc = " ".join(desc_parts).replace("|", "\\|")
                    lines.append(f"| `{fname}` | `{ftype}` | {desc} |")
                lines.append("")
            else:
                lines.append("*No fields — this event carries no additional data.*\n")

    (out_dir / "gameevents.md").write_text("\n".join(lines), encoding="utf-8")


def generate_gameevents_schema(
    gameevents: list[dict[str, Any]],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate ``gameevents_schema.json`` — a community-enriched mirror
    of the parsed ``.gameevents`` registry.

    Format mirrors the natural shape of the upstream KV1 source: a flat
    list of events under top-level ``events``, each preserving its
    parsed ``name`` / ``comment`` / ``source`` / ``properties`` /
    ``fields`` keys.  Field type tags (``bool``, ``byte``, ``short``,
    ``player_controller``, …) come straight from the .gameevents
    sources — see ``_GAMEEVENTS_TYPE_MAP`` for human-readable mappings,
    rendered into the Markdown reference page.

    The single addition is an optional ``annotations`` block on events
    and fields carrying community-curated descriptions / notes /
    warnings from ``docs/overlays/gameevents.yml``.

    See ``generate_cs2_schema`` for the matching cs2_schema.json
    pivot — same pattern, same rationale (JSON Schema 2020-12 was
    abandoned for the entity dump, kept here would be inconsistent).
    """
    overlay = overlays.get("gameevents", {})
    overlay_events: dict = overlay.get("events", {}) or {}

    events_out: list[dict[str, Any]] = []
    for ev in gameevents:
        ename = ev["name"]
        eov = overlay_events.get(ename, {}) if isinstance(overlay_events, dict) else {}

        record: dict[str, Any] = {
            "name": ename,
            "comment": ev.get("comment", ""),
            "source": ev.get("source", ""),
            "properties": dict(ev.get("properties", {})),
            "fields": [
                {
                    "name": fld["name"],
                    "type": fld["type"],
                    "comment": fld.get("comment", ""),
                }
                for fld in ev.get("fields", [])
            ],
        }

        annots = _overlay_annotations(eov)
        if annots:
            record["annotations"] = annots

        # Per-field overlays — same `annotations` projection.
        overlay_flds = eov.get("fields", {}) if isinstance(eov, dict) else {}
        if isinstance(overlay_flds, dict) and overlay_flds:
            for fld in record["fields"]:
                fov = overlay_flds.get(fld["name"])
                fld_annots = _overlay_annotations(fov)
                if fld_annots:
                    fld["annotations"] = fld_annots

        events_out.append(record)

    out: dict[str, Any] = {
        "schema_format_version": SCHEMA_FORMAT_VERSION,
        "events": events_out,
    }
    schema_dir = out_dir / "downstream-codegen-schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)
    (schema_dir / "gameevents_schema.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# CS2 entity schema generation
# ---------------------------------------------------------------------------
#
# cs2_schema.json is now a community-enriched mirror of upstream
# cs2.json.gz from DumpSource2 (no longer a JSON Schema 2020-12 document).
# The earlier JSON Schema attempt was abandoned because standard codegens
# (quicktype, json-schema-to-typescript, NJsonSchema, ...) couldn't handle
# the layered allOf/$ref inheritance and synthetic defs we used to model
# native CS2 types.  See generate_cs2_schema() for details.


def _collect_module_variants(entity: dict[str, Any]) -> list[dict[str, Any]]:
    """Return [primary, *duplicates] in module-sorted order.

    Cross-module twins (e.g. ``CCSPlayerController`` in both ``client`` and
    ``server``) get collapsed to a single in-memory entry by
    ``_add_entity`` (with the alternative variant attached as a
    ``duplicate``).  This helper yields them all so the schema emitter can
    write one record per (module, name).
    """
    variants = [entity, *entity.get("duplicates", [])]
    return sorted(variants, key=lambda v: v.get("module", ""))


def _build_description(
    overlay: dict[str, Any] | None,
    inline_comments: list[str] | None = None,
) -> str | None:
    parts: list[str] = []
    if overlay:
        if overlay.get("description"):
            parts.append(str(overlay["description"]).strip())
    if inline_comments:
        cmt = " ".join(c.strip() for c in inline_comments if c.strip())
        if cmt:
            parts.append(cmt)
    if not parts:
        return None
    return " ".join(parts).strip() or None


def _overlay_annotations(overlay: dict[str, Any] | None) -> dict[str, Any]:
    """Project a (sub-)overlay into the additive ``annotations`` block used
    by cs2_schema.json.  Empty / missing values are skipped so a no-op
    overlay leaves no residue."""
    out: dict[str, Any] = {}
    if not isinstance(overlay, dict):
        return out
    for key in ("description", "notes", "warning"):
        val = overlay.get(key)
        if val:
            out[key] = str(val).strip()
    return out


_KV3_TRAILING_COMMA_RE = re.compile(r",(\s*[}\]])")


def _try_parse_kv3_defaults(value: str) -> Any:
    """Attempt to parse an ``MGetKV3ClassDefaults`` value string as JSON.

    Upstream emits the KV3 defaults as a tab-indented string; the basic
    shape is JSON-compatible but tolerates two non-JSON forms:

    - trailing commas in arrays / objects (stripped)
    - ``<HIDDEN FOR DIFF>`` opaque-value sentinels (mapped to ``null``)

    Returns the parsed object on success, ``None`` on failure.  The raw
    string is *always* preserved on the metadata record; this is an
    additive companion, never a replacement.
    """
    if not isinstance(value, str):
        return None
    if "Could not parse" in value:
        return None
    normalized = value.replace("<HIDDEN FOR DIFF>", "null")
    normalized = _KV3_TRAILING_COMMA_RE.sub(r"\1", normalized)
    try:
        return json.loads(normalized)
    except (json.JSONDecodeError, ValueError):
        return None


def _attach_kv3_value_parsed(metadata: list[dict[str, Any]] | None) -> None:
    """Walk a metadata list and add a ``value_parsed`` companion key to
    every ``MGetKV3ClassDefaults`` entry whose JSON-encoded ``value``
    parses successfully.  Modifies ``metadata`` in place; tolerates a
    missing or non-list input.
    """
    if not isinstance(metadata, list):
        return
    for entry in metadata:
        if not isinstance(entry, dict):
            continue
        if entry.get("name") != "MGetKV3ClassDefaults":
            continue
        parsed = _try_parse_kv3_defaults(entry.get("value"))
        if parsed is not None:
            entry["value_parsed"] = parsed


def _enrich_record(
    raw: dict[str, Any],
    entity: dict[str, Any],
    overlays: dict[str, dict],
) -> dict[str, Any]:
    """Return a deep-copy of ``raw`` with overlay-derived ``annotations``
    blocks layered onto the entity itself, its fields (classes), or its
    members (enums).  ``raw`` stays otherwise byte-identical to upstream
    cs2.json.gz, plus a ``value_parsed`` companion on parseable KV3
    default-metadata entries.
    """
    record = copy.deepcopy(raw)
    overlay = get_overlay(overlays, entity.get("module", ""), entity["name"]) or {}

    annots = _overlay_annotations(overlay)
    if annots:
        record["annotations"] = annots

    _attach_kv3_value_parsed(record.get("metadata"))
    for child in record.get("fields", []) or []:
        _attach_kv3_value_parsed(child.get("metadata"))

    overlay_fields = overlay.get("fields") if isinstance(overlay, dict) else None
    if isinstance(overlay_fields, dict) and overlay_fields:
        children_key = "members" if entity["kind"] == "enum" else "fields"
        for child in record.get(children_key, []):
            cov = overlay_fields.get(child.get("name", ""))
            child_annots = _overlay_annotations(cov)
            if child_annots:
                child["annotations"] = child_annots

    return record


def generate_cs2_schema(
    entities: dict[str, dict],
    overlays: dict[str, dict],
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
) -> Path:
    """Generate ``cs2_schema.json`` — a community-enriched mirror of
    upstream ``cs2.json.gz`` from DumpSource2.

    Format mirrors cs2.json.gz exactly: same top-level keys (``generator``,
    ``revision``, ``version_date``, ``version_time``, ``classes``,
    ``enums``), same per-class and per-enum shape, same field/member
    structure with structured ``type`` objects and ``[{name, value}]``
    metadata.  Consumers can use any tooling that already targets the
    DumpSource2 dump.

    The single addition is an optional ``annotations`` block on classes,
    fields, enums, and members carrying community-curated descriptions,
    notes, and warnings from ``docs/overlays/``.  Entities with no
    overlay match are emitted byte-for-byte as upstream.

    Why not JSON Schema 2020-12: tried and abandoned.  Standard codegens
    (quicktype, json-schema-to-typescript, NJsonSchema, etc.) couldn't
    handle the layered ``allOf``/``$ref`` inheritance or the synthetic
    defs we used to model native CS2 types (CHandle<X>, CUtlVector<T>,
    Vector, ...).  Mirroring upstream's structured shape lets each
    consumer apply its own type-mapping policy without fighting JSON
    Schema's vocabulary.
    """
    seen: set[tuple[str, str]] = set()
    classes_out: list[dict[str, Any]] = []
    enums_out: list[dict[str, Any]] = []

    # Walk every (module, name) variant — cross-module twins (e.g.
    # CCSPlayerController in both client + server) emit one record each,
    # mirroring upstream's natural representation.  ``_collect_module_variants``
    # yields the primary plus any duplicates the (module, name) deduper
    # held back.
    for entity in sorted(entities.values(), key=lambda e: (e["kind"], e["name"])):
        for variant in _collect_module_variants(entity):
            key = (variant.get("module", ""), variant["name"])
            if key in seen:
                continue
            seen.add(key)
            raw = variant.get("raw")
            if raw is None:
                continue  # synthetic / unsourced entity — skip
            record = _enrich_record(raw, variant, overlays)
            (enums_out if variant["kind"] == "enum" else classes_out).append(record)

    out: dict[str, Any] = {"schema_format_version": SCHEMA_FORMAT_VERSION}
    # Echo upstream's header keys verbatim so the file remains a drop-in
    # peer of cs2.json.gz for build/revision tracking.
    if source_info:
        for k in ("generator", "revision", "version_date", "version_time"):
            if k in source_info:
                out[k] = source_info[k]
    out["classes"] = classes_out
    out["enums"] = enums_out

    schema_dir = out_dir / "downstream-codegen-schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)
    out_path = schema_dir / "cs2_schema.json"
    out_path.write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return out_path


def generate_convars_schema(
    convars: list[dict],
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
) -> None:
    """Emit ``convars_schema.json`` — a structured projection of
    DumpSource2/convars.txt.

    Each entry preserves the four fields ``parse_convars`` already
    surfaces (``name``, ``default``, ``flags``, ``description``).  This
    is the codegen-friendly counterpart to ``convars.md``; downstream
    consumers wanting strongly-typed convar constants no longer need to
    parse Markdown.  No overlay annotation pipeline is wired up yet —
    add one if community-curated convar notes become a need.
    """
    schema_dir = out_dir / "downstream-codegen-schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)

    out: dict[str, Any] = {"schema_format_version": SCHEMA_FORMAT_VERSION}
    if source_info:
        for k in ("revision", "version_date", "version_time"):
            if k in source_info:
                out[k] = source_info[k]
    out["convars"] = [
        {
            "name": cv["name"],
            "default": cv.get("default", ""),
            "flags": list(cv.get("flags", []) or []),
            "description": cv.get("description", ""),
        }
        for cv in convars
    ]
    (schema_dir / "convars_schema.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def generate_commands_schema(
    commands: list[dict],
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
) -> None:
    """Emit ``commands_schema.json`` — structured counterpart to
    ``commands.md``.  Mirrors :func:`generate_convars_schema`; commands
    just have no ``default`` value.
    """
    schema_dir = out_dir / "downstream-codegen-schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)

    out: dict[str, Any] = {"schema_format_version": SCHEMA_FORMAT_VERSION}
    if source_info:
        for k in ("revision", "version_date", "version_time"):
            if k in source_info:
                out[k] = source_info[k]
    out["commands"] = [
        {
            "name": cmd["name"],
            "flags": list(cmd.get("flags", []) or []),
            "description": cmd.get("description", ""),
        }
        for cmd in commands
    ]
    (schema_dir / "commands_schema.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _project_constant_annotations(entry: dict[str, Any]) -> dict[str, str]:
    """Pull description/notes/warning out of a well-known-constants YAML
    entry and return them as the `annotations` block used everywhere
    else in the codegen schemas.
    """
    out: dict[str, str] = {}
    for key in ("description", "notes", "warning"):
        val = entry.get(key)
        if val:
            out[key] = str(val).strip()
    return out


def generate_well_known_constants_schema(
    overlays_dir: Path,
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
) -> None:
    """Emit ``well_known_constants.json`` from
    ``docs/overlays/well_known_constants.yml`` — integer / enum values
    that downstream tooling needs but that DumpSource2 doesn't expose as
    named enum types (team numbers, ``m_gamePhase``, ``CSWeaponState_t``,
    …).

    The YAML is the source of truth; the matching tables in
    ``AGENTS.md`` are kept in sync by hand.  Per-constant and per-member
    ``description`` / ``notes`` / ``warning`` keys are projected into
    the JSON as the same ``annotations`` block used by
    ``cs2_schema.json``.
    """
    schema_dir = out_dir / "downstream-codegen-schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)

    if not HAS_YAML:
        return
    src = overlays_dir / "well_known_constants.yml"
    try:
        text = src.read_text(encoding="utf-8")
    except OSError:
        return

    try:
        raw = yaml.safe_load(text) or {}
    except yaml.YAMLError as exc:  # pragma: no cover — surfaced at gen time
        print(f"  WARN: well_known_constants.yml failed to parse: {exc}", file=sys.stderr)
        return

    constants_out: list[dict[str, Any]] = []
    for entry in raw.get("constants", []) or []:
        if not isinstance(entry, dict) or "name" not in entry:
            continue
        rec: dict[str, Any] = {
            "name": entry["name"],
            "comment": entry.get("comment", ""),
        }
        annots = _project_constant_annotations(entry)
        if annots:
            rec["annotations"] = annots
        members_out: list[dict[str, Any]] = []
        for m in entry.get("members", []) or []:
            if not isinstance(m, dict) or "name" not in m or "value" not in m:
                continue
            mrec: dict[str, Any] = {"name": m["name"], "value": m["value"]}
            mannots = _project_constant_annotations(m)
            if mannots:
                mrec["annotations"] = mannots
            members_out.append(mrec)
        rec["members"] = members_out
        constants_out.append(rec)

    out: dict[str, Any] = {"schema_format_version": SCHEMA_FORMAT_VERSION}
    if source_info:
        for k in ("revision", "version_date", "version_time"):
            if k in source_info:
                out[k] = source_info[k]
    out["constants"] = constants_out

    (schema_dir / "well_known_constants.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _collect_type_vocabulary(entities: dict[str, dict]) -> dict[str, Any]:
    """Walk every (module, name) entity variant and return the actually-
    occurring values for ``type.category``, ``type.name`` (for the
    ``builtin`` and ``atomic`` categories), and ``metadata.name``.  Used
    by the codegen-schemas README so the documented vocabulary tracks
    reality instead of rotting against upstream additions.

    Also counts the "size > 0 + zero fields" classes so the README can
    quote an exact number from the current build instead of a stale
    figure.
    """
    categories: set[str] = set()
    builtins: set[str] = set()
    atomics: set[str] = set()
    metadata_keys: set[str] = set()
    size_only_classes = 0

    def walk_type(t: Any) -> None:
        if not isinstance(t, dict):
            return
        cat = t.get("category")
        if isinstance(cat, str):
            categories.add(cat)
            name = t.get("name")
            if isinstance(name, str):
                if cat == "builtin":
                    builtins.add(name)
                elif cat == "atomic":
                    atomics.add(name)
        for k in ("inner", "inner2", "inner3"):
            inner = t.get(k)
            if inner is not None:
                walk_type(inner)

    def walk_metadata(meta: Any) -> None:
        if not isinstance(meta, list):
            return
        for entry in meta:
            if isinstance(entry, dict):
                key = entry.get("name")
                if isinstance(key, str):
                    metadata_keys.add(key)

    size_only_records = 0
    for entity in entities.values():
        for variant in _collect_module_variants(entity):
            raw = variant.get("raw")
            if not isinstance(raw, dict):
                continue
            walk_metadata(raw.get("metadata"))
            fields = raw.get("fields") or []
            if (entity.get("kind") != "enum"
                    and raw.get("size", 0) > 0
                    and not fields
                    and not raw.get("parents")):
                # Schema-unregistered runtime class: has a binary size
                # but neither fields nor a schema parent.  Subclasses
                # that simply add no fields of their own (e.g. CAK47 →
                # CCSWeaponBaseGun) don't count — their parent has the
                # schema data.
                size_only_records += 1
            for fld in fields:
                walk_type(fld.get("type"))
                walk_metadata(fld.get("metadata"))
            for mem in raw.get("members", []) or []:
                walk_metadata(mem.get("metadata"))
    size_only_classes = size_only_records

    return {
        "categories": sorted(categories),
        "builtins": sorted(builtins),
        "atomics": sorted(atomics),
        "metadata_keys": sorted(metadata_keys),
        "size_only_classes": size_only_classes,
    }


def _format_vocab_section(title: str, items: list[str], wrap: bool = True) -> str:
    if not items:
        return f"### {title}\n\n_(none observed in this build)_\n"
    if wrap:
        rendered = ", ".join(f"`{it}`" for it in items)
        return f"### {title}\n\n{rendered}\n"
    # One per line for long metadata lists.
    rendered = "\n".join(f"- `{it}`" for it in items)
    return f"### {title}\n\n{rendered}\n"


def generate_codegen_schemas_readme(
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
    entities: dict[str, dict] | None = None,
) -> None:
    """Emit ``downstream-codegen-schemas/README.md`` — a small landing
    page next to the JSON files that explains what they are and points
    at ``AGENTS.md`` for the full format reference.  Generated each run
    so the source-revision footer stays current.

    When ``entities`` is supplied, the README also includes a "Type
    vocabulary observed in this build" section enumerating every
    ``category`` / ``builtin`` / ``atomic`` / ``metadata`` key that
    actually appears in ``cs2_schema.json``.  Auto-derived so it tracks
    upstream additions automatically.
    """
    schema_dir = out_dir / "downstream-codegen-schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)

    rev_line = ""
    if source_info:
        rev = source_info.get("revision")
        date = source_info.get("version_date")
        if rev and date:
            rev_line = f"\n_Last regenerated against CS2 build `{rev}` ({date})._\n"

    vocab_block = ""
    size_only_count: int | None = None
    if entities is not None:
        vocab = _collect_type_vocabulary(entities)
        size_only_count = vocab["size_only_classes"]
        vocab_block = "\n".join([
            "",
            "## Type vocabulary observed in this build",
            "",
            "Auto-derived from the actual content of `cs2_schema.json` so",
            "the documented vocabulary tracks upstream additions.",
            "",
            _format_vocab_section("Field `type.category` values", vocab["categories"]),
            _format_vocab_section("`builtin` type names", vocab["builtins"]),
            _format_vocab_section("`atomic` type names", vocab["atomics"]),
            _format_vocab_section(
                "Metadata keys (class / field / enum / member)",
                vocab["metadata_keys"],
                wrap=False,
            ),
        ])

    size_only_phrase = (
        f"{size_only_count} classes"
        if size_only_count is not None
        else "Some classes"
    )

    body = f"""# Downstream codegen schemas

Machine-readable schemas for CS2 entity classes, structs, enums, and game
events — kept in shapes that mirror upstream sources so any tooling that
already targets those sources works unchanged.

## Files

- **`cs2_schema.json`** — community-enriched mirror of
  [DumpSource2's `cs2.json.gz`](https://github.com/ValveResourceFormat/SchemaExplorer/blob/main/schemas/cs2.json.gz).
  Top-level: `generator`, `revision`, `version_date`, `version_time`,
  `classes`, `enums` — exactly upstream's shape.  Optional
  `annotations` blocks layer in community-curated descriptions / notes
  / warnings.  Cross-module twins (e.g. `CCSPlayerController` in both
  `client` and `server`) emit one record per `(module, name)`.

- **`gameevents_schema.json`** — community-enriched mirror of the
  parsed `.gameevents` KV1 registry.  Top-level: `events` list; each
  record preserves its parsed `name` / `comment` / `source` /
  `properties` / `fields` from the upstream KV1 source.  Same
  `annotations` enrichment pattern as `cs2_schema.json`.

- **`convars_schema.json`** — structured projection of
  `DumpSource2/convars.txt`.  Top-level: `convars` list; each entry has
  `name` / `default` / `flags` / `description`.  Codegen-friendly
  counterpart to `convars.md`.

- **`commands_schema.json`** — structured projection of
  `DumpSource2/commands.txt`.  Top-level: `commands` list; each entry
  has `name` / `flags` / `description`.

- **`well_known_constants.json`** — community-curated reference tables
  for integer / enum values that downstream tooling needs but that
  DumpSource2 doesn't expose as named enum types (team numbers,
  `m_gamePhase`, `CSWeaponState_t`, …).  Top-level: `constants` list;
  each entry has `name` / `comment` / `members[]` with the same
  `annotations` pattern as the schema files.

All five files share a single top-level `schema_format_version` string
that is bumped as a family.  Bump the major when a field is removed or
renamed in any of the five; bump the minor when a field is added.
Additive `annotations` blocks do not require a bump.

## Class records with `size > 0` and no fields

{size_only_phrase} in `cs2_schema.json` report a non-zero `size` but
expose zero fields — `CNmGraphInstance` (992 B),
`CBasePulseGraphInstance`, `CPulseExecCursor`, `CNavVolume`, `CBtNode`,
etc.  These are internal Source 2 runtime classes that the schema
reflection system knows the binary size of but never registers
field-level reflection for.  Downstream codegen consumers can safely
emit them as empty classes; field-level layout is not recoverable from
the dump.

## Why some upstream fields are absent

The mirror only emits what the upstream `cs2.json.gz` carries.  Several
fields that *were* present in older SchemaExplorer dumps no longer
appear and so are absent here too: per-class `abstract`, per-enum
`flags`, per-atomic `handle_kind`, per-enum `storage_size`.  These are
recoverable from the runtime but are not currently projected by
DumpSource2 — file upstream at `ValveResourceFormat/SchemaExplorer` if
you need them restored.

## Why this shape (and not JSON Schema 2020-12)

`cs2_schema.json` and `gameevents_schema.json` were originally JSON
Schema 2020-12 documents.  Standard codegens (quicktype, NJsonSchema,
json-schema-to-typescript) couldn't handle the layered `allOf` /
`$ref` inheritance and the synthetic defs needed to model native CS2
types (`CHandle<X>`, `CUtlVector<T>`, `Vector`, …).  Mirroring the
upstream structured shape lets each consumer apply its own
type-mapping policy without fighting JSON Schema's vocabulary.  The
three companion files (`convars_schema.json`, `commands_schema.json`,
`well_known_constants.json`) follow the same shape-pragmatic pattern:
plain JSON objects with conventional field names, no schema header.

## Format reference

Full per-key documentation lives in
[`AGENTS.md`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/AGENTS.md#cs2_schemajson-format)
at the repository root.

## Auto-generated — do not hand-edit

These files are regenerated every 4 hours from upstream by
[`.github/workflows/generate-docs.yml`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/.github/workflows/generate-docs.yml).
To change the generated output, edit the generator
(`docs/generate_docs.py`) or the community overlays under
`docs/overlays/` instead.
{vocab_block}
{rev_line}"""
    (schema_dir / "README.md").write_text(body, encoding="utf-8")


def generate_index_md(
    entities: dict[str, dict],
    protos: list[dict],
    convars: list[dict],
    commands: list[dict],
    out_dir: Path,
    gameevents: list[dict[str, Any]] | None = None,
) -> None:
    """Generate the Jekyll home page index.md."""
    by_module: dict[str, list] = defaultdict(list)
    for e in entities.values():
        by_module[e["module"]].append(e)

    total_entities = len(entities)
    total_proto_msgs = sum(len(p.get("messages", [])) for p in protos)

    lines: list[str] = []
    lines.append(_md_front_matter(layout="home", title="CS2 Developer Reference", nav_order="1", nav_exclude="true"))
    lines.append("# CS2 Developer Reference\n")
    lines.append(
        "Auto-generated documentation from the CS2 game tracking data. "
        "Includes entity schemas, network message definitions, game events, "
        "console variables, and commands.\n"
    )
    lines.append("## Statistics\n")
    lines.append("| Category | Count |")
    lines.append("|----------|-------|")
    lines.append(f"| Schema Entities | {total_entities} |")
    lines.append(f"| Proto Files | {len(protos)} |")
    lines.append(f"| Proto Messages | {total_proto_msgs} |")
    if gameevents is not None:
        lines.append(f"| Game Events | {len(gameevents)} |")
    lines.append(f"| ConVars | {len(convars)} |")
    lines.append(f"| Commands | {len(commands)} |")
    lines.append("")
    lines.append("## Quick Links\n")
    lines.append("- [Schema Entities](generated/schemas.md) – Classes, structs, and enums from CS2's schema dump ([codegen schema](generated/downstream-codegen-schemas/cs2_schema.json))")
    lines.append("- [Protobufs](generated/protobufs.md) – Network message and game event definitions")
    if gameevents is not None:
        lines.append("- [Game Events](generated/gameevents.md) – Game event definitions with field schemas ([codegen schema](generated/downstream-codegen-schemas/gameevents_schema.json))")
    lines.append("- [ConVars](generated/convars.md) – Console variable reference with flags and defaults ([codegen schema](generated/downstream-codegen-schemas/convars_schema.json))")
    lines.append("- [Commands](generated/commands.md) – Console command reference ([codegen schema](generated/downstream-codegen-schemas/commands_schema.json))")
    lines.append("- [Well-Known Constants](generated/downstream-codegen-schemas/well_known_constants.json) – Curated tables for team numbers, game phase, weapon state, etc.")
    lines.append("- [Codegen schemas index](generated/downstream-codegen-schemas/README.md) – Format reference, type vocabulary, and version policy for all five JSON schemas above")
    lines.append("- [Entity Hierarchy Diagram](generated/diagrams/server_hierarchy.md) – UML inheritance diagram for server & client entities")
    lines.append("")
    lines.append("## Schema Modules\n")
    module_list = "  ".join(
        f"[{mod}](generated/schemas/{mod}.md) ({len(ents)})"
        for mod, ents in sorted(by_module.items())
    )
    lines.append(module_list)
    lines.append("")
    (out_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def generate_global_diagram_md(entities: dict[str, dict], out_dir: Path) -> None:
    """Generate diagrams/server_hierarchy.md – full server/client hierarchy."""
    lines_d: list[str] = []
    seen_edges: set[tuple[str, str]] = set()

    for e in entities.values():
        if e["module"] not in ("server", "client"):
            continue
        if not e.get("bases"):
            continue
        child = _mermaid_safe(e["name"])
        for base in e["bases"]:
            parent = _mermaid_safe(base)
            edge = (base, e["name"])
            if edge not in seen_edges:
                lines_d.append(f"    {parent} <|-- {child}")
                seen_edges.add(edge)

    if not lines_d:
        return

    lines_d = list(dict.fromkeys(lines_d))

    (out_dir / "diagrams").mkdir(exist_ok=True)
    md_lines: list[str] = []
    md_lines.append(_md_front_matter(
        layout="default",
        title="Entity Hierarchy",
        parent="Schemas",
        nav_exclude="true",
    ))
    md_lines.append("# Entity Hierarchy Diagram\n")
    md_lines.append(
        "Inheritance relationships between server and client entities "
        "(capped at 300 edges for readability).\n"
    )
    md_lines.append("```mermaid")
    md_lines.append("classDiagram")
    md_lines.extend(lines_d[:300])
    md_lines.append("```\n")

    (out_dir / "diagrams" / "server_hierarchy.md").write_text(
        "\n".join(md_lines), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate CS2 Jekyll/Markdown documentation.")
    parser.add_argument("--repo-root", default=".", help="Path to the repository root")
    parser.add_argument(
        "--data-root",
        default=None,
        help=(
            "Path to the CS2OpenDev-Docs data tree (contains DumpSource2/ and "
            "Protobufs/).  Defaults to --repo-root.  Override when running from a "
            "standalone documentation repository that tracks game data in a "
            "submodule or sibling checkout."
        ),
    )
    parser.add_argument("--output", default="docs", help="Jekyll source directory (home page goes here; the rest goes under <output>/generated/)")
    parser.add_argument(
        "--schema-json",
        default=None,
        help=(
            "Path to DumpSource2's cs2.json (or cs2.json.gz).  When omitted, "
            "the generator looks under <data-root>/SchemaExplorer/schemas/ "
            "and <data-root>/DumpSource2/.  Override for local development "
            "(e.g. point at ~/Downloads/cs2.json)."
        ),
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    data_root = Path(args.data_root).resolve() if args.data_root else repo_root
    out_dir = Path(args.output).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    generated_dir = out_dir / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)

    overlays_dir = repo_root / "docs" / "overlays"

    print("Loading overlays…")
    if not HAS_YAML:
        print("  WARNING: PyYAML not found – overlay annotations will be skipped.")
        print("  Install with: pip install pyyaml")
    overlays = load_overlays(overlays_dir)
    print(f"  Loaded {len(overlays)} overlay file(s).")

    if args.schema_json:
        schema_json_path: Path | None = Path(args.schema_json).resolve()
        if not schema_json_path.is_file():
            print(f"ERROR: --schema-json file not found: {schema_json_path}", file=sys.stderr)
            return 2
    else:
        schema_json_path = find_schema_json(data_root)
    if schema_json_path is None:
        print(
            "ERROR: could not locate cs2.json.  Looked under "
            f"{data_root}/DumpSource2/ and "
            f"{data_root.parent}/schema-explorer/schemas/.  "
            "Pass --schema-json PATH, or initialise the schema-explorer submodule "
            "(`git submodule update --init upstream/schema-explorer`).",
            file=sys.stderr,
        )
        return 2
    print(f"Loading schema JSON from {schema_json_path}…")
    entities, schema_source_info = load_schema_json(schema_json_path)
    print(f"  Loaded {len(entities)} entities across "
          f"{len({e['module'] for e in entities.values()})} modules.")
    if schema_source_info.get("revision"):
        print(f"  Source revision: {schema_source_info['revision']} "
              f"({schema_source_info.get('version_date', '?')})")

    protobufs_root = data_root / "Protobufs"
    print("Compiling proto descriptors…")
    protos = load_proto_descriptors(protobufs_root)
    print(f"  Loaded {len(protos)} proto files.")

    dump_dir = data_root / "DumpSource2"
    print("Parsing convars and commands…")
    convars = parse_convars(dump_dir / "convars.txt")
    commands = parse_commands(dump_dir / "commands.txt")
    print(f"  {len(convars)} convars, {len(commands)} commands.")

    print("Parsing game events…")
    gameevents = parse_all_gameevents(data_root)
    print(f"  Parsed {len(gameevents)} game events.")

    print("Generating Markdown UML diagram pages…")
    uml_md = generate_module_uml_md(entities, generated_dir)
    generate_global_diagram_md(entities, generated_dir)
    print(f"  Generated {len(uml_md)} module UML Markdown pages.")

    print("Generating Markdown schema pages (with embedded entity details)…")
    generate_schemas_index_md(entities, overlays, generated_dir, diagram_modules=uml_md)
    print(f"  Generated {len({e['module'] for e in entities.values()})} module pages "
          f"covering {len(entities)} entities.")

    print("Generating Markdown protobuf pages…")
    generate_protobufs_md_page(protos, overlays, generated_dir)

    print("Generating Markdown convar and command pages…")
    generate_convars_md_page(convars, generated_dir)
    generate_commands_md_page(commands, generated_dir)

    print("Generating convars_schema.json and commands_schema.json…")
    generate_convars_schema(convars, generated_dir, source_info=schema_source_info)
    generate_commands_schema(commands, generated_dir, source_info=schema_source_info)

    print("Generating well_known_constants.json…")
    generate_well_known_constants_schema(
        overlays_dir, generated_dir, source_info=schema_source_info
    )

    print("Generating game events documentation…")
    generate_gameevents_md_page(gameevents, overlays, generated_dir)
    generate_gameevents_schema(gameevents, overlays, generated_dir)

    print("Generating cs2_schema.json (community-enriched mirror of cs2.json.gz)…")
    cs2_schema_path = generate_cs2_schema(
        entities, overlays, generated_dir, source_info=schema_source_info
    )
    schema_kb = cs2_schema_path.stat().st_size // 1024
    print(f"  Wrote {cs2_schema_path.name} ({schema_kb} KiB).")

    generate_codegen_schemas_readme(
        generated_dir, source_info=schema_source_info, entities=entities
    )

    print("Generating Markdown home page…")
    generate_index_md(entities, protos, convars, commands, out_dir, gameevents=gameevents)

    print(f"\nDone!  Home page: {out_dir}/index.md")
    print(f"        Generated content: {generated_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
