---
layout: default
title: Entity Hierarchy
parent: Schemas
nav_exclude: true
---

# Entity Hierarchy Diagram

Inheritance relationships between server and client entities (capped at 300 edges for readability).

```mermaid
classDiagram
    C_BaseModelEntity <|-- CBaseAnimGraph
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    CEntityInstance <|-- C_BaseEntity
    C_BaseEntity <|-- C_BaseModelEntity
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
    C_CSPlayerPawnBase <|-- C_CSPlayerPawn
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    CBaseAnimGraph <|-- CBaseCombatCharacter
    CEntityInstance <|-- CBaseEntity
    CBaseEntity <|-- CBaseModelEntity
    CBaseCombatCharacter <|-- CBasePlayerPawn
    CCSPlayerPawnBase <|-- CCSPlayerPawn
    CBasePlayerPawn <|-- CCSPlayerPawnBase
```
