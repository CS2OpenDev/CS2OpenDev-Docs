---
title: levellist_t
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / levellist_t

# levellist_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** server

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sMapName` | CUtlString |  |  |
| `0x8` | `m_sLandmarkName` | CUtlString |  |  |
| `0x10` | `m_hEntLandmark` | CEntityHandle |  |  |
| `0x14` | `m_vecLandmarkOrigin` | VectorWS |  |  |
| `0x20` | `m_vecLandmarkAngles` | QAngle |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sMapName&quot;: &quot;&quot;,
	&quot;m_sLandmarkName&quot;: &quot;&quot;,
	&quot;m_hEntLandmark&quot;: null,
	&quot;m_vecLandmarkOrigin&quot;: null,
	&quot;m_vecLandmarkAngles&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	]
}</pre>
</details>
