---
layout: default
title: CRelativeTransform
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CRelativeTransform

# CRelativeTransform

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 16 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    CRelativeTransform --> CBaseEntity
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bTransformIsWorldSpace` | bool |  |  |
| `0x10` | `m_transform` | CTransform |  |  |
| `0x30` | `m_transformWS` | CTransformWS |  |  |
| `0x50` | `m_hEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>null</pre>
</details>
