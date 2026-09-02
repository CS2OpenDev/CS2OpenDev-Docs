---
layout: default
title: CPreviewList
nav_exclude: true
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CPreviewList

# CPreviewList

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** sounddoc_lib

**Relationships:**

```mermaid
classDiagram
    CPreviewList *-- CPreviewEntry
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sounds` | CUtlVector< [CPreviewEntry](../sounddoc_lib/CPreviewEntry.md) > |  |  |
| `0x18` | `m_bPreviewInGame` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sounds&quot;:
	[
	],
	&quot;m_bPreviewInGame&quot;: false
}</pre>
</details>
