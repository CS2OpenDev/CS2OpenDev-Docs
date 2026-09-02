---
title: "CNmGraphEventConditionNode::CDefinition"
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmGraphEventConditionNode::CDefinition

# CNmGraphEventConditionNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoolValueNode::CDefinition](../animlib/CNmBoolValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmBoolValueNode::CDefinition` <|-- `CNmGraphEventConditionNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmBoolValueNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
    `CNmGraphEventConditionNode::CDefinition` *-- CNmBitFlags
    `CNmGraphEventConditionNode::CDefinition` *-- `CNmGraphEventConditionNode::Condition_t`
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nSourceStateNodeIdx` | int16 |  |  |
| `0x14` | `m_eventConditionRules` | [CNmBitFlags](../animlib/CNmBitFlags.md) |  |  |
| `0x18` | `m_conditions` | CUtlVectorFixedGrowable< [CNmGraphEventConditionNode::Condition_t](../animlib/CNmGraphEventConditionNode.Condition_t.md), 5 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmGraphEventConditionNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nSourceStateNodeIdx&quot;: -1,
	&quot;m_eventConditionRules&quot;:
	{
		&quot;m_flags&quot;: 0
	},
	&quot;m_conditions&quot;:
	[
	]
}</pre>
</details>
