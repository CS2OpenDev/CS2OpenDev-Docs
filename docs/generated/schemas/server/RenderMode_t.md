---
layout: default
title: RenderMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / RenderMode_t

# RenderMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Transparency / rendering method for a model entity (m_nRenderMode).

**Kind:** enum · **Underlying:** `uint8_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `kRenderNormal` | 0 | Opaque, standard rendering. |
| `kRenderTransAlpha` | 1 | Alpha-blended translucency. |
| `kRenderNone` | 2 | Not rendered (invisible but still present). |
| `kRenderModeCount` | 3 |  |
