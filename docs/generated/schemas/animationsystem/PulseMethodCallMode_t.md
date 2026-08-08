---
layout: default
title: PulseMethodCallMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / PulseMethodCallMode_t

# PulseMethodCallMode_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** animationsystem

## Values

| Name | Value | Description |
|------|-------|-------------|
| `SYNC_WAIT_FOR_COMPLETION` | 0 | Wait For Completion — Synchronous - Wait for this node to fully complete before proceeding. |
| `ASYNC_FIRE_AND_FORGET` | 1 | Proceed Immediately — Asynchronous - This node executes independently using a new Cursor. Formerly 'Fire and Forget'. Equivalent to scheduling using an additional 'Fire Child Cursors' node. |
