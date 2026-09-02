---
title: SteamAudioReverbSettings_t
module: steamaudio
kind: class
---

[Schemas](../../schemas.md) / [steamaudio](../steamaudio.md) / SteamAudioReverbSettings_t

# SteamAudioReverbSettings_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 20 bytes (`0x14`) · **Align:** 4 · **Module:** steamaudio

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nNumRays` | int32 |  |  |
| `0x4` | `m_nNumBounces` | int32 |  |  |
| `0x8` | `m_flIRDuration` | float32 |  |  |
| `0xc` | `m_nAmbisonicsOrder` | int32 |  |  |
| `0x10` | `m_bExportScene` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nNumRays&quot;: 0,
	&quot;m_nNumBounces&quot;: 0,
	&quot;m_flIRDuration&quot;: 0.000000,
	&quot;m_nAmbisonicsOrder&quot;: 0,
	&quot;m_bExportScene&quot;: false
}</pre>
</details>
