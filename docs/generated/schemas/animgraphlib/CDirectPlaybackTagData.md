---
layout: default
title: CDirectPlaybackTagData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CDirectPlaybackTagData

# CDirectPlaybackTagData

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

**Relationships:**

```mermaid
classDiagram
    CDirectPlaybackTagData *-- TagSpan_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sequenceName` | CUtlString |  |  |
| `0x8` | `m_tags` | CUtlVector< [TagSpan_t](../animgraphlib/TagSpan_t.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sequenceName&quot;: &quot;&quot;,
	&quot;m_tags&quot;:
	[
	]
}</pre>
</details>
