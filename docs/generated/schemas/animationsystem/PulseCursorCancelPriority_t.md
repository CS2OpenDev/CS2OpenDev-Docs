---
layout: default
title: PulseCursorCancelPriority_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / PulseCursorCancelPriority_t

# PulseCursorCancelPriority_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** animationsystem

## Values

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Keep running normally. |
| `CancelOnSucceeded` | 1 | Kill After. — Do not stop the current yielding node, but do not continue to the next node afterwards. |
| `SoftCancel` | 2 | Kill Elegantly. — Request elegant wind-down of any associated work (e.g. vcd interrupt). |
| `HardCancel` | 3 | Kill Immediately. — Stop without any wind-down. |
