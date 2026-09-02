---
layout: default
title: CVMixBoxverbProcessorDesc
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixBoxverbProcessorDesc

# CVMixBoxverbProcessorDesc

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Inherits from:** [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md)

**Relationships:**

```mermaid
classDiagram
    CVMixBaseProcessorDesc <|-- CVMixBoxverbProcessorDesc
    CVMixBoxverbProcessorDesc *-- VMixBoxverbDesc_t
```

## Memory layout

4 fields (1 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x14` | `m_nChannels` | int32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x18` | `m_flxfade` | float32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x20` | `m_desc` | [VMixBoxverbDesc_t](../soundsystem_lowlevel/VMixBoxverbDesc_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVMixBoxverbProcessorDesc&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_nChannels&quot;: -1,
	&quot;m_flxfade&quot;: 0.100000,
	&quot;m_desc&quot;:
	{
		&quot;m_flSizeMax&quot;: 0.000000,
		&quot;m_flSizeMin&quot;: 0.000000,
		&quot;m_flComplexity&quot;: 0.000000,
		&quot;m_flDiffusion&quot;: 0.000000,
		&quot;m_flModDepth&quot;: 0.000000,
		&quot;m_flModRate&quot;: 0.000000,
		&quot;m_bParallel&quot;: false,
		&quot;m_filterType&quot;:
		{
			&quot;m_nFilterType&quot;: &quot;FILTER_UNKNOWN&quot;,
			&quot;m_nFilterSlope&quot;: &quot;FILTER_SLOPE_12dB&quot;,
			&quot;m_bEnabled&quot;: true,
			&quot;m_fldbGain&quot;: 0.000000,
			&quot;m_flCutoffFreq&quot;: 1000.000000,
			&quot;m_flQ&quot;: 0.707107
		},
		&quot;m_flWidth&quot;: 0.000000,
		&quot;m_flHeight&quot;: 0.000000,
		&quot;m_flDepth&quot;: 0.000000,
		&quot;m_flFeedbackScale&quot;: 0.000000,
		&quot;m_flFeedbackWidth&quot;: 0.000000,
		&quot;m_flFeedbackHeight&quot;: 0.000000,
		&quot;m_flFeedbackDepth&quot;: 0.000000,
		&quot;m_flOutputGain&quot;: 0.000000,
		&quot;m_flTaps&quot;: 0.000000
	}
}</pre>
</details>
