---
title: CParticleVisibilityInputs
module: particles
kind: class
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CParticleVisibilityInputs

# CParticleVisibilityInputs

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 4 · **Module:** particles

## Memory layout

19 fields (19 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flCameraBias` | float32 |  | `MPropertyFriendlyName camera depth bias` |
| `0x4` | `m_nCPin` | int32 |  | `MPropertyFriendlyName input control point number` |
| `0x8` | `m_flProxyRadius` | float32 |  | `MPropertyFriendlyName input proxy radius` `MPropertySuppressExpr m_nCPin == -1` |
| `0xc` | `m_flInputMin` | float32 |  | `MPropertyFriendlyName input proxy pixel visibility minimum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x10` | `m_flInputMax` | float32 |  | `MPropertyFriendlyName input proxy pixel visibility maximum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x14` | `m_flInputPixelVisFade` | float32 |  | `MPropertyFriendlyName input proxy pixel visibility fade out time` `MPropertySuppressExpr m_nCPin == -1` |
| `0x18` | `m_flNoPixelVisibilityFallback` | float32 |  | `MPropertyFriendlyName input proxy unsupported hardware fallback value` `MPropertySuppressExpr m_nCPin == -1` |
| `0x1c` | `m_flDistanceInputMin` | float32 |  | `MPropertyFriendlyName input distance minimum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x20` | `m_flDistanceInputMax` | float32 |  | `MPropertyFriendlyName input distance maximum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x24` | `m_flDotInputMin` | float32 |  | `MPropertyFriendlyName input dot minimum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x28` | `m_flDotInputMax` | float32 |  | `MPropertyFriendlyName input dot maximum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x2c` | `m_bDotCPAngles` | bool |  | `MPropertyFriendlyName input dot use CP angles` `MPropertySuppressExpr m_nCPin == -1` |
| `0x2d` | `m_bDotCameraAngles` | bool |  | `MPropertyFriendlyName input dot use Camera angles` `MPropertySuppressExpr m_nCPin == -1` |
| `0x30` | `m_flAlphaScaleMin` | float32 |  | `MPropertyFriendlyName output alpha scale minimum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x34` | `m_flAlphaScaleMax` | float32 |  | `MPropertyFriendlyName output alpha scale maximum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x38` | `m_flRadiusScaleMin` | float32 |  | `MPropertyFriendlyName output radius scale minimum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x3c` | `m_flRadiusScaleMax` | float32 |  | `MPropertyFriendlyName output radius scale maximum` `MPropertySuppressExpr m_nCPin == -1` |
| `0x40` | `m_flRadiusScaleFOVBase` | float32 |  | `MPropertyFriendlyName output radius FOV scale base` `MPropertySuppressExpr m_nCPin == -1` |
| `0x44` | `m_bRightEye` | bool |  | `MParticleAdvancedField` `MPropertyFriendlyName vr camera right eye` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flCameraBias&quot;: 0.000000,
	&quot;m_nCPin&quot;: -1,
	&quot;m_flProxyRadius&quot;: 1.000000,
	&quot;m_flInputMin&quot;: 0.000000,
	&quot;m_flInputMax&quot;: 1.000000,
	&quot;m_flInputPixelVisFade&quot;: 0.250000,
	&quot;m_flNoPixelVisibilityFallback&quot;: 1.000000,
	&quot;m_flDistanceInputMin&quot;: 0.000000,
	&quot;m_flDistanceInputMax&quot;: 0.000000,
	&quot;m_flDotInputMin&quot;: 0.000000,
	&quot;m_flDotInputMax&quot;: 0.000000,
	&quot;m_bDotCPAngles&quot;: true,
	&quot;m_bDotCameraAngles&quot;: false,
	&quot;m_flAlphaScaleMin&quot;: 0.000000,
	&quot;m_flAlphaScaleMax&quot;: 1.000000,
	&quot;m_flRadiusScaleMin&quot;: 1.000000,
	&quot;m_flRadiusScaleMax&quot;: 1.000000,
	&quot;m_flRadiusScaleFOVBase&quot;: 0.000000,
	&quot;m_bRightEye&quot;: false
}</pre>
</details>
