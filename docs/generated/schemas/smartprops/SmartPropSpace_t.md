---
layout: default
title: SmartPropSpace_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / SmartPropSpace_t

# SmartPropSpace_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `WORLD` | 0 | World space — World space transform, not relative to the specific smart prop object placement. |
| `OBJECT` | 1 | Object space — Object space transform, relative to the object placement, but does not include the current element transform. |
| `ELEMENT` | 2 | Element space — Element space transform, includes the transform of the current element, which is also relative to the object. |
