---
layout: home
title: CS2 Developer Reference
nav_order: 1
nav_exclude: true
---

# CS2 Developer Reference

Auto-generated reference for the **shipped CS2 runtime**, extracted deterministically from the game binaries by [CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker): entity schemas, protobuf wire messages, network/demo message tables, game events, console variables & commands, and the game-content tables (items, game modes, surfaces, props, maps).

{: .note }
> Source: CS2 build **24304127** · 2026-07-20 · `windows-x86_64` · schema `0.5.0`

## Statistics

| Category | Count |
|----------|-------|
| Schema Entities | 4194 |
| Proto Files | 40 |
| Proto Messages | 762 |
| Game Events | 289 |
| ConVars | 3954 |
| Commands | 1132 |

## Quick Links

- [Schema Entities](generated/schemas.md) – Classes, structs, and enums from CS2's runtime schema ([codegen schema](generated/downstream-codegen-schemas/cs2_schema.json))
- [Protobufs](generated/protobufs.md) – Network message and game event definitions
- [Game Events](generated/gameevents.md) – Game event definitions with field schemas ([codegen schema](generated/downstream-codegen-schemas/gameevents_schema.json))
- [ConVars](generated/convars.md) – Console variable reference with flags and defaults ([codegen schema](generated/downstream-codegen-schemas/convars_schema.json))
- [Commands](generated/commands.md) – Console command reference ([codegen schema](generated/downstream-codegen-schemas/commands_schema.json))
- [Items & Economy](generated/items.md)
- [Network Messages](generated/network.md)
- [Game Modes](generated/gamemodes.md)
- [Changelog](generated/changelog.md)
- [Maps](generated/maps.md)
- [Surface Properties](generated/surfaces.md)
- [Prop Data](generated/props.md)
- [Modules](generated/modules.md)
- [Well-Known Constants](generated/downstream-codegen-schemas/well_known_constants.json) – Curated tables for team numbers, game phase, weapon state, etc.
- [Codegen schemas index](generated/downstream-codegen-schemas/README.md) – Format reference, type vocabulary, and version policy for all five JSON schemas above
- [Entity Hierarchy Diagram](generated/diagrams/server_hierarchy.md) – UML inheritance diagram for server & client entities

## Schema Modules

[!GlobalTypes](generated/schemas/!GlobalTypes.md) (591)  [animationsystem](generated/schemas/animationsystem.md) (51)  [animdoclib](generated/schemas/animdoclib.md) (197)  [animgraphdoclib](generated/schemas/animgraphdoclib.md) (158)  [animgraphlib](generated/schemas/animgraphlib.md) (243)  [animlib](generated/schemas/animlib.md) (180)  [client](generated/schemas/client.md) (484)  [compositematerialslib](generated/schemas/compositematerialslib.md) (10)  [engine2](generated/schemas/engine2.md) (42)  [entity2](generated/schemas/entity2.md) (16)  [hammer](generated/schemas/hammer.md) (7)  [host](generated/schemas/host.md) (2)  [mapdoclib](generated/schemas/mapdoclib.md) (3)  [materialsystem2](generated/schemas/materialsystem2.md) (15)  [mathlib_extended](generated/schemas/mathlib_extended.md) (11)  [met](generated/schemas/met.md) (3)  [modeldoc_editor](generated/schemas/modeldoc_editor.md) (3)  [modellib](generated/schemas/modellib.md) (114)  [modtools](generated/schemas/modtools.md) (2)  [navlib](generated/schemas/navlib.md) (14)  [networksystem](generated/schemas/networksystem.md) (1)  [particles](generated/schemas/particles.md) (434)  [particleslib](generated/schemas/particleslib.md) (21)  [physicslib](generated/schemas/physicslib.md) (99)  [pulse_runtime_lib](generated/schemas/pulse_runtime_lib.md) (98)  [pulse_system](generated/schemas/pulse_system.md) (42)  [pulsedoc_lib](generated/schemas/pulsedoc_lib.md) (3)  [rendersystemdx11](generated/schemas/rendersystemdx11.md) (4)  [resourcecompiler](generated/schemas/resourcecompiler.md) (17)  [resourcefile](generated/schemas/resourcefile.md) (6)  [resourcesystem](generated/schemas/resourcesystem.md) (48)  [scenesystem](generated/schemas/scenesystem.md) (9)  [schemasystem](generated/schemas/schemasystem.md) (1)  [server](generated/schemas/server.md) (914)  [smartprops](generated/schemas/smartprops.md) (149)  [sounddoc_lib](generated/schemas/sounddoc_lib.md) (139)  [soundsystem](generated/schemas/soundsystem.md) (35)  [soundsystem_lowlevel](generated/schemas/soundsystem_lowlevel.md) (73)  [soundsystem_voicecontainers](generated/schemas/soundsystem_voicecontainers.md) (42)  [steamaudio](generated/schemas/steamaudio.md) (17)  [texturelib](generated/schemas/texturelib.md) (4)  [tier2](generated/schemas/tier2.md) (2)  [toolscene](generated/schemas/toolscene.md) (11)  [toolutils2](generated/schemas/toolutils2.md) (21)  [vphysics2](generated/schemas/vphysics2.md) (14)  [worldrenderer](generated/schemas/worldrenderer.md) (29)
