---
layout: default
title: CSeqPoseSetting
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CSeqPoseSetting

# CSeqPoseSetting

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sPoseParameter` | CBufferString |  |  |
| `0x10` | `m_sAttachment` | CBufferString |  |  |
| `0x20` | `m_sReferenceSequence` | CBufferString |  |  |
| `0x30` | `m_flValue` | float32 |  |  |
| `0x34` | `m_bX` | bool |  |  |
| `0x35` | `m_bY` | bool |  |  |
| `0x36` | `m_bZ` | bool |  |  |
| `0x38` | `m_eType` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sPoseParameter&quot;: &quot;&quot;,
	&quot;m_sAttachment&quot;: &quot;&quot;,
	&quot;m_sReferenceSequence&quot;: &quot;&quot;,
	&quot;m_flValue&quot;: 0.000000,
	&quot;m_bX&quot;: false,
	&quot;m_bY&quot;: false,
	&quot;m_bZ&quot;: false,
	&quot;m_eType&quot;: 0
}</pre>
</details>
