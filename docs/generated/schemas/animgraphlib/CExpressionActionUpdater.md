---
title: CExpressionActionUpdater
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CExpressionActionUpdater

# CExpressionActionUpdater

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CAnimActionUpdater](../animgraphlib/CAnimActionUpdater.md)

**Relationships:**

```mermaid
classDiagram
    CAnimActionUpdater <|-- CExpressionActionUpdater
    CExpressionActionUpdater *-- CAnimParamHandle
    CExpressionActionUpdater *-- AnimParamType_t
    CExpressionActionUpdater *-- AnimScriptHandle
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_hParam` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x1a` | `m_eParamType` | [AnimParamType_t](../animgraphlib/AnimParamType_t.md) |  |  |
| `0x1c` | `m_hScript` | [AnimScriptHandle](../modellib/AnimScriptHandle.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CExpressionActionUpdater&quot;,
	&quot;m_hParam&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_eParamType&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
	&quot;m_hScript&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	}
}</pre>
</details>
