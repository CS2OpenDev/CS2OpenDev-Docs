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

Module names follow SchemaTracker's `projectName` grouping, which is also the
directory name under `docs/generated/schemas/`.  Build 25000182 has 47 of them:

```
animationsystem  animdoclib  animgraphdoclib  animgraphlib  animlib  client
compositematerialslib  engine2  entity2  hammer  host  mapdoclib
materialsystem2  mathlib_extended  met  modeldoc_editor  modellib  modtools
navlib  networksystem  panorama_content  particles  particleslib  physicslib
pulse_runtime_lib  pulse_system  pulsedoc_lib  qcontrols  rendersystemdx11
resourcecompiler  resourcefile  resourcesystem  scenesystem  schemasystem
server  smartprops  sounddoc_lib  soundsystem  soundsystem_lowlevel
soundsystem_voicecontainers  steamaudio  texturelib  tier2  toolscene
toolutils2  vphysics2  worldrenderer
```

plus `protobufs` for Protobuf files.  There is no `globaltypes` module: every
enum now carries a `projectName`, so shared enums such as `SolidType_t` and
`MoveType_t` are filed under `server.yml` alongside the classes that use
them.  Run the generator with `--strict` to be told which of your keys do
not match this build.

Overlays are matched on `<module>/<name>` first and then by name alone across
every module, so a key filed under the wrong module still renders. It would
attach to an unrelated class of the same name if one appeared, and the
generator prints it as a `MODULE` advisory, so prefer the real module.

For the 189 client/server twins (`CCSPlayerController` in `server`,
`C_CSPlayerController` and `CCSPlayerController` in `client`) the name-only
fallback means one entry annotates both variants.  That is right when the
prose is about the concept and wrong when the twins differ in field set or
offsets; file the key under the module you actually verified.

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

### Enum member annotations

An enum uses the same `fields:` key as a class; each key is a member name and
its `description` / `notes` land in the Description column of the enum's
Values table and in the `annotations` block of that member in
`cs2_schema.json`.

```yaml
# docs/overlays/server.yml
SolidType_t:
  description: "Collision representation used by CCollisionProperty."
  fields:
    SOLID_VPHYSICS:
      description: "Collide against the VPhysics representation."
    SOLID_BBOX:
      description: "Axis-aligned bounding box."
      notes: "Cheapest solid type; used by most brush entities."
```

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

## Checking your overlay

The generator validates every overlay key against the build it is rendering.
It always prints what did not resolve; `--strict` turns that into a non-zero
exit so a typo fails the run instead of vanishing from the site:

```bash
python3 docs/generate_docs.py --repo-root . \
  --artifacts-root ./upstream/schema-tracker/artifacts --build latest \
  --platform windows-x86_64 --output /tmp/docs-check --strict
```

Two kinds of report come out of it:

- `UNRESOLVED`: the class, enum, field, proto message, proto field or game
  event does not exist in this build.  The nearest existing name is printed
  alongside.  These fail under `--strict`.
- `MODULE`: the name exists but not in the module the key is filed under.
  It still renders through the name-only fallback; fix the module anyway.

A YAML syntax error is fatal with or without `--strict`: the file and the
parse error are printed and the run exits 2, so a bad edit can no longer
delete a whole module's annotations silently.

## Contributing

1. **Fork** the repository and create a branch.
2. Add or edit a YAML file under `docs/overlays/`.
3. Run the generator with `--strict` and fix anything it reports.
4. Open a pull request with a clear description of the information you are adding.

Please prefer **factual, source-cited** information from:
- Official Valve developer documentation
- AlliedModders / HL2SDK headers
- HLAE source code
- Your own verified reverse-engineering work

Speculation is fine but should be labelled as such (e.g. *"likely used for …"*).
