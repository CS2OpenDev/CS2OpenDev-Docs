---
title: CGameSceneNodeHandle (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CGameSceneNodeHandle

# CGameSceneNodeHandle

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** client

**Twin:** [CGameSceneNodeHandle (server)](../server/CGameSceneNodeHandle.md)

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_hOwner` | CEntityHandle |  |  |
| `0xc` | `m_name` | CUtlStringToken |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CGameSceneNodeHandle&quot;,
	&quot;m_hOwner&quot;: null,
	&quot;m_name&quot;: &quot;&quot;
}</pre>
</details>
