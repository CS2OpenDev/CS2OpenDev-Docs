---
layout: default
title: CVMixDynamicsProcessorDesc
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixDynamicsProcessorDesc

# CVMixDynamicsProcessorDesc

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Inherits from:** [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md)

**Relationships:**

```mermaid
classDiagram
    CVMixBaseProcessorDesc <|-- CVMixDynamicsProcessorDesc
    CVMixDynamicsProcessorDesc *-- VMixDynamicsDesc_t
```

## Memory layout

4 fields (1 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x14` | `m_nChannels` | int32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x18` | `m_flxfade` | float32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x20` | `m_desc` | [VMixDynamicsDesc_t](../soundsystem_lowlevel/VMixDynamicsDesc_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVMixDynamicsProcessorDesc&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_nChannels&quot;: -1,
	&quot;m_flxfade&quot;: 0.100000,
	&quot;m_desc&quot;:
	{
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
	}
}</pre>
</details>
