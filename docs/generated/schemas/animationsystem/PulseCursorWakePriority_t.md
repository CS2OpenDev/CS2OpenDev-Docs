---
layout: default
title: PulseCursorWakePriority_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / PulseCursorWakePriority_t

# PulseCursorWakePriority_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** animationsystem

## Values

| Name | Value | Description |
|------|-------|-------------|
| `WakeElegantly` | 0 | Proceed Elegantly. — Request elegant wind-down of any associated work (e.g. vcd interrupt), then proceed afterwards. |
| `WakeImmediate` | 1 | Proceed Immediately. — Stop the node action without any wind-down, then proceed afterwards. |
