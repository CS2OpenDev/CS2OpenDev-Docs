---
title: CNavVolumeBreadthFirstSearch
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CNavVolumeBreadthFirstSearch

# CNavVolumeBreadthFirstSearch

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 192 bytes (`0xc0`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CNavVolumeCalculatedVector](../server/CNavVolumeCalculatedVector.md)

**Relationships:**

```mermaid
classDiagram
    CNavVolumeCalculatedVector <|-- CNavVolumeBreadthFirstSearch
    CNavVolume <|-- CNavVolumeCalculatedVector
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0xa8` | `m_vStartPos` | VectorWS |  |  |
| `0xb4` | `m_flSearchDist` | float32 |  |  |
