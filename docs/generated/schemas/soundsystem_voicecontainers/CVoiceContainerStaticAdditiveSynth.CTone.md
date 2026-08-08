---
layout: default
title: "CVoiceContainerStaticAdditiveSynth::CTone"
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_voicecontainers](../soundsystem_voicecontainers.md) / CVoiceContainerStaticAdditiveSynth::CTone

# CVoiceContainerStaticAdditiveSynth::CTone

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** soundsystem_voicecontainers

**Relationships:**

```mermaid
classDiagram
    "CVoiceContainerStaticAdditiveSynth::CTone" *-- CVoiceContainerStaticAdditiveSynth
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_harmonics` | CUtlVector< [CVoiceContainerStaticAdditiveSynth](../soundsystem_voicecontainers/CVoiceContainerStaticAdditiveSynth.md)::CHarmonic > |  | `MPropertyFriendlyName Harmonics` |
| `0x18` | `m_curve` | CPiecewiseCurve |  | `MPropertyFriendlyName Envelope` |
| `0x58` | `m_bSyncInstances` | bool |  | `MPropertyFriendlyName Play All Instances In Sync` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_harmonics&quot;:
	[
	],
	&quot;m_curve&quot;:
	{
		&quot;m_spline&quot;:
		[
		],
		&quot;m_tangents&quot;:
		[
		],
		&quot;m_vDomainMins&quot;:
		[
			0.000000,
			0.000000
		],
		&quot;m_vDomainMaxs&quot;:
		[
			0.000000,
			0.000000
		]
	},
	&quot;m_bSyncInstances&quot;: false
}</pre>
</details>
