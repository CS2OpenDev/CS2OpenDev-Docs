---
layout: default
title: "CNmSyncEventIndexConditionNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmSyncEventIndexConditionNode::CDefinition

# CNmSyncEventIndexConditionNode::CDefinition

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoolValueNode::CDefinition](../animlib/CNmBoolValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmSyncEventIndexConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nSourceStateNodeIdx` | int16 |  |  |
| `0x12` | `m_triggerMode` | CNmSyncEventIndexConditionNode::TriggerMode_t |  |  |
| `0x14` | `m_syncEventIdx` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmSyncEventIndexConditionNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nSourceStateNodeIdx&quot;: -1,
	&quot;m_triggerMode&quot;: &quot;ExactlyAtEventIndex&quot;,
	&quot;m_syncEventIdx&quot;: -1
}</pre>
</details>
