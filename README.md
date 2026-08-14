## CS2 Developer Reference

Structured, navigatable HTML documentation for Counter-Strike 2 — entity
schemas, network message (Protobuf) references, ConVars, commands, game events,
game content, and UML inheritance diagrams — auto-generated from
[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)
and published to **GitHub Pages**.

### How it works

A single upstream repo is included as a **read-only git submodule**:

- [`CS2OpenDev/CS2OpenDev-SchemaTracker`](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)
  at `upstream/schema-tracker/` — one deterministic, provenance-tracked,
  proto-validated artifact set per `(build, platform)` under
  `artifacts/<build_id>/<platform>/`.  SchemaTracker walks the shipped CS2
  runtime binaries in-process and emits clean JSON: `entity_schema.json`
  (classes, enums, fields, offsets, sizes, parents, metadata, binary module +
  projectName), a prebuilt `protos.descriptorset`, `convars.json`,
  `commands.json`, `gameevents.json`, `provenance.json`, plus a whole
  game-content layer (items, game modes, surfaces, props, maps, network/demo
  message tables) and a cumulative `schema_evolution.json`.

This replaced the previous three-link chain (GameTracking-CS2 +
SchemaExplorer/DumpSource2 + an external `protoc`) with one source we control.
`protoc` is no longer required — the generator reads the prebuilt
`FileDescriptorSet` directly via `google.protobuf.descriptor_pb2`.

A scheduled GitHub Actions workflow runs every **4 hours**, checks out the
SchemaTracker [`latest`](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker/tree/latest)
branch (a shallow single-branch clone carrying only the newest build plus a
root `LATEST.json` pointer, so the multi-GB history is never fetched), and
regenerates documentation if anything changed.  The generated Markdown is
committed back to this repo and deployed to GitHub Pages automatically.

```
CS2OpenDev/CS2OpenDev-SchemaTracker (latest branch)
    └── upstream/schema-tracker/  ← submodule tracking `latest` (single build + LATEST.json)
            artifacts/<build_id>/<platform>/*.json + protos.descriptorset
            │
            ▼
  this repo
    ├── docs/generate_docs.py   ← the only generator
    ├── docs/overlays/          ← community annotations (hand-edited)
    ├── docs/index.md           ← generated home page
    └── docs/generated/         ← generated reference docs (committed) → GitHub Pages
```

### Browse the docs

Visit the GitHub Pages site for this repository, or browse `docs/generated/`
directly.

### Protobuf Reference

Every Protobuf file has a page in [`docs/generated/proto/`](docs/generated/proto/)
containing a Mermaid class diagram, full field tables, enum value listings, and
overlay-based annotations.  The wire-protocol tables (integer message ID →
protobuf message type, per channel) live at
[`docs/generated/network.md`](docs/generated/network.md), cross-linked to the
proto pages.

### Downstream codegen schemas

For tooling builders (C# / Rust / Go / TypeScript SDKs, demo parsers,
plugins, etc.), structured JSON outputs live under
[`docs/generated/downstream-codegen-schemas/`](docs/generated/downstream-codegen-schemas/):

- `cs2_schema.json` — community-enriched projection of SchemaTracker's native
  `entity_schema.json` (classes, structs, enums, field offsets, sizes,
  inheritance, binary module + projectName, flags, metadata).  This is a
  **breaking `2.0`** shape — no longer a byte-for-byte DumpSource2 mirror; see
  the index README for the migration note.
- `gameevents_schema.json` — structured mirror of the game-event registry.
- `convars_schema.json` / `commands_schema.json` — structured projections
  of the ConVars and commands tables (with `valueType`, min/max, completion
  flags).
- `well_known_constants.json` — curated tables for values not exposed as
  named enums (team numbers, `m_gamePhase`, `CSWeaponState_t`).

All share an additive `annotations` enrichment pattern and a top-level
`schema_format_version` string.  See the
[index README](docs/generated/downstream-codegen-schemas/README.md) for the
format reference, a per-build type-vocabulary inventory, and the version
bump policy.

### Contributing annotations

Community members can add descriptions, notes, and reverse-engineered details
to any entity, Protobuf message, or game event by placing a YAML file under
`docs/overlays/`.  These annotations are merged into the generated HTML at
build time — the generated schema itself stays a faithful, provable mirror of
the SchemaTracker source; community knowledge lives in the overlays alongside it.

See [`docs/overlays/README.md`](docs/overlays/README.md) for the full format and examples.

### Running the generator locally

```bash
# Clone with the submodule (tracks SchemaTracker's `latest` branch)
git clone --recurse-submodules --shallow-submodules https://github.com/CS2OpenDev/CS2OpenDev-Docs.git
cd CS2OpenDev-Docs

# Or initialise the submodule in an existing clone (--remote follows `latest`)
git submodule update --init --remote --depth 1 upstream/schema-tracker

pip install pyyaml protobuf   # protoc is NOT needed

python3 docs/generate_docs.py \
  --repo-root . \
  --artifacts-root ./upstream/schema-tracker/artifacts \
  --build latest --platform windows-x86_64 \
  --output docs
```

The `latest` branch also carries the cumulative
`artifacts/schema_evolution/<platform>.json`, so the **Schema History** page
and `field_history.json` render straight from a plain submodule run — no
supplemental fetch needed.  Alternatively, point `--artifacts-root` at a full
SchemaTracker checkout's `artifacts/` directory:

```bash
python3 docs/generate_docs.py --repo-root . \
  --artifacts-root /path/to/CS2OpenDev-SchemaTracker/artifacts --output docs
```

### Join our Discord

[![Join our Discord](https://discord.com/api/guilds/467730051622764565/embed.png?style=banner2)](https://steamdb.info/discord/)
