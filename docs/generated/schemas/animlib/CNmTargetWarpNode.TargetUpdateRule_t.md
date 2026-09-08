---
title: "CNmTargetWarpNode::TargetUpdateRule_t"
module: animlib
kind: enum
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTargetWarpNode::TargetUpdateRule_t

# CNmTargetWarpNode::TargetUpdateRule_t

> Source: **Build 25175329** · 2026-09-07 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint8_t` · **Module:** animlib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 |  |
| `Recalculate` | 1 | Recalculate Warped Root Motion |
| `Offset` | 2 | Offset Warped Root Motion |
| `RecalculateOrOffset` | 3 | Recalculate Or Offset Warped Root Motion — Will offset the warped root motion if we are pass warp events |
