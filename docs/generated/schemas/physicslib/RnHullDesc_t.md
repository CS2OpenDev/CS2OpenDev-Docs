---
title: RnHullDesc_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / RnHullDesc_t

# RnHullDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 272 bytes (`0x110`) · **Align:** 8 · **Module:** physicslib

**Inherits from:** [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md)

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnHullDesc_t
    RnHullDesc_t *-- RnHull_t
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
| `0x18` | `m_Hull` | [RnHull_t](../physicslib/RnHull_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nCollisionAttributeIndex&quot;: 0,
	&quot;m_nSurfacePropertyIndex&quot;: 0,
	&quot;m_UserFriendlyName&quot;: &quot;&quot;,
	&quot;m_bUserFriendlyNameSealed&quot;: false,
	&quot;m_bUserFriendlyNameLong&quot;: false,
	&quot;m_nToolMaterialHash&quot;: 0,
	&quot;m_Hull&quot;:
	{
		&quot;m_vCentroid&quot;:
		[
			0.000000,
			0.000000,
			0.000000
		],
		&quot;m_flMaxAngularRadius&quot;: 0.000000,
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
		&quot;m_MassProperties&quot;:
		[
			1.000000,
			0.000000,
			0.000000,
			0.000000,
			0.000000,
			1.000000,
			0.000000,
			0.000000,
			0.000000,
			0.000000,
			1.000000,
			0.000000
		],
		&quot;m_flVolume&quot;: 0.000000,
		&quot;m_flSurfaceArea&quot;: 0.000000,
		&quot;m_nFlags&quot;: 0,
		&quot;m_pRegionSVM&quot;: null,
		&quot;m_Vertices&quot;: &quot;[BINARY BLOB]&quot;,
		&quot;m_VertexPositions&quot;: &quot;[BINARY BLOB]&quot;,
		&quot;m_Edges&quot;: &quot;[BINARY BLOB]&quot;,
		&quot;m_Faces&quot;: &quot;[BINARY BLOB]&quot;,
		&quot;m_Planes&quot;: &quot;[BINARY BLOB]&quot;
	}
}</pre>
</details>
