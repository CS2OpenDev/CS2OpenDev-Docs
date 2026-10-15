---
title: NmContactAudioInfo_t
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / NmContactAudioInfo_t

# NmContactAudioInfo_t

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animlib

**Metadata:** `MPropertyAutoExpandSelf`

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_audioActionID` | CGlobalSymbol |  | `MPropertyAttributeEditor VDataChoice( scripts/nm_contact_audio_actions.vdata )` `MPropertyFriendlyName Audio Action` |
| `0x8` | `m_audioTypeID` | CGlobalSymbol |  | `MPropertyAttributeEditor VDataChoice( scripts/nm_contact_audio_types.vdata )` `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Audio Type` |
| `0x10` | `m_soundeventOverrideID` | CGlobalSymbol |  | `MPropertyAttrStateCallback` `MPropertyFriendlyName Audio Soundevent Override` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_audioActionID&quot;: &quot;&quot;,
	&quot;m_audioTypeID&quot;: &quot;&quot;,
	&quot;m_soundeventOverrideID&quot;: &quot;&quot;
}</pre>
</details>
