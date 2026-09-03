---
title: CModelConfigElement_SetBodygroupOnAttachedModels
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CModelConfigElement_SetBodygroupOnAttachedModels

# CModelConfigElement_SetBodygroupOnAttachedModels

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** modellib

**Inherits from:** [CModelConfigElement](../modellib/CModelConfigElement.md)

**Relationships:**

```mermaid
classDiagram
    CModelConfigElement <|-- CModelConfigElement_SetBodygroupOnAttachedModels
```

## Memory layout

4 fields (2 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_ElementName` | CUtlString | [CModelConfigElement](../modellib/CModelConfigElement.md) |  |
| `0x10` | `m_NestedElements` | CUtlVector< [CModelConfigElement](../modellib/CModelConfigElement.md)* > | [CModelConfigElement](../modellib/CModelConfigElement.md) |  |
| `0x48` | `m_GroupName` | CUtlString |  |  |
| `0x50` | `m_nChoice` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CModelConfigElement_SetBodygroupOnAttachedModels&quot;,
	&quot;m_ElementName&quot;: &quot;&quot;,
	&quot;m_NestedElements&quot;:
	[
	],
	&quot;m_GroupName&quot;: &quot;&quot;,
	&quot;m_nChoice&quot;: 0
}</pre>
</details>
