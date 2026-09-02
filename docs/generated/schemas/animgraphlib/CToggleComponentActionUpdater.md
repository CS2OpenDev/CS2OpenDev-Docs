---
layout: default
title: CToggleComponentActionUpdater
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CToggleComponentActionUpdater

# CToggleComponentActionUpdater

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CAnimActionUpdater](../animgraphlib/CAnimActionUpdater.md)

**Relationships:**

```mermaid
classDiagram
    CAnimActionUpdater <|-- CToggleComponentActionUpdater
    CToggleComponentActionUpdater *-- AnimComponentID
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_componentID` | [AnimComponentID](../modellib/AnimComponentID.md) |  |  |
| `0x1c` | `m_bSetEnabled` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CToggleComponentActionUpdater&quot;,
	&quot;m_componentID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bSetEnabled&quot;: true
}</pre>
</details>
