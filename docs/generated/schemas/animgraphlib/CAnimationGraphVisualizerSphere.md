---
title: CAnimationGraphVisualizerSphere
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CAnimationGraphVisualizerSphere

# CAnimationGraphVisualizerSphere

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 16 · **Module:** animgraphlib

**Inherits from:** [CAnimationGraphVisualizerPrimitiveBase](../animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md)

**Relationships:**

```mermaid
classDiagram
    CAnimationGraphVisualizerPrimitiveBase <|-- CAnimationGraphVisualizerSphere
```

## Memory layout

6 fields (3 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_Type` | [CAnimationGraphVisualizerPrimitiveType](../animgraphlib/CAnimationGraphVisualizerPrimitiveType.md) | [CAnimationGraphVisualizerPrimitiveBase](../animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |  |
| `0xc` | `m_OwningAnimNodePaths` | [AnimNodeID](../modellib/AnimNodeID.md)[11] | [CAnimationGraphVisualizerPrimitiveBase](../animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |  |
| `0x38` | `m_nOwningAnimNodePathCount` | int32 | [CAnimationGraphVisualizerPrimitiveBase](../animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |  |
| `0x40` | `m_vWsPosition` | VectorAligned |  |  |
| `0x50` | `m_flRadius` | float32 |  |  |
| `0x54` | `m_Color` | Color |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimationGraphVisualizerSphere&quot;,
	&quot;m_Type&quot;: &quot;ANIMATIONGRAPHVISUALIZERPRIMITIVETYPE_Sphere&quot;,
	&quot;m_OwningAnimNodePaths&quot;:
	[
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		}
	],
	&quot;m_nOwningAnimNodePathCount&quot;: 0,
	&quot;m_vWsPosition&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_flRadius&quot;: -1.000000,
	&quot;m_Color&quot;:
	[
		0,
		0,
		0,
		0
	]
}</pre>
</details>
