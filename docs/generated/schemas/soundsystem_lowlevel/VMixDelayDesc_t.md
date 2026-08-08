---
layout: default
title: VMixDelayDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixDelayDesc_t

# VMixDelayDesc_t

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 4 · **Module:** soundsystem_lowlevel

**Relationships:**

```mermaid
classDiagram
    VMixDelayDesc_t *-- VMixFilterDesc_t
```

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_feedbackFilter` | [VMixFilterDesc_t](../soundsystem_lowlevel/VMixFilterDesc_t.md) |  |  |
| `0x10` | `m_bEnableFilter` | bool |  |  |
| `0x14` | `m_flDelay` | float32 |  |  |
| `0x18` | `m_flDirectGain` | float32 |  |  |
| `0x1c` | `m_flDelayGain` | float32 |  |  |
| `0x20` | `m_flFeedbackGain` | float32 |  |  |
| `0x24` | `m_flWidth` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_feedbackFilter&quot;:
	{
		&quot;m_nFilterType&quot;: &quot;FILTER_UNKNOWN&quot;,
		&quot;m_nFilterSlope&quot;: &quot;FILTER_SLOPE_12dB&quot;,
		&quot;m_bEnabled&quot;: true,
		&quot;m_fldbGain&quot;: 0.000000,
		&quot;m_flCutoffFreq&quot;: 1000.000000,
		&quot;m_flQ&quot;: 0.707107
	},
	&quot;m_bEnableFilter&quot;: false,
	&quot;m_flDelay&quot;: 0.000000,
	&quot;m_flDirectGain&quot;: 0.000000,
	&quot;m_flDelayGain&quot;: 0.000000,
	&quot;m_flFeedbackGain&quot;: 0.000000,
	&quot;m_flWidth&quot;: 0.000000
}</pre>
</details>
