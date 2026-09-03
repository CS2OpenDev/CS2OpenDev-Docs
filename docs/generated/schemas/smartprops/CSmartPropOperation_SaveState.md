---
title: CSmartPropOperation_SaveState
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropOperation_SaveState

# CSmartPropOperation_SaveState

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** smartprops

**Inherits from:** [CSmartPropOperation](../smartprops/CSmartPropOperation.md)

**Metadata:** `MPropertyDescription Save the current state, allowing it to be restored at a later state.`, `MPropertyFriendlyName Save State`, `MVDataClassGroup State`, `MVDataNodeTintColor`

**Relationships:**

```mermaid
classDiagram
    CSmartPropOperation <|-- CSmartPropOperation_SaveState
    CSmartPropModifier <|-- CSmartPropOperation
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bEnabled` | CSmartPropAttributeBool | [CSmartPropModifier](../smartprops/CSmartPropModifier.md) | `MVDataEnableKey` |
| `0x50` | `m_StateName` | CUtlString |  | `MPropertyAttributeEditor SmartPropItemNameEditor( SavedState )` `MPropertyDescription Name to assign to the saved state, the save state can be restored later using this name.` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CSmartPropOperation_SaveState&quot;,
	&quot;m_bEnabled&quot;: true,
	&quot;m_StateName&quot;: &quot;&quot;
}</pre>
</details>
