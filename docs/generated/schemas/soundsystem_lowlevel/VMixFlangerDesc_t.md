---
layout: default
title: VMixFlangerDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixFlangerDesc_t

# VMixFlangerDesc_t

**Kind:** class · **Size:** 36 bytes (`0x24`) · **Align:** 4 · **Module:** soundsystem_lowlevel

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bPhaseInvert` | bool |  |  |
| `0x4` | `m_flGlideTime` | float32 |  |  |
| `0x8` | `m_flDelay` | float32 |  |  |
| `0xc` | `m_flOutputGain` | float32 |  |  |
| `0x10` | `m_flFeedbackGain` | float32 |  |  |
| `0x14` | `m_flFeedforwardGain` | float32 |  |  |
| `0x18` | `m_flModRate` | float32 |  |  |
| `0x1c` | `m_flModDepth` | float32 |  |  |
| `0x20` | `m_bApplyAntialiasing` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_bPhaseInvert&quot;: false,
	&quot;m_flGlideTime&quot;: 0.000000,
	&quot;m_flDelay&quot;: 0.000000,
	&quot;m_flOutputGain&quot;: 0.000000,
	&quot;m_flFeedbackGain&quot;: 0.000000,
	&quot;m_flFeedforwardGain&quot;: 0.000000,
	&quot;m_flModRate&quot;: 0.000000,
	&quot;m_flModDepth&quot;: 0.000000,
	&quot;m_bApplyAntialiasing&quot;: false
}</pre>
</details>
