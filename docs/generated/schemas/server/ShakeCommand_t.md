---
layout: default
title: ShakeCommand_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / ShakeCommand_t

# ShakeCommand_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Screen-shake command type sent to clients (start / stop / amplitude / frequency / duration).

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `SHAKE_START` | 0 |  |
| `SHAKE_STOP` | 1 |  |
| `SHAKE_AMPLITUDE` | 2 |  |
| `SHAKE_FREQUENCY` | 3 |  |
| `SHAKE_START_RUMBLEONLY` | 4 |  |
| `SHAKE_START_NORUMBLE` | 5 |  |
| `SHAKE_DURATION` | 6 |  |
