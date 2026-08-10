---
layout: default
title: SmartPropDetailFadeLevel_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / SmartPropDetailFadeLevel_t

# SmartPropDetailFadeLevel_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `NONE` | 0 | None — No fade out. The object will not fade out, but will still be culled when below the minimum size and will pop at that that point. |
| `MOST_AGGRESSIVE` | 1 | Most Aggressive — Most aggressive fade out. The object will fade out while still quite large on screen. |
| `MORE_AGGRESSIVE` | 2 | More Aggressive — More aggressive fade out. The object will fade out while larger on screen than normal. |
| `NORMAL` | 3 | Normal — Normal fade out. The object will fade at when at the standard size on screen. |
| `LESS_AGGRESSIVE` | 4 | Less Aggressive — Less aggressive fade out. The object will not fade out until it is smaller on screen than normal. |
| `LEAST_AGGRESSIVE` | 5 | Least Aggressive — Least aggressive fade out. The object will be quite small before fading out. Fade out will only complete at the size cull limit. |
