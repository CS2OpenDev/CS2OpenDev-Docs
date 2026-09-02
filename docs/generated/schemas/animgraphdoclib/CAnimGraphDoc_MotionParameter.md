---
layout: default
title: CAnimGraphDoc_MotionParameter
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_MotionParameter

# CAnimGraphDoc_MotionParameter

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animgraphdoclib

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_MotionParameter *-- AnimParamID
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_name` | CUtlString |  |  |
| `0x20` | `m_id` | [AnimParamID](../modellib/AnimParamID.md) |  |  |
| `0x24` | `m_flMinValue` | float32 |  |  |
| `0x28` | `m_flMaxValue` | float32 |  |  |
| `0x2c` | `m_nSamples` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_MotionParameter&quot;,
	&quot;m_name&quot;: &quot;Unnamed&quot;,
	&quot;m_id&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_flMinValue&quot;: 0.000000,
	&quot;m_flMaxValue&quot;: 1.000000,
	&quot;m_nSamples&quot;: 5
}</pre>
</details>
