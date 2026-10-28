---
title: CVMixDescription
module: soundsystem
kind: class
---

[Schemas](../../schemas.md) / [soundsystem](../soundsystem.md) / CVMixDescription

# CVMixDescription

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 272 bytes (`0x110`) · **Align:** 8 · **Module:** soundsystem

**Inherits from:** [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md)

**Relationships:**

```mermaid
classDiagram
    CVMixBaseGraphDescription <|-- CVMixDescription
    CVMixDescription *-- CSubmix
    CVMixDescription *-- CVoiceContainerBase
```

## Memory layout

19 fields (4 declared here, 15 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) | `MKV3TransferName Name` |
| `0x8` | `m_nGraphOutputChannels` | int32 | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0xc` | `m_bIsMainGraph` | bool | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0x10` | `m_processorNodes` | CUtlLeanVector< std::unique_ptr< [CVMixBaseProcessorDesc](../soundsystem_lowlevel/CVMixBaseProcessorDesc.md) > > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) | `MKV3TransferName m_Processors` |
| `0x20` | `m_graphInputs` | CUtlLeanVector< [CVMixGraphInput](../soundsystem_lowlevel/CVMixGraphInput.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0x30` | `m_controlTransientInputs` | CUtlLeanVector< [CVMixControlInput](../soundsystem_lowlevel/CVMixControlInput.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0x40` | `m_controlOutputs` | CUtlLeanVector< [CVMixControlOutput](../soundsystem_lowlevel/CVMixControlOutput.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0x50` | `m_impulseResponseInputs` | CUtlLeanVector< [CVMixImpulseResponseInput](../soundsystem_lowlevel/CVMixImpulseResponseInput.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0x60` | `m_mixCommands` | CUtlLeanVector< [CVMixCommand](../soundsystem_lowlevel/CVMixCommand.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) | `MKV3TransferName m_MixCommands` |
| `0x70` | `m_heap` | [CVMixHeap](../soundsystem_lowlevel/CVMixHeap.md) | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0x80` | `m_audioMeters` | CUtlLeanVector< [CVMixAudioMeter](../soundsystem_lowlevel/CVMixAudioMeter.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0x90` | `m_controlMeters` | CUtlLeanVector< [CVMixControlMeter](../soundsystem_lowlevel/CVMixControlMeter.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0xa0` | `m_nameInputMeters` | CUtlLeanVector< [CVMixNameInputMeter](../soundsystem_lowlevel/CVMixNameInputMeter.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0xb0` | `m_additionalOutputs` | CUtlLeanVector< [CVMixAdditionalOutput](../soundsystem_lowlevel/CVMixAdditionalOutput.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0xc0` | `m_automaticControlInputs` | CUtlLeanVector< [CVMixAutomaticControlInput](../soundsystem_lowlevel/CVMixAutomaticControlInput.md) > | [CVMixBaseGraphDescription](../soundsystem_lowlevel/CVMixBaseGraphDescription.md) |  |
| `0xd0` | `m_submixList` | CUtlLeanVector< [CSubmix](../soundsystem/CSubmix.md) > |  | `MKV3TransferName m_Submixes` |
| `0xe0` | `m_sources` | CUtlLeanVector< std::unique_ptr< [CVoiceContainerBase](../soundsystem_voicecontainers/CVoiceContainerBase.md) > > |  |  |
| `0xf0` | `m_impulseResponseValues` | CUtlLeanVector< uint64 > |  |  |
| `0x100` | `m_nNameHashCode` | uint32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;Name&quot;: &quot;&quot;,
	&quot;m_nGraphOutputChannels&quot;: -1,
	&quot;m_bIsMainGraph&quot;: false,
	&quot;m_Processors&quot;:
	[
	],
	&quot;m_graphInputs&quot;:
	[
	],
	&quot;m_controlTransientInputs&quot;:
	[
	],
	&quot;m_controlOutputs&quot;:
	[
	],
	&quot;m_impulseResponseInputs&quot;:
	[
	],
	&quot;m_MixCommands&quot;:
	[
	],
	&quot;m_heap&quot;:
	{
		&quot;m_storage&quot;:
		[
		]
	},
	&quot;m_audioMeters&quot;:
	[
	],
	&quot;m_controlMeters&quot;:
	[
	],
	&quot;m_nameInputMeters&quot;:
	[
	],
	&quot;m_additionalOutputs&quot;:
	[
	],
	&quot;m_automaticControlInputs&quot;:
	[
	],
	&quot;m_Submixes&quot;:
	[
	],
	&quot;m_sources&quot;:
	[
	],
	&quot;m_impulseResponseValues&quot;:
	[
	],
	&quot;m_nNameHashCode&quot;: 0
}</pre>
</details>
