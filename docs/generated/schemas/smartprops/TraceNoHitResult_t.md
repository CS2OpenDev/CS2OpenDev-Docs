---
layout: default
title: TraceNoHitResult_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / TraceNoHitResult_t

# TraceNoHitResult_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `NOTHING` | 0 | Do nothing — If no surface it hit, don't update the transform at all, act as if the trace was not performed. |
| `DISCARD` | 1 | Stop evaluation — If no surface is hit stop evaluation of the current element, no following modifiers will be evaluated and the current transform will not be modified. |
| `MOVE_TO_START` | 2 | Move to start — If no surface is hit move the current transform to the start of the trace. |
| `MOVE_TO_END` | 3 | Move to end — If no surface is hit move the current transform to the end of the trace. |
