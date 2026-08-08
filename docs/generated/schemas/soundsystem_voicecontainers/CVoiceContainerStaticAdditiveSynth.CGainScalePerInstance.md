---
layout: default
title: "CVoiceContainerStaticAdditiveSynth::CGainScalePerInstance"
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_voicecontainers](../soundsystem_voicecontainers.md) / CVoiceContainerStaticAdditiveSynth::CGainScalePerInstance

# CVoiceContainerStaticAdditiveSynth::CGainScalePerInstance

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 4 · **Module:** soundsystem_voicecontainers

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flMinVolume` | float32 |  | `MPropertyFriendlyName Quietest Volume` |
| `0x4` | `m_nInstancesAtMinVolume` | int32 |  | `MPropertyFriendlyName # Instances Playing Until We Get Louder Than Quietest Volume` |
| `0x8` | `m_flMaxVolume` | float32 |  | `MPropertyFriendlyName Loudest Volume` |
| `0xc` | `m_nInstancesAtMaxVolume` | int32 |  | `MPropertyFriendlyName # Instances Playing Required To Reach Loudest Volume` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flMinVolume&quot;: 1.000000,
	&quot;m_nInstancesAtMinVolume&quot;: 1,
	&quot;m_flMaxVolume&quot;: 1.000000,
	&quot;m_nInstancesAtMaxVolume&quot;: 1
}</pre>
</details>
