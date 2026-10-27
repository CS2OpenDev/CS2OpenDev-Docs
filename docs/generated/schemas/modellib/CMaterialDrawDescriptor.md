---
title: CMaterialDrawDescriptor
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CMaterialDrawDescriptor

# CMaterialDrawDescriptor

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 288 bytes (`0x120`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    CMaterialDrawDescriptor *-- `CMaterialDrawDescriptor::RigidMeshPart_t`
    CMaterialDrawDescriptor *-- RenderPrimitiveType_t
    CMaterialDrawDescriptor *-- CRenderBufferBinding
    CMaterialDrawDescriptor *-- InfoForResourceTypeIMaterial2
```

## Memory layout

19 fields (19 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flUvDensity` | float32 |  |  |
| `0x4` | `m_vTintColor` | Vector |  |  |
| `0x10` | `m_flAlpha` | float32 |  |  |
| `0x18` | `m_nNumMeshlets` | uint32 |  |  |
| `0x20` | `m_nFirstMeshlet` | uint32 |  |  |
| `0x24` | `m_nAppliedIndexOffset` | uint32 |  |  |
| `0x28` | `m_nEmissivePrimitiveCount` | int32 |  |  |
| `0x2c` | `m_nDepthVertexBufferIndex` | uint8 |  |  |
| `0x2d` | `m_nMeshletPackedIVBIndex` | uint8 |  |  |
| `0x30` | `m_rigidMeshParts` | CUtlLeanVector< [CMaterialDrawDescriptor::RigidMeshPart_t](../modellib/CMaterialDrawDescriptor.RigidMeshPart_t.md) > |  |  |
| `0x40` | `m_rootBvhNodes` | CUtlLeanVector< uint16 > |  |  |
| `0x50` | `m_nPrimitiveType` | [RenderPrimitiveType_t](../modellib/RenderPrimitiveType_t.md) |  |  |
| `0x54` | `m_nBaseVertex` | int32 |  |  |
| `0x58` | `m_nVertexCount` | int32 |  |  |
| `0x5c` | `m_nStartIndex` | int32 |  |  |
| `0x60` | `m_nIndexCount` | int32 |  |  |
| `0xc8` | `m_indexBuffer` | [CRenderBufferBinding](../modellib/CRenderBufferBinding.md) |  |  |
| `0xe8` | `m_meshletPackedIVB` | [CRenderBufferBinding](../modellib/CRenderBufferBinding.md) |  |  |
| `0x118` | `m_material` | CStrongHandle< [InfoForResourceTypeIMaterial2](../resourcesystem/InfoForResourceTypeIMaterial2.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
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
	&quot;m_nEmissivePrimitiveCount&quot;: -1,
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
}</pre>
</details>
