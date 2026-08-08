---
layout: default
title: CResponseQueue
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CResponseQueue

# CResponseQueue

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 255 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    CResponseQueue --> CAI_Expresser
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x38` | `m_ExpresserTargets` | CUtlVector< [CAI_Expresser](../server/CAI_Expresser.md)* > |  |  |
