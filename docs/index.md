---
layout: home
title: CS2 Developer Reference
nav_order: 1
nav_exclude: true
---

# CS2 Developer Reference

Auto-generated reference for the **shipped CS2 runtime**, extracted deterministically from the game binaries by [CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker): entity schemas, protobuf wire messages, network/demo message tables, game events, console variables & commands, and the game-content tables (items, game modes, surfaces, props, maps).

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

## Statistics

| Category | Count |
|----------|-------|
| Schema Entities | 4201 |
| Proto Files | 40 |
| Proto Messages | 622 |
| Game Events | 289 |
| ConVars | 3955 |
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
- [Schema History](generated/schema-history.md)
- [Well-Known Constants](generated/downstream-codegen-schemas/well_known_constants.json) – Curated tables for team numbers, game phase, weapon state, etc.
- [Codegen schemas index](generated/downstream-codegen-schemas/README.md) – Format reference, type vocabulary, and version policy for all five JSON schemas above
- [Entity Hierarchy Diagram](generated/diagrams/server_hierarchy.md) – UML inheritance diagram for server & client entities

## Schema Modules

[animationsystem](generated/schemas/animationsystem.md) (54)  [animdoclib](generated/schemas/animdoclib.md) (209)  [animgraphdoclib](generated/schemas/animgraphdoclib.md) (172)  [animgraphlib](generated/schemas/animgraphlib.md) (300)  [animlib](generated/schemas/animlib.md) (217)  [client](generated/schemas/client.md) (490)  [compositematerialslib](generated/schemas/compositematerialslib.md) (17)  [engine2](generated/schemas/engine2.md) (42)  [entity2](generated/schemas/entity2.md) (18)  [hammer](generated/schemas/hammer.md) (10)  [host](generated/schemas/host.md) (2)  [mapdoclib](generated/schemas/mapdoclib.md) (3)  [materialsystem2](generated/schemas/materialsystem2.md) (20)  [mathlib_extended](generated/schemas/mathlib_extended.md) (13)  [met](generated/schemas/met.md) (3)  [modeldoc_editor](generated/schemas/modeldoc_editor.md) (4)  [modellib](generated/schemas/modellib.md) (140)  [modtools](generated/schemas/modtools.md) (2)  [navlib](generated/schemas/navlib.md) (17)  [networksystem](generated/schemas/networksystem.md) (1)  [panorama_content](generated/schemas/panorama_content.md) (2)  [particles](generated/schemas/particles.md) (507)  [particleslib](generated/schemas/particleslib.md) (39)  [physicslib](generated/schemas/physicslib.md) (103)  [pulse_runtime_lib](generated/schemas/pulse_runtime_lib.md) (109)  [pulse_system](generated/schemas/pulse_system.md) (42)  [pulsedoc_lib](generated/schemas/pulsedoc_lib.md) (4)  [qcontrols](generated/schemas/qcontrols.md) (15)  [rendersystemdx11](generated/schemas/rendersystemdx11.md) (7)  [resourcecompiler](generated/schemas/resourcecompiler.md) (19)  [resourcefile](generated/schemas/resourcefile.md) (6)  [resourcesystem](generated/schemas/resourcesystem.md) (48)  [scenesystem](generated/schemas/scenesystem.md) (15)  [schemasystem](generated/schemas/schemasystem.md) (3)  [server](generated/schemas/server.md) (1141)  [smartprops](generated/schemas/smartprops.md) (167)  [sounddoc_lib](generated/schemas/sounddoc_lib.md) (141)  [soundsystem](generated/schemas/soundsystem.md) (48)  [soundsystem_lowlevel](generated/schemas/soundsystem_lowlevel.md) (80)  [soundsystem_voicecontainers](generated/schemas/soundsystem_voicecontainers.md) (49)  [steamaudio](generated/schemas/steamaudio.md) (17)  [texturelib](generated/schemas/texturelib.md) (10)  [tier2](generated/schemas/tier2.md) (2)  [toolscene](generated/schemas/toolscene.md) (12)  [toolutils2](generated/schemas/toolutils2.md) (23)  [vphysics2](generated/schemas/vphysics2.md) (15)  [worldrenderer](generated/schemas/worldrenderer.md) (32)
