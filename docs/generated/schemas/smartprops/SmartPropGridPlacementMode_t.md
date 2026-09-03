---
title: SmartPropGridPlacementMode_t
module: smartprops
kind: enum
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / SmartPropGridPlacementMode_t

# SmartPropGridPlacementMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `SEGMENT` | 0 | Array — Generate the grid by placing N x N children. |
| `FILL` | 1 | Fill — Fill the area based on the largest bounds of child elements as specified in their selection criteria. |
