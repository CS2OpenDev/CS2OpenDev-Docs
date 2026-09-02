---
layout: default
title: EngineCountdownTimer (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / EngineCountdownTimer

# EngineCountdownTimer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** client

**Twin:** [EngineCountdownTimer (server)](../server/EngineCountdownTimer.md)

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_duration` | float32 |  |  |
| `0xc` | `m_timestamp` | float32 |  | `MKV3TransferSaveOpsForField GetEngineTimeSaveRestoreOps` |
| `0x10` | `m_timescale` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>null</pre>
</details>
