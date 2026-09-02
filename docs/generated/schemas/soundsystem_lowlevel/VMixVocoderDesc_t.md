---
layout: default
title: VMixVocoderDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixVocoderDesc_t

# VMixVocoderDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 4 · **Module:** soundsystem_lowlevel

## Memory layout

10 fields (10 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nBandCount` | int32 |  |  |
| `0x4` | `m_flBandwidth` | float32 |  |  |
| `0x8` | `m_fldBModGain` | float32 |  |  |
| `0xc` | `m_flFreqRangeStart` | float32 |  |  |
| `0x10` | `m_flFreqRangeEnd` | float32 |  |  |
| `0x14` | `m_fldBUnvoicedGain` | float32 |  |  |
| `0x18` | `m_flAttackTimeMS` | float32 |  |  |
| `0x1c` | `m_flReleaseTimeMS` | float32 |  |  |
| `0x20` | `m_nDebugBand` | int32 |  |  |
| `0x24` | `m_bPeakMode` | bool |  |  |
