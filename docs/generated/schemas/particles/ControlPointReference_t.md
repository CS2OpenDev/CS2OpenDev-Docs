---
layout: default
title: ControlPointReference_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / ControlPointReference_t

# ControlPointReference_t

**Kind:** class · **Size:** 20 bytes (`0x14`) · **Align:** 4 · **Module:** particles

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_controlPointNameString` | int32 |  | `MPropertyFriendlyName Control point` |
| `0x4` | `m_vOffsetFromControlPoint` | Vector |  | `MPropertyFriendlyName Offset from control point` |
| `0x10` | `m_bOffsetInLocalSpace` | bool |  | `MPropertyFriendlyName Use local space offset` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_controlPointNameString&quot;: 0,
	&quot;m_vOffsetFromControlPoint&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_bOffsetInLocalSpace&quot;: false
}</pre>
</details>
