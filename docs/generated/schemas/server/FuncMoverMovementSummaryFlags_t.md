---
title: FuncMoverMovementSummaryFlags_t
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / FuncMoverMovementSummaryFlags_t

# FuncMoverMovementSummaryFlags_t

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `eNone` | 0 |  |
| `eMovementBegin` | 1 |  |
| `eStopBegin` | 2 |  |
| `eStopComplete` | 4 |  |
| `eReversing` | 8 |  |
| `eEventsDispatched` | 16 |  |
| `eLoopToStart` | 32 |  |
| `eLoopToEnd` | 64 |  |
| `eTransitionComplete` | 128 |  |
| `eStoppedDuringTransition` | 256 |  |
