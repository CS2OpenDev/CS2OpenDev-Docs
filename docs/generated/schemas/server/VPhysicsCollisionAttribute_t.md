---
layout: default
title: VPhysicsCollisionAttribute_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / VPhysicsCollisionAttribute_t

# VPhysicsCollisionAttribute_t

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** server

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nInteractsAs` | uint64 |  |  |
| `0x10` | `m_nInteractsWith` | uint64 |  |  |
| `0x18` | `m_nInteractsExclude` | uint64 |  |  |
| `0x20` | `m_nEntityId` | uint32 |  |  |
| `0x24` | `m_nOwnerId` | uint32 |  |  |
| `0x28` | `m_nHierarchyId` | uint16 |  |  |
| `0x2a` | `m_nDetailLayerMask` | uint16 |  |  |
| `0x2c` | `m_nDetailLayerMaskType` | uint8 |  |  |
| `0x2d` | `m_nTargetDetailLayer` | uint8 |  |  |
| `0x2e` | `m_nCollisionGroup` | uint8 |  |  |
| `0x2f` | `m_nCollisionFunctionMask` | uint8 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;VPhysicsCollisionAttribute_t&quot;,
	&quot;m_nInteractsAs&quot;: 0,
	&quot;m_nInteractsWith&quot;: 0,
	&quot;m_nInteractsExclude&quot;: 0,
	&quot;m_nEntityId&quot;: 0,
	&quot;m_nOwnerId&quot;: 0,
	&quot;m_nHierarchyId&quot;: 0,
	&quot;m_nDetailLayerMask&quot;: 0,
	&quot;m_nDetailLayerMaskType&quot;: 0,
	&quot;m_nTargetDetailLayer&quot;: 0,
	&quot;m_nCollisionGroup&quot;: 0,
	&quot;m_nCollisionFunctionMask&quot;: 0
}</pre>
</details>
