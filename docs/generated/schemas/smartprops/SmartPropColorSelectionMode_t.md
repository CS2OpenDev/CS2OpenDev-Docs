---
layout: default
title: SmartPropColorSelectionMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / SmartPropColorSelectionMode_t

# SmartPropColorSelectionMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `SPECIFIC_COLOR` | 0 | Specific Color — Specify a specific color value (may be linked to a variable |
| `GRADIENT_RANDOM` | 1 | Gradient Random — Pick a random color from anywhere on the authored color gradient |
| `GRADIENT_RANDOM_STOP` | 2 | Gradient Random Stop — Randomly select one of the color stops specified on the gradient. Never picks a value between stops. |
| `GRADIENT_LOCATION` | 3 | Gradient Specific Value — Use a color value from a specified location on the gradient |
