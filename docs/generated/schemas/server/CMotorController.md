---
title: CMotorController
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CMotorController

# CMotorController

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** server

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_speed` | float32 |  |  |
| `0xc` | `m_maxTorque` | float32 |  |  |
| `0x10` | `m_axis` | Vector |  |  |
| `0x1c` | `m_inertiaFactor` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMotorController&quot;,
	&quot;m_speed&quot;: 0.000000,
	&quot;m_maxTorque&quot;: 0.000000,
	&quot;m_axis&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_inertiaFactor&quot;: 0.000000
}</pre>
</details>
