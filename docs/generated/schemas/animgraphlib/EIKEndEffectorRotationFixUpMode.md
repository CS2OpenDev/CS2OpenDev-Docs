---
title: EIKEndEffectorRotationFixUpMode
module: animgraphlib
kind: enum
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / EIKEndEffectorRotationFixUpMode

# EIKEndEffectorRotationFixUpMode

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** animgraphlib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | None — However the end effector ends up after the solve, it's rotation will remain unchanged. |
| `MatchTargetOrientation` | 1 | Match Target Orientation — The targets orientation will be stamped onto the end effector. |
| `LookAtTargetForward` | 2 | Look At Target Forward — The targets forward vector will be used to build a look orientation while preserving the rotation of the end effector after the solve as much as possible. |
| `MaintainParentOrientation` | 3 | Maintain Parent Orientation — Use the parent bone's orientation as the end effector's orientation. |
| `Count` | 4 |  |
