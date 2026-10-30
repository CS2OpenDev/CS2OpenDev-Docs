---
title: ColorOptionsEditableData_t
module: hammer
kind: class
---

[Schemas](../../schemas.md) / [hammer](../hammer.md) / ColorOptionsEditableData_t

# ColorOptionsEditableData_t

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** n/a (unspecified) · **Module:** hammer

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `bUseCustom` | bool |  | `MPropertyFriendlyName Use Custom Colors` |
| `0x1` | `bWhiteOnBlack` | bool |  | `MPropertyFriendlyName White on black` |
| `0x4` | `clrGrid` | Color |  | `MPropertyFriendlyName Grid Color` |
| `0x8` | `clrGridFractional` | Color |  | `MPropertyFriendlyName Grid Color for sub 1-unit lines` |
| `0xc` | `clrGrid10` | Color |  | `MPropertyFriendlyName Grid Color for every 10th line` |
| `0x10` | `clrGrid1024` | Color |  | `MPropertyFriendlyName Grid Color for every 1024 units line` |
| `0x14` | `clrBrush` | Color |  | `MPropertyFriendlyName Brush Color` |
| `0x18` | `clrSelection` | Color |  | `MPropertyFriendlyName Color of the selected brushes` |
| `0x1c` | `clrToolSelection` | Color |  | `MPropertyFriendlyName Color of the selection tool` |
