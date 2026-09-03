---
title: PulseCursorWakePriority_t
module: pulse_runtime_lib
kind: enum
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / PulseCursorWakePriority_t

# PulseCursorWakePriority_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** pulse_runtime_lib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `WakeElegantly` | 0 | Proceed Elegantly. — Request elegant wind-down of any associated work (e.g. vcd interrupt), then proceed afterwards. |
| `WakeImmediate` | 1 | Proceed Immediately. — Stop the node action without any wind-down, then proceed afterwards. |
