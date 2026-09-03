---
title: SteamAudioCustomDataOcclusionSettings_t
module: steamaudio
kind: class
---

[Schemas](../../schemas.md) / [steamaudio](../steamaudio.md) / SteamAudioCustomDataOcclusionSettings_t

# SteamAudioCustomDataOcclusionSettings_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 12 bytes (`0xc`) · **Align:** 4 · **Module:** steamaudio

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bEnablePathing` | bool |  |  |
| `0x1` | `m_bEnableReflections` | bool |  |  |
| `0x4` | `m_nReflectionRays` | int32 |  |  |
| `0x8` | `m_nReflectionBounces` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_bEnablePathing&quot;: false,
	&quot;m_bEnableReflections&quot;: false,
	&quot;m_nReflectionRays&quot;: 0,
	&quot;m_nReflectionBounces&quot;: 0
}</pre>
</details>
