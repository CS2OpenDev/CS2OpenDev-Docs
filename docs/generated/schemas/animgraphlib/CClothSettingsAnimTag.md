---
layout: default
title: CClothSettingsAnimTag
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CClothSettingsAnimTag

# CClothSettingsAnimTag

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CAnimTagBase](../animgraphlib/CAnimTagBase.md)

**Metadata:** `MPropertyFriendlyName Cloth Settings Tag`

**Relationships:**

```mermaid
classDiagram
    CAnimTagBase <|-- CClothSettingsAnimTag
```

## Memory layout

9 fields (4 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_name` | CGlobalSymbol | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |
| `0x20` | `m_sComment` | CUtlString | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertyAttributeEditor TextBlock()` `MPropertyFriendlyName Comment` `MPropertySortPriority -100` |
| `0x28` | `m_group` | CGlobalSymbol | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertySuppressField` |
| `0x30` | `m_tagID` | [AnimTagID](../modellib/AnimTagID.md) | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertySuppressField` |
| `0x48` | `m_bIsReferenced` | bool | [CAnimTagBase](../animgraphlib/CAnimTagBase.md) | `MPropertySuppressField` |
| `0x58` | `m_flStiffness` | float32 |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName Stiffness` |
| `0x5c` | `m_flEaseIn` | float32 |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName EaseIn` |
| `0x60` | `m_flEaseOut` | float32 |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName EaseOut` |
| `0x68` | `m_nVertexSet` | CUtlString |  | `MPropertyFriendlyName VertexSet` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CClothSettingsAnimTag&quot;,
	&quot;m_name&quot;: &quot;Unnamed Tag&quot;,
	&quot;m_sComment&quot;: &quot;&quot;,
	&quot;m_group&quot;: &quot;&quot;,
	&quot;m_tagID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bIsReferenced&quot;: false,
	&quot;m_flStiffness&quot;: 1.000000,
	&quot;m_flEaseIn&quot;: 0.000000,
	&quot;m_flEaseOut&quot;: 0.000000,
	&quot;m_nVertexSet&quot;: &quot;&quot;
}</pre>
</details>
