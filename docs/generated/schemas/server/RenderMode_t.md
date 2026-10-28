---
title: RenderMode_t
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / RenderMode_t

# RenderMode_t

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

Transparency / rendering method for a model entity (m_nRenderMode).

**Kind:** enum · **Underlying:** `uint8_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `kRenderNormal` | 0 | Opaque, standard rendering. |
| `kRenderTransAlpha` | 1 | Alpha-blended translucency. |
| `kRenderNone` | 2 | Not rendered (invisible but still present). |
| `kRenderModeCount` | 3 |  |
