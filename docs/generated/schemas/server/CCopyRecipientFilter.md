---
layout: default
title: CCopyRecipientFilter
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCopyRecipientFilter

# CCopyRecipientFilter

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** server

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_Flags` | int32 |  |  |
| `0x10` | `m_Recipients` | CUtlVector< CPlayerSlot > |  |  |
| `0x30` | `m_slotPlayerExcludedDueToPrediction` | CPlayerSlot |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CCopyRecipientFilter&quot;,
	&quot;m_Flags&quot;: 0,
	&quot;m_Recipients&quot;:
	[
	],
	&quot;m_slotPlayerExcludedDueToPrediction&quot;: -1
}</pre>
</details>
