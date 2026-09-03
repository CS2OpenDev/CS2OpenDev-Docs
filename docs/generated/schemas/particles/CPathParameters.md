---
title: CPathParameters
module: particles
kind: class
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CPathParameters

# CPathParameters

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 16 · **Module:** particles

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nStartControlPointNumber` | int32 |  | `MPropertyFriendlyName start control point number` |
| `0x4` | `m_nEndControlPointNumber` | int32 |  | `MPropertyFriendlyName end control point number` |
| `0x8` | `m_nBulgeControl` | int32 |  | `MPropertyFriendlyName bulge control 0=random 1=orientation of start pnt 2=orientation of end point` |
| `0xc` | `m_flBulge` | float32 |  | `MPropertyFriendlyName random bulge` |
| `0x10` | `m_flMidPoint` | float32 |  | `MPropertyFriendlyName mid point position` |
| `0x14` | `m_vStartPointOffset` | Vector |  | `MPropertyFriendlyName Offset from curve start point for path start` `MVectorIsCoordinate` |
| `0x20` | `m_vMidPointOffset` | Vector |  | `MPropertyFriendlyName Offset from curve midpoint for curve center` `MVectorIsCoordinate` |
| `0x2c` | `m_vEndOffset` | Vector |  | `MPropertyFriendlyName Offset from control point for path end` `MVectorIsCoordinate` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nStartControlPointNumber&quot;: 0,
	&quot;m_nEndControlPointNumber&quot;: 0,
	&quot;m_nBulgeControl&quot;: 0,
	&quot;m_flBulge&quot;: 0.000000,
	&quot;m_flMidPoint&quot;: 0.500000,
	&quot;m_vStartPointOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vMidPointOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vEndOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	]
}</pre>
</details>
