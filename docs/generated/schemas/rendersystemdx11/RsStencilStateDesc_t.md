---
layout: default
title: RsStencilStateDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [rendersystemdx11](../rendersystemdx11.md) / RsStencilStateDesc_t

# RsStencilStateDesc_t

**Kind:** class · **Size:** 6 bytes (`0x6`) · **Align:** 255 · **Module:** rendersystemdx11

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bStencilEnable` | bitfield:1 |  |  |
| `0x0` | `m_backStencilDepthFailOp` | bitfield:3 |  |  |
| `0x0` | `m_backStencilFailOp` | bitfield:3 |  |  |
| `0x0` | `m_backStencilFunc` | bitfield:4 |  |  |
| `0x0` | `m_backStencilPassOp` | bitfield:3 |  |  |
| `0x0` | `m_frontStencilDepthFailOp` | bitfield:3 |  |  |
| `0x0` | `m_frontStencilFailOp` | bitfield:3 |  |  |
| `0x0` | `m_frontStencilFunc` | bitfield:4 |  |  |
| `0x0` | `m_frontStencilPassOp` | bitfield:3 |  |  |
| `0x4` | `m_nStencilReadMask` | uint8 |  |  |
| `0x5` | `m_nStencilWriteMask` | uint8 |  |  |
