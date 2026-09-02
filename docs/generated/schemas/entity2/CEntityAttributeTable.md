---
layout: default
title: CEntityAttributeTable
nav_exclude: true
---

[Schemas](../../schemas.md) / [entity2](../entity2.md) / CEntityAttributeTable

# CEntityAttributeTable

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** n/a (unspecified) · **Module:** entity2

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Attributes` | CUtlOrderedMap< CUtlStringTokenNoRegistration, Attribute_t > |  |  |
| `0x28` | `m_Names` | CUtlOrderedMap< CUtlStringTokenNoRegistration, CUtlString > |  |  |
