---
title: RsStencilStateDesc_t
module: rendersystemdx11
kind: class
---

[Schemas](../../schemas.md) / [rendersystemdx11](../rendersystemdx11.md) / RsStencilStateDesc_t

# RsStencilStateDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 6 bytes (`0x6`) · **Align:** n/a (unspecified) · **Module:** rendersystemdx11

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` bit 0 | `m_bStencilEnable` | bitfield:1 |  |  |
| `0x0` bits 1..3 | `m_backStencilDepthFailOp` | bitfield:3 |  |  |
| `0x0` bits 4..6 | `m_backStencilFailOp` | bitfield:3 |  |  |
| `0x0` bits 7..10 | `m_backStencilFunc` | bitfield:4 |  |  |
| `0x0` bits 11..13 | `m_backStencilPassOp` | bitfield:3 |  |  |
| `0x0` bits 14..16 | `m_frontStencilDepthFailOp` | bitfield:3 |  |  |
| `0x0` bits 17..19 | `m_frontStencilFailOp` | bitfield:3 |  |  |
| `0x0` bits 20..23 | `m_frontStencilFunc` | bitfield:4 |  |  |
| `0x0` bits 24..26 | `m_frontStencilPassOp` | bitfield:3 |  |  |
| `0x4` | `m_nStencilReadMask` | uint8 |  |  |
| `0x5` | `m_nStencilWriteMask` | uint8 |  |  |
