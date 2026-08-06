---
layout: default
title: Changelog
nav_order: 10
---

# Build Changelog

{: .note }
> Source: CS2 build **24537688** · 2026-08-03 · `windows-x86_64` · schema `0.5.0`

Difference between build **24304127** and **24537688** (`windows-x86_64`), grouped by data family.

## classes (+0 / −0 / ~2)

| Entry | Field changes |
|-------|---------------|
| `client.dll/C_CSPlayerPawn` | field_count: `101` → `102` |
| `server.dll/CCSPlayerPawn` | field_count: `104` → `105` |

## enums (+0 / −0 / ~1)

| Entry | Field changes |
|-------|---------------|
| `!GlobalTypes/EGCItemMsg` | member:k_EMsgGCTradingBase: `1500` → ``; member:k_EMsgGCTrading_CancelSession: `1510` → ``; member:k_EMsgGCTrading_ConfirmOffer: `1512` → ``; member:k_EMsgGCTrading_InitiateTradeRequest: `1501` → ``; member:k_EMsgGCTrading_InitiateTradeResponse: `1502` → ``; member:k_EMsgGCTrading_ReadinessResponse: `1508` → ``; member:k_EMsgGCTrading_RemoveItem: `1505` → ``; member:k_EMsgGCTrading_SessionClosed: `1509` → ``; member:k_EMsgGCTrading_SetItem: `1504` → ``; member:k_EMsgGCTrading_SetReadiness: `1507` → ``; member:k_EMsgGCTrading_StartSession: `1503` → ``; member:k_EMsgGCTrading_TradeChatMsg: `1511` → ``; member:k_EMsgGCTrading_TradeTypingChatMsg: `1513` → ``; member:k_EMsgGCTrading_UpdateTradeInfo: `1506` → `` |

## convars (+0 / −0 / ~1)

| Entry | Field changes |
|-------|---------------|
| `composite_material_cache_count_max` | default: `16` → `24` |

## engine_constants (+0 / −14 / ~0)

**Removed:** `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTradingBase`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_CancelSession`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_ConfirmOffer`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_InitiateTradeRequest`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_InitiateTradeResponse`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_ReadinessResponse`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_RemoveItem`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_SessionClosed`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_SetItem`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_SetReadiness`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_StartSession`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_TradeChatMsg`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_TradeTypingChatMsg`, `schema_enum:!GlobalTypes/EGCItemMsg/EGCItemMsg::k_EMsgGCTrading_UpdateTradeInfo`
