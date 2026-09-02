---
title: VMixConvolutionDesc_t
module: soundsystem_lowlevel
kind: class
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixConvolutionDesc_t

# VMixConvolutionDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 4 · **Module:** soundsystem_lowlevel

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_fldbGain` | float32 |  | `MPropertyAttributeRange -36 3` `MPropertyFriendlyName gain of wet signal (dB)` |
| `0x4` | `m_flPreDelayMS` | float32 |  | `MPropertyFriendlyName Pre-delay (ms)` |
| `0x8` | `m_flWetMix` | float32 |  | `MPropertyFriendlyName Dry/Wet` |
| `0xc` | `m_fldbLow` | float32 |  | `MPropertyAttributeRange -24 24` `MPropertyFriendlyName Low EQ gain (dB)` |
| `0x10` | `m_fldbMid` | float32 |  | `MPropertyAttributeRange -24 24` `MPropertyFriendlyName Mid EQ gain (dB)` |
| `0x14` | `m_fldbHigh` | float32 |  | `MPropertyAttributeRange -24 24` `MPropertyFriendlyName High EQ gain (dB)` |
| `0x18` | `m_flLowCutoffFreq` | float32 |  | `MPropertyFriendlyName Low Cutoff Freq (Hz)` |
| `0x1c` | `m_flHighCutoffFreq` | float32 |  | `MPropertyFriendlyName High Cutoff Freq (Hz)` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_fldbGain&quot;: -12.000000,
	&quot;m_flPreDelayMS&quot;: 0.000000,
	&quot;m_flWetMix&quot;: 1.000000,
	&quot;m_fldbLow&quot;: 0.000000,
	&quot;m_fldbMid&quot;: 0.000000,
	&quot;m_fldbHigh&quot;: 0.000000,
	&quot;m_flLowCutoffFreq&quot;: 1500.000000,
	&quot;m_flHighCutoffFreq&quot;: 7500.000000
}</pre>
</details>
