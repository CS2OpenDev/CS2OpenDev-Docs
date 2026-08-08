---
layout: default
title: CAnimAttachment
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CAnimAttachment

# CAnimAttachment

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 16 · **Module:** modellib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_influenceRotations` | Quaternion[3] |  |  |
| `0x30` | `m_influenceOffsets` | VectorAligned[3] |  |  |
| `0x60` | `m_influenceIndices` | int32[3] |  |  |
| `0x6c` | `m_influenceWeights` | float32[3] |  |  |
| `0x78` | `m_numInfluences` | uint8 |  |  |
