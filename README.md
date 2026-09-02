## CS2 Developer Reference

Structured documentation for Counter-Strike 2: entity schemas, network message
(Protobuf) references, ConVars, commands, game events, game content, and UML
inheritance diagrams, auto-generated from
[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)
and published to **GitHub Pages**.

### Architecture

A single upstream repo is included as a **read-only git submodule**:

- [`CS2OpenDev/CS2OpenDev-SchemaTracker`](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)
  at `upstream/schema-tracker/`: one deterministic, provenance-tracked,
  proto-validated artifact set per `(build, platform)` under
  `artifacts/<build_id>/<platform>/`. SchemaTracker walks the shipped CS2
  runtime and tool binaries in-process and emits clean JSON: `entity_schema.json`
  (classes, enums, fields, offsets, sizes, parents, metadata, binary module +
  projectName), a prebuilt `protos.descriptorset`, `convars.json`,
  `commands.json`, `gameevents.json`, `provenance.json`, plus a game-content
  layer (items, game modes, surfaces, props, maps, network/demo message
  tables) and a cumulative `schema_evolution.json`.

`docs/generate_docs.py` reads that artifact set plus the hand-edited YAML
overlays in `docs/overlays/` and writes two outputs:

- `docs/generated/`: Markdown reference pages (`schemas/`, `proto/`,
  `diagrams/`, `convars.md`, `commands.md`, …) plus the portable JSON schemas
  under `downstream-codegen-schemas/` (`cs2_schema.json`,
  `gameevents_schema.json`, `convars_schema.json`, `commands_schema.json`,
  `well_known_constants.json`, `field_history.json`). This stays a
  first-class artifact in its own right: it renders directly in an IDE or on
  GitHub, and AI tools fetch it raw (see `AGENTS.md`).
- `docs/generated/data/`: a second JSON bundle, written by
  `docs/site_data.py` (invoked by the same generator run), that backs every
  page of the Astro site. See `docs/generated/data/README.md` for the format
  of each file.

The `site/` directory is an Astro 7 + Starlight site that renders every page
from `docs/generated/downstream-codegen-schemas/cs2_schema.json` and
`docs/generated/data/*.json`. It never reads the generated Markdown. See
`site/README.md` for how the site is built.

```
CS2OpenDev/CS2OpenDev-SchemaTracker (latest branch)
    └── upstream/schema-tracker/   ← submodule tracking `latest` (single build + LATEST.json)
            artifacts/<build_id>/<platform>/*.json + protos.descriptorset
            │
            ▼
  this repo
    ├── docs/generate_docs.py      ← the only generator; also runs docs/site_data.py
    ├── docs/overlays/             ← community annotations (hand-edited)
    ├── docs/index.md              ← generated Markdown landing page
    ├── docs/generated/            ← generated Markdown + downstream JSON schemas (committed)
    ├── docs/generated/data/       ← generated JSON data bundle for the site (committed)
    └── site/                      ← Astro + Starlight site, reads the JSON above
            │
            ▼
      GitHub Pages
```

### Browse the docs

Visit the GitHub Pages site for this repository, or browse `docs/generated/`
directly on GitHub.

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
  --output docs --strict
```

`--strict` fails the run on any overlay key that doesn't resolve against the
build; see `docs/overlays/README.md`. Run the generator's tests with:

```bash
python3 -m unittest discover -s docs/tests -t docs/tests
```

### Running the site locally

```bash
cd site
npm ci
npm run dev      # http://localhost:4321/CS2OpenDev-Docs/
npm run build    # full static build into site/dist/ (~25s, ~1.5GB)
npm run check    # type check, then link and size checks against the build
```

`SITE_SUBSET=<n> npm run build` builds a fast subset (first `n` entities per
module) for iterating on a page without waiting on all ~4,400 entity routes.
See `site/README.md` for the full set of env vars and what reads what.

### Contributing annotations

Community members can add descriptions, notes, and reverse-engineered detail
to any entity, Protobuf message, ConVar, command, or game event by placing a
YAML file under `docs/overlays/`. These annotations are merged into both
generated outputs at build time; the generated schema itself stays a
faithful, provable mirror of the SchemaTracker source, and community
knowledge lives in the overlays alongside it.

See [`docs/overlays/README.md`](docs/overlays/README.md) for the full format
and examples.

### Workflow

`.github/workflows/generate-docs.yml` polls for new SchemaTracker builds
every 4 hours and rebuilds immediately on a push touching the overlays, the
generator, its tests, or the site. It regenerates the docs with `--strict`,
runs the generator's tests, builds the Astro site, runs its link and size
checks, and deploys to GitHub Pages.

### Join our Discord

[![Join our Discord](https://discord.com/api/guilds/467730051622764565/embed.png?style=banner2)](https://steamdb.info/discord/)
