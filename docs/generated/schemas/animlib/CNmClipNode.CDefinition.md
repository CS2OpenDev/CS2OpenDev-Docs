---
layout: default
title: "CNmClipNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmClipNode::CDefinition

# CNmClipNode::CDefinition

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmClipReferenceNode::CDefinition](../animlib/CNmClipReferenceNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmClipReferenceNode::CDefinition" <|-- "CNmClipNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

## Memory layout

9 fields (8 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nPlayInReverseValueNodeIdx` | int16 |  |  |
| `0x12` | `m_nResetTimeValueNodeIdx` | int16 |  |  |
| `0x14` | `m_bSampleRootMotion` | bool |  |  |
| `0x15` | `m_bAllowLooping` | bool |  |  |
| `0x16` | `m_nDataSlotIdx` | int16 |  |  |
| `0x18` | `m_graphEvents` | CUtlVectorFixedGrowable< CGlobalSymbol, 2 > |  |  |
| `0x40` | `m_flSpeedMultiplier` | float32 |  |  |
| `0x44` | `m_nStartSyncEventOffset` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmClipNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nPlayInReverseValueNodeIdx&quot;: -1,
	&quot;m_nResetTimeValueNodeIdx&quot;: -1,
	&quot;m_bSampleRootMotion&quot;: true,
	&quot;m_bAllowLooping&quot;: false,
	&quot;m_nDataSlotIdx&quot;: -1,
	&quot;m_graphEvents&quot;:
	[
	],
	&quot;m_flSpeedMultiplier&quot;: 1.000000,
	&quot;m_nStartSyncEventOffset&quot;: 0
}</pre>
</details>
