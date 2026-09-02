---
layout: default
title: "CNmTimeConditionNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTimeConditionNode::CDefinition

# CNmTimeConditionNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoolValueNode::CDefinition](../animlib/CNmBoolValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmBoolValueNode::CDefinition` <|-- `CNmTimeConditionNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmBoolValueNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
    `CNmTimeConditionNode::CDefinition` *-- `CNmTimeConditionNode::ComparisonType_t`
    `CNmTimeConditionNode::CDefinition` *-- `CNmTimeConditionNode::Operator_t`
```

## Memory layout

6 fields (5 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_sourceStateNodeIdx` | int16 |  |  |
| `0x12` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x14` | `m_flComparand` | float32 |  |  |
| `0x18` | `m_type` | [CNmTimeConditionNode::ComparisonType_t](../animlib/CNmTimeConditionNode.ComparisonType_t.md) |  |  |
| `0x19` | `m_operator` | [CNmTimeConditionNode::Operator_t](../animlib/CNmTimeConditionNode.Operator_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmTimeConditionNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_sourceStateNodeIdx&quot;: -1,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_flComparand&quot;: 0.000000,
	&quot;m_type&quot;: &quot;ElapsedTime&quot;,
	&quot;m_operator&quot;: &quot;LessThan&quot;
}</pre>
</details>
