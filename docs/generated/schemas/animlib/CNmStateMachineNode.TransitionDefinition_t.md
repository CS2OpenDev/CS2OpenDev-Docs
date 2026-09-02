---
layout: default
title: "CNmStateMachineNode::TransitionDefinition_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmStateMachineNode::TransitionDefinition_t

# CNmStateMachineNode::TransitionDefinition_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 2 · **Module:** animlib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nTargetStateIdx` | int16 |  |  |
| `0x2` | `m_nConditionNodeIdx` | int16 |  |  |
| `0x4` | `m_nTransitionNodeIdx` | int16 |  |  |
| `0x6` | `m_bCanBeForced` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nTargetStateIdx&quot;: -1,
	&quot;m_nConditionNodeIdx&quot;: -1,
	&quot;m_nTransitionNodeIdx&quot;: -1,
	&quot;m_bCanBeForced&quot;: false
}</pre>
</details>
