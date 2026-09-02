---
title: CFeMorphLayer
module: physicslib
kind: class
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / CFeMorphLayer

# CFeMorphLayer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 136 bytes (`0x88`) · **Align:** 8 · **Module:** physicslib

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Name` | CUtlString |  |  |
| `0x8` | `m_nNameHash` | uint32 |  |  |
| `0x10` | `m_Nodes` | CUtlVector< uint16 > |  |  |
| `0x28` | `m_InitPos` | CUtlVector< Vector > |  |  |
| `0x40` | `m_Gravity` | CUtlVector< float32 > |  |  |
| `0x58` | `m_GoalStrength` | CUtlVector< float32 > |  |  |
| `0x70` | `m_GoalDamping` | CUtlVector< float32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_nNameHash&quot;: 0,
	&quot;m_Nodes&quot;:
	[
	],
	&quot;m_InitPos&quot;:
	[
	],
	&quot;m_Gravity&quot;:
	[
	],
	&quot;m_GoalStrength&quot;:
	[
	],
	&quot;m_GoalDamping&quot;:
	[
	]
}</pre>
</details>
