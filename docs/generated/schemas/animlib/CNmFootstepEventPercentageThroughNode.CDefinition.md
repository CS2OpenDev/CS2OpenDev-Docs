---
layout: default
title: "CNmFootstepEventPercentageThroughNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFootstepEventPercentageThroughNode::CDefinition

# CNmFootstepEventPercentageThroughNode::CDefinition

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmFloatValueNode::CDefinition](../animlib/CNmFloatValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFootstepEventPercentageThroughNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFootstepEventPercentageThroughNode::CDefinition" *-- NmFootPhaseCondition_t
    "CNmFootstepEventPercentageThroughNode::CDefinition" *-- CNmBitFlags
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nSourceStateNodeIdx` | int16 |  |  |
| `0x12` | `m_phaseCondition` | [NmFootPhaseCondition_t](../!GlobalTypes/NmFootPhaseCondition_t.md) |  |  |
| `0x14` | `m_eventConditionRules` | [CNmBitFlags](../animlib/CNmBitFlags.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFootstepEventPercentageThroughNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nSourceStateNodeIdx&quot;: -1,
	&quot;m_phaseCondition&quot;: &quot;LeftFootDown&quot;,
	&quot;m_eventConditionRules&quot;:
	{
		&quot;m_flags&quot;: 0
	}
}</pre>
</details>
