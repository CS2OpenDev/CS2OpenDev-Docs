# CS2 Developer Reference – Copilot workspace context

This repository contains **auto-generated, structured documentation** for
Counter-Strike 2, extracted from the
[SteamDatabase/GameTracking-CS2](https://github.com/SteamDatabase/GameTracking-CS2)
game-file dump (a read-only git submodule at `data/`).

## What is in this repo

| Path | Contents |
|------|----------|
| `data/` | Git submodule – raw CS2 game files (DumpSource2 schemas, Protobufs, convars) |
| `docs/generate_docs.py` | Python generator that produces all Markdown docs from `data/` |
| `docs/overlays/` | YAML community-annotation files merged into the generated docs |
| `docs/generated/schemas/` | One Markdown file per engine module (entity classes, structs, enums) |
| `docs/generated/proto/` | One Markdown file per `.proto` file (messages, fields, enums) |
| `docs/generated/diagrams/` | Mermaid UML class-hierarchy diagrams per module |
| `docs/generated/convars.md` | All CS2 console variables (name, default, flags, description) |
| `docs/generated/commands.md` | All CS2 console commands |
| `.github/workflows/generate-docs.yml` | Scheduled workflow: updates submodule → regenerates docs → opens a PR |

> Everything under `docs/generated/` is auto-generated — do not hand-edit. To
> change content, edit `docs/generate_docs.py` or add an overlay under
> `docs/overlays/`.

## Key entity classes (server-side)

- **`CBaseEntity`** → base of all server entities (see `docs/generated/schemas/server.md`)
- **`CCSPlayerController`** → CS2 player controller
- **`CCSWeaponBase`** / **`CCSWeaponBaseGun`** → weapon hierarchy
- **`CCSGameRules`** → game-rules singleton

## Key Protobuf groups

- `cstrike15_gcmessages.proto` – match-making, lobby, inventory GC messages
- `cstrike15_usermessages.proto` – per-client user messages (HUD, radar, …)
- `netmessages.proto` – core engine network messages
- `cs_gameevents.proto` – game events (bomb plant, kill, round end, …)
- `demo.proto` – demo-file recording format

## Adding community annotations

Place a YAML file at `docs/overlays/<module>/<EntityName>.yml` and run the
generator. See `docs/overlays/README.md` for the format.

## Running the generator locally

```bash
git clone --recurse-submodules https://github.com/sid2934/CS2-OpenDevDocs.git
cd CS2-OpenDevDocs
pip install pyyaml
python3 docs/generate_docs.py --repo-root . --data-root ./data --output docs
```
