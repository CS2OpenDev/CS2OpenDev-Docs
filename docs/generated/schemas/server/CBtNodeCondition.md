---
layout: default
title: CBtNodeCondition
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CBtNodeCondition

# CBtNodeCondition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CBtNodeDecorator](../server/CBtNodeDecorator.md)

**Derived by:** [CBtNodeConditionInactive](../server/CBtNodeConditionInactive.md)

**Relationships:**

```mermaid
classDiagram
    CBtNodeDecorator <|-- CBtNodeCondition
    CBtNode <|-- CBtNodeDecorator
    CBtNodeCondition <|-- CBtNodeConditionInactive
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x58` | `m_bNegated` | bool |  |  |
