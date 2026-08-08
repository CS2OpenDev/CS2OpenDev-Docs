---
layout: default
title: CPhysSurfacePropertiesAudio
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CPhysSurfacePropertiesAudio

# CPhysSurfacePropertiesAudio

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 4 · **Module:** modellib

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_reflectivity` | float32 |  | `MKV3TransferName audioreflectivity` |
| `0x4` | `m_hardnessFactor` | float32 |  | `MKV3TransferName audiohardnessfactor` |
| `0x8` | `m_roughnessFactor` | float32 |  | `MKV3TransferName audioroughnessfactor` |
| `0xc` | `m_roughThreshold` | float32 |  | `MKV3TransferName scrapeRoughThreshold` |
| `0x10` | `m_hardThreshold` | float32 |  | `MKV3TransferName impactHardThreshold` |
| `0x14` | `m_hardVelocityThreshold` | float32 |  | `MKV3TransferName audioHardMinVelocity` |
| `0x18` | `m_flStaticImpactVolume` | float32 |  | `MKV3TransferName staticImpactVolume` |
| `0x1c` | `m_flOcclusionFactor` | float32 |  | `MKV3TransferName occlusionFactor` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;audioreflectivity&quot;: 0.000000,
	&quot;audiohardnessfactor&quot;: 0.000000,
	&quot;audioroughnessfactor&quot;: 0.000000,
	&quot;scrapeRoughThreshold&quot;: 0.000000,
	&quot;impactHardThreshold&quot;: 0.000000,
	&quot;audioHardMinVelocity&quot;: 0.000000,
	&quot;staticImpactVolume&quot;: 0.000000,
	&quot;occlusionFactor&quot;: 0.000000
}</pre>
</details>
