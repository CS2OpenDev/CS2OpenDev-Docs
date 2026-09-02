---
layout: default
title: CCSPlayerAnimationState
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayerAnimationState

# CCSPlayerAnimationState

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 224 bytes (`0xe0`) · **Align:** n/a (unspecified) · **Module:** server

**Relationships:**

```mermaid
classDiagram
    CCSPlayerAnimationState *-- `CCSPlayerAnimationState::MoveType_t`
    CCSPlayerAnimationState *-- `CCSPlayerAnimationState::GroundMoveState_t`
    CCSPlayerAnimationState *-- `CCSPlayerAnimationState::Direction_t`
    CCSPlayerAnimationState *-- `CCSPlayerAnimationState::AirAction_t`
    CCSPlayerAnimationState *-- GameTick_t
```

## Memory layout

16 fields (16 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_currentMoveType` | [CCSPlayerAnimationState::MoveType_t](../server/CCSPlayerAnimationState.MoveType_t.md) |  |  |
| `0x19` | `m_groundMoveState` | [CCSPlayerAnimationState::GroundMoveState_t](../server/CCSPlayerAnimationState.GroundMoveState_t.md) |  |  |
| `0x1a` | `m_groundActionDirection` | [CCSPlayerAnimationState::Direction_t](../server/CCSPlayerAnimationState.Direction_t.md) |  |  |
| `0x1b` | `m_airAction` | [CCSPlayerAnimationState::AirAction_t](../server/CCSPlayerAnimationState.AirAction_t.md) |  |  |
| `0x1c` | `m_bWasOnGroundLastUpdate` | bool |  |  |
| `0x1d` | `m_bWasStationaryLastUpdate` | bool |  |  |
| `0x20` | `m_actionStartTick` | [GameTick_t](../entity2/GameTick_t.md) |  |  |
| `0x24` | `m_staticAimTimerStartTick` | [GameTick_t](../entity2/GameTick_t.md) |  |  |
| `0x28` | `m_plantAndTurnStartTick` | [GameTick_t](../entity2/GameTick_t.md) |  |  |
| `0x2c` | `m_flTurnOnSpotAngle` | float32 |  |  |
| `0x30` | `m_flPreviousAimYaw` | float32 |  |  |
| `0x34` | `m_flPreviousHorizontalSpeed` | float32 |  |  |
| `0x38` | `m_flFootIKOffsetLeft` | float32 |  |  |
| `0x3c` | `m_flFootIKOffsetRight` | float32 |  |  |
| `0x40` | `m_flWeaponDropPercentageDueToMovement` | float32 |  |  |
| `0x44` | `m_flWeaponDropSmoothDampVelocity` | float32 |  |  |
