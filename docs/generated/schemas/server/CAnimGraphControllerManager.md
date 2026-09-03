---
title: CAnimGraphControllerManager
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CAnimGraphControllerManager

# CAnimGraphControllerManager

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 152 bytes (`0x98`) · **Align:** n/a (unspecified) · **Module:** server

**Relationships:**

```mermaid
classDiagram
    CAnimGraphControllerManager --> CAnimGraphControllerBase
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_controllers` | CUtlVector< [CAnimGraphControllerBase](../server/CAnimGraphControllerBase.md)* > |  |  |
| `0x90` | `m_bGraphBindingsCreated` | bool |  |  |
