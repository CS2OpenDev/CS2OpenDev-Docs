---
layout: default
title: "CNmSyncTrack::Event_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmSyncTrack::Event_t

# CNmSyncTrack::Event_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animlib

**Relationships:**

```mermaid
classDiagram
    `CNmSyncTrack::Event_t` *-- NmPercent_t
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_ID` | CGlobalSymbol |  |  |
| `0x8` | `m_startTime` | [NmPercent_t](../animlib/NmPercent_t.md) |  |  |
| `0xc` | `m_duration` | [NmPercent_t](../animlib/NmPercent_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
	&quot;m_startTime&quot;:
	{
		&quot;m_flValue&quot;: 0.000000
	},
	&quot;m_duration&quot;:
	{
		&quot;m_flValue&quot;: 1.000000
	}
}</pre>
</details>
