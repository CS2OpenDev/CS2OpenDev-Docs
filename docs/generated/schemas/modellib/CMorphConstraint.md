---
title: CMorphConstraint
module: modellib
kind: class
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CMorphConstraint

# CMorphConstraint

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** modellib

**Inherits from:** [CBaseConstraint](../modellib/CBaseConstraint.md)

**Relationships:**

```mermaid
classDiagram
    CBaseConstraint <|-- CMorphConstraint
    CBoneConstraintBase <|-- CBaseConstraint
```

## Memory layout

8 fields (4 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_name` | CUtlString | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |
| `0x28` | `m_vUpVector` | Vector | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |
| `0x38` | `m_slaves` | CUtlLeanVector< [CConstraintSlave](../modellib/CConstraintSlave.md) > | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |
| `0x48` | `m_targets` | CUtlVector< [CConstraintTarget](../modellib/CConstraintTarget.md) > | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |
| `0x60` | `m_sTargetMorph` | CUtlString |  |  |
| `0x68` | `m_nSlaveChannel` | int32 |  |  |
| `0x6c` | `m_flMin` | float32 |  |  |
| `0x70` | `m_flMax` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMorphConstraint&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_vUpVector&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_slaves&quot;:
	[
	],
	&quot;m_targets&quot;:
	[
	],
	&quot;m_sTargetMorph&quot;: &quot;&quot;,
	&quot;m_nSlaveChannel&quot;: 0,
	&quot;m_flMin&quot;: 0.000000,
	&quot;m_flMax&quot;: 1.000000
}</pre>
</details>
