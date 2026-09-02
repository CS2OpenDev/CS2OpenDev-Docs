---
layout: default
title: CGlowProperty (server)
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CGlowProperty

# CGlowProperty

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** server

**Twin:** [CGlowProperty (client)](../client/CGlowProperty.md)

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_fGlowColor` | Vector |  | `MNotSaved` |
| `0x30` | `m_iGlowType` | int32 |  |  |
| `0x34` | `m_iGlowTeam` | int32 |  | `MNotSaved` |
| `0x38` | `m_nGlowRange` | int32 |  | `MNotSaved` |
| `0x3c` | `m_nGlowRangeMin` | int32 |  | `MNotSaved` |
| `0x40` | `m_glowColorOverride` | Color |  | `MNotSaved` |
| `0x44` | `m_bFlashing` | bool |  | `MNotSaved` |
| `0x48` | `m_flGlowTime` | float32 |  | `MNotSaved` |
| `0x4c` | `m_flGlowStartTime` | float32 |  | `MNotSaved` |
| `0x50` | `m_bEligibleForScreenHighlight` | bool |  |  |
| `0x51` | `m_bGlowing` | bool |  | `MNotSaved` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CGlowProperty&quot;,
	&quot;m_iGlowType&quot;: 0,
	&quot;m_bEligibleForScreenHighlight&quot;: false
}</pre>
</details>
