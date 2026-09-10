---
title: ObserverMode_t
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / ObserverMode_t

# ObserverMode_t

> Source: **Build 25218825** · 2026-09-09 · `windows-x86_64` · schema `0.10.0`

Spectator camera mode (m_iObserverMode).

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `OBS_MODE_NONE` | 0 | Not observing. |
| `OBS_MODE_FIXED` | 1 | Fixed camera position. |
| `OBS_MODE_IN_EYE` | 2 | First-person: sees through the observed player's eyes. |
| `OBS_MODE_CHASE` | 3 | Third-person chase camera behind the observed player. |
| `OBS_MODE_ROAMING` | 4 | Free-roaming (free-fly) camera. |
| `NUM_OBSERVER_MODES` | 5 |  |
