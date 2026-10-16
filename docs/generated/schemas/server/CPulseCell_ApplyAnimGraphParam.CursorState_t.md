---
title: "CPulseCell_ApplyAnimGraphParam::CursorState_t"
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_ApplyAnimGraphParam::CursorState_t

# CPulseCell_ApplyAnimGraphParam::CursorState_t

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    `CPulseCell_ApplyAnimGraphParam::CursorState_t` --> CBaseEntity
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `hEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x8` | `sParamName` | CUtlString |  |  |
| `0x10` | `bApplyToExternalGraphs` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;hEntity&quot;: null,
	&quot;sParamName&quot;: &quot;&quot;,
	&quot;bApplyToExternalGraphs&quot;: false
}</pre>
</details>
