---
layout: default
title: "CNmGraphDocDataDictionary::IDSet_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmGraphDocDataDictionary::IDSet_t

# CNmGraphDocDataDictionary::IDSet_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animdoclib

**Metadata:** `MPropertyAutoExpandSelf`

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_ID` | V_uuid_t |  | `MPropertySuppressField` |
| `0x10` | `m_name` | CUtlString |  | `MPropertyFlattenIntoParentRow` |
| `0x18` | `m_graphIDs` | CUtlVector< CGlobalSymbol > |  | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Graph IDs` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_graphIDs&quot;:
	[
	]
}</pre>
</details>
