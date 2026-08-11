---
layout: default
title: Prop Data
nav_order: 13
---

# Prop & Collision Data

{: .note }
> Source: CS2 build **24662694** · 2026-08-10 · `windows-x86_64` · schema `0.5.1`

## Prop classes (71)

| Class | Properties |
|-------|------------|
| `Cardboard.Base` | dmg.bullets=`0.5`; dmg.club=`1.25`; dmg.explosive=`1.5` |
| `Cardboard.Indestructable` | base=`Cardboard.Base` |
| `Cardboard.Large` | base=`Cardboard.Base`; health=`40`; physicsmode=`1` |
| `Cardboard.Medium` | base=`Cardboard.Base`; health=`20` |
| `Cardboard.Small` | base=`Cardboard.Base`; health=`10` |
| `Cardboard.break` | base=`Cardboard.Base`; health=`10`; physicsmode=`1` |
| `Cardboard.breakclient` | base=`Cardboard.Base`; health=`10`; physicsmode=`3` |
| `Cardboard.physics` | base=`Cardboard.Base`; health=`15` |
| `Cloth.Base` | dmg.bullets=`0.5`; dmg.club=`0.75`; dmg.explosive=`1.5` |
| `Cloth.Large` | base=`Cloth.Base`; health=`100`; physicsmode=`1` |
| `Cloth.Medium` | base=`Cloth.Base`; health=`50` |
| `Cloth.Object` | base=`Cloth.Base`; physicsmode=`3` |
| `Cloth.Small` | base=`Cloth.Base`; health=`30` |
| `Door.Standard` | dmg.bullets=`1.0`; dmg.club=`1.25`; dmg.explosive=`1.5`; health=`1000` |
| `Flesh.Base` | dmg.bullets=`1.25`; dmg.club=`1.0`; dmg.explosive=`1.5` |
| `Flesh.Small` | base=`Flesh.Base`; health=`10` |
| `Flesh.Tiny` | base=`Flesh.Base`; health=`3` |
| `Glass.Base` | dmg.bullets=`1.0`; dmg.club=`1.0`; dmg.explosive=`0.1` |
| `Glass.CSWindow` | base=`Glass.Window`; health=`1` |
| `Glass.CSWindow2` | base=`Glass.Window`; health=`1`; physicsmode=`1` |
| `Glass.Small` | base=`Glass.Base`; damage_table=`glass`; health=`5`; physicsmode=`3` |
| `Glass.Window` | base=`Glass.Base`; damage_table=`glass`; dmg.bullets=`0.5`; dmg.explosive=`1.0`; health=`1`; physicsmode=`1` |
| `Glass.WindowStrong` | base=`Glass.Base`; damage_table=`glass`; dmg.bullets=`0.5`; dmg.explosive=`1.0`; health=`100`; physicsmode=`3` |
| `Glass.picture` | base=`Glass.Base`; physicsmode=`1` |
| `Item.Base` | dmg.bullets=`1.0`; dmg.club=`1.0`; dmg.explosive=`1.0`; health=`0` |
| `Item.Large` | base=`Item.Base`; physicsmode=`1` |
| `Item.Medium` | base=`Item.Base` |
| `Item.Small` | base=`Item.Base` |
| `Metal.Base` | dmg.bullets=`1.0`; dmg.club=`1.0`; dmg.explosive=`1.0`; health=`0` |
| `Metal.Large` | base=`Metal.Base`; physicsmode=`1` |
| `Metal.Medium` | base=`Metal.Base`; physicsmode=`1` |
| `Metal.MediumClient` | base=`Metal.Base`; physicsmode=`3` |
| `Metal.Small` | base=`Metal.Base` |
| `Metal.break` | base=`Metal.Base`; health=`10`; physicsmode=`1` |
| `Metal.break2` | base=`Metal.Base`; health=`100`; physicsmode=`1` |
| `Plastic.Base` | dmg.bullets=`1.0`; dmg.club=`1.0`; dmg.explosive=`1.0`; health=`0` |
| `Plastic.Large` | base=`Plastic.Base`; physicsmode=`1` |
| `Plastic.Medium` | base=`Plastic.Base` |
| `Plastic.Small` | base=`Plastic.Base` |
| `Plastic.Small2` | base=`Plastic.Base`; physicsmode=`1` |
| `Plastic.SmallClient` | base=`Plastic.Base`; physicsmode=`3` |
| `Plastic.break` | base=`Plastic.Base`; health=`10`; physicsmode=`1` |
| `PlasticSmall.NoBreak` | base=`Plastic.Base`; physicsmode=`3` |
| `PlasticSmall.break` | base=`Plastic.Base`; health=`10`; physicsmode=`3` |
| `Pottery.Base` | dmg.bullets=`1.0`; dmg.club=`1.25`; dmg.explosive=`1.5` |
| `Pottery.Huge` | base=`Pottery.Base`; health=`100`; physicsmode=`1` |
| `Pottery.Large` | base=`Pottery.Base`; health=`70`; physicsmode=`1` |
| `Pottery.Medium` | base=`Pottery.Base`; health=`40` |
| `Pottery.Plant` | base=`Pottery.Base`; physicsmode=`3` |
| `Pottery.PlantBreak` | base=`Pottery.Base`; health=`20`; physicsmode=`3` |
| `Pottery.Small` | base=`Pottery.Base`; damage_table=`glass`; health=`5` |
| `Pottery.break` | base=`Pottery.Base`; health=`20`; physicsmode=`3` |
| `Pottery.break2` | base=`Pottery.Base`; health=`20`; physicsmode=`1` |
| `Stone.Base` | dmg.bullets=`1.0`; dmg.club=`1.0`; dmg.explosive=`1.0` |
| `Stone.Gigantic` | base=`Stone.Base`; health=`600`; physicsmode=`1` |
| `Stone.Huge` | base=`Stone.Base`; health=`400`; physicsmode=`1` |
| `Stone.Large` | base=`Stone.Base`; health=`200`; physicsmode=`1` |
| `Stone.Medium` | base=`Stone.Base`; health=`100` |
| `Stone.Small` | base=`Stone.Base`; health=`50`; physicsmode=`3` |
| `Wooden.Barrel` | base=`Wooden.Base`; breakable_count=`0`; health=`50`; physicsmode=`1` |
| `Wooden.Barrel2` | base=`Wooden.Base`; breakable_count=`0`; health=`201`; physicsmode=`1` |
| `Wooden.Base` | breakable_model=`WoodChunks`; breakable_skin=`0`; dmg.bullets=`0.75`; dmg.club=`2.0`; dmg.explosive=`1.5` |
| `Wooden.Huge` | base=`Wooden.Base`; breakable_count=`10`; health=`130`; physicsmode=`1` |
| `Wooden.Large` | base=`Wooden.Base`; breakable_count=`6`; health=`50`; physicsmode=`1` |
| `Wooden.Medium` | base=`Wooden.Base`; breakable_count=`4`; health=`30` |
| `Wooden.MediumNobreak` | base=`Wooden.Base`; physicsmode=`3` |
| `Wooden.Small` | base=`Wooden.Base`; breakable_count=`2`; health=`20` |
| `Wooden.Small2` | base=`Wooden.Base`; breakable_count=`2`; health=`1`; physicsmode=`1` |
| `Wooden.Tiny` | base=`Wooden.Base`; breakable_count=`0`; health=`6`; physicsmode=`3` |
| `Wooden.chair` | base=`Wooden.Base`; breakable_count=`4`; health=`25` |
| `Wooden.sticks` | base=`Wooden.Base`; breakable_count=`0`; physicsmode=`1` |

## Collision groups (15)

| Group | Description | Interacts as | Interacts with |
|-------|-------------|--------------|----------------|
| `ConditionallySolid` | Solid to only players and npcs, has the same functionality as clip brush | `playerclip`, `npcclip` |  |
| `ConditionallySolid` | Solid to drones only | `csgo_droneclip` |  |
| `ConditionallySolid` | Solid to grenades only | `csgo_grenadeclip` |  |
| `ConditionallySolid` | Solid but exclude bullets & grenades. | `passbullets` |  |
| `ConditionallySolid` | Solid but exclude bullets, grenades, and players.  csgo_railings_no_players usually have a separate clip brush for player collisions. | `passbullets` |  |
| `default` | Default collision |  |  |
| `ConditionallySolid` | Default collision, but occlude sound, block soundscape selection, etc | `blocksound`, `CONTENTS_SOLID` |  |
| `default` | Default collision but passes thrown grenades |  |  |
| `default` | Default collision but passes player movement and thrown grenades |  |  |
| `default` | Default collision, except ignored by player movement |  |  |
| `ConditionallySolid` | not solid to players or npc and passes bullets | `` |  |
| `ConditionallySolid` | Solid to everything but bullets | `passbullets` |  |
| `ConditionallySolid` | Does not collide with anything, but blocks sound | `blocksound` |  |
| `ConditionallySolid` | Default collision, but do not block line of sight | `CONTENTS_SOLID_NO_BLOCK_LOS` |  |
| `ConditionallySolid` | Solid but does not block light or LOS | `window` |  |

## Breakable gib groups (4)

- **`ConcreteChunks`**: 5 models
- **`GlassChunks`**: 6 models
- **`MetalChunks`**: 5 models
- **`WoodChunks`**: 5 models
