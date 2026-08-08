---
layout: default
title: MoodAnimation_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / MoodAnimation_t

# MoodAnimation_t

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animationsystem

**Metadata:** `MPropertyArrayElementNameKey m_sName`

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sName` | CModelAnimNameWithDeltas |  | `MPropertyDescription Name of the animation` |
| `0x8` | `m_flWeight` | float32 |  | `MPropertyDescription Weight of the animation, higher numbers get picked more` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sName&quot;: &quot;&quot;,
	&quot;m_flWeight&quot;: 1.000000
}</pre>
</details>
