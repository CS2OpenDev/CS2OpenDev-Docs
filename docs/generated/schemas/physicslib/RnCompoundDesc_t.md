---
layout: default
title: RnCompoundDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / RnCompoundDesc_t

# RnCompoundDesc_t

**Kind:** class · **Size:** 168 bytes (`0xa8`) · **Align:** 8 · **Module:** physicslib

**Inherits from:** [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md)

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnCompoundDesc_t
    RnCompoundDesc_t *-- RnCompound_t
```

## Memory layout

7 fields (1 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nCollisionAttributeIndex` | uint32 | [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md) |  |
| `0x4` | `m_nSurfacePropertyIndex` | uint32 | [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md) |  |
| `0x8` | `m_UserFriendlyName` | CUtlString | [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md) |  |
| `0x10` | `m_bUserFriendlyNameSealed` | bool | [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md) |  |
| `0x11` | `m_bUserFriendlyNameLong` | bool | [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md) |  |
| `0x14` | `m_nToolMaterialHash` | uint32 | [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md) |  |
| `0x18` | `m_Compound` | [RnCompound_t](../physicslib/RnCompound_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nCollisionAttributeIndex&quot;: 0,
	&quot;m_nSurfacePropertyIndex&quot;: 0,
	&quot;m_UserFriendlyName&quot;: &quot;&quot;,
	&quot;m_bUserFriendlyNameSealed&quot;: false,
	&quot;m_bUserFriendlyNameLong&quot;: false,
	&quot;m_nToolMaterialHash&quot;: 0,
	&quot;m_Compound&quot;:
	{
		&quot;m_Spheres&quot;:
		[
		],
		&quot;m_Capsules&quot;:
		[
		],
		&quot;m_Hulls&quot;:
		[
		],
		&quot;m_Meshes&quot;:
		[
		],
		&quot;m_Bounds&quot;:
		{
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
			]
		},
		&quot;m_vOrthographicAreas&quot;:
		[
			0.000000,
			0.000000,
			0.000000
		],
		&quot;m_flSurfaceArea&quot;: 0.000000,
		&quot;m_flVolume&quot;: 0.000000
	}
}</pre>
</details>
