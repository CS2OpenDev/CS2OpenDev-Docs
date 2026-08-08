---
layout: default
title: CAnimGraphDoc_StateTransition
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_StateTransition

# CAnimGraphDoc_StateTransition

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 8 · **Module:** animgraphdoclib

**Derived by:** [CAnimGraphDoc_ComponentStateTransition](../animgraphdoclib/CAnimGraphDoc_ComponentStateTransition.md), [CAnimGraphDoc_NodeStateTransition](../animgraphdoclib/CAnimGraphDoc_NodeStateTransition.md)

**Metadata:** `MPropertyFriendlyName Transition`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_StateTransition <|-- CAnimGraphDoc_ComponentStateTransition
    CAnimGraphDoc_StateTransition <|-- CAnimGraphDoc_NodeStateTransition
    CAnimGraphDoc_StateTransition *-- CAnimGraphDoc_ConditionContainer
    CAnimGraphDoc_StateTransition *-- AnimStateID
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x28` | `m_conditionList` | [CAnimGraphDoc_ConditionContainer](../animgraphdoclib/CAnimGraphDoc_ConditionContainer.md) |  | `MPropertySuppressField` |
| `0x58` | `m_srcState` | [AnimStateID](../modellib/AnimStateID.md) |  | `MPropertySuppressField` |
| `0x5c` | `m_destState` | [AnimStateID](../modellib/AnimStateID.md) |  | `MPropertySuppressField` |
| `0x60` | `m_sComment` | CUtlString |  | `MPropertyAttributeEditor TextBlock()` `MPropertyFriendlyName Comment` `MPropertySortPriority -100` |
| `0x68` | `m_bDisabled` | bool |  | `MPropertyFriendlyName Disable` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_StateTransition&quot;,
	&quot;m_conditionList&quot;:
	{
		&quot;_class&quot;: &quot;CAnimGraphDoc_ConditionContainer&quot;,
		&quot;m_conditions&quot;:
		[
		]
	},
	&quot;m_srcState&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_destState&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_sComment&quot;: &quot;&quot;,
	&quot;m_bDisabled&quot;: false
}</pre>
</details>
