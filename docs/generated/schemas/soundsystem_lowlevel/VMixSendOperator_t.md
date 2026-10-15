---
title: VMixSendOperator_t
module: soundsystem_lowlevel
kind: enum
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixSendOperator_t

# VMixSendOperator_t

> Source: **Build 25947352** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** enum · **Underlying:** `uint16_t` · **Module:** soundsystem_lowlevel

## Values

| Name | Value | Description |
|------|-------|-------------|
| `NO_VOICES` | -1 (`0xffff`) |  |
| `ALL_VOICES` | 0 | All |
| `ROOM_VOICES` | 1 | Room Voices |
| `FACING_VOICES` | 2 | Facing Voices |
| `MIXGROUP_VOICES` | 3 | By Mixgroup |
| `NAMED_SEND` | 4 | By Named Send |
| `INVERSE_NAMED_SENDS` | 5 | 1 - (Sum of Named Sends) |
| `INVERSE_TOTAL_SEND` | 6 | 1 - (Sum of all sends) |
| `ALL_MAX_SEND` | 7 | All Voices with max Send Value |
| `TRACK` | 8 | Send To Track |
