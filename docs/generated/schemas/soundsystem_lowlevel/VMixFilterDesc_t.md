---
title: VMixFilterDesc_t
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixFilterDesc_t

# VMixFilterDesc_t

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 4 · **Module:** soundsystem_lowlevel

**Derived by:** [VMixEQFilterDesc_t](../soundsystem_lowlevel/VMixEQFilterDesc_t.md)

**Relationships:**

```mermaid
classDiagram
    VMixFilterDesc_t <|-- VMixEQFilterDesc_t
    VMixFilterDesc_t *-- VMixFilterType_t
    VMixFilterDesc_t *-- VMixFilterSlope_t
```

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_fldbGain` | float32 |  |  |
| `0x4` | `m_flCutoffFreq` | float32 |  |  |
| `0x8` | `m_flQ` | float32 |  |  |
| `0xc` | `m_nFilterType` | [VMixFilterType_t](../soundsystem_lowlevel/VMixFilterType_t.md) |  |  |
| `0xd` | `m_nFilterSlope` | [VMixFilterSlope_t](../soundsystem_lowlevel/VMixFilterSlope_t.md) |  |  |
| `0xe` | `m_bEnabled` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_fldbGain&quot;: 0.000000,
	&quot;m_flCutoffFreq&quot;: 1000.000000,
	&quot;m_flQ&quot;: 0.707107,
	&quot;m_nFilterType&quot;: &quot;FILTER_UNKNOWN&quot;,
	&quot;m_nFilterSlope&quot;: &quot;FILTER_SLOPE_12dB&quot;,
	&quot;m_bEnabled&quot;: true
}</pre>
</details>
