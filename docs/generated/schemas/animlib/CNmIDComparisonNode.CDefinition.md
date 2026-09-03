---
title: "CNmIDComparisonNode::CDefinition"
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmIDComparisonNode::CDefinition

# CNmIDComparisonNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoolValueNode::CDefinition](../animlib/CNmBoolValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmBoolValueNode::CDefinition` <|-- `CNmIDComparisonNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmBoolValueNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
    `CNmIDComparisonNode::CDefinition` *-- `CNmIDComparisonNode::Comparison_t`
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x12` | `m_comparison` | [CNmIDComparisonNode::Comparison_t](../animlib/CNmIDComparisonNode.Comparison_t.md) |  |  |
| `0x18` | `m_comparisionIDs` | CUtlLeanVectorFixedGrowable< CGlobalSymbol, 4 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmIDComparisonNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_comparison&quot;: &quot;Matches&quot;,
	&quot;m_comparisionIDs&quot;:
	[
	]
}</pre>
</details>
