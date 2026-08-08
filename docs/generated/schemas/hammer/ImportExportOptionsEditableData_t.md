---
layout: default
title: ImportExportOptionsEditableData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [hammer](../hammer.md) / ImportExportOptionsEditableData_t

# ImportExportOptionsEditableData_t

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** hammer

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `bExportProps` | bool |  | `MPropertyFriendlyName Export Props` |
| `0x1` | `bExportHidden` | bool |  | `MPropertyFriendlyName Export Hidden Objects` |
| `0x2` | `bExportFbxEmbedTextures` | bool |  | `MPropertyFriendlyName Export FBX Embed Textures From Content If Available` `MPropertySuppressField` |
| `0x4` | `nExportFbxUnit` | [ImportExportOptionsEditableData_t](../hammer/ImportExportOptionsEditableData_t.md)::ExportFbxUnit_t |  | `MPropertyFriendlyName Export Hammer Units To FBX Units` |
| `0x8` | `nExportDefaultFormat` | [ImportExportOptionsEditableData_t](../hammer/ImportExportOptionsEditableData_t.md)::ExportDefaultFormat_t |  | `MPropertyFriendlyName Export Default Format` |
| `0xc` | `nExportEncoding` | [ImportExportOptionsEditableData_t](../hammer/ImportExportOptionsEditableData_t.md)::ExportEncoding_t |  | `MPropertyFriendlyName Export Encoding` |
