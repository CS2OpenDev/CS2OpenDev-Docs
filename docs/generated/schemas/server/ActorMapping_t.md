---
layout: default
title: ActorMapping_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / ActorMapping_t

# ActorMapping_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    ActorMapping_t --> CBaseEntity
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sActorName` | CUtlString |  |  |
| `0x8` | `m_hEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sActorName&quot;: &quot;&quot;,
	&quot;m_hEntity&quot;: null
}</pre>
</details>
