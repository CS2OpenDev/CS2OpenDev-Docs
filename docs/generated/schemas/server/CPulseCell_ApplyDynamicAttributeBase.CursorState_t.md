---
title: "CPulseCell_ApplyDynamicAttributeBase::CursorState_t"
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_ApplyDynamicAttributeBase::CursorState_t

# CPulseCell_ApplyDynamicAttributeBase::CursorState_t

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    `CPulseCell_ApplyDynamicAttributeBase::CursorState_t` --> CBaseEntity
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_hEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x8` | `m_szAttributeKey` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_hEntity&quot;: null,
	&quot;m_szAttributeKey&quot;: &quot;&quot;
}</pre>
</details>
