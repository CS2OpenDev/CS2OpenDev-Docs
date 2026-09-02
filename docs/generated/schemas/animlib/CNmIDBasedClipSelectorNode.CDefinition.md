---
layout: default
title: "CNmIDBasedClipSelectorNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmIDBasedClipSelectorNode::CDefinition

# CNmIDBasedClipSelectorNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmClipReferenceNode::CDefinition](../animlib/CNmClipReferenceNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmClipReferenceNode::CDefinition` <|-- `CNmIDBasedClipSelectorNode::CDefinition`
    `CNmPoseNode::CDefinition` <|-- `CNmClipReferenceNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmPoseNode::CDefinition`
```

## Memory layout

6 fields (5 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 5 > |  |  |
| `0x28` | `m_optionIDs` | CUtlLeanVectorFixedGrowable< CGlobalSymbol, 5 > |  |  |
| `0x58` | `m_nParameterNodeIdx` | int16 |  |  |
| `0x5a` | `m_nFallbackNodeIdx` | int16 |  |  |
| `0x5c` | `m_bIgnoreInvalidOptions` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmIDBasedClipSelectorNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_optionNodeIndices&quot;:
	[
	],
	&quot;m_optionIDs&quot;:
	[
	],
	&quot;m_nParameterNodeIdx&quot;: -1,
	&quot;m_nFallbackNodeIdx&quot;: -1,
	&quot;m_bIgnoreInvalidOptions&quot;: false
}</pre>
</details>
