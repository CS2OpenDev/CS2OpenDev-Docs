---
title: CEditableMotionGraph
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CEditableMotionGraph

# CEditableMotionGraph

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CMotionGraph](../animgraphlib/CMotionGraph.md)

**Relationships:**

```mermaid
classDiagram
    CMotionGraph <|-- CEditableMotionGraph
```

## Memory layout

7 fields (0 declared here, 7 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_paramSpans` | [CParamSpanUpdater](../animgraphlib/CParamSpanUpdater.md) | [CMotionGraph](../animgraphlib/CMotionGraph.md) |  |
| `0x28` | `m_tags` | CUtlVector< [TagSpan_t](../animgraphlib/TagSpan_t.md) > | [CMotionGraph](../animgraphlib/CMotionGraph.md) |  |
| `0x40` | `m_pRootNode` | CSmartPtr< [CMotionNode](../animgraphlib/CMotionNode.md) > | [CMotionGraph](../animgraphlib/CMotionGraph.md) |  |
| `0x48` | `m_nParameterCount` | int32 | [CMotionGraph](../animgraphlib/CMotionGraph.md) |  |
| `0x4c` | `m_nConfigStartIndex` | int32 | [CMotionGraph](../animgraphlib/CMotionGraph.md) |  |
| `0x50` | `m_nConfigCount` | int32 | [CMotionGraph](../animgraphlib/CMotionGraph.md) |  |
| `0x54` | `m_bLoop` | bool | [CMotionGraph](../animgraphlib/CMotionGraph.md) |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CEditableMotionGraph&quot;,
	&quot;m_paramSpans&quot;:
	{
		&quot;m_spans&quot;:
		[
		]
	},
	&quot;m_tags&quot;:
	[
	],
	&quot;m_pRootNode&quot;: null,
	&quot;m_nParameterCount&quot;: 0,
	&quot;m_nConfigStartIndex&quot;: -1,
	&quot;m_nConfigCount&quot;: -1,
	&quot;m_bLoop&quot;: false
}</pre>
</details>
