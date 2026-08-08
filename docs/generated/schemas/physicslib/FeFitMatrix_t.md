---
layout: default
title: FeFitMatrix_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeFitMatrix_t

# FeFitMatrix_t

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 16 · **Module:** physicslib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `bone` | CTransform |  |  |
| `0x20` | `vCenter` | Vector |  |  |
| `0x2c` | `nEnd` | uint16 |  |  |
| `0x2e` | `nNode` | uint16 |  |  |
| `0x30` | `nBeginDynamic` | uint16 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;bone&quot;:
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
	&quot;vCenter&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;nEnd&quot;: 0,
	&quot;nNode&quot;: 0,
	&quot;nBeginDynamic&quot;: 0
}</pre>
</details>
