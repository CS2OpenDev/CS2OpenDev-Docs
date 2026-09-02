---
title: CVMixConvolutionProcessorDesc
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixConvolutionProcessorDesc

# CVMixConvolutionProcessorDesc

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Inherits from:** [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md)

**Relationships:**

```mermaid
classDiagram
    CVMixBaseProcessorDesc <|-- CVMixConvolutionProcessorDesc
    CVMixConvolutionProcessorDesc *-- VMixConvolutionDesc_t
```

## Memory layout

4 fields (1 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x14` | `m_nChannels` | int32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x18` | `m_flxfade` | float32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x20` | `m_desc` | [VMixConvolutionDesc_t](../soundsystem_lowlevel/VMixConvolutionDesc_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVMixConvolutionProcessorDesc&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_nChannels&quot;: -1,
	&quot;m_flxfade&quot;: 0.100000,
	&quot;m_desc&quot;:
	{
		&quot;m_fldbGain&quot;: -12.000000,
		&quot;m_flPreDelayMS&quot;: 0.000000,
		&quot;m_flWetMix&quot;: 1.000000,
		&quot;m_fldbLow&quot;: 0.000000,
		&quot;m_fldbMid&quot;: 0.000000,
		&quot;m_fldbHigh&quot;: 0.000000,
		&quot;m_flLowCutoffFreq&quot;: 1500.000000,
		&quot;m_flHighCutoffFreq&quot;: 7500.000000
	}
}</pre>
</details>
