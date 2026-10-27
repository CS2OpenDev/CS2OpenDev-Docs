---
title: CPulseGraphInstance_ServerEntity
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseGraphInstance_ServerEntity

# CPulseGraphInstance_ServerEntity

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 320 bytes (`0x140`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CBasePulseGraphInstance](../pulse_runtime_lib/CBasePulseGraphInstance.md)

**Derived by:** [CPulseGraphInstance_GameBlackboard](../server/CPulseGraphInstance_GameBlackboard.md)

**Relationships:**

```mermaid
classDiagram
    CBasePulseGraphInstance <|-- CPulseGraphInstance_ServerEntity
    CPulseGraphInstance_ServerEntity <|-- CPulseGraphInstance_GameBlackboard
    CPulseGraphInstance_ServerEntity --> CBaseEntity
```

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x118` | `m_hOwner` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x11c` | `m_bActivated` | bool |  |  |
| `0x120` | `m_sNameFixupStaticPrefix` | CUtlSymbolLarge |  |  |
| `0x128` | `m_sNameFixupParent` | CUtlSymbolLarge |  |  |
| `0x130` | `m_sNameFixupLocal` | CUtlSymbolLarge |  |  |
| `0x138` | `m_sProceduralWorldNameForRelays` | CUtlSymbolLarge |  |  |
