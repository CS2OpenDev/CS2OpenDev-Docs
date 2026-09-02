---
title: "CNmSyncTrack::EventMarker_t"
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmSyncTrack::EventMarker_t

# CNmSyncTrack::EventMarker_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animlib

**Relationships:**

```mermaid
classDiagram
    `CNmSyncTrack::EventMarker_t` *-- NmPercent_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_startTime` | [NmPercent_t](../animlib/NmPercent_t.md) |  |  |
| `0x8` | `m_ID` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_startTime&quot;:
	{
		&quot;m_flValue&quot;: 0.000000
	},
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
}</pre>
</details>
