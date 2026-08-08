---
layout: default
title: MaterialGroup_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / MaterialGroup_t

# MaterialGroup_t

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    MaterialGroup_t *-- InfoForResourceTypeIMaterial2
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  |  |
| `0x8` | `m_materials` | CUtlVector< CStrongHandle< [InfoForResourceTypeIMaterial2](../resourcesystem/InfoForResourceTypeIMaterial2.md) > > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_materials&quot;:
	[
	]
}</pre>
</details>
