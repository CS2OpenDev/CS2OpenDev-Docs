---
title: MovementData
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / MovementData

# MovementData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 232 bytes (`0xe8`) · **Align:** 4 · **Module:** animgraphlib

## Memory layout

18 fields (18 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_goalWayPointPos` | Vector |  |  |
| `0xc` | `m_vMoveDir` | CAnimNetVar< Vector > |  |  |
| `0x20` | `m_vAcceleration` | CAnimNetVar< Vector > |  |  |
| `0x34` | `m_flCurrentMoveSpeed` | CAnimNetVar< float32 > |  |  |
| `0x40` | `m_flTargetMoveSpeed` | CAnimNetVar< float32 > |  |  |
| `0x4c` | `m_flGoalDistance` | CAnimNetVar< float32 > |  |  |
| `0x58` | `m_flBoundaryRadius` | CAnimNetVar< float32 > |  |  |
| `0x64` | `m_bGoalChanged` | bool |  |  |
| `0x68` | `m_bHasPath` | CAnimNetVar< bool > |  |  |
| `0x74` | `m_flFacingHeading` | CAnimNetVar< float32 > |  |  |
| `0x80` | `m_vManualFacingDirection` | Vector |  |  |
| `0x8c` | `m_vManualFacingTarget` | VectorWS |  |  |
| `0x98` | `m_nFacingMode` | CAnimNetVar< uint8 > |  |  |
| `0xa4` | `m_bForceFacing` | CAnimNetVar< bool > |  |  |
| `0xb0` | `m_nActiveMotorIndex` | CAnimNetVar< int32 > |  |  |
| `0xbc` | `m_bOnGround` | CAnimNetVar< bool > |  |  |
| `0xc8` | `m_vFacingPosition` | CAnimNetVar< Vector > |  |  |
| `0xdc` | `m_vPrevFacingPosition` | Vector |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_goalWayPointPos&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vMoveDir&quot;:
	[
		1.000000,
		0.000000,
		0.000000
	],
	&quot;m_vAcceleration&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_flCurrentMoveSpeed&quot;: 0.000000,
	&quot;m_flTargetMoveSpeed&quot;: 0.000000,
	&quot;m_flGoalDistance&quot;: -1.000000,
	&quot;m_flBoundaryRadius&quot;: 100.000000,
	&quot;m_bGoalChanged&quot;: false,
	&quot;m_bHasPath&quot;: false,
	&quot;m_flFacingHeading&quot;: 0.000000,
	&quot;m_vManualFacingDirection&quot;:
	[
		1.000000,
		0.000000,
		0.000000
	],
	&quot;m_vManualFacingTarget&quot;: null,
	&quot;m_nFacingMode&quot;: 0,
	&quot;m_bForceFacing&quot;: false,
	&quot;m_nActiveMotorIndex&quot;: -1,
	&quot;m_bOnGround&quot;: true,
	&quot;m_vFacingPosition&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vPrevFacingPosition&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	]
}</pre>
</details>
