---
title: CSeqSynthAnimDesc
module: animationsystem
kind: class
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CSeqSynthAnimDesc

# CSeqSynthAnimDesc

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** animationsystem

**Relationships:**

```mermaid
classDiagram
    CSeqSynthAnimDesc *-- CSeqSeqDescFlag
    CSeqSynthAnimDesc *-- CSeqTransition
    CSeqSynthAnimDesc *-- CAnimActivity
```

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sName` | CBufferString |  |  |
| `0x10` | `m_flags` | [CSeqSeqDescFlag](../animationsystem/CSeqSeqDescFlag.md) |  |  |
| `0x1c` | `m_transition` | [CSeqTransition](../animationsystem/CSeqTransition.md) |  |  |
| `0x24` | `m_nLocalBaseReference` | int16 |  |  |
| `0x26` | `m_nLocalBoneMask` | int16 |  |  |
| `0x28` | `m_activityArray` | CUtlVector< [CAnimActivity](../animationsystem/CAnimActivity.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sName&quot;: &quot;&quot;,
	&quot;m_flags&quot;:
	{
		&quot;m_bLooping&quot;: false,
		&quot;m_bSnap&quot;: false,
		&quot;m_bAutoplay&quot;: false,
		&quot;m_bPost&quot;: false,
		&quot;m_bHidden&quot;: false,
		&quot;m_bMulti&quot;: false,
		&quot;m_bLegacyDelta&quot;: false,
		&quot;m_bLegacyWorldspace&quot;: false,
		&quot;m_bLegacyCyclepose&quot;: false,
		&quot;m_bLegacyRealtime&quot;: false,
		&quot;m_bModelDoc&quot;: false
	},
	&quot;m_transition&quot;:
	{
		&quot;m_flFadeInTime&quot;: 0.000000,
		&quot;m_flFadeOutTime&quot;: 0.000000
	},
	&quot;m_nLocalBaseReference&quot;: 0,
	&quot;m_nLocalBoneMask&quot;: 0,
	&quot;m_activityArray&quot;:
	[
	]
}</pre>
</details>
