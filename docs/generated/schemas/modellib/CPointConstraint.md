---
layout: default
title: CPointConstraint
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CPointConstraint

# CPointConstraint

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** modellib

**Inherits from:** [CBaseConstraint](../modellib/CBaseConstraint.md)

**Relationships:**

```mermaid
classDiagram
    CBaseConstraint <|-- CPointConstraint
    CBoneConstraintBase <|-- CBaseConstraint
```

## Memory layout

4 fields (0 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_name` | CUtlString | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |
| `0x28` | `m_vUpVector` | Vector | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |
| `0x38` | `m_slaves` | CUtlLeanVector< [CConstraintSlave](../modellib/CConstraintSlave.md) > | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |
| `0x48` | `m_targets` | CUtlVector< [CConstraintTarget](../modellib/CConstraintTarget.md) > | [CBaseConstraint](../modellib/CBaseConstraint.md) |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CPointConstraint&quot;,
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
	]
}</pre>
</details>
