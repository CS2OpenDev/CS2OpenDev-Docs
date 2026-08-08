---
layout: default
title: CSteamAudioCompressedReverb
nav_exclude: true
---

[Schemas](../../schemas.md) / [steamaudio](../steamaudio.md) / CSteamAudioCompressedReverb

# CSteamAudioCompressedReverb

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** steamaudio

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nChannels` | int32 |  |  |
| `0x4` | `m_nBands` | int32 |  |  |
| `0x8` | `m_nBins` | int32 |  |  |
| `0xc` | `m_nProbes` | int32 |  |  |
| `0x10` | `m_vecNumSingularValues` | CUtlVector< int32 > |  |  |
| `0x28` | `m_vecDictionary` | CUtlVector< float32 > |  |  |
| `0x40` | `m_vecCompressedData` | CUtlVector< float32 > |  |  |
| `0x58` | `m_pCompressedData` | IPLCompressedEnergyFields |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nChannels&quot;: 0,
	&quot;m_nBands&quot;: 0,
	&quot;m_nBins&quot;: 0,
	&quot;m_nProbes&quot;: 0,
	&quot;m_vecNumSingularValues&quot;:
	[
	],
	&quot;m_vecDictionary&quot;:
	[
	],
	&quot;m_vecCompressedData&quot;:
	[
	]
}</pre>
</details>
