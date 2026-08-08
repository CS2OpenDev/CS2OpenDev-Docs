---
layout: default
title: CPulseServerCursor
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseServerCursor

# CPulseServerCursor

**Kind:** class · **Size:** 240 bytes (`0xf0`) · **Align:** 255 · **Module:** server

**Inherits from:** [CPulseExecCursor](../pulse_runtime_lib/CPulseExecCursor.md)

**Relationships:**

```mermaid
classDiagram
    CPulseExecCursor <|-- CPulseServerCursor
    CPulseServerCursor --> CBaseEntity
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0xe8` | `m_hActivator` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0xec` | `m_hCaller` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
