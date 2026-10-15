---
title: CPathParameters
module: particles
kind: class
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CPathParameters

# CPathParameters

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 16 · **Module:** particles

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nStartControlPointNumber` | int32 |  | `MPropertyFriendlyName start control point number` |
| `0x4` | `m_nMidControlPointNumber` | int32 |  | `MPropertyFriendlyName mid control point number` |
| `0x8` | `m_nEndControlPointNumber` | int32 |  | `MPropertyFriendlyName end control point number` |
| `0xc` | `m_nBulgeControl` | int32 |  | `MPropertyFriendlyName bulge control 0=random 1=orientation of start pnt 2=orientation of end point` `MPropertySuppressExpr m_nMidControlPointNumber != -1` |
| `0x10` | `m_flBulge` | float32 |  | `MPropertyFriendlyName random bulge` `MPropertySuppressExpr m_nMidControlPointNumber != -1` |
| `0x14` | `m_flMidPoint` | float32 |  | `MPropertyFriendlyName mid point position` `MPropertySuppressExpr m_nMidControlPointNumber != -1` |
| `0x18` | `m_vStartPointOffset` | Vector |  | `MPropertyFriendlyName Offset from curve start point for path start` `MVectorIsCoordinate` |
| `0x24` | `m_vMidPointOffset` | Vector |  | `MPropertyFriendlyName Offset from curve midpoint for curve center` `MVectorIsCoordinate` |
| `0x30` | `m_vEndOffset` | Vector |  | `MPropertyFriendlyName Offset from control point for path end` `MVectorIsCoordinate` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nStartControlPointNumber&quot;: 0,
	&quot;m_nMidControlPointNumber&quot;: -1,
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
