---
layout: default
title: Surface Properties
nav_order: 12
---

# Surface Properties

{: .note }
> Source: CS2 build **24537688** · 2026-08-03 · `windows-x86_64` · schema `0.5.0`

303 surface records — footstep sounds, physics, and bullet-penetration modifiers per material.  The same material can appear more than once, keyed by source file / scope.

| Surface | Scope | Source | Properties |
|---------|-------|--------|------------|
| `Balloon` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Default.StepLeft` |
| `Metal_Box` | ct_player | `surfaceproperties_footsteps.txt` |  |
| `Metal_Box` | t_player | `surfaceproperties_footsteps.txt` |  |
| `Metal_Box` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.5` |
| `Plastic_Box` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Plastic_Box.StepLeft`; walkright=`CT_Plastic_Box.StepLeft` |
| `Plastic_Box` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Plastic_Box.StepLeft`; walkright=`T_Plastic_Box.StepLeft` |
| `Plastic_Box` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.75`; gamematerial=`L` |
| `Plastic_Box` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_plastic.vpcf`; effect_simplified=`particles/impact_fx/impact_plastic_cheap.vpcf`; impactDecalName=`Impact.Plastic` |
| `Plastic_Box` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.05, 0.25, 0.35, 0.25, 0.18, 0.12, 0.07, 0.04, 0.02, 0.02]`; scatteringCoefficients=`[0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]`; transmissionCoefficients=`[1, 1, 0.36, 0.092, 0.023, 0.006, 0.001, 0, 0, 0, 0]` |
| `WeaponFlashbang` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_GlassBottle.StepLeft`; walkright=`CT_GlassBottle.StepLeft` |
| `WeaponFlashbang` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_GlassBottle.StepLeft`; walkright=`T_GlassBottle.StepLeft` |
| `WeaponHEGrenade` | ct_player | `surfaceproperties_footsteps.txt` |  |
| `WeaponHEGrenade` | t_player | `surfaceproperties_footsteps.txt` |  |
| `WeaponIncendiary` | ct_player | `surfaceproperties_footsteps.txt` |  |
| `WeaponIncendiary` | t_player | `surfaceproperties_footsteps.txt` |  |
| `WeaponMolotov` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_GlassBottle.StepLeft`; walkright=`CT_GlassBottle.StepLeft` |
| `WeaponMolotov` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_GlassBottle.StepLeft`; walkright=`T_GlassBottle.StepLeft` |
| `Wood` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Wood.StepLeft`; walkright=`CT_Wood.StepLeft` |
| `Wood` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Wood.StepLeft`; walkright=`T_Wood.StepLeft` |
| `Wood` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.6`; bulletPenetrationDistanceModifier=`0.9`; gamematerial=`W` |
| `Wood` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_wood.vpcf`; effect_simplified=`particles/impact_fx/impact_wood_cheap.vpcf`; impactDecalName=`Impact.Wood`; impactGrazingDecalName=`Impact.Wood_Grazing` |
| `Wood` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.05, 0.1, 0.07, 0.05, 0.04, 0.04, 0.04, 0.04, 0.05, 0.05]`; scatteringCoefficients=`[0.01, 0.01, 0.02, 0.03, 0.05, 0.06, 0.08, 0.1, 0.1, 0.12, 0.15]`; transmissionCoefficients=`[0.95, 0.35, 0.11, 0.04, 0.02, 0.01, 0.01, 0, 0, 0, 0]` |
| `Wood_Basket` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Wood_Basket.StepLeft`; walkright=`CT_Wood_Basket.StepLeft` |
| `Wood_Basket` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Wood_Basket.StepLeft`; walkright=`T_Wood_Basket.StepLeft` |
| `Wood_Basket` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.9` |
| `Wood_Box` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_WoodBox.StepLeft`; walkright=`CT_WoodBox.StepLeft` |
| `Wood_Box` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_WoodBox.StepLeft`; walkright=`T_WoodBox.StepLeft` |
| `Wood_Box` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.9` |
| `Wood_Crate` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Wood_Crate.StepLeft`; walkright=`CT_Wood_Crate.StepLeft` |
| `Wood_Crate` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Wood_Crate.StepLeft`; walkright=`T_Wood_Crate.StepLeft` |
| `Wood_Crate` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.9` |
| `Wood_Dense` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Wood_Solid.StepLeft`; walkright=`CT_Wood_Solid.StepLeft` |
| `Wood_Dense` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Wood_Solid.StepLeft`; walkright=`T_Wood_Solid.StepLeft` |
| `Wood_Dense` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.3`; bulletPenetrationDistanceModifier=`0.5`; gamematerial=`13` |
| `Wood_Ladder` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Wood_Ladder.StepLeft`; walkright=`CT_Wood_Ladder.StepLeft` |
| `Wood_Ladder` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Wood_Ladder.StepLeft`; walkright=`T_Wood_Ladder.StepLeft` |
| `Wood_Ladder` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.9`; climbable=`true`; gamematerial=`X` |
| `Wood_Panel` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Wood_Panel.StepLeft`; walkright=`CT_Wood_Panel.StepLeft` |
| `Wood_Panel` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Wood_Panel.StepLeft`; walkright=`T_Wood_Panel.StepLeft` |
| `Wood_Plank` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.85` |
| `Wood_Solid` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.8` |
| `alienflesh` |  | `surfaceproperties_game.txt` | gamematerial=`H` |
| `armorflesh` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.3`; bulletPenetrationDistanceModifier=`0.5`; gamematerial=`M` |
| `asphalt` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.3`; bulletPenetrationDistanceModifier=`0.55`; gamematerial=`Q` |
| `asphalt` |  | `surfaceproperties_impact_effects.txt` | impactDecalName=`Impact.Asphalt`; impactGrazingDecalName=`Impact.Asphalt_Grazing` |
| `asphalt` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.02, 0.03, 0.04, 0.04, 0.05, 0.04, 0.03, 0.02, 0.01]`; scatteringCoefficients=`[0, 0, 0.05, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]`; transmissionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0, 0, 0, 0, 0, 0, 0]` |
| `audioblocker` |  | `surfaceproperties_game.txt` | gamematerial=`X` |
| `audioblocker` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`; scatteringCoefficients=`[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `blockbullets` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.001`; bulletPenetrationDistanceModifier=`0.01`; gamematerial=`X` |
| `blockbullets` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `bloodyflesh` |  | `surfaceproperties_game.txt` | gamematerial=`B` |
| `brass_bell_large` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `brass_bell_medium` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `brass_bell_small` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `brass_bell_smallest` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `brass_bell_smallest_g` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `brick` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.3`; bulletPenetrationDistanceModifier=`0.47`; gamematerial=`R` |
| `cardboard` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Cardboard.StepLeft`; walkright=`CT_Cardboard.StepLeft` |
| `cardboard` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Cardboard.StepLeft`; walkright=`T_Cardboard.StepLeft` |
| `cardboard` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.99`; bulletPenetrationDistanceModifier=`0.95`; gamematerial=`U` |
| `cardboard` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0, 0.01, 0.05, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02]`; scatteringCoefficients=`[0, 0, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]`; transmissionCoefficients=`[0.99, 0.98, 0.95, 0.9, 0.8, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]` |
| `carpet` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Carpet.StepLeft`; walkright=`T_Carpet.StepLeft` |
| `carpet` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Carpet.StepLeft`; walkright=`T_Carpet.StepLeft` |
| `carpet` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.75`; gamematerial=`7` |
| `carpet` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_carpet.vpcf`; effect_simplified=`particles/impact_fx/impact_carpet_cheap.vpcf`; impactDecalName=`Impact.Upholstery`; impactGrazingDecalName=`Impact.Upholstery_Grazing` |
| `carpet` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0, 0.01, 0.05, 0.2, 0.3, 0.35, 0.5, 0.6, 0.6, 0.5]`; scatteringCoefficients=`[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.15, 0.2, 0.2, 0.2, 0.2]`; transmissionCoefficients=`[0.05, 0.02, 0.01, 0.01, 0, 0, 0, 0, 0, 0, 0]` |
| `ceiling_tile` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Ceiling_Tile.StepLeft`; walkright=`CT_Ceiling_Tile.StepLeft` |
| `ceiling_tile` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Ceiling_Tile.StepLeft`; walkright=`T_Ceiling_Tile.StepLeft` |
| `ceiling_tile` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.05, 0.3, 0.45, 0.7, 0.8, 0.8, 0.65, 0.45, 0.45, 0.3]`; scatteringCoefficients=`[0, 0, 0.05, 0.05, 0.1, 0.2, 0.25, 0.25, 0.25, 0.2, 0.2]`; transmissionCoefficients=`[0.8, 0.6, 0.4, 0.3, 0.2, 0.05, 0.1, 0.2, 0.3, 0.3, 0.3]` |
| `chain` |  | `surfaceproperties_game.txt` |  |
| `chainlink` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_ChainLink.StepLeft`; walkright=`CT_ChainLink.StepLeft` |
| `chainlink` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_ChainLink.StepLeft`; walkright=`T_ChainLink.StepLeft` |
| `chainlink` |  | `surfaceproperties_game.txt` | allowsmokethrough=`true`; bulletPenetrationDamageModifier=`0.99`; bulletPenetrationDistanceModifier=`0.99`; gamematerial=`G` |
| `chainlink` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_chainlink.vpcf` |
| `chainlink` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.02, 0.03, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; scatteringCoefficients=`[0, 0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.8, 0.9]`; transmissionCoefficients=`[0.1, 0.05, 0.01, 0.01, 0.01, 0, 0, 0, 0, 0, 0]` |
| `clay` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.6`; bulletPenetrationDistanceModifier=`0.95`; gamematerial=`1` |
| `computer` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.45`; bulletPenetrationDistanceModifier=`0.4`; gamematerial=`P` |
| `computer` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_computer.vpcf`; effect_simplified=`particles/impact_fx/impact_computer_cheap.vpcf`; impactDecalName=`Impact.Computer` |
| `concrete` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Concrete.StepLeft`; walkright=`CT_Concrete.StepLeft` |
| `concrete` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Concrete.StepLeft`; walkright=`T_Concrete.StepLeft` |
| `concrete` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.25`; bulletPenetrationDistanceModifier=`0.5`; gamematerial=`C` |
| `concrete` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_concrete.vpcf`; effect_simplified=`particles/impact_fx/impact_concrete_cheap.vpcf`; impactDecalName=`Impact.Concrete` |
| `concrete` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0, 0, 0.01, 0.02, 0.02, 0.02, 0.02, 0.05, 0.05, 0.05]`; scatteringCoefficients=`[0.01, 0.01, 0.05, 0.05, 0.07, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]`; transmissionCoefficients=`[0.001, 0.001, 0.001, 0.001, 0, 0, 0, 0, 0, 0, 0]` |
| `concrete_polished` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Ceiling_Tile.StepLeft`; walkright=`CT_Ceiling_Tile.StepLeft` |
| `concrete_polished` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Ceiling_Tile.StepLeft`; walkright=`T_Ceiling_Tile.StepLeft` |
| `default` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Default.StepLeft`; walkright=`CT_Default.StepLeft` |
| `default` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Default.StepLeft`; walkright=`T_Default.StepLeft` |
| `default` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.5`; bulletPenetrationDistanceModifier=`0.5`; climbable=`false`; gamematerial=`C`; jumpfactor=`1`; maxspeedfactor=`1` |
| `default` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_concrete.vpcf`; effect_simplified=`particles/impact_fx/impact_concrete_cheap.vpcf`; impactDecalName=`Impact.Concrete` |
| `default` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `default_silent` |  | `surfaceproperties_game.txt` | gamematerial=`X` |
| `default_silent` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`; scatteringCoefficients=`[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `dirt` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Dirt.StepLeft`; walkright=`CT_Dirt.StepLeft` |
| `dirt` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Dirt.StepLeft`; walkright=`T_Dirt.StepLeft` |
| `dirt` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.3`; bulletPenetrationDistanceModifier=`0.6`; gamematerial=`D` |
| `dirt` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_dirt.vpcf`; effect_simplified=`particles/impact_fx/impact_dirt_cheap.vpcf`; impactDecalName=`Impact.Dirt` |
| `dirt` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.05, 0.05, 0.05, 0.15, 0.35, 0.7, 0.85, 0.88, 0.85, 0.8, 0.75]`; scatteringCoefficients=`[0.1, 0.1, 0.1, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45]`; transmissionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]` |
| `dufflebag_survivalCase` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Silent.StepLeft`; walkright=`CT_Silent.StepLeft` |
| `dufflebag_survivalCase` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Silent.StepLeft`; walkright=`T_Silent.StepLeft` |
| `flesh` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Flesh.StepLeft`; walkright=`CT_Flesh.StepLeft` |
| `flesh` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Flesh.StepLeft`; walkright=`T_Flesh.StepLeft` |
| `flesh` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.9`; gamematerial=`F` |
| `flesh` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.03, 0.05, 0.29, 0.43, 0.51, 0.68, 0.71, 0.73, 0.75, 0.8]`; scatteringCoefficients=`[0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]`; transmissionCoefficients=`[0.95, 0.9, 0.8, 0.7, 0.5, 0.3, 0.1, 0.05, 0.02, 0.01, 0.01]` |
| `foliage` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Foliage.StepLeft`; walkright=`CT_Foliage.StepLeft` |
| `foliage` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Foliage.StepLeft`; walkright=`T_Foliage.StepLeft` |
| `foliage` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.95`; gamematerial=`O` |
| `foliage` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_leaves.vpcf`; effect_simplified=`particles/impact_fx/impact_leaves_cheap.vpcf`; impactDecalName=`Impact.Leaves` |
| `fruit` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Flesh.StepLeft`; walkright=`CT_Flesh.StepLeft` |
| `fruit` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Flesh.StepLeft`; walkright=`T_Flesh.StepLeft` |
| `fruit` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.9`; gamematerial=`F` |
| `glass` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Glass.StepLeft`; walkright=`CT_Glass.StepLeft` |
| `glass` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Glass.StepLeft`; walkright=`T_Glass.StepLeft` |
| `glass` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.99`; gamematerial=`Y` |
| `glass` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_glass.vpcf`; effect_simplified=`particles/impact_fx/impact_glass_cheap.vpcf`; impactDecalName=`Impact.Glass` |
| `glass` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.01, 0.05, 0.1, 0.06, 0.04, 0.03, 0.02, 0.02, 0.02, 0.02]`; scatteringCoefficients=`[0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.05, 0.07, 0.1, 0.1, 0.1]`; transmissionCoefficients=`[0.98, 0.25, 0.06, 0.003, 0.001, 0.001, 0, 0, 0, 0, 0]` |
| `glassbottle` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_GlassBottle.StepLeft`; walkright=`CT_GlassBottle.StepLeft` |
| `glassbottle` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_GlassBottle.StepLeft`; walkright=`T_GlassBottle.StepLeft` |
| `glassbottle` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.99` |
| `glassfloor` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Glass.StepLeft`; walkright=`CT_Glass.StepLeft` |
| `glassfloor` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Glass.StepLeft`; walkright=`T_Glass.StepLeft` |
| `glassfloor` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.99`; gamematerial=`Y` |
| `glassfloor` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_glass.vpcf`; impactDecalName=`Impact.Glass`; impactGrazingDecalName=`Impact.Glass` |
| `glassfloor` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.01, 0.05, 0.1, 0.06, 0.04, 0.03, 0.02, 0.02, 0.02, 0.02]`; scatteringCoefficients=`[0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.05, 0.07, 0.1, 0.1, 0.1]`; transmissionCoefficients=`[0.98, 0.25, 0.06, 0.003, 0.001, 0.001, 0, 0, 0, 0, 0]` |
| `grass` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Grass.StepLeft`; walkright=`CT_Grass.StepLeft` |
| `grass` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Grass.StepLeft`; walkright=`T_Grass.StepLeft` |
| `grass` |  | `surfaceproperties_game.txt` | gamematerial=`J` |
| `grass` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_grass.vpcf` |
| `grass` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.02, 0.03, 0.06, 0.12, 0.25, 0.6, 0.92, 0.94, 0.95, 0.96]`; scatteringCoefficients=`[0.02, 0.04, 0.06, 0.1, 0.2, 0.4, 0.6, 0.75, 0.85, 0.9, 0.9]`; transmissionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]` |
| `gravel` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Gravel.StepLeft`; walkright=`CT_Gravel.StepLeft` |
| `gravel` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Gravel.StepLeft`; walkright=`T_Gravel.StepLeft` |
| `gravel` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.4` |
| `grenade` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Grenade.StepLeft`; walkright=`CT_Grenade.StepLeft` |
| `grenade` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Grenade.StepLeft`; walkright=`T_Grenade.StepLeft` |
| `ice` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.75` |
| `ice` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.1]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `ladder` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Ladder.StepLeft`; walkright=`CT_Ladder.StepLeft` |
| `ladder` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Ladder.StepLeft`; walkright=`T_Ladder.StepLeft` |
| `ladder` |  | `surfaceproperties_game.txt` | climbable=`true`; gamematerial=`X` |
| `metal` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.4` |
| `metal_barrel` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalBarrel.StepLeft`; walkright=`CT_MetalBarrel.StepLeft` |
| `metal_barrel` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalBarrel.StepLeft`; walkright=`T_MetalBarrel.StepLeft` |
| `metal_barrel` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.01`; bulletPenetrationDistanceModifier=`0.01`; gamematerial=`12` |
| `metal_barrelSoundOverride` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalBarrel.StepLeft`; walkright=`CT_MetalBarrel.StepLeft` |
| `metal_barrelSoundOverride` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalBarrel.StepLeft`; walkright=`T_MetalBarrel.StepLeft` |
| `metal_barrel_explodingSurvival` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalVehicle.StepLeft`; walkright=`CT_MetalVehicle.StepLeft` |
| `metal_barrel_explodingSurvival` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalVehicle.StepLeft`; walkright=`T_MetalVehicle.StepLeft` |
| `metal_sand_barrel` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalBarrel.StepLeft`; walkright=`CT_MetalBarrel.StepLeft` |
| `metal_sand_barrel` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalBarrel.StepLeft`; walkright=`T_MetalBarrel.StepLeft` |
| `metal_sand_barrel` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.01`; bulletPenetrationDistanceModifier=`0.01`; gamematerial=`12` |
| `metal_sheet_corrugated` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalBarrel.StepLeft`; walkright=`CT_MetalBarrel.StepLeft` |
| `metal_sheet_corrugated` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalBarrel.StepLeft`; walkright=`T_MetalBarrel.StepLeft` |
| `metal_shield` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Weapon.StepLeft`; walkright=`CT_Weapon.StepLeft` |
| `metal_shield` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Weapon.StepLeft`; walkright=`T_Weapon.StepLeft` |
| `metal_shield` |  | `surfaceproperties_game.txt` | gamematerial=`14` |
| `metal_survivalCase` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Silent.StepLeft`; walkright=`CT_Silent.StepLeft` |
| `metal_survivalCase` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Silent.StepLeft`; walkright=`T_Silent.StepLeft` |
| `metal_vehicleSoundOverride` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalVehicle.StepLeft`; walkright=`CT_MetalVehicle.StepLeft` |
| `metal_vehicleSoundOverride` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalVehicle.StepLeft`; walkright=`T_MetalVehicle.StepLeft` |
| `metaldogtags` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.4` |
| `metalgrate` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalGrate.StepLeft`; walkright=`CT_MetalGrate.StepLeft` |
| `metalgrate` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalGrate.StepLeft`; walkright=`T_MetalGrate.StepLeft` |
| `metalgrate` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.99`; bulletPenetrationDistanceModifier=`0.95`; gamematerial=`G` |
| `metalgrate` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_metal_grate.vpcf`; effect_simplified=`particles/impact_fx/impact_metal_cheap.vpcf`; impactDecalName=`Impact.Metal`; impactGrazingDecalName=`Impact.Metal_Grazing` |
| `metalgrate` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.02, 0.03, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; scatteringCoefficients=`[0, 0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.8, 0.9]`; transmissionCoefficients=`[0.1, 0.05, 0.01, 0.01, 0.01, 0, 0, 0, 0, 0, 0]` |
| `metalpanel` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalVehicle.StepLeft`; walkright=`CT_MetalVehicle.StepLeft` |
| `metalpanel` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalVehicle.StepLeft`; walkright=`T_MetalVehicle.StepLeft` |
| `metalpanel` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.45`; bulletPenetrationDistanceModifier=`0.5`; gamematerial=`V` |
| `metalrailing` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalRailing.StepLeft`; walkright=`CT_MetalRailing.StepLeft` |
| `metalrailing` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalRailing.StepLeft`; walkright=`T_MetalRailing.StepLeft` |
| `metalrailing` |  | `surfaceproperties_game.txt` | allowsmokethrough=`true` |
| `metalvehicle` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalVehicle.StepLeft`; walkright=`CT_MetalVehicle.StepLeft` |
| `metalvehicle` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalVehicle.StepLeft`; walkright=`T_MetalVehicle.StepLeft` |
| `metalvehicle` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.5` |
| `metalvent` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_MetalVent.StepLeft`; walkright=`CT_MetalVent.StepLeft` |
| `metalvent` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_MetalVent.StepLeft`; walkright=`T_MetalVent.StepLeft` |
| `metalvent` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.45`; bulletPenetrationDistanceModifier=`0.6`; gamematerial=`V` |
| `metalvent` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_metal_vent.vpcf`; effect_simplified=`particles/impact_fx/impact_metal_vent_cheap.vpcf`; impactDecalName=`Impact.Vent` |
| `mud` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Mud.StepLeft`; walkright=`CT_Mud.StepLeft` |
| `mud` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Mud.StepLeft`; walkright=`T_Mud.StepLeft` |
| `mud` |  | `surfaceproperties_game.txt` | gamematerial=`11` |
| `no_decal` |  | `surfaceproperties_game.txt` | gamematerial=`-` |
| `no_decal` |  | `surfaceproperties_impact_effects.txt` | impactDecalName=`` |
| `no_decal` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.02, 0.02, 0.02, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.12, 0.12]`; scatteringCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]`; transmissionCoefficients=`[0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002, 0.001, 0.015, 0.002]` |
| `plaster` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Concrete.StepLeft`; walkright=`CT_Concrete.StepLeft` |
| `plaster` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Concrete.StepLeft`; walkright=`T_Concrete.StepLeft` |
| `plaster` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.6`; bulletPenetrationDistanceModifier=`0.7`; gamematerial=`2` |
| `plaster` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_plaster.vpcf`; effect_simplified=`particles/impact_fx/impact_plaster_cheap.vpcf`; impactDecalName=`Impact.Plaster` |
| `plaster` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.02, 0.03, 0.03, 0.02, 0.03, 0.04, 0.05, 0.05, 0.05]`; scatteringCoefficients=`[0, 0.01, 0.02, 0.03, 0.05, 0.05, 0.05, 0.07, 0.1, 0.1, 0.1]`; transmissionCoefficients=`[0.001, 0.001, 0.001, 0.001, 0, 0, 0, 0, 0, 0, 0]` |
| `plaster_drywall` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Drywall.StepLeft`; walkright=`CT_Drywall.StepLeft` |
| `plaster_drywall` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Drywall.StepLeft`; walkright=`T_Drywall.StepLeft` |
| `plastic` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_plastic.vpcf`; effect_simplified=`particles/impact_fx/impact_plastic_cheap.vpcf`; impactDecalName=`Impact.Plastic` |
| `plastic_autoCover` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Plastic_autoCover.StepLeft`; walkright=`CT_Plastic_autoCover.StepLeft` |
| `plastic_autoCover` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Plastic_autoCover.StepLeft`; walkright=`T_Plastic_autoCover.StepLeft` |
| `plastic_barrel` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Plastic_Barrel.StepLeft`; walkright=`CT_Plastic_Barrel.StepLeft` |
| `plastic_barrel` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Plastic_Barrel.StepLeft`; walkright=`T_Plastic_Barrel.StepLeft` |
| `plastic_barrel` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.7`; gamematerial=`L` |
| `plastic_barrel` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_plastic.vpcf`; effect_simplified=`particles/impact_fx/impact_plastic_cheap.vpcf`; impactDecalName=`Impact.Plastic` |
| `plastic_barrel` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.05, 0.25, 0.35, 0.25, 0.18, 0.12, 0.07, 0.04, 0.02, 0.02]`; scatteringCoefficients=`[0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]`; transmissionCoefficients=`[1, 1, 0.36, 0.092, 0.023, 0.006, 0.001, 0, 0, 0, 0]` |
| `plastic_dumpster` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Plastic_Box.StepLeft`; walkright=`CT_Plastic_Box.StepLeft` |
| `plastic_dumpster` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Plastic_Box.StepLeft`; walkright=`T_Plastic_Box.StepLeft` |
| `plastic_milkCrate` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Plastic_milkCrate.StepLeft`; walkright=`CT_Plastic_milkCrate.StepLeft` |
| `plastic_milkCrate` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Plastic_milkCrate.StepLeft`; walkright=`T_Plastic_milkCrate.StepLeft` |
| `plastic_solid` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0` |
| `plastic_survivalCase` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Silent.StepLeft`; walkright=`CT_Silent.StepLeft` |
| `plastic_survivalCase` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Silent.StepLeft`; walkright=`T_Silent.StepLeft` |
| `player` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`; scatteringCoefficients=`[0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]`; transmissionCoefficients=`[0.95, 0.9, 0.8, 0.7, 0.5, 0.3, 0.1, 0.05, 0.02, 0.01, 0.01]` |
| `player_control_clip` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`1`; gamematerial=`I` |
| `player_control_clip` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`; scatteringCoefficients=`[0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]`; transmissionCoefficients=`[0.95, 0.9, 0.8, 0.7, 0.5, 0.3, 0.1, 0.05, 0.02, 0.01, 0.01]` |
| `porcelain` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.95` |
| `pottery` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.6`; bulletPenetrationDistanceModifier=`0.95`; gamematerial=`1` |
| `pottery` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_pottery.vpcf`; effect_simplified=`particles/impact_fx/impact_pottery_cheap.vpcf`; impactDecalName=`Impact.Tile` |
| `potterylarge` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.6`; bulletPenetrationDistanceModifier=`0.95`; gamematerial=`1` |
| `potterylarge` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_pottery.vpcf`; effect_simplified=`particles/impact_fx/impact_pottery_cheap.vpcf`; impactDecalName=`Impact.Tile` |
| `puddle` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Water.StepLeft`; walkright=`CT_Water.StepLeft` |
| `puddle` | t_player | `surfaceproperties_footsteps.txt` | runright=`T_Water.StepLeft`; walkleft=`T_Water.StepLeft`; walkright=`T_Water.StepLeft` |
| `puddle` |  | `surfaceproperties_game.txt` | gamematerial=`10` |
| `puddle` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.03]`; scatteringCoefficients=`[0, 0, 0.01, 0.02, 0.02, 0.03, 0.05, 0.1, 0.15, 0.2, 0.3]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `quicksand` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.2` |
| `quicksand` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.05, 0.05, 0.05, 0.05, 0.07, 0.07, 0.07, 0.05, 0.02, 0.02, 0.01]`; scatteringCoefficients=`[0, 0, 0.01, 0.02, 0.02, 0.03, 0.05, 0.05, 0.08, 0.1, 0.1]`; transmissionCoefficients=`[0.5, 0.15, 0.03, 0.01, 0, 0, 0, 0, 0, 0, 0]` |
| `rock` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.25`; gamematerial=`3` |
| `rock` |  | `surfaceproperties_impact_effects.txt` | impactDecalName=`Impact.Rock` |
| `rock` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0, 0.01, 0.01, 0.01, 0.02, 0.02, 0.03, 0.04, 0.05, 0.05]`; scatteringCoefficients=`[0.1, 0.12, 0.15, 0.2, 0.28, 0.35, 0.45, 0.55, 0.6, 0.65, 0.65]`; transmissionCoefficients=`[0.001, 0.001, 0.001, 0.001, 0, 0, 0, 0, 0, 0, 0]` |
| `rubber` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Rubber.StepLeft`; walkright=`CT_Rubber.StepLeft` |
| `rubber` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Rubber.StepLeft`; walkright=`T_Rubber.StepLeft` |
| `rubber` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.5`; bulletPenetrationDistanceModifier=`0.85`; gamematerial=`4` |
| `rubber` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_rubber.vpcf`; effect_simplified=`particles/impact_fx/impact_rubber_cheap.vpcf`; impactDecalName=`Impact.Rubber` |
| `rubber` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0, 0, 0, 0.05, 0.05, 0.1, 0.05, 0, 0, 0]`; scatteringCoefficients=`[0, 0, 0.02, 0.05, 0.05, 0.05, 0.05, 0.05, 0.08, 0.1, 0.1]`; transmissionCoefficients=`[1, 0.99, 0.8, 0.1, 0.02, 0.01, 0, 0, 0, 0, 0]` |
| `sand` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Sand.StepLeft`; walkright=`CT_Sand.StepLeft` |
| `sand` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Sand.StepLeft`; walkright=`T_Sand.StepLeft` |
| `sand` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.25`; bulletPenetrationDistanceModifier=`0.3`; gamematerial=`N` |
| `sheetrock` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Drywall.StepLeft`; walkright=`CT_Drywall.StepLeft` |
| `sheetrock` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Drywall.StepLeft`; walkright=`T_Drywall.StepLeft` |
| `sheetrock` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.6`; bulletPenetrationDistanceModifier=`0.85`; gamematerial=`5` |
| `sheetrock` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_plaster.vpcf`; effect_simplified=`particles/impact_fx/impact_plaster_cheap.vpcf`; impactDecalName=`Impact.Sheetrock` |
| `sheetrock` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.01, 0.4, 0.29, 0.1, 0.05, 0.04, 0.04, 0.05, 0.05, 0.05]`; scatteringCoefficients=`[0, 0, 0, 0.05, 0.05, 0.1, 0.1, 0.15, 0.2, 0.2, 0.2]`; transmissionCoefficients=`[0.3, 0.4, 0.5, 0.05, 0.01, 0.01, 0, 0, 0, 0, 0]` |
| `slime` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_SlipperySlime.StepLeft`; walkright=`CT_SlipperySlime.StepLeft` |
| `slime` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_SlipperySlime.StepLeft`; walkright=`T_SlipperySlime.StepLeft` |
| `slime` |  | `surfaceproperties_game.txt` | gamematerial=`S` |
| `slime` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.05, 0.05, 0.05, 0.05, 0.07, 0.07, 0.07, 0.05, 0.02, 0.02, 0.01]`; scatteringCoefficients=`[0, 0, 0.01, 0.02, 0.02, 0.03, 0.05, 0.05, 0.08, 0.1, 0.1]`; transmissionCoefficients=`[0.5, 0.15, 0.03, 0.01, 0, 0, 0, 0, 0, 0, 0]` |
| `slipperyslide` |  | `surfaceproperties_game.txt` | jumpfactor=`0.7` |
| `slipperyslime` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_SlipperySlime.StepLeft`; walkright=`CT_SlipperySlime.StepLeft` |
| `slipperyslime` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_SlipperySlime.StepLeft`; walkright=`T_SlipperySlime.StepLeft` |
| `slipperyslime` |  | `surfaceproperties_game.txt` | jumpfactor=`0.7` |
| `slipperyslime` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.05, 0.05, 0.05, 0.05, 0.07, 0.07, 0.07, 0.05, 0.02, 0.02, 0.01]`; scatteringCoefficients=`[0, 0, 0.01, 0.02, 0.02, 0.03, 0.05, 0.05, 0.08, 0.1, 0.1]`; transmissionCoefficients=`[0.5, 0.15, 0.03, 0.01, 0, 0, 0, 0, 0, 0, 0]` |
| `slowgrass` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Grass.StepLeft`; walkright=`CT_Grass.StepLeft` |
| `slowgrass` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Grass.StepLeft`; walkright=`T_Grass.StepLeft` |
| `slowgrass` |  | `surfaceproperties_game.txt` | gamematerial=`J`; maxspeedfactor=`1` |
| `slowgrass` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_wet_grass.vpcf` |
| `slowgrass` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.02, 0.03, 0.06, 0.12, 0.25, 0.6, 0.92, 0.94, 0.95, 0.96]`; scatteringCoefficients=`[0.02, 0.04, 0.06, 0.1, 0.2, 0.4, 0.6, 0.75, 0.85, 0.9, 0.9]`; transmissionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]` |
| `snow` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Snow.StepLeft`; walkright=`CT_Snow.StepLeft` |
| `snow` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Snow.StepLeft`; walkright=`T_Snow.StepLeft` |
| `snow` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.85`; gamematerial=`K` |
| `snow` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_snow.vpcf`; effect_simplified=`particles/impact_fx/impact_snow_cheap.vpcf`; impactDecalName=`Impact.Snow`; impactGrazingDecalName=`Impact.Snow_Grazing` |
| `snow` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.05, 0.1, 0.15, 0.25, 0.4, 0.55, 0.7, 0.8, 0.9, 0.95]`; scatteringCoefficients=`[0.1, 0.12, 0.14, 0.15, 0.18, 0.18, 0.15, 0.12, 0.07, 0.03, 0.02]`; transmissionCoefficients=`[0.3, 0.3, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05, 0.05]` |
| `soccerball` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Rubber.StepLeft`; walkright=`CT_Rubber.StepLeft` |
| `soccerball` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Rubber.StepLeft`; walkright=`T_Rubber.StepLeft` |
| `soccerball` |  | `surfaceproperties_game.txt` | gamematerial=`-` |
| `soccerball` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.05, 0.25, 0.35, 0.25, 0.18, 0.12, 0.07, 0.04, 0.02, 0.02]`; scatteringCoefficients=`[0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]`; transmissionCoefficients=`[1, 1, 0.36, 0.092, 0.023, 0.006, 0.001, 0, 0, 0, 0]` |
| `solidmetal` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_SolidMetal.StepLeft`; walkright=`CT_SolidMetal.StepLeft` |
| `solidmetal` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_SolidMetal.StepLeft`; walkright=`T_SolidMetal.StepLeft` |
| `solidmetal` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.3`; bulletPenetrationDistanceModifier=`0.27`; gamematerial=`M` |
| `solidmetal` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_metal.vpcf`; effect_simplified=`particles/impact_fx/impact_metal_cheap.vpcf`; impactDecalName=`Impact.Metal`; impactGrazingDecalName=`Impact.Metal_Grazing` |
| `solidmetal` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03, 0.03]`; scatteringCoefficients=`[0.05, 0.05, 0.05, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.1, 0.1]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `stucco` |  | `surfaceproperties_game.txt` | gamematerial=`2` |
| `sugarcane` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Grass.StepLeft`; walkright=`CT_Grass.StepLeft` |
| `sugarcane` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Grass.StepLeft`; walkright=`T_Grass.StepLeft` |
| `sugarcane` |  | `surfaceproperties_game.txt` | gamematerial=`J` |
| `tile` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Tile.StepLeft`; walkright=`CT_Tile.StepLeft` |
| `tile` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Tile.StepLeft`; walkright=`T_Tile.StepLeft` |
| `tile` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.3`; bulletPenetrationDistanceModifier=`0.7`; gamematerial=`T` |
| `tile` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_tile.vpcf`; effect_simplified=`particles/impact_fx/impact_tile_cheap.vpcf`; impactDecalName=`Impact.Tile` |
| `tile` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.02]`; scatteringCoefficients=`[0, 0, 0, 0.05, 0.1, 0.1, 0.2, 0.2, 0.2, 0.25, 0.25]`; transmissionCoefficients=`[0.001, 0.001, 0.001, 0.001, 0, 0, 0, 0, 0, 0, 0]` |
| `tile_survivalCase` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Silent.StepLeft`; walkright=`CT_Silent.StepLeft` |
| `tile_survivalCase` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Silent.StepLeft`; walkright=`T_Silent.StepLeft` |
| `tile_survivalCase_GIB` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Silent.StepLeft`; walkright=`CT_Silent.StepLeft` |
| `tile_survivalCase_GIB` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Silent.StepLeft`; walkright=`T_Silent.StepLeft` |
| `upholstery` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.75`; gamematerial=`9` |
| `upholstery` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_upholstery.vpcf`; effect_simplified=`particles/impact_fx/impact_upholstery_cheap.vpcf`; impactDecalName=`Impact.Upholstery`; impactGrazingDecalName=`Impact.Upholstery_Grazing` |
| `upholstery` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.3, 0.2, 0.1]`; scatteringCoefficients=`[0, 0, 0.05, 0.1, 0.3, 0.5, 0.7, 0.8, 0.8, 0.8, 0.8]`; transmissionCoefficients=`[0.99, 0.98, 0.95, 0.9, 0.8, 0.8, 0.5, 0.3, 0.1, 0.05, 0.05]` |
| `wade` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`Player.Wade`; walkright=`Player.Wade` |
| `wade` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`Player.Wade`; walkright=`Player.Wade` |
| `wade` |  | `surfaceproperties_game.txt` | gamematerial=`X` |
| `water` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Water.StepLeft`; walkright=`CT_Water.StepLeft` |
| `water` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Water.StepLeft`; walkright=`T_Water.StepLeft` |
| `water` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.3`; gamematerial=`S` |
| `water` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/water_impact/water_splash_03.vpcf` |
| `water` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.03]`; scatteringCoefficients=`[0, 0, 0.01, 0.02, 0.02, 0.03, 0.05, 0.1, 0.15, 0.2, 0.3]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `watermelon` |  | `surfaceproperties_game.txt` | bulletPenetrationDamageModifier=`0.6`; bulletPenetrationDistanceModifier=`0.95` |
| `weapon` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Weapon.StepLeft`; walkright=`CT_Weapon.StepLeft` |
| `weapon` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Weapon.StepLeft`; walkright=`T_Weapon.StepLeft` |
| `weapon_magazine` |  | `surfaceproperties_game.txt` | gamematerial=`M` |
| `wet` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_WetTile.StepLeft`; walkright=`CT_WetTile.StepLeft` |
| `wet` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_WetTile.StepLeft`; walkright=`T_WetTile.StepLeft` |
| `wet` |  | `surfaceproperties_game.txt` | gamematerial=`S` |
| `wet` |  | `surfaceproperties_impact_effects.txt` | effect=`particles/impact_fx/impact_concrete_wet.vpcf`; effect_simplified=`particles/impact_fx/impact_concrete_wet_cheap.vpcf`; impactDecalName=`` |
| `wet` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.03]`; scatteringCoefficients=`[0, 0, 0.01, 0.02, 0.02, 0.03, 0.05, 0.1, 0.15, 0.2, 0.3]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `wet_concrete` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_WetConcrete.StepLeft`; walkright=`CT_WetConcrete.StepLeft` |
| `wet_concrete` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_WetConcrete.StepLeft`; walkright=`T_WetConcrete.StepLeft` |
| `wet_mud` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_WetMud.StepLeft`; walkright=`CT_WetMud.StepLeft` |
| `wet_mud` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_WetMud.StepLeft`; walkright=`CT_WetMud.StepLeft` |
| `wet_sand` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Wet_Sand.StepLeft`; walkright=`CT_Wet_Sand.StepLeft` |
| `wet_sand` | t_player | `surfaceproperties_footsteps.txt` | walkleft=`T_Wet_Sand.StepLeft`; walkright=`T_Wet_Sand.StepLeft` |
| `wet_sand` |  | `surfaceproperties_steamaudio.txt` | absorptionCoefficients=`[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.03]`; scatteringCoefficients=`[0, 0, 0.01, 0.02, 0.02, 0.03, 0.05, 0.1, 0.15, 0.2, 0.3]`; transmissionCoefficients=`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
