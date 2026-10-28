---
title: CVMixInputBase
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixInputBase

# CVMixInputBase

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** soundsystem_lowlevel

**Derived by:** [CVMixControlInput](../soundsystem_lowlevel/CVMixControlInput.md), [CVMixControlMeter](../soundsystem_lowlevel/CVMixControlMeter.md), [CVMixControlOutput](../soundsystem_lowlevel/CVMixControlOutput.md), [CVMixGraphInput](../soundsystem_lowlevel/CVMixGraphInput.md), [CVMixImpulseResponseInput](../soundsystem_lowlevel/CVMixImpulseResponseInput.md), [CVMixNameInputMeter](../soundsystem_lowlevel/CVMixNameInputMeter.md)

**Relationships:**

```mermaid
classDiagram
    CVMixInputBase <|-- CVMixControlInput
    CVMixInputBase <|-- CVMixControlMeter
    CVMixInputBase <|-- CVMixControlOutput
    CVMixInputBase <|-- CVMixGraphInput
    CVMixInputBase <|-- CVMixImpulseResponseInput
    CVMixInputBase <|-- CVMixNameInputMeter
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;GameInput&quot;
}</pre>
</details>
