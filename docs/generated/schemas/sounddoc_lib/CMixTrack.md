---
title: CMixTrack
module: sounddoc_lib
kind: class
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CMixTrack

# CMixTrack

> Source: **Build 25947352** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** sounddoc_lib

**Inherits from:** [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md)

**Metadata:** `MPropertyDescription This node creates a track.Voices can be played on a track.  This is the source of audio for your graph.`, `MPropertyFriendlyName VMix Track Node`

**Relationships:**

```mermaid
classDiagram
    CMixPropertyBase <|-- CMixTrack
    CMixTrack *-- VMixMixDownRule_t
    CMixTrack *-- VMixSendOperator_t
```

## Memory layout

10 fields (4 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Node name` `MPropertyFriendlyName Name` `MPropertySortPriority 1` |
| `0x10` | `m_Comment` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Description of how this is used  the graph for people reading the graph` `MPropertySortPriority -2` |
| `0x18` | `m_bActive` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x19` | `m_bSolo` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x1a` | `m_bEditProperties` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x1c` | `m_nGenerationId` | int32 | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x20` | `m_nChannels` | int32 |  | `MPropertyAttributeChoiceName channel_count` `MPropertyDescription Leave this as "Automatic" unless you are forcing mono/stereo for some reason.  That way each graph will get configured to match the incoming vsnd (for a voice graph) or the audio device (main mix graph)` |
| `0x24` | `m_nMixDown` | [VMixMixDownRule_t](../soundsystem_lowlevel/VMixMixDownRule_t.md) |  | `MPropertyDescription This determines what happens when your incoming audio doesn't match the channel count for the track.  e.g. for a mono track, this is the rule for what happens to stereo audio` `MPropertyFriendlyName Mix Down Rule` |
| `0x26` | `m_nSendOperator` | [VMixSendOperator_t](../soundsystem_lowlevel/VMixSendOperator_t.md) |  | `MPropertyDescription This refers to a piece of code in the sound engine that will select specific child voices to be mixed into this track and at what mix level each voice will be mixed.<br>If you want to drive that with data, choose "By Named Send" and author a list of send names for this track.  Then any sound event can send to one of those names and the audio will be mixed here.` `MPropertyFriendlyName Send Child Voices` `MPropertyGroupName Child Voices` |
| `0x28` | `m_SendNames` | CUtlString[4] |  | `MPropertyFriendlyName Send Names` `MPropertyGroupName Child Voices` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMixTrack&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_Comment&quot;: &quot;&quot;,
	&quot;m_bActive&quot;: true,
	&quot;m_bSolo&quot;: false,
	&quot;m_bEditProperties&quot;: false,
	&quot;m_nGenerationId&quot;: 0,
	&quot;m_nChannels&quot;: -1,
	&quot;m_nMixDown&quot;: &quot;SUM&quot;,
	&quot;m_nSendOperator&quot;: &quot;NAMED_SEND&quot;,
	&quot;m_SendNames&quot;:
	[
		&quot;&quot;,
		&quot;&quot;,
		&quot;&quot;,
		&quot;&quot;
	]
}</pre>
</details>
