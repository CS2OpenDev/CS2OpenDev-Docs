---
title: FeVertexMapDesc_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeVertexMapDesc_t

# FeVertexMapDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** physicslib

## Memory layout

12 fields (12 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `sName` | CUtlString |  |  |
| `0x8` | `nNameHash` | uint32 |  |  |
| `0xc` | `nColor` | uint32 |  |  |
| `0x10` | `nFlags` | uint32 |  |  |
| `0x14` | `nVertexBase` | uint16 |  |  |
| `0x16` | `nVertexCount` | uint16 |  |  |
| `0x18` | `nMapOffset` | uint32 |  |  |
| `0x1c` | `nNodeListOffset` | uint32 |  |  |
| `0x20` | `vCenterOfMass` | Vector |  |  |
| `0x2c` | `flVolumetricSolveStrength` | float32 |  |  |
| `0x30` | `nScaleSourceNode` | int16 |  |  |
| `0x32` | `nNodeListCount` | uint16 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;sName&quot;: &quot;&quot;,
	&quot;nNameHash&quot;: 0,
	&quot;nColor&quot;: 0,
	&quot;nFlags&quot;: 0,
	&quot;nVertexBase&quot;: 0,
	&quot;nVertexCount&quot;: 0,
	&quot;nMapOffset&quot;: 0,
	&quot;nNodeListOffset&quot;: 0,
	&quot;vCenterOfMass&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;flVolumetricSolveStrength&quot;: 0.000000,
	&quot;nScaleSourceNode&quot;: -1,
	&quot;nNodeListCount&quot;: 0
}</pre>
</details>
