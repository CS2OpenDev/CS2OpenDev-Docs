---
title: CFlexRule
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CFlexRule

# CFlexRule

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    CFlexRule *-- CFlexOp
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nFlex` | int32 |  |  |
| `0x8` | `m_FlexOps` | CUtlVector< [CFlexOp](../modellib/CFlexOp.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nFlex&quot;: 0,
	&quot;m_FlexOps&quot;:
	[
	]
}</pre>
</details>
