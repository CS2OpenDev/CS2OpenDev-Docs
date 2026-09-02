---
layout: default
title: VMixShaperDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixShaperDesc_t

# VMixShaperDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 20 bytes (`0x14`) · **Align:** 4 · **Module:** soundsystem_lowlevel

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nShape` | int32 |  | `MPropertyAttributeRange 0 14` `MPropertyFriendlyName Shape` |
| `0x4` | `m_fldbDrive` | float32 |  | `MPropertyAttributeRange 0 36` `MPropertyFriendlyName Drive (dB)` |
| `0x8` | `m_fldbOutputGain` | float32 |  | `MPropertyAttributeRange -36 0` `MPropertyFriendlyName Output Gain (dB)` |
| `0xc` | `m_flWetMix` | float32 |  | `MPropertyFriendlyName Dry/Wet` |
| `0x10` | `m_nOversampleFactor` | int32 |  | `MPropertyFriendlyName Oversampling` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nShape&quot;: 0,
	&quot;m_fldbDrive&quot;: 0.000000,
	&quot;m_fldbOutputGain&quot;: 0.000000,
	&quot;m_flWetMix&quot;: 1.000000,
	&quot;m_nOversampleFactor&quot;: 1
}</pre>
</details>
