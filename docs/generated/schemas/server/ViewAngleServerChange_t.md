---
title: ViewAngleServerChange_t (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / ViewAngleServerChange_t

# ViewAngleServerChange_t

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [ViewAngleServerChange_t (client)](../client/ViewAngleServerChange_t.md)

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
