---
layout: default
title: RnMeshDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / RnMeshDesc_t

# RnMeshDesc_t

**Kind:** class · **Size:** 216 bytes (`0xd8`) · **Align:** 8 · **Module:** physicslib

**Inherits from:** [RnShapeDesc_t](../physicslib/RnShapeDesc_t.md)

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnMeshDesc_t
    RnMeshDesc_t *-- RnMesh_t
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
| `0x18` | `m_Mesh` | [RnMesh_t](../physicslib/RnMesh_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nCollisionAttributeIndex&quot;: 0,
	&quot;m_nSurfacePropertyIndex&quot;: 0,
	&quot;m_UserFriendlyName&quot;: &quot;&quot;,
	&quot;m_bUserFriendlyNameSealed&quot;: false,
	&quot;m_bUserFriendlyNameLong&quot;: false,
	&quot;m_nToolMaterialHash&quot;: 0,
	&quot;m_Mesh&quot;:
	{
		&quot;m_vMin&quot;:
		[
			0.000000,
			0.000000,
			0.000000
		],
		&quot;m_vMax&quot;:
		[
			0.000000,
			0.000000,
			0.000000
		],
		&quot;m_Materials&quot;:
		[
		],
		&quot;m_vOrthographicAreas&quot;:
		[
			0.000000,
			0.000000,
			0.000000
		],
		&quot;m_nFlags&quot;: 0,
		&quot;m_nDebugFlags&quot;: 0,
		&quot;m_Nodes&quot;: &quot;[BINARY BLOB]&quot;,
		&quot;m_Triangles&quot;: &quot;[BINARY BLOB]&quot;,
		&quot;m_Vertices&quot;: &quot;[BINARY BLOB]&quot;
	}
}</pre>
</details>
