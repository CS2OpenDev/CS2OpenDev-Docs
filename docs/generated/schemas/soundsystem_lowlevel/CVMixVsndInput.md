---
title: CVMixVsndInput
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixVsndInput

# CVMixVsndInput

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Inherits from:** [CVMixInputBase](../soundsystem_lowlevel/CVMixInputBase.md)

**Relationships:**

```mermaid
classDiagram
    CVMixInputBase <|-- CVMixVsndInput
```

## Memory layout

3 fields (2 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString | [CVMixInputBase](../soundsystem_lowlevel/CVMixInputBase.md) |  |
| `0x10` | `m_defaultValue` | CUtlString |  |  |
| `0x18` | `m_nProcessor` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;GameInput&quot;,
	&quot;m_defaultValue&quot;: &quot;&quot;,
	&quot;m_nProcessor&quot;: -1
}</pre>
</details>
