---
layout: default
title: SndBeatEventKeyedMidiNotes_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem](../soundsystem.md) / SndBeatEventKeyedMidiNotes_t

# SndBeatEventKeyedMidiNotes_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** soundsystem

**Inherits from:** [SndBeatEventKeys_t](../soundsystem/SndBeatEventKeys_t.md)

**Relationships:**

```mermaid
classDiagram
    SndBeatEventKeys_t <|-- SndBeatEventKeyedMidiNotes_t
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flKey` | float32 | [SndBeatEventKeys_t](../soundsystem/SndBeatEventKeys_t.md) | `MPropertyFriendlyName Key` |
| `0x10` | `m_nStatus` | uint8 |  | `MPropertyFriendlyName Status` |
| `0x11` | `m_nNote` | uint8 |  | `MPropertyFriendlyName Note` |
| `0x12` | `m_nVelocity` | uint8 |  | `MPropertyFriendlyName Velocity` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;SndBeatEventKeyedMidiNotes_t&quot;,
	&quot;m_flKey&quot;: 0.000000,
	&quot;m_nStatus&quot;: 9,
	&quot;m_nNote&quot;: 60,
	&quot;m_nVelocity&quot;: 127
}</pre>
</details>
