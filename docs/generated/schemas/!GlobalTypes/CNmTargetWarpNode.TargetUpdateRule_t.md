---
layout: default
title: "CNmTargetWarpNode::TargetUpdateRule_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / CNmTargetWarpNode::TargetUpdateRule_t

# CNmTargetWarpNode::TargetUpdateRule_t

**Kind:** enum · **Underlying:** `uint8_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 |  |
| `Recalculate` | 1 | Recalculate Warped Root Motion |
| `Offset` | 2 | Offset Warped Root Motion |
| `RecalculateOrOffset` | 3 | Recalculate Or Offset Warped Root Motion — Will offset the warped root motion if we are pass warp events |
