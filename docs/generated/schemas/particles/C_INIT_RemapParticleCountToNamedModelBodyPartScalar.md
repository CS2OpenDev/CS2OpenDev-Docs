---
title: C_INIT_RemapParticleCountToNamedModelBodyPartScalar
module: particles
kind: class
---

[Schemas](../../schemas.md) / [particles](../particles.md) / C_INIT_RemapParticleCountToNamedModelBodyPartScalar

# C_INIT_RemapParticleCountToNamedModelBodyPartScalar

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 560 bytes (`0x230`) · **Align:** 8 · **Module:** particles

**Inherits from:** [C_INIT_RemapParticleCountToNamedModelElementScalar](../particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md)

**Relationships:**

```mermaid
classDiagram
    C_INIT_RemapParticleCountToNamedModelElementScalar <|-- C_INIT_RemapParticleCountToNamedModelBodyPartScalar
    C_INIT_RemapParticleCountToScalar <|-- C_INIT_RemapParticleCountToNamedModelElementScalar
    CParticleFunctionInitializer <|-- C_INIT_RemapParticleCountToScalar
    CParticleFunction <|-- CParticleFunctionInitializer
```

## Memory layout

34 fields (0 declared here, 34 inherited). Offsets are absolute from the object base.

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
| `0x1e0` | `m_nFieldOutput` | [ParticleAttributeIndex_t](../particles/ParticleAttributeIndex_t.md) | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyAttributeChoiceName particlefield_scalar` `MPropertyFriendlyName output field` |
| `0x1e4` | `m_nInputMin` | int32 | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName input minimum` |
| `0x1e8` | `m_nInputMax` | int32 | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName input maximum` |
| `0x1ec` | `m_nScaleControlPoint` | int32 | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName input scale control point` |
| `0x1f0` | `m_nScaleControlPointField` | int32 | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyAttributeChoiceName vector_component` `MPropertyFriendlyName input scale control point field` |
| `0x1f4` | `m_flOutputMin` | float32 | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName output minimum` |
| `0x1f8` | `m_flOutputMax` | float32 | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName output maximum` |
| `0x1fc` | `m_nSetMethod` | [ParticleSetMethod_t](../particleslib/ParticleSetMethod_t.md) | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName set value method` |
| `0x200` | `m_bActiveRange` | bool | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName only active within specified input range` |
| `0x201` | `m_bInvert` | bool | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName invert input from total particle count` |
| `0x202` | `m_bWrap` | bool | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName wrap input` |
| `0x204` | `m_flRemapBias` | float32 | [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md) | `MPropertyFriendlyName remap bias` |
| `0x210` | `m_hModel` | CStrongHandle< [InfoForResourceTypeCModel](../resourcesystem/InfoForResourceTypeCModel.md) > | [C_INIT_RemapParticleCountToNamedModelElementScalar](../particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) |  |
| `0x218` | `m_outputMinName` | CUtlString | [C_INIT_RemapParticleCountToNamedModelElementScalar](../particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) | `MPropertyFriendlyName output min name` |
| `0x220` | `m_outputMaxName` | CUtlString | [C_INIT_RemapParticleCountToNamedModelElementScalar](../particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) | `MPropertyFriendlyName output max name` |
| `0x228` | `m_bModelFromRenderer` | bool | [C_INIT_RemapParticleCountToNamedModelElementScalar](../particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;C_INIT_RemapParticleCountToNamedModelBodyPartScalar&quot;,
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
	&quot;m_nFieldOutput&quot;: 3,
	&quot;m_nInputMin&quot;: 0,
	&quot;m_nInputMax&quot;: 10,
	&quot;m_nScaleControlPoint&quot;: -1,
	&quot;m_nScaleControlPointField&quot;: 0,
	&quot;m_flOutputMin&quot;: 0.000000,
	&quot;m_flOutputMax&quot;: 1.000000,
	&quot;m_nSetMethod&quot;: &quot;PARTICLE_SET_REPLACE_VALUE&quot;,
	&quot;m_bActiveRange&quot;: false,
	&quot;m_bInvert&quot;: false,
	&quot;m_bWrap&quot;: false,
	&quot;m_flRemapBias&quot;: 0.500000,
	&quot;m_hModel&quot;: &quot;&quot;,
	&quot;m_outputMinName&quot;: &quot;&quot;,
	&quot;m_outputMaxName&quot;: &quot;&quot;,
	&quot;m_bModelFromRenderer&quot;: false
}</pre>
</details>
