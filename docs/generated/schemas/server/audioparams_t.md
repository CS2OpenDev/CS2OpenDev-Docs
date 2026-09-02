---
layout: default
title: audioparams_t (server)
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / audioparams_t

# audioparams_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 120 bytes (`0x78`) · **Align:** 8 · **Module:** server

**Twin:** [audioparams_t (client)](../client/audioparams_t.md)

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `localSound` | VectorWS[8] |  |  |
| `0x68` | `soundscapeIndex` | int32 |  |  |
| `0x6c` | `localBits` | uint8 |  |  |
| `0x70` | `soundscapeEntityListIndex` | int32 |  |  |
| `0x74` | `soundEventHash` | uint32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;audioparams_t&quot;,
	&quot;localSound&quot;:
	[
		null,
		null,
		null,
		null,
		null,
		null,
		null,
		null
	],
	&quot;soundscapeIndex&quot;: 0,
	&quot;localBits&quot;: 0,
	&quot;soundscapeEntityListIndex&quot;: 0,
	&quot;soundEventHash&quot;: 0
}</pre>
</details>
