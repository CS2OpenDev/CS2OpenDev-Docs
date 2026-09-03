---
title: CAnimConflictBase
module: animgraphdoclib
kind: class
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimConflictBase

# CAnimConflictBase

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** n/a (unspecified) · **Module:** animgraphdoclib

**Derived by:** [CAnimParameterConflict](../animgraphdoclib/CAnimParameterConflict.md), [CAnimTagConflict](../animgraphdoclib/CAnimTagConflict.md)

**Relationships:**

```mermaid
classDiagram
    CAnimConflictBase <|-- CAnimParameterConflict
    CAnimConflictBase <|-- CAnimTagConflict
    CAnimConflictBase *-- CAnimConflictInfo_t
    CAnimConflictBase *-- AnimConflictType_t
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_sConflictDesc` | CUtlString |  |  |
| `0x20` | `m_nResolveIdx` | int32 |  |  |
| `0x28` | `m_conflictData` | [CAnimConflictInfo_t](../animgraphdoclib/CAnimConflictInfo_t.md)[2] |  |  |
| `0x68` | `m_eConflictType` | [AnimConflictType_t](../animgraphdoclib/AnimConflictType_t.md) |  |  |
