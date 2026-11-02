---
title: CVMixToolEffectsList
module: sounddoc_lib
kind: class
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CVMixToolEffectsList

# CVMixToolEffectsList

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** sounddoc_lib

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bIsAutomaticDSP` | bool |  | `MKV3TransferName IsAutomaticDSP` |
| `0x8` | `m_list` | CUtlVector< CVMixEffectPreset > |  | `MKV3TransferName presets` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;IsAutomaticDSP&quot;: false,
	&quot;presets&quot;:
	[
	]
}</pre>
</details>
