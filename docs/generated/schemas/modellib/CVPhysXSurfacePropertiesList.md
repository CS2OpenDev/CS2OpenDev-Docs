---
layout: default
title: CVPhysXSurfacePropertiesList
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CVPhysXSurfacePropertiesList

# CVPhysXSurfacePropertiesList

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    CVPhysXSurfacePropertiesList --> CPhysSurfaceProperties
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_surfacePropertiesList` | CUtlVector< [CPhysSurfaceProperties](../modellib/CPhysSurfaceProperties.md)* > |  | `MKV3TransferName SurfacePropertiesList` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;SurfacePropertiesList&quot;:
	[
	]
}</pre>
</details>
