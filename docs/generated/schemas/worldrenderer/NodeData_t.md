---
layout: default
title: NodeData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [worldrenderer](../worldrenderer.md) / NodeData_t

# NodeData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** worldrenderer

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nParent` | int32 |  |  |
| `0x4` | `m_vOrigin` | Vector |  |  |
| `0x10` | `m_vMinBounds` | Vector |  |  |
| `0x1c` | `m_vMaxBounds` | Vector |  |  |
| `0x28` | `m_flMinimumDistance` | float32 |  |  |
| `0x30` | `m_ChildNodeIndices` | CUtlVector< int32 > |  |  |
| `0x48` | `m_worldNodePrefix` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nParent&quot;: 0,
	&quot;m_vOrigin&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vMinBounds&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vMaxBounds&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_flMinimumDistance&quot;: 0.000000,
	&quot;m_ChildNodeIndices&quot;:
	[
	],
	&quot;m_worldNodePrefix&quot;: &quot;&quot;
}</pre>
</details>
