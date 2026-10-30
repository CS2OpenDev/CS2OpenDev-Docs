---
title: CVoiceContainerShapedNoise
module: soundsystem_voicecontainers
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_voicecontainers](../soundsystem_voicecontainers.md) / CVoiceContainerShapedNoise

# CVoiceContainerShapedNoise

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 336 bytes (`0x150`) · **Align:** 8 · **Module:** soundsystem_voicecontainers

**Inherits from:** [CVoiceContainerGenerator](../soundsystem_voicecontainers/CVoiceContainerGenerator.md)

**Metadata:** `MPropertyDescription This is a synth meant to generate whoosh noises.`, `MPropertyFriendlyName Wind Generator Container`

**Relationships:**

```mermaid
classDiagram
    CVoiceContainerGenerator <|-- CVoiceContainerShapedNoise
    CVoiceContainerBase <|-- CVoiceContainerGenerator
```

## Memory layout

13 fields (9 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_bRegisteredVMix` | bool | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) |  |
| `0x14` | `m_nResourceName` | CUtlStringToken | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) |  |
| `0x30` | `m_vSound` | [CVSound](../soundsystem_voicecontainers/CVSound.md) | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) | `MPropertySuppressField` |
| `0x70` | `m_pEnvelopeAnalyzer` | [CVoiceContainerAnalysisBase](../soundsystem_voicecontainers/CVoiceContainerAnalysisBase.md)* | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) | `MPropertySuppressExpr true` |
| `0x78` | `m_bUseCurveForFrequency` | bool |  |  |
| `0x7c` | `m_flFrequency` | float32 |  | `MPropertySuppressExpr m_bUseCurveForFrequency == 1` |
| `0x80` | `m_frequencySweep` | CPiecewiseCurve |  | `MPropertyFriendlyName Frequency Sweep` `MPropertySuppressExpr m_bUseCurveForFrequency == 0` |
| `0xc0` | `m_bUseCurveForResonance` | bool |  |  |
| `0xc4` | `m_flResonance` | float32 |  | `MPropertySuppressExpr m_bUseCurveForResonance == 1` |
| `0xc8` | `m_resonanceSweep` | CPiecewiseCurve |  | `MPropertyFriendlyName Resonance Sweep` `MPropertySuppressExpr m_bUseCurveForResonance == 0` |
| `0x108` | `m_bUseCurveForAmplitude` | bool |  |  |
| `0x10c` | `m_flGainInDecibels` | float32 |  | `MPropertySuppressExpr m_bUseCurveForAmplitude == 1` |
| `0x110` | `m_gainSweep` | CPiecewiseCurve |  | `MPropertyFriendlyName Gain Sweep (in Decibels)` `MPropertySuppressExpr m_bUseCurveForAmplitude == 0` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVoiceContainerShapedNoise&quot;,
	&quot;m_bRegisteredVMix&quot;: false,
	&quot;m_nResourceName&quot;: &quot;&quot;,
	&quot;m_vSound&quot;:
	{
		&quot;m_Sentences&quot;:
		[
		],
		&quot;m_nRate&quot;: 0,
		&quot;m_nFormat&quot;: &quot;PCM16&quot;,
		&quot;m_nChannels&quot;: 0,
		&quot;m_nLoopStart&quot;: 0,
		&quot;m_nSampleCount&quot;: 0,
		&quot;m_flDuration&quot;: 0.000000,
		&quot;m_nStreamingSize&quot;: 0,
		&quot;m_nLoopEnd&quot;: 0
	},
	&quot;m_pEnvelopeAnalyzer&quot;: null,
	&quot;m_bUseCurveForFrequency&quot;: false,
	&quot;m_flFrequency&quot;: 440.000000,
	&quot;m_frequencySweep&quot;:
	{
		&quot;m_spline&quot;:
		[
		],
		&quot;m_tangents&quot;:
		[
		],
		&quot;m_vDomainMins&quot;:
		[
			0.000000,
			0.000000
		],
		&quot;m_vDomainMaxs&quot;:
		[
			0.000000,
			0.000000
		]
	},
	&quot;m_bUseCurveForResonance&quot;: false,
	&quot;m_flResonance&quot;: 4.000000,
	&quot;m_resonanceSweep&quot;:
	{
		&quot;m_spline&quot;:
		[
		],
		&quot;m_tangents&quot;:
		[
		],
		&quot;m_vDomainMins&quot;:
		[
			0.000000,
			0.000000
		],
		&quot;m_vDomainMaxs&quot;:
		[
			0.000000,
			0.000000
		]
	},
	&quot;m_bUseCurveForAmplitude&quot;: false,
	&quot;m_flGainInDecibels&quot;: 1.000000,
	&quot;m_gainSweep&quot;:
	{
		&quot;m_spline&quot;:
		[
		],
		&quot;m_tangents&quot;:
		[
		],
		&quot;m_vDomainMins&quot;:
		[
			0.000000,
			0.000000
		],
		&quot;m_vDomainMaxs&quot;:
		[
			0.000000,
			0.000000
		]
	}
}</pre>
</details>
