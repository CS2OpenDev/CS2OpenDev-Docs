---
layout: default
title: C_IronSightController
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / C_IronSightController

# C_IronSightController

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 176 bytes (`0xb0`) · **Align:** n/a (unspecified) · **Module:** client

## Memory layout

13 fields (13 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_bIronSightAvailable` | bool |  |  |
| `0x14` | `m_flIronSightAmount` | float32 |  |  |
| `0x18` | `m_flIronSightAmountGained` | float32 |  |  |
| `0x1c` | `m_flIronSightAmountBiased` | float32 |  |  |
| `0x20` | `m_flIronSightAmount_Interpolated` | float32 |  |  |
| `0x24` | `m_flIronSightAmountGained_Interpolated` | float32 |  |  |
| `0x28` | `m_flIronSightAmountBiased_Interpolated` | float32 |  |  |
| `0x2c` | `m_flInterpolationLastUpdated` | float32 |  |  |
| `0x30` | `m_angDeltaAverage` | QAngle[8] |  |  |
| `0x90` | `m_angViewLast` | QAngle |  |  |
| `0x9c` | `m_vecDotCoords` | Vector2D |  |  |
| `0xa4` | `m_flFiringInaccuracyExtraWidthMultiplier` | float32 |  |  |
| `0xa8` | `m_flSpeedRatio` | float32 |  |  |
