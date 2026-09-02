---
title: "CPulseCell_PlaySequence::CursorState_t (server)"
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_PlaySequence::CursorState_t

# CPulseCell_PlaySequence::CursorState_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 4 bytes (`0x4`) · **Align:** 4 · **Module:** server

**Twin:** [CPulseCell_PlaySequence::CursorState_t (client)](../client/CPulseCell_PlaySequence.CursorState_t.md)

**Relationships:**

```mermaid
classDiagram
    `CPulseCell_PlaySequence::CursorState_t` --> CBaseAnimGraph
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_hTarget` | CHandle< [CBaseAnimGraph](../server/CBaseAnimGraph.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_hTarget&quot;: null
}</pre>
</details>
