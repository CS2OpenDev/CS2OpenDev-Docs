---
layout: default
title: CDSPMixgroupModifier
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem](../soundsystem.md) / CDSPMixgroupModifier

# CDSPMixgroupModifier

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** soundsystem

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_mixgroup` | CUtlString |  | `MPropertyDescription Name of the mixgroup. TODO: needs to be autopopulated with mixgroups.` `MPropertyFriendlyName Mixgroup Name` |
| `0x8` | `m_flModifier` | float32 |  | `MPropertyDescription The amount to multiply the volume of the non-spatialized reverb/dsp by when at the max reverb blend distance. 1.0 leaves the volume unchanged.` `MPropertyFriendlyName Max reverb gain amount for listener DSP.` |
| `0xc` | `m_flModifierMin` | float32 |  | `MPropertyDescription The amount to multiply the volume of the non-spatialized reverb/dsp by when at the min reverb blend distance. 1.0 leaves the volume unchanged.` `MPropertyFriendlyName Min reverb gain amount amount for listener DSP.` |
| `0x10` | `m_flSourceModifier` | float32 |  | `MPropertyDescription If set to >= 0, we will use this mix modifier for source-specific DSP effects. Otherwise we will use the listener DSP value.` `MPropertyFriendlyName Max reverb gain amount for source-specific DSP.` |
| `0x14` | `m_flSourceModifierMin` | float32 |  | `MPropertyDescription If set to >= 0, we will use this mix modifier for source-specific DSP effects. Otherwise we will use the listener DSP value.` `MPropertyFriendlyName Min reverb gain amount for source-specific DSP.` |
| `0x18` | `m_flListenerReverbModifierWhenSourceReverbIsActive` | float32 |  | `MPropertyDescription When a source has source-specific DSP, this can be used as an additional mix stage for the listener reverb amount.` `MPropertyFriendlyName Modification amount for listener DSP when source DSP is used.` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_mixgroup&quot;: &quot;default&quot;,
	&quot;m_flModifier&quot;: 1.000000,
	&quot;m_flModifierMin&quot;: 0.000000,
	&quot;m_flSourceModifier&quot;: -1.000000,
	&quot;m_flSourceModifierMin&quot;: -1.000000,
	&quot;m_flListenerReverbModifierWhenSourceReverbIsActive&quot;: 1.000000
}</pre>
</details>
