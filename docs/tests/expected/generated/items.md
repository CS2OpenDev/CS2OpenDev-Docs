---
layout: default
title: Items & Economy
nav_order: 7
---

# Items & Economy

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Economy definitions extracted from the content pack's `items_game.txt`: weapon / equipment items, their prefabs, paint kits (skins), sticker kits, music kits, and the rarity / quality scales.  Name tokens (`#SFUI_*`, `#PaintKit_*`, …) resolve to display strings via the localization table.

## Items

6 item definitions.

| defIndex | Name token | Classname | Prefab | Item type |
|----------|------------|-----------|--------|-----------|
| 0 | `#SFUI_WPNHUD_Knife` | `weapon_knife` |  |  |
| 1 |  |  | `weapon_deagle_prefab` |  |
| 2 |  |  | `weapon_elite_prefab` |  |
| 3 |  |  | `weapon_fiveseven_prefab` |  |
| 4 |  |  | `weapon_glock_prefab` |  |
| 7 |  |  | `weapon_ak47_prefab` |  |

## Paint Kits — skins

3 paint kits.

| defIndex | Name | Description tag |
|----------|------|----------------|
| 0 | `default` | `#PaintKit_Default_Tag` |
| 2 | `so_olive` | `#PaintKit_so_olive_Tag` |
| 3 | `so_red` | `#PaintKit_so_red_Tag` |

## Sticker Kits

3 sticker kits.

| defIndex | Name | Item name token | Description |
|----------|------|-----------------|-------------|
| 0 | `default` | `#StickerKit_Default` | `#StickerKit_Desc_Default` |
| 1 | `dh_gologo1` | `#StickerKit_dh_gologo1` | `#StickerKit_desc_dh_gologo1` |
| 2 | `dh_gologo1_holo` | `#StickerKit_dh_gologo1_holo` | `#StickerKit_desc_dh_gologo1_holo` |

## Music Kits

2 music kits.

| defIndex | Name | Loc name |
|----------|------|----------|
| 1 | `valve_cs2_01` | `#musickit_valve_cs2_01` |
| 2 | `valve_02` | `#musickit_valve_csgo_02` |

## Prefabs

4 prefabs.

| id | Parent prefab | Classname | Item type |
|----|---------------|-----------|-----------|
| `antwerp2022_signature_capsule_prefab` | `weapon_case_base` |  |  |
| `antwerp2022_sticker_capsule_prefab` | `weapon_case_base` |  |  |
| `antwerp2022_tournament_journal_prefab` | `fan_shield` |  |  |
| `antwerp2022_tournament_pass_prefab` | `fan_token` |  |  |

## Rarities

3 rarities.

| id | Value | Loc key | Weapon loc key |
|----|-------|---------|----------------|
| `ancient` | 6 | `Rarity_Ancient` | `Rarity_Ancient_Weapon` |
| `common` | 1 | `Rarity_Common` | `Rarity_Common_Weapon` |
| `default` | 0 | `Rarity_Default` | `Rarity_Default_Weapon` |

## Qualities

3 qualities.

| id | Value |
|----|-------|
| `community` | 5 |
| `completed` | 10 |
| `customized` | 8 |
