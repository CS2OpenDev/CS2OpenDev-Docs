---
title: FeSDFRigid_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeSDFRigid_t

# FeSDFRigid_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** physicslib

**Derived by:** [FeBuildSDFRigid_t](../physicslib/FeBuildSDFRigid_t.md)

**Relationships:**

```mermaid
classDiagram
    FeSDFRigid_t <|-- FeBuildSDFRigid_t
```

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `vLocalMin` | Vector |  |  |
| `0xc` | `vLocalMax` | Vector |  |  |
| `0x18` | `flBounciness` | float32 |  |  |
| `0x1c` | `nNode` | uint16 |  |  |
| `0x1e` | `nCollisionMask` | uint16 |  |  |
| `0x20` | `nVertexMapIndex` | uint16 |  |  |
| `0x22` | `nFlags` | uint16 |  |  |
| `0x28` | `m_Distances` | CUtlVector< float32 > |  |  |
| `0x40` | `m_nWidth` | int32 |  |  |
| `0x44` | `m_nHeight` | int32 |  |  |
| `0x48` | `m_nDepth` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;vLocalMin&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;vLocalMax&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;flBounciness&quot;: 0.000000,
	&quot;nNode&quot;: 0,
	&quot;nCollisionMask&quot;: 65535,
	&quot;nVertexMapIndex&quot;: 65535,
	&quot;nFlags&quot;: 0,
	&quot;m_Distances&quot;:
	[
	],
	&quot;m_nWidth&quot;: 8,
	&quot;m_nHeight&quot;: 8,
	&quot;m_nDepth&quot;: 8
}</pre>
</details>
