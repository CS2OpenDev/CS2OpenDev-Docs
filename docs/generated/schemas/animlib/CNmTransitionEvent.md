---
layout: default
title: CNmTransitionEvent
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTransitionEvent

# CNmTransitionEvent

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmEvent](../animlib/CNmEvent.md)

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmTransitionEvent
    CNmTransitionEvent *-- NmTransitionRule_t
```

## Memory layout

5 fields (2 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flStartTime` | [NmPercent_t](../animlib/NmPercent_t.md) | [CNmEvent](../animlib/CNmEvent.md) |  |
| `0xc` | `m_flDuration` | [NmPercent_t](../animlib/NmPercent_t.md) | [CNmEvent](../animlib/CNmEvent.md) |  |
| `0x10` | `m_syncID` | CGlobalSymbol | [CNmEvent](../animlib/CNmEvent.md) |  |
| `0x18` | `m_rule` | [NmTransitionRule_t](../animlib/NmTransitionRule_t.md) |  |  |
| `0x20` | `m_ID` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmTransitionEvent&quot;,
	&quot;m_flStartTime&quot;:
	{
		&quot;m_flValue&quot;: 0.000000
	},
	&quot;m_flDuration&quot;:
	{
		&quot;m_flValue&quot;: 0.000000
	},
	&quot;m_syncID&quot;: &quot;&quot;,
	&quot;m_rule&quot;: &quot;BlockTransition&quot;,
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
}</pre>
</details>
