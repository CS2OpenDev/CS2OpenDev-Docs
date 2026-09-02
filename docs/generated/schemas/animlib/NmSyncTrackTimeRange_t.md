---
title: NmSyncTrackTimeRange_t
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / NmSyncTrackTimeRange_t

# NmSyncTrackTimeRange_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 4 · **Module:** animlib

**Relationships:**

```mermaid
classDiagram
    NmSyncTrackTimeRange_t *-- NmSyncTrackTime_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_startTime` | [NmSyncTrackTime_t](../animlib/NmSyncTrackTime_t.md) |  |  |
| `0x8` | `m_endTime` | [NmSyncTrackTime_t](../animlib/NmSyncTrackTime_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_startTime&quot;:
	{
		&quot;m_nEventIdx&quot;: 0,
		&quot;m_percentageThrough&quot;:
		{
			&quot;m_flValue&quot;: 0.000000
		}
	},
	&quot;m_endTime&quot;:
	{
		&quot;m_nEventIdx&quot;: 0,
		&quot;m_percentageThrough&quot;:
		{
			&quot;m_flValue&quot;: 0.000000
		}
	}
}</pre>
</details>
