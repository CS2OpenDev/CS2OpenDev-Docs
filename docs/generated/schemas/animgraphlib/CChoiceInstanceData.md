---
layout: default
title: CChoiceInstanceData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CChoiceInstanceData

# CChoiceInstanceData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 52 bytes (`0x34`) · **Align:** 4 · **Module:** animgraphlib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_currentChoice` | CAnimNetVar< int32 > |  |  |
| `0x1c` | `m_previousChoice` | int32 |  |  |
| `0x20` | `m_flClipStartTime` | CAnimNetVar< float32 > |  |  |
| `0x2c` | `m_choicePreviousCycle` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_currentChoice&quot;: -1,
	&quot;m_previousChoice&quot;: -1,
	&quot;m_flClipStartTime&quot;: 0.000000,
	&quot;m_choicePreviousCycle&quot;: 0.000000
}</pre>
</details>
