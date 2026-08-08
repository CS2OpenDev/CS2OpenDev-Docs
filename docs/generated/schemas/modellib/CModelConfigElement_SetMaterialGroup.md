---
layout: default
title: CModelConfigElement_SetMaterialGroup
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CModelConfigElement_SetMaterialGroup

# CModelConfigElement_SetMaterialGroup

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** modellib

**Inherits from:** [CModelConfigElement](../modellib/CModelConfigElement.md)

**Relationships:**

```mermaid
classDiagram
    CModelConfigElement <|-- CModelConfigElement_SetMaterialGroup
```

## Memory layout

3 fields (1 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_ElementName` | CUtlString | [CModelConfigElement](../modellib/CModelConfigElement.md) |  |
| `0x10` | `m_NestedElements` | CUtlVector< [CModelConfigElement](../modellib/CModelConfigElement.md)* > | [CModelConfigElement](../modellib/CModelConfigElement.md) |  |
| `0x48` | `m_MaterialGroupName` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CModelConfigElement_SetMaterialGroup&quot;,
	&quot;m_ElementName&quot;: &quot;&quot;,
	&quot;m_NestedElements&quot;:
	[
	],
	&quot;m_MaterialGroupName&quot;: &quot;&quot;
}</pre>
</details>
