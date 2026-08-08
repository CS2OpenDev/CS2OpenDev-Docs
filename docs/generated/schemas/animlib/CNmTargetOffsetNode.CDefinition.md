---
layout: default
title: "CNmTargetOffsetNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTargetOffsetNode::CDefinition

# CNmTargetOffsetNode::CDefinition

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 16 · **Module:** animlib

**Inherits from:** [CNmTargetValueNode::CDefinition](../animlib/CNmTargetValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmTargetValueNode::CDefinition" <|-- "CNmTargetOffsetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

5 fields (4 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x12` | `m_bIsBoneSpaceOffset` | bool |  |  |
| `0x20` | `m_rotationOffset` | Quaternion |  |  |
| `0x30` | `m_translationOffset` | Vector |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmTargetOffsetNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_bIsBoneSpaceOffset&quot;: true,
	&quot;m_rotationOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_translationOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	]
}</pre>
</details>
