---
title: VMixDynamicsBand_t
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixDynamicsBand_t

# VMixDynamicsBand_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 36 bytes (`0x24`) · **Align:** 4 · **Module:** soundsystem_lowlevel

## Memory layout

10 fields (10 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_fldbGainInput` | float32 |  | `MPropertyFriendlyName Input Gain (dB)` |
| `0x4` | `m_fldbGainOutput` | float32 |  | `MPropertyFriendlyName Output Gain (dB)` |
| `0x8` | `m_fldbThresholdBelow` | float32 |  | `MPropertyFriendlyName Below Threshold(dB)` |
| `0xc` | `m_fldbThresholdAbove` | float32 |  | `MPropertyFriendlyName Above Threshold(dB)` |
| `0x10` | `m_flRatioBelow` | float32 |  | `MPropertyFriendlyName Upward Ratio` |
| `0x14` | `m_flRatioAbove` | float32 |  | `MPropertyFriendlyName Downward Ratio` |
| `0x18` | `m_flAttackTimeMS` | float32 |  | `MPropertyFriendlyName Attack time (ms)` |
| `0x1c` | `m_flReleaseTimeMS` | float32 |  | `MPropertyFriendlyName Release time (ms)` |
| `0x20` | `m_bEnable` | bool |  | `MPropertyFriendlyName Enabled` |
| `0x21` | `m_bSolo` | bool |  | `MPropertyFriendlyName Solo` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_fldbGainInput&quot;: 0.000000,
	&quot;m_fldbGainOutput&quot;: 0.000000,
	&quot;m_fldbThresholdBelow&quot;: -40.000000,
	&quot;m_fldbThresholdAbove&quot;: -30.000000,
	&quot;m_flRatioBelow&quot;: 12.000000,
	&quot;m_flRatioAbove&quot;: 4.000000,
	&quot;m_flAttackTimeMS&quot;: 50.000000,
	&quot;m_flReleaseTimeMS&quot;: 200.000000,
	&quot;m_bEnable&quot;: false,
	&quot;m_bSolo&quot;: false
}</pre>
</details>
