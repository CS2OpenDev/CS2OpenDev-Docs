---
title: FeVertexMapBuild_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeVertexMapBuild_t

# FeVertexMapBuild_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** physicslib

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_VertexMapName` | CUtlString |  |  |
| `0x8` | `m_nNameHash` | uint32 |  |  |
| `0xc` | `m_Color` | Color |  |  |
| `0x10` | `m_flVolumetricSolveStrength` | float32 |  |  |
| `0x14` | `m_nScaleSourceNode` | int32 |  |  |
| `0x18` | `m_Weights` | CUtlVector< float32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_VertexMapName&quot;: &quot;&quot;,
	&quot;m_nNameHash&quot;: 0,
	&quot;m_Color&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_flVolumetricSolveStrength&quot;: 0.000000,
	&quot;m_nScaleSourceNode&quot;: -1,
	&quot;m_Weights&quot;:
	[
	]
}</pre>
</details>
