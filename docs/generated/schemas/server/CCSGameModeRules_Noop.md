---
layout: default
title: CCSGameModeRules_Noop (server)
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSGameModeRules_Noop

# CCSGameModeRules_Noop

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** server

**Twin:** [CCSGameModeRules_Noop (client)](../client/CCSGameModeRules_Noop.md)

**Inherits from:** [CCSGameModeRules](../server/CCSGameModeRules.md)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_Noop
```

## Memory layout

1 field (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CCSGameModeRules](../server/CCSGameModeRules.md) | `MNotSaved` |
