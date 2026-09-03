---
title: CFootstepLandedAnimTag
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CFootstepLandedAnimTag

# CFootstepLandedAnimTag

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CAnimTagBase](../animgraphlib/CAnimTagBase.md)

**Metadata:** `MPropertyFriendlyName FootstepLanded Tag`

**Relationships:**

```mermaid
classDiagram
    CAnimTagBase <|-- CFootstepLandedAnimTag
    CFootstepLandedAnimTag *-- FootstepLandedFootSoundType_t
    CFootstepLandedAnimTag *-- FootstepJumpPhase_t
```

## Memory layout

10 fields (5 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_name` | CGlobalSymbol | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |
| `0x20` | `m_sComment` | CUtlString | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertyAttributeEditor TextBlock()` `MPropertyFriendlyName Comment` `MPropertySortPriority -100` |
| `0x28` | `m_group` | CGlobalSymbol | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertySuppressField` |
| `0x30` | `m_tagID` | [AnimTagID](../modellib/AnimTagID.md) | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertySuppressField` |
| `0x48` | `m_bIsReferenced` | bool | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertySuppressField` |
| `0x58` | `m_FootstepType` | [FootstepLandedFootSoundType_t](../animgraphlib/FootstepLandedFootSoundType_t.md) |  | `MPropertyFriendlyName Footstep Type` |
| `0x60` | `m_OverrideSoundName` | CUtlString |  | `MPropertyAttributeChoiceName Sound` `MPropertyFriendlyName Override Sound` |
| `0x68` | `m_DebugAnimSourceString` | CUtlString |  | `MPropertyFriendlyName Debug Name` |
| `0x70` | `m_BoneName` | CUtlString |  | `MPropertyAttributeChoiceName Bone` `MPropertyFriendlyName Bone Name` |
| `0x78` | `m_footstepJumpPhase` | [FootstepJumpPhase_t](../animgraphlib/FootstepJumpPhase_t.md) |  | `MPropertyFriendlyName Jump Phase` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CFootstepLandedAnimTag&quot;,
	&quot;m_name&quot;: &quot;Unnamed Tag&quot;,
	&quot;m_sComment&quot;: &quot;&quot;,
	&quot;m_group&quot;: &quot;&quot;,
	&quot;m_tagID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bIsReferenced&quot;: false,
	&quot;m_FootstepType&quot;: &quot;FOOTSOUND_Left&quot;,
	&quot;m_OverrideSoundName&quot;: &quot;&quot;,
	&quot;m_DebugAnimSourceString&quot;: &quot;&quot;,
	&quot;m_BoneName&quot;: &quot;&quot;,
	&quot;m_footstepJumpPhase&quot;: &quot;Unknown&quot;
}</pre>
</details>
