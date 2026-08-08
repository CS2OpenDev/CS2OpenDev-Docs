---
layout: default
title: "CPulseCell_Outflow_PlaySceneBase::CursorState_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_Outflow_PlaySceneBase::CursorState_t

# CPulseCell_Outflow_PlaySceneBase::CursorState_t

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 8 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    "CPulseCell_Outflow_PlaySceneBase::CursorState_t" --> CBaseEntity
    "CPulseCell_Outflow_PlaySceneBase::CursorState_t" *-- PulseCursorID_t
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sceneInstance` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x4` | `m_mainActor` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x8` | `m_cursorIDToEventID` | CUtlHashtable< [PulseCursorID_t](../pulse_runtime_lib/PulseCursorID_t.md), int32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sceneInstance&quot;: null,
	&quot;m_mainActor&quot;: null,
	&quot;m_cursorIDToEventID&quot;:
	{
	}
}</pre>
</details>
