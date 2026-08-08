---
layout: default
title: PickMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / PickMode_t

# PickMode_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `LARGEST_FIRST` | 0 | Largest fitting — Pick the largest child element that will fit in the remaining length of the line, repeat this process until the line is full or no child will fit in the remaining length. |
| `RANDOM` | 1 | Random fitting — Pick a random choice from the child elements that will fit within the remaining length, repeat this process until the line is full or no child will fit in the remaining length. |
| `ALL_IN_ORDER` | 2 | Place all in order — Place all of the child elements in the order they are specified even if they do not fit the line or do not fill the line. NOTE: end cap settings are ignored in this mode. |
