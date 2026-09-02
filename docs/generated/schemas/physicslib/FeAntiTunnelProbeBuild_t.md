---
layout: default
title: FeAntiTunnelProbeBuild_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeAntiTunnelProbeBuild_t

# FeAntiTunnelProbeBuild_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** physicslib

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `flWeight` | float32 |  |  |
| `0x4` | `flActivationDistance` | float32 |  |  |
| `0x8` | `flBias` | float32 |  |  |
| `0xc` | `flCurvature` | float32 |  |  |
| `0x10` | `nFlags` | uint32 |  |  |
| `0x14` | `nProbeNode` | uint16 |  |  |
| `0x18` | `targetNodes` | CUtlVector< uint16 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;flWeight&quot;: 1.000000,
	&quot;flActivationDistance&quot;: 1.000000,
	&quot;flBias&quot;: 0.000000,
	&quot;flCurvature&quot;: 0.000000,
	&quot;nFlags&quot;: 0,
	&quot;nProbeNode&quot;: 0,
	&quot;targetNodes&quot;:
	[
	]
}</pre>
</details>
