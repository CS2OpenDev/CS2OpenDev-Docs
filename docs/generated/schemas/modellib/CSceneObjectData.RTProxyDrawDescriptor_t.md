---
layout: default
title: "CSceneObjectData::RTProxyDrawDescriptor_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CSceneObjectData::RTProxyDrawDescriptor_t

# CSceneObjectData::RTProxyDrawDescriptor_t

**Kind:** class · **Size:** 352 bytes (`0x160`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    "CSceneObjectData::RTProxyDrawDescriptor_t" *-- CMaterialDrawDescriptor
    "CSceneObjectData::RTProxyDrawDescriptor_t" *-- VertexAlbedoFormat_t
```

## Memory layout

13 fields (13 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_materialGroupToken` | uint32 |  |  |
| `0x4` | `m_nSrcDrawIndex` | int32 |  |  |
| `0x8` | `m_drawDesc` | [CMaterialDrawDescriptor](../modellib/CMaterialDrawDescriptor.md) |  |  |
| `0x120` | `m_mWorldFromLocal` | matrix3x4_t |  |  |
| `0x150` | `m_nVertexAlbedoFormat` | [VertexAlbedoFormat_t](../modellib/VertexAlbedoFormat_t.md) |  |  |
| `0x151` | `m_nVertexAlbedoVB` | int8 |  |  |
| `0x152` | `m_nVertexAlbedoOffset` | uint16 |  |  |
| `0x154` | `m_nVertexAlbedoStride` | uint16 |  |  |
| `0x156` | `m_nVertexEmissiveFormat` | [VertexAlbedoFormat_t](../modellib/VertexAlbedoFormat_t.md) |  |  |
| `0x157` | `m_nVertexEmissiveVB` | int8 |  |  |
| `0x158` | `m_nVertexEmissiveOffset` | uint16 |  |  |
| `0x15a` | `m_nVertexEmissiveStride` | uint16 |  |  |
| `0x15c` | `m_fEmissiveFactor` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_materialGroupToken&quot;: 0,
	&quot;m_nSrcDrawIndex&quot;: -1,
	&quot;m_drawDesc&quot;:
	{
		&quot;m_flUvDensity&quot;: 0.000000,
		&quot;m_vTintColor&quot;:
		[
			1.000000,
			1.000000,
			1.000000
		],
		&quot;m_flAlpha&quot;: 1.000000,
		&quot;m_nNumMeshlets&quot;: 0,
		&quot;m_nFirstMeshlet&quot;: 0,
		&quot;m_nAppliedIndexOffset&quot;: 0,
		&quot;m_nDepthVertexBufferIndex&quot;: 255,
		&quot;m_nMeshletPackedIVBIndex&quot;: 255,
		&quot;m_rigidMeshParts&quot;:
		[
		],
		&quot;m_rootBvhNodes&quot;:
		[
		],
		&quot;m_nPrimitiveType&quot;: &quot;RENDER_PRIM_TRIANGLES&quot;,
		&quot;m_nBaseVertex&quot;: 0,
		&quot;m_nVertexCount&quot;: 0,
		&quot;m_nStartIndex&quot;: 0,
		&quot;m_nIndexCount&quot;: 0,
		&quot;m_indexBuffer&quot;:
		{
			&quot;m_hBuffer&quot;: 0,
			&quot;m_nBindOffsetBytes&quot;: 0
		},
		&quot;m_meshletPackedIVB&quot;:
		{
			&quot;m_hBuffer&quot;: 0,
			&quot;m_nBindOffsetBytes&quot;: 0
		},
		&quot;m_material&quot;: &quot;&quot;,
		&quot;m_vertexBuffers&quot;:
		[
		]
	},
	&quot;m_mWorldFromLocal&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_nVertexAlbedoFormat&quot;: &quot;VERTEX_ALBEDO_NONE&quot;,
	&quot;m_nVertexAlbedoVB&quot;: -1,
	&quot;m_nVertexAlbedoOffset&quot;: 0,
	&quot;m_nVertexAlbedoStride&quot;: 0,
	&quot;m_nVertexEmissiveFormat&quot;: &quot;VERTEX_ALBEDO_NONE&quot;,
	&quot;m_nVertexEmissiveVB&quot;: -1,
	&quot;m_nVertexEmissiveOffset&quot;: 0,
	&quot;m_nVertexEmissiveStride&quot;: 0,
	&quot;m_fEmissiveFactor&quot;: 0.000000
}</pre>
</details>
