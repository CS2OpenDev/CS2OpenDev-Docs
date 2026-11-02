---
title: NoiseOscillatorDef_t
module: mathlib_extended
kind: class
---

[Schemas](../../schemas.md) / [mathlib_extended](../mathlib_extended.md) / NoiseOscillatorDef_t

# NoiseOscillatorDef_t

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 12 bytes (`0xc`) · **Align:** 4 · **Module:** mathlib_extended

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flPhase` | float32 |  | `MPropertyAttributeRange 0 1` |
| `0x4` | `m_flFrequency` | float32 |  | `MPropertyAttributeRange biased 0.001 100` |
| `0x8` | `m_flAmplitude` | float32 |  | `MPropertyAttributeRange -10 10` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flPhase&quot;: 0.000000,
	&quot;m_flFrequency&quot;: 1.000000,
	&quot;m_flAmplitude&quot;: 1.000000
}</pre>
</details>
