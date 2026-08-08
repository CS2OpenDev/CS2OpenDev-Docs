---
layout: default
title: CStateMachineComponent
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CStateMachineComponent

# CStateMachineComponent

**Kind:** class · **Size:** 104 bytes (`0x68`) · **Align:** 8 · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_Component](../animgraphdoclib/CAnimGraphDoc_Component.md), [CAnimGraphDoc_StateMachine](../animgraphdoclib/CAnimGraphDoc_StateMachine.md)

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_Component <|-- CStateMachineComponent
```

## Memory layout

6 fields (1 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_group` | CUtlString | [CAnimGraphDoc_Component](../animgraphdoclib/CAnimGraphDoc_Component.md) | `MPropertySuppressField` |
| `0x28` | `m_id` | [AnimComponentID](../modellib/AnimComponentID.md) | [CAnimGraphDoc_Component](../animgraphdoclib/CAnimGraphDoc_Component.md) | `MPropertySuppressField` |
| `0x2c` | `m_bStartEnabled` | bool | [CAnimGraphDoc_Component](../animgraphdoclib/CAnimGraphDoc_Component.md) | `MPropertyFriendlyName Start Enabled` |
| `0x30` | `m_nPriority` | int32 | [CAnimGraphDoc_Component](../animgraphdoclib/CAnimGraphDoc_Component.md) | `MPropertyFriendlyName Priority` |
| `0x34` | `m_networkMode` | [AnimNodeNetworkMode](../!GlobalTypes/AnimNodeNetworkMode.md) | [CAnimGraphDoc_Component](../animgraphdoclib/CAnimGraphDoc_Component.md) | `MPropertyFriendlyName Network Mode` |
| `0x60` | `m_sName` | CUtlString |  | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |

**Also inherits (secondary base classes):** [CAnimGraphDoc_StateMachine](../animgraphdoclib/CAnimGraphDoc_StateMachine.md) — additional-base fields sit at a shifted offset the schema does not record; see each base's own page for its layout.

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CStateMachineComponent&quot;,
	&quot;m_group&quot;: &quot;&quot;,
	&quot;m_id&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bStartEnabled&quot;: true,
	&quot;m_nPriority&quot;: 100,
	&quot;m_networkMode&quot;: &quot;ServerAuthoritative&quot;,
	&quot;m_states&quot;:
	[
	],
	&quot;m_sName&quot;: &quot;Unnamed&quot;
}</pre>
</details>
