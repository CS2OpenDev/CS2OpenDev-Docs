---
layout: default
title: VMixDynamicsCompressorDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixDynamicsCompressorDesc_t

# VMixDynamicsCompressorDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 36 bytes (`0x24`) · **Align:** 4 · **Module:** soundsystem_lowlevel

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_fldbOutputGain` | float32 |  | `MPropertyFriendlyName Output Gain (dB)` |
| `0x4` | `m_fldbCompressionThreshold` | float32 |  | `MPropertyFriendlyName Threshold (dB)` |
| `0x8` | `m_fldbKneeWidth` | float32 |  | `MPropertyFriendlyName Knee Width (dB)` |
| `0xc` | `m_flCompressionRatio` | float32 |  | `MPropertyFriendlyName Compression Ratio` |
| `0x10` | `m_flAttackTimeMS` | float32 |  | `MPropertyFriendlyName Attack time (ms)` |
| `0x14` | `m_flReleaseTimeMS` | float32 |  | `MPropertyFriendlyName Release time (ms)` |
| `0x18` | `m_flRMSTimeMS` | float32 |  | `MPropertyFriendlyName Threshold detection time (ms)` |
| `0x1c` | `m_flWetMix` | float32 |  | `MPropertyFriendlyName Dry/Wet` |
| `0x20` | `m_bPeakMode` | bool |  | `MPropertyFriendlyName Peak mode` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_fldbOutputGain&quot;: 0.000000,
	&quot;m_fldbCompressionThreshold&quot;: -6.000000,
	&quot;m_fldbKneeWidth&quot;: 0.000000,
	&quot;m_flCompressionRatio&quot;: 2.000000,
	&quot;m_flAttackTimeMS&quot;: 100.000000,
	&quot;m_flReleaseTimeMS&quot;: 400.000000,
	&quot;m_flRMSTimeMS&quot;: 300.000000,
	&quot;m_flWetMix&quot;: 1.000000,
	&quot;m_bPeakMode&quot;: false
}</pre>
</details>
