---
layout: default
title: VMixDynamicsDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixDynamicsDesc_t

# VMixDynamicsDesc_t

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 4 · **Module:** soundsystem_lowlevel

## Memory layout

12 fields (12 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_fldbGain` | float32 |  |  |
| `0x4` | `m_fldbNoiseGateThreshold` | float32 |  |  |
| `0x8` | `m_fldbCompressionThreshold` | float32 |  |  |
| `0xc` | `m_fldbLimiterThreshold` | float32 |  |  |
| `0x10` | `m_fldbKneeWidth` | float32 |  |  |
| `0x14` | `m_flRatio` | float32 |  |  |
| `0x18` | `m_flLimiterRatio` | float32 |  |  |
| `0x1c` | `m_flAttackTimeMS` | float32 |  |  |
| `0x20` | `m_flReleaseTimeMS` | float32 |  |  |
| `0x24` | `m_flRMSTimeMS` | float32 |  |  |
| `0x28` | `m_flWetMix` | float32 |  |  |
| `0x2c` | `m_bPeakMode` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_fldbGain&quot;: 0.000000,
	&quot;m_fldbNoiseGateThreshold&quot;: 0.000000,
	&quot;m_fldbCompressionThreshold&quot;: 0.000000,
	&quot;m_fldbLimiterThreshold&quot;: 0.000000,
	&quot;m_fldbKneeWidth&quot;: 0.000000,
	&quot;m_flRatio&quot;: 0.000000,
	&quot;m_flLimiterRatio&quot;: 0.000000,
	&quot;m_flAttackTimeMS&quot;: 0.000000,
	&quot;m_flReleaseTimeMS&quot;: 0.000000,
	&quot;m_flRMSTimeMS&quot;: 0.000000,
	&quot;m_flWetMix&quot;: 0.000000,
	&quot;m_bPeakMode&quot;: false
}</pre>
</details>
