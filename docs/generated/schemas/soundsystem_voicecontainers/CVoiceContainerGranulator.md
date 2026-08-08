---
layout: default
title: CVoiceContainerGranulator
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_voicecontainers](../soundsystem_voicecontainers.md) / CVoiceContainerGranulator

# CVoiceContainerGranulator

**Kind:** class · **Size:** 344 bytes (`0x158`) · **Align:** 8 · **Module:** soundsystem_voicecontainers

**Inherits from:** [CVoiceContainerAsyncGenerator](../soundsystem_voicecontainers/CVoiceContainerAsyncGenerator.md)

**Metadata:** `MPropertyFriendlyName Granulator Container`

**Relationships:**

```mermaid
classDiagram
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerGranulator
    CVoiceContainerGenerator <|-- CVoiceContainerAsyncGenerator
    CVoiceContainerBase <|-- CVoiceContainerGenerator
    CVoiceContainerGranulator *-- InfoForResourceTypeCVoiceContainerBase
```

## Memory layout

8 fields (6 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x28` | `m_vSound` | [CVSound](../soundsystem_voicecontainers/CVSound.md) | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) | `MPropertySuppressField` |
| `0x68` | `m_pEnvelopeAnalyzer` | [CVoiceContainerAnalysisBase](../soundsystem_voicecontainers/CVoiceContainerAnalysisBase.md)* | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) | `MPropertySuppressExpr true` |
| `0x80` | `m_flGrainLength` | float32 |  |  |
| `0x84` | `m_flGrainCrossfadeAmount` | float32 |  |  |
| `0x88` | `m_flStartJitter` | float32 |  |  |
| `0x8c` | `m_flPlaybackJitter` | float32 |  |  |
| `0x90` | `m_bShouldWraparound` | bool |  |  |
| `0x98` | `m_sourceAudio` | CStrongHandle< [InfoForResourceTypeCVoiceContainerBase](../resourcesystem/InfoForResourceTypeCVoiceContainerBase.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVoiceContainerGranulator&quot;,
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
	&quot;m_flGrainLength&quot;: 0.100000,
	&quot;m_flGrainCrossfadeAmount&quot;: 0.100000,
	&quot;m_flStartJitter&quot;: 0.000000,
	&quot;m_flPlaybackJitter&quot;: 0.000000,
	&quot;m_bShouldWraparound&quot;: false,
	&quot;m_sourceAudio&quot;: &quot;&quot;
}</pre>
</details>
