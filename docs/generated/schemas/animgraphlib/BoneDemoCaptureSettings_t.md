---
layout: default
title: BoneDemoCaptureSettings_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / BoneDemoCaptureSettings_t

# BoneDemoCaptureSettings_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_boneName` | CUtlString |  | `MPropertyAttributeChoiceName Bone` `MPropertyFriendlyName Bone` |
| `0x8` | `m_flErrorSplineRotationMax` | float32 |  | `MPropertySuppressField` |
| `0xc` | `m_flErrorSplineTranslationMax` | float32 |  | `MPropertySuppressField` |
| `0x10` | `m_flErrorSplineScaleMax` | float32 |  | `MPropertySuppressField` |
| `0x14` | `m_flErrorQuantizationRotationMax` | float32 |  | `MPropertySuppressField` |
| `0x18` | `m_flErrorQuantizationTranslationMax` | float32 |  | `MPropertySuppressField` |
| `0x1c` | `m_flErrorQuantizationScaleMax` | float32 |  | `MPropertySuppressField` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_boneName&quot;: &quot;&quot;,
	&quot;m_flErrorSplineRotationMax&quot;: 1.000000,
	&quot;m_flErrorSplineTranslationMax&quot;: 1.000000,
	&quot;m_flErrorSplineScaleMax&quot;: 1.000000,
	&quot;m_flErrorQuantizationRotationMax&quot;: 1.000000,
	&quot;m_flErrorQuantizationTranslationMax&quot;: 1.000000,
	&quot;m_flErrorQuantizationScaleMax&quot;: 1.000000
}</pre>
</details>
