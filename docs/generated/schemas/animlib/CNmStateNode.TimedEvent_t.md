---
layout: default
title: "CNmStateNode::TimedEvent_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmStateNode::TimedEvent_t

# CNmStateNode::TimedEvent_t

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animlib

**Relationships:**

```mermaid
classDiagram
    "CNmStateNode::TimedEvent_t" *-- Comparison_t
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_ID` | CGlobalSymbol |  |  |
| `0x8` | `m_flTimeValueSeconds` | float32 |  |  |
| `0xc` | `m_comparisionOperator` | CNmStateNode::TimedEvent_t::[Comparison_t](../!GlobalTypes/Comparison_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
	&quot;m_flTimeValueSeconds&quot;: 0.000000,
	&quot;m_comparisionOperator&quot;: &quot;LessThanEqual&quot;
}</pre>
</details>
