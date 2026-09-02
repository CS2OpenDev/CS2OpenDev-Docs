---
layout: default
title: CAttributeManager (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CAttributeManager

# CAttributeManager

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CAttributeManager (server)](../server/CAttributeManager.md)

**Derived by:** [C_AttributeContainer](../client/C_AttributeContainer.md)

**Relationships:**

```mermaid
classDiagram
    CAttributeManager <|-- C_AttributeContainer
    CAttributeManager --> C_BaseEntity
    CAttributeManager *-- `CAttributeManager::cached_attribute_float_t`
```

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_Providers` | CUtlVector< CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > > |  |  |
| `0x20` | `m_iReapplyProvisionParity` | int32 |  |  |
| `0x24` | `m_hOuter` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  |  |
| `0x28` | `m_bPreventLoopback` | bool |  |  |
| `0x2c` | `m_ProviderType` | attributeprovidertypes_t |  |  |
| `0x30` | `m_CachedResults` | CUtlVector< [CAttributeManager::cached_attribute_float_t](../client/CAttributeManager.cached_attribute_float_t.md) > |  |  |
