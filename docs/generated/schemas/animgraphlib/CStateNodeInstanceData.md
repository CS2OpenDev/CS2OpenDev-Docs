---
layout: default
title: CStateNodeInstanceData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CStateNodeInstanceData

# CStateNodeInstanceData

**Kind:** class · **Size:** 76 bytes (`0x4c`) · **Align:** 255 · **Module:** animgraphlib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_stateWeights` | CRelativeArray< float32 > |  |  |
| `0x8` | `m_vTransitionVelocityDeltaWS` | Vector |  |  |
| `0x20` | `m_currentStateStartTime` | CAnimNetVar< float32 > |  |  |
| `0x3c` | `m_resetCount` | CAnimNetVar< uint8 > |  |  |
