# Overlay Annotations

This directory contains YAML files that add **community-contributed descriptions
and notes** to the auto-generated CS2 documentation.  They are merged into the
generated HTML at build time without touching the auto-generated schema files.

---

## Directory layout

```
docs/overlays/
├── README.md            ← you are here
├── server.yml           ← multi-entity overlay for the 'server' module
├── gameevents.yml       ← overlay for game events (from .gameevents files)
├── protobufs/           ← overlays for Protobufs/*.proto (single-file format)
│   └── cs_gameevents.yml
└── <module>.yml         ← multi-entity overlays for any schema module
```

---

## Overlay formats

### Multi-entity format *(recommended)*

Place a single `<module>.yml` file in this directory.  Top-level keys are
entity (class / struct / enum) names; their values are the per-entity overlay
dicts.  This lets you document many entities in one file.

```yaml
# docs/overlays/server.yml
CCSPlayerController:
  description: >
    One-line or multi-line description of what this entity represents.
  notes: >
    Reverse-engineered notes, lifecycle behaviour, quirks, etc.
  warning: >
    Optional – shown in an amber box.
  fields:
    m_iPing:
      description: "Player ping in milliseconds."
      notes: "Updated approximately every 5 seconds."
    m_hPlayerPawn:
      description: "Handle to the player's active pawn entity."

CBaseEntity:
  description: "Base class for all server-side entities."
```

Supported modules follow the directory names under `DumpSource2/schemas/`
(e.g. `server`, `client`, `entity2`, `animgraphlib`, …) plus `protobufs`
for Protobuf files.

A few module-level files use the same physical layout but a different
top-level shape because their downstream generator wants the file as a
unit:

- `gameevents.yml` — top-level `events:` mapping of `<event_name>:` →
  overlay dict, applied to `gameevents_schema.json`.
- `well_known_constants.yml` — top-level `constants:` list, projected
  into `well_known_constants.json`.

The loader treats these the same as ordinary module files but also
keeps the raw file dict accessible under the bare module key, so the
relevant generator can pull the whole thing in one read.

### Single-entity format *(legacy)*

One file per entity, placed in a subdirectory named after the module:

```
docs/overlays/<module>/<EntityName>.yml
```

The file content is the overlay dict directly (no top-level entity key).

```yaml
# docs/overlays/server/CCSPlayerController.yml  ← legacy path
description: >
  One-line or multi-line description of what this entity represents.
fields:
  m_iPing:
    description: "Player ping in milliseconds."
```

Both formats can coexist.  If the same entity key appears in both, the
single-entity file wins.

---

## Protobuf file overlays

For Protobuf files, use the stem of the `.proto` filename as the key:

```yaml
# docs/overlays/protobufs/cs_gameevents.yml  (single-file format)
description: "CS2-specific game event messages."

messages:
  CMsgTEFireBullets:
    description: "Temporary entity event broadcast when a player fires a weapon."
    notes: "Seed allows demo parsers to reproduce bullet spread."
    fields:
      seed:
        description: "PRNG seed used to reproduce the bullet spread trajectory."
      weapon_id:
        description: "Item definition index of the weapon fired."
```

Or use the multi-entity format in a single `protobufs.yml` file:

```yaml
# docs/overlays/protobufs.yml
cs_gameevents:
  description: "CS2-specific game event messages."
  messages:
    CMsgTEFireBullets:
      description: "Broadcast when a player fires."
```

---

## Game events overlays

For game events (from `.gameevents` files), use a file named `gameevents.yml`
in this directory.  Top-level keys are `description`, `notes`, and `events`.
Under `events`, each key is an event name; its value supports `description`,
`notes`, `warning`, and per-field annotations under `fields`:

```yaml
# docs/overlays/gameevents.yml
description: >
  Optional page-level description shown at the top of the Game Events page.
notes: >
  Optional page-level notes callout.
events:
  player_death:
    description: "Fired when a player is killed."
    notes: "This event extends the base engine player_death with CS2-specific fields."
    fields:
      headshot:
        description: "Whether the killing blow was a headshot."
      weapon:
        description: "Weapon classname used by the attacker."
        notes: "Does not include the 'weapon_' prefix."
  round_end:
    description: "Fired when a round ends."
    warning: "The 'reason' field uses CS-specific enum values not documented here."
```

---

## Contributing

1. **Fork** the repository and create a branch.
2. Add or edit a YAML file under `docs/overlays/`.
3. Open a pull request with a clear description of the information you are adding.

Please prefer **factual, source-cited** information from:
- Official Valve developer documentation
- AlliedModders / HL2SDK headers
- HLAE source code
- Your own verified reverse-engineering work

Speculation is fine but should be labelled as such (e.g. *"likely used for …"*).
