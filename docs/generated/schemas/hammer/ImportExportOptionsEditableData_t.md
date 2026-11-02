---
title: ImportExportOptionsEditableData_t
module: hammer
kind: class
---

[Schemas](../../schemas.md) / [hammer](../hammer.md) / ImportExportOptionsEditableData_t

# ImportExportOptionsEditableData_t

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 20 bytes (`0x14`) · **Align:** n/a (unspecified) · **Module:** hammer

**Relationships:**

```mermaid
classDiagram
    ImportExportOptionsEditableData_t *-- `ImportExportOptionsEditableData_t::ExportFbxUnit_t`
    ImportExportOptionsEditableData_t *-- `ImportExportOptionsEditableData_t::ExportDefaultFormat_t`
    ImportExportOptionsEditableData_t *-- `ImportExportOptionsEditableData_t::ExportEncoding_t`
```

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `bExportProps` | bool |  | `MPropertyFriendlyName Export Props` |
| `0x1` | `bExportHidden` | bool |  | `MPropertyFriendlyName Export Hidden Objects` |
| `0x2` | `bExportBones` | bool |  | `MPropertyDescription Export the bones of models. Only supported by FBX export` `MPropertyFriendlyName Export Bones (FBX only)` |
| `0x3` | `bExportSkinning` | bool |  | `MPropertyDescription Export the skinning of models. Only supported by FBX export, Requires exporting bones. NOTE: exporting skinning can generate an FBX with skinned and un-skinned objects, which can cause problems if referenced by a vmdl.` `MPropertyFriendlyName Export Skinning (FBX only)` |
| `0x4` | `bExportFbxEmbedTextures` | bool |  | `MPropertyFriendlyName Export FBX Embed Textures From Content If Available` `MPropertySuppressField` |
| `0x8` | `nExportFbxUnit` | [ImportExportOptionsEditableData_t::ExportFbxUnit_t](../hammer/ImportExportOptionsEditableData_t.ExportFbxUnit_t.md) |  | `MPropertyFriendlyName Export Hammer Units To FBX Units` |
| `0xc` | `nExportDefaultFormat` | [ImportExportOptionsEditableData_t::ExportDefaultFormat_t](../hammer/ImportExportOptionsEditableData_t.ExportDefaultFormat_t.md) |  | `MPropertyFriendlyName Export Default Format` |
| `0x10` | `nExportEncoding` | [ImportExportOptionsEditableData_t::ExportEncoding_t](../hammer/ImportExportOptionsEditableData_t.ExportEncoding_t.md) |  | `MPropertyFriendlyName Export Encoding` |
