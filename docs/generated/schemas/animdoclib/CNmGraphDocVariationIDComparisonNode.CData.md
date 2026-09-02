---
title: "CNmGraphDocVariationIDComparisonNode::CData"
module: animdoclib
kind: class
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmGraphDocVariationIDComparisonNode::CData

# CNmGraphDocVariationIDComparisonNode::CData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animdoclib

**Inherits from:** [CNmGraphDocVariationDataNode::CData](../animdoclib/CNmGraphDocVariationDataNode.CData.md)

**Relationships:**

```mermaid
classDiagram
    `CNmGraphDocVariationDataNode::CData` <|-- `CNmGraphDocVariationIDComparisonNode::CData`
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_values` | CUtlVector< CGlobalSymbol > |  | `MPropertyAttributeEditor AnimGraphID()` `MPropertyAutoExpandSelf` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmGraphDocVariationIDComparisonNode::CData&quot;,
	&quot;m_values&quot;:
	[
	]
}</pre>
</details>
