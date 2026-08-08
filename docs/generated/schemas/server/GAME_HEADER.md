---
layout: default
title: GAME_HEADER
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / GAME_HEADER

# GAME_HEADER

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** server

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sComment` | CUtlString |  |  |
| `0x8` | `m_nSpawnGroupCount` | int32 |  |  |
| `0x10` | `m_sLandmark` | CUtlString |  |  |
| `0x18` | `m_sRequiredAddons` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sComment&quot;: &quot;&quot;,
	&quot;m_nSpawnGroupCount&quot;: 0,
	&quot;m_sLandmark&quot;: &quot;&quot;,
	&quot;m_sRequiredAddons&quot;: &quot;&quot;
}</pre>
</details>
