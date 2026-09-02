---
title: ApplyColorMode_t
module: smartprops
kind: enum
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / ApplyColorMode_t

# ApplyColorMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `MULTIPLY_OBJECT` | 0 | Multiply object tint — Multiply with the object level color tint and replace the current color value. |
| `MULTIPLY_CURRENT` | 1 | Multiply current tint — Multiply with the current color tint value. |
| `REPLACE` | 2 | Replace tint — Replace the current color tint value completely, overwriting any object level tint. |
