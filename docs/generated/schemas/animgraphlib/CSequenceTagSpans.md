---
layout: default
title: CSequenceTagSpans
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CSequenceTagSpans

# CSequenceTagSpans

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

**Relationships:**

```mermaid
classDiagram
    CSequenceTagSpans *-- TagSpan_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sSequenceName` | CGlobalSymbol |  |  |
| `0x8` | `m_tags` | CUtlVector< [TagSpan_t](../animgraphlib/TagSpan_t.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sSequenceName&quot;: &quot;&quot;,
	&quot;m_tags&quot;:
	[
	]
}</pre>
</details>
