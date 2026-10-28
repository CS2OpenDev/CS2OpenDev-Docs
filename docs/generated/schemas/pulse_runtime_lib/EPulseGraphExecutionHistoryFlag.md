---
title: EPulseGraphExecutionHistoryFlag
module: pulse_runtime_lib
kind: enum
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / EPulseGraphExecutionHistoryFlag

# EPulseGraphExecutionHistoryFlag

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** pulse_runtime_lib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `NO_FLAGS` | 0 |  |
| `CURSOR_ADD_TAG` | 1 |  |
| `CURSOR_REMOVE_TAG` | 2 |  |
| `CURSOR_RETIRED` | 4 |  |
| `CURSOR_CREATE_CHILD` | 8 |  |
| `REQUIREMENT_PASS` | 16 |  |
| `REQUIREMENT_FAIL` | 32 |  |
| `CALL_TO_PULSE` | 64 |  |
| `RETURN` | 128 |  |
