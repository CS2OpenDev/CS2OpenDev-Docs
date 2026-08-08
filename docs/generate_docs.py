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
                                  [--artifacts-root PATH] [--build ID|latest]
                                  [--platform windows-x86_64|linux-x86_64]

    --repo-root       Root of the repository that contains docs/, overlays/,
                      etc. (default: current directory)
    --artifacts-root  CS2OpenDev-SchemaTracker's artifacts/ directory.
                      Defaults to <repo-root>/upstream/schema-tracker/artifacts.
    --build           Build id to document, or 'latest' (default).
    --platform        Which platform's artifact set to render
                      (default: windows-x86_64).

The schema, protobuf, convar, command, and game-event data all come from a
single CS2OpenDev-SchemaTracker artifact set — no upstream submodules or
`protoc` are required.

Dependencies:
    pip install pyyaml protobuf
"""

from __future__ import annotations

import argparse
import copy
import html
import json
import re
import shutil
import sys
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
# Additive `annotations` blocks do not require a bump.
#
# 2.0: the entity schema source moved from DumpSource2's cs2.json.gz to
# CS2OpenDev-SchemaTracker's entity_schema.json.  cs2_schema.json now mirrors
# SchemaTracker's *native* shape (camelCase keys, string-encoded int64 offsets/
# sizes, UPPERCASE type categories, projectName/binary-module split) rather than
# DumpSource2's shape — a deliberate breaking change for downstream consumers.
SCHEMA_FORMAT_VERSION = "2.0"

# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def _as_int(v: Any) -> int | None:
    """Coerce SchemaTracker's numeric-but-stringified fields to ``int``.

    ``entity_schema.json`` encodes class ``size`` and field ``offset`` as
    decimal strings (``"1192"``, ``"48"``) while ``alignment`` is already an
    int.  Everything downstream (offset sorting, hex formatting, the layout
    tables) wants a real int, so we normalise once at the conversion boundary
    — the raw record echoed into ``cs2_schema.json`` is left untouched.
    """
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, int):
        return v
    if isinstance(v, str):
        s = v.strip()
        try:
            return int(s, 0) if s[:2].lower() == "0x" else int(s)
        except ValueError:
            return None
    return None


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
    """Return the display string for a SchemaTracker ``SchemaType`` node.

    SchemaTracker already renders the fully-qualified C++ type into the
    node's ``name`` for *every* category — ``"CAnimNetVar< int32 >"`` (ATOMIC),
    ``"CPulse_Chunk*"`` (PTR), ``"char[128]"`` (FIXED_ARRAY),
    ``"bitfield:1"`` (BITFIELD), and the bare name for BUILTIN /
    DECLARED_CLASS / DECLARED_ENUM — so no recursive reconstruction is
    needed.  The nested ``inner`` nodes are retained only for
    ``_innermost_declared_module`` cross-reference resolution.
    """
    if not isinstance(t, dict):
        return "?"
    return t.get("name", "?")


def _innermost_declared_module(t: dict[str, Any]) -> str | None:
    """Walk a SchemaTracker type tree and return the binary module of the
    innermost declared class or enum, or None if the type isn't ultimately
    a reference to another entity.

    Handles wrapper categories that nest a target (``PTR``, ``FIXED_ARRAY``,
    ``ATOMIC`` like ``CHandle<X>`` / ``CUtlVector<X>``).  For multi-arg
    templates we return the first inner's module — the primary referenced type.
    """
    if not isinstance(t, dict):
        return None
    if t.get("category") in ("DECLARED_CLASS", "DECLARED_ENUM"):
        return t.get("module")
    for inner_key in ("inner", "inner2", "inner3"):
        if t.get(inner_key):
            mod = _innermost_declared_module(t[inner_key])
            if mod:
                return mod
    return None


def _grouping_module(record: dict[str, Any]) -> str:
    """Return the module name used to bucket an entity into a schema page.

    SchemaTracker classes carry a ``projectName`` (``client``, ``server``,
    ``entity2``, ``pulse_runtime_lib``, ``particleslib``, ``animgraphlib``)
    — the closest analogue to the old DumpSource2 module axis, so we group
    classes by it.  Enums carry no ``projectName``, only the binary
    ``module`` they were registered in (``server.dll`` on Windows,
    ``libserver.so`` on Linux), so we normalise that to a bare name so the
    two axes line up on shared modules like ``client`` / ``server``.
    """
    pn = record.get("projectName")
    if pn:
        return pn
    mod = (record.get("module", "") or "").rsplit("/", 1)[-1]
    for suffix in (".dll", ".so"):
        if mod.endswith(suffix):
            mod = mod[: -len(suffix)]
            break
    if mod.startswith("lib"):
        mod = mod[3:]
    return mod or "unknown"


def _convert_class(cls: dict[str, Any]) -> dict[str, Any]:
    """Convert one SchemaTracker ``SchemaClass`` into the entity dict shape
    used by the rest of the generator.

    Metadata is preserved as ``[{name, value, valueParsed?}]`` (the native
    shape) so codegen consumers get the split.  The binary ``module`` the
    class lives in is surfaced separately from the ``projectName``-based
    grouping module.  ``raw`` keeps the untouched SchemaTracker record so
    ``generate_cs2_schema`` can echo its native shape with overlay
    annotations layered on top.
    """
    fields: list[dict[str, Any]] = []
    for f in cls.get("fields", []):
        ftype = f.get("type", {})
        out: dict[str, Any] = {
            "name": f.get("name", ""),
            "type": _stringify_type(ftype),
            "offset": _as_int(f.get("offset")),
            "annotations": list(f.get("metadata", [])),
        }
        # SchemaTracker gives the referenced type's binary module directly
        # via ``typeModule``; fall back to walking the type tree.
        type_module = f.get("typeModule") or _innermost_declared_module(ftype)
        if type_module:
            out["type_module"] = type_module
        fields.append(out)

    parents = cls.get("parents", [])

    return {
        "name": cls["name"],
        "kind": "class",
        "module": _grouping_module(cls),
        "binary_module": cls.get("module", ""),
        "bases": [p.get("name", "") for p in parents],
        "base_modules": [p.get("module", "") for p in parents],
        "fields": fields,
        "metadata": list(cls.get("metadata", [])),
        "enum_underlying": None,
        "size": _as_int(cls.get("size")),
        "alignment": _as_int(cls.get("alignment")),
        "flags": cls.get("flags"),
        "cpp_name": cls.get("cppName"),
        "raw": cls,
    }


def _convert_enum(en: dict[str, Any]) -> dict[str, Any]:
    """Convert one SchemaTracker ``SchemaEnum`` into the entity dict shape
    used by the rest of the generator.

    Per-member metadata (``MPropertyFriendlyName``, ``MPropertyDescription``,
    etc.) is preserved on each value's ``annotations`` list, surfaced both in
    the Markdown enum table's Description column and in cs2_schema.json.
    ``enum_underlying`` carries SchemaTracker's ``alignment`` — the
    underlying integer type name (e.g. ``uint32_t``).
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
        "module": _grouping_module(en),
        "binary_module": en.get("module", ""),
        "bases": [],
        "base_modules": [],
        "fields": fields,
        "metadata": list(en.get("metadata", [])),
        "enum_underlying": en.get("alignment"),
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


def load_entity_schema(build_dir: Path) -> dict[str, dict]:
    """Load ``entity_schema.json`` from a SchemaTracker build/platform dir.

    Returns the entity map keyed by name.  SchemaTracker walks the shipped
    CS2 runtime binaries in-process, so the JSON carries inheritance,
    sizes, offsets, metadata, and the binary module each class/enum lives
    in — replacing DumpSource2's cs2.json.gz as the schema source.
    """
    path = build_dir / "entity_schema.json"
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)

    entities: dict[str, dict] = {}
    for cls in data.get("classes", []):
        _add_entity(entities, _convert_class(cls))
    for en in data.get("enums", []):
        ent = _convert_enum(en)
        # An enum statically linked into several binaries is registered once
        # per module (e.g. the Pulse enums appear in animationsystem.dll,
        # particles.dll, client.dll and server.dll).  Unlike classes — whose
        # client/server twins genuinely differ — these are the identical enum,
        # so we keep only the first registration rather than scattering copies
        # across per-binary module pages.
        if ent["name"] not in entities:
            _add_entity(entities, ent)
    return entities


def _read_latest_pointer(artifacts_root: Path) -> int | None:
    """Read the build id from a ``latest``-branch ``LATEST.json`` pointer.

    SchemaTracker's ``latest`` branch carries exactly one build plus a root
    ``LATEST.json`` (sibling of ``artifacts/``) naming it — e.g.
    ``{"build_id": 24537688, "platforms": [...], "source_commit": "..."}``.
    Preferring the pointer over a directory scan makes ``--build latest``
    robust and side-steps a full walk of a many-build ``artifacts/`` tree.
    Returns ``None`` when no readable pointer is present (the full-repo
    layout), so callers fall back to the numeric-directory scan.
    """
    ptr = artifacts_root.parent / "LATEST.json"
    if not ptr.is_file():
        return None
    try:
        data = json.loads(ptr.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    try:
        return int(data.get("build_id"))
    except (TypeError, ValueError):
        return None


def resolve_build_dir(
    artifacts_root: Path, build: str | None, platform: str
) -> Path | None:
    """Resolve a SchemaTracker ``artifacts/<build_id>/<platform>/`` directory.

    ``build`` may be an explicit numeric build id or ``"latest"``/``None``.
    For ``latest`` we prefer a ``LATEST.json`` pointer (the ``latest`` branch
    ships one), then fall back to the highest-numbered committed build
    directory that carries this platform's ``entity_schema.json`` (the
    full-repo layout, which has no pointer).
    """
    if not artifacts_root.is_dir():
        return None
    if build and build != "latest":
        cand = artifacts_root / build / platform
        return cand if (cand / "entity_schema.json").is_file() else None
    ordered: list[int] = []
    pointed = _read_latest_pointer(artifacts_root)
    if pointed is not None:
        ordered.append(pointed)
    ordered.extend(
        sorted(
            (int(p.name) for p in artifacts_root.iterdir()
             if p.is_dir() and p.name.isdigit()),
            reverse=True,
        )
    )
    seen: set[int] = set()
    for bid in ordered:
        if bid in seen:
            continue
        seen.add(bid)
        cand = artifacts_root / str(bid) / platform
        if (cand / "entity_schema.json").is_file():
            return cand
    return None


def build_source_info(build_dir: Path, platform: str) -> dict[str, Any]:
    """Assemble the ``source_info`` header from a build's ``provenance.json``.

    Carries the keys the downstream schema emitters echo (``generator``,
    ``revision``, ``version_date``, ``version_time``) plus SchemaTracker
    provenance (build id, schema version, tool version) for page footers.
    """
    info: dict[str, Any] = {
        "generator": "https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker",
        "platform": platform,
        "build_id": build_dir.parent.name,
    }
    prov_path = build_dir / "provenance.json"
    if prov_path.is_file():
        try:
            prov = json.loads(prov_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return info
        info["build_id"] = prov.get("buildId", info["build_id"])
        info["schema_version"] = prov.get("schemaVersion", "")
        cs2_build = prov.get("cs2Build", {}) or {}
        info["revision"] = str(
            cs2_build.get("schemaRevision") or info["build_id"] or ""
        )
        manifest_utc = (prov.get("steam", {}) or {}).get("manifestCreatedUtc", "")
        info["version_date"] = manifest_utc.split("T")[0] if manifest_utc else ""
        info["version_time"] = manifest_utc
        tool = prov.get("tool", {}) or {}
        info["tool_version"] = tool.get("semver", "")
        info["tool_commit"] = tool.get("gitCommit", "")
    return info


# ---------------------------------------------------------------------------
# Proto loader (prebuilt FileDescriptorSet)
# ---------------------------------------------------------------------------
#
# SchemaTracker ships each build's own protobuf definitions as a prebuilt
# ``protos.descriptorset`` — a serialized google.protobuf.FileDescriptorSet
# of the descriptors embedded in the game binaries.  We read it directly and
# walk it via google.protobuf.descriptor_pb2, so no ``protoc`` invocation
# (and no external protobuf-compiler dependency) is needed any more.
#
# Note: these descriptors are reconstructed from the binary and carry no
# SourceCodeInfo, so the proto pages have no field/message comments — the
# wire-message tables (network_messages.json) provide the ID↔type mapping
# that used to justify the comments.  We skip the bundled
# ``google/protobuf/*`` well-known files.

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


def load_proto_descriptors(descriptorset_path: Path) -> list[dict[str, Any]]:
    """Read SchemaTracker's prebuilt ``protos.descriptorset`` and return one
    summary dict per game proto file.

    See the ``Proto loader`` block comment above for the design rationale.
    The bundled ``google/protobuf/*`` well-known files are skipped.
    """
    try:
        from google.protobuf import descriptor_pb2
    except ImportError as exc:
        raise RuntimeError(
            "python protobuf runtime not installed: pip install protobuf"
        ) from exc

    fds = descriptor_pb2.FileDescriptorSet.FromString(
        descriptorset_path.read_bytes()
    )
    results: list[dict[str, Any]] = []
    for fdp in sorted(fds.file, key=lambda f: f.name):
        if fdp.name.startswith("google/"):
            continue
        results.append(_proto_descriptor_to_dict(fdp))
    return results


def load_convars_json(path: Path) -> list[dict]:
    """Load SchemaTracker's ``convars.json``.

    Richer than the old ``convars.txt`` regex parse: each convar also
    carries its ``value_type`` and optional min/max bounds.
    """
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    convars: list[dict] = []
    for cv in data.get("convars", []):
        convars.append({
            "name": cv.get("name", ""),
            "default": cv.get("default", "") or "",
            "flags": list(cv.get("flags", []) or []),
            "description": cv.get("description", "") or "",
            "value_type": cv.get("valueType", "") or "",
            "has_min": bool(cv.get("hasMin", False)),
            "min_value": cv.get("minValue", "") or "",
            "has_max": bool(cv.get("hasMax", False)),
            "max_value": cv.get("maxValue", "") or "",
        })
    return convars


def load_commands_json(path: Path) -> list[dict]:
    """Load SchemaTracker's ``commands.json``.

    Adds ``has_completion_callback`` over the old ``commands.txt`` parse.
    """
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    commands: list[dict] = []
    for cmd in data.get("commands", []):
        commands.append({
            "name": cmd.get("name", ""),
            "flags": list(cmd.get("flags", []) or []),
            "description": cmd.get("description", "") or "",
            "has_completion_callback": bool(cmd.get("hasCompletionCallback", False)),
        })
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

def load_gameevents_json(path: Path) -> list[dict[str, Any]]:
    """Load SchemaTracker's ``gameevents.json`` — the structurally-parsed
    game-event registry.

    Each event dict carries ``name``, ``comment``, ``source`` (the
    originating ``.gameevents`` basename), ``properties`` (event-level
    metadata like ``local`` / ``reliable``), and ``fields`` (each
    ``{name, type, comment}``) — the same shape the old KV1 parser
    produced, so the renderers are unchanged.
    """
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    events: list[dict[str, Any]] = []
    for ev in data.get("events", []):
        events.append({
            "name": ev.get("name", ""),
            "comment": ev.get("comment", "") or "",
            "source": ev.get("source", "") or "",
            "properties": dict(ev.get("properties", {}) or {}),
            "fields": [
                {
                    "name": f.get("name", ""),
                    "type": f.get("type", ""),
                    "comment": f.get("comment", "") or "",
                }
                for f in ev.get("fields", [])
            ],
        })
    return events


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


def _type_filename(name: str) -> str:
    """Return the per-type page stem (no extension) for an entity *name*.

    Nested-type names carry ``::`` (430+ of them, e.g. ``CNmBlend1DNode::CDefinition``);
    ``::`` maps to ``.`` (a dot never appears in an identifier, so no collision
    with a real ``A.B`` name is possible) and any other filesystem-unsafe
    character collapses to ``_``.  This is the single canonical name→file
    mapping every schema link routes through.
    """
    stem = name.replace("::", ".")
    stem = re.sub(r'[<>:"/\\|?*\s]+', "_", stem)
    return stem


def _schema_page_href(
    name: str, entities: dict[str, dict], from_module: str
) -> str | None:
    """Relative link from a per-class page in *from_module* to *name*'s page.

    Per-type pages live at ``schemas/<module>/<TypeFile>.md``, so from a page
    inside ``schemas/<from_module>/`` the target is ``../<module>/<file>.md``.
    Prefers a same-module duplicate variant (client/server twins) so readers
    stay in the module they came from.  Returns ``None`` for an unresolved
    name (render it as plain text).
    """
    e = entities.get(name)
    if not e:
        return None
    mod = e["module"]
    if from_module and from_module != mod and any(
        d["module"] == from_module for d in e.get("duplicates", [])
    ):
        mod = from_module
    return f"../{mod}/{_type_filename(name)}.md"


def _flatten_layout(
    entity: dict[str, Any], entities: dict[str, dict]
) -> tuple[list[dict[str, Any]], list[str]]:
    """Return a class's full field layout: own fields plus fields inherited
    along the **primary-parent spine** (``bases[0]`` recursively), each tagged
    with its declaring class.

    SchemaTracker field offsets are absolute from the object base and the
    primary base always occupies offset 0, so base field offsets carry over
    unchanged into the derived class — the merged list sorts correctly by
    offset for the single-inheritance case that covers every gameplay entity.

    Secondary bases (``bases[1:]`` on any class in the spine) sit at a shift we
    can't recover from the schema alone, so their offsets would be misleading
    if merged; we return their names separately for the caller to surface as
    links rather than inventing absolute offsets.

    Returns ``(rows, secondary_base_names)`` where each row is
    ``{"field", "declaring", "inherited"}`` sorted by offset (fields with no
    offset sink to the end, stable in declaration order).
    """
    rows: list[dict[str, Any]] = []
    secondary: list[str] = []
    seen_fields: set[str] = set()   # a derived field shadows a base's namesake
    visited: set[str] = {entity["name"]}

    def add_fields(e: dict[str, Any], is_self: bool) -> None:
        for f in e.get("fields", []):
            fn = f.get("name", "")
            if fn in seen_fields:
                continue
            seen_fields.add(fn)
            rows.append({"field": f, "declaring": e["name"], "inherited": not is_self})

    def walk_bases(e: dict[str, Any]) -> None:
        for i, b in enumerate(e.get("bases", [])):
            if i == 0:
                if b in visited:
                    continue
                visited.add(b)
                be = entities.get(b)
                if be:
                    add_fields(be, False)
                    walk_bases(be)
            elif b not in secondary:
                secondary.append(b)

    add_fields(entity, True)   # pass entity directly so client/server dups keep their own fields
    walk_bases(entity)
    rows.sort(
        key=lambda r: (0, r["field"]["offset"])
        if isinstance(r["field"].get("offset"), int)
        else (1, 0)
    )
    return rows, secondary


def _md_link_type(
    type_str: str, entities: dict[str, dict], current_module: str = ""
) -> str:
    """Wrap known entity names in a type string with Markdown links to their
    per-type pages.

    Emitted from a per-type page at ``schemas/<current_module>/<X>.md``, so the
    target ``../<module>/<file>.md`` resolves whether the referenced type lives
    in the same module or another.  Prefers a same-module duplicate variant so
    readers stay within the module they came from.
    """
    def replace(m: re.Match) -> str:
        word = m.group(0)
        if word in entities:
            href = _schema_page_href(word, entities, current_module)
            if href:
                return f"[{word}]({href})"
        return word

    return re.sub(r"\b[A-Z_]\w+\b", replace, type_str)


def _md_front_matter(**kwargs: str) -> str:
    """Render a YAML front matter block for Jekyll."""
    lines = ["---"]
    for key, val in kwargs.items():
        s = str(val)
        # Quote values that would otherwise be mis-parsed: those containing a
        # flow/indicator char, and those *starting* with a YAML indicator —
        # notably ``!`` (the ``!GlobalTypes`` module), which YAML reads as a
        # tag.  Quoted double-quoted scalars are always safe, so we escape and
        # quote rather than try to enumerate every safe case.
        if any(c in s for c in (':', '#', '[', ']', '{', '}')) or s[:1] in (
            '!', '&', '*', '?', '|', '>', '@', '`', '%', '"', "'", '-', ' '
        ):
            esc = s.replace('\\', '\\\\').replace('"', '\\"')
            lines.append(f'{key}: "{esc}"')
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


def _render_schema_type_page(
    e: dict[str, Any],
    mod: str,
    entities: dict[str, dict],
    overlays: dict[str, dict],
) -> str:
    """Render one class/enum's standalone Markdown page (``schemas/<mod>/<Type>.md``).

    The class case carries the full **memory layout** — own fields plus fields
    inherited along the primary-parent spine, each with its absolute offset —
    which the old single-file-per-module rendering never produced.
    """
    name = e["name"]
    kind = e["kind"]
    overlay = get_overlay(overlays, mod, name)
    L: list[str] = []
    L.append(_md_front_matter(layout="default", title=name, nav_exclude="true"))

    # Breadcrumb (this page lives at schemas/<mod>/<Type>.md).
    L.append(f"[Schemas](../../schemas.md) / [{mod}](../{mod}.md) / {name}\n")
    L.append(f"# {name}\n")

    if overlay.get("description"):
        L.append(f"{overlay['description']}\n")
    if overlay.get("notes"):
        L.append(f"> 📝 {overlay['notes']}\n")
    if overlay.get("warning"):
        L.append(f"> ⚠️ {overlay['warning']}\n")

    # Stat line — kind, size/alignment (classes), underlying int (enums), module.
    stats = [f"**Kind:** {kind}"]
    if isinstance(e.get("size"), int):
        stats.append(f"**Size:** {e['size']} bytes (`0x{e['size']:x}`)")
    if isinstance(e.get("alignment"), int):
        stats.append(f"**Align:** {e['alignment']}")
    if kind == "enum" and e.get("enum_underlying"):
        stats.append(f"**Underlying:** `{e['enum_underlying']}`")
    stats.append(f"**Module:** {mod}")
    L.append(" · ".join(stats) + "\n")

    # Inherits / derived.
    if e.get("bases"):
        base_links = []
        for b in e["bases"]:
            href = _schema_page_href(b, entities, mod)
            base_links.append(f"[{b}]({href})" if href else b)
        L.append(f"**Inherits from:** {', '.join(base_links)}\n")
    derived = sorted(
        (d for d in entities.values() if name in d.get("bases", [])),
        key=lambda x: x["name"],
    )
    if derived:
        links = []
        for d in derived:
            href = _schema_page_href(d["name"], entities, mod)
            links.append(f"[{d['name']}]({href})" if href else d["name"])
        L.append(f"**Derived by:** {', '.join(links)}\n")

    # Metadata tags — drop MNetworkVarNames (repeats field info) and the big
    # MGetKV3ClassDefaults blob (rendered separately as a collapsible below).
    if e.get("metadata"):
        tags = [
            f"`{_format_metadata(m)}`" for m in e["metadata"]
            if isinstance(m, dict) and m.get("name")
            and not m["name"].startswith("MNetworkVarNames")
            and m["name"] != "MGetKV3ClassDefaults"
        ]
        if tags:
            L.append(f"**Metadata:** {', '.join(tags)}\n")

    # Relationship diagram.
    diagram_lines = _build_md_relationship_diagram(name, e, entities)
    if diagram_lines:
        L.append("**Relationships:**\n")
        L.append("```mermaid")
        L.append("classDiagram")
        L.extend(diagram_lines)
        L.append("```\n")

    if kind == "enum":
        vals = e.get("fields", [])
        if vals:
            L.append("## Values\n")
            L.append("| Name | Value | Description |")
            L.append("|------|-------|-------------|")
            for fld in vals:
                desc = _metadata_friendly_text(fld.get("annotations")).replace("|", "\\|")
                L.append(f"| `{fld['name']}` | {fld.get('value', '')} | {desc} |")
            L.append("")
    else:
        rows, secondary = _flatten_layout(e, entities)
        overlay_fields = overlay.get("fields", {}) or {}
        if rows:
            own = sum(1 for r in rows if not r["inherited"])
            L.append("## Memory layout\n")
            L.append(
                f"{len(rows)} fields ({own} declared here, {len(rows) - own} "
                "inherited). Offsets are absolute from the object base.\n"
            )
            L.append("| Offset | Field | Type | From | Annotations |")
            L.append("|--------|-------|------|------|-------------|")
            for r in rows:
                fld = r["field"]
                fname = fld.get("name", "")
                off = fld.get("offset")
                off_str = f"`0x{off:x}`" if isinstance(off, int) else "—"
                type_linked = _md_link_type(fld.get("type", ""), entities, mod)
                if r["inherited"]:
                    dhref = _schema_page_href(r["declaring"], entities, mod)
                    from_cell = (
                        f"[{r['declaring']}]({dhref})" if dhref else r["declaring"]
                    )
                else:
                    from_cell = ""
                annot_str = " ".join(
                    f"`{_format_metadata(a)}`"
                    for a in fld.get("annotations", [])
                    if isinstance(a, dict) and a.get("name")
                )
                desc_parts: list[str] = []
                fover = (
                    overlay_fields.get(fname, {})
                    if not r["inherited"] and isinstance(overlay_fields, dict)
                    else {}
                )
                if fover and isinstance(fover, dict):
                    if fover.get("description"):
                        desc_parts.append(str(fover["description"]))
                    if fover.get("notes"):
                        desc_parts.append(f"*{fover['notes']}*")
                if annot_str:
                    desc_parts.append(annot_str)
                ann_cell = " ".join(desc_parts).replace("|", "\\|")
                L.append(
                    f"| {off_str} | `{fname}` | {type_linked} | {from_cell} | {ann_cell} |"
                )
            L.append("")
        if secondary:
            sec_links = []
            for b in secondary:
                href = _schema_page_href(b, entities, mod)
                sec_links.append(f"[{b}]({href})" if href else b)
            L.append(
                f"**Also inherits (secondary base classes):** {', '.join(sec_links)} "
                "— additional-base fields sit at a shifted offset the schema does "
                "not record; see each base's own page for its layout.\n"
            )

    # MGetKV3ClassDefaults — raw KV3 default block, collapsed to keep the page
    # scannable.  Rendered as escaped <pre> so it survives regardless of the
    # kramdown block-HTML setting.
    kv3 = None
    for m in e.get("metadata", []) or []:
        if isinstance(m, dict) and m.get("name") == "MGetKV3ClassDefaults":
            kv3 = m.get("value")
            break
    if isinstance(kv3, str) and kv3.strip():
        L.append("<details><summary>KV3 class defaults</summary>\n")
        L.append(f"<pre>{html.escape(kv3)}</pre>")
        L.append("</details>\n")

    return "\n".join(L)


def generate_schemas_index_md(
    entities: dict[str, dict],
    overlays: dict[str, dict],
    out_dir: Path,
    diagram_modules: set[str] | None = None,
) -> None:
    """Generate the schema reference: a master index, a slim per-module index
    page, and one standalone page per class/enum.

    Types are split one-file-per-type (``schemas/<module>/<Type>.md``) so pages
    stay small and greppable and every type is deep-linkable — replacing the
    old single-giant-file-per-module layout.  Per-type pages carry the full
    memory layout (field offsets + inherited fields) that the old rendering
    dropped.
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
    lines.append(
        "Every class, struct, and enum extracted from CS2's runtime schema, "
        "organised by module. Each module page lists its types; each type has "
        "its own page carrying the full **memory layout** — field offsets, "
        "class size, and fields inherited from base classes.\n"
    )
    lines.append("## Modules\n")
    lines.append("| Module | Types | UML |")
    lines.append("|--------|-------|-----|")
    for mod in sorted(by_module):
        count = len(by_module[mod])
        has_diagram = diagram_modules is None or mod in diagram_modules
        uml_cell = f"[📊 Diagram](diagrams/{mod}.md)" if has_diagram else "—"
        lines.append(
            f"| [{mod}](schemas/{mod}.md) | {count} | {uml_cell} |"
        )
    lines.append("")
    (out_dir / "schemas.md").write_text("\n".join(lines), encoding="utf-8")

    # Per-module: a slim index page (schemas/<mod>.md) linking to one page per
    # type (schemas/<mod>/<Type>.md).
    (out_dir / "schemas").mkdir(exist_ok=True)
    for mod, ents in by_module.items():
        sorted_ents = sorted(ents, key=lambda x: (x["kind"], x["name"]))
        mod_dir = out_dir / "schemas" / mod
        mod_dir.mkdir(parents=True, exist_ok=True)

        # Slim module index.
        idx: list[str] = []
        idx.append(_md_front_matter(
            layout="default",
            title=mod,
            parent="Schemas",
            nav_exclude="true",
        ))
        idx.append(f"# Module: {mod}\n")
        if diagram_modules is None or mod in diagram_modules:
            idx.append(f"[📊 View UML Diagram](../diagrams/{mod}.md)\n")
        idx.append(
            f"{len(sorted_ents)} types. Each links to its own page with the "
            "full field layout.\n"
        )
        idx.append("| Type | Kind | Size | Fields | Inherits |")
        idx.append("|------|------|------|--------|----------|")
        for e in sorted_ents:
            fname = _type_filename(e["name"])
            size = e.get("size")
            size_str = str(size) if isinstance(size, int) else "—"
            field_count = len(e.get("fields", []))
            base_cells = []
            for b in e.get("bases", []):
                be = entities.get(b)
                if be:
                    bmod = be["module"]
                    if bmod != mod and any(
                        d["module"] == mod for d in be.get("duplicates", [])
                    ):
                        bmod = mod
                    base_cells.append(f"[{b}]({bmod}/{_type_filename(b)}.md)")
                else:
                    base_cells.append(b)
            idx.append(
                f"| [{e['name']}]({mod}/{fname}.md) | {e['kind']} | {size_str} "
                f"| {field_count} | {', '.join(base_cells)} |"
            )
        idx.append("")
        (out_dir / "schemas" / f"{mod}.md").write_text(
            "\n".join(idx), encoding="utf-8"
        )

        # One standalone page per type.
        for e in sorted_ents:
            page = _render_schema_type_page(e, mod, entities, overlays)
            (mod_dir / f"{_type_filename(e['name'])}.md").write_text(
                page, encoding="utf-8"
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
    """Generate ``cs2_schema.json`` — the entity schema in
    CS2OpenDev-SchemaTracker's native shape, enriched with overlays.

    Each record is SchemaTracker's own ``entity_schema.json`` class/enum
    object emitted verbatim (camelCase keys, string-encoded int64
    offsets/sizes, UPPERCASE type ``category`` values, the
    ``module``/``projectName`` split), with an optional additive
    ``annotations`` block on classes, fields, enums, and members carrying
    community-curated descriptions / notes / warnings from
    ``docs/overlays/``.  A class registered in more than one binary emits
    one record per ``(module, name)``.  See ``AGENTS.md`` for the full
    per-key format reference.
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
                if cat == "BUILTIN":
                    builtins.add(name)
                elif cat == "ATOMIC":
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
                    and int(raw.get("size", 0) or 0) > 0
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
events — projected straight from
[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)'s
per-build artifacts so consumers get one deterministic, provenance-tracked
source instead of a chain of third-party dumps.

## Files

- **`cs2_schema.json`** — the entity schema in SchemaTracker's **native**
  shape (`schema_format_version` `2.0`).  Top-level: `generator`, `revision`,
  `version_date`, `version_time`, `classes`, `enums`.  Each class carries
  `name`, `module` (the binary it lives in), `projectName`, `cppName`,
  `size`, `alignment`, `flags` / `flags2`, `parents[]`, `fields[]`
  (`name`, `offset`, `type`, `typeModule`, `metadata`), and inheritance
  depths; each enum carries `alignment` (underlying integer type) and
  `members[]`.  Integer offsets / sizes are **string-encoded** and type
  `category` values are **UPPERCASE** (`BUILTIN`, `ATOMIC`, `DECLARED_CLASS`,
  `PTR`, `FIXED_ARRAY`, `BITFIELD`, …).  Optional `annotations` blocks layer
  in community-curated descriptions / notes / warnings.  A class registered
  in more than one binary emits one record per `(module, name)`.

- **`gameevents_schema.json`** — the game-event registry.  Top-level:
  `events` list; each record has `name` / `comment` / `source` /
  `properties` / `fields`.  Same `annotations` enrichment pattern.

- **`convars_schema.json`** — the console-variable table.  Top-level:
  `convars` list; each entry has `name` / `default` / `flags` /
  `description` (SchemaTracker additionally exposes `valueType` and min/max
  in the source artifact).  Codegen-friendly counterpart to `convars.md`.

- **`commands_schema.json`** — the console-command table.  Top-level:
  `commands` list; each entry has `name` / `flags` / `description`.

- **`well_known_constants.json`** — community-curated reference tables
  for integer / enum values downstream tooling needs but that the schema
  doesn't expose as named enum types (team numbers, `m_gamePhase`,
  `CSWeaponState_t`, …).  Top-level: `constants` list; each entry has
  `name` / `comment` / `members[]` with the same `annotations` pattern.

- **`field_history.json`** — whole-history evolution of every
  `(class, field)`, projected from SchemaTracker's cumulative
  `schema_evolution.json` (Layer A).  Top-level: `baseline_build`,
  `latest_build`, `transition_count`, `fields` list (each `class` /
  `field` / `firstSeenBuild` / `lastSeenBuild` / `typeHistory`, plus an
  overlay-supplied `confirmedRename` where the community has verified one),
  and `enums`.  Serves alias resolution / forward-back schema migration
  for demo parsers and SDKs.  See the [Schema History](../schema-history.html)
  page for the human-readable break radar.

All six files share a single top-level `schema_format_version` string
that is bumped as a family.  Bump the major when a field is removed or
renamed in any of them; bump the minor when a field is added.
Additive `annotations` blocks do not require a bump.

## Coverage — runtime only

SchemaTracker walks the **shipped CS2 runtime binaries** in-process, so
`cs2_schema.json` covers exactly the schema those binaries register
(`client`, `server`, `entity2`, `pulse_runtime_lib`, `particleslib`,
`animgraphlib`).  The Source 2 editor / tooling schema (hammer, modeldoc,
resourcecompiler, worldrenderer, …) is intentionally **not** present — it
never ships in the game.

## Class records with `size > 0` and no fields

{size_only_phrase} in `cs2_schema.json` report a non-zero `size` but
expose zero fields.  These are internal Source 2 runtime classes that the
schema system knows the binary size of but never registers field-level
reflection for.  Downstream codegen consumers can safely emit them as
empty classes; field-level layout is not recoverable from the binary.

## Format reference

Full per-key documentation lives in
[`AGENTS.md`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/AGENTS.md#cs2_schemajson-format)
at the repository root.

## Auto-generated — do not hand-edit

These files are regenerated every 4 hours from the latest
CS2OpenDev-SchemaTracker build by
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
    source_info: dict[str, Any] | None = None,
    extra_pages: list[tuple[str, str]] | None = None,
) -> None:
    """Generate the Jekyll home page index.md."""
    # Match generate_schemas_index_md's bucketing (primary + cross-module
    # duplicate variants) so the home-page module list links every page that
    # actually gets written.
    by_module: dict[str, list] = defaultdict(list)
    for e in entities.values():
        by_module[e["module"]].append(e)
        for dup in e.get("duplicates", []):
            by_module[dup["module"]].append(dup)

    total_entities = len(entities)
    total_proto_msgs = sum(len(p.get("messages", [])) for p in protos)
    source_info = source_info or {}
    extra_pages = extra_pages or []

    lines: list[str] = []
    lines.append(_md_front_matter(layout="home", title="CS2 Developer Reference", nav_order="1", nav_exclude="true"))
    lines.append("# CS2 Developer Reference\n")
    lines.append(
        "Auto-generated reference for the **shipped CS2 runtime**, extracted "
        "deterministically from the game binaries by "
        "[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker): "
        "entity schemas, protobuf wire messages, network/demo message tables, "
        "game events, console variables & commands, and the game-content tables "
        "(items, game modes, surfaces, props, maps).\n"
    )
    if source_info.get("build_id"):
        lines.append(_provenance_block(source_info))
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
    lines.append("- [Schema Entities](generated/schemas.md) – Classes, structs, and enums from CS2's runtime schema ([codegen schema](generated/downstream-codegen-schemas/cs2_schema.json))")
    lines.append("- [Protobufs](generated/protobufs.md) – Network message and game event definitions")
    if gameevents is not None:
        lines.append("- [Game Events](generated/gameevents.md) – Game event definitions with field schemas ([codegen schema](generated/downstream-codegen-schemas/gameevents_schema.json))")
    lines.append("- [ConVars](generated/convars.md) – Console variable reference with flags and defaults ([codegen schema](generated/downstream-codegen-schemas/convars_schema.json))")
    lines.append("- [Commands](generated/commands.md) – Console command reference ([codegen schema](generated/downstream-codegen-schemas/commands_schema.json))")
    for title, fname in extra_pages:
        lines.append(f"- [{title}](generated/{fname})")
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
# Content-artifact pages (economy, wire tables, build metadata)
# ---------------------------------------------------------------------------
#
# These render SchemaTracker artifacts that have no analogue in the old
# DumpSource2 pipeline.  Each is content-gated: a build whose content depot
# was never acquired simply won't have the file, so every loader tolerates a
# missing artifact by returning an empty structure and the generator skips the
# page.


def _load_content_json(build_dir: Path, name: str) -> dict[str, Any] | None:
    """Load a SchemaTracker artifact JSON, or None if it isn't present."""
    path = build_dir / name
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _provenance_block(source_info: dict[str, Any]) -> str:
    """A one-line provenance callout for the top of a generated page."""
    build = source_info.get("build_id", "?")
    date = source_info.get("version_date", "")
    plat = source_info.get("platform", "")
    sv = source_info.get("schema_version", "")
    bits = [f"CS2 build **{build}**"]
    if date:
        bits.append(date)
    if plat:
        bits.append(f"`{plat}`")
    if sv:
        bits.append(f"schema `{sv}`")
    return f"{{: .note }}\n> Source: {' · '.join(bits)}\n"


def _md_escape(text: Any) -> str:
    return str(text or "").replace("|", "\\|").replace("\n", " ")


def generate_items_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Economy items, prefabs, paint/sticker/music kits, rarities, qualities."""
    lines = [_md_front_matter(layout="default", title="Items & Economy", nav_order="7")]
    lines.append("# Items & Economy\n")
    lines.append(_provenance_block(source_info))
    lines.append(
        "Economy definitions extracted from the content pack's `items_game.txt`: "
        "weapon / equipment items, their prefabs, paint kits (skins), sticker "
        "kits, music kits, and the rarity / quality scales.  Name tokens "
        "(`#SFUI_*`, `#PaintKit_*`, …) resolve to display strings via the "
        "localization table.\n"
    )

    items = data.get("items", [])
    lines.append(f"## Items ({len(items)})\n")
    lines.append("| defIndex | Name token | Classname | Prefab | Item type |")
    lines.append("|----------|------------|-----------|--------|-----------|")
    for it in items:
        lines.append(
            f"| {it.get('defIndex','')} | `{_md_escape(it.get('nameToken'))}` "
            f"| `{_md_escape(it.get('classname'))}` | `{_md_escape(it.get('prefab'))}` "
            f"| {_md_escape(it.get('itemTypeName'))} |"
        )
    lines.append("")

    paint = data.get("paintKits", [])
    lines.append(f"## Paint Kits — skins ({len(paint)})\n")
    lines.append("| defIndex | Name | Description tag |")
    lines.append("|----------|------|----------------|")
    for pk in paint:
        lines.append(
            f"| {pk.get('defIndex','')} | `{_md_escape(pk.get('name'))}` "
            f"| `{_md_escape(pk.get('descriptionTag'))}` |"
        )
    lines.append("")

    stickers = data.get("stickerKits", [])
    lines.append(f"## Sticker Kits ({len(stickers)})\n")
    lines.append("| defIndex | Name | Item name token | Description |")
    lines.append("|----------|------|-----------------|-------------|")
    for sk in stickers:
        lines.append(
            f"| {sk.get('defIndex','')} | `{_md_escape(sk.get('name'))}` "
            f"| `{_md_escape(sk.get('itemName'))}` | `{_md_escape(sk.get('descriptionString'))}` |"
        )
    lines.append("")

    music = data.get("musicDefinitions", [])
    lines.append(f"## Music Kits ({len(music)})\n")
    lines.append("| defIndex | Name | Loc name |")
    lines.append("|----------|------|----------|")
    for m in music:
        lines.append(
            f"| {m.get('defIndex','')} | `{_md_escape(m.get('name'))}` "
            f"| `{_md_escape(m.get('locName'))}` |"
        )
    lines.append("")

    prefabs = data.get("prefabs", [])
    lines.append(f"## Prefabs ({len(prefabs)})\n")
    lines.append("| id | Parent prefab | Classname | Item type |")
    lines.append("|----|---------------|-----------|-----------|")
    for pf in prefabs:
        lines.append(
            f"| `{_md_escape(pf.get('id'))}` | `{_md_escape(pf.get('prefab'))}` "
            f"| `{_md_escape(pf.get('classname'))}` | {_md_escape(pf.get('itemTypeName'))} |"
        )
    lines.append("")

    rarities = data.get("rarities", [])
    qualities = data.get("qualities", [])
    lines.append(f"## Rarities ({len(rarities)})\n")
    lines.append("| id | Value | Loc key | Weapon loc key |")
    lines.append("|----|-------|---------|----------------|")
    for r in rarities:
        lines.append(
            f"| `{_md_escape(r.get('id'))}` | {r.get('value','')} "
            f"| `{_md_escape(r.get('locKey'))}` | `{_md_escape(r.get('locKeyWeapon'))}` |"
        )
    lines.append("")
    lines.append(f"## Qualities ({len(qualities)})\n")
    lines.append("| id | Value |")
    lines.append("|----|-------|")
    for q in qualities:
        lines.append(f"| `{_md_escape(q.get('id'))}` | {q.get('value','')} |")
    lines.append("")

    (out_dir / "items.md").write_text("\n".join(lines), encoding="utf-8")


def generate_network_md(
    netmsgs: dict[str, Any] | None,
    demomsgs: dict[str, Any] | None,
    protos: list[dict],
    source_info: dict[str, Any],
    out_dir: Path,
) -> None:
    """Wire-protocol tables: message-ID → protobuf type, cross-linked to the proto pages."""
    # Build a message-name → proto file map for cross-linking.
    msg_to_file: dict[str, str] = {}

    def _index_messages(msgs: list[dict], filename: str) -> None:
        for m in msgs:
            msg_to_file[m["name"]] = filename
            _index_messages(m.get("nested", []), filename)

    for p in protos:
        stem = Path(p["filename"]).stem
        _index_messages(p.get("messages", []), stem)

    def _link(type_name: str) -> str:
        stem = msg_to_file.get(type_name)
        if stem:
            return f"[`{type_name}`](proto/{stem}.md)"
        return f"`{type_name}`"

    lines = [_md_front_matter(layout="default", title="Network Messages", nav_order="8")]
    lines.append("# Network & Demo Messages\n")
    lines.append(_provenance_block(source_info))
    lines.append(
        "The wire-protocol tables: integer message IDs mapped to the protobuf "
        "message type carried, recovered from a static RTTI scan of the shipped "
        "binaries.  Each type links to its definition on the "
        "[protobuf pages](protobufs.md).\n"
    )

    if netmsgs:
        for ch in netmsgs.get("channels", []):
            msgs = ch.get("messages", [])
            lines.append(f"## {ch.get('name','')} ({len(msgs)})\n")
            lines.append("| ID | Message type |")
            lines.append("|----|--------------|")
            for m in msgs:
                lines.append(f"| {m.get('id','')} | {_link(m.get('protoMessageType',''))} |")
            lines.append("")

    if demomsgs:
        msgs = demomsgs.get("messages", [])
        lines.append(f"## Demo stream (`.dem`) messages ({len(msgs)})\n")
        lines.append(
            "The command-ID table for demo playback — a flat id space where a "
            "single id can bind more than one message type.\n"
        )
        lines.append("| ID | Message type |")
        lines.append("|----|--------------|")
        for m in msgs:
            lines.append(f"| {m.get('id','')} | {_link(m.get('protoMessageType',''))} |")
        lines.append("")

    (out_dir / "network.md").write_text("\n".join(lines), encoding="utf-8")


def generate_gamemodes_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Game types / modes and the map-group registry."""
    lines = [_md_front_matter(layout="default", title="Game Modes", nav_order="9")]
    lines.append("# Game Modes & Map Groups\n")
    lines.append(_provenance_block(source_info))
    lines.append(
        "Game types and their nested game modes (from `gamemodes.txt`): max "
        "players, map groups, and per-mode convar overrides.\n"
    )

    for gt in data.get("gameTypes", []):
        modes = gt.get("gameModes", [])
        lines.append(f"## Game type: `{gt.get('id','')}` ({len(modes)} modes)\n")
        for gm in modes:
            lines.append(f"### `{gm.get('id','')}`\n")
            lines.append(f"- **Name token:** `{_md_escape(gm.get('nameId'))}`")
            lines.append(f"- **Max players:** {gm.get('maxPlayers','')}")
            mgs = gm.get("mapGroupsMp", [])
            if mgs:
                lines.append(f"- **Map groups:** {', '.join(f'`{g}`' for g in mgs)}")
            convars = gm.get("convars", [])
            if convars:
                lines.append(f"- **ConVar overrides:** {len(convars)}")
                lines.append("")
                lines.append("| ConVar | Value |")
                lines.append("|--------|-------|")
                for cv in convars:
                    lines.append(f"| `{_md_escape(cv.get('name'))}` | `{_md_escape(cv.get('value'))}` |")
            lines.append("")

    groups = data.get("mapGroups", [])
    lines.append(f"## Map groups ({len(groups)})\n")
    lines.append("| id | Maps |")
    lines.append("|----|------|")
    for g in groups:
        maps = ", ".join(f"`{m}`" for m in g.get("maps", []))
        lines.append(f"| `{_md_escape(g.get('id'))}` | {maps} |")
    lines.append("")

    (out_dir / "gamemodes.md").write_text("\n".join(lines), encoding="utf-8")


def generate_changelog_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """What changed between the previous committed build and this one."""
    lines = [_md_front_matter(layout="default", title="Changelog", nav_order="10")]
    lines.append("# Build Changelog\n")
    lines.append(_provenance_block(source_info))
    lines.append(
        f"Difference between build **{data.get('fromBuild','?')}** and "
        f"**{data.get('toBuild','?')}** (`{data.get('platform','')}`), grouped by "
        "data family.\n"
    )

    for fam in data.get("families", []):
        added, removed, changed = fam.get("added", []), fam.get("removed", []), fam.get("changed", [])
        if not (added or removed or changed):
            continue
        lines.append(
            f"## {fam.get('family','')} "
            f"(+{len(added)} / −{len(removed)} / ~{len(changed)})\n"
        )
        if added:
            lines.append("**Added:** " + ", ".join(f"`{_md_escape(a)}`" for a in added[:200]))
            if len(added) > 200:
                lines.append(f"… and {len(added) - 200} more")
            lines.append("")
        if removed:
            lines.append("**Removed:** " + ", ".join(f"`{_md_escape(r)}`" for r in removed[:200]))
            if len(removed) > 200:
                lines.append(f"… and {len(removed) - 200} more")
            lines.append("")
        if changed:
            lines.append("| Entry | Field changes |")
            lines.append("|-------|---------------|")
            for ch in changed[:400]:
                deltas = "; ".join(
                    f"{_md_escape(fc.get('field'))}: `{_md_escape(fc.get('oldValue'))}` → "
                    f"`{_md_escape(fc.get('newValue'))}`"
                    for fc in ch.get("fields", [])
                )
                lines.append(f"| `{_md_escape(ch.get('name'))}` | {deltas} |")
            if len(changed) > 400:
                lines.append(f"\n… and {len(changed) - 400} more changed entries")
            lines.append("")

    (out_dir / "changelog.md").write_text("\n".join(lines), encoding="utf-8")


def generate_maps_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Per-map radar/overview metadata + maps inventory."""
    lines = [_md_front_matter(layout="default", title="Maps", nav_order="11")]
    lines.append("# Maps & Radar Overviews\n")
    lines.append(_provenance_block(source_info))
    names = data.get("mapNames", [])
    lines.append(f"Maps inventory ({len(names)}): "
                 + ", ".join(f"`{n}`" for n in names) + "\n")
    lines.append("## Radar overview metadata\n")
    lines.append("| Map | Material | pos (x, y) | Scale | CT spawn | T spawn |")
    lines.append("|-----|----------|-----------|-------|----------|---------|")
    for m in data.get("maps", []):
        lines.append(
            f"| `{_md_escape(m.get('name'))}` | `{_md_escape(m.get('material'))}` "
            f"| {m.get('posX','')}, {m.get('posY','')} | {m.get('scale','')} "
            f"| {m.get('ctSpawnX','')}, {m.get('ctSpawnY','')} "
            f"| {m.get('tSpawnX','')}, {m.get('tSpawnY','')} |"
        )
    lines.append("")
    (out_dir / "maps.md").write_text("\n".join(lines), encoding="utf-8")


def generate_surfaces_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Per-material surface physics / footstep table."""
    lines = [_md_front_matter(layout="default", title="Surface Properties", nav_order="12")]
    lines.append("# Surface Properties\n")
    lines.append(_provenance_block(source_info))
    surfaces = data.get("surfaces", [])
    lines.append(
        f"{len(surfaces)} surface records — footstep sounds, physics, and "
        "bullet-penetration modifiers per material.  The same material can "
        "appear more than once, keyed by source file / scope.\n"
    )
    lines.append("| Surface | Scope | Source | Properties |")
    lines.append("|---------|-------|--------|------------|")
    for s in surfaces:
        props = "; ".join(
            f"{_md_escape(p.get('name'))}=`{_md_escape(p.get('value'))}`"
            for p in s.get("properties", [])
        )
        lines.append(
            f"| `{_md_escape(s.get('name'))}` | {_md_escape(s.get('scope'))} "
            f"| `{_md_escape(s.get('sourceFile'))}` | {props} |"
        )
    lines.append("")
    (out_dir / "surfaces.md").write_text("\n".join(lines), encoding="utf-8")


def generate_props_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Breakable-prop physics classes, gib groups, collision-group registry."""
    lines = [_md_front_matter(layout="default", title="Prop Data", nav_order="13")]
    lines.append("# Prop & Collision Data\n")
    lines.append(_provenance_block(source_info))

    prop_classes = data.get("propClasses", [])
    lines.append(f"## Prop classes ({len(prop_classes)})\n")
    lines.append("| Class | Properties |")
    lines.append("|-------|------------|")
    for pc in prop_classes:
        props = "; ".join(
            f"{_md_escape(p.get('name'))}=`{_md_escape(p.get('value'))}`"
            for p in pc.get("properties", [])
        )
        lines.append(f"| `{_md_escape(pc.get('id'))}` | {props} |")
    lines.append("")

    groups = data.get("collisionGroups", [])
    lines.append(f"## Collision groups ({len(groups)})\n")
    lines.append("| Group | Description | Interacts as | Interacts with |")
    lines.append("|-------|-------------|--------------|----------------|")
    for g in groups:
        lines.append(
            f"| `{_md_escape(g.get('collisionGroup'))}` | {_md_escape(g.get('description'))} "
            f"| {', '.join(f'`{x}`' for x in g.get('interactAs', []))} "
            f"| {', '.join(f'`{x}`' for x in g.get('interactWith', []))} |"
        )
    lines.append("")

    breakables = data.get("breakableModels", [])
    lines.append(f"## Breakable gib groups ({len(breakables)})\n")
    for b in breakables:
        lines.append(f"- **`{_md_escape(b.get('id'))}`**: {len(b.get('models', []))} models")
    lines.append("")
    (out_dir / "props.md").write_text("\n".join(lines), encoding="utf-8")


def generate_modules_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Per-binary inventory: hashes, sizes, and resolved interface versions."""
    lines = [_md_front_matter(layout="default", title="Modules", nav_order="14")]
    lines.append("# Binary Modules\n")
    lines.append(_provenance_block(source_info))
    modules = data.get("modules", [])
    lines.append(
        f"{len(modules)} binaries read for this build, each with its SHA-256, "
        "size, export / schema-registration counts, and the engine interface "
        "versions it resolved at load.\n"
    )
    lines.append("| Path | Size | Exports | Schema regs | Interfaces |")
    lines.append("|------|------|---------|-------------|------------|")
    for m in modules:
        ifaces = ", ".join(f"`{i}`" for i in m.get("resolvedInterfaces", []))
        lines.append(
            f"| `{_md_escape(m.get('path'))}` | {m.get('fileSize','')} "
            f"| {m.get('exportCount','')} | {m.get('schemaRegistrationCount','')} "
            f"| {ifaces} |"
        )
    lines.append("")
    (out_dir / "modules.md").write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Schema history (Layer A — the schema_evolution.json artifact)
# ---------------------------------------------------------------------------
#
# SchemaTracker emits one cumulative, whole-history schema_evolution.json per
# platform at a FIXED path (artifacts/schema_evolution/<platform>.json) — NOT
# under a build dir, because it rolls up every committed build's snapshot diff.
# Docs is a thin consumer (see the Schema Lens design): render the mechanical
# facts + a portable field_history view, and fold in community overlays for the
# judgment the machine deliberately withholds (confirmed renames, semantic
# breaks).  We never mutate the upstream artifact.

# How many changed classes to render in full field-op detail per recent
# transition (the big historical re-walks touch >1000 classes; cap the page).
_HISTORY_DETAIL_CLASS_CAP = 60
# How many of the most-recent non-empty transitions get a detail section.
_HISTORY_DETAIL_TRANSITIONS = 3

_FIELDOP_LABEL = {
    "ADD": "＋field",
    "REMOVE": "−field",
    "TYPE_CHANGE": "~type",
    "OFFSET_CHANGE": "~offset",
    "META_CHANGE": "~meta",
}


def load_schema_evolution(artifacts_root: Path, platform: str) -> dict[str, Any] | None:
    """Read the fixed-path cumulative evolution artifact, or None if absent.

    Lives at ``artifacts/schema_evolution/<platform>.json``, outside any build
    dir.  Content-gated like the other new artifacts: a tree that hasn't run the
    ``evolution`` pass simply won't have it, and the page is skipped.
    """
    path = artifacts_root / "schema_evolution" / f"{platform}.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _transition_counts(tr: dict[str, Any]) -> dict[str, int]:
    """Summary op counts for one transition."""
    changed = tr.get("classChanged", [])
    return {
        "class_added": len(tr.get("classAdded", [])),
        "class_removed": len(tr.get("classRemoved", [])),
        "class_changed": len(changed),
        "enum_added": len(tr.get("enumAdded", [])),
        "enum_removed": len(tr.get("enumRemoved", [])),
        "enum_changed": len(tr.get("enumChanged", [])),
        "field_ops": sum(len(cd.get("fieldOps", [])) for cd in changed),
    }


def _transition_is_empty(c: dict[str, int]) -> bool:
    return not any(c.values())


def _confirmed_rename_index(lens_overlay: dict[str, Any]) -> dict[tuple[str, str], dict]:
    """Index overlay-confirmed renames by (class, from-field) and (class, to-field)."""
    idx: dict[tuple[str, str], dict] = {}
    for r in lens_overlay.get("confirmed_renames", []) or []:
        cls = r.get("class", "")
        for fld in (r.get("from"), r.get("to")):
            if cls and fld:
                idx[(cls, fld)] = r
    return idx


def generate_schema_history_md(
    evolution: dict[str, Any],
    lens_overlay: dict[str, Any],
    source_info: dict[str, Any],
    out_dir: Path,
) -> None:
    """The schema-evolution "break radar": whole-history summary + recent detail."""
    transitions = evolution.get("transitions", [])
    baseline = evolution.get("baselineBuild", "?")
    latest = evolution.get("latestBuild", "?")
    platform = evolution.get("platform", source_info.get("platform", ""))

    summarised = [(tr, _transition_counts(tr)) for tr in transitions]
    non_empty = [(tr, c) for tr, c in summarised if not _transition_is_empty(c)]

    lines = [_md_front_matter(layout="default", title="Schema History", nav_order="15")]
    lines.append("# Schema History\n")
    lines.append(_provenance_block(source_info))

    if lens_overlay.get("description"):
        lines.append(str(lens_overlay["description"]).strip() + "\n")
    else:
        lines.append(
            "Field-precise, build-to-build evolution of the CS2 C++ entity schema, "
            "derived by diffing every committed `entity_schema.json` snapshot "
            "(SchemaTracker's cumulative `schema_evolution.json`, Layer A).  Unlike "
            "the coarse [Changelog](changelog.html) — which only reports *that* a "
            "class changed — this reports *which field* was added, removed, retyped, "
            "or moved.\n"
        )
    if lens_overlay.get("notes"):
        lines.append("{: .note }\n> " + str(lens_overlay["notes"]).strip().replace("\n", "\n> ") + "\n")

    lines.append(
        f"- **Platform:** `{platform}` (the canonical render; `linux-x86_64` "
        "differs only in offsets/sizes)\n"
        f"- **Baseline build:** `{baseline}` · **Latest build:** `{latest}`\n"
        f"- **Transitions:** {len(transitions)} total, **{len(non_empty)} with "
        f"structural changes** ({len(transitions) - len(non_empty)} no-op builds)\n"
        f"- **Full per-field history:** the portable "
        "[`field_history.json`](downstream-codegen-schemas/field_history.json) "
        "carries first/last-seen and the type history for every "
        f"`(class, field)` across all builds.\n"
    )
    lines.append(
        "To bring an instance captured under build *X* forward to build *Y*, apply "
        "each transition in `[X, Y)` in order.  Every op carries both endpoints, so "
        "the same chain replays backward.\n"
    )

    # --- whole-history summary table (non-empty only, most-recent first) ---
    lines.append("## Transitions with structural changes\n")
    lines.append("| Transition | Classes +/−/~ | Enums +/−/~ | Field ops |")
    lines.append("|------------|---------------|-------------|-----------|")
    for tr, c in reversed(non_empty):
        lines.append(
            f"| `{tr.get('fromBuild','')}` → `{tr.get('toBuild','')}` "
            f"| {c['class_added']} / {c['class_removed']} / {c['class_changed']} "
            f"| {c['enum_added']} / {c['enum_removed']} / {c['enum_changed']} "
            f"| {c['field_ops']} |"
        )
    lines.append("")

    # --- recent detail sections ---
    rename_idx = _confirmed_rename_index(lens_overlay)
    lines.append("## Most recent structural changes\n")
    detail = list(reversed(non_empty))[:_HISTORY_DETAIL_TRANSITIONS]
    if not detail:
        lines.append("_No structural changes recorded yet._\n")
    for tr, c in detail:
        frm, to = tr.get("fromBuild", ""), tr.get("toBuild", "")
        lines.append(f"### `{frm}` → `{to}`\n")
        added = tr.get("classAdded", [])
        removed = tr.get("classRemoved", [])
        if added:
            shown = ", ".join(f"`{a}`" for a in added[:40])
            more = f" … (+{len(added) - 40} more)" if len(added) > 40 else ""
            lines.append(f"**Classes added ({len(added)}):** {shown}{more}\n")
        if removed:
            shown = ", ".join(f"`{r}`" for r in removed[:40])
            more = f" … (+{len(removed) - 40} more)" if len(removed) > 40 else ""
            lines.append(f"**Classes removed ({len(removed)}):** {shown}{more}\n")

        changed = tr.get("classChanged", [])
        if changed:
            lines.append(f"**Classes changed ({len(changed)}):**\n")
            lines.append("| Class | Field ops | Layout |")
            lines.append("|-------|-----------|--------|")
            for cd in changed[:_HISTORY_DETAIL_CLASS_CAP]:
                kinds: dict[str, int] = {}
                for op in cd.get("fieldOps", []):
                    kinds[op.get("kind", "")] = kinds.get(op.get("kind", ""), 0) + 1
                ops_txt = ", ".join(
                    f"{_FIELDOP_LABEL.get(k, k)}×{n}" for k, n in sorted(kinds.items())
                ) or "—"
                layout = []
                if cd.get("resize"):
                    rz = cd["resize"]
                    layout.append(f"resize {rz.get('from','?')}→{rz.get('to','?')}")
                if cd.get("realign"):
                    layout.append("realign")
                if cd.get("reparent"):
                    layout.append("reparent")
                if cd.get("flags"):
                    layout.append("flags")
                # note any overlay-confirmed rename touching this class
                cls_name = cd.get("name", "")
                confirmed = [
                    r for (cn, _), r in rename_idx.items() if cn == cls_name
                ]
                if confirmed:
                    layout.append(f"✎{len(set(id(r) for r in confirmed))} rename")
                lines.append(
                    f"| `{cls_name}` | {ops_txt} | {', '.join(layout) or '—'} |"
                )
            if len(changed) > _HISTORY_DETAIL_CLASS_CAP:
                lines.append(
                    f"| … | _{len(changed) - _HISTORY_DETAIL_CLASS_CAP} more changed "
                    "classes — see `field_history.json`_ | |"
                )
            lines.append("")

    (out_dir / "schema-history.md").write_text("\n".join(lines), encoding="utf-8")


def generate_field_history_json(
    evolution: dict[str, Any],
    lens_overlay: dict[str, Any],
    source_info: dict[str, Any],
    out_dir: Path,
) -> Path:
    """Portable per-(class,field) history for downstream alias resolution (DVN G3).

    A straight projection of the artifact's ``fieldHistory``/``enumHistory``,
    plus overlay-confirmed renames folded into an authoritative ``aliasChain``
    (the two-tier field_history seam: SchemaTracker emits mechanical facts, Docs
    publishes the confirmed version).
    """
    rename_idx = _confirmed_rename_index(lens_overlay)

    fields = []
    for fh in evolution.get("fieldHistory", []):
        cls = fh.get("className", "")
        rec = {
            "class": cls,
            "field": fh.get("field", ""),
            "firstSeenBuild": fh.get("firstSeenBuild", ""),
            "lastSeenBuild": fh.get("lastSeenBuild", ""),
            "typeHistory": fh.get("typeHistory", []),
        }
        r = rename_idx.get((cls, fh.get("field", "")))
        if r:
            rec["confirmedRename"] = {
                "from": r.get("from", ""),
                "to": r.get("to", ""),
                "note": r.get("note", ""),
            }
        fields.append(rec)

    out = {
        "schema_format_version": SCHEMA_FORMAT_VERSION,
        "source": source_info,
        "platform": evolution.get("platform", source_info.get("platform", "")),
        "baseline_build": evolution.get("baselineBuild", ""),
        "latest_build": evolution.get("latestBuild", ""),
        "transition_count": len(evolution.get("transitions", [])),
        "fields": fields,
        "enums": [
            {
                "enum": eh.get("enumName", ""),
                "firstSeenBuild": eh.get("firstSeenBuild", ""),
                "lastSeenBuild": eh.get("lastSeenBuild", ""),
            }
            for eh in evolution.get("enumHistory", [])
        ],
    }
    path = out_dir / "downstream-codegen-schemas" / "field_history.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate CS2 Jekyll/Markdown documentation.")
    parser.add_argument("--repo-root", default=".", help="Path to the repository root")
    parser.add_argument(
        "--artifacts-root",
        default=None,
        help=(
            "Path to CS2OpenDev-SchemaTracker's artifacts/ directory "
            "(contains <build_id>/<platform>/ sets).  Defaults to "
            "<repo-root>/upstream/schema-tracker/artifacts."
        ),
    )
    parser.add_argument(
        "--build",
        default="latest",
        help=(
            "SchemaTracker build id to document, or 'latest' (default) for the "
            "highest-numbered committed build carrying the chosen platform."
        ),
    )
    parser.add_argument(
        "--platform",
        default="windows-x86_64",
        choices=["windows-x86_64", "linux-x86_64"],
        help="Which platform's artifact set to document (default: windows-x86_64).",
    )
    parser.add_argument("--output", default="docs", help="Jekyll source directory (home page goes here; the rest goes under <output>/generated/)")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    artifacts_root = (
        Path(args.artifacts_root).resolve() if args.artifacts_root
        else repo_root / "upstream" / "schema-tracker" / "artifacts"
    )
    out_dir = Path(args.output).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    generated_dir = out_dir / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)

    # Wipe the fully-regenerated per-item subdirectories so pages for
    # modules / protos that no longer exist in the current build (e.g. the
    # Source 2 editor/tooling schema, which SchemaTracker doesn't cover)
    # don't linger as stale orphans.  Flat files directly under generated/
    # are always overwritten in place, so they need no pruning.
    for sub in ("schemas", "proto", "diagrams"):
        stale = generated_dir / sub
        if stale.is_dir():
            shutil.rmtree(stale)
    # Content-artifact pages are content-gated (a build may not ship every
    # table), so clear them too and let this run recreate only what exists.
    for page in ("items.md", "network.md", "gamemodes.md", "changelog.md",
                 "maps.md", "surfaces.md", "props.md", "modules.md"):
        stale_page = generated_dir / page
        if stale_page.is_file():
            stale_page.unlink()

    overlays_dir = repo_root / "docs" / "overlays"

    print("Loading overlays…")
    if not HAS_YAML:
        print("  WARNING: PyYAML not found – overlay annotations will be skipped.")
        print("  Install with: pip install pyyaml")
    overlays = load_overlays(overlays_dir)
    print(f"  Loaded {len(overlays)} overlay file(s).")

    build_dir = resolve_build_dir(artifacts_root, args.build, args.platform)
    if build_dir is None:
        print(
            f"ERROR: could not resolve a SchemaTracker build under {artifacts_root} "
            f"(build={args.build!r}, platform={args.platform!r}).  Initialise the "
            "submodule (`git submodule update --init upstream/schema-tracker`) or "
            "pass --artifacts-root PATH.",
            file=sys.stderr,
        )
        return 2
    schema_source_info = build_source_info(build_dir, args.platform)
    print(f"Loading SchemaTracker build {schema_source_info.get('build_id', '?')} "
          f"({args.platform}) from {build_dir}…")
    entities = load_entity_schema(build_dir)
    print(f"  Loaded {len(entities)} entities across "
          f"{len({e['module'] for e in entities.values()})} modules.")
    if schema_source_info.get("version_date"):
        print(f"  Steam build date: {schema_source_info['version_date']} "
              f"(schema_version {schema_source_info.get('schema_version', '?')})")

    print("Reading proto descriptor set…")
    protos = load_proto_descriptors(build_dir / "protos.descriptorset")
    print(f"  Loaded {len(protos)} proto files.")

    print("Loading convars and commands…")
    convars = load_convars_json(build_dir / "convars.json")
    commands = load_commands_json(build_dir / "commands.json")
    print(f"  {len(convars)} convars, {len(commands)} commands.")

    print("Loading game events…")
    gameevents = load_gameevents_json(build_dir / "gameevents.json")
    print(f"  Loaded {len(gameevents)} game events.")

    print("Generating Markdown UML diagram pages…")
    uml_md = generate_module_uml_md(entities, generated_dir)
    generate_global_diagram_md(entities, generated_dir)
    print(f"  Generated {len(uml_md)} module UML Markdown pages.")

    print("Generating Markdown schema pages (per-type pages with memory layout)…")
    generate_schemas_index_md(entities, overlays, generated_dir, diagram_modules=uml_md)
    print(f"  Generated {len({e['module'] for e in entities.values()})} module index pages "
          f"covering {len(entities)} entities (one page each).")

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

    print("Generating content-artifact pages…")
    extra_pages: list[tuple[str, str]] = []  # (title, filename) for index nav

    items = _load_content_json(build_dir, "item_definitions.json")
    if items:
        generate_items_md(items, schema_source_info, generated_dir)
        extra_pages.append(("Items & Economy", "items.md"))

    netmsgs = _load_content_json(build_dir, "network_messages.json")
    demomsgs = _load_content_json(build_dir, "demo_messages.json")
    if netmsgs or demomsgs:
        generate_network_md(netmsgs, demomsgs, protos, schema_source_info, generated_dir)
        extra_pages.append(("Network Messages", "network.md"))

    gamemodes = _load_content_json(build_dir, "game_modes.json")
    if gamemodes:
        generate_gamemodes_md(gamemodes, schema_source_info, generated_dir)
        extra_pages.append(("Game Modes", "gamemodes.md"))

    changelog = _load_content_json(build_dir, "changelog.json")
    if changelog:
        generate_changelog_md(changelog, schema_source_info, generated_dir)
        extra_pages.append(("Changelog", "changelog.md"))

    maps = _load_content_json(build_dir, "map_overviews.json")
    if maps:
        generate_maps_md(maps, schema_source_info, generated_dir)
        extra_pages.append(("Maps", "maps.md"))

    surfaces = _load_content_json(build_dir, "surface_properties.json")
    if surfaces:
        generate_surfaces_md(surfaces, schema_source_info, generated_dir)
        extra_pages.append(("Surface Properties", "surfaces.md"))

    props = _load_content_json(build_dir, "prop_data.json")
    if props:
        generate_props_md(props, schema_source_info, generated_dir)
        extra_pages.append(("Prop Data", "props.md"))

    modules = _load_content_json(build_dir, "modules.json")
    if modules:
        generate_modules_md(modules, schema_source_info, generated_dir)
        extra_pages.append(("Modules", "modules.md"))
    print(f"  Generated {len(extra_pages)} content-artifact page(s).")

    print("Generating schema history (schema_evolution.json)…")
    evolution = load_schema_evolution(artifacts_root, args.platform)
    if evolution:
        lens_overlay = overlays.get("schema-lens", {}) or {}
        generate_schema_history_md(
            evolution, lens_overlay, schema_source_info, generated_dir
        )
        fh_path = generate_field_history_json(
            evolution, lens_overlay, schema_source_info, generated_dir
        )
        extra_pages.append(("Schema History", "schema-history.md"))
        n_tr = len(evolution.get("transitions", []))
        n_fh = len(evolution.get("fieldHistory", []))
        print(
            f"  Rendered {n_tr} transitions; wrote {fh_path.name} "
            f"({n_fh} field histories, {fh_path.stat().st_size // 1024} KiB)."
        )
    else:
        print("  No schema_evolution.json for this platform — skipped.")

    print("Generating Markdown home page…")
    generate_index_md(
        entities, protos, convars, commands, out_dir,
        gameevents=gameevents, source_info=schema_source_info, extra_pages=extra_pages,
    )

    print(f"\nDone!  Home page: {out_dir}/index.md")
    print(f"        Generated content: {generated_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
