---
layout: default
title: CMixPropertyBase
nav_exclude: true
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CMixPropertyBase

# CMixPropertyBase

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** sounddoc_lib

**Derived by:** [CMixAmp](../sounddoc_lib/CMixAmp.md), [CMixAudioMeter](../sounddoc_lib/CMixAudioMeter.md), [CMixAudioSource](../sounddoc_lib/CMixAudioSource.md), [CMixAutoFilter](../sounddoc_lib/CMixAutoFilter.md), [CMixBlendAudio](../sounddoc_lib/CMixBlendAudio.md), [CMixBlendVsndsToImpulseResponse](../sounddoc_lib/CMixBlendVsndsToImpulseResponse.md), [CMixBoxverb](../sounddoc_lib/CMixBoxverb.md), [CMixBoxverb2](../sounddoc_lib/CMixBoxverb2.md), [CMixControlAutomatic](../sounddoc_lib/CMixControlAutomatic.md), [CMixControlCrossfade](../sounddoc_lib/CMixControlCrossfade.md), [CMixControlCurve](../sounddoc_lib/CMixControlCurve.md), [CMixControlInput](../sounddoc_lib/CMixControlInput.md), [CMixControlInputArray](../sounddoc_lib/CMixControlInputArray.md), [CMixControlListener](../sounddoc_lib/CMixControlListener.md), [CMixControlMax](../sounddoc_lib/CMixControlMax.md), [CMixControlMeter](../sounddoc_lib/CMixControlMeter.md), [CMixControlOutput](../sounddoc_lib/CMixControlOutput.md), [CMixControlRemap](../sounddoc_lib/CMixControlRemap.md), [CMixControlStackInput](../sounddoc_lib/CMixControlStackInput.md), [CMixControlTransientInput](../sounddoc_lib/CMixControlTransientInput.md), [CMixConvolution](../sounddoc_lib/CMixConvolution.md), [CMixDelay](../sounddoc_lib/CMixDelay.md), [CMixDelayImpulseResponse](../sounddoc_lib/CMixDelayImpulseResponse.md), [CMixDiffusor](../sounddoc_lib/CMixDiffusor.md), [CMixDualCompressor](../sounddoc_lib/CMixDualCompressor.md), [CMixDynamics](../sounddoc_lib/CMixDynamics.md), [CMixDynamics3Band](../sounddoc_lib/CMixDynamics3Band.md), [CMixDynamicsCompressor](../sounddoc_lib/CMixDynamicsCompressor.md), [CMixEQ8](../sounddoc_lib/CMixEQ8.md), [CMixEffectChain](../sounddoc_lib/CMixEffectChain.md), [CMixEffectName](../sounddoc_lib/CMixEffectName.md), [CMixEnvelope](../sounddoc_lib/CMixEnvelope.md), [CMixEnvelopeTrigger](../sounddoc_lib/CMixEnvelopeTrigger.md), [CMixFilter](../sounddoc_lib/CMixFilter.md), [CMixFlanger](../sounddoc_lib/CMixFlanger.md), [CMixFreeverb](../sounddoc_lib/CMixFreeverb.md), [CMixGroupBox](../sounddoc_lib/CMixGroupBox.md), [CMixImpulseResponseInput](../sounddoc_lib/CMixImpulseResponseInput.md), [CMixModDelay](../sounddoc_lib/CMixModDelay.md), [CMixOsc](../sounddoc_lib/CMixOsc.md), [CMixOutput](../sounddoc_lib/CMixOutput.md), [CMixPanner](../sounddoc_lib/CMixPanner.md), [CMixPitchShift](../sounddoc_lib/CMixPitchShift.md), [CMixPlateverb](../sounddoc_lib/CMixPlateverb.md), [CMixPresetDSP](../sounddoc_lib/CMixPresetDSP.md), [CMixRemapVsndToImpulseResponse](../sounddoc_lib/CMixRemapVsndToImpulseResponse.md), [CMixShaper](../sounddoc_lib/CMixShaper.md), [CMixSplitter](../sounddoc_lib/CMixSplitter.md), [CMixSplitterBlend](../sounddoc_lib/CMixSplitterBlend.md), [CMixSteamAudioDirect](../sounddoc_lib/CMixSteamAudioDirect.md), [CMixSteamAudioHybridReverb](../sounddoc_lib/CMixSteamAudioHybridReverb.md), [CMixSteamAudioPathing](../sounddoc_lib/CMixSteamAudioPathing.md), [CMixSteamAudioSource](../sounddoc_lib/CMixSteamAudioSource.md), [CMixStereoDelay](../sounddoc_lib/CMixStereoDelay.md), [CMixSubgraph](../sounddoc_lib/CMixSubgraph.md), [CMixSubgraphSwitch](../sounddoc_lib/CMixSubgraphSwitch.md), [CMixSum](../sounddoc_lib/CMixSum.md), [CMixTrack](../sounddoc_lib/CMixTrack.md), [CMixUtility](../sounddoc_lib/CMixUtility.md), [CMixVocoder](../sounddoc_lib/CMixVocoder.md), [CMixVsndName](../sounddoc_lib/CMixVsndName.md)

**Relationships:**

```mermaid
classDiagram
    CMixPropertyBase <|-- CMixAmp
    CMixPropertyBase <|-- CMixAudioMeter
    CMixPropertyBase <|-- CMixAudioSource
    CMixPropertyBase <|-- CMixAutoFilter
    CMixPropertyBase <|-- CMixBlendAudio
    CMixPropertyBase <|-- CMixBlendVsndsToImpulseResponse
    CMixPropertyBase <|-- CMixBoxverb
    CMixPropertyBase <|-- CMixBoxverb2
    CMixPropertyBase <|-- CMixControlAutomatic
    CMixPropertyBase <|-- CMixControlCrossfade
    CMixPropertyBase <|-- CMixControlCurve
    CMixPropertyBase <|-- CMixControlInput
    CMixPropertyBase <|-- CMixControlInputArray
    CMixPropertyBase <|-- CMixControlListener
    CMixPropertyBase <|-- CMixControlMax
    CMixPropertyBase <|-- CMixControlMeter
    CMixPropertyBase <|-- CMixControlOutput
    CMixPropertyBase <|-- CMixControlRemap
    CMixPropertyBase <|-- CMixControlStackInput
    CMixPropertyBase <|-- CMixControlTransientInput
    CMixPropertyBase <|-- CMixConvolution
    CMixPropertyBase <|-- CMixDelay
    CMixPropertyBase <|-- CMixDelayImpulseResponse
    CMixPropertyBase <|-- CMixDiffusor
    CMixPropertyBase <|-- CMixDualCompressor
    CMixPropertyBase <|-- CMixDynamics
    CMixPropertyBase <|-- CMixDynamics3Band
    CMixPropertyBase <|-- CMixDynamicsCompressor
    CMixPropertyBase <|-- CMixEQ8
    CMixPropertyBase <|-- CMixEffectChain
    CMixPropertyBase <|-- CMixEffectName
    CMixPropertyBase <|-- CMixEnvelope
    CMixPropertyBase <|-- CMixEnvelopeTrigger
    CMixPropertyBase <|-- CMixFilter
    CMixPropertyBase <|-- CMixFlanger
    CMixPropertyBase <|-- CMixFreeverb
    CMixPropertyBase <|-- CMixGroupBox
    CMixPropertyBase <|-- CMixImpulseResponseInput
    CMixPropertyBase <|-- CMixModDelay
    CMixPropertyBase <|-- CMixOsc
    CMixPropertyBase <|-- CMixOutput
    CMixPropertyBase <|-- CMixPanner
    CMixPropertyBase <|-- CMixPitchShift
    CMixPropertyBase <|-- CMixPlateverb
    CMixPropertyBase <|-- CMixPresetDSP
    CMixPropertyBase <|-- CMixRemapVsndToImpulseResponse
    CMixPropertyBase <|-- CMixShaper
    CMixPropertyBase <|-- CMixSplitter
    CMixPropertyBase <|-- CMixSplitterBlend
    CMixPropertyBase <|-- CMixSteamAudioDirect
    CMixPropertyBase <|-- CMixSteamAudioHybridReverb
    CMixPropertyBase <|-- CMixSteamAudioPathing
    CMixPropertyBase <|-- CMixSteamAudioSource
    CMixPropertyBase <|-- CMixStereoDelay
    CMixPropertyBase <|-- CMixSubgraph
    CMixPropertyBase <|-- CMixSubgraphSwitch
    CMixPropertyBase <|-- CMixSum
    CMixPropertyBase <|-- CMixTrack
    CMixPropertyBase <|-- CMixUtility
    CMixPropertyBase <|-- CMixVocoder
    CMixPropertyBase <|-- CMixVsndName
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString |  | `MPropertyDescription Node name` `MPropertyFriendlyName Name` `MPropertySortPriority 1` |
| `0x10` | `m_Comment` | CUtlString |  | `MPropertyDescription Description of how this is used  the graph for people reading the graph` `MPropertySortPriority -2` |
| `0x18` | `m_bActive` | bool |  | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x19` | `m_bSolo` | bool |  | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x1a` | `m_bEditProperties` | bool |  | `MPropertyHideField` `MPropertySortPriority -1` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMixPropertyBase&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_Comment&quot;: &quot;&quot;,
	&quot;m_bActive&quot;: true,
	&quot;m_bSolo&quot;: false,
	&quot;m_bEditProperties&quot;: false
}</pre>
</details>
