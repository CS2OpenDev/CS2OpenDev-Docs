# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is (and is not)

This repo is a **documentation generator and Jekyll site**, not a CS2 plugin / SDK / runtime. It auto-generates Markdown reference docs (entity schemas, Protobuf messages, ConVars, commands, UML diagrams) from a snapshot of CS2 game files and publishes them to GitHub Pages.

Do **not** write CS2 plugin code, server-side logic, demo parsers, or game tooling here. Such requests should be redirected to a separate consumer project — this repo only describes the data those projects need. `AGENTS.md` and `.github/agents/cs2-engineer.agent.md` exist as **deliverables for external consumers** of the docs (loaded into their AI tools); they do not describe what gets built *in this repo*.

## Architecture

```
SteamDatabase/GameTracking-CS2 (upstream)         ValveResourceFormat/SchemaExplorer (upstream)
    └── upstream/data/  ← read-only git submodule    └── upstream/schema-explorer/  ← read-only git submodule
            │                                                      │
            ▼                                                      ▼
    docs/generate_docs.py           ← the only generator
    docs/overlays/                  ← YAML community annotations (HAND-EDITED)
            │
            ▼
    docs/index.md                   ← GENERATED home page (Jekyll requires it at site root)
    docs/generated/                 ← GENERATED reference docs (everything else)
        schemas.md, schemas/*.md
        protobufs.md, proto/*.md
        diagrams/*.md
        convars.md, commands.md, gameevents.md
        cs2_schema.json              ← portable JSON Schema (2020-12) for codegen
        gameevents_schema.json       ← portable JSON Schema for game events
            │
            ▼
    Jekyll (just-the-docs theme, hand-maintained _config.yml + _includes/) → GitHub Pages
```

Inputs the generator reads:
- `upstream/schema-explorer/schemas/cs2.json.gz` — DumpSource2's structured entity dump (classes, structs, enums, fields, offsets, sizes, parents, metadata).  This is the source of truth for the schema; it replaced the old regex `.h` parser in Phase 1.1 of `TOOLING_OVERHAUL.md`.
- `upstream/data/Protobufs/*.proto` — ~42 proto files, compiled per-file via `protoc --descriptor_set_out --include_source_info` and walked with `google.protobuf.descriptor_pb2`.  This replaced the old regex `.proto` parser in Phase 1.2.  Per-file (not one big set) to dodge cross-file enum-value collisions in the upstream dump.
- `upstream/data/DumpSource2/convars.txt`, `upstream/data/DumpSource2/commands.txt`
- `upstream/data/DumpSource2/module_metadata/` — per-module metadata
- `upstream/data/game/csgo/pak01_dir/resource/*.gameevents` — Valve KeyValues1

The `upstream/data/DumpSource2/schemas/<module>/*.h` files are *no longer parsed* — the generator now consumes the structured JSON instead.  Phase 2.1 of TOOLING_OVERHAUL upstreams the JSON to GameTracking-CS2 itself; once that lands, the `upstream/schema-explorer/` submodule will be retired.

External tools the generator shells out to:
- `protoc` — Protocol Buffers compiler.  Install with `brew install protobuf` (macOS) or `apt install protobuf-compiler` (Debian/Ubuntu).

Per-entity overlays at `docs/overlays/<module>.yml` (multi-entity, recommended) or `docs/overlays/<module>/<EntityName>.yml` (legacy single-file) get merged into the generated output. Format is documented in `docs/overlays/README.md`.

## Critical rules

- **Never hand-edit anything under `docs/generated/`.** Every file there is overwritten by the next generator run. The home page (`docs/index.md`) is also generated — don't hand-edit it. To change generated content, edit either (a) the generator script or (b) an overlay YAML.
- `docs/_config.yml`, `docs/_includes/`, and `docs/Gemfile` are **hand-maintained**. The generator does not touch them. Theme/layout customization goes here.
- **Never edit `upstream/data/` or `upstream/schema-explorer/`** — both are read-only submodules pointing at upstream repos (`SteamDatabase/GameTracking-CS2` and `ValveResourceFormat/SchemaExplorer` respectively). Fresh clones need `git submodule update --init --recursive` (or `git clone --recurse-submodules`); the submodules are empty otherwise and the generator will exit with an error.
- The submodule pointers are only advanced by the scheduled GitHub Action (`.github/workflows/generate-docs.yml`) — don't bump them locally as part of a content change unless that's specifically what you're doing.
- `AGENTS.md` is the canonical context-for-external-AI-tools file. If schema/architecture facts change, update it there (not in CLAUDE.md, which is for *this* repo's contributors).
- `TOOLING_OVERHAUL.md` is the living plan for the input-source migration (regex parsers → consume `cs2.json` from DumpSource2 + `protoc` descriptors). Update its checkboxes as work lands; revisit the TypeScript decision at the Phase 3 boundary.

## Common commands

```bash
# After a fresh clone without --recurse-submodules:
git submodule update --init

# Regenerate all docs (the only build step that matters):
pip install pyyaml jsonschema protobuf
# (protoc itself must also be on PATH — `brew install protobuf` / `apt install protobuf-compiler`)
python3 docs/generate_docs.py --repo-root . --data-root ./upstream/data --output docs
```

There is no test suite, lint config, or build step beyond the Python generator and Jekyll. Validation is "run the generator, `git status` should show changes only under `docs/generated/` (plus `docs/index.md` if entity counts changed)."

## Workflow behavior worth knowing

`.github/workflows/generate-docs.yml` runs every 4 hours (cron) and on pushes that touch `docs/overlays/**`, `docs/generate_docs.py`, or the workflow itself.

- **Push event** → regenerates and commits straight to the branch (`[skip ci]`).
- **Schedule / manual dispatch** → opens or updates a PR on branch `automated/docs-update`.

So: a PR that only edits an overlay will trigger a regeneration commit on the same branch. Don't be surprised when generated files under `docs/generated/` change without you authoring them.
