---
title: CBaseRendererSource2
module: particles
kind: class
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CBaseRendererSource2

# CBaseRendererSource2

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 11992 bytes (`0x2ed8`) · **Align:** n/a (unspecified) · **Module:** particles

**Inherits from:** [CParticleFunctionRenderer](../particles/CParticleFunctionRenderer.md)

**Derived by:** [CBaseTrailRenderer](../particles/CBaseTrailRenderer.md), [C_OP_RenderRopes](../particles/C_OP_RenderRopes.md), [C_OP_RenderSprites](../particles/C_OP_RenderSprites.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunctionRenderer <|-- CBaseRendererSource2
    CParticleFunction <|-- CParticleFunctionRenderer
    CBaseRendererSource2 <|-- CBaseTrailRenderer
    CBaseRendererSource2 <|-- C_OP_RenderRopes
    CBaseRendererSource2 <|-- C_OP_RenderSprites
    CBaseRendererSource2 *-- CParticleCollectionRendererFloatInput
    CBaseRendererSource2 *-- ParticleAttributeIndex_t
    CBaseRendererSource2 *-- CParticleCollectionRendererVecInput
    CBaseRendererSource2 *-- ParticleColorBlendType_t
    CBaseRendererSource2 *-- SpriteCardShaderType_t
    CBaseRendererSource2 *-- ParticleSequenceCropOverride_t
    CBaseRendererSource2 *-- TextureGroup_t
    CBaseRendererSource2 *-- AnimationType_t
    CBaseRendererSource2 *-- ParticleOutputBlendMode_t
    CBaseRendererSource2 *-- ParticleFogType_t
```

## Memory layout

84 fields (65 declared here, 19 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flOpStrength` | [CParticleCollectionFloatInput](../particleslib/CParticleCollectionFloatInput.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator strength` `MPropertySortPriority -100` |
| `0x180` | `m_nOpEndCapState` | [ParticleEndcapMode_t](../particles/ParticleEndcapMode_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator end cap state` `MPropertySortPriority -100` |
| `0x184` | `m_nToolsState` | [ParticleToolsState_t](../particles/ParticleToolsState_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator enabled in tools or game only` `MPropertySortPriority -100` |
| `0x188` | `m_flOpStartFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadein` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade` |
| `0x18c` | `m_flOpEndFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadein` `MPropertySortPriority -100` |
| `0x190` | `m_flOpStartFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadeout` `MPropertySortPriority -100` |
| `0x194` | `m_flOpEndFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadeout` `MPropertySortPriority -100` |
| `0x198` | `m_flOpFadeOscillatePeriod` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade oscillate` `MPropertySortPriority -100` |
| `0x19c` | `m_bNormalizeToStopTime` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName normalize fade times to endcap` `MPropertySortPriority -100` |
| `0x1a0` | `m_flOpTimeOffsetMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset min` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Time Offset` |
| `0x1a4` | `m_flOpTimeOffsetMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset max` `MPropertySortPriority -100` |
| `0x1a8` | `m_nOpTimeOffsetSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset seed` `MPropertySortPriority -100` |
| `0x1ac` | `m_nOpTimeScaleSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale seed` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Timescale Modifiers` |
| `0x1b0` | `m_flOpTimeScaleMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale min` `MPropertySortPriority -100` |
| `0x1b4` | `m_flOpTimeScaleMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale max` `MPropertySortPriority -100` |
| `0x1ba` | `m_bDisableOperator` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyStartGroup` `MPropertySuppressField` |
| `0x1c0` | `m_Notes` | CUtlString | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleHelpField` `MPropertyAttributeEditor TextBlock()` `MPropertyFriendlyName operator help and notes` `MPropertySortPriority -100` |
| `0x1e0` | `VisibilityInputs` | [CParticleVisibilityInputs](../particles/CParticleVisibilityInputs.md) | [CParticleFunctionRenderer](../particles/CParticleFunctionRenderer.md) | `MPropertySortPriority -1` |
| `0x228` | `m_bCannotBeRefracted` | bool | [CParticleFunctionRenderer](../particles/CParticleFunctionRenderer.md) | `MPropertyFriendlyName I cannot be refracted through refracting objects like water` `MPropertySortPriority -1` `MPropertyStartGroup Rendering filter` |
| `0x230` | `m_flRadiusScale` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName radius scale` `MPropertySortPriority 700` `MPropertyStartGroup +Renderer Modifiers` |
| `0x3a8` | `m_flAlphaScale` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName alpha scale` `MPropertySortPriority 700` |
| `0x520` | `m_flRollScale` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName rotation roll scale` `MPropertySortPriority 700` |
| `0x698` | `m_nAlpha2Field` | [ParticleAttributeIndex_t](../particleslib/ParticleAttributeIndex_t.md) |  | `MPropertyAttributeChoiceName particlefield_scalar` `MPropertyFriendlyName per-particle alpha scale attribute` `MPropertySortPriority 700` |
| `0x6a0` | `m_vecColorScale` | [CParticleCollectionRendererVecInput](../particleslib/CParticleCollectionRendererVecInput.md) |  | `MPropertyFriendlyName color blend` `MPropertySortPriority 700` |
| `0xd78` | `m_nColorBlendType` | [ParticleColorBlendType_t](../particleslib/ParticleColorBlendType_t.md) |  | `MPropertyFriendlyName color blend type` `MPropertySortPriority 700` |
| `0xd7c` | `m_nShaderType` | [SpriteCardShaderType_t](../particles/SpriteCardShaderType_t.md) |  | `MPropertyFriendlyName Shader` `MPropertySortPriority 600` `MPropertyStartGroup +Material` |
| `0xd80` | `m_strShaderOverride` | CUtlString |  | `MPropertyFriendlyName Custom Shader` `MPropertySortPriority 600` `MPropertySuppressExpr m_nShaderType != SPRITECARD_SHADER_CUSTOM` |
| `0xd88` | `m_flCenterXOffset` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName X offset of center point` `MPropertySortPriority 600` |
| `0xf00` | `m_flCenterYOffset` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName Y offset of center point` `MPropertySortPriority 600` |
| `0x1078` | `m_flBumpStrength` | float32 |  | `MPropertyFriendlyName Bump Strength` `MPropertySortPriority 600` |
| `0x107c` | `m_nCropTextureOverride` | [ParticleSequenceCropOverride_t](../particles/ParticleSequenceCropOverride_t.md) |  | `MPropertyFriendlyName Sheet Crop Behavior` `MPropertySortPriority 600` |
| `0x1080` | `m_vecTexturesInput` | CUtlLeanVector< [TextureGroup_t](../particles/TextureGroup_t.md) > |  | `MParticleRequireDefaultArrayEntry` `MPropertyAutoExpandSelf` `MPropertyFriendlyName Textures` `MPropertySortPriority 600` |
| `0x1090` | `m_flAnimationRate` | float32 |  | `MPropertyAttributeRange 0 5` `MPropertyFriendlyName animation rate` `MPropertySortPriority 500` `MPropertyStartGroup Animation` |
| `0x1094` | `m_nAnimationType` | [AnimationType_t](../particleslib/AnimationType_t.md) |  | `MPropertyFriendlyName animation type` `MPropertySortPriority 500` |
| `0x1098` | `m_bAnimateInFPS` | bool |  | `MPropertyFriendlyName set animation value in FPS` `MPropertySortPriority 500` |
| `0x10a0` | `m_flMotionVectorScaleU` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName motion vector scale U` `MPropertySortPriority 500` |
| `0x1218` | `m_flMotionVectorScaleV` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName motion vector scale V` `MPropertySortPriority 500` |
| `0x1390` | `m_flSelfIllumAmount` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange 0 2` `MPropertyFriendlyName self illum amount` `MPropertySortPriority 400` `MPropertyStartGroup Lighting and Shadows` |
| `0x1508` | `m_flDiffuseAmount` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName diffuse lighting amount` `MPropertySortPriority 400` |
| `0x1680` | `m_flDiffuseClamp` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName diffuse max contribution clamp` `MPropertySortPriority 400` `MPropertySuppressExpr mod != hlx` |
| `0x17f8` | `m_nLightingControlPoint` | int32 |  | `MPropertyFriendlyName diffuse lighting origin Control Point` `MPropertySortPriority 400` |
| `0x17fc` | `m_nOutputBlendMode` | [ParticleOutputBlendMode_t](../particles/ParticleOutputBlendMode_t.md) |  | `MPropertyFriendlyName output blend mode` `MPropertySortPriority 300` `MPropertyStartGroup +Color and alpha adjustments` |
| `0x1800` | `m_bGammaCorrectVertexColors` | bool |  | `MPropertyFriendlyName Gamma-correct vertex colors` `MPropertySortPriority 300` |
| `0x1801` | `m_bSaturateColorPreAlphaBlend` | bool |  | `MPropertyFriendlyName Saturate color pre alphablend` `MPropertySortPriority 300` `MPropertySuppressExpr mod != dota && mod != hlx` |
| `0x1808` | `m_flAddSelfAmount` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName add self amount over alphablend` `MPropertySortPriority 300` |
| `0x1980` | `m_flDesaturation` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName desaturation amount` `MPropertySortPriority 300` |
| `0x1af8` | `m_flOverbrightFactor` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName overbright factor` `MPropertySortPriority 300` |
| `0x1c70` | `m_nHSVShiftControlPoint` | int32 |  | `MPropertyFriendlyName HSV Shift Control Point` `MPropertySortPriority 300` |
| `0x1c74` | `m_nFogType` | [ParticleFogType_t](../particles/ParticleFogType_t.md) |  | `MPropertyFriendlyName Apply fog to particle` `MPropertySortPriority 300` |
| `0x1c78` | `m_flFogAmount` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName Fog Scale` `MPropertySortPriority 300` `MPropertySuppressExpr mod != hlx` |
| `0x1df0` | `m_bTintByFOW` | bool |  | `MPropertyFriendlyName Apply fog of war to color` `MPropertySortPriority 300` `MPropertySuppressExpr mod != dota` |
| `0x1df1` | `m_bTintByGlobalLight` | bool |  | `MPropertyFriendlyName Apply global light to color` `MPropertySortPriority 300` `MPropertySuppressExpr mod != dota` |
| `0x1df4` | `m_nPerParticleAlphaReference` | [SpriteCardPerParticleScale_t](../particles/SpriteCardPerParticleScale_t.md) |  | `MPropertyFriendlyName alpha reference` `MPropertySortPriority 300` `MPropertyStartGroup Color and alpha adjustments/Alpha Reference` |
| `0x1df8` | `m_nPerParticleAlphaRefWindow` | [SpriteCardPerParticleScale_t](../particles/SpriteCardPerParticleScale_t.md) |  | `MPropertyFriendlyName alpha reference window size` `MPropertySortPriority 300` |
| `0x1dfc` | `m_nAlphaReferenceType` | [ParticleAlphaReferenceType_t](../particles/ParticleAlphaReferenceType_t.md) |  | `MPropertyFriendlyName alpha reference type` `MPropertySortPriority 300` |
| `0x1e00` | `m_flAlphaReferenceSoftness` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName alpha reference softness` `MPropertySortPriority 300` |
| `0x1f78` | `m_flSourceAlphaValueToMapToZero` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName source alpha value to map to alpha of zero` `MPropertySortPriority 300` |
| `0x20f0` | `m_flSourceAlphaValueToMapToOne` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange 0 1` `MPropertyFriendlyName source alpha value to map to alpha of 1` `MPropertySortPriority 300` |
| `0x2268` | `m_bRefract` | bool |  | `MPropertyFriendlyName refract background` `MPropertySortPriority 200` `MPropertyStartGroup Refraction` |
| `0x2269` | `m_bRefractSolid` | bool |  | `MPropertyFriendlyName refract draws opaque - alpha scales refraction` `MPropertySortPriority 200` `MPropertySuppressExpr !m_bRefract` |
| `0x226a` | `m_bRefract2Passes` | bool |  | `MPropertyFriendlyName refract in 2 passes - can refract particles behind, requires (MBOIT!)` `MPropertySortPriority 200` `MPropertySuppressExpr mod != hlx &#124;&#124; !m_bRefract` |
| `0x2270` | `m_flRefractAmount` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyAttributeRange -2 2` `MPropertyFriendlyName refract amount` `MPropertySortPriority 200` `MPropertySuppressExpr !m_bRefract` |
| `0x23e8` | `m_nRefractBlurRadius` | int32 |  | `MPropertyFriendlyName refract blur radius` `MPropertySortPriority 200` `MPropertySuppressExpr !m_bRefract` |
| `0x23ec` | `m_nRefractBlurType` | [BlurFilterType_t](../particles/BlurFilterType_t.md) |  | `MPropertyFriendlyName refract blur type` `MPropertySortPriority 200` `MPropertySuppressExpr !m_bRefract` |
| `0x23f0` | `m_bOnlyRenderInEffectsBloomPass` | bool |  | `MPropertyFriendlyName Only Render in effects bloom pass` `MPropertySortPriority 1100` `MPropertyStartGroup` |
| `0x23f1` | `m_bOnlyRenderInEffectsWaterPass` | bool |  | `MPropertyFriendlyName Only Render in effects water pass` `MPropertySortPriority 1050` `MPropertySuppressExpr mod != csgo && mod != hlx` |
| `0x23f2` | `m_bUseMixedResolutionRendering` | bool |  | `MPropertyFriendlyName Use Mixed Resolution Rendering` `MPropertySortPriority 1200` |
| `0x23f3` | `m_bOnlyRenderInEffecsGameOverlay` | bool |  | `MPropertyFriendlyName Only Render in effects game overlay pass` `MPropertySortPriority 1210` `MPropertySuppressExpr mod != csgo` |
| `0x23f4` | `m_stencilTestID` | char[128] |  | `MPropertyFriendlyName stencil test ID` `MPropertySortPriority 0` `MPropertyStartGroup Stencil` |
| `0x2474` | `m_bStencilTestExclude` | bool |  | `MPropertyFriendlyName only write where stencil is NOT stencil test ID` `MPropertySortPriority 0` |
| `0x2475` | `m_stencilWriteID` | char[128] |  | `MPropertyFriendlyName stencil write ID` `MPropertySortPriority 0` |
| `0x24f5` | `m_bWriteStencilOnDepthPass` | bool |  | `MPropertyFriendlyName write stencil on z-buffer test success` `MPropertySortPriority 0` |
| `0x24f6` | `m_bWriteStencilOnDepthFail` | bool |  | `MPropertyFriendlyName write stencil on z-buffer test failure` `MPropertySortPriority 0` |
| `0x24f7` | `m_bReverseZBuffering` | bool |  | `MPropertyFriendlyName reverse z-buffer test` `MPropertySortPriority 900` `MPropertyStartGroup Depth buffer control and effects` |
| `0x24f8` | `m_bDisableZBuffering` | bool |  | `MPropertyFriendlyName disable z-buffer test` `MPropertySortPriority 900` |
| `0x24fc` | `m_nFeatheringMode` | [ParticleDepthFeatheringMode_t](../particles/ParticleDepthFeatheringMode_t.md) |  | `MPropertyFriendlyName Depth feathering mode` `MPropertySortPriority 900` |
| `0x2500` | `m_flFeatheringMinDist` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName particle feathering closest distance to surface` `MPropertySortPriority 900` |
| `0x2678` | `m_flFeatheringMaxDist` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName particle feathering farthest distance to surface` `MPropertySortPriority 900` |
| `0x27f0` | `m_flFeatheringFilter` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName particle feathering alpha filter` `MPropertySortPriority 900` |
| `0x2968` | `m_flFeatheringDepthMapFilter` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName particle feathering depthmap layer filter` `MPropertySortPriority 900` `MPropertySuppressExpr mod != hlx` |
| `0x2ae0` | `m_flDepthBias` | [CParticleCollectionRendererFloatInput](../particleslib/CParticleCollectionRendererFloatInput.md) |  | `MPropertyFriendlyName depth comparison bias` `MPropertySortPriority 900` |
| `0x2c58` | `m_nSortMethod` | [ParticleSortingChoiceList_t](../particles/ParticleSortingChoiceList_t.md) |  | `MPropertyFriendlyName Sort Method` `MPropertySortPriority 900` |
| `0x2c5c` | `m_bBlendFramesSeq0` | bool |  | `MPropertyFriendlyName blend sequence animation frames` `MPropertySortPriority 500` `MPropertyStartGroup Animation` |
| `0x2c5d` | `m_bMaxLuminanceBlendingSequence0` | bool |  | `MPropertyFriendlyName use max-luminance blending for sequence` `MPropertySortPriority 500` `MPropertySuppressExpr !m_bBlendFramesSeq0` |
