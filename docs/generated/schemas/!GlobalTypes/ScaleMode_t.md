---
layout: default
title: ScaleMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / ScaleMode_t

# ScaleMode_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `NONE` | 0 | No scaling — Do not allow selected elements to be scaled, the parts may not fit the line exactly |
| `SCALE_END_TO_FIT` | 1 | Scale last — Apply scale to the last element in order to fit the line. Only proceed to scale additional elements if the scale range of the last element is not sufficient. |
| `SCALE_EQUALLY` | 2 | Scale equally — Attempt to apply the same amount of scale to all of the elements placed on the line while still respecting their size constraints. |
| `SCALE_MAXIMIZE` | 3 | Maximize scale — Each element will be scaled to is maximum allowable size that will still fit on the line. |
