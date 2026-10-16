---
title: CPulseGraphInstance_GameBlackboard
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseGraphInstance_GameBlackboard

# CPulseGraphInstance_GameBlackboard

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 336 bytes (`0x150`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md)

**Relationships:**

```mermaid
classDiagram
    CPulseGraphInstance_ServerEntity <|-- CPulseGraphInstance_GameBlackboard
    CBasePulseGraphInstance <|-- CPulseGraphInstance_ServerEntity
```

## Memory layout

6 fields (0 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x118` | `m_hOwner` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md) |  |
| `0x11c` | `m_bActivated` | bool | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md) |  |
| `0x120` | `m_sNameFixupStaticPrefix` | CUtlSymbolLarge | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md) |  |
| `0x128` | `m_sNameFixupParent` | CUtlSymbolLarge | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md) |  |
| `0x130` | `m_sNameFixupLocal` | CUtlSymbolLarge | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md) |  |
| `0x138` | `m_sProceduralWorldNameForRelays` | CUtlSymbolLarge | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md) |  |
