---
layout: default
title: C_INIT_StatusEffect
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / C_INIT_StatusEffect

# C_INIT_StatusEffect

**Kind:** class · **Size:** 576 bytes (`0x240`) · **Align:** 8 · **Module:** particles

**Inherits from:** [CParticleFunctionInitializer](../particles/CParticleFunctionInitializer.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunctionInitializer <|-- C_INIT_StatusEffect
    CParticleFunction <|-- CParticleFunctionInitializer
    C_INIT_StatusEffect *-- Detail2Combo_t
```

## Memory layout

36 fields (18 declared here, 18 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flOpStrength` | [CParticleCollectionFloatInput](../particleslib/CParticleCollectionFloatInput.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator strength` `MPropertySortPriority -100` |
| `0x178` | `m_nOpEndCapState` | [ParticleEndcapMode_t](../particles/ParticleEndcapMode_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator end cap state` `MPropertySortPriority -100` |
| `0x17c` | `m_nToolsState` | [ParticleToolsState_t](../particles/ParticleToolsState_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator enabled in tools or game only` `MPropertySortPriority -100` |
| `0x180` | `m_flOpStartFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadein` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade` |
| `0x184` | `m_flOpEndFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadein` `MPropertySortPriority -100` |
| `0x188` | `m_flOpStartFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadeout` `MPropertySortPriority -100` |
| `0x18c` | `m_flOpEndFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadeout` `MPropertySortPriority -100` |
| `0x190` | `m_flOpFadeOscillatePeriod` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade oscillate` `MPropertySortPriority -100` |
| `0x194` | `m_bNormalizeToStopTime` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName normalize fade times to endcap` `MPropertySortPriority -100` |
| `0x198` | `m_flOpTimeOffsetMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset min` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Time Offset` |
| `0x19c` | `m_flOpTimeOffsetMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset max` `MPropertySortPriority -100` |
| `0x1a0` | `m_nOpTimeOffsetSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset seed` `MPropertySortPriority -100` |
| `0x1a4` | `m_nOpTimeScaleSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale seed` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Timescale Modifiers` |
| `0x1a8` | `m_flOpTimeScaleMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale min` `MPropertySortPriority -100` |
| `0x1ac` | `m_flOpTimeScaleMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale max` `MPropertySortPriority -100` |
| `0x1b2` | `m_bDisableOperator` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyStartGroup` `MPropertySuppressField` |
| `0x1b8` | `m_Notes` | CUtlString | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleHelpField` `MPropertyFriendlyName operator help and notes` `MPropertySortPriority -100` |
| `0x1d8` | `m_nAssociatedEmitterIndex` | int32 | [CParticleFunctionInitializer](../particles/CParticleFunctionInitializer.md) | `MPropertyFriendlyName Associated emitter Index` |
| `0x1e0` | `m_nDetail2Combo` | [Detail2Combo_t](../particles/Detail2Combo_t.md) |  | `MPropertyFriendlyName D_DETAIL_2` |
| `0x1e4` | `m_flDetail2Rotation` | float32 |  | `MPropertyFriendlyName $DETAIL2ROTATION` |
| `0x1e8` | `m_flDetail2Scale` | float32 |  | `MPropertyFriendlyName $DETAIL2SCALE` |
| `0x1ec` | `m_flDetail2BlendFactor` | float32 |  | `MPropertyFriendlyName $DETAIL2BLENDFACTOR` |
| `0x1f0` | `m_flColorWarpIntensity` | float32 |  | `MPropertyFriendlyName $COLORWARPINTENSITY` |
| `0x1f4` | `m_flDiffuseWarpBlendToFull` | float32 |  | `MPropertyFriendlyName $DIFFUSEWARPBLENDTOFULL` |
| `0x1f8` | `m_flEnvMapIntensity` | float32 |  | `MPropertyFriendlyName $ENVMAPINTENSITY` |
| `0x1fc` | `m_flAmbientScale` | float32 |  | `MPropertyFriendlyName $AMBIENTSCALE` |
| `0x200` | `m_specularColor` | Color |  | `MPropertyFriendlyName $SPECULARCOLOR` |
| `0x204` | `m_flSpecularScale` | float32 |  | `MPropertyFriendlyName $SPECULARSCALE` |
| `0x208` | `m_flSpecularExponent` | float32 |  | `MPropertyFriendlyName $SPECULAREXPONENT` |
| `0x20c` | `m_flSpecularExponentBlendToFull` | float32 |  | `MPropertyFriendlyName $SPECULAREXPONENTBLENDTOFULL` |
| `0x210` | `m_flSpecularBlendToFull` | float32 |  | `MPropertyFriendlyName $SPECULARBLENDTOFULL` |
| `0x214` | `m_rimLightColor` | Color |  | `MPropertyFriendlyName $RIMLIGHTCOLOR` |
| `0x218` | `m_flRimLightScale` | float32 |  | `MPropertyFriendlyName $RIMLIGHTSCALE` |
| `0x21c` | `m_flReflectionsTintByBaseBlendToNone` | float32 |  | `MPropertyFriendlyName $REFLECTIONSTINTBYBASEBLENDTONONE` |
| `0x220` | `m_flMetalnessBlendToFull` | float32 |  | `MPropertyFriendlyName $METALNESSBLENDTOFULL` |
| `0x224` | `m_flSelfIllumBlendToFull` | float32 |  | `MPropertyFriendlyName $SELFILLUMBLENDTOFULL` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;C_INIT_StatusEffect&quot;,
	&quot;m_flOpStrength&quot;:
	{
		&quot;m_nType&quot;: &quot;PF_TYPE_LITERAL&quot;,
		&quot;m_nMapType&quot;: &quot;PF_MAP_TYPE_DIRECT&quot;,
		&quot;m_flLiteralValue&quot;: 1.000000,
		&quot;m_NamedValue&quot;: &quot;&quot;,
		&quot;m_nControlPoint&quot;: 0,
		&quot;m_nScalarAttribute&quot;: 3,
		&quot;m_nVectorAttribute&quot;: 6,
		&quot;m_nVectorComponent&quot;: 0,
		&quot;m_bReverseOrder&quot;: false,
		&quot;m_flRandomMin&quot;: 0.000000,
		&quot;m_flRandomMax&quot;: 1.000000,
		&quot;m_bHasRandomSignFlip&quot;: false,
		&quot;m_nRandomSeed&quot;: &lt;HIDDEN FOR DIFF&gt;,
		&quot;m_nRandomMode&quot;: &quot;PF_RANDOM_MODE_CONSTANT&quot;,
		&quot;m_strSnapshotSubset&quot;: &quot;&quot;,
		&quot;m_flLOD0&quot;: 0.000000,
		&quot;m_flLOD1&quot;: 0.000000,
		&quot;m_flLOD2&quot;: 0.000000,
		&quot;m_flLOD3&quot;: 0.000000,
		&quot;m_nNoiseInputVectorAttribute&quot;: 0,
		&quot;m_flNoiseOutputMin&quot;: 0.000000,
		&quot;m_flNoiseOutputMax&quot;: 1.000000,
		&quot;m_flNoiseScale&quot;: 0.100000,
		&quot;m_vecNoiseOffsetRate&quot;:
		[
			0.000000,
			0.000000,
			0.000000
		],
		&quot;m_flNoiseOffset&quot;: 0.000000,
		&quot;m_nNoiseOctaves&quot;: 1,
		&quot;m_nNoiseTurbulence&quot;: &quot;PF_NOISE_TURB_NONE&quot;,
		&quot;m_nNoiseType&quot;: &quot;PF_NOISE_TYPE_PERLIN&quot;,
		&quot;m_nNoiseModifier&quot;: &quot;PF_NOISE_MODIFIER_NONE&quot;,
		&quot;m_flNoiseTurbulenceScale&quot;: 1.000000,
		&quot;m_flNoiseTurbulenceMix&quot;: 0.500000,
		&quot;m_flNoiseImgPreviewScale&quot;: 1.000000,
		&quot;m_bNoiseImgPreviewLive&quot;: true,
		&quot;m_flNoCameraFallback&quot;: 0.000000,
		&quot;m_bUseBoundsCenter&quot;: false,
		&quot;m_nInputMode&quot;: &quot;PF_INPUT_MODE_CLAMPED&quot;,
		&quot;m_flMultFactor&quot;: 1.000000,
		&quot;m_flInput0&quot;: 0.000000,
		&quot;m_flInput1&quot;: 1.000000,
		&quot;m_flOutput0&quot;: 0.000000,
		&quot;m_flOutput1&quot;: 1.000000,
		&quot;m_flNotchedRangeMin&quot;: 0.000000,
		&quot;m_flNotchedRangeMax&quot;: 1.000000,
		&quot;m_flNotchedOutputOutside&quot;: 0.000000,
		&quot;m_flNotchedOutputInside&quot;: 1.000000,
		&quot;m_nRoundType&quot;: &quot;PF_ROUND_TYPE_NEAREST&quot;,
		&quot;m_nBiasType&quot;: &quot;PF_BIAS_TYPE_STANDARD&quot;,
		&quot;m_flBiasParameter&quot;: 0.000000,
		&quot;m_Curve&quot;:
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
		}
	},
	&quot;m_nOpEndCapState&quot;: &quot;PARTICLE_ENDCAP_ALWAYS_ON&quot;,
	&quot;m_nToolsState&quot;: &quot;PARTICLE_TOOLS_STATE_ALWAYS_ON&quot;,
	&quot;m_flOpStartFadeInTime&quot;: 0.000000,
	&quot;m_flOpEndFadeInTime&quot;: 0.000000,
	&quot;m_flOpStartFadeOutTime&quot;: 0.000000,
	&quot;m_flOpEndFadeOutTime&quot;: 0.000000,
	&quot;m_flOpFadeOscillatePeriod&quot;: 0.000000,
	&quot;m_bNormalizeToStopTime&quot;: false,
	&quot;m_flOpTimeOffsetMin&quot;: 0.000000,
	&quot;m_flOpTimeOffsetMax&quot;: 0.000000,
	&quot;m_nOpTimeOffsetSeed&quot;: 0,
	&quot;m_nOpTimeScaleSeed&quot;: 0,
	&quot;m_flOpTimeScaleMin&quot;: 1.000000,
	&quot;m_flOpTimeScaleMax&quot;: 1.000000,
	&quot;m_bDisableOperator&quot;: false,
	&quot;m_Notes&quot;: &quot;&quot;,
	&quot;m_nAssociatedEmitterIndex&quot;: -1,
	&quot;m_nDetail2Combo&quot;: &quot;DETAIL_2_COMBO_UNINITIALIZED&quot;,
	&quot;m_flDetail2Rotation&quot;: -1.000000,
	&quot;m_flDetail2Scale&quot;: -1.000000,
	&quot;m_flDetail2BlendFactor&quot;: -1.000000,
	&quot;m_flColorWarpIntensity&quot;: -1.000000,
	&quot;m_flDiffuseWarpBlendToFull&quot;: -1.000000,
	&quot;m_flEnvMapIntensity&quot;: -1.000000,
	&quot;m_flAmbientScale&quot;: -1.000000,
	&quot;m_specularColor&quot;:
	[
		0,
		0,
		0
	],
	&quot;m_flSpecularScale&quot;: -1.000000,
	&quot;m_flSpecularExponent&quot;: -1.000000,
	&quot;m_flSpecularExponentBlendToFull&quot;: -1.000000,
	&quot;m_flSpecularBlendToFull&quot;: -1.000000,
	&quot;m_rimLightColor&quot;:
	[
		0,
		0,
		0
	],
	&quot;m_flRimLightScale&quot;: -1.000000,
	&quot;m_flReflectionsTintByBaseBlendToNone&quot;: -1.000000,
	&quot;m_flMetalnessBlendToFull&quot;: -1.000000,
	&quot;m_flSelfIllumBlendToFull&quot;: -1.000000
}</pre>
</details>
