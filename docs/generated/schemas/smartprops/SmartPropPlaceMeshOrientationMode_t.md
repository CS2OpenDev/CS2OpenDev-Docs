---
title: SmartPropPlaceMeshOrientationMode_t
module: smartprops
kind: enum
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / SmartPropPlaceMeshOrientationMode_t

# SmartPropPlaceMeshOrientationMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `FIRST_OPEN_EDGE` | 0 | First Open Edge — Orientation of child elements placed on faces will be driven by position of center of first open edge relative to face center. |
| `FIRST_CLOSED_EDGE` | 1 | First Closed Edge — Orientation of child elements placed on faces will be driven by position of center of first closed edge relative to face center. |
| `UVMAP1` | 2 | UV Channel 1 — Orientation of child elements placed on faces will be driven by orthonormalized UV basis at face center. U axis is prioritized during orthonormalization. |
| `UVMAP2` | 3 | UV Channel 2 — Orientation of child elements placed on faces will be driven by orthonormalized UV basis at face center. U axis is prioritized during orthonormalization. |
