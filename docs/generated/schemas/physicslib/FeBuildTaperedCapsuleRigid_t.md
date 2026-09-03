---
title: FeBuildTaperedCapsuleRigid_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeBuildTaperedCapsuleRigid_t

# FeBuildTaperedCapsuleRigid_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 16 · **Module:** physicslib

**Inherits from:** [FeTaperedCapsuleRigid_t](../physicslib/FeTaperedCapsuleRigid_t.md)

**Relationships:**

```mermaid
classDiagram
    FeTaperedCapsuleRigid_t <|-- FeBuildTaperedCapsuleRigid_t
```

## Memory layout

8 fields (3 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `vSphere` | fltx4[2] | [FeTaperedCapsuleRigid_t](../physicslib/FeTaperedCapsuleRigid_t.md) |  |
| `0x20` | `nNode` | uint16 | [FeTaperedCapsuleRigid_t](../physicslib/FeTaperedCapsuleRigid_t.md) |  |
| `0x22` | `nCollisionMask` | uint16 | [FeTaperedCapsuleRigid_t](../physicslib/FeTaperedCapsuleRigid_t.md) |  |
| `0x24` | `nVertexMapIndex` | uint16 | [FeTaperedCapsuleRigid_t](../physicslib/FeTaperedCapsuleRigid_t.md) |  |
| `0x26` | `nFlags` | uint16 | [FeTaperedCapsuleRigid_t](../physicslib/FeTaperedCapsuleRigid_t.md) |  |
| `0x30` | `m_nPriority` | int32 |  |  |
| `0x34` | `m_nVertexMapHash` | uint32 |  |  |
| `0x38` | `m_nAntitunnelGroupBits` | uint32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;vSphere&quot;:
	[
		[
			0.000000,
			0.000000,
			0.000000,
			0.000000
		],
		[
			0.000000,
			0.000000,
			0.000000,
			0.000000
		]
	],
	&quot;nNode&quot;: 0,
	&quot;nCollisionMask&quot;: 65535,
	&quot;nVertexMapIndex&quot;: 65535,
	&quot;nFlags&quot;: 0,
	&quot;m_nPriority&quot;: 0,
	&quot;m_nVertexMapHash&quot;: 0,
	&quot;m_nAntitunnelGroupBits&quot;: 0
}</pre>
</details>
