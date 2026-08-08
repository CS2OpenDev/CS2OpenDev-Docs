---
layout: default
title: MotionMatchingInstanceData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / MotionMatchingInstanceData

# MotionMatchingInstanceData

**Kind:** class · **Size:** 288 bytes (`0x120`) · **Align:** 16 · **Module:** animgraphlib

**Relationships:**

```mermaid
classDiagram
    MotionMatchingInstanceData *-- MotionSelection
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x2c` | `m_currentSelection` | [MotionSelection](../animgraphlib/MotionSelection.md) |  |  |
| `0x84` | `m_previousSelection` | [MotionSelection](../animgraphlib/MotionSelection.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_currentSelection&quot;:
	{
		&quot;m_nConfigIndex&quot;:
		{
			&quot;m_index&quot;: 4294967295
		},
		&quot;m_flCycleZeroTime&quot;: 0.000000,
		&quot;m_flPlaybackSpeed&quot;: 1.000000,
		&quot;m_flStartTime&quot;: 0.000000,
		&quot;m_nSample&quot;: -1
	},
	&quot;m_previousSelection&quot;:
	{
		&quot;m_nConfigIndex&quot;:
		{
			&quot;m_index&quot;: 4294967295
		},
		&quot;m_flCycleZeroTime&quot;: 0.000000,
		&quot;m_flPlaybackSpeed&quot;: 1.000000,
		&quot;m_flStartTime&quot;: 0.000000,
		&quot;m_nSample&quot;: -1
	}
}</pre>
</details>
