---
title: CStateNodeInstanceData
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CStateNodeInstanceData

# CStateNodeInstanceData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 76 bytes (`0x4c`) · **Align:** n/a (unspecified) · **Module:** animgraphlib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_stateWeights` | CRelativeArray< float32 > |  |  |
| `0x8` | `m_vTransitionVelocityDeltaWS` | Vector |  |  |
| `0x20` | `m_currentStateStartTime` | CAnimNetVar< float32 > |  |  |
| `0x3c` | `m_resetCount` | CAnimNetVar< uint8 > |  |  |
