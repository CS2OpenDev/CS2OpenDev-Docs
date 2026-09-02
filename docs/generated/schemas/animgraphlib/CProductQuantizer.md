---
title: CProductQuantizer
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CProductQuantizer

# CProductQuantizer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

**Relationships:**

```mermaid
classDiagram
    CProductQuantizer *-- CVectorQuantizer
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_subQuantizers` | CUtlVector< [CVectorQuantizer](../animgraphlib/CVectorQuantizer.md) > |  |  |
| `0x18` | `m_nDimensions` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_subQuantizers&quot;:
	[
	],
	&quot;m_nDimensions&quot;: 0
}</pre>
</details>
