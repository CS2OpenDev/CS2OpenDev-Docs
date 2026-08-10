# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is (and is not)

This repo is a **documentation generator and Jekyll site**, not a CS2 plugin / SDK / runtime. It auto-generates Markdown reference docs (entity schemas, Protobuf messages, ConVars, commands, UML diagrams) from a snapshot of CS2 game files and publishes them to GitHub Pages.

Do **not** write CS2 plugin code, server-side logic, demo parsers, or game tooling here. Such requests should be redirected to a separate consumer project — this repo only describes the data those projects need. `AGENTS.md` and `.github/agents/cs2-engineer.agent.md` exist as **deliverables for external consumers** of the docs (loaded into their AI tools); they do not describe what gets built *in this repo*.

## Architecture

```
CS2OpenDev/CS2OpenDev-SchemaTracker (upstream, `latest` branch)
    └── upstream/schema-tracker/  ← read-only git submodule tracking `latest` (single build + LATEST.json)
            artifacts/<build_id>/<platform>/*.json + protos.descriptorset
            │
            ▼
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

Everything comes from **one** CS2OpenDev-SchemaTracker artifact set —
`artifacts/<build_id>/<platform>/` — selected by `resolve_build_dir` (highest-numbered
committed build for the chosen platform, default `windows-x86_64`). Inputs the generator reads:
- `entity_schema.json` — the structured entity dump (classes, structs, enums, fields, offsets, sizes, parents, metadata, binary `module` + `projectName`).  Source of truth for the schema; loaded by `load_entity_schema` and shaped by `_convert_class`/`_convert_enum`.
- `protos.descriptorset` — a **prebuilt** `FileDescriptorSet` of the build's protobufs, read directly via `google.protobuf.descriptor_pb2` (no `protoc`).  `google/protobuf/*` well-known files are skipped.
- `convars.json`, `commands.json` — loaded as structured JSON (richer than the old text dumps: `valueType`, min/max, completion-callback flags).
- `gameevents.json` — structurally-parsed game-event registry.
- `provenance.json` — build id, Steam date, schema/tool versions (page/schema headers).

SchemaTracker walks the **shipped CS2 runtime binaries**, so coverage is runtime-only
(~1,500 entities across `client`/`server`/`entity2`/`pulse_runtime_lib`/`particleslib`/`animgraphlib`);
the Source 2 editor/tooling schema is deliberately absent. Content artifacts
(`item_definitions.json`, `game_modes.json`, `network_messages.json`, `changelog.json`, …)
are available for new pages but not all wired up yet.

No external tools are shelled out — `protoc` is no longer required.

Per-entity overlays at `docs/overlays/<module>.yml` (multi-entity, recommended) or `docs/overlays/<module>/<EntityName>.yml` (legacy single-file) get merged into the generated output. Format is documented in `docs/overlays/README.md`.

## Critical rules

- **Never hand-edit anything under `docs/generated/`.** Every file there is overwritten by the next generator run. The home page (`docs/index.md`) is also generated — don't hand-edit it. To change generated content, edit either (a) the generator script or (b) an overlay YAML.
- `docs/_config.yml`, `docs/_includes/`, and `docs/Gemfile` are **hand-maintained**. The generator does not touch them. Theme/layout customization goes here.
- **Never edit `upstream/schema-tracker/`** — it's a read-only submodule pointing at `CS2OpenDev/CS2OpenDev-SchemaTracker`. It tracks that repo's **`latest`** branch, which carries only the newest build's artifacts plus a root `LATEST.json` pointer — so `git submodule update --init --remote --depth 1 upstream/schema-tracker` is a tens-of-MB checkout, not the multi-GB full history. Without it materialised, the generator exits with an error. For local dev you can bypass the submodule with `--artifacts-root <path-to-a-SchemaTracker-checkout>/artifacts`. Note: the `latest` branch now also carries `artifacts/schema_evolution/<platform>.json` (input to the Schema History page), so a plain `latest`-only checkout renders Schema History too — no supplemental fetch required.
- The submodule pointers are only advanced by the scheduled GitHub Action (`.github/workflows/generate-docs.yml`) — don't bump them locally as part of a content change unless that's specifically what you're doing.
- `AGENTS.md` is the canonical context-for-external-AI-tools file. If schema/architecture facts change, update it there (not in CLAUDE.md, which is for *this* repo's contributors).

## Common commands

```bash
# Materialise just the latest SchemaTracker build (shallow clone of `latest`):
git clone --depth 1 --single-branch --branch latest \
  https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker.git upstream/schema-tracker
# (or, via the submodule declaration:)
#   git submodule update --init --remote --depth 1 upstream/schema-tracker

# Regenerate all docs (the only build step that matters):
pip install pyyaml protobuf   # protoc is NOT needed
python3 docs/generate_docs.py --repo-root . \
  --artifacts-root ./upstream/schema-tracker/artifacts --build latest \
  --platform windows-x86_64 --output docs

# Local dev against a full SchemaTracker checkout (skip the submodule):
python3 docs/generate_docs.py --repo-root . \
  --artifacts-root /path/to/CS2OpenDev-SchemaTracker/artifacts --output docs
```

There is no test suite, lint config, or build step beyond the Python generator and Jekyll. Validation is "run the generator, `git status` should show changes only under `docs/generated/` (plus `docs/index.md` if entity counts changed)."

## Workflow behavior worth knowing

`.github/workflows/generate-docs.yml` runs every 4 hours (cron) and on pushes that touch `docs/overlays/**`, `docs/generate_docs.py`, or the workflow itself.

- **Push event** → regenerates and commits straight to the branch (`[skip ci]`).
- **Schedule / manual dispatch** → opens or updates a PR on branch `automated/docs-update`.

So: a PR that only edits an overlay will trigger a regeneration commit on the same branch. Don't be surprised when generated files under `docs/generated/` change without you authoring them.
