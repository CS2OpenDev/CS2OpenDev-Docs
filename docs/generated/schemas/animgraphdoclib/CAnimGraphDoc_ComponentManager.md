---
layout: default
title: CAnimGraphDoc_ComponentManager
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_ComponentManager

# CAnimGraphDoc_ComponentManager

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 8 · **Module:** animgraphdoclib

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_ComponentManager *-- CAnimGraphDoc_Component
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_components` | CUtlVector< CSmartPtr< [CAnimGraphDoc_Component](../animgraphdoclib/CAnimGraphDoc_Component.md) > > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_ComponentManager&quot;,
	&quot;m_components&quot;:
	[
	]
}</pre>
</details>
