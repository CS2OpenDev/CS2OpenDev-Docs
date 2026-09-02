---
title: SoundCommand_t
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / SoundCommand_t

# SoundCommand_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** server

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_time` | float32 |  |  |
| `0xc` | `m_deltaTime` | float32 |  |  |
| `0x10` | `m_command` | soundcommands_t |  |  |
| `0x14` | `m_value` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_time&quot;: 0.000000,
	&quot;m_deltaTime&quot;: 0.000000,
	&quot;m_command&quot;: &quot;SOUNDCTRL_CHANGE_VOLUME&quot;,
	&quot;m_value&quot;: 0.000000
}</pre>
</details>
