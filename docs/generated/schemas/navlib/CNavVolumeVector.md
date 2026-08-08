---
layout: default
title: CNavVolumeVector
nav_exclude: true
---

[Schemas](../../schemas.md) / [navlib](../navlib.md) / CNavVolumeVector

# CNavVolumeVector

**Kind:** class · **Size:** 160 bytes (`0xa0`) · **Align:** 255 · **Module:** navlib

**Inherits from:** [CNavVolume](../navlib/CNavVolume.md)

**Derived by:** [CNavVolumeAll](../navlib/CNavVolumeAll.md)

**Relationships:**

```mermaid
classDiagram
    CNavVolume <|-- CNavVolumeVector
    CNavVolumeVector <|-- CNavVolumeAll
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x80` | `m_bHasBeenPreFiltered` | bool |  |  |
