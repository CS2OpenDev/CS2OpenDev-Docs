---
layout: default
title: CRandomNumberGeneratorParameters
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CRandomNumberGeneratorParameters

# CRandomNumberGeneratorParameters

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 4 · **Module:** particles

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bDistributeEvenly` | bool |  | `MPropertyFriendlyName Distribute evenly` |
| `0x4` | `m_nSeed` | int32 |  | `MPropertyFriendlyName Seed (negative values=randomize)` `MPropertySuppressExpr !m_bDistributeEvenly` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_bDistributeEvenly&quot;: false,
	&quot;m_nSeed&quot;: -1
}</pre>
</details>
