---
layout: default
title: CAnimGraphDoc_NodeManager
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_NodeManager

# CAnimGraphDoc_NodeManager

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** animgraphdoclib

**Derived by:** [CAnimGraphDoc_MotionNodeManager](../animgraphdoclib/CAnimGraphDoc_MotionNodeManager.md)

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_NodeManager <|-- CAnimGraphDoc_MotionNodeManager
    CAnimGraphDoc_NodeManager *-- AnimNodeID
    CAnimGraphDoc_NodeManager *-- CAnimGraphDoc_Node
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nodes` | CUtlHashtable< [AnimNodeID](../modellib/AnimNodeID.md), CSmartPtr< [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) > > |  | `MPropertySuppressField` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_NodeManager&quot;,
	&quot;m_nodes&quot;:
	[
	]
}</pre>
</details>
