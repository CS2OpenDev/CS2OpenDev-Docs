---
layout: default
title: SelectorInstanceData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / SelectorInstanceData_t

# SelectorInstanceData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 44 bytes (`0x2c`) · **Align:** n/a (unspecified) · **Module:** animgraphlib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_weights` | CRelativeArray< float32 > |  |  |
| `0x8` | `m_currentIndexStartTime` | CAnimNetVar< float32 > |  |  |
| `0x14` | `m_currentIndex` | int32 |  |  |
| `0x18` | `m_previousIndex` | int32 |  |  |
