---
layout: default
title: CMotionNodeSequence
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CMotionNodeSequence

# CMotionNodeSequence

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CMotionNode](../animgraphlib/CMotionNode.md)

**Relationships:**

```mermaid
classDiagram
    CMotionNode <|-- CMotionNodeSequence
    CMotionNodeSequence *-- TagSpan_t
    CMotionNodeSequence *-- HSequence
```

## Memory layout

5 fields (3 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_name` | CUtlString | [CMotionNode](../animgraphlib/CMotionNode.md) |  |
| `0x20` | `m_id` | [AnimNodeID](../modellib/AnimNodeID.md) | [CMotionNode](../animgraphlib/CMotionNode.md) |  |
| `0x28` | `m_tags` | CUtlVector< [TagSpan_t](../animgraphlib/TagSpan_t.md) > |  |  |
| `0x40` | `m_hSequence` | [HSequence](../animationsystem/HSequence.md) |  |  |
| `0x44` | `m_flPlaybackSpeed` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMotionNodeSequence&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_id&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_tags&quot;:
	[
	],
	&quot;m_hSequence&quot;: -1,
	&quot;m_flPlaybackSpeed&quot;: 1.000000
}</pre>
</details>
