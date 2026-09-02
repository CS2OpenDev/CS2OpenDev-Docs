---
title: CSmartPropFilter_Expression
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropFilter_Expression

# CSmartPropFilter_Expression

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** smartprops

**Inherits from:** [CSmartPropFilter](../smartprops/CSmartPropFilter.md)

**Metadata:** `MPropertyDescription Evaluates the specified expression, if the result of the expression is false evaluation of the element is stopped.`, `MPropertyFriendlyName Filter: Expression`, `MVDataClassGroup Filter`

**Relationships:**

```mermaid
classDiagram
    CSmartPropFilter <|-- CSmartPropFilter_Expression
    CSmartPropModifier <|-- CSmartPropFilter
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bEnabled` | CSmartPropAttributeBool | [CSmartPropModifier](../smartprops/CSmartPropModifier.md) | `MVDataEnableKey` |
| `0x50` | `m_Expression` | CUtlString |  | `MPropertyAttributeEditor SmartPropAttributeEditor(expression)` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CSmartPropFilter_Expression&quot;,
	&quot;m_bEnabled&quot;: true,
	&quot;m_Expression&quot;: &quot;&quot;
}</pre>
</details>
