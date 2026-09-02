---
title: CAnimGraphDoc_ConflictManager
module: animgraphdoclib
kind: class
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_ConflictManager

# CAnimGraphDoc_ConflictManager

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** animgraphdoclib

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_ConflictManager *-- CAnimConflictBase
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_conflicts` | CUtlVector< CSmartPtr< [CAnimConflictBase](../animgraphdoclib/CAnimConflictBase.md) > > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_ConflictManager&quot;,
	&quot;m_conflicts&quot;:
	[
	]
}</pre>
</details>
