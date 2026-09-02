---
title: VMixPannerDesc_t
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixPannerDesc_t

# VMixPannerDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 4 · **Module:** soundsystem_lowlevel

**Relationships:**

```mermaid
classDiagram
    VMixPannerDesc_t *-- VMixPannerType_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_type` | [VMixPannerType_t](../soundsystem_lowlevel/VMixPannerType_t.md) |  |  |
| `0x4` | `m_flStrength` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_type&quot;: &quot;PANNER_TYPE_LINEAR&quot;,
	&quot;m_flStrength&quot;: 0.000000
}</pre>
</details>
