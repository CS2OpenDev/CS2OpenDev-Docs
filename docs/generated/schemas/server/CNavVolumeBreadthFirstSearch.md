---
layout: default
title: CNavVolumeBreadthFirstSearch
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CNavVolumeBreadthFirstSearch

# CNavVolumeBreadthFirstSearch

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

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
