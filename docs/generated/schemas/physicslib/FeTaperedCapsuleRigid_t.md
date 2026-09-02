---
layout: default
title: FeTaperedCapsuleRigid_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeTaperedCapsuleRigid_t

# FeTaperedCapsuleRigid_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 16 · **Module:** physicslib

**Derived by:** [FeBuildTaperedCapsuleRigid_t](../physicslib/FeBuildTaperedCapsuleRigid_t.md)

**Relationships:**

```mermaid
classDiagram
    FeTaperedCapsuleRigid_t <|-- FeBuildTaperedCapsuleRigid_t
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `vSphere` | fltx4[2] |  |  |
| `0x20` | `nNode` | uint16 |  |  |
| `0x22` | `nCollisionMask` | uint16 |  |  |
| `0x24` | `nVertexMapIndex` | uint16 |  |  |
| `0x26` | `nFlags` | uint16 |  |  |

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
	&quot;nFlags&quot;: 0
}</pre>
</details>
