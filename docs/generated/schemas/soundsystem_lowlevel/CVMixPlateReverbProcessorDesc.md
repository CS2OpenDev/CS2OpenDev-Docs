---
title: CVMixPlateReverbProcessorDesc
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixPlateReverbProcessorDesc

# CVMixPlateReverbProcessorDesc

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Inherits from:** [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md)

**Relationships:**

```mermaid
classDiagram
    CVMixBaseProcessorDesc <|-- CVMixPlateReverbProcessorDesc
    CVMixPlateReverbProcessorDesc *-- VMixPlateverbDesc_t
```

## Memory layout

4 fields (1 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x14` | `m_nChannels` | int32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x18` | `m_flxfade` | float32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x20` | `m_desc` | [VMixPlateverbDesc_t](../soundsystem_lowlevel/VMixPlateverbDesc_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVMixPlateReverbProcessorDesc&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_nChannels&quot;: -1,
	&quot;m_flxfade&quot;: 0.100000,
	&quot;m_desc&quot;:
	{
		&quot;m_flPrefilter&quot;: 0.000000,
		&quot;m_flInputDiffusion1&quot;: 0.000000,
		&quot;m_flInputDiffusion2&quot;: 0.000000,
		&quot;m_flDecay&quot;: 0.000000,
		&quot;m_flDamp&quot;: 0.000000,
		&quot;m_flFeedbackDiffusion1&quot;: 0.000000,
		&quot;m_flFeedbackDiffusion2&quot;: 0.000000
	}
}</pre>
</details>
