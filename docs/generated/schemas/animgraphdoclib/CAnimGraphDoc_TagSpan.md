---
layout: default
title: CAnimGraphDoc_TagSpan
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_TagSpan

# CAnimGraphDoc_TagSpan

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animgraphdoclib

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_TagSpan *-- AnimTagID
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_id` | [AnimTagID](../modellib/AnimTagID.md) |  |  |
| `0x24` | `m_fStartCycle` | float32 |  |  |
| `0x28` | `m_fDuration` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_TagSpan&quot;,
	&quot;m_id&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_fStartCycle&quot;: 0.000000,
	&quot;m_fDuration&quot;: 0.100000
}</pre>
</details>
