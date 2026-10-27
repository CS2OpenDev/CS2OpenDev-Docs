---
title: VPhysics2ShapeDef_t
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / VPhysics2ShapeDef_t

# VPhysics2ShapeDef_t

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 104 bytes (`0x68`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    VPhysics2ShapeDef_t *-- RnSphereDesc_t
    VPhysics2ShapeDef_t *-- RnCapsuleDesc_t
    VPhysics2ShapeDef_t *-- RnHullDesc_t
    VPhysics2ShapeDef_t *-- RnMeshDesc_t
    VPhysics2ShapeDef_t *-- RnCompoundDesc_t
```

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_spheres` | CUtlLeanVector< [RnSphereDesc_t](../physicslib/RnSphereDesc_t.md) > |  |  |
| `0x10` | `m_capsules` | CUtlLeanVector< [RnCapsuleDesc_t](../physicslib/RnCapsuleDesc_t.md) > |  |  |
| `0x20` | `m_hulls` | CUtlLeanVector< [RnHullDesc_t](../physicslib/RnHullDesc_t.md) > |  |  |
| `0x30` | `m_meshes` | CUtlLeanVector< [RnMeshDesc_t](../physicslib/RnMeshDesc_t.md) > |  |  |
| `0x40` | `m_compounds` | CUtlLeanVector< [RnCompoundDesc_t](../physicslib/RnCompoundDesc_t.md) > |  |  |
| `0x50` | `m_CollisionAttributeIndices` | CUtlVector< uint16 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_spheres&quot;:
	[
	],
	&quot;m_capsules&quot;:
	[
	],
	&quot;m_hulls&quot;:
	[
	],
	&quot;m_meshes&quot;:
	[
	],
	&quot;m_compounds&quot;:
	[
	],
	&quot;m_CollisionAttributeIndices&quot;:
	[
	]
}</pre>
</details>
