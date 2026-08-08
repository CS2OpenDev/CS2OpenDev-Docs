---
layout: default
title: "CNmBlend1DNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmBlend1DNode::CDefinition

# CNmBlend1DNode::CDefinition

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmParameterizedBlendNode::CDefinition" <|-- "CNmBlend1DNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmParameterizedBlendNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

## Memory layout

5 fields (1 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_sourceNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 5 > | [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md) |  |
| `0x28` | `m_nInputParameterValueNodeIdx` | int16 | [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md) |  |
| `0x2a` | `m_bAllowLooping` | bool | [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md) |  |
| `0x30` | `m_parameterization` | CNmParameterizedBlendNode::Parameterization_t |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmBlend1DNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_sourceNodeIndices&quot;:
	[
	],
	&quot;m_nInputParameterValueNodeIdx&quot;: -1,
	&quot;m_bAllowLooping&quot;: true,
	&quot;m_parameterization&quot;:
	{
		&quot;m_blendRanges&quot;:
		[
		],
		&quot;m_parameterRange&quot;:
		{
			&quot;m_flMin&quot;: 340282346638528859811704183484516925440.000000,
			&quot;m_flMax&quot;: -340282346638528859811704183484516925440.000000
		}
	}
}</pre>
</details>
