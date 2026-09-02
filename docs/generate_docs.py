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
import math
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
# 2.1: SchemaTracker's 0.9.0 walkers (v1.3.0 corpus) added two fields to ATOMIC
# type nodes, echoed here verbatim — `atomicCategory` (the explicit
# SchemaAtomicCategory discriminator: ATOMIC_PLAIN / ATOMIC_T /
# ATOMIC_COLLECTION_OF_T / ATOMIC_TT / ATOMIC_I) and a widened `count`
# (COLLECTION_OF_T fixed-buffer capacity N, read from the binary's
# m_nFixedBufferCount — previously only the two ATOMIC_I bit-vector types
# carried a non-zero count). Additive → minor bump (SchemaTracker#8).
# 2.2: convars_schema.json gained the optional `value_type` key and the
# always-present numeric `min` / `max` keys (null when unbounded), and
# commands_schema.json gained `has_completion_callback`; all four were
# already loaded from the artifact and only the emitters dropped them.
# Additive → minor bump.
SCHEMA_FORMAT_VERSION = "2.2"

# Public site base, used to build absolute cross-links (e.g. cs2_schema.json's
# diagram_url, issue #21.4) that resolve for a consumer reading the JSON with
# no site context.  Matches the URLs hand-listed in AGENTS.md.
SITE_BASE = "https://cs2opendev.github.io/CS2OpenDev-Docs"

# Canonical C# namespace injected into the normalised .proto overlays (issue
# #21.3).  A single shared namespace puts every generated message type in one
# place, removing the CS0433 collision hazard consumers hit when the decompiled
# protos generate into the global namespace.  Org-scoped and distinct from the
# entity SDK's ``CS2OpenDev.Sdk.*`` roots.
PROTO_CSHARP_NAMESPACE = "CS2OpenDev.Protobuf"

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


def _bound_number(raw: Any) -> int | float | None:
    """A convar bound as a JSON number: int when integral, else float; None
    when blank or not finite (JSON has no Infinity)."""
    if raw in (None, ""):
        return None
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(value):
        return None
    return int(value) if value.is_integer() else value


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

def _strip_overlay_strings(node: Any) -> Any:
    """Strip surrounding whitespace from every string in an overlay tree."""
    if isinstance(node, str):
        return node.strip()
    if isinstance(node, dict):
        return {k: _strip_overlay_strings(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_strip_overlay_strings(v) for v in node]
    return node


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
        except (yaml.YAMLError, OSError) as exc:
            # A silent skip here removed every annotation of a module from the
            # site and the scheduled job committed the result.
            print(f"ERROR: {yml} failed to parse: {exc}", file=sys.stderr)
            sys.exit(2)
        if not isinstance(data, dict):
            continue
        # Block scalars (``description: >``) end in a newline that would land
        # inside a table cell and split the row.
        data = _strip_overlay_strings(data)
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



# Markdown table cells are line-oriented: a raw newline ends the row and
# GFM then rejects the whole block, and a bare `<word>` is parsed as an
# HTML tag.  Everything that reaches a cell goes through one of the four
# helpers below.  The split that matters is *who wrote the text*: upstream data
# from the game binaries is escaped hard, overlay YAML is authored Markdown and
# keeps its links and emphasis.

_CELL_NEWLINE_RE = re.compile(r"\s*(?:\r\n|\r|\n)\s*")
# Only a `<` that could open a tag; template types (`CUtlVector< int32 >`) keep
# their angle brackets so the raw Markdown stays readable.
_TAGLIKE_RE = re.compile(r"<(?=[A-Za-z/!?])")


def _defuse_tags(text: str) -> str:
    """Escape only the `<` characters that would start an HTML element."""
    return _TAGLIKE_RE.sub("&lt;", text)


def _md_cell(text: Any, newline: str = "<br>") -> str:
    """One upstream free-text value, safe for a Markdown table cell.

    HTML-escapes first (so `Test_LoopCount <count>` shows its arguments), then
    escapes the pipe, then folds newlines.
    """
    s = "" if text is None else str(text)
    s = s.strip()
    if not s:
        return ""
    s = html.escape(s, quote=False)
    s = s.replace("|", "\\|")
    return _CELL_NEWLINE_RE.sub(newline, s)


def _md_prose(text: Any, newline: str = "<br>") -> str:
    """One overlay-authored value, safe for a Markdown table cell.

    Overlay YAML is written by contributors as Markdown, so links and emphasis
    survive; only the two characters that break the table are touched.  Block
    scalars (``description: >``) end in a newline, hence the strip.
    """
    s = "" if text is None else str(text)
    s = s.strip()
    if not s:
        return ""
    s = s.replace("|", "\\|")
    return _CELL_NEWLINE_RE.sub(newline, s)


def _md_code_cell(text: Any) -> str:
    """Body of a backticked table cell.

    A code span renders its content literally, so HTML entities must *not* be
    pre-escaped here; `&#124;` is the only pipe form GFM renders inside code.
    """
    s = "" if text is None else str(text)
    s = s.strip()
    if not s:
        return ""
    s = s.replace("|", "&#124;")
    return _CELL_NEWLINE_RE.sub(" ", s)


def _code(value: Any) -> str:
    """A backticked cell, or an empty cell when the value is empty.

    Two adjacent empty code spans used to merge into a single cell containing
    a pipe and shift every following column left.
    """
    s = _md_code_cell(value)
    return f"`{s}`" if s else ""


def _md_escape(text: Any) -> str:
    """Deprecated alias for :func:`_md_cell`."""
    return _md_cell(text)


# Schema type names may be nested (``CNmBlend1DNode::CDefinition``); the old
# ``\b[A-Z_]\w+\b`` stopped at the first ``:`` and linked the outer class only.
_TYPE_REF_RE = re.compile(r"\b[A-Z_]\w+(?:::\w+)*\b")


def _longest_known_prefix(word: str, entities: dict[str, dict]) -> str | None:
    """Longest ``A::B::C`` prefix of *word* that names a known entity."""
    parts = word.split("::")
    for n in range(len(parts), 0, -1):
        cand = "::".join(parts[:n])
        if cand in entities:
            return cand
    return None


def _extract_type_refs(type_str: str, entities: dict[str, dict]) -> list[str]:
    """Return names of known schema entities referenced in a field type string."""
    seen: list[str] = []
    for m in _TYPE_REF_RE.finditer(type_str):
        word = _longest_known_prefix(m.group(0), entities)
        if word and word not in seen:
            seen.append(word)
    return seen


_MERMAID_PLAIN_RE = re.compile(r"^[A-Za-z_]\w*$")
_MERMAID_ID_RE = re.compile(r"\W")


def _mermaid_safe(name: str) -> str:
    """Make a name safe for Mermaid by quoting if needed.

    Mermaid 10.9's classDiagram grammar rejects a double-quoted class name
    (``"A::B"`` is a parse error); backticks parse in every position the
    generator emits - edges, class blocks, labelled arrows, enumerations.
    """
    if _MERMAID_PLAIN_RE.match(name):
        return name
    return f"`{name}`"


def _mermaid_id(name: str) -> str:
    """A plain-identifier node id for a qualified name."""
    return _MERMAID_ID_RE.sub("_", name)


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


def _proto_link_type(
    ftype: str,
    local_names: dict[str, str],
    global_names: dict[str, tuple[str, str]] | None = None,
) -> str:
    """Plain text for primitives, an anchor link for a type this build defines.

    Descriptor field types arrive fully qualified (``CDemoClassInfo.class_t``),
    so the qualified name is tried first; the simple name is only an alias when
    it is unambiguous.  A type defined in another file links to that file's
    page instead of a dead in-page anchor.
    """
    raw = ftype.lstrip(".")
    simple = raw.split(".")[-1]
    if simple in _PROTO_PRIMITIVES:
        return raw
    local = local_names.get(raw) or local_names.get(simple)
    if local:
        return f"[{raw}](#{_proto_anchor(local)})"
    if global_names:
        hit = global_names.get(raw) or global_names.get(simple)
        if hit:
            stem, qualified = hit
            return f"[{raw}]({stem}.md#{_proto_anchor(qualified)})"
    return _defuse_tags(raw)


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


def _resolve_variant(
    name: str,
    entities: dict[str, dict],
    prefer_module: str = "",
    prefer_binary_module: str = "",
) -> dict[str, Any] | None:
    """Return the ``(module, name)`` variant of *name* that a caller in
    *prefer_module* should read.

    ``entities`` is keyed by bare name and the first registration wins, so for
    the 189 client/server twins the client record is always the primary.  A
    server class walking to ``CBaseEntity`` must get the server record or it
    inherits the client layout and the client's offsets.  Preference order:
    same ``projectName``, then same binary module (SchemaTracker records the
    parent's binary in ``base_modules``), then the primary record.
    """
    primary = entities.get(name)
    if primary is None:
        return None
    dups = primary.get("duplicates")
    if not dups:
        return primary
    variants = [primary, *dups]
    if prefer_module:
        for v in variants:
            if v.get("module") == prefer_module:
                return v
    if prefer_binary_module:
        for v in variants:
            if v.get("binary_module") == prefer_binary_module:
                return v
    return primary


def _all_variants(name: str, entities: dict[str, dict]) -> list[dict[str, Any]]:
    """Every ``(module, name)`` record registered under *name*."""
    e = entities.get(name)
    if not e:
        return []
    return [e, *e.get("duplicates", [])]


def _base_variant_for(
    child: dict[str, Any], base_name: str, entities: dict[str, dict]
) -> dict[str, Any] | None:
    """Return the variant of *base_name* that *child* actually derives from.

    ``bases`` and ``base_modules`` are positionally paired, so the binary
    module of the parent is read off the same index.
    """
    bases = child.get("bases", [])
    bmods = child.get("base_modules", [])
    for i, b in enumerate(bases):
        if b == base_name:
            return _resolve_variant(
                b,
                entities,
                child.get("module", ""),
                bmods[i] if i < len(bmods) else "",
            )
    return None


def _own_children(
    variant: dict[str, Any],
    entities: dict[str, dict],
    children: dict[str, list[dict]],
) -> list[dict[str, Any]]:
    """Children that derive from *this* variant, not from a same-named twin.

    A client class listing ``CBaseAnimGraph`` as its base derives from the
    client variant; without this filter it also shows up under the server
    variant's Derived-by list and in its diagram.
    """
    name = variant["name"]
    return [
        c for c in children.get(name, [])
        if _base_variant_for(c, name, entities) is variant
    ]


def _declaring_module(
    row: dict[str, Any], entities: dict[str, dict], from_module: str
) -> str:
    """Grouping module of the class a layout row was declared in."""
    return row.get("declaring_module") or from_module


_BITFIELD_RE = re.compile(r"^bitfield:(\d+)$")


def _annotate_bitfields(rows: list[dict[str, Any]]) -> None:
    """Attach a ``bits`` (lo, hi) range to each run of bitfield rows.

    Every member of a bitfield shares the byte offset; the bit position is
    only recoverable by accumulating the declared widths in order, which the
    offset sort preserves.
    """
    run_offset: Any = None
    bit = 0
    for r in rows:
        fld = r["field"]
        off = fld.get("offset")
        m = _BITFIELD_RE.match(str(fld.get("type", "")))
        if not m or not isinstance(off, int):
            run_offset = None
            bit = 0
            continue
        width = int(m.group(1))
        if off != run_offset:
            run_offset = off
            bit = 0
        r["bits"] = (bit, bit + width - 1)
        bit += width


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
            rows.append({
                "field": f,
                "declaring": e["name"],
                "declaring_module": e.get("module", ""),
                "inherited": not is_self,
            })

    def walk_bases(e: dict[str, Any]) -> None:
        for i, b in enumerate(e.get("bases", [])):
            if i == 0:
                if b in visited:
                    continue
                visited.add(b)
                be = _base_variant_for(e, b, entities)
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
    _annotate_bitfields(rows)
    return rows, secondary


def check_module_layout_consistency(
    entities: dict[str, dict]
) -> tuple[list[str], int]:
    """Verify no page inherits a layout from a foreign-module twin.

    Returns ``(violations, exempt)``.  A violation is an inherited row whose
    declaring class sits in another module *while a same-module variant of
    that class exists*, which is the client/server offset mixing this build
    once shipped.  ``exempt`` counts the legitimate cross-module rows: bases such
    as ``CPlayerPawnComponent`` that SchemaTracker only ever registers under
    one projectName, so there is no same-module variant to prefer.
    """
    violations: list[str] = []
    exempt = 0
    for entity in entities.values():
        for variant in (entity, *entity.get("duplicates", [])):
            if variant.get("kind") == "enum":
                continue
            mod = variant.get("module", "")
            rows, _ = _flatten_layout(variant, entities)
            for r in rows:
                if not r["inherited"]:
                    continue
                dname = r["declaring"]
                dmod = r.get("declaring_module", "")
                if dmod == mod:
                    continue
                dmods = {v.get("module", "") for v in _all_variants(dname, entities)}
                if mod in dmods:
                    violations.append(
                        f"{mod}/{variant['name']}: field "
                        f"`{r['field'].get('name', '')}` attributed to "
                        f"{dmod or '?'}/{dname}"
                    )
                else:
                    exempt += 1
    return violations, exempt


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
        cand = _longest_known_prefix(word, entities)
        if cand:
            href = _schema_page_href(cand, entities, current_module)
            if href:
                rest = word[len(cand):]
                return f"[{cand}]({href}){rest}"
        return word

    return _TYPE_REF_RE.sub(replace, _defuse_tags(type_str).replace("|", "\\|"))


_UNSIGNED_UNDERLYING_RE = re.compile(r"^uint(\d+)_t$")


def _enum_value_cell(value: Any, underlying: Any) -> str:
    """Render an enum member's value.

    SchemaTracker reports member values signed.  Under an unsigned underlying
    type a `-1` is really the all-ones pattern, so the wrapped hex is shown
    alongside it rather than leaving the reader to guess the width.
    """
    s = "" if value is None else str(value).strip()
    if not s:
        return ""
    m = _UNSIGNED_UNDERLYING_RE.match(str(underlying or ""))
    if m:
        try:
            n = int(s, 0)
        except ValueError:
            return _md_cell(s)
        if n < 0:
            bits = int(m.group(1))
            return f"{s} (`0x{n & ((1 << bits) - 1):x}`)"
    return _md_cell(s)


def _md_front_matter(**kwargs: str) -> str:
    """Render a small YAML front matter block for a generated page."""
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


def _build_children_index(entities: dict[str, dict]) -> dict[str, list[dict]]:
    """Map base-class name to the entities that list it in ``bases``.

    Every ``(module, name)`` variant is indexed, not just the primary record,
    so a server class's children include the server twins that ``_add_entity``
    parked under ``duplicates``.  Callers narrow the list with
    :func:`_own_children`.
    """
    children: dict[str, list[dict]] = defaultdict(list)
    for e in entities.values():
        for variant in (e, *e.get("duplicates", [])):
            for b in dict.fromkeys(variant.get("bases", [])):
                children[b].append(variant)
    return children


def _build_md_relationship_diagram(
    name: str,
    entity: dict,
    entities: dict[str, dict],
    children: dict[str, list[dict]] | None = None,
) -> list[str]:
    """Build Mermaid classDiagram lines for an entity's relationships."""
    if children is None:
        children = _build_children_index(entities)
    lines: list[str] = []
    seen_edges: set[tuple[str, str]] = set()

    # Walk up inheritance chain (up to 5 levels), staying inside the module
    # the page belongs to whenever the base has a same-module variant.
    chain: list[str] = [name]
    current = entity
    for _ in range(5):
        bases = current.get("bases", [])
        if not bases:
            break
        parent = bases[0]
        chain.append(parent)
        current = _base_variant_for(current, parent, entities) or {}
        if not current:
            break

    for i in range(len(chain) - 1):
        child = chain[i]
        parent = chain[i + 1]
        edge = (parent, child)
        if edge not in seen_edges:
            lines.append(f"    {_mermaid_safe(parent)} <|-- {_mermaid_safe(child)}")
            seen_edges.add(edge)

    for e in _own_children(entity, entities, children):
        if e["name"] != name:
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
    children: dict[str, list[dict]] | None = None,
    source_info: dict[str, Any] | None = None,
) -> str:
    """Render one class/enum's standalone Markdown page (``schemas/<mod>/<Type>.md``).

    The class case carries the full **memory layout** — own fields plus fields
    inherited along the primary-parent spine, each with its absolute offset —
    which the old single-file-per-module rendering never produced.
    """
    if children is None:
        children = _build_children_index(entities)
    name = e["name"]
    kind = e["kind"]
    overlay = get_overlay(overlays, mod, name)
    L: list[str] = []
    # The 189 client/server twins share a bare name; the module goes in the
    # title so a search result says which one it landed on.
    twins = [v for v in _all_variants(name, entities) if v.get("module") != mod]
    title = f"{name} ({mod})" if twins else name
    L.append(_md_front_matter(title=title, module=mod, kind=kind))

    # Breadcrumb (this page lives at schemas/<mod>/<Type>.md).
    L.append(f"[Schemas](../../schemas.md) / [{mod}](../{mod}.md) / {name}\n")
    L.append(f"# {name}\n")
    if source_info:
        L.append(_provenance_block(source_info))

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
        # 0xFF is the schema system's "alignment unspecified" sentinel.
        align = e["alignment"]
        stats.append(
            "**Align:** n/a (unspecified)" if align == 255 else f"**Align:** {align}"
        )
    if kind == "enum" and e.get("enum_underlying"):
        stats.append(f"**Underlying:** `{e['enum_underlying']}`")
    stats.append(f"**Module:** {mod}")
    L.append(" · ".join(stats) + "\n")

    if twins:
        links = ", ".join(
            f"[{name} ({v['module']})](../{v['module']}/{_type_filename(name)}.md)"
            for v in sorted(twins, key=lambda v: v.get("module", ""))
        )
        L.append(f"**Twin:** {links}\n")

    # Inherits / derived.
    if e.get("bases"):
        base_links = []
        for b in e["bases"]:
            href = _schema_page_href(b, entities, mod)
            base_links.append(f"[{b}]({href})" if href else b)
        L.append(f"**Inherits from:** {', '.join(base_links)}\n")
    derived = sorted(_own_children(e, entities, children), key=lambda x: x["name"])
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
            _code(_format_metadata(m)) for m in e["metadata"]
            if isinstance(m, dict) and m.get("name")
            and not m["name"].startswith("MNetworkVarNames")
            and m["name"] != "MGetKV3ClassDefaults"
        ]
        if tags:
            L.append(f"**Metadata:** {', '.join(tags)}\n")

    # Relationship diagram.
    diagram_lines = _build_md_relationship_diagram(name, e, entities, children)
    if diagram_lines:
        L.append("**Relationships:**\n")
        L.append("```mermaid")
        L.append("classDiagram")
        L.extend(diagram_lines)
        L.append("```\n")

    if kind == "enum":
        vals = e.get("fields", [])
        underlying = e.get("enum_underlying") or ""
        overlay_members = overlay.get("fields", {}) or {}
        if not isinstance(overlay_members, dict):
            overlay_members = {}
        if vals:
            L.append("## Values\n")
            L.append("| Name | Value | Description |")
            L.append("|------|-------|-------------|")
            for fld in vals:
                parts: list[str] = []
                mover = overlay_members.get(fld["name"], {})
                if isinstance(mover, dict):
                    if mover.get("description"):
                        parts.append(_md_prose(mover["description"]))
                    if mover.get("notes"):
                        parts.append(f"*{_md_prose(mover['notes'])}*")
                upstream = _md_cell(_metadata_friendly_text(fld.get("annotations")))
                if upstream:
                    parts.append(upstream)
                L.append(
                    f"| {_code(fld['name'])} | {_enum_value_cell(fld.get('value', ''), underlying)} "
                    f"| {' '.join(p for p in parts if p)} |"
                )
            L.append("")
    else:
        rows, secondary = _flatten_layout(e, entities)
        overlay_fields = overlay.get("fields", {}) or {}
        if not isinstance(overlay_fields, dict):
            overlay_fields = {}
        if rows:
            own = sum(1 for r in rows if not r["inherited"])
            L.append("## Memory layout\n")
            L.append(
                f"{len(rows)} {'field' if len(rows) == 1 else 'fields'} "
                f"({own} declared here, {len(rows) - own} "
                "inherited). Offsets are absolute from the object base.\n"
            )
            L.append("| Offset | Field | Type | From | Annotations |")
            L.append("|--------|-------|------|------|-------------|")
            for r in rows:
                fld = r["field"]
                fname = fld.get("name", "")
                off = fld.get("offset")
                off_str = f"`0x{off:x}`" if isinstance(off, int) else "—"
                bits = r.get("bits")
                if bits and isinstance(off, int):
                    lo, hi = bits
                    off_str += f" bit {lo}" if hi == lo else f" bits {lo}..{hi}"
                type_linked = _md_link_type(fld.get("type", ""), entities, mod)
                if r["inherited"]:
                    dhref = _schema_page_href(r["declaring"], entities, mod)
                    from_cell = (
                        f"[{r['declaring']}]({dhref})" if dhref else r["declaring"]
                    )
                else:
                    from_cell = ""
                annot_str = " ".join(
                    _code(_format_metadata(a))
                    for a in fld.get("annotations", [])
                    if isinstance(a, dict) and a.get("name")
                )
                desc_parts: list[str] = []
                # An inherited row carries the *declaring* class's annotation:
                # 87% of the rows on this site are inherited copies, so looking
                # only at this page's overlay hides almost all field prose.
                if r["inherited"]:
                    dover = get_overlay(
                        overlays, _declaring_module(r, entities, mod), r["declaring"]
                    )
                    dfields = dover.get("fields", {}) if isinstance(dover, dict) else {}
                    fover = (
                        dfields.get(fname, {}) if isinstance(dfields, dict) else {}
                    )
                else:
                    fover = overlay_fields.get(fname, {})
                if fover and isinstance(fover, dict):
                    if fover.get("description"):
                        desc_parts.append(_md_prose(fover["description"]))
                    if fover.get("notes"):
                        desc_parts.append(f"*{_md_prose(fover['notes'])}*")
                if annot_str:
                    desc_parts.append(annot_str)
                ann_cell = " ".join(p for p in desc_parts if p)
                L.append(
                    f"| {off_str} | {_code(fname)} | {type_linked} | {from_cell} "
                    f"| {ann_cell} |"
                )
            L.append("")
        else:
            L.append("## Memory layout\n")
            size = e.get("size")
            size_txt = f" ({size} bytes of opaque storage)" if isinstance(size, int) else ""
            L.append(f"No schema-visible fields{size_txt}.\n")
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
    # scannable.  Rendered as escaped <pre> since the raw value can itself
    # contain angle brackets and quotes.
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
    source_info: dict[str, Any] | None = None,
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

    # One base-name -> children index for the whole run; the per-page
    # relationship diagram and the Derived-by list both read it.
    children = _build_children_index(entities)

    # Master schemas.md
    lines: list[str] = []
    lines.append(_md_front_matter(title="Schemas"))
    lines.append("# Schema Reference\n")
    if source_info:
        lines.append(_provenance_block(source_info))
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
            title=mod,
            module=mod,
        ))
        idx.append(f"# Module: {mod}\n")
        if source_info:
            idx.append(_provenance_block(source_info))
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
            page = _render_schema_type_page(
                e, mod, entities, overlays, children, source_info
            )
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
            title=f"UML: {mod}",
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


def _proto_flatten_messages(
    msgs: list[dict], prefix: str = ""
) -> list[tuple[str, dict]]:
    """``(qualified name, message)`` for every message, nested included."""
    out: list[tuple[str, dict]] = []
    for m in msgs:
        qualified = f"{prefix}{m['name']}"
        out.append((qualified, m))
        out.extend(_proto_flatten_messages(m.get("nested", []), f"{qualified}."))
    return out


def _proto_flatten_enums(proto: dict) -> list[tuple[str, dict]]:
    """``(qualified name, enum)`` for top-level and message-nested enums."""
    out: list[tuple[str, dict]] = [
        (e["name"], e) for e in proto.get("enums", [])
    ]
    for qualified, msg in _proto_flatten_messages(proto.get("messages", [])):
        for en in msg.get("enums", []):
            out.append((f"{qualified}.{en['name']}", en))
    return out


def _proto_name_index(proto: dict) -> dict[str, str]:
    """Map every way a field can name a local type to its qualified name.

    A simple name is registered as an alias only when it is unambiguous in
    this file: ``key_t`` exists under two different parents in
    ``gameevents.proto``, and collapsing them merged two unrelated types.
    """
    qualified = [q for q, _ in _proto_flatten_messages(proto.get("messages", []))]
    qualified += [q for q, _ in _proto_flatten_enums(proto)]
    index: dict[str, str] = {q: q for q in qualified}
    simple_counts: dict[str, int] = {}
    for q in qualified:
        simple_counts[q.split(".")[-1]] = simple_counts.get(q.split(".")[-1], 0) + 1
    for q in qualified:
        simple = q.split(".")[-1]
        if simple_counts[simple] == 1:
            index.setdefault(simple, q)
    return index


def _build_proto_mermaid(proto: dict) -> list[str]:
    """Build Mermaid classDiagram lines for a proto file.

    Returns a list of lines to be embedded inside a ``classDiagram`` block.
    Returns an empty list when there is nothing to diagram.
    """
    all_msgs = _proto_flatten_messages(proto.get("messages", []))
    all_enums = _proto_flatten_enums(proto)

    if not all_msgs and not all_enums:
        return []

    # Node ids are qualified so two nested types with the same simple name
    # (``key_t`` under two parents) stay separate nodes.
    names = _proto_name_index(proto)

    def node(qualified: str) -> str:
        return _mermaid_id(qualified)

    def decl(qualified: str) -> str:
        nid = _mermaid_id(qualified)
        return f'{nid}["{qualified}"]' if nid != qualified else nid

    lines: list[str] = ["direction LR", ""]

    for qualified, msg in all_msgs:
        lines.append(f"  class {decl(qualified)} {{")
        for fld in msg.get("fields", []):
            ftype = fld["type"].lstrip(".")
            type_str = f"List~{ftype}~" if fld.get("label") == "repeated" else ftype
            lines.append(f"    +{type_str} {fld['name']}")
        lines.append("  }")
        lines.append("")

    # Relationship arrows (message-type fields within the same file)
    seen_arrows: set[str] = set()
    for qualified, msg in all_msgs:
        src = node(qualified)
        for fld in msg.get("fields", []):
            raw = fld["type"].lstrip(".")
            if raw.split(".")[-1] in _PROTO_PRIMITIVES:
                continue
            target = names.get(raw) or names.get(raw.split(".")[-1])
            if not target:
                continue
            tgt = node(target)
            arrow_key = f"{src}-->{tgt}"
            if arrow_key in seen_arrows:
                continue
            seen_arrows.add(arrow_key)
            suffix = "[]" if fld.get("label") == "repeated" else ""
            lines.append(f"  {src} --> {tgt} : {fld['name']}{suffix}")
    if seen_arrows:
        lines.append("")

    for qualified, en in all_enums:
        lines.append(f"  class {decl(qualified)}{{")
        lines.append("    <<enumeration>>")
        for v in en.get("values", []):
            lines.append(f"    {v['name']}")
        lines.append("  }")
        lines.append("")

    return lines


def _proto_global_index(protos: list[dict]) -> dict[str, tuple[str, str]]:
    """Map a type name to ``(page stem, qualified name)`` across every file.

    Files are walked in filename order and the first definition of a name
    wins, so the 2 cross-file symbol collisions the decompiled set carries
    resolve deterministically.
    """
    index: dict[str, tuple[str, str]] = {}
    for proto in sorted(protos, key=lambda x: x["filename"]):
        stem = proto["filename"].removesuffix(".proto")
        for alias, qualified in _proto_name_index(proto).items():
            index.setdefault(alias, (stem, qualified))
    return index


def _proto_field_desc(
    fld: dict, fover: dict | None
) -> str:
    """The Description cell for one proto field row."""
    parts: list[str] = []
    if isinstance(fover, dict) and fover.get("description"):
        parts.append(_md_prose(fover["description"]))
    if fld.get("comment"):
        parts.append(_md_cell(fld["comment"]))
    if fld.get("oneof"):
        parts.append(f"*(oneof: {_code(fld['oneof'])})*")
    if fld.get("deprecated"):
        parts.append("**deprecated**")
    if fld.get("packed") is True:
        parts.append("*(packed)*")
    if fld.get("default", ""):
        parts.append(f"*(default: {_code(fld['default'])})*")
    return " ".join(p for p in parts if p)


def generate_protobufs_md_page(
    protos: list[dict],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate protobufs.md and per-file proto Markdown pages."""
    (out_dir / "proto").mkdir(exist_ok=True)

    global_names = _proto_global_index(protos)
    stems = {p["filename"].removesuffix(".proto") for p in protos}

    # Master index
    idx_lines: list[str] = []
    idx_lines.append(_md_front_matter(title="Protobufs"))
    idx_lines.append("# Protobuf Reference\n")
    idx_lines.append("Network message definitions and game event structures from CS2's Protobufs directory.\n")
    idx_lines.append("| File | Messages | Enums |")
    idx_lines.append("|------|----------|-------|")
    for proto in sorted(protos, key=lambda x: x["filename"]):
        fname = proto["filename"]
        stem = fname.removesuffix(".proto")
        top_msgs = len(proto.get("messages", []))
        all_msgs = len(_proto_flatten_messages(proto.get("messages", [])))
        top_enums = len(proto.get("enums", []))
        all_enums = len(_proto_flatten_enums(proto))
        msg_cell = (
            f"{top_msgs} (+{all_msgs - top_msgs} nested)"
            if all_msgs > top_msgs else str(top_msgs)
        )
        enum_cell = (
            f"{top_enums} (+{all_enums - top_enums} nested)"
            if all_enums > top_enums else str(top_enums)
        )
        idx_lines.append(f"| [{fname}](proto/{stem}.md) | {msg_cell} | {enum_cell} |")
    idx_lines.append("")
    (out_dir / "protobufs.md").write_text("\n".join(idx_lines), encoding="utf-8")

    # Per-file pages
    for proto in protos:
        pfile = proto["filename"]
        stem = pfile.removesuffix(".proto")
        overlay = overlays.get(f"protobufs/{stem}", {})
        local_names = _proto_name_index(proto)

        p_lines: list[str] = []
        p_lines.append(_md_front_matter(
            title=pfile,
            proto=pfile,
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
            import_cells = []
            for imp in proto["imports"]:
                istem = imp.removesuffix(".proto")
                import_cells.append(
                    f"[`{imp}`]({istem}.md)" if istem in stems else f"`{imp}`"
                )
            meta_bits.append("**Imports:** " + ", ".join(import_cells))
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

        def _enum_section(qualified: str, en: dict, level: int) -> None:
            p_lines.append(f"{'#' * level} `{qualified}`\n")
            p_lines.append("| Name | Value |")
            p_lines.append("|------|-------|")
            for v in en.get("values", []):
                p_lines.append(f"| {_code(v['name'])} | {v['number']} |")
            p_lines.append("")

        if proto.get("enums"):
            p_lines.append("## Enums\n")
            for en in proto["enums"]:
                _enum_section(en["name"], en, 3)

        overlay_msgs: dict = overlay.get("messages", {}) or {}
        if not isinstance(overlay_msgs, dict):
            overlay_msgs = {}

        def _message_section(qualified: str, msg: dict, level: int) -> None:
            mname = msg["name"]
            # Overlay keys are written as the message name; a nested type can
            # also be addressed by its qualified name.
            mover = overlay_msgs.get(qualified) or overlay_msgs.get(mname) or {}
            if not isinstance(mover, dict):
                mover = {}
            p_lines.append(f"{'#' * level} `{qualified}`\n")
            if mover.get("description"):
                p_lines.append(f"{mover['description']}\n")
            if mover.get("notes"):
                p_lines.append(f"> 📝 {mover['notes']}\n")

            # Surface oneof groups before the fields table so readers
            # know which fields are mutually exclusive.
            nonempty_oneofs = [o for o in msg.get("oneofs", []) if o.get("fields")]
            if nonempty_oneofs:
                oneof_bits = ", ".join(
                    f"`{o['name']}` ({', '.join(o['fields'])})"
                    for o in nonempty_oneofs
                )
                p_lines.append(f"**Oneofs:** {oneof_bits}\n")

            if msg.get("fields"):
                overlay_flds = mover.get("fields", {}) or {}
                if not isinstance(overlay_flds, dict):
                    overlay_flds = {}
                p_lines.append("| Field | Number | Type | Label | Description |")
                p_lines.append("|-------|--------|------|-------|-------------|")
                for fld in sorted(
                    msg["fields"], key=lambda f: int(f.get("number", "0"))
                ):
                    ftype_display = _proto_link_type(
                        fld["type"], local_names, global_names
                    )
                    p_lines.append(
                        f"| {_code(fld['name'])} | {fld.get('number', '')} "
                        f"| {ftype_display} | {fld.get('label', 'optional')} "
                        f"| {_proto_field_desc(fld, overlay_flds.get(fld['name']))} |"
                    )
                p_lines.append("")
            else:
                p_lines.append("*(no fields)*\n")

            for en in msg.get("enums", []):
                _enum_section(f"{qualified}.{en['name']}", en, min(level + 1, 6))
            for nested in msg.get("nested", []):
                _message_section(
                    f"{qualified}.{nested['name']}", nested, min(level + 1, 6)
                )

        if proto.get("messages"):
            p_lines.append("## Messages\n")
            for msg in proto["messages"]:
                _message_section(msg["name"], msg, 3)

        (out_dir / "proto" / f"{stem}.md").write_text("\n".join(p_lines), encoding="utf-8")


def _convar_range(cv: dict) -> str:
    """The `min .. max` bound cell for a convar, or an empty cell."""
    lo = str(cv.get("min_value", "") or "") if cv.get("has_min") else ""
    hi = str(cv.get("max_value", "") or "") if cv.get("has_max") else ""
    if lo and hi:
        return _code(f"{lo} .. {hi}")
    if lo:
        return _code(f">= {lo}")
    if hi:
        return _code(f"<= {hi}")
    return ""


def generate_convars_md_page(
    convars: list[dict],
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
) -> None:
    """Generate convars.md."""
    lines: list[str] = []
    lines.append(_md_front_matter(title="ConVars"))
    lines.append("# ConVar Reference\n")
    if source_info:
        lines.append(_provenance_block(source_info))
    lines.append(
        "All console variables extracted from CS2, with the value type and the "
        "bounds the engine enforces where it declares them.\n"
    )
    lines.append("| Name | Type | Default | Range | Flags | Description |")
    lines.append("|------|------|---------|-------|-------|-------------|")
    for cv in convars:
        flags = " ".join(_code(f) for f in cv["flags"])
        lines.append(
            f"| {_code(cv['name'])} | {_code(cv.get('value_type'))} "
            f"| {_code(cv['default'])} | {_convar_range(cv)} | {flags} "
            f"| {_md_cell(cv['description'])} |"
        )
    lines.append("")
    (out_dir / "convars.md").write_text("\n".join(lines), encoding="utf-8")


def generate_commands_md_page(
    commands: list[dict],
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
) -> None:
    """Generate commands.md."""
    lines: list[str] = []
    lines.append(_md_front_matter(title="Commands"))
    lines.append("# Console Commands\n")
    if source_info:
        lines.append(_provenance_block(source_info))
    lines.append("All console commands extracted from CS2.\n")
    lines.append("| Command | Flags | Description |")
    lines.append("|---------|-------|-------------|")
    for cmd in commands:
        flags = " ".join(_code(f) for f in cmd["flags"])
        if cmd.get("has_completion_callback"):
            flags = (flags + " " if flags else "") + "`autocomplete`"
        lines.append(
            f"| {_code(cmd['name'])} | {flags} | {_md_cell(cmd['description'])} |"
        )
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
    lines.append(_md_front_matter(title="Game Events"))
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
        lines.append(f"| {_code(tname)} | {_md_cell(tinfo['description'])} |")
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
        lines.append(f"| {_code(src)} | {len(by_source[src])} | {_md_cell(label)} |")
    lines.append("")

    # Heading text per event, computed once so the index anchors and the
    # section headings can never drift apart.  15 event names occur in two or
    # three source files; a bare `#name` index link sent 16 rows to the wrong
    # section.
    duplicated = {
        n for n in {ev["name"] for ev in gameevents}
        if sum(1 for ev in gameevents if ev["name"] == n) > 1
    }
    headings: dict[int, str] = {
        id(ev): (f"{ev['name']} ({ev['source']})" if ev["name"] in duplicated
                 else ev["name"])
        for ev in gameevents
    }

    # Quick-reference index
    lines.append("## Event Index\n")
    lines.append("| Event | Source | Fields | Description |")
    lines.append("|-------|--------|--------|-------------|")
    for ev in gameevents:
        anchor = _proto_anchor(headings[id(ev)])
        eov = overlay_events.get(ev["name"], {}) if isinstance(overlay_events, dict) else {}
        desc = ""
        if eov and isinstance(eov, dict) and eov.get("description"):
            desc = _md_prose(eov["description"])
        elif ev["comment"]:
            desc = _md_cell(ev["comment"])
        lines.append(
            f"| [{ev['name']}](#{anchor}) | {_code(ev['source'])} "
            f"| {len(ev['fields'])} | {desc} |"
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

            lines.append(f"### {headings[id(ev)]}\n")

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
                        desc_parts.append(_md_prose(fov["description"]))
                    if fld["comment"]:
                        desc_parts.append(_md_cell(fld["comment"]))
                    if fov and isinstance(fov, dict) and fov.get("notes"):
                        desc_parts.append(f"*{_md_prose(fov['notes'])}*")
                    desc = " ".join(p for p in desc_parts if p)
                    lines.append(f"| {_code(fname)} | {_code(ftype)} | {desc} |")
                lines.append("")
            else:
                lines.append("*No fields — this event carries no additional data.*\n")

    (out_dir / "gameevents.md").write_text("\n".join(lines), encoding="utf-8")


def _coerce_build_id(val: Any) -> Any:
    """Return *val* as an ``int`` when it is an all-digits string, else the
    value unchanged.

    Issue #19: ``build_id`` is the Steam CS2 game build — a monotonic,
    numeric provenance key.  SchemaTracker's ``provenance.json`` stores
    ``buildId`` as a string (``"24537688"``); ``LATEST.json`` stores it as a
    number.  Normalise to a number so the emitted header is consistent and
    consumers can stamp it without re-parsing.
    """
    if isinstance(val, bool):  # bool is an int subclass — never a build id
        return val
    if isinstance(val, int):
        return val
    if isinstance(val, str) and val.isdigit():
        return int(val)
    return val


def _schema_header(source_info: dict[str, Any] | None) -> dict[str, Any]:
    """The shared provenance header echoed into every downstream schema.

    Carries ``build_id`` (the Steam CS2 game build — numeric and monotonic;
    issue #19) and ``platform`` (which OS artifact set the schema projects;
    issue #21) alongside the walker ``revision`` and the build timestamps, so
    a consumer can tell exactly which CS2 build and platform a schema
    describes.  ``revision`` identifies the walker/hl2sdk pin — two different
    game builds read by the same pinned hl2sdk share a ``revision`` but not a
    ``build_id`` — so both keys are kept; they answer different questions.

    ``generator`` is echoed when present.  Keys come out in a stable,
    documented order (generator, build_id, platform, revision, dates).
    """
    hdr: dict[str, Any] = {}
    if not source_info:
        return hdr
    if source_info.get("generator"):
        hdr["generator"] = source_info["generator"]
    if source_info.get("build_id") not in (None, ""):
        hdr["build_id"] = _coerce_build_id(source_info["build_id"])
    if source_info.get("platform"):
        hdr["platform"] = source_info["platform"]
    for k in ("revision", "version_date", "version_time"):
        if source_info.get(k) not in (None, ""):
            hdr[k] = source_info[k]
    return hdr


def generate_gameevents_schema(
    gameevents: list[dict[str, Any]],
    overlays: dict[str, dict],
    out_dir: Path,
    source_info: dict[str, Any] | None = None,
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

    out: dict[str, Any] = {"schema_format_version": SCHEMA_FORMAT_VERSION}
    out.update(_schema_header(source_info))
    out["events"] = events_out
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
    diagram_modules: set[str] | None = None,
) -> Path:
    """Generate ``cs2_schema.json`` — the entity schema in
    CS2OpenDev-SchemaTracker's native shape, enriched with overlays.

    Each record is SchemaTracker's own ``entity_schema.json`` class/enum
    object emitted verbatim (camelCase keys, string-encoded int64
    offsets/sizes, UPPERCASE type ``category`` values, the
    ``module``/``projectName`` split), with an optional additive
    ``annotations`` block on classes, fields, enums, and members carrying
    community-curated descriptions / notes / warnings from
    ``docs/overlays/``.  A class registered under more than one
    ``projectName`` emits one record per ``(projectName, name)``.  See
    ``AGENTS.md`` for the full per-key format reference.

    ``diagram_modules`` (issue #21.4) is the set of grouping modules that got
    a UML page; a class in one of them gets an optional ``diagram_url`` back-
    reference to that page so a consumer can close the loop from a type to its
    inheritance diagram.
    """
    diagram_modules = diagram_modules or set()
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
            module = variant.get("module", "")
            key = (module, variant["name"])
            if key in seen:
                continue
            seen.add(key)
            raw = variant.get("raw")
            if raw is None:
                continue  # synthetic / unsourced entity — skip
            record = _enrich_record(raw, variant, overlays)
            # Cross-link the UML diagram for classes whose module has one.
            if variant["kind"] != "enum" and module in diagram_modules:
                record["diagram_url"] = f"{SITE_BASE}/schemas/{module}/hierarchy/"
            (enums_out if variant["kind"] == "enum" else classes_out).append(record)

    out: dict[str, Any] = {"schema_format_version": SCHEMA_FORMAT_VERSION}
    # Provenance header: build_id (numeric CS2 game build) + platform +
    # walker revision + dates, so the file stays a self-describing, drop-in
    # peer of cs2.json.gz.  See _schema_header (issues #19 / #21).
    out.update(_schema_header(source_info))
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
    """Emit ``convars_schema.json``, the structured projection of
    SchemaTracker's ``convars.json``.

    Each entry carries ``name``, ``default``, ``flags``, ``description``,
    ``value_type`` (when the artifact records one) and numeric ``min`` /
    ``max`` (null on an unbounded side).  This is the codegen-friendly
    counterpart to the ConVars page; downstream consumers wanting
    strongly-typed convar constants no longer need to parse Markdown.  No
    overlay annotation pipeline is wired up yet.
    """
    schema_dir = out_dir / "downstream-codegen-schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)

    out: dict[str, Any] = {"schema_format_version": SCHEMA_FORMAT_VERSION}
    out.update(_schema_header(source_info))
    # value_type / min / max are additive (schema_format_version 2.2): the
    # loader has carried them since the SchemaTracker switch and only the
    # emitters dropped them.
    records: list[dict[str, Any]] = []
    for cv in convars:
        rec: dict[str, Any] = {
            "name": cv["name"],
            "default": cv.get("default", ""),
            "flags": list(cv.get("flags", []) or []),
            "description": cv.get("description", ""),
        }
        if cv.get("value_type"):
            rec["value_type"] = cv["value_type"]
        rec["min"] = _bound_number(cv.get("min_value")) if cv.get("has_min") else None
        rec["max"] = _bound_number(cv.get("max_value")) if cv.get("has_max") else None
        records.append(rec)
    out["convars"] = records
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
    out.update(_schema_header(source_info))
    out["commands"] = [
        {
            "name": cmd["name"],
            "flags": list(cmd.get("flags", []) or []),
            "description": cmd.get("description", ""),
            "has_completion_callback": bool(cmd.get("has_completion_callback", False)),
        }
        for cmd in commands
    ]
    (schema_dir / "commands_schema.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


_PROTO_SYNTAX_RE = re.compile(r'^\s*syntax\s*=\s*"[^"]*"\s*;\s*$')
_PROTO_IMPORT_RE = re.compile(r'^\s*import\s+(?:public\s+|weak\s+)?"([^"]+)"\s*;')


def _normalise_proto_text(text: str, present: set[str]) -> tuple[str, list[str]]:
    """Return ``(normalised text, dropped import targets)`` — *text* with
    ``option csharp_namespace`` injected and any unresolvable ``import``
    stripped (issue #21.3).

    SchemaTracker's decompiled ``.proto`` files carry no ``option
    csharp_namespace``, so C# codegen emits every message into the global
    namespace — a CS0433 collision hazard the moment a consumer references two
    protobuf assemblies.  We insert a single shared namespace right after the
    ``syntax`` line.

    We deliberately do **not** add a ``package`` statement: these files use
    hundreds of root-qualified (``.Type``) cross-references that assume the
    empty package, and packaging them would break that resolution without a
    fragile rewrite of every reference.  ``csharp_namespace`` alone fixes the
    C# problem the issue describes; the proto type graph is left untouched.

    ``present`` is the set of proto paths shipped in this overlay directory
    (relative, forward-slashed, incl. the ``google/`` well-knowns).  Any
    ``import`` naming a file outside that set is dropped: it is a dangling
    import inherited from the decompile (the only one in the CS2 set is
    ``cs_prediction_events.proto``'s unused ``prediction_events.proto``), and
    leaving it in makes the file fail ``protoc`` with *File not found* before
    any real error is reachable.
    """
    dropped: list[str] = []
    out_lines: list[str] = []
    for line in text.splitlines(keepends=True):
        m = _PROTO_IMPORT_RE.match(line)
        if m and m.group(1) not in present:
            dropped.append(m.group(1))
            out_lines.append(
                f'// Removed by CS2OpenDev-Docs (issue #21.3): unresolved import '
                f'"{m.group(1)}" (not shipped in this set).\n'
            )
            continue
        out_lines.append(line)
    text = "".join(out_lines)

    if "csharp_namespace" in text:
        return text, dropped  # already normalised upstream — leave it alone
    inject = (
        "\n// Injected by CS2OpenDev-Docs (issue #21.3): a single shared C# "
        "namespace\n// so message types don't land in the global namespace "
        "(CS0433 hazard).\n"
        f'option csharp_namespace = "{PROTO_CSHARP_NAMESPACE}";\n'
    )
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if _PROTO_SYNTAX_RE.match(line):
            lines.insert(i + 1, inject)
            return "".join(lines), dropped
    # No syntax line (proto2 default) — prepend the option at the top.
    return inject.lstrip("\n") + text, dropped


def _scan_proto_symbols(text: str) -> tuple[set[str], set[str]]:
    """Return ``(top-level message names, global enum-value names)`` for one
    ``.proto`` source, tracking brace depth so nested definitions are excluded.

    protobuf uses C++ scoping: a top-level ``message`` name and the values of a
    *top-level* ``enum`` are global identifiers.  A name that appears at global
    scope in two files is a hard ``protoc`` redefinition error — that is what we
    surface (issue #21.3 follow-up), rather than assume the directory compiles
    as a unit.  Comments and nested scopes are stripped/skipped first.
    """
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//[^\n]*", "", text)
    messages: set[str] = set()
    enum_values: set[str] = set()
    depth = 0
    enum_open_depths: list[int] = []  # brace depth at which each open enum began
    for tok in re.findall(r"message\s+\w+|enum\s+\w+|[{}]|\w+\s*=\s*-?\d+", text):
        if tok == "{":
            depth += 1
        elif tok == "}":
            depth -= 1
            if enum_open_depths and depth < enum_open_depths[-1]:
                enum_open_depths.pop()
        elif tok.startswith("message"):
            if depth == 0:
                messages.add(tok.split()[1])
        elif tok.startswith("enum"):
            enum_open_depths.append(depth + 1)
        else:  # NAME = number
            if enum_open_depths and enum_open_depths[-1] == 1 and depth == 1:
                enum_values.add(tok.split("=")[0].strip())
    return messages, enum_values


def generate_proto_overlays(build_dir: Path, out_dir: Path) -> dict[str, Any]:
    """Copy the build's ``.proto`` text into
    ``downstream-codegen-schemas/proto/``, normalised with a shared
    ``option csharp_namespace`` (issue #21.3).

    For most consumers SchemaTracker's prebuilt ``protos.descriptorset`` is the
    better path (``protoc --descriptor_set_in`` skips text parsing and import
    resolution).  These normalised text files are for consumers compiling the
    protos from source, who would otherwise re-inject the namespace themselves.

    The whole tree is copied verbatim in structure — including the vendored
    ``google/protobuf/*`` well-knowns — so imports resolve without relying on a
    toolchain's bundled include path.  ``import``s of files absent from the set
    are dropped (see :func:`_normalise_proto_text`).  Because the decompiled
    protos share the empty package, some global symbols are defined in more than
    one file; those cross-file collisions are detected and returned so the
    README can name them (the directory is a per-file reference, not a set that
    ``protoc *.proto`` compiles as a unit).

    Returns ``{count, collisions, dropped_imports}`` for the README.
    """
    src_dir = build_dir / "protos"
    if not src_dir.is_dir():
        return {"count": 0, "collisions": {}, "dropped_imports": []}
    dst_dir = out_dir / "downstream-codegen-schemas" / "proto"
    if dst_dir.is_dir():
        shutil.rmtree(dst_dir)  # drop overlays for protos no longer in the build
    dst_dir.mkdir(parents=True, exist_ok=True)

    # Every .proto shipped in the build, as a relative forward-slashed path —
    # the resolvable-import universe (top-level files + google/ well-knowns).
    present: set[str] = {
        p.relative_to(src_dir).as_posix() for p in src_dir.rglob("*.proto")
    }

    written = 0
    msg_files: dict[str, list[str]] = {}
    eval_files: dict[str, list[str]] = {}
    dropped: list[str] = []
    for src in sorted(src_dir.rglob("*.proto")):
        rel = src.relative_to(src_dir).as_posix()
        try:
            text = src.read_text(encoding="utf-8")
        except OSError:
            continue
        dst = dst_dir / src.relative_to(src_dir)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if rel.startswith("google/"):
            # Vendored well-known types: copy verbatim, own package/namespace.
            dst.write_text(text, encoding="utf-8")
        else:
            norm, dropped_here = _normalise_proto_text(text, present)
            for d in dropped_here:
                dropped.append(f"{rel}: {d}")
            dst.write_text(norm, encoding="utf-8")
            msgs, evals = _scan_proto_symbols(text)
            for x in msgs:
                msg_files.setdefault(x, []).append(rel)
            for x in evals:
                eval_files.setdefault(x, []).append(rel)
        written += 1

    collisions = {
        "messages": {k: sorted(v) for k, v in sorted(msg_files.items()) if len(v) > 1},
        "enum_values": {k: sorted(v) for k, v in sorted(eval_files.items()) if len(v) > 1},
    }
    return {"count": written, "collisions": collisions, "dropped_imports": sorted(dropped)}


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
    out.update(_schema_header(source_info))
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
    atomic_categories: set[str] = set()
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
            # schema_format_version 2.1: ATOMIC nodes carry the explicit
            # SchemaAtomicCategory discriminator (SchemaTracker >= 0.9.0).
            acat = t.get("atomicCategory")
            if isinstance(acat, str):
                atomic_categories.add(acat)
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
        "atomic_categories": sorted(atomic_categories),
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
    proto_info: dict[str, Any] | None = None,
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
    platform = ""
    build_id: Any = None
    if source_info:
        rev = source_info.get("revision")
        date = source_info.get("version_date")
        if rev and date:
            rev_line = f"\n_Last regenerated against CS2 build `{rev}` ({date})._\n"
        platform = source_info.get("platform", "") or ""
        if source_info.get("build_id") not in (None, ""):
            build_id = _coerce_build_id(source_info["build_id"])

    # Issue #21.1: state the platform these schemas project and how the
    # per-(build, platform) artifacts are collapsed into one record set, so a
    # consumer never has to derive it by set-comparison.
    platform_phrase = f"`{platform}`" if platform else "a single platform"
    build_phrase = f" (CS2 build `{build_id}`)" if build_id is not None else ""
    platform_block = f"""## Platform & provenance

Every file here projects **one** `(build, platform)` artifact set:
{platform_phrase}{build_phrase}.  The `build_id` (the Steam CS2 game build,
numeric and monotonic) and `platform` are stamped into each schema's header
alongside the walker `revision` and the build timestamps — read them there
rather than assuming.

Windows is the canonical render because it is the superset: it carries the
tool-side modules (`hammer`, `sfm`, `modeldoc_editor`, …) that have no Linux
binaries.  A consumer that assumes Linux would get a silently wrong answer
about which classes exist, so the platform is named explicitly in every
header.  If both platforms are ever published, select by the header's
`platform` field.

## How duplicate class registrations are collapsed

`cs2_schema.json` emits **one record per `(projectName, name)`**, not one per
upstream `(binary-module, name)`.  `projectName` is SchemaTracker's
coarse-grained project axis (`client`, `server`, `entity2`,
`pulse_runtime_lib`, `particleslib`, `animgraphlib`); the finer `module` /
`cppName` from upstream are preserved verbatim on each record.

- A class registered in several binaries that all roll up to the **same**
  `projectName` collapses to a single record.  This dominates the
  `pulse_runtime_lib` cell classes (e.g. `CBasePulseGraphInstance`), which are
  statically linked into many tool binaries but describe one type.
- A name that legitimately appears under **different** `projectName`s — the
  cross-project case such as `CCSPlayerController` in both `client` and
  `server` — keeps one record per project.  So a name appearing more than once
  is expected, and the discriminator is the record's `projectName`.
"""

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
                "ATOMIC `type.atomicCategory` values (schema_format_version 2.1+)",
                vocab["atomic_categories"],
            ),
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

    # Issue #21.3 follow-up: the proto/ directory is a per-file reference, not a
    # set that compiles as a unit.  Name the cross-file symbol collisions (they
    # stem from the decompiled empty-package protos) and any dropped dangling
    # imports so a consumer knows to pick a subset rather than run `protoc *`.
    proto_block = ""
    if proto_info and proto_info.get("count"):
        cols = proto_info.get("collisions", {}) or {}
        lines = [
            "",
            "## `proto/` — a per-file reference, not a compilable set",
            "",
            "The `.proto/` directory mirrors SchemaTracker's decompiled protobuf",
            "sources (the vendored `google/protobuf/*` well-knowns are included so",
            "imports resolve).  Because the decompiled files share the **empty**",
            "package, a few global symbols are defined in more than one file, so",
            "`protoc *.proto` over the whole directory fails on a redefinition.",
            "Each collision below is between exactly **two** files; compile any",
            "subset that does not include both files of a listed pair and it",
            "resolves cleanly (the demo/engine closure used by CS2 demo parsers",
            "is one such subset).",
            "",
        ]
        msg = cols.get("messages", {})
        ev = cols.get("enum_values", {})
        if msg or ev:
            lines.append("**Cross-file symbol collisions** (same global identifier "
                         "defined in two files — a `protoc` redefinition error):")
            lines.append("")
            for name, files in msg.items():
                lines.append(f"- message `{name}` — {', '.join(f'`{f}`' for f in files)}")
            for name, files in ev.items():
                lines.append(f"- enum value `{name}` — {', '.join(f'`{f}`' for f in files)}")
            lines.append("")
        dropped = proto_info.get("dropped_imports", []) or []
        if dropped:
            lines.append("**Dropped unresolved imports** (dangling in the decompile; "
                         "each is marked with a comment in the file):")
            lines.append("")
            for d in dropped:
                lines.append(f"- `{d}`")
            lines.append("")
        proto_block = "\n".join(lines)

    body = f"""# Downstream codegen schemas

Machine-readable schemas for CS2 entity classes, structs, enums, and game
events — projected straight from
[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)'s
per-build artifacts so consumers get one deterministic, provenance-tracked
source instead of a chain of third-party dumps.

{platform_block}
## Files

- **`cs2_schema.json`** — the entity schema in SchemaTracker's **native**
  shape (`schema_format_version` `{SCHEMA_FORMAT_VERSION}`).  Top-level: `generator`, `build_id`,
  `platform`, `revision`, `version_date`, `version_time`, `classes`, `enums`.
  Each class carries `name`, `module` (the binary it lives in), `projectName`,
  `cppName`, `size`, `alignment`, `flags` / `flags2`, `parents[]`, `fields[]`
  (`name`, `offset`, `type`, `typeModule`, `metadata`), and inheritance
  depths; each enum carries `alignment` (underlying integer type) and
  `members[]`.  Integer offsets / sizes are **string-encoded** and type
  `category` values are **UPPERCASE** (`BUILTIN`, `ATOMIC`, `DECLARED_CLASS`,
  `PTR`, `FIXED_ARRAY`, `BITFIELD`, …).  As of `2.1` (SchemaTracker 0.9.0
  walkers, the v1.3.0 corpus), ATOMIC type nodes also carry
  `atomicCategory` — the explicit `SchemaAtomicCategory` discriminator
  (`ATOMIC_PLAIN` / `ATOMIC_T` / `ATOMIC_COLLECTION_OF_T` / `ATOMIC_TT` /
  `ATOMIC_I`) that previously had to be inferred from which `inner` keys
  were present — and `ATOMIC_COLLECTION_OF_T` nodes populate `count` with
  the fixed-buffer capacity `N` of the `CUtlVectorFixedGrowable< T, N >`
  family, read from the binary's own record (never parsed from the type
  name).  A non-zero `count` on an ATOMIC node therefore no longer implies
  `ATOMIC_I` — switch on `atomicCategory` instead
  ([SchemaTracker#8](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker/issues/8)).
  Optional `annotations` blocks layer
  in community-curated descriptions / notes / warnings, and an optional
  `diagram_url` on a class points at its module's UML inheritance diagram.
  Records are keyed by `(projectName, name)` — see [How duplicate class
  registrations are collapsed](#how-duplicate-class-registrations-are-collapsed)
  below.

- **`gameevents_schema.json`** — the game-event registry.  Top-level:
  `events` list; each record has `name` / `comment` / `source` /
  `properties` / `fields`.  Same `annotations` enrichment pattern.

- **`convars_schema.json`** — the console-variable table.  Top-level:
  `convars` list; each entry has `name` / `default` / `flags` /
  `description` / `value_type` (upstream's declared type, e.g. `Float32`,
  `Int32`, `Bool`, `String`; omitted when the artifact records none) /
  `min` / `max` (JSON numbers: an integer when the bound is integral, else
  a float; `null` on a side upstream leaves unbounded).  Codegen-friendly
  counterpart to the ConVars page.

- **`commands_schema.json`** — the console-command table.  Top-level:
  `commands` list; each entry has `name` / `flags` / `description` /
  `has_completion_callback` (boolean: the command registers an argument
  autocomplete callback).

- **`well_known_constants.json`** — community-curated reference tables
  for integer / enum values downstream tooling needs but that the schema
  doesn't expose as named enum types (team numbers, `m_gamePhase`,
  `CSWeaponState_t`, …).  Top-level: `constants` list; each entry has
  `name` / `comment` / `members[]` with the same `annotations` pattern.

- **`proto/*.proto`** — the build's protobuf definitions as text, copied from
  SchemaTracker (including the vendored `google/protobuf/*` well-knowns) and
  normalised with a single shared
  `option csharp_namespace = "{PROTO_CSHARP_NAMESPACE}";` so C# codegen doesn't
  drop every message into the global namespace (a CS0433 collision hazard).
  Unresolvable (dangling) imports are dropped.  No `package` statement is
  added — the decompiled protos use hundreds of root-qualified (`.Type`)
  cross-references that assume the empty package, so packaging them would break
  resolution.  This is a **per-file reference, not a set that compiles as a
  unit** — see [below](#proto--a-per-file-reference-not-a-compilable-set).
  Most consumers should prefer SchemaTracker's prebuilt `protos.descriptorset`
  (`protoc --descriptor_set_in`, which skips text parsing and import
  resolution entirely); these files are for compiling the protos from source.

- **`field_history.json`** — whole-history evolution of every
  `(class, field)`, projected from SchemaTracker's cumulative
  `schema_evolution.json` (Layer A).  Top-level: `baseline_build`,
  `latest_build`, `transition_count`, `fields` list (each `class` /
  `field` / `firstSeenBuild` / `lastSeenBuild` / `typeHistory`, plus an
  overlay-supplied `confirmedRename` where the community has verified one),
  and `enums`.  **`[firstSeenBuild, lastSeenBuild]` is a presence *hull*,
  not continuous presence**: a field can be absent for intermediate builds
  with no trace in this file (e.g. the 775 classes that vanished at
  `22876476 → 22877907` and returned one build later).  Reconstruct exact
  presence from `schema_evolution.json`'s per-transition add/remove ops.
  The evolution artifact's neutral rename/move *evidence surfaces*
  (`pairedEvidence` plus the unselected `pairCandidates` /
  `classPairCandidates` / `fieldMoveCandidates` lists) are **not**
  projected into this file — read them from the artifact itself; the
  [Schema History](../schema-history.md) page documents them and serves
  as the human-readable break radar.  Serves alias resolution /
  forward-back schema migration for demo parsers and SDKs.

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
{proto_block}
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
    """Generate the site home page, index.md."""
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
    lines.append(_md_front_matter(title="CS2 Developer Reference"))
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
        title="Entity Hierarchy",
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
    """A one-line provenance blockquote for the top of a generated page."""
    build = source_info.get("build_id", "?")
    date = source_info.get("version_date", "")
    plat = source_info.get("platform", "")
    sv = source_info.get("schema_version", "")
    bits = [f"**Build {build}**"]
    if date:
        bits.append(date)
    if plat:
        bits.append(f"`{plat}`")
    if sv:
        bits.append(f"schema `{sv}`")
    return f"> Source: {' · '.join(bits)}\n"


def generate_items_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Economy items, prefabs, paint/sticker/music kits, rarities, qualities."""
    lines = [_md_front_matter(title="Items & Economy")]
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
    lines.append("## Items\n")
    lines.append(f"{len(items)} item definitions.\n")
    lines.append("| defIndex | Name token | Classname | Prefab | Item type |")
    lines.append("|----------|------------|-----------|--------|-----------|")
    for it in items:
        lines.append(
            f"| {it.get('defIndex','')} | {_code(it.get('nameToken'))} "
            f"| {_code(it.get('classname'))} | {_code(it.get('prefab'))} "
            f"| {_md_cell(it.get('itemTypeName'))} |"
        )
    lines.append("")

    paint = data.get("paintKits", [])
    lines.append("## Paint Kits — skins\n")
    lines.append(f"{len(paint)} paint kits.\n")
    lines.append("| defIndex | Name | Description tag |")
    lines.append("|----------|------|----------------|")
    for pk in paint:
        lines.append(
            f"| {pk.get('defIndex','')} | {_code(pk.get('name'))} "
            f"| {_code(pk.get('descriptionTag'))} |"
        )
    lines.append("")

    stickers = data.get("stickerKits", [])
    lines.append("## Sticker Kits\n")
    lines.append(f"{len(stickers)} sticker kits.\n")
    lines.append("| defIndex | Name | Item name token | Description |")
    lines.append("|----------|------|-----------------|-------------|")
    for sk in stickers:
        lines.append(
            f"| {sk.get('defIndex','')} | {_code(sk.get('name'))} "
            f"| {_code(sk.get('itemName'))} | {_code(sk.get('descriptionString'))} |"
        )
    lines.append("")

    music = data.get("musicDefinitions", [])
    lines.append("## Music Kits\n")
    lines.append(f"{len(music)} music kits.\n")
    lines.append("| defIndex | Name | Loc name |")
    lines.append("|----------|------|----------|")
    for m in music:
        lines.append(
            f"| {m.get('defIndex','')} | {_code(m.get('name'))} "
            f"| {_code(m.get('locName'))} |"
        )
    lines.append("")

    prefabs = data.get("prefabs", [])
    lines.append("## Prefabs\n")
    lines.append(f"{len(prefabs)} prefabs.\n")
    lines.append("| id | Parent prefab | Classname | Item type |")
    lines.append("|----|---------------|-----------|-----------|")
    for pf in prefabs:
        lines.append(
            f"| {_code(pf.get('id'))} | {_code(pf.get('prefab'))} "
            f"| {_code(pf.get('classname'))} | {_md_cell(pf.get('itemTypeName'))} |"
        )
    lines.append("")

    rarities = data.get("rarities", [])
    qualities = data.get("qualities", [])
    lines.append("## Rarities\n")
    lines.append(f"{len(rarities)} rarities.\n")
    lines.append("| id | Value | Loc key | Weapon loc key |")
    lines.append("|----|-------|---------|----------------|")
    for r in rarities:
        lines.append(
            f"| {_code(r.get('id'))} | {r.get('value','')} "
            f"| {_code(r.get('locKey'))} | {_code(r.get('locKeyWeapon'))} |"
        )
    lines.append("")
    lines.append("## Qualities\n")
    lines.append(f"{len(qualities)} qualities.\n")
    lines.append("| id | Value |")
    lines.append("|----|-------|")
    for q in qualities:
        lines.append(f"| {_code(q.get('id'))} | {q.get('value','')} |")
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
    # name -> (page stem, qualified name).  The qualified name is what the
    # proto page uses for its heading, so the anchor computed here matches.
    msg_to_file: dict[str, tuple[str, str]] = {}

    def _index_messages(msgs: list[dict], filename: str, prefix: str = "") -> None:
        for m in msgs:
            qualified = f"{prefix}{m['name']}"
            msg_to_file[m["name"]] = (filename, qualified)
            _index_messages(m.get("nested", []), filename, f"{qualified}.")

    for p in protos:
        stem = Path(p["filename"]).stem
        _index_messages(p.get("messages", []), stem)

    def _link(type_name: str) -> str:
        entry = msg_to_file.get(type_name)
        if entry:
            stem, qualified = entry
            return f"[`{type_name}`](proto/{stem}.md#{_proto_anchor(qualified)})"
        return _code(type_name)

    lines = [_md_front_matter(title="Network Messages")]
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
            lines.append(f"## {ch.get('name','')}\n")
            lines.append(f"{len(msgs)} message ids.\n")
            lines.append("| ID | Message type |")
            lines.append("|----|--------------|")
            for m in msgs:
                lines.append(f"| {m.get('id','')} | {_link(m.get('protoMessageType',''))} |")
            lines.append("")

    if demomsgs:
        msgs = demomsgs.get("messages", [])
        lines.append("## Demo stream messages\n")
        lines.append(f"{len(msgs)} command ids in the `.dem` stream.\n")
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
    lines = [_md_front_matter(title="Game Modes")]
    lines.append("# Game Modes & Map Groups\n")
    lines.append(_provenance_block(source_info))
    lines.append(
        "Game types and their nested game modes (from `gamemodes.txt`): max "
        "players, map groups, and per-mode convar overrides.\n"
    )

    for gt in data.get("gameTypes", []):
        modes = gt.get("gameModes", [])
        lines.append(f"## Game type: `{gt.get('id','')}`\n")
        lines.append(f"{len(modes)} modes.\n")
        for gm in modes:
            lines.append(f"### `{gm.get('id','')}`\n")
            lines.append(f"- **Name token:** {_code(gm.get('nameId'))}")
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
                    lines.append(f"| {_code(cv.get('name'))} | {_code(cv.get('value'))} |")
            lines.append("")

    groups = data.get("mapGroups", [])
    lines.append("## Map groups\n")
    lines.append(f"{len(groups)} map groups.\n")
    lines.append("| id | Maps |")
    lines.append("|----|------|")
    for g in groups:
        maps = ", ".join(f"`{m}`" for m in g.get("maps", []))
        lines.append(f"| {_code(g.get('id'))} | {maps} |")
    lines.append("")

    (out_dir / "gamemodes.md").write_text("\n".join(lines), encoding="utf-8")


def generate_changelog_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """What changed between the previous committed build and this one."""
    lines = [_md_front_matter(title="Changelog")]
    lines.append("# Build Changelog\n")
    lines.append(_provenance_block(source_info))
    lines.append(
        f"Difference between build **{data.get('fromBuild','?')}** and "
        f"**{data.get('toBuild','?')}** (`{data.get('platform','')}`), grouped by "
        "data family.\n"
    )

    families = data.get("families", []) or []
    fam_names = [str(f.get("family", "")) for f in families if f.get("family")]
    if fam_names:
        lines.append(
            "Families diffed: " + ", ".join(f"`{n}`" for n in fam_names) + ".\n"
        )
    if not any(
        f.get("added") or f.get("removed") or f.get("changed") for f in families
    ):
        listed = ", ".join(fam_names) if fam_names else "any diffed family"
        lines.append(
            f"No changes in {listed} between build "
            f"{data.get('fromBuild','?')} and {data.get('toBuild','?')}. "
            "Field-level history for every build is on the "
            "[Schema History](schema-history.md#transitions-with-structural-changes) "
            "page.\n"
        )

    for fam in families:
        added, removed, changed = fam.get("added", []), fam.get("removed", []), fam.get("changed", [])
        if not (added or removed or changed):
            continue
        lines.append(
            f"## {fam.get('family','')} "
            f"(+{len(added)} / −{len(removed)} / ~{len(changed)})\n"
        )
        if added:
            lines.append("**Added:** " + ", ".join(f"{_code(a)}" for a in added[:200]))
            if len(added) > 200:
                lines.append(f"… and {len(added) - 200} more")
            lines.append("")
        if removed:
            lines.append("**Removed:** " + ", ".join(f"{_code(r)}" for r in removed[:200]))
            if len(removed) > 200:
                lines.append(f"… and {len(removed) - 200} more")
            lines.append("")
        if changed:
            lines.append("| Entry | Field changes |")
            lines.append("|-------|---------------|")
            for ch in changed[:400]:
                deltas = "; ".join(
                    f"{_md_cell(fc.get('field'))}: {_code(fc.get('oldValue'))} → "
                    f"{_code(fc.get('newValue'))}"
                    for fc in ch.get("fields", [])
                )
                lines.append(f"| {_code(ch.get('name'))} | {deltas} |")
            if len(changed) > 400:
                lines.append(f"\n… and {len(changed) - 400} more changed entries")
            lines.append("")

    (out_dir / "changelog.md").write_text("\n".join(lines), encoding="utf-8")


def generate_maps_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Per-map radar/overview metadata + maps inventory."""
    lines = [_md_front_matter(title="Maps")]
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
            f"| {_code(m.get('name'))} | {_code(m.get('material'))} "
            f"| {m.get('posX','')}, {m.get('posY','')} | {m.get('scale','')} "
            f"| {m.get('ctSpawnX','')}, {m.get('ctSpawnY','')} "
            f"| {m.get('tSpawnX','')}, {m.get('tSpawnY','')} |"
        )
    lines.append("")
    (out_dir / "maps.md").write_text("\n".join(lines), encoding="utf-8")


def generate_surfaces_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Per-material surface physics / footstep table."""
    lines = [_md_front_matter(title="Surface Properties")]
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
            f"{_md_cell(p.get('name'))}={_code(p.get('value'))}"
            for p in s.get("properties", [])
        )
        lines.append(
            f"| {_code(s.get('name'))} | {_md_cell(s.get('scope'))} "
            f"| {_code(s.get('sourceFile'))} | {props} |"
        )
    lines.append("")
    (out_dir / "surfaces.md").write_text("\n".join(lines), encoding="utf-8")


def generate_props_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Breakable-prop physics classes, gib groups, collision-group registry."""
    lines = [_md_front_matter(title="Prop Data")]
    lines.append("# Prop & Collision Data\n")
    lines.append(_provenance_block(source_info))

    prop_classes = data.get("propClasses", [])
    lines.append("## Prop classes\n")
    lines.append(f"{len(prop_classes)} prop classes.\n")
    lines.append("| Class | Properties |")
    lines.append("|-------|------------|")
    for pc in prop_classes:
        props = "; ".join(
            f"{_md_cell(p.get('name'))}={_code(p.get('value'))}"
            for p in pc.get("properties", [])
        )
        lines.append(f"| {_code(pc.get('id'))} | {props} |")
    lines.append("")

    groups = data.get("collisionGroups", [])
    lines.append("## Collision groups\n")
    lines.append(f"{len(groups)} collision groups.\n")
    lines.append("| Group | Description | Interacts as | Interacts with |")
    lines.append("|-------|-------------|--------------|----------------|")
    for g in groups:
        lines.append(
            f"| {_code(g.get('collisionGroup'))} | {_md_cell(g.get('description'))} "
            f"| {', '.join(f'`{x}`' for x in g.get('interactAs', []))} "
            f"| {', '.join(f'`{x}`' for x in g.get('interactWith', []))} |"
        )
    lines.append("")

    breakables = data.get("breakableModels", [])
    lines.append("## Breakable gib groups\n")
    lines.append(f"{len(breakables)} gib groups.\n")
    for b in breakables:
        lines.append(f"- **{_code(b.get('id'))}**: {len(b.get('models', []))} models")
    lines.append("")
    (out_dir / "props.md").write_text("\n".join(lines), encoding="utf-8")


def generate_modules_md(data: dict[str, Any], source_info: dict[str, Any], out_dir: Path) -> None:
    """Per-binary inventory: hashes, sizes, and resolved interface versions."""
    lines = [_md_front_matter(title="Modules")]
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
            f"| {_code(m.get('path'))} | {m.get('fileSize','')} "
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

    lines = [_md_front_matter(title="Schema History")]
    lines.append("# Schema History\n")
    lines.append(_provenance_block(source_info))

    if lens_overlay.get("description"):
        lines.append(str(lens_overlay["description"]).strip() + "\n")
    else:
        lines.append(
            "Field-precise, build-to-build evolution of the CS2 C++ entity schema, "
            "derived by diffing every committed `entity_schema.json` snapshot "
            "(SchemaTracker's cumulative `schema_evolution.json`, Layer A).  Unlike "
            "the coarse [Changelog](changelog.md) — which only reports *that* a "
            "class changed — this reports *which field* was added, removed, retyped, "
            "or moved.\n"
        )
    if lens_overlay.get("notes"):
        lines.append("> " + str(lens_overlay["notes"]).strip().replace("\n", "\n> ") + "\n")

    schema_version = evolution.get("schemaVersion", "")
    version_bullet = (
        f"- **Artifact schema version:** `{schema_version}` "
        "(SchemaTracker's `schemas/schema_evolution.proto` family)\n"
        if schema_version
        else ""
    )
    lines.append(
        f"- **Platform:** `{platform}` (the canonical render; windows is a "
        "strict **superset** in class coverage — historical Windows-only tool "
        "binaries such as `hammer.dll` / `sfm.dll` have no Linux counterparts "
        "— while shared classes differ in offsets/sizes per platform)\n"
        f"- **Baseline build:** `{baseline}` · **Latest build:** `{latest}`\n"
        f"{version_bullet}"
        f"- **Transitions:** {len(transitions)} total, **{len(non_empty)} with "
        f"structural changes** ({len(transitions) - len(non_empty)} no-op builds)\n"
        f"- **Full per-field history:** the portable "
        "[`field_history.json`](downstream-codegen-schemas/field_history.json) "
        "carries first/last-seen and the type history for every "
        "`(class, field)` across all builds.  Its "
        "`[firstSeenBuild, lastSeenBuild]` interval is a presence **hull**, "
        "not continuous presence — a field can be absent for intermediate "
        "builds with no trace there; exact presence replays from the "
        "transitions below.\n"
    )
    lines.append(
        "To bring an instance captured under build *X* forward to build *Y*, apply "
        "each transition in `[X, Y)` in order.  Every op carries both endpoints, so "
        "the same chain replays backward.\n"
    )

    # --- evidence-surface reference (schema_evolution 0.6.0–0.8.0) ---
    lines.append("## Evidence surfaces\n")
    lines.append(
        "The artifact is **facts-only**: it never asserts a rename, a move, or "
        "a safety verdict.  Alongside the raw add/remove ops it emits neutral "
        "*evidence* lists, each signal independently provable from the two "
        "snapshots being diffed.  Promotion to a confirmed rename happens "
        "downstream, in [`docs/overlays/schema-lens.yml`]"
        "(https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/docs/overlays/schema-lens.yml).\n"
    )
    lines.append("| Surface | Scope | Signals | Since |")
    lines.append("|---------|-------|---------|-------|")
    lines.append(
        "| `classChanged[].pairedEvidence` | removed+added field pairs within "
        "one class, greedy 1:1, pre-filtered to same offset **and** same "
        "rendered type | always exactly `offsetExact`, `typeMatch` | frozen "
        "(pre-0.6.0) |"
    )
    lines.append(
        "| `classChanged[].pairCandidates` | **every** removed/added field "
        "pair within one class whose rendered types are equal **or** whose "
        "offsets are equal — N:M, deliberately unselected | `typeMatch`, "
        "`offsetExact`, `sizeMatch` (never alone) | 0.6.0 |"
    )
    lines.append(
        "| `classPairCandidates` | removed/added **class** pairs sharing a "
        "bare (module-stripped) name — the cross-module move the qualified "
        "key cannot see | `bareNameMatch` (floor), `sizeMatch`, "
        "`fieldSetMatch` | 0.6.0 |"
    )
    lines.append(
        "| `fieldMoveCandidates` | a same-named, same-typed field removed "
        "from one **surviving** class and added to another (hoist / "
        "push-down / sideways move) | `fieldNameMatch` + `typeMatch` "
        "(floor), `parentChainUp`, `parentChainDown` | 0.6.0 |"
    )
    lines.append("")
    lines.append(
        "The candidate lists are **complete on their own** — every "
        "`pairedEvidence` pair reappears in `pairCandidates`, so consumers "
        "never need to union the two surfaces.  A 1:1 pick among tied "
        "candidates would be an inference, which is why the wider surfaces "
        "stay unselected; `offsetAdjacent` is never emitted (any adjacency "
        "threshold is consumer policy, not a fact).  `pairedEvidence` itself "
        "is frozen for compatibility.\n"
    )
    lines.append(
        "Later artifact revisions add further facts: **0.7.0** covers "
        "class-attribute changes (`staticFieldOps`, `cppName`, `projectName`, "
        "inheritance depths, `flags2`) and a calendar axis — each transition "
        "carries `fromManifestCreatedUtc` / `toManifestCreatedUtc`, verbatim "
        "from the two builds' Steam provenance records; **0.8.0** adds "
        "structured per-key metadata ops (`metaOps` on classes, fields, and "
        "enum members; values over 256 UTF-8 bytes are carried as a SHA-256 "
        "hash + byte count instead of inline).\n"
    )

    # --- whole-history summary table (non-empty only, most-recent first) ---
    # The Date column is the successor build's Steam manifest-creation date
    # (schema_evolution 0.7.0's calendar axis); blank on pre-0.7.0 artifacts.
    lines.append("## Transitions with structural changes\n")
    lines.append("| Transition | Date | Classes +/−/~ | Enums +/−/~ | Field ops |")
    lines.append("|------------|------|---------------|-------------|-----------|")
    for tr, c in reversed(non_empty):
        date = (tr.get("toManifestCreatedUtc", "") or "")[:10] or "—"
        lines.append(
            f"| {_code(tr.get('fromBuild',''))} → {_code(tr.get('toBuild',''))} "
            f"| {_md_cell(date)} "
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
        f_ts = tr.get("fromManifestCreatedUtc", "")
        t_ts = tr.get("toManifestCreatedUtc", "")
        if f_ts or t_ts:
            lines.append(f"*Steam manifests created `{f_ts or '?'}` → `{t_ts or '?'}`*\n")
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

        cpc = tr.get("classPairCandidates", [])
        fmc = tr.get("fieldMoveCandidates", [])
        if cpc or fmc:
            lines.append(
                f"**Unselected candidates:** {len(cpc)} class-pair, "
                f"{len(fmc)} field-move — neutral evidence only, see "
                "[Evidence surfaces](#evidence-surfaces).\n"
            )

        changed = tr.get("classChanged", [])
        if changed:
            lines.append(f"**Classes changed ({len(changed)}):**\n")
            lines.append("| Class | Field ops | Layout |")
            lines.append("|-------|-----------|--------|")
            for cd in changed[:_HISTORY_DETAIL_CLASS_CAP]:
                kinds: dict[str, int] = {}
                for op in cd.get("fieldOps", []):
                    kinds[op.get("kind", "")] = kinds.get(op.get("kind", ""), 0) + 1
                op_parts = [
                    f"{_FIELDOP_LABEL.get(k, k)}×{n}" for k, n in sorted(kinds.items())
                ]
                if cd.get("staticFieldOps"):
                    op_parts.append(f"static×{len(cd['staticFieldOps'])}")
                if cd.get("metaOps"):
                    op_parts.append(f"meta×{len(cd['metaOps'])}")
                if cd.get("pairedEvidence"):
                    op_parts.append(f"paired×{len(cd['pairedEvidence'])}")
                if cd.get("pairCandidates"):
                    op_parts.append(f"cand×{len(cd['pairCandidates'])}")
                ops_txt = ", ".join(op_parts) or "—"
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
                    f"| {_code(cls_name)} | {_md_cell(ops_txt)} "
                    f"| {_md_cell(', '.join(layout)) or '—'} |"
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
    plus overlay-confirmed renames folded into an authoritative
    ``confirmedRename`` block on the affected records (the two-tier
    field_history seam: SchemaTracker emits mechanical facts, Docs publishes
    the confirmed version).

    ``[firstSeenBuild, lastSeenBuild]`` is a presence *hull*, not a guarantee
    of continuous presence — a field can be absent for intermediate builds
    (e.g. the 775-class blip at ``22876476 -> 22880072``) with no trace here.
    Exact presence replays from ``schema_evolution.json``'s transitions.
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
# Overlay validation
# ---------------------------------------------------------------------------

# Overlay files whose top-level shape is not a map of entity names.
_NON_ENTITY_OVERLAYS = {"convar_flags", "gameevents", "schema-lens", "well_known_constants"}


def _nearest(name: str, pool: Any) -> str:
    """`(did you mean X?)` for an overlay key that resolved to nothing."""
    import difflib

    hits = difflib.get_close_matches(name, list(pool), n=1, cutoff=0.6)
    return f" (nearest: {hits[0]})" if hits else ""


def check_overlay_keys(
    overlays: dict[str, dict],
    entities: dict[str, dict],
    protos: list[dict],
    gameevents: list[dict[str, Any]],
) -> tuple[list[str], list[str]]:
    """Report overlay keys that name something this build does not have.

    Returns ``(unresolved, module_mismatch)``.  Unresolved keys annotate
    nothing at all.  A module mismatch still renders, through the name-only
    fallback in :func:`get_overlay`, but the key is filed under a module the
    entity does not live in and would attach to an unrelated class of the same
    name if one ever appeared.
    """
    unresolved: list[str] = []
    mismatched: list[str] = []

    entity_names = set(entities)
    schema_modules = {
        v.get("module", "")
        for e in entities.values()
        for v in _all_variants(e["name"], entities)
    }
    # A file stem must be a schema module, a listed wrapper file or the
    # protobufs directory; anything else annotates nothing, whatever it names.
    known_stems = schema_modules | _NON_ENTITY_OVERLAYS | {"protobufs"}
    for stem in sorted({k.split("/", 1)[0] for k in overlays}):
        if stem not in known_stems:
            unresolved.append(
                f"{stem}: no such module or overlay file{_nearest(stem, known_stems)}"
            )

    def _member_names(name: str) -> set[str]:
        out: set[str] = set()
        for v in _all_variants(name, entities):
            out |= {f.get("name", "") for f in v.get("fields", [])}
        return out

    for key, data in sorted(overlays.items()):
        if "/" not in key or not isinstance(data, dict):
            continue
        module, name = key.split("/", 1)
        if module not in schema_modules:
            continue
        if name not in entity_names:
            unresolved.append(f"{key}: no such class or enum{_nearest(name, entity_names)}")
            continue
        modules = {v.get("module", "") for v in _all_variants(name, entities)}
        if module not in modules:
            mismatched.append(
                f"{key}: {name} lives in {', '.join(sorted(modules))}"
            )
        members = _member_names(name)
        fields = data.get("fields") or {}
        if isinstance(fields, dict):
            for fname in sorted(fields):
                if fname not in members:
                    unresolved.append(
                        f"{key}.{fname}: no such field{_nearest(fname, members)}"
                    )

    # --- proto overlays ---
    by_stem = {p["filename"].removesuffix(".proto"): p for p in protos}
    for key, data in sorted(overlays.items()):
        if not key.startswith("protobufs/") or not isinstance(data, dict):
            continue
        stem = key.split("/", 1)[1]
        proto = by_stem.get(stem)
        if proto is None:
            unresolved.append(
                f"{key}: no such proto file{_nearest(stem, by_stem)}"
            )
            continue
        names = _proto_name_index(proto)
        msgs = {q: m for q, m in _proto_flatten_messages(proto.get("messages", []))}
        overlay_msgs = data.get("messages") or {}
        if not isinstance(overlay_msgs, dict):
            continue
        for mname in sorted(overlay_msgs):
            qualified = names.get(mname)
            if qualified is None or qualified not in msgs:
                unresolved.append(
                    f"{key}.{mname}: no such message{_nearest(mname, msgs)}"
                )
                continue
            mover = overlay_msgs[mname]
            if not isinstance(mover, dict):
                continue
            have = {f["name"] for f in msgs[qualified].get("fields", [])}
            fields = mover.get("fields") or {}
            if isinstance(fields, dict):
                for fname in sorted(fields):
                    if fname not in have:
                        unresolved.append(
                            f"{key}.{mname}.{fname}: no such field"
                            f"{_nearest(fname, have)}"
                        )

    # --- game-event overlays ---
    ge_overlay = overlays.get("gameevents", {}) or {}
    ge_events = ge_overlay.get("events") or {}
    if isinstance(ge_events, dict):
        by_name: dict[str, set[str]] = {}
        for ev in gameevents:
            by_name.setdefault(ev["name"], set()).update(
                f["name"] for f in ev.get("fields", [])
            )
        for ename in sorted(ge_events):
            if ename not in by_name:
                unresolved.append(
                    f"gameevents/{ename}: no such event{_nearest(ename, by_name)}"
                )
                continue
            eov = ge_events[ename]
            if not isinstance(eov, dict):
                continue
            fields = eov.get("fields") or {}
            if isinstance(fields, dict):
                for fname in sorted(fields):
                    if fname not in by_name[ename]:
                        unresolved.append(
                            f"gameevents/{ename}.{fname}: no such field"
                            f"{_nearest(fname, by_name[ename])}"
                        )

    return unresolved, mismatched


# ---------------------------------------------------------------------------
# Output self-checks
# ---------------------------------------------------------------------------

_TABLE_SEPARATOR_RE = re.compile(r"^\|[\s\-:|]+\|\s*$")


def check_markdown_tables(root: Path) -> list[str]:
    """Return ``file:line`` for every table row that does not start with `|`.

    A newline inside a cell splits the row; GFM then rejects the whole
    block and re-parses the rest of the page as one paragraph, which is how
    convars.md and commands.md stopped rendering a table at all.
    """
    problems: list[str] = []
    for path in sorted(root.rglob("*.md")):
        in_fence = False
        in_pre = False
        in_table = False
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                in_table = False
                continue
            if in_fence:
                continue
            if "<pre>" in stripped:
                in_pre = True
            if "</pre>" in stripped:
                in_pre = False
                continue
            if in_pre:
                continue
            if in_table:
                if not stripped:
                    in_table = False
                elif not stripped.startswith("|"):
                    problems.append(f"{path}:{n}: {stripped[:80]}")
                    in_table = False
            elif _TABLE_SEPARATOR_RE.match(stripped):
                in_table = True
    return problems


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the CS2 reference: Markdown, codegen JSON and the site data bundle.")
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
    parser.add_argument("--output", default="docs", help="Output directory (home page goes here; everything else goes under <output>/generated/)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Fail the run when an overlay key names a class, field, message or "
            "event this build does not have, or is filed under the wrong module."
        ),
    )
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
    generate_schemas_index_md(
        entities, overlays, generated_dir, diagram_modules=uml_md,
        source_info=schema_source_info,
    )
    print(f"  Generated {len({e['module'] for e in entities.values()})} module index pages "
          f"covering {len(entities)} entities (one page each).")

    print("Checking inherited layouts resolve inside their own module…")
    layout_violations, layout_exempt = check_module_layout_consistency(entities)
    print(f"  {len(layout_violations)} cross-module inherited row(s); "
          f"{layout_exempt} exempt (base exists in one module only).")
    if layout_violations:
        for v in layout_violations[:20]:
            print(f"  ERROR: {v}", file=sys.stderr)
        if len(layout_violations) > 20:
            print(f"  ERROR: … and {len(layout_violations) - 20} more",
                  file=sys.stderr)
        return 3

    print("Generating Markdown protobuf pages…")
    generate_protobufs_md_page(protos, overlays, generated_dir)

    proto_info = generate_proto_overlays(build_dir, generated_dir)
    _pc = len(proto_info["collisions"]["messages"]) + len(proto_info["collisions"]["enum_values"])
    print(f"  Wrote {proto_info['count']} normalised .proto overlay file(s) "
          f"({len(proto_info['dropped_imports'])} dangling import(s) dropped, "
          f"{_pc} cross-file symbol collision(s) documented).")

    print("Generating Markdown convar and command pages…")
    generate_convars_md_page(convars, generated_dir, source_info=schema_source_info)
    generate_commands_md_page(commands, generated_dir, source_info=schema_source_info)

    print("Generating convars_schema.json and commands_schema.json…")
    generate_convars_schema(convars, generated_dir, source_info=schema_source_info)
    generate_commands_schema(commands, generated_dir, source_info=schema_source_info)

    print("Generating well_known_constants.json…")
    generate_well_known_constants_schema(
        overlays_dir, generated_dir, source_info=schema_source_info
    )

    print("Generating game events documentation…")
    generate_gameevents_md_page(gameevents, overlays, generated_dir)
    generate_gameevents_schema(
        gameevents, overlays, generated_dir, source_info=schema_source_info
    )

    print("Generating cs2_schema.json (community-enriched mirror of cs2.json.gz)…")
    cs2_schema_path = generate_cs2_schema(
        entities, overlays, generated_dir, source_info=schema_source_info,
        diagram_modules=uml_md,
    )
    schema_kb = cs2_schema_path.stat().st_size // 1024
    print(f"  Wrote {cs2_schema_path.name} ({schema_kb} KiB).")

    generate_codegen_schemas_readme(
        generated_dir, source_info=schema_source_info, entities=entities,
        proto_info=proto_info,
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

    print("Checking overlay keys against this build…")
    overlay_unresolved, overlay_mismatched = check_overlay_keys(
        overlays, entities, protos, gameevents
    )
    print(f"  {len(overlay_unresolved)} unresolved overlay key(s), "
          f"{len(overlay_mismatched)} filed under the wrong module.")
    for line in overlay_unresolved:
        print(f"  UNRESOLVED {line}", file=sys.stderr)
    for line in overlay_mismatched:
        print(f"  MODULE     {line}", file=sys.stderr)
    if (overlay_unresolved or overlay_mismatched) and args.strict:
        print("  --strict: overlay keys must all resolve and sit under the module "
              "that declares them.", file=sys.stderr)
        return 5

    print("Checking generated Markdown tables…")
    table_problems = check_markdown_tables(out_dir)
    print(f"  {len(table_problems)} broken table row(s).")
    if table_problems:
        for tp in table_problems[:20]:
            print(f"  ERROR: {tp}", file=sys.stderr)
        if len(table_problems) > 20:
            print(f"  ERROR: … and {len(table_problems) - 20} more", file=sys.stderr)
        return 4

    print("Generating site data bundle…")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import site_data
    site_files = site_data.emit_site_data(
        repo_root, artifacts_root=artifacts_root, build=args.build,
        platform=args.platform, output=out_dir,
    )
    print(f"  {len(site_files)} file(s), {sum(site_files.values()) / 1024:.0f} KB under {generated_dir / 'data'}")
    for i in site_data.INFOS:
        print(f"  INFO {i}")
    for w in site_data.WARNINGS:
        print(f"  WARNING {w}", file=sys.stderr)
    if site_data.WARNINGS and args.strict:
        print("  --strict: site data warnings are fatal.", file=sys.stderr)
        return 6

    print(f"\nDone!  Home page: {out_dir}/index.md")
    print(f"        Generated content: {generated_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
