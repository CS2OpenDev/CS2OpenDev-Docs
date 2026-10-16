---
title: CVMixCommand
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixCommand

# CVMixCommand

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 4 · **Module:** soundsystem_lowlevel

**Relationships:**

```mermaid
classDiagram
    CVMixCommand *-- VMixGraphCommandID_t
    CVMixCommand *-- CVMixDataOffset
```

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nCommand` | [VMixGraphCommandID_t](../soundsystem_lowlevel/VMixGraphCommandID_t.md) |  | `MKV3TransferName command` |
| `0x4` | `m_nParameterNameHash` | uint32 |  | `MKV3TransferName paramName` |
| `0x8` | `m_nOutputSubmix` | [CVMixDataOffset](../soundsystem_lowlevel/CVMixDataOffset.md) |  | `MKV3TransferName outputSubmix` |
| `0xc` | `m_nInputSubmix0` | [CVMixDataOffset](../soundsystem_lowlevel/CVMixDataOffset.md) |  | `MKV3TransferName inputSubmix0` |
| `0x10` | `m_nInputSubmix1` | [CVMixDataOffset](../soundsystem_lowlevel/CVMixDataOffset.md) |  | `MKV3TransferName inputSubmix1` |
| `0x14` | `m_nProcessor` | int32 |  | `MKV3TransferName processor` |
| `0x18` | `m_nInputValue0` | [CVMixDataOffset](../soundsystem_lowlevel/CVMixDataOffset.md) |  |  |
| `0x1c` | `m_nInputValue1` | [CVMixDataOffset](../soundsystem_lowlevel/CVMixDataOffset.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;command&quot;: &quot;CMD_INVALID&quot;,
	&quot;paramName&quot;: 0,
	&quot;outputSubmix&quot;:
	{
		&quot;category&quot;: &quot;NULL_POINTER&quot;,
		&quot;type&quot;: &quot;VO_CHAR&quot;,
		&quot;index&quot;: 0
	},
	&quot;inputSubmix0&quot;:
	{
		&quot;category&quot;: &quot;NULL_POINTER&quot;,
		&quot;type&quot;: &quot;VO_CHAR&quot;,
		&quot;index&quot;: 0
	},
	&quot;inputSubmix1&quot;:
	{
		&quot;category&quot;: &quot;NULL_POINTER&quot;,
		&quot;type&quot;: &quot;VO_CHAR&quot;,
		&quot;index&quot;: 0
	},
	&quot;processor&quot;: -1,
	&quot;m_nInputValue0&quot;:
	{
		&quot;category&quot;: &quot;NULL_POINTER&quot;,
		&quot;type&quot;: &quot;VO_CHAR&quot;,
		&quot;index&quot;: 0
	},
	&quot;m_nInputValue1&quot;:
	{
		&quot;category&quot;: &quot;NULL_POINTER&quot;,
		&quot;type&quot;: &quot;VO_CHAR&quot;,
		&quot;index&quot;: 0
	}
}</pre>
</details>
