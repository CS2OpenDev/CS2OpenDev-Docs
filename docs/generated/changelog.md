---
title: Changelog
---

# Build Changelog

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

Difference between build **26144732** and **26281801** (`windows-x86_64`), grouped by data family.

Families diffed: `classes`, `enums`, `convars`, `commands`, `engine_constants`.

## classes (+0 / −0 / ~3)

| Entry | Field changes |
|-------|---------------|
| `client.dll/C_CSGameRules` | field_count: `98` → `99` |
| `server.dll/CCSGameRules` | field_count: `189` → `190` |
| `server.dll/CCSWeaponBase` | field_count: `59` → `58` |

## enums (+0 / −0 / ~1)

| Entry | Field changes |
|-------|---------------|
| `!GlobalTypes/WeaponGameplayAnimState` | member:WPN_ANIMSTATE_RELOAD_OUTRO_SILENT:  → `803`; member:WPN_ANIMSTATE_RELOAD_SILENT:  → `802` |

## convars (+2 / −0 / ~0)

**Added:** `cl_weapon_stealth_reload_toggle`, `vulkan_pipeline_cache_max_size_mb`

## engine_constants (+2 / −0 / ~0)

**Added:** `schema_enum:!GlobalTypes/WeaponGameplayAnimState/WeaponGameplayAnimState::WPN_ANIMSTATE_RELOAD_OUTRO_SILENT`, `schema_enum:!GlobalTypes/WeaponGameplayAnimState/WeaponGameplayAnimState::WPN_ANIMSTATE_RELOAD_SILENT`
