---
layout: default
title: EDestructiblePartDamagePassThroughType
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / EDestructiblePartDamagePassThroughType

# EDestructiblePartDamagePassThroughType

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `Normal` | 0 | Damage reduces the part's health pool and the owner entity equally. |
| `Absorb` | 1 | Damage reduces the part's health pool but not the owner entity until destroyed. (i.e., limited armour) |
| `InvincibleAbsorb` | 2 | Damage is completely ignored - i.e., this part ignores the health value and does not send damage to the owner entity. |
| `InvinciblePassthrough` | 3 | Damage reduces the owner entity but not the part (health is ignored): part can only be destroyed by gibbing or procedurally. |
