---
title: CNmSkeleton
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmSkeleton

# CNmSkeleton

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 256 bytes (`0x100`) · **Align:** 8 · **Module:** animlib

**Relationships:**

```mermaid
classDiagram
    CNmSkeleton *-- NmBoneMaskSetDefinition_t
    CNmSkeleton *-- `CNmSkeleton::SecondarySkeleton_t`
    CNmSkeleton *-- CNmFloatChannelSet_t
    CNmSkeleton *-- `CNmSkeleton::ContactConfig_t`
```

## Memory layout

13 fields (13 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_ID` | CGlobalSymbol |  |  |
| `0x8` | `m_boneIDs` | CUtlLeanVector< CGlobalSymbol > |  |  |
| `0x18` | `m_parentIndices` | CUtlVector< int32 > |  |  |
| `0x30` | `m_parentSpaceReferencePose` | CUtlVector< CTransform > |  |  |
| `0x48` | `m_modelSpaceReferencePose` | CUtlVector< CTransform > |  |  |
| `0x60` | `m_numBonesToSampleAtLowLOD` | int32 |  |  |
| `0x64` | `m_bIsPropSkeleton` | bool |  |  |
| `0x88` | `m_maskDefinitions` | CUtlLeanVector< [NmBoneMaskSetDefinition_t](../animlib/NmBoneMaskSetDefinition_t.md) > |  |  |
| `0xa8` | `m_secondarySkeletons` | CUtlLeanVector< [CNmSkeleton::SecondarySkeleton_t](../animlib/CNmSkeleton.SecondarySkeleton_t.md) > |  |  |
| `0xb8` | `m_floatChannelSets` | CUtlLeanVector< [CNmFloatChannelSet_t](../animlib/CNmFloatChannelSet_t.md) > |  |  |
| `0xc8` | `m_contactConfigs` | CUtlVector< [CNmSkeleton::ContactConfig_t](../animlib/CNmSkeleton.ContactConfig_t.md) > |  |  |
| `0xe0` | `m_gameplayRelevantBoneIndices` | CUtlVector< int32 > |  |  |
| `0xf8` | `m_nSpecialDependencyHash` | int64 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
	&quot;m_boneIDs&quot;:
	[
	],
	&quot;m_parentIndices&quot;:
	[
	],
	&quot;m_parentSpaceReferencePose&quot;:
	[
	],
	&quot;m_modelSpaceReferencePose&quot;:
	[
	],
	&quot;m_numBonesToSampleAtLowLOD&quot;: 0,
	&quot;m_bIsPropSkeleton&quot;: false,
	&quot;m_maskDefinitions&quot;:
	[
	],
	&quot;m_secondarySkeletons&quot;:
	[
	],
	&quot;m_floatChannelSets&quot;:
	[
	],
	&quot;m_contactConfigs&quot;:
	[
	],
	&quot;m_gameplayRelevantBoneIndices&quot;:
	[
	],
	&quot;m_nSpecialDependencyHash&quot;: 0
}</pre>
</details>
