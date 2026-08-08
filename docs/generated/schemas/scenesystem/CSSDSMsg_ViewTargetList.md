---
layout: default
title: CSSDSMsg_ViewTargetList
nav_exclude: true
---

[Schemas](../../schemas.md) / [scenesystem](../scenesystem.md) / CSSDSMsg_ViewTargetList

# CSSDSMsg_ViewTargetList

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** scenesystem

**Relationships:**

```mermaid
classDiagram
    CSSDSMsg_ViewTargetList *-- SceneViewId_t
    CSSDSMsg_ViewTargetList *-- CSSDSMsg_ViewTarget
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_viewId` | [SceneViewId_t](../scenesystem/SceneViewId_t.md) |  |  |
| `0x10` | `m_ViewName` | CUtlString |  |  |
| `0x18` | `m_Targets` | CUtlVector< [CSSDSMsg_ViewTarget](../scenesystem/CSSDSMsg_ViewTarget.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_viewId&quot;:
	{
		&quot;m_nViewId&quot;: 0,
		&quot;m_nFrameCount&quot;: 0
	},
	&quot;m_ViewName&quot;: &quot;&quot;,
	&quot;m_Targets&quot;:
	[
	]
}</pre>
</details>
