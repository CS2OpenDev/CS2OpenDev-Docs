---
layout: default
title: ViewAngleServerChange_t (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / ViewAngleServerChange_t

# ViewAngleServerChange_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [ViewAngleServerChange_t (server)](../server/ViewAngleServerChange_t.md)

**Relationships:**

```mermaid
classDiagram
    ViewAngleServerChange_t *-- FixAngleSet_t
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x30` | `nType` | [FixAngleSet_t](../server/FixAngleSet_t.md) |  |  |
| `0x34` | `qAngle` | QAngle |  |  |
| `0x40` | `nIndex` | uint32 |  |  |
