---
title: CRopeOverlapHit
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CRopeOverlapHit

# CRopeOverlapHit

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    CRopeOverlapHit --> CBaseEntity
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_hEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x8` | `m_vecOverlappingLinks` | CUtlVector< int32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_hEntity&quot;: null,
	&quot;m_vecOverlappingLinks&quot;:
	[
	]
}</pre>
</details>
