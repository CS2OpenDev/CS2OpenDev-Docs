---
title: client
module: client
---

# Module: client

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/client.md)

8 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CBaseAnimGraph](client/CBaseAnimGraph.md) | class | 4480 | 17 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [CGameSceneNode](client/CGameSceneNode.md) | class | 304 | 34 |  |
| [C_BaseCombatCharacter](client/C_BaseCombatCharacter.md) | class | 4616 | 6 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_BaseEntity](client/C_BaseEntity.md) | class | 1536 | 82 | [CEntityInstance](entity2/CEntityInstance.md) |
| [C_BaseModelEntity](client/C_BaseModelEntity.md) | class | 4016 | 44 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_BasePlayerPawn](client/C_BasePlayerPawn.md) | class | 5088 | 28 | [C_BaseCombatCharacter](client/C_BaseCombatCharacter.md) |
| [C_CSPlayerPawn](client/C_CSPlayerPawn.md) | class | 13424 | 102 | [C_CSPlayerPawnBase](client/C_CSPlayerPawnBase.md) |
| [C_CSPlayerPawnBase](client/C_CSPlayerPawnBase.md) | class | 5248 | 26 | [C_BasePlayerPawn](client/C_BasePlayerPawn.md) |
