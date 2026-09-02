---
layout: default
title: CSkeletonAnimationController
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CSkeletonAnimationController

# CSkeletonAnimationController

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [ISkeletonAnimationController](../server/ISkeletonAnimationController.md)

**Derived by:** [CBaseAnimGraphController](../server/CBaseAnimGraphController.md), [CBaseAnimGraphController](../server/CBaseAnimGraphController.md)

**Relationships:**

```mermaid
classDiagram
    ISkeletonAnimationController <|-- CSkeletonAnimationController
    CSkeletonAnimationController <|-- CBaseAnimGraphController
    CSkeletonAnimationController --> CSkeletonInstance
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_pSkeletonInstance` | [CSkeletonInstance](../server/CSkeletonInstance.md)* |  | `MNotSaved` |
