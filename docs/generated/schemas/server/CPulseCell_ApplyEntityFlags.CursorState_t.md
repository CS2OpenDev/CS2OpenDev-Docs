---
title: "CPulseCell_ApplyEntityFlags::CursorState_t"
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_ApplyEntityFlags::CursorState_t

# CPulseCell_ApplyEntityFlags::CursorState_t

> Source: **Build 25947352** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 4 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    `CPulseCell_ApplyEntityFlags::CursorState_t` --> CBaseEntity
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_hEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x4` | `m_uFlags` | uint32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_hEntity&quot;: null,
	&quot;m_uFlags&quot;: 0
}</pre>
</details>
