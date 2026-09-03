---
title: CFlexOp
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CFlexOp

# CFlexOp

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 4 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    CFlexOp *-- FlexOpCode_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_OpCode` | [FlexOpCode_t](../modellib/FlexOpCode_t.md) |  |  |
| `0x4` | `m_Data` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_OpCode&quot;: 0,
	&quot;m_Data&quot;: 0
}</pre>
</details>
