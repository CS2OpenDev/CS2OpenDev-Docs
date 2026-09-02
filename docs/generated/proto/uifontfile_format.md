---
layout: default
title: uifontfile_format.proto
parent: Protobufs
nav_exclude: true
---

# `uifontfile_format.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CUIFontFilePB {
    +string font_file_name
    +bytes opentype_font_data
  }

  class CUIFontFilePackagePB {
    +uint32 package_version
    +List~CUIFontFilePackagePB.CUIEncryptedFontFilePB~ encrypted_font_files
  }

  class CUIFontFilePackagePB_CUIEncryptedFontFilePB["CUIFontFilePackagePB.CUIEncryptedFontFilePB"] {
    +bytes encrypted_contents
  }

  CUIFontFilePackagePB --> CUIFontFilePackagePB_CUIEncryptedFontFilePB : encrypted_font_files[]

```

## Messages

### `CUIFontFilePB`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `font_file_name` | 1 | string | optional |  |
| `opentype_font_data` | 2 | bytes | optional |  |

### `CUIFontFilePackagePB`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `package_version` | 1 | uint32 | optional |  |
| `encrypted_font_files` | 2 | [CUIFontFilePackagePB.CUIEncryptedFontFilePB](#cuifontfilepackagepbcuiencryptedfontfilepb) | repeated |  |

#### `CUIFontFilePackagePB.CUIEncryptedFontFilePB`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `encrypted_contents` | 1 | bytes | optional |  |
