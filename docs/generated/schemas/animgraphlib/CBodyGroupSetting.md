---
layout: default
title: CBodyGroupSetting
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CBodyGroupSetting

# CBodyGroupSetting

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animgraphlib

**Metadata:** `MPropertyElementNameFn`, `MPropertyFriendlyName Body Group Setting`

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_BodyGroupName` | CUtlString |  | `MPropertyAttributeChoiceName BodyGroup` `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName BodyGroup` |
| `0x8` | `m_nBodyGroupOption` | int32 |  | `MPropertyAttributeChoiceName BodyGroupOption` `MPropertyFriendlyName BodyGroup Option` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_BodyGroupName&quot;: &quot;&quot;,
	&quot;m_nBodyGroupOption&quot;: 0
}</pre>
</details>
