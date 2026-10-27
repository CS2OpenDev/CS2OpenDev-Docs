---
title: RnCompoundTreeNode_t
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / RnCompoundTreeNode_t

# RnCompoundTreeNode_t

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 28 bytes (`0x1c`) · **Align:** 4 · **Module:** physicslib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` bits 0..28 | `m_nSubtreeEndOrCompoundId` | bitfield:29 |  |  |
| `0x0` bits 29..31 | `m_nType` | bitfield:3 |  |  |
| `0x0` | `m_vMin` | Vector |  |  |
| `0xc` | `m_vMax` | Vector |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_vMin&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vMax&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_nType&quot;: 0,
	&quot;m_nSubtreeEndOrCompoundId&quot;: 0
}</pre>
</details>
