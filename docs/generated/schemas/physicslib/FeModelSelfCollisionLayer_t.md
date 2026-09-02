---
title: FeModelSelfCollisionLayer_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeModelSelfCollisionLayer_t

# FeModelSelfCollisionLayer_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** physicslib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Name` | CUtlString |  |  |
| `0x8` | `m_Nodes` | CUtlVector< uint16 > |  |  |
| `0x20` | `m_flParentReaction` | float32 |  |  |
| `0x24` | `m_nFlags` | uint32 |  |  |
| `0x28` | `m_nEndIdx` | uint32[4] |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_Nodes&quot;:
	[
	],
	&quot;m_flParentReaction&quot;: 0.000000,
	&quot;m_nFlags&quot;: 0,
	&quot;m_nEndIdx&quot;:
	[
		0,
		0,
		0,
		0
	]
}</pre>
</details>
