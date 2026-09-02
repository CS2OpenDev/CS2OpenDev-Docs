---
layout: default
title: CMorphData
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CMorphData

# CMorphData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    CMorphData *-- CMorphRectData
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  |  |
| `0x8` | `m_morphRectDatas` | CUtlVector< [CMorphRectData](../modellib/CMorphRectData.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_morphRectDatas&quot;:
	[
	]
}</pre>
</details>
