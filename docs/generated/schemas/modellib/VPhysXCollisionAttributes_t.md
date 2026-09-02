---
title: VPhysXCollisionAttributes_t
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / VPhysXCollisionAttributes_t

# VPhysXCollisionAttributes_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 208 bytes (`0xd0`) · **Align:** 8 · **Module:** modellib

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nIncludeDetailLayerCount` | int32 |  |  |
| `0x4` | `m_CollisionGroup` | uint32 |  |  |
| `0x8` | `m_InteractAs` | CUtlVector< uint32 > |  |  |
| `0x20` | `m_InteractWith` | CUtlVector< uint32 > |  |  |
| `0x38` | `m_InteractExclude` | CUtlVector< uint32 > |  |  |
| `0x50` | `m_DetailLayers` | CUtlVector< uint32 > |  |  |
| `0x68` | `m_CollisionGroupString` | CUtlString |  |  |
| `0x70` | `m_InteractAsStrings` | CUtlVector< CUtlString > |  |  |
| `0x88` | `m_InteractWithStrings` | CUtlVector< CUtlString > |  |  |
| `0xa0` | `m_InteractExcludeStrings` | CUtlVector< CUtlString > |  |  |
| `0xb8` | `m_DetailLayerStrings` | CUtlVector< CUtlString > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nIncludeDetailLayerCount&quot;: 0,
	&quot;m_CollisionGroup&quot;: 0,
	&quot;m_InteractAs&quot;:
	[
	],
	&quot;m_InteractWith&quot;:
	[
	],
	&quot;m_InteractExclude&quot;:
	[
	],
	&quot;m_DetailLayers&quot;:
	[
	],
	&quot;m_CollisionGroupString&quot;: &quot;&quot;,
	&quot;m_InteractAsStrings&quot;:
	[
	],
	&quot;m_InteractWithStrings&quot;:
	[
	],
	&quot;m_InteractExcludeStrings&quot;:
	[
	],
	&quot;m_DetailLayerStrings&quot;:
	[
	]
}</pre>
</details>
