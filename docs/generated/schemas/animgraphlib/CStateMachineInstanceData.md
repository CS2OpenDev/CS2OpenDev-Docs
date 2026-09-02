---
layout: default
title: CStateMachineInstanceData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CStateMachineInstanceData

# CStateMachineInstanceData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 28 bytes (`0x1c`) · **Align:** 4 · **Module:** animgraphlib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flTimeInState` | float32 |  |  |
| `0x4` | `m_currentTransitionIndex` | CAnimNetVar< int32 > |  |  |
| `0x10` | `m_prevStateIndex` | int32 |  |  |
| `0x14` | `m_scheduledTransitionIndex` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flTimeInState&quot;: 0.000000,
	&quot;m_currentTransitionIndex&quot;: -1,
	&quot;m_prevStateIndex&quot;: -1,
	&quot;m_scheduledTransitionIndex&quot;: -1
}</pre>
</details>
