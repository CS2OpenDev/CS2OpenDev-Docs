# Tooling Overhaul Plan

> Living plan tracking the migration from regex-based extraction to consuming
> upstream structured outputs.  Update the checkboxes as work lands.  Open
> questions stay near the top so we surface decisions before they ossify.

## Mission statement

CS2-OpenDevDocs is the single open-source location for **community-enriched**
Counter-Strike 2 documentation — both human-readable (Markdown, Mermaid) and
codegen-ready (JSON Schema, `.proto`).  Our value is curation, annotation, and
presentation.  Extraction is upstream's job.

We will:

- Consume upstream tooling rather than reinvent it.
- Never fork upstream tools — contribute back when changes are needed.
- Originate only the things only we can: the **community overlay system**, the
  **aggregated reference site**, and the **codegen-ready schema bundles**.
- Get the most detailed information possible from the most definitive source of
  truth possible.

---

## Sources of truth

| Domain | Definitive source | How extracted today (upstream) | Format we should consume |
|---|---|---|---|
| Entity schemas (classes, structs, enums, fields, offsets, sizes, parents, metadata) | `CSchemaSystem` runtime reflection in live game DLLs | `ValveResourceFormat/DumpSource2` calls `InstallSchemaBindings` on every game DLL, then walks `CSchemaSystemTypeScope` | `cs2.json.gz` redistributed in `ValveResourceFormat/SchemaExplorer` at `schemas/cs2.json.gz` (added as a git submodule — see Phase 1.1) |
| Network protobufs | `FileDescriptor`s compiled into CS2 binaries | `SteamDatabase/GameTracking-CS2` extracts `.proto` files from binaries | `.proto` files → `protoc --descriptor_set_out --include_source_info` → `FileDescriptorSet` |
| Game events | `.gameevents` files (KeyValues1 format) shipped in game `pak01_dir/resource/` | `GameTracking-CS2` extracts them into `data/game/...` | KV1 text — small, parse in-house OR with a KV1 library (see KV note below) |
| ConVars / Commands | `ICvar` runtime enumeration | `DumpSource2` (text dump) | Plain text — small, current parser fine |
| Module metadata | runtime | `DumpSource2` (text dump) | Plain text — small |
| Free-form descriptions, notes, warnings, codegen hints | **Nothing upstream — purely human-authored** | — | `docs/overlays/<module>.yml` — **the project's identity** |

### KV1 format note

`.gameevents` files are KeyValues1 — confirmed by inspection
(`data/game/csgo/pak01_dir/resource/*.gameevents` are wrapped `"name" { ... }`
KV blocks with `//` comments).  ValveResourceFormat publishes
[`ValveKeyValue`](https://github.com/ValveResourceFormat/ValveKeyValue) — the
canonical .NET parser.  Because it's .NET-only it isn't a runtime dependency
for our Python (or future TypeScript) generator, but it's the **reference
implementation** of the format.  Cross-language equivalents:

- Python: `vdf` PyPI package (ValvePython) — clean KV1 reader/writer
- TypeScript: `vdfjs` / `simple-vdf`
- Our current ~150-line in-house parser is fine for the single use case
  (`.gameevents` only) and avoids an extra dependency

**Decision:** keep the current in-house KV1 parser unless we hit a real
fidelity bug.  If we do, swap to `vdf` (Python) / `vdfjs` (TS).  Don't
restructure to call the .NET tool.

---

## Tool stack commitment

### Inputs (consume — do not reinvent)
- [x] `data/` git submodule of `SteamDatabase/GameTracking-CS2` — runs every
      CS2 update; source for `.proto`, `.gameevents`, and game content
- [x] `schema-explorer/` git submodule of `ValveResourceFormat/SchemaExplorer` —
      provides `schemas/cs2.json.gz` (DumpSource2's output, redistributed);
      replaces our regex `.h` parser (Phase 1.1).  *Path note:* lives at the
      repo root rather than under `data/SchemaExplorer/` because Git rejects
      a submodule nested inside another submodule.
- [x] `protoc` + `google.protobuf.descriptor_pb2` — replaces our regex
      `.proto` parser (Phase 1.2)
- [x] `PyYAML` — overlay loading
- [x] `jsonschema` — meta-schema self-validation

### Generator (the part we own — keep small)
- [x] Python `generate_docs.py` — current home
- [x] Jekyll + `just-the-docs` theme — search, mermaid, dark mode, mobile
      handled out of the box
- [x] Mermaid diagrams generated inline in Markdown — differentiator vs. plain
      SchemaExplorer

### Outputs
- [x] Markdown reference site → GitHub Pages
- [x] `cs2_schema.json` (entities, JSON Schema 2020-12, codegen-ready)
- [x] `gameevents_schema.json` (events, JSON Schema 2020-12, codegen-ready)
- [ ] Per-proto JSON Schemas — **explicitly out of scope** (proto codegens
      consume `.proto` / `FileDescriptorSet` natively; JSON Schema for proto
      messages would be reinventing)

---

## Things we will explicitly NOT do

1. Don't **fork** any upstream tool.  Contribute back instead.
2. Don't write our own VPK / KV3 / VPK_C extractor — that's
   `ValveResourceFormat` (the main project) territory.
3. Don't write our own protobuf parser — `protoc` exists and is bulletproof.
4. Don't generate per-proto JSON Schemas — proto codegens want `.proto`.
5. Don't ship a runtime tool — DumpSource2 needs a CS2 install + matching
   game-revision DLLs to work.  This repo stays static-publisher.
6. Don't take ownership of HL2SDK churn — that's DumpSource2's problem.

---

## Phased migration

### Phase 1 — Switch input sources (immediately actionable, all local)

Goal: stop parsing what upstream tools already structure for us.

- [x] **1.1 Schema input pivot**
  - [x] Add `ValveResourceFormat/SchemaExplorer` as a git submodule at
        `schema-explorer/` (sibling of `data/`, since Git rejects a submodule
        nested inside another submodule).  `schemas/cs2.json.gz` lives on
        its `main` branch and is committed (no LFS, no fetching gymnastics).
        **Note on cadence:** SchemaExplorer is not an independent mirror —
        the shared `steamtracking/gametracking` workflow that GameTracking-CS2
        invokes pushes `cs2.json.gz` to SchemaExplorer as part of the same
        pipeline run that updates the `.h` files we already consume.  Same
        trigger, same revision, same CS2 patch.  The regen workflow bumps
        both submodules together; they will normally point at the same
        upstream revision.
  - [x] In the generator, gunzip
        `schema-explorer/schemas/cs2.json.gz` at load time (Python stdlib
        `gzip` — no extra dependency).  `find_schema_json()` also accepts
        a future `data/DumpSource2/schemas.json[.gz]` location for Phase 2.1.
  - [x] Replaced `parse_schema_file` / `parse_all_schemas` with
        `load_schema_json()` that produces the same entity dict shape but
        sourced from the structured cs2.json (gain: `offset`, `size`,
        structured `type.category`, multi-parent, proper module namespacing).
  - [x] Updated `generate_cs2_json_schema` to emit `x-cs2-offset` on each
        property and `x-cs2-size` on each entity definition.
  - [x] Verified `CCSPlayerController` is preserved in **both** `client` and
        `server` modules (the new `_add_entity` dedupes on `(module, name)`,
        so cross-module siblings land in `duplicates` and both render).
  - [x] Deleted ~150 lines of `.h` regex parser plus ~110 lines of dead
        `generate_entity_md_page` (~260 lines net reduction once the JSON
        loader's ~180 lines are subtracted from the win).
  - [x] Updated `.github/workflows/generate-docs.yml` to bump
        `schema-explorer/` on every scheduled run alongside `data/`.

- [x] **1.2 Proto input pivot**
  - [x] Added `protobuf-compiler` (apt) to the workflow tool install plus
        the `protobuf` Python runtime alongside `pyyaml`/`jsonschema`.
  - [x] `load_proto_descriptors()` runs `protoc --descriptor_set_out
        --include_source_info` per file (one invocation per `.proto`).
        **Per-file rather than one big set** because CS2's protobuf dump
        contains cross-file enum-value collisions (e.g.
        `k_EMsgGCSystemMessage` is defined in both `base_gcmessages.proto`
        and `enums_clientserver.proto` — protoc treats enum values as
        global siblings under proto2 scoping rules).  Compiling without
        `--include_imports` keeps each file isolated.
  - [x] Replaced `parse_proto_file` with descriptor walker
        (`_proto_descriptor_to_dict`) that emits the same dict shape but
        sourced from `descriptor_pb2.FileDescriptorProto`.  Gains:
        real default values, source-info comments (leading + trailing),
        nested-enum discovery (the regex parser missed several — see the
        Mermaid diagram diff for `base_gcmessages`, `netmessages`, and
        the `steamnetworkingsockets_*` files), and downstream access to
        oneofs/services/options when we want them.
  - [x] No changes needed to `generate_protobufs_md_page` — the dict
        shape is preserved, and existing per-file Markdown output is
        byte-identical to the old regex parser for 81% of files; the
        rest gain content (didn't lose any).
  - [x] Deleted ~110 lines of `.proto` regex parser.

- [x] **1.3 Cleanup**
  - [x] Drop `generate_entity_md_page` (already dead code, never called)
  - [x] Confirm `generate_docs.py` is meaningfully smaller (Phase 1.1
        delivered ~50 lines net; the ~360-line target factors in Phase 1.2
        proto-parser deletion as well).
  - [x] Run end-to-end, diff `docs/generated/` for sanity (entity counts
        match exactly per-module; gains: 7 new module diagrams that
        previously had no resolvable bases under the regex parser, and
        `x-cs2-offset` / `x-cs2-size` on every property/entity).

### Phase 2 — Upstream contributions (parallel, opportunistic)

Goal: reduce coordination cost downstream of the same data we already consume.

- [ ] **2.1 PR on `SteamDatabase/GameTracking-CS2`: also commit the JSON
      output to the tracking repo itself**
  - [ ] DumpSource2 already produces `schemas.json` (or `.gz`) when invoked
        with the existing `dumpsource2-schema-json` input — they currently
        push it only to `ValveResourceFormat/SchemaExplorer`
  - [ ] Propose also writing it to `data/DumpSource2/schemas.json.gz` in
        the GameTracking-CS2 repo so consumers don't need a second submodule
  - [ ] When merged, drop our `data/SchemaExplorer/` submodule and read the
        JSON from our existing `data/` submodule

- [ ] **2.2 PR on `ValveResourceFormat/DumpSource2`: add a JSON-Schema
      exporter**
  - [ ] Open issue proposing `json_schema_exporter.cpp` alongside
        `json_exporter.cpp` and `filesystem_exporter.cpp`
  - [ ] Reference our shipped `cs2_schema.json` as the design spec
  - [ ] Implement (~300 lines C++ following the existing `json_exporter.cpp`
        pattern; intermediate representation already has every field needed)
  - [ ] Pitch: portable to any JSON Schema codegen (NJsonSchema, quicktype,
        json-schema-to-typescript), zero impact on existing outputs
  - [ ] When merged, our generator drops its JSON-Schema emission and
        consumes the upstream output (Phase 3)

- [ ] **2.3 (Stretch) `gameevents_exporter.cpp` for DumpSource2**
  - [ ] Investigate whether DumpSource2 has access to a runtime gameevents
        registry, or whether `.gameevents` parsing belongs elsewhere
  - [ ] If feasible, propose a unified events emitter

### Why we will NOT run DumpSource2 in our own CI

Considered and rejected.  The shared `steamtracking/gametracking` workflow
that GameTracking-CS2 already invokes runs DumpSource2 (with
`dumpsource2-schema-json: "cs2"`) on every CS2 patch and pushes the JSON
output to `ValveResourceFormat/SchemaExplorer`.  Running it ourselves would
require:

- A Windows runner with Steam credentials in repository secrets
- ~30 GB of game files downloaded per run via SteamCMD
- Reuse of the same `steamtracking/gametracking` shared workflow

…to produce a file that is already produced and committed to a public repo
on the exact cadence we need.  Strictly duplicate work.  We consume
SchemaExplorer's submodule until Phase 2.1 ships; then we consume
GameTracking-CS2 directly.

### Phase 3 — Generator becomes presenter only (long-term)

Goal: when DumpSource2 ships JSON Schema natively, our generator's only job is
"merge community overlays + render Markdown."

- [ ] **3.1 Drop our schema → JSON Schema generation code (~350 lines)**
- [ ] **3.2 Consume DumpSource2's emitted `cs2_schema.json` directly**
- [ ] **3.3 Layer overlay enrichments (descriptions, notes, warnings,
      codegen hints) onto the upstream JSON Schema**
- [ ] **3.4 Re-evaluate generator language** (see TypeScript section below)

---

## TypeScript evaluation

**Question:** would TypeScript be a better platform than Python for this
generator?

**On the merits, yes — slightly.** TypeScript matches the work we do better:

| Factor | Python | TypeScript |
|---|---|---|
| Markdown emission | string concatenation | `unified` / `remark` ecosystem (mature) |
| JSON Schema tooling | `jsonschema` (validation) | `ajv` (validation), `json-schema-to-typescript` (peers, same JS ecosystem) |
| Protobuf parsing | `protoc` + `descriptor_pb2` (needs protoc binary) | `protobufjs` (pure-JS, no protoc dependency) |
| Mermaid render | external | first-class JS support (`mermaid` is itself JS) |
| YAML | `PyYAML` (excellent) | `js-yaml` (excellent) |
| Type safety on a 1500+ line generator | dynamic — already showing strain (scattered `isinstance` checks) | static — catches the entire class of bugs |
| Tooling distribution | `pip install` | `npm install` (heavier) |
| CI install time | ~5s | ~30s |
| Single-language alignment with most JSON Schema codegen consumers | mismatch | match |
| Future Jekyll replacement (Astro/Eleventy/Next) | mismatch | match |

**Verdict:** **defer the language decision to the Phase 3 boundary.**

Reasoning:

1. Right now the generator is ~1750 lines and works.  A rewrite for its own
   sake doesn't pay off.
2. Phase 1 is a *shrink* (~360 lines deleted).  Doing Phase 1 in TypeScript
   would mean a full rewrite for a refactor that's otherwise mostly mechanical.
   Wrong time.
3. After Phase 3, the generator collapses to ~600 lines that's primarily
   "load JSON → walk YAML overlays → emit Markdown."  That's the right size
   to do a clean TypeScript rewrite — small enough to port quickly, large
   enough that static typing pays for itself.
4. If we do migrate at Phase 3, the resulting toolchain is more cohesive:
   `protobufjs` removes the `protoc` build dependency, `unified` plugins make
   Markdown extension trivial, and the same project could later host a fully
   TS-based static site if/when Jekyll is replaced.

**Decision recorded:** stay Python through Phases 1 and 2.  At Phase 3
boundary, evaluate seriously and likely port.

- [ ] (Phase 3) Re-open the language question with a concrete TypeScript
      port spike before committing

---

## Maintenance equilibrium goal

After Phase 1 and Phase 3, the steady-state breakdown of work on this repo:

- **0 hours/week** — schema / proto / convar extraction (all upstream)
- **0 hours/week** — schema → JSON Schema conversion (DumpSource2)
- **low / variable** — community overlay PRs (the project's actual purpose)
- **occasional** — Jekyll theme + generator bug fixes
- **rare** — adapting to upstream input format changes

That distribution is the goal: effort concentrates on what only this project
does.

---

## Open questions / decisions to revisit

- [ ] **Whether the per-proto Mermaid diagrams stay** after switching to
      `protoc` descriptors.  Some `.proto` files are huge and the diagrams
      may not render meaningfully.  Worth a sanity check during Phase 1.2.
- [ ] **Overlay schema extension** for codegen hints (per-field nullability
      override, flags-enum marker, etc.).  Defer until a community contributor
      asks.
