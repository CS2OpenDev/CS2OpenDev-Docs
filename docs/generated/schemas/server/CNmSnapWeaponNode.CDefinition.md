---
layout: default
title: "CNmSnapWeaponNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CNmSnapWeaponNode::CDefinition

# CNmSnapWeaponNode::CDefinition

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** server

**Inherits from:** [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmSnapWeaponNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

## Memory layout

5 fields (3 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nChildNodeIdx` | int16 | [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md) |  |
| `0x18` | `m_nFlashedAmountNodeIdx` | int16 |  |  |
| `0x1a` | `m_nWeaponCategoryNodeIdx` | int16 |  |  |
| `0x1c` | `m_nWeaponTypeNodeIdx` | int16 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmSnapWeaponNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nChildNodeIdx&quot;: -1,
	&quot;m_nFlashedAmountNodeIdx&quot;: -1,
	&quot;m_nWeaponCategoryNodeIdx&quot;: -1,
	&quot;m_nWeaponTypeNodeIdx&quot;: -1
}</pre>
</details>
