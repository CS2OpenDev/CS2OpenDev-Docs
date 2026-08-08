---
layout: default
title: "CnmGraphDocFootIKNode::CData"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CnmGraphDocFootIKNode::CData

# CnmGraphDocFootIKNode::CData

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animdoclib

**Inherits from:** [CNmGraphDocVariationDataNode::CData](../animdoclib/CNmGraphDocVariationDataNode.CData.md)

**Relationships:**

```mermaid
classDiagram
    "CNmGraphDocVariationDataNode::CData" <|-- "CnmGraphDocFootIKNode::CData"
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_leftEffectorBoneName` | CUtlString |  |  |
| `0x10` | `m_rightEffectorBoneName` | CUtlString |  |  |
| `0x18` | `m_flBlendTimeSeconds` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CnmGraphDocFootIKNode::CData&quot;,
	&quot;m_leftEffectorBoneName&quot;: &quot;&quot;,
	&quot;m_rightEffectorBoneName&quot;: &quot;&quot;,
	&quot;m_flBlendTimeSeconds&quot;: 0.000000
}</pre>
</details>
