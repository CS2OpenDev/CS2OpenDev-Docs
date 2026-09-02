---
layout: default
title: "CNmGraphDocAnimationPoseNode::CData"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmGraphDocAnimationPoseNode::CData

# CNmGraphDocAnimationPoseNode::CData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animdoclib

**Inherits from:** [CNmGraphDocVariationDataNode::CData](../animdoclib/CNmGraphDocVariationDataNode.CData.md)

**Relationships:**

```mermaid
classDiagram
    `CNmGraphDocVariationDataNode::CData` <|-- `CNmGraphDocAnimationPoseNode::CData`
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_clip` | CUtlString |  | `MPropertyAttributeEditor AssetBrowse( vnmclip, *requiredoubleclick )` |
| `0x10` | `m_variationTimeValue` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmGraphDocAnimationPoseNode::CData&quot;,
	&quot;m_clip&quot;: &quot;&quot;,
	&quot;m_variationTimeValue&quot;: -1.000000
}</pre>
</details>
