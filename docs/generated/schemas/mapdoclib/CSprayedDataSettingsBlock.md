---
title: CSprayedDataSettingsBlock
module: mapdoclib
kind: class
---

[Schemas](../../schemas.md) / [mapdoclib](../mapdoclib.md) / CSprayedDataSettingsBlock

# CSprayedDataSettingsBlock

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 92 bytes (`0x5c`) · **Align:** 4 · **Module:** mapdoclib

## Memory layout

13 fields (13 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flMinDensity` | float32 |  |  |
| `0x4` | `m_flMaxDensity` | float32 |  |  |
| `0x8` | `m_flMinScale` | float32 |  |  |
| `0xc` | `m_flMaxScale` | float32 |  |  |
| `0x10` | `m_vMinAngle` | QAngle |  |  |
| `0x1c` | `m_vMaxAngle` | QAngle |  |  |
| `0x28` | `m_vMinColor` | Vector |  |  |
| `0x34` | `m_vMaxColor` | Vector |  |  |
| `0x40` | `m_flSpacingMul` | float32 |  |  |
| `0x44` | `m_flSlopeThreshold` | float32 |  |  |
| `0x48` | `m_vMasterDirection` | Vector |  |  |
| `0x54` | `m_flMasterDirectionInfluence` | float32 |  |  |
| `0x58` | `m_bEnabled` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flMinDensity&quot;: 1.000000,
	&quot;m_flMaxDensity&quot;: 1.000000,
	&quot;m_flMinScale&quot;: 0.500000,
	&quot;m_flMaxScale&quot;: 1.000000,
	&quot;m_vMinAngle&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vMaxAngle&quot;:
	[
		0.000000,
		360.000000,
		0.000000
	],
	&quot;m_vMinColor&quot;:
	[
		1.000000,
		1.000000,
		1.000000
	],
	&quot;m_vMaxColor&quot;:
	[
		1.000000,
		1.000000,
		1.000000
	],
	&quot;m_flSpacingMul&quot;: 1.000000,
	&quot;m_flSlopeThreshold&quot;: 100000.000000,
	&quot;m_vMasterDirection&quot;:
	[
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_flMasterDirectionInfluence&quot;: 0.000000,
	&quot;m_bEnabled&quot;: true
}</pre>
</details>
