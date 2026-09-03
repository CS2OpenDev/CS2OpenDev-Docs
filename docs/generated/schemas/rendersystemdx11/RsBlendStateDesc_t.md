---
title: RsBlendStateDesc_t
module: rendersystemdx11
kind: class
---

[Schemas](../../schemas.md) / [rendersystemdx11](../rendersystemdx11.md) / RsBlendStateDesc_t

# RsBlendStateDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** n/a (unspecified) · **Module:** rendersystemdx11

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` bit 0 | `m_bAlphaToCoverageEnable` | bitfield:1 |  |  |
| `0x0` bit 1 | `m_bIndependentBlendEnable` | bitfield:1 |  |  |
| `0x0` bits 2..31 | `m_blendOpBits` | bitfield:30 |  |  |
| `0x0` | `m_srcBlendBits` | uint32 |  |  |
| `0x4` | `m_destBlendBits` | uint32 |  |  |
| `0x8` | `m_srcBlendAlphaBits` | uint32 |  |  |
| `0xc` | `m_destBlendAlphaBits` | uint32 |  |  |
| `0x10` | `m_renderTargetWriteMaskBits` | uint32 |  |  |
| `0x18` | `m_blendOpAlphaBits` | uint32 |  |  |
| `0x1c` | `m_blendEnableBits` | uint8 |  |  |
| `0x1d` | `m_srgbWriteEnableBits` | uint8 |  |  |
