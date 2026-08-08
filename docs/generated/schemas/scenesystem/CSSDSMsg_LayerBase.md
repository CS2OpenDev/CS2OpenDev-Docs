---
layout: default
title: CSSDSMsg_LayerBase
nav_exclude: true
---

[Schemas](../../schemas.md) / [scenesystem](../scenesystem.md) / CSSDSMsg_LayerBase

# CSSDSMsg_LayerBase

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** scenesystem

**Derived by:** [CSSDSMsg_PostLayer](../scenesystem/CSSDSMsg_PostLayer.md), [CSSDSMsg_PreLayer](../scenesystem/CSSDSMsg_PreLayer.md)

**Relationships:**

```mermaid
classDiagram
    CSSDSMsg_LayerBase <|-- CSSDSMsg_PostLayer
    CSSDSMsg_LayerBase <|-- CSSDSMsg_PreLayer
    CSSDSMsg_LayerBase *-- SceneViewId_t
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_viewId` | [SceneViewId_t](../scenesystem/SceneViewId_t.md) |  |  |
| `0x10` | `m_ViewName` | CUtlString |  |  |
| `0x18` | `m_nLayerId` | uint64 |  |  |
| `0x20` | `m_LayerName` | CUtlString |  |  |
| `0x28` | `m_displayText` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_viewId&quot;:
	{
		&quot;m_nViewId&quot;: 0,
		&quot;m_nFrameCount&quot;: 0
	},
	&quot;m_ViewName&quot;: &quot;&quot;,
	&quot;m_nLayerId&quot;: 0,
	&quot;m_LayerName&quot;: &quot;&quot;,
	&quot;m_displayText&quot;: &quot;&quot;
}</pre>
</details>
