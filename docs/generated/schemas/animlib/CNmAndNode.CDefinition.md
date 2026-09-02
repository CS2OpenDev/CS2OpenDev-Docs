---
layout: default
title: "CNmAndNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmAndNode::CDefinition

# CNmAndNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoolValueNode::CDefinition](../animlib/CNmBoolValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmBoolValueNode::CDefinition` <|-- `CNmAndNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmBoolValueNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 4 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmAndNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_conditionNodeIndices&quot;:
	[
	]
}</pre>
</details>
