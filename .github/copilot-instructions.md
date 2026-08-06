# CS2 Developer Reference – Copilot workspace context

This repository contains **auto-generated, structured documentation** for
Counter-Strike 2, extracted from the
[CS2OpenDev/CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)
artifact set (a read-only git submodule at `upstream/schema-tracker/`).

## What is in this repo

| Path | Contents |
|------|----------|
| `upstream/schema-tracker/` | Git submodule – SchemaTracker artifacts (`artifacts/<build_id>/<platform>/*.json` + `protos.descriptorset`); tracks the `latest` branch (single build + root `LATEST.json`) |
| `docs/generate_docs.py` | Python generator that produces all Markdown docs from the SchemaTracker artifacts |
| `docs/overlays/` | YAML community-annotation files merged into the generated docs |
| `docs/generated/schemas/` | One Markdown file per module (entity classes, structs, enums) |
| `docs/generated/proto/` | One Markdown file per `.proto` file (messages, fields, enums) |
| `docs/generated/network.md` | Wire-protocol tables: message ID → protobuf message type, per channel |
| `docs/generated/diagrams/` | Mermaid UML class-hierarchy diagrams per module |
| `docs/generated/convars.md` | All CS2 console variables (name, default, flags, description) |
| `docs/generated/commands.md` | All CS2 console commands |
| `.github/workflows/generate-docs.yml` | Scheduled workflow: materialises latest SchemaTracker build → regenerates docs → opens a PR |

> Everything under `docs/generated/` is auto-generated — do not hand-edit. To
> change content, edit `docs/generate_docs.py` or add an overlay under
> `docs/overlays/`.  `protoc` is not required; the generator reads the prebuilt
> `protos.descriptorset` directly.

## Key entity classes (server-side)

- **`CBaseEntity`** → base of all server entities (see `docs/generated/schemas/server.md`)
- **`CCSPlayerController`** → CS2 player controller
- **`CCSWeaponBase`** / **`CCSWeaponBaseGun`** → weapon hierarchy
- **`CCSGameRules`** → game-rules singleton

## Key Protobuf groups

- `cstrike15_gcmessages.proto` – match-making, lobby, inventory GC messages
- `demo.proto` – demo-file recording format
- `networksystem_protomessages.proto` – Source 2 network-system messages
- `steammessages.proto` – Steam platform messages

> Note: the core wire protos (`netmessages`, `usermessages`,
> `cstrike15_usermessages`, `cs_gameevents`, `networkbasetypes`) now ship in
> SchemaTracker's `protos.descriptorset` and render with their overlays under
> `docs/overlays/protobufs/`.

## Adding community annotations

Place a YAML file under `docs/overlays/` (multi-entity `<module>.yml` preferred)
and run the generator. See `docs/overlays/README.md` for the format.

## Running the generator locally

```bash
git clone --recurse-submodules --shallow-submodules https://github.com/CS2OpenDev/CS2OpenDev-Docs.git
cd CS2OpenDev-Docs
# (existing clone: git submodule update --init --remote --depth 1 upstream/schema-tracker)
pip install pyyaml protobuf
python3 docs/generate_docs.py --repo-root . \
  --artifacts-root ./upstream/schema-tracker/artifacts --build latest \
  --platform windows-x86_64 --output docs
```
