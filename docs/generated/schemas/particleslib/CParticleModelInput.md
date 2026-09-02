---
layout: default
title: CParticleModelInput
nav_exclude: true
---

[Schemas](../../schemas.md) / [particleslib](../particleslib.md) / CParticleModelInput

# CParticleModelInput

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** particleslib

**Inherits from:** [CParticleInput](../particleslib/CParticleInput.md)

**Metadata:** `MCustomFGDMetadata { KV3DefaultTestFnName = 'CParticleModelInputDefaultTestFunc' }`, `MPropertyCustomEditor ModelInput()`

**Relationships:**

```mermaid
classDiagram
    CParticleInput <|-- CParticleModelInput
    CParticleModelInput *-- ParticleModelType_t
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_nType` | [ParticleModelType_t](../particleslib/ParticleModelType_t.md) |  |  |
| `0x18` | `m_NamedValue` | CParticleNamedValueRef |  |  |
| `0x58` | `m_nControlPoint` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nType&quot;: &quot;PM_TYPE_INVALID&quot;,
	&quot;m_NamedValue&quot;: &quot;&quot;,
	&quot;m_nControlPoint&quot;: -1
}</pre>
</details>
