---
layout: default
title: FootStepTrigger
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / FootStepTrigger

# FootStepTrigger

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

**Relationships:**

```mermaid
classDiagram
    FootStepTrigger *-- StepPhase
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_tags` | CUtlVector< int32 > |  |  |
| `0x18` | `m_nFootIndex` | int32 |  |  |
| `0x1c` | `m_triggerPhase` | [StepPhase](../animgraphlib/StepPhase.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_tags&quot;:
	[
	],
	&quot;m_nFootIndex&quot;: -1,
	&quot;m_triggerPhase&quot;: &quot;StepPhase_OnGround&quot;
}</pre>
</details>
