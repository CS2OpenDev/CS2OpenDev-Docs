## CS2 Developer Reference

Structured, navigatable HTML documentation for Counter-Strike 2 — entity
schemas, network message (Protobuf) references, ConVars, and UML inheritance
diagrams — auto-generated from [GameTracking-CS2](https://github.com/SteamDatabase/GameTracking-CS2)
and published to **GitHub Pages**.

### How it works

Two upstream repos are included as **read-only git submodules**:

- [`SteamDatabase/GameTracking-CS2`](https://github.com/SteamDatabase/GameTracking-CS2)
  at `upstream/data/` — Protobufs, .gameevents, ConVars, commands.
- [`ValveResourceFormat/SchemaExplorer`](https://github.com/ValveResourceFormat/SchemaExplorer)
  at `upstream/schema-explorer/` — DumpSource2's structured `cs2.json.gz` (the
  source of truth for entity schemas: classes, enums, fields, offsets, sizes,
  parents, metadata).

A scheduled GitHub Actions workflow runs every **4 hours**, advances both
submodules to upstream HEAD, and regenerates documentation if anything
changed.  The updated submodule pointers and generated Markdown are committed
back to this repo and deployed to GitHub Pages automatically.

```
SteamDatabase/GameTracking-CS2          ValveResourceFormat/SchemaExplorer
    └── upstream/data/  ← submodule pointer    └── upstream/schema-explorer/  ← submodule pointer
            │                                            │
            ▼                                            ▼
  this repo
    ├── docs/generate_docs.py   ← generator
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
overlay-based annotations.

### Downstream codegen schemas

For tooling builders (C# / Rust / Go / TypeScript SDKs, demo parsers,
plugins, etc.), structured JSON outputs live under
[`docs/generated/downstream-codegen-schemas/`](docs/generated/downstream-codegen-schemas/):

- `cs2_schema.json` — community-enriched mirror of DumpSource2's
  `cs2.json.gz` (classes, structs, enums, field offsets, sizes, inheritance,
  metadata).  Byte-for-byte compatible with upstream so any tool already
  targeting `cs2.json.gz` works unchanged.
- `gameevents_schema.json` — structured mirror of the parsed
  `.gameevents` registry.
- `convars_schema.json` / `commands_schema.json` — structured projections
  of the ConVars and commands tables.
- `well_known_constants.json` — curated tables for values not exposed as
  named enums in the dump (team numbers, `m_gamePhase`, `CSWeaponState_t`).

All five share an additive `annotations` enrichment pattern and a top-level
`schema_format_version` string.  See the
[index README](docs/generated/downstream-codegen-schemas/README.md) for the
format reference, a per-build type-vocabulary inventory, and the version
bump policy.

### Contributing annotations

Community members can add descriptions, notes, and reverse-engineered details
to any entity or Protobuf message by placing a YAML file under `docs/overlays/`.
These annotations are merged into the generated HTML at build time.

See [`docs/overlays/README.md`](docs/overlays/README.md) for the full format and examples.

### Running the generator locally

```bash
# Clone with both submodules
git clone --recurse-submodules https://github.com/CS2OpenDev/CS2OpenDev-Docs.git
cd CS2OpenDev-Docs

# Or initialise the submodules in an existing clone
git submodule update --init --recursive

pip install pyyaml protobuf
# protoc itself must also be on PATH (brew install protobuf / apt install protobuf-compiler)

python3 docs/generate_docs.py \
  --repo-root . \
  --data-root ./upstream/data \
  --output docs
```

For local development without an upstream submodule pull, point at any
DumpSource2 `cs2.json` (gzipped or not) directly:

```bash
python3 docs/generate_docs.py --schema-json /path/to/cs2.json
```

### Join our Discord

[![Join our Discord](https://discord.com/api/guilds/467730051622764565/embed.png?style=banner2)](https://steamdb.info/discord/)
