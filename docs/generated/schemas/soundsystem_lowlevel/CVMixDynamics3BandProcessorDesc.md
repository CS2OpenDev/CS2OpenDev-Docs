---
title: CVMixDynamics3BandProcessorDesc
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixDynamics3BandProcessorDesc

# CVMixDynamics3BandProcessorDesc

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 184 bytes (`0xb8`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Inherits from:** [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md)

**Relationships:**

```mermaid
classDiagram
    CVMixBaseProcessorDesc <|-- CVMixDynamics3BandProcessorDesc
    CVMixDynamics3BandProcessorDesc *-- VMixDynamics3BandDesc_t
```

## Memory layout

8 fields (1 declared here, 7 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x10` | `m_nDebugId` | uint32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x14` | `m_flxfade` | float32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x18` | `m_nChannels` | int32 | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x1c` | `m_bDebugBypass` | bool | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x20` | `m_paramEnable` | [CVMixParameterFloat](../soundsystem_lowlevel/CVMixParameterFloat.md) | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x24` | `m_paramMix` | [CVMixParameterFloat](../soundsystem_lowlevel/CVMixParameterFloat.md) | [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |  |
| `0x28` | `m_desc` | [VMixDynamics3BandDesc_t](../soundsystem_lowlevel/VMixDynamics3BandDesc_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVMixDynamics3BandProcessorDesc&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_nDebugId&quot;: 0,
	&quot;m_flxfade&quot;: 0.100000,
	&quot;m_nChannels&quot;: -1,
	&quot;m_bDebugBypass&quot;: false,
	&quot;m_paramEnable&quot;:
	{
		&quot;m_offset&quot;:
		{
			&quot;category&quot;: &quot;NULL_POINTER&quot;,
			&quot;type&quot;: &quot;VO_CHAR&quot;,
			&quot;index&quot;: 0
		}
	},
	&quot;m_paramMix&quot;:
	{
		&quot;m_offset&quot;:
		{
			&quot;category&quot;: &quot;NULL_POINTER&quot;,
			&quot;type&quot;: &quot;VO_CHAR&quot;,
			&quot;index&quot;: 0
		}
	},
	&quot;m_desc&quot;:
	{
		&quot;m_fldbGainOutput&quot;: 0.000000,
		&quot;m_flRMSTimeMS&quot;: 0.000000,
		&quot;m_fldbKneeWidth&quot;: 0.000000,
		&quot;m_flDepth&quot;: 0.000000,
		&quot;m_flWetMix&quot;: 0.000000,
		&quot;m_flTimeScale&quot;: 0.000000,
		&quot;m_flLowCutoffFreq&quot;: 0.000000,
		&quot;m_flHighCutoffFreq&quot;: 0.000000,
		&quot;m_bPeakMode&quot;: false,
		&quot;m_bandDesc&quot;:
		[
			{
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
			},
			{
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
			},
			{
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
			}
		]
	}
}</pre>
</details>
