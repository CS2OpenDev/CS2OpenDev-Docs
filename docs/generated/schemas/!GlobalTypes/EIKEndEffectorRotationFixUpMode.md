---
layout: default
title: EIKEndEffectorRotationFixUpMode
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / EIKEndEffectorRotationFixUpMode

# EIKEndEffectorRotationFixUpMode

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | None — However the end effector ends up after the solve, it's rotation will remain unchanged. |
| `MatchTargetOrientation` | 1 | Match Target Orientation — The targets orientation will be stamped onto the end effector. |
| `LookAtTargetForward` | 2 | Look At Target Forward — The targets forward vector will be used to build a look orientation while preserving the rotation of the end effector after the solve as much as possible. |
| `MaintainParentOrientation` | 3 | Maintain Parent Orientation — Use the parent bone's orientation as the end effector's orientation. |
| `Count` | 4 |  |
