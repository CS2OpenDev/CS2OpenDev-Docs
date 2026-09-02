---
title: "CNmStateNode::CDefinition"
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmStateNode::CDefinition

# CNmStateNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 176 bytes (`0xb0`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPoseNode::CDefinition](../animlib/CNmPoseNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmPoseNode::CDefinition` <|-- `CNmStateNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmPoseNode::CDefinition`
    `CNmStateNode::CDefinition` *-- `CNmStateNode::TimedEvent_t`
```

## Memory layout

12 fields (11 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nChildNodeIdx` | int16 |  |  |
| `0x18` | `m_entryEvents` | CUtlLeanVectorFixedGrowable< CGlobalSymbol, 3 > |  |  |
| `0x38` | `m_executeEvents` | CUtlLeanVectorFixedGrowable< CGlobalSymbol, 3 > |  |  |
| `0x58` | `m_exitEvents` | CUtlLeanVectorFixedGrowable< CGlobalSymbol, 3 > |  |  |
| `0x78` | `m_timedRemainingEvents` | CUtlLeanVectorFixedGrowable< [CNmStateNode::TimedEvent_t](../animlib/CNmStateNode.TimedEvent_t.md), 1 > |  |  |
| `0x90` | `m_timedElapsedEvents` | CUtlLeanVectorFixedGrowable< [CNmStateNode::TimedEvent_t](../animlib/CNmStateNode.TimedEvent_t.md), 1 > |  |  |
| `0xa8` | `m_nLayerWeightNodeIdx` | int16 |  |  |
| `0xaa` | `m_nLayerRootMotionWeightNodeIdx` | int16 |  |  |
| `0xac` | `m_nLayerBoneMaskNodeIdx` | int16 |  |  |
| `0xae` | `m_bIsOffState` | bool |  |  |
| `0xaf` | `m_bUseActualElapsedTimeInStateForTimedEvents` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmStateNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nChildNodeIdx&quot;: -1,
	&quot;m_entryEvents&quot;:
	[
	],
	&quot;m_executeEvents&quot;:
	[
	],
	&quot;m_exitEvents&quot;:
	[
	],
	&quot;m_timedRemainingEvents&quot;:
	[
	],
	&quot;m_timedElapsedEvents&quot;:
	[
	],
	&quot;m_nLayerWeightNodeIdx&quot;: -1,
	&quot;m_nLayerRootMotionWeightNodeIdx&quot;: -1,
	&quot;m_nLayerBoneMaskNodeIdx&quot;: -1,
	&quot;m_bIsOffState&quot;: false,
	&quot;m_bUseActualElapsedTimeInStateForTimedEvents&quot;: false
}</pre>
</details>
