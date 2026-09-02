---
title: constraint_hingeparams_t
module: vphysics2
kind: class
---

[Schemas](../../schemas.md) / [vphysics2](../vphysics2.md) / constraint_hingeparams_t

# constraint_hingeparams_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 4 · **Module:** vphysics2

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `worldPosition` | VectorWS |  |  |
| `0xc` | `worldAxisDirection` | Vector |  |  |
| `0x18` | `hingeAxis` | constraint_axislimit_t |  | `MNotSaved` |
| `0x28` | `constraint` | constraint_breakableparams_t |  | `MNotSaved` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;worldPosition&quot;: null,
	&quot;worldAxisDirection&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	]
}</pre>
</details>
