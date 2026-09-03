---
title: CSteamAudioProbeLineSegment
module: steamaudio
kind: class
---

[Schemas](../../schemas.md) / [steamaudio](../steamaudio.md) / CSteamAudioProbeLineSegment

# CSteamAudioProbeLineSegment

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** steamaudio

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_vStart` | Vector |  |  |
| `0xc` | `m_vEnd` | Vector |  |  |
| `0x18` | `m_vecIntervals` | CUtlVector< float32 > |  |  |
| `0x30` | `m_vecProbeIndices` | CUtlVector< int32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_vStart&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vEnd&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vecIntervals&quot;:
	[
	],
	&quot;m_vecProbeIndices&quot;:
	[
	]
}</pre>
</details>
