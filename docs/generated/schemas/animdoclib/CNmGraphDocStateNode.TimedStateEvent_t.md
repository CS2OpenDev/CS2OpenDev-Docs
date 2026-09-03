---
title: "CNmGraphDocStateNode::TimedStateEvent_t"
module: animdoclib
kind: class
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmGraphDocStateNode::TimedStateEvent_t

# CNmGraphDocStateNode::TimedStateEvent_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animdoclib

**Metadata:** `MPropertyAutoExpandSelf`

**Relationships:**

```mermaid
classDiagram
    `CNmGraphDocStateNode::TimedStateEvent_t` *-- `CNmGraphDocStateNode::TimedStateEventType_t`
    `CNmGraphDocStateNode::TimedStateEvent_t` *-- `CNmStateNode::TimedEvent_t::Comparison_t`
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_ID` | CGlobalSymbol |  | `MPropertyAttributeEditor AnimGraphID()` |
| `0x8` | `m_type` | [CNmGraphDocStateNode::TimedStateEventType_t](../animdoclib/CNmGraphDocStateNode.TimedStateEventType_t.md) |  |  |
| `0xc` | `m_comparisonOperator` | [CNmStateNode::TimedEvent_t::Comparison_t](../animlib/CNmStateNode.TimedEvent_t.Comparison_t.md) |  |  |
| `0x10` | `m_flTimeValueSeconds` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
	&quot;m_type&quot;: &quot;TimeElapsed&quot;,
	&quot;m_comparisonOperator&quot;: &quot;LessThanEqual&quot;,
	&quot;m_flTimeValueSeconds&quot;: 0.200000
}</pre>
</details>
