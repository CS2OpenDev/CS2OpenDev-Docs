---
title: CSmartPropChoiceOption
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropChoiceOption

# CSmartPropChoiceOption

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 8 · **Module:** smartprops

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Name` | CUtlString |  | `MPropertyFriendlyName Option Value Name` |
| `0x8` | `m_DisplayName` | CUtlString |  | `MPropertyFriendlyName Option Display Name` |
| `0x10` | `m_VariableValues` | CUtlVector< CSmartPropAttributeVariableValue > |  | `MPropertyAttributeEditor SmartPropAttributeEditor(VariableValue)` `MPropertyAutoExpandSelf` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_DisplayName&quot;: &quot;&quot;,
	&quot;m_VariableValues&quot;:
	[
	]
}</pre>
</details>
