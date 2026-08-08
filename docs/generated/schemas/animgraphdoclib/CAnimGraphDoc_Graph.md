---
layout: default
title: CAnimGraphDoc_Graph
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_Graph

# CAnimGraphDoc_Graph

**Kind:** class · **Size:** 328 bytes (`0x148`) · **Align:** 8 · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_SubGraph](../animgraphdoclib/CAnimGraphDoc_SubGraph.md)

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_SubGraph <|-- CAnimGraphDoc_Graph
    CAnimGraphDoc_Graph *-- CAnimGraphSettingsManager
    CAnimGraphDoc_Graph *-- CAnimGraphDoc_ClipDataManager
```

## Memory layout

10 fields (4 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nodeManager` | [CAnimGraphDoc_NodeManager](../animgraphdoclib/CAnimGraphDoc_NodeManager.md) | [CAnimGraphDoc_SubGraph](../animgraphdoclib/CAnimGraphDoc_SubGraph.md) |  |
| `0x50` | `m_componentManager` | [CAnimGraphDoc_ComponentManager](../animgraphdoclib/CAnimGraphDoc_ComponentManager.md) | [CAnimGraphDoc_SubGraph](../animgraphdoclib/CAnimGraphDoc_SubGraph.md) |  |
| `0x78` | `m_localParameters` | CUtlVector< CSmartPtr< [CAnimParameterBase](../animgraphlib/CAnimParameterBase.md) > > | [CAnimGraphDoc_SubGraph](../animgraphdoclib/CAnimGraphDoc_SubGraph.md) |  |
| `0x90` | `m_localTags` | CUtlVector< CSmartPtr< [CAnimTagBase](../animgraphlib/CAnimTagBase.md) > > | [CAnimGraphDoc_SubGraph](../animgraphdoclib/CAnimGraphDoc_SubGraph.md) |  |
| `0xa8` | `m_referencedParamGroups` | CUtlVector< CUtlString > | [CAnimGraphDoc_SubGraph](../animgraphdoclib/CAnimGraphDoc_SubGraph.md) |  |
| `0xc0` | `m_referencedTagGroups` | CUtlVector< CUtlString > | [CAnimGraphDoc_SubGraph](../animgraphdoclib/CAnimGraphDoc_SubGraph.md) |  |
| `0xe0` | `m_pSettingsManager` | CSmartPtr< [CAnimGraphSettingsManager](../animgraphlib/CAnimGraphSettingsManager.md) > |  |  |
| `0xf0` | `m_clipDataManager` | [CAnimGraphDoc_ClipDataManager](../animgraphdoclib/CAnimGraphDoc_ClipDataManager.md) |  |  |
| `0x138` | `m_modelName` | CUtlString |  |  |
| `0x140` | `m_previewModelName` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_Graph&quot;,
	&quot;m_nodeManager&quot;:
	{
		&quot;_class&quot;: &quot;CAnimGraphDoc_NodeManager&quot;,
		&quot;m_nodes&quot;:
		[
		]
	},
	&quot;m_componentManager&quot;:
	{
		&quot;_class&quot;: &quot;CAnimGraphDoc_ComponentManager&quot;,
		&quot;m_components&quot;:
		[
		]
	},
	&quot;m_localParameters&quot;:
	[
	],
	&quot;m_localTags&quot;:
	[
	],
	&quot;m_referencedParamGroups&quot;:
	[
	],
	&quot;m_referencedTagGroups&quot;:
	[
	],
	&quot;m_pSettingsManager&quot;:
	{
		&quot;_class&quot;: &quot;CAnimGraphSettingsManager&quot;,
		&quot;m_settingsGroups&quot;:
		[
			{
				&quot;_class&quot;: &quot;CAnimGraphNetworkSettings&quot;,
				&quot;m_bNetworkingEnabled&quot;: true
			}
		]
	},
	&quot;m_clipDataManager&quot;:
	{
		&quot;_class&quot;: &quot;CAnimGraphDoc_ClipDataManager&quot;,
		&quot;m_itemTable&quot;:
		{
		}
	},
	&quot;m_modelName&quot;: &quot;&quot;,
	&quot;m_previewModelName&quot;: &quot;&quot;
}</pre>
</details>
