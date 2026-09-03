---
title: VPhysXConstraintParams_t
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / VPhysXConstraintParams_t

# VPhysXConstraintParams_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 248 bytes (`0xf8`) · **Align:** 4 · **Module:** modellib

## Memory layout

46 fields (46 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nType` | int8 |  |  |
| `0x1` | `m_nTranslateMotion` | int8 |  |  |
| `0x2` | `m_nRotateMotion` | int8 |  |  |
| `0x3` | `m_nFlags` | int8 |  |  |
| `0x4` | `m_anchor` | Vector[2] |  |  |
| `0x1c` | `m_axes` | QuaternionStorage[2] |  |  |
| `0x3c` | `m_maxForce` | float32 |  |  |
| `0x40` | `m_maxTorque` | float32 |  |  |
| `0x44` | `m_linearLimitValue` | float32 |  |  |
| `0x48` | `m_linearLimitRestitution` | float32 |  |  |
| `0x4c` | `m_linearLimitSpring` | float32 |  |  |
| `0x50` | `m_linearLimitDamping` | float32 |  |  |
| `0x54` | `m_twistLowLimitValue` | float32 |  |  |
| `0x58` | `m_twistLowLimitRestitution` | float32 |  |  |
| `0x5c` | `m_twistLowLimitSpring` | float32 |  |  |
| `0x60` | `m_twistLowLimitDamping` | float32 |  |  |
| `0x64` | `m_twistHighLimitValue` | float32 |  |  |
| `0x68` | `m_twistHighLimitRestitution` | float32 |  |  |
| `0x6c` | `m_twistHighLimitSpring` | float32 |  |  |
| `0x70` | `m_twistHighLimitDamping` | float32 |  |  |
| `0x74` | `m_swing1LimitValue` | float32 |  |  |
| `0x78` | `m_swing1LimitRestitution` | float32 |  |  |
| `0x7c` | `m_swing1LimitSpring` | float32 |  |  |
| `0x80` | `m_swing1LimitDamping` | float32 |  |  |
| `0x84` | `m_swing2LimitValue` | float32 |  |  |
| `0x88` | `m_swing2LimitRestitution` | float32 |  |  |
| `0x8c` | `m_swing2LimitSpring` | float32 |  |  |
| `0x90` | `m_swing2LimitDamping` | float32 |  |  |
| `0x94` | `m_goalPosition` | Vector |  |  |
| `0xa0` | `m_goalOrientation` | QuaternionStorage |  |  |
| `0xb0` | `m_goalAngularVelocity` | Vector |  |  |
| `0xbc` | `m_driveSpringX` | float32 |  |  |
| `0xc0` | `m_driveSpringY` | float32 |  |  |
| `0xc4` | `m_driveSpringZ` | float32 |  |  |
| `0xc8` | `m_driveDampingX` | float32 |  |  |
| `0xcc` | `m_driveDampingY` | float32 |  |  |
| `0xd0` | `m_driveDampingZ` | float32 |  |  |
| `0xd4` | `m_driveSpringTwist` | float32 |  |  |
| `0xd8` | `m_driveSpringSwing` | float32 |  |  |
| `0xdc` | `m_driveSpringSlerp` | float32 |  |  |
| `0xe0` | `m_driveDampingTwist` | float32 |  |  |
| `0xe4` | `m_driveDampingSwing` | float32 |  |  |
| `0xe8` | `m_driveDampingSlerp` | float32 |  |  |
| `0xec` | `m_solverIterationCount` | int32 |  |  |
| `0xf0` | `m_projectionLinearTolerance` | float32 |  |  |
| `0xf4` | `m_projectionAngularTolerance` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nType&quot;: 0,
	&quot;m_nTranslateMotion&quot;: 0,
	&quot;m_nRotateMotion&quot;: 0,
	&quot;m_nFlags&quot;: 0,
	&quot;m_anchor&quot;:
	[
		[
			0.000000,
			0.000000,
			0.000000
		],
		[
			0.000000,
			0.000000,
			0.000000
		]
	],
	&quot;m_axes&quot;:
	[
		[
			0.000000,
			0.000000,
			0.000000,
			0.000000
		],
		[
			0.000000,
			0.000000,
			0.000000,
			0.000000
		]
	],
	&quot;m_maxForce&quot;: 0.000000,
	&quot;m_maxTorque&quot;: 0.000000,
	&quot;m_linearLimitValue&quot;: 0.000000,
	&quot;m_linearLimitRestitution&quot;: 0.000000,
	&quot;m_linearLimitSpring&quot;: 0.000000,
	&quot;m_linearLimitDamping&quot;: 0.000000,
	&quot;m_twistLowLimitValue&quot;: 0.000000,
	&quot;m_twistLowLimitRestitution&quot;: 0.000000,
	&quot;m_twistLowLimitSpring&quot;: 0.000000,
	&quot;m_twistLowLimitDamping&quot;: 0.000000,
	&quot;m_twistHighLimitValue&quot;: 0.000000,
	&quot;m_twistHighLimitRestitution&quot;: 0.000000,
	&quot;m_twistHighLimitSpring&quot;: 0.000000,
	&quot;m_twistHighLimitDamping&quot;: 0.000000,
	&quot;m_swing1LimitValue&quot;: 0.000000,
	&quot;m_swing1LimitRestitution&quot;: 0.000000,
	&quot;m_swing1LimitSpring&quot;: 0.000000,
	&quot;m_swing1LimitDamping&quot;: 0.000000,
	&quot;m_swing2LimitValue&quot;: 0.000000,
	&quot;m_swing2LimitRestitution&quot;: 0.000000,
	&quot;m_swing2LimitSpring&quot;: 0.000000,
	&quot;m_swing2LimitDamping&quot;: 0.000000,
	&quot;m_goalPosition&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_goalOrientation&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_goalAngularVelocity&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_driveSpringX&quot;: 0.000000,
	&quot;m_driveSpringY&quot;: 0.000000,
	&quot;m_driveSpringZ&quot;: 0.000000,
	&quot;m_driveDampingX&quot;: 0.000000,
	&quot;m_driveDampingY&quot;: 0.000000,
	&quot;m_driveDampingZ&quot;: 0.000000,
	&quot;m_driveSpringTwist&quot;: 0.000000,
	&quot;m_driveSpringSwing&quot;: 0.000000,
	&quot;m_driveSpringSlerp&quot;: 0.000000,
	&quot;m_driveDampingTwist&quot;: 0.000000,
	&quot;m_driveDampingSwing&quot;: 0.000000,
	&quot;m_driveDampingSlerp&quot;: 0.000000,
	&quot;m_solverIterationCount&quot;: 0,
	&quot;m_projectionLinearTolerance&quot;: 0.000000,
	&quot;m_projectionAngularTolerance&quot;: 0.000000
}</pre>
</details>
