---
layout: default
title: "CnmGraphDocFollowBoneNode::CData"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CnmGraphDocFollowBoneNode::CData

# CnmGraphDocFollowBoneNode::CData

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animdoclib

**Inherits from:** [CNmGraphDocVariationDataNode::CData](../animdoclib/CNmGraphDocVariationDataNode.CData.md)

**Relationships:**

```mermaid
classDiagram
    "CNmGraphDocVariationDataNode::CData" <|-- "CnmGraphDocFollowBoneNode::CData"
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_boneName` | CUtlString |  |  |
| `0x10` | `m_followTargetBoneName` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CnmGraphDocFollowBoneNode::CData&quot;,
	&quot;m_boneName&quot;: &quot;&quot;,
	&quot;m_followTargetBoneName&quot;: &quot;&quot;
}</pre>
</details>
