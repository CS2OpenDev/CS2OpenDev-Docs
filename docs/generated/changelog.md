---
title: Changelog
---

# Build Changelog

> Source: **Build 25218825** · 2026-09-09 · `windows-x86_64` · schema `0.10.0`

Difference between build **25175329** and **25218825** (`windows-x86_64`), grouped by data family.

Families diffed: `classes`, `enums`, `convars`, `commands`, `engine_constants`.

## classes (+2 / −0 / ~4)

**Added:** `client.dll/CCSCustomPlayerCamera`, `server.dll/CCSCustomPlayerCamera`

| Entry | Field changes |
|-------|---------------|
| `client.dll/CCSCustomHudLayout` | field_count: `6` → `7` |
| `client.dll/CCSPlayerCamera` | field_count: `3` → `0`; parent: `C_BaseEntity` → `CCSCustomPlayerCamera` |
| `server.dll/CCSCustomHudLayout` | field_count: `6` → `7` |
| `server.dll/CCSPlayerCamera` | field_count: `3` → `0`; parent: `CBaseEntity` → `CCSCustomPlayerCamera` |

## enums (+1 / −0 / ~2)

**Added:** `!GlobalTypes/CustomCameraMode_t`

| Entry | Field changes |
|-------|---------------|
| `!GlobalTypes/ECstrike15UserMessages` | member:CS_UM_SayText: `305` → ; member:CS_UM_SayText2: `306` → ; member:CS_UM_SayText2_CSGOLegacy:  → `306`; member:CS_UM_SayText_CSGOLegacy:  → `305`; member:CS_UM_TextMsg: `307` → ; member:CS_UM_TextMsg_CSGOLegacy:  → `307`; member:CS_UM_UpdateTeamMoney: `328` → ; member:CS_UM_UpdateTeamMoney_CSGOLegacy:  → `328` |
| `!GlobalTypes/SVC_Messages` | member:svc_EncryptedData:  → `78` |

## convars (+5 / −1 / ~0)

**Added:** `cl_decryptdata_key`, `cl_decryptdata_key_pub`, `tv_encryptdata_key`, `tv_encryptdata_key_pub`, `tv_relaytextchat`

**Removed:** `tv_show_allchat`

## engine_constants (+9 / −4 / ~0)

**Added:** `schema_enum:!GlobalTypes/CustomCameraMode_t/CustomCameraMode_t::CUSTOM_CAMERA_MODE_CONTROLLED`, `schema_enum:!GlobalTypes/CustomCameraMode_t/CustomCameraMode_t::CUSTOM_CAMERA_MODE_CONTROLLED_POSITION`, `schema_enum:!GlobalTypes/CustomCameraMode_t/CustomCameraMode_t::CUSTOM_CAMERA_MODE_DISABLED`, `schema_enum:!GlobalTypes/CustomCameraMode_t/CustomCameraMode_t::CUSTOM_CAMERA_MODE_FOLLOW_POSITION`, `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_SayText2_CSGOLegacy`, `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_SayText_CSGOLegacy`, `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_TextMsg_CSGOLegacy`, `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_UpdateTeamMoney_CSGOLegacy`, `schema_enum:!GlobalTypes/SVC_Messages/SVC_Messages::svc_EncryptedData`

**Removed:** `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_SayText`, `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_SayText2`, `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_TextMsg`, `schema_enum:!GlobalTypes/ECstrike15UserMessages/ECstrike15UserMessages::CS_UM_UpdateTeamMoney`
