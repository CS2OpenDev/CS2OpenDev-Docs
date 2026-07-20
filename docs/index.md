---
layout: home
title: CS2 Developer Reference
nav_order: 1
nav_exclude: true
---

# CS2 Developer Reference

Auto-generated reference for the **shipped CS2 runtime**, extracted deterministically from the game binaries by [CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker): entity schemas, protobuf wire messages, network/demo message tables, game events, console variables & commands, and the game-content tables (items, game modes, surfaces, props, maps).

{: .note }
> Source: CS2 build **24134959** · 2026-07-09 · `windows-x86_64` · schema `0.4.0`

## Statistics

| Category | Count |
|----------|-------|
| Schema Entities | 1079 |
| Proto Files | 32 |
| Proto Messages | 497 |
| Game Events | 195 |
| ConVars | 3354 |
| Commands | 841 |

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

[animationsystem](generated/schemas/animationsystem.md) (4)  [animgraphlib](generated/schemas/animgraphlib.md) (1)  [client](generated/schemas/client.md) (463)  [entity2](generated/schemas/entity2.md) (4)  [particleslib](generated/schemas/particleslib.md) (2)  [pulse_runtime_lib](generated/schemas/pulse_runtime_lib.md) (66)  [server](generated/schemas/server.md) (724)
