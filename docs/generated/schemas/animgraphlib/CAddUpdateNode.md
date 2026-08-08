---
layout: default
title: CAddUpdateNode
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CAddUpdateNode

# CAddUpdateNode

**Kind:** class · **Size:** 160 bytes (`0xa0`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CBinaryUpdateNode](../animgraphlib/CBinaryUpdateNode.md)

**Relationships:**

```mermaid
classDiagram
    CBinaryUpdateNode <|-- CAddUpdateNode
    CAnimUpdateNodeBase <|-- CBinaryUpdateNode
    CAddUpdateNode *-- BinaryNodeChildOption
```

## Memory layout

14 fields (5 declared here, 9 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_nodePath` | [CAnimNodePath](../animgraphlib/CAnimNodePath.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x48` | `m_networkMode` | [AnimNodeNetworkMode](../!GlobalTypes/AnimNodeNetworkMode.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x50` | `m_name` | CUtlString | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x60` | `m_pChild1` | [CAnimUpdateNodeRef](../animgraphlib/CAnimUpdateNodeRef.md) | [CBinaryUpdateNode](../animgraphlib/CBinaryUpdateNode.md) |  |
| `0x70` | `m_pChild2` | [CAnimUpdateNodeRef](../animgraphlib/CAnimUpdateNodeRef.md) | [CBinaryUpdateNode](../animgraphlib/CBinaryUpdateNode.md) |  |
| `0x80` | `m_timingBehavior` | [BinaryNodeTiming](../!GlobalTypes/BinaryNodeTiming.md) | [CBinaryUpdateNode](../animgraphlib/CBinaryUpdateNode.md) |  |
| `0x84` | `m_flTimingBlend` | float32 | [CBinaryUpdateNode](../animgraphlib/CBinaryUpdateNode.md) |  |
| `0x88` | `m_bResetChild1` | bool | [CBinaryUpdateNode](../animgraphlib/CBinaryUpdateNode.md) |  |
| `0x89` | `m_bResetChild2` | bool | [CBinaryUpdateNode](../animgraphlib/CBinaryUpdateNode.md) |  |
| `0x94` | `m_footMotionTiming` | [BinaryNodeChildOption](../!GlobalTypes/BinaryNodeChildOption.md) |  |  |
| `0x98` | `m_bApplyToFootMotion` | bool |  |  |
| `0x99` | `m_bApplyChannelsSeparately` | bool |  |  |
| `0x9a` | `m_bUseModelSpace` | bool |  |  |
| `0x9b` | `m_bApplyScale` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAddUpdateNode&quot;,
	&quot;m_nodePath&quot;:
	{
		&quot;m_path&quot;:
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
		&quot;m_nCount&quot;: 0
	},
	&quot;m_networkMode&quot;: &quot;ServerAuthoritative&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_pChild1&quot;:
	{
		&quot;m_nodeIndex&quot;: -1
	},
	&quot;m_pChild2&quot;:
	{
		&quot;m_nodeIndex&quot;: -1
	},
	&quot;m_timingBehavior&quot;: &quot;UseChild1&quot;,
	&quot;m_flTimingBlend&quot;: 0.500000,
	&quot;m_bResetChild1&quot;: true,
	&quot;m_bResetChild2&quot;: true,
	&quot;m_footMotionTiming&quot;: &quot;Child1&quot;,
	&quot;m_bApplyToFootMotion&quot;: true,
	&quot;m_bApplyChannelsSeparately&quot;: true,
	&quot;m_bUseModelSpace&quot;: false,
	&quot;m_bApplyScale&quot;: false
}</pre>
</details>
