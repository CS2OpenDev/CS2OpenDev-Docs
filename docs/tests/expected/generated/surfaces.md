---
layout: default
title: Surface Properties
nav_order: 12
---

# Surface Properties

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

4 surface records — footstep sounds, physics, and bullet-penetration modifiers per material.  The same material can appear more than once, keyed by source file / scope.

| Surface | Scope | Source | Properties |
|---------|-------|--------|------------|
| `Balloon` | ct_player | `surfaceproperties_footsteps.txt` | walkleft=`CT_Default.StepLeft` |
| `Metal_Box` | ct_player | `surfaceproperties_footsteps.txt` |  |
| `Metal_Box` | t_player | `surfaceproperties_footsteps.txt` |  |
| `Metal_Box` |  | `surfaceproperties_game.txt` | bulletPenetrationDistanceModifier=`0.5` |
