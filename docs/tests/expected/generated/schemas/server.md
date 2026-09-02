---
layout: default
title: server
parent: Schemas
nav_exclude: true
---

# Module: server

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/server.md)

12 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CBaseAnimGraph](server/CBaseAnimGraph.md) | class | 2400 | 15 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CBaseCombatCharacter](server/CBaseCombatCharacter.md) | class | 2608 | 10 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CBaseEntity](server/CBaseEntity.md) | class | 1192 | 85 | [CEntityInstance](entity2/CEntityInstance.md) |
| [CBaseModelEntity](server/CBaseModelEntity.md) | class | 1904 | 40 | [CBaseEntity](server/CBaseEntity.md) |
| [CBasePlayerPawn](server/CBasePlayerPawn.md) | class | 3040 | 25 | [CBaseCombatCharacter](server/CBaseCombatCharacter.md) |
| [CCSPlayerPawn](server/CCSPlayerPawn.md) | class | 4992 | 105 | [CCSPlayerPawnBase](server/CCSPlayerPawnBase.md) |
| [CCSPlayerPawnBase](server/CCSPlayerPawnBase.md) | class | 3376 | 15 | [CBasePlayerPawn](server/CBasePlayerPawn.md) |
| [CGameSceneNode](server/CGameSceneNode.md) | class | 272 | 31 |  |
| [BloodType](server/BloodType.md) | enum | — | 9 |  |
| [LifeState_t](server/LifeState_t.md) | enum | — | 6 |  |
| [MoveType_t](server/MoveType_t.md) | enum | — | 14 |  |
| [SolidType_t](server/SolidType_t.md) | enum | — | 10 |  |
