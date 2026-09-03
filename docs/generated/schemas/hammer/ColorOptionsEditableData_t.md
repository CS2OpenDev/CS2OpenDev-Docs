---
title: ColorOptionsEditableData_t
module: hammer
kind: class
---

[Schemas](../../schemas.md) / [hammer](../hammer.md) / ColorOptionsEditableData_t

# ColorOptionsEditableData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 30 bytes (`0x1e`) · **Align:** n/a (unspecified) · **Module:** hammer

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `bUseCustom` | bool |  | `MPropertyFriendlyName Use Custom Colors` |
| `0x1` | `bWhiteOnBlack` | bool |  | `MPropertyFriendlyName White on black` |
| `0x2` | `clrGrid` | Color |  | `MPropertyFriendlyName Grid Color` |
| `0x6` | `clrGridFractional` | Color |  | `MPropertyFriendlyName Grid Color for sub 1-unit lines` |
| `0xa` | `clrGrid10` | Color |  | `MPropertyFriendlyName Grid Color for every 10th line` |
| `0xe` | `clrGrid1024` | Color |  | `MPropertyFriendlyName Grid Color for every 1024 units line` |
| `0x12` | `clrBrush` | Color |  | `MPropertyFriendlyName Brush Color` |
| `0x16` | `clrSelection` | Color |  | `MPropertyFriendlyName Color of the selected brushes` |
| `0x1a` | `clrToolSelection` | Color |  | `MPropertyFriendlyName Color of the selection tool` |
