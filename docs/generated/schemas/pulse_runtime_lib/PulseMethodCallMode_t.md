---
layout: default
title: PulseMethodCallMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / PulseMethodCallMode_t

# PulseMethodCallMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** pulse_runtime_lib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `SYNC_WAIT_FOR_COMPLETION` | 0 | Wait For Completion — Synchronous - Wait for this node to fully complete before proceeding. |
| `ASYNC_FIRE_AND_FORGET` | 1 | Proceed Immediately — Asynchronous - This node executes independently using a new Cursor. Formerly 'Fire and Forget'. Equivalent to scheduling using an additional 'Fire Child Cursors' node. |
