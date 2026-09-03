---
title: FeBuildBoxRigid_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeBuildBoxRigid_t

# FeBuildBoxRigid_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 16 · **Module:** physicslib

**Inherits from:** [FeBoxRigid_t](../physicslib/FeBoxRigid_t.md)

**Relationships:**

```mermaid
classDiagram
    FeBoxRigid_t <|-- FeBuildBoxRigid_t
```

## Memory layout

9 fields (3 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `tmFrame2` | CTransform | [FeBoxRigid_t](../physicslib/FeBoxRigid_t.md) |  |
| `0x20` | `nNode` | uint16 | [FeBoxRigid_t](../physicslib/FeBoxRigid_t.md) |  |
| `0x22` | `nCollisionMask` | uint16 | [FeBoxRigid_t](../physicslib/FeBoxRigid_t.md) |  |
| `0x24` | `vSize` | Vector | [FeBoxRigid_t](../physicslib/FeBoxRigid_t.md) |  |
| `0x30` | `nVertexMapIndex` | uint16 | [FeBoxRigid_t](../physicslib/FeBoxRigid_t.md) |  |
| `0x32` | `nFlags` | uint16 | [FeBoxRigid_t](../physicslib/FeBoxRigid_t.md) |  |
| `0x40` | `m_nPriority` | int32 |  |  |
| `0x44` | `m_nVertexMapHash` | uint32 |  |  |
| `0x48` | `m_nAntitunnelGroupBits` | uint32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;tmFrame2&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000,
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;nNode&quot;: 0,
	&quot;nCollisionMask&quot;: 65535,
	&quot;vSize&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;nVertexMapIndex&quot;: 65535,
	&quot;nFlags&quot;: 0,
	&quot;m_nPriority&quot;: 0,
	&quot;m_nVertexMapHash&quot;: 0,
	&quot;m_nAntitunnelGroupBits&quot;: 0
}</pre>
</details>
