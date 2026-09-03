---
title: "CSmartPropPulse_SelectionLinearLength::Criteria_t"
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropPulse_SelectionLinearLength::Criteria_t

# CSmartPropPulse_SelectionLinearLength::Criteria_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** n/a (unspecified) · **Module:** smartprops

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flLength` | float32 |  | `MPropertyDescription Specifies the length of the line that will be taken up if this element is selected.` |
| `0x4` | `m_bAllowScale` | bool |  | `MPropertyDescription Can this object be scaled. If enabled the minimum and maximum lengths must be set to specify the size range of allowable scale.` |
| `0x8` | `m_flMinLength` | float32 |  | `MPropertyDescription Minimum allowable length for the object. Must be <= length. If length is 100 and minimum length is 20, then the object may be assigned a scale in the rage [ 0.2, 1.0 ].` `MPropertyFriendlyName Minimum length` `MPropertySuppressExpr m_bAllowScale == false` |
| `0xc` | `m_flMaxLength` | float32 |  | `MPropertyDescription Maximum allowable length for the object. Must be >= length. If length is 100 and maximum length is 160, then the object may be assigned a scale in the rage [ 1.0, 1.6 ].` `MPropertyFriendlyName Maximum length` `MPropertySuppressExpr m_bAllowScale == false` |
