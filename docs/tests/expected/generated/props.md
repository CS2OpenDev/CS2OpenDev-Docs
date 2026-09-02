---
layout: default
title: Prop Data
nav_order: 13
---

# Prop & Collision Data

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

## Prop classes

3 prop classes.

| Class | Properties |
|-------|------------|
| `Cardboard.Base` | dmg.bullets=`0.5`; dmg.club=`1.25`; dmg.explosive=`1.5` |
| `Cardboard.Indestructable` | base=`Cardboard.Base` |
| `Cardboard.Large` | base=`Cardboard.Base`; health=`40`; physicsmode=`1` |

## Collision groups

4 collision groups.

| Group | Description | Interacts as | Interacts with |
|-------|-------------|--------------|----------------|
| `ConditionallySolid` | Solid to only players and npcs, has the same functionality as clip brush | `playerclip`, `npcclip` |  |
| `ConditionallySolid` | Solid to drones only | `csgo_droneclip` |  |
| `ConditionallySolid` | Solid to grenades only | `csgo_grenadeclip` |  |
| `ConditionallySolid` | Solid but exclude bullets &amp; grenades. | `passbullets` |  |

## Breakable gib groups

2 gib groups.

- **`ConcreteChunks`**: 5 models
- **`GlassChunks`**: 6 models
