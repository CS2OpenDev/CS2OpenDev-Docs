---
layout: default
title: CNmTargetWarpEvent
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTargetWarpEvent

# CNmTargetWarpEvent

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmEvent](../animlib/CNmEvent.md)

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmTargetWarpEvent
    CNmTargetWarpEvent *-- NmTargetWarpRule_t
    CNmTargetWarpEvent *-- NmTargetWarpAlgorithm_t
```

## Memory layout

5 fields (2 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flStartTime` | [NmPercent_t](../animlib/NmPercent_t.md) | [CNmEvent](../animlib/CNmEvent.md) |  |
| `0xc` | `m_flDuration` | [NmPercent_t](../animlib/NmPercent_t.md) | [CNmEvent](../animlib/CNmEvent.md) |  |
| `0x10` | `m_syncID` | CGlobalSymbol | [CNmEvent](../animlib/CNmEvent.md) |  |
| `0x18` | `m_rule` | [NmTargetWarpRule_t](../animlib/NmTargetWarpRule_t.md) |  |  |
| `0x19` | `m_algorithm` | [NmTargetWarpAlgorithm_t](../animlib/NmTargetWarpAlgorithm_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmTargetWarpEvent&quot;,
	&quot;m_flStartTime&quot;:
	{
		&quot;m_flValue&quot;: 0.000000
	},
	&quot;m_flDuration&quot;:
	{
		&quot;m_flValue&quot;: 0.000000
	},
	&quot;m_syncID&quot;: &quot;&quot;,
	&quot;m_rule&quot;: &quot;WarpXYZ&quot;,
	&quot;m_algorithm&quot;: &quot;Bezier&quot;
}</pre>
</details>
