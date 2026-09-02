---
layout: default
title: EMaterialLayer_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [met](../met.md) / EMaterialLayer_t

# EMaterialLayer_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 8 · **Module:** met

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_VariableNames` | CUtlVector< CUtlString > |  |  |
| `0x18` | `m_HiddenVariableUiNames` | CUtlVector< std::pair< CUtlString, CUtlString > > |  |  |
| `0x30` | `m_ReferenceVariableIndex` | int32 |  |  |
| `0x38` | `m_RefType` | CUtlString |  |  |
| `0x40` | `m_RefFileEnding` | CUtlString |  |  |
| `0x48` | `m_bActive` | bool |  |  |
| `0x50` | `inheritedVariableValues` | KeyValues3 |  |  |
| `0x60` | `inheritedVariableSources` | KeyValues3 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_VariableNames&quot;:
	[
	],
	&quot;m_HiddenVariableUiNames&quot;:
	[
	],
	&quot;m_ReferenceVariableIndex&quot;: -1,
	&quot;m_RefType&quot;: &quot;&quot;,
	&quot;m_RefFileEnding&quot;: &quot;&quot;,
	&quot;m_bActive&quot;: true,
	&quot;inheritedVariableValues&quot;: null,
	&quot;inheritedVariableSources&quot;: null
}</pre>
</details>
