---
layout: default
title: CVoiceContainerLoopTrigger
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_voicecontainers](../soundsystem_voicecontainers.md) / CVoiceContainerLoopTrigger

# CVoiceContainerLoopTrigger

**Kind:** class · **Size:** 160 bytes (`0xa0`) · **Align:** 8 · **Module:** soundsystem_voicecontainers

**Inherits from:** [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md)

**Derived by:** [CVoiceContainerLoopTriggerWithRandomPanner](../soundsystem_voicecontainers/CVoiceContainerLoopTriggerWithRandomPanner.md)

**Metadata:** `MPropertyDescription Continuously retriggers a sound and optionally fades to the new instance.`, `MPropertyFriendlyName LoopTrigger`

**Relationships:**

```mermaid
classDiagram
    CVoiceContainerBase <|-- CVoiceContainerLoopTrigger
    CVoiceContainerLoopTrigger <|-- CVoiceContainerLoopTriggerWithRandomPanner
    CVoiceContainerLoopTrigger *-- CSoundContainerReference
```

## Memory layout

7 fields (5 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x28` | `m_vSound` | [CVSound](../soundsystem_voicecontainers/CVSound.md) | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) | `MPropertySuppressField` |
| `0x68` | `m_pEnvelopeAnalyzer` | [CVoiceContainerAnalysisBase](../soundsystem_voicecontainers/CVoiceContainerAnalysisBase.md)* | [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) | `MPropertySuppressExpr true` |
| `0x70` | `m_flRetriggerTimeMin` | float32 |  |  |
| `0x74` | `m_flRetriggerTimeMax` | float32 |  |  |
| `0x78` | `m_flFadeTime` | float32 |  |  |
| `0x7c` | `m_bCrossFade` | bool |  |  |
| `0x80` | `m_sound` | [CSoundContainerReference](../soundsystem_voicecontainers/CSoundContainerReference.md) |  | `MPropertyFriendlyName Vsnd Reference` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CVoiceContainerLoopTrigger&quot;,
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
	&quot;m_flRetriggerTimeMin&quot;: 1.000000,
	&quot;m_flRetriggerTimeMax&quot;: 1.000000,
	&quot;m_flFadeTime&quot;: 0.500000,
	&quot;m_bCrossFade&quot;: false,
	&quot;m_sound&quot;:
	{
		&quot;m_namespace&quot;: &quot;&quot;,
		&quot;m_bUseReference&quot;: true,
		&quot;m_sound&quot;: &quot;&quot;,
		&quot;m_pSound&quot;: null
	}
}</pre>
</details>
