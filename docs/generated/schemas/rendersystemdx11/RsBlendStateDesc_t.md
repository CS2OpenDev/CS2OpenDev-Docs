---
layout: default
title: RsBlendStateDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [rendersystemdx11](../rendersystemdx11.md) / RsBlendStateDesc_t

# RsBlendStateDesc_t

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 255 · **Module:** rendersystemdx11

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bAlphaToCoverageEnable` | bitfield:1 |  |  |
| `0x0` | `m_bIndependentBlendEnable` | bitfield:1 |  |  |
| `0x0` | `m_blendOpBits` | bitfield:30 |  |  |
| `0x0` | `m_srcBlendBits` | uint32 |  |  |
| `0x4` | `m_destBlendBits` | uint32 |  |  |
| `0x8` | `m_srcBlendAlphaBits` | uint32 |  |  |
| `0xc` | `m_destBlendAlphaBits` | uint32 |  |  |
| `0x10` | `m_renderTargetWriteMaskBits` | uint32 |  |  |
| `0x18` | `m_blendOpAlphaBits` | uint32 |  |  |
| `0x1c` | `m_blendEnableBits` | uint8 |  |  |
| `0x1d` | `m_srgbWriteEnableBits` | uint8 |  |  |
