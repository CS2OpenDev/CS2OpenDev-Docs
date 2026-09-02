---
title: CVMixDynamicsCompressorProcessorDesc
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixDynamicsCompressorProcessorDesc

# CVMixDynamicsCompressorProcessorDesc

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Inherits from:** [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md)

**Relationships:**

```mermaid
classDiagram
    CVMixBaseProcessorDesc <|-- CVMixDynamicsCompressorProcessorDesc
    CVMixDynamicsCompressorProcessorDesc *-- VMixDynamicsCompressorDesc_t
```

## Memory layout

4 fields (1 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x14` | `m_nChannels` | int32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x18` | `m_flxfade` | float32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x20` | `m_desc` | [VMixDynamicsCompressorDesc_t](../soundsystem_lowlevel/VMixDynamicsCompressorDesc_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVMixDynamicsCompressorProcessorDesc&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_nChannels&quot;: -1,
	&quot;m_flxfade&quot;: 0.100000,
	&quot;m_desc&quot;:
	{
		&quot;m_fldbOutputGain&quot;: 0.000000,
		&quot;m_fldbCompressionThreshold&quot;: -6.000000,
		&quot;m_fldbKneeWidth&quot;: 0.000000,
		&quot;m_flCompressionRatio&quot;: 2.000000,
		&quot;m_flAttackTimeMS&quot;: 100.000000,
		&quot;m_flReleaseTimeMS&quot;: 400.000000,
		&quot;m_flRMSTimeMS&quot;: 300.000000,
		&quot;m_flWetMix&quot;: 1.000000,
		&quot;m_bPeakMode&quot;: false
	}
}</pre>
</details>
