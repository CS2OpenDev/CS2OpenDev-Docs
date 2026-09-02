---
title: CExplosionTypeData (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CExplosionTypeData

# CExplosionTypeData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 256 bytes (`0x100`) · **Align:** 8 · **Module:** client

**Twin:** [CExplosionTypeData (server)](../server/CExplosionTypeData.md)

**Metadata:** `MVDataAssociatedFile scripts/explosion_types.vdata`, `MVDataOverlayType 1`, `MVDataRoot`

**Relationships:**

```mermaid
classDiagram
    CExplosionTypeData *-- InfoForResourceTypeIParticleSystemDefinition
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_SoundName` | CSoundEventName |  |  |
| `0x10` | `m_ParticleEffect` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../resourcesystem/InfoForResourceTypeIParticleSystemDefinition.md) > > |  |  |
| `0xf0` | `m_bIsIncindiary` | bool |  | `MPropertyDescription Whether this explosion relates to fire` |
| `0xf1` | `m_bHasForces` | bool |  | `MPropertyDescription Whether this explosion has explosive forces` |
| `0xf8` | `m_DecalType` | CGlobalSymbol |  | `MPropertyDescription Decal to use when this explosion occurs` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_SoundName&quot;: &quot;&quot;,
	&quot;m_ParticleEffect&quot;: &quot;&quot;,
	&quot;m_bIsIncindiary&quot;: false,
	&quot;m_bHasForces&quot;: false,
	&quot;m_DecalType&quot;: &quot;Scorch&quot;
}</pre>
</details>
