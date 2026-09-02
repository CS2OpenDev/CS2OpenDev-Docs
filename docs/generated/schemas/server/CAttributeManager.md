---
title: CAttributeManager (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CAttributeManager

# CAttributeManager

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CAttributeManager (client)](../client/CAttributeManager.md)

**Derived by:** [CAttributeContainer](../server/CAttributeContainer.md)

**Relationships:**

```mermaid
classDiagram
    CAttributeManager <|-- CAttributeContainer
    CAttributeManager --> CBaseEntity
    CAttributeManager *-- `CAttributeManager::cached_attribute_float_t`
```

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_Providers` | CUtlVector< CHandle< [CBaseEntity](../server/CBaseEntity.md) > > |  |  |
| `0x20` | `m_iReapplyProvisionParity` | int32 |  |  |
| `0x24` | `m_hOuter` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x28` | `m_bPreventLoopback` | bool |  |  |
| `0x2c` | `m_ProviderType` | attributeprovidertypes_t |  |  |
| `0x30` | `m_CachedResults` | CUtlVector< [CAttributeManager::cached_attribute_float_t](../server/CAttributeManager.cached_attribute_float_t.md) > |  |  |
