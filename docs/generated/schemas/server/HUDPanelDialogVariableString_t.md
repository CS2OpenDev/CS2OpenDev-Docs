---
layout: default
title: HUDPanelDialogVariableString_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / HUDPanelDialogVariableString_t

# HUDPanelDialogVariableString_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** n/a (unspecified) · **Module:** server

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nPanelIdIndex` | uint16 |  |  |
| `0xa` | `m_nDialogVariableIndex` | uint16 |  |  |
| `0x10` | `m_sValue` | CUtlString |  |  |
| `0x18` | `m_bIsSet` | bool |  |  |
