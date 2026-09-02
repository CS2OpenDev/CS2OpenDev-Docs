---
layout: default
title: CRandomPannerControls
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_voicecontainers](../soundsystem_voicecontainers.md) / CRandomPannerControls

# CRandomPannerControls

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** soundsystem_voicecontainers

**Metadata:** `MPropertyDescription Sets a control input every time it's instantiated`, `MPropertyFriendlyName Random Panner Control`

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_panningControlInputName` | CUtlString |  | `MPropertyFriendlyName Panning Control Input Name` |
| `0x8` | `m_volumeControlInputName` | CUtlString |  | `MPropertyFriendlyName Volume Control Input Name` |
| `0x10` | `m_flMinVolume` | float32 |  | `MPropertyFriendlyName Minimum Random Volume DB` |
| `0x14` | `m_flMaxVolume` | float32 |  | `MPropertyFriendlyName Maximum Random Volume DB` |
| `0x18` | `m_strVectorStackParam` | CUtlString |  | `MPropertyFriendlyName Forward Vector Stack Parameter Name` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_panningControlInputName&quot;: &quot;random_pan&quot;,
	&quot;m_volumeControlInputName&quot;: &quot;random_volume&quot;,
	&quot;m_flMinVolume&quot;: -12.000000,
	&quot;m_flMaxVolume&quot;: 0.000000,
	&quot;m_strVectorStackParam&quot;: &quot;ListenerForwardVector&quot;
}</pre>
</details>
