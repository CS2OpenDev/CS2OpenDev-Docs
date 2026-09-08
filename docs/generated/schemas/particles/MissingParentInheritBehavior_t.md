---
title: MissingParentInheritBehavior_t
module: particles
kind: enum
---

[Schemas](../../schemas.md) / [particles](../particles.md) / MissingParentInheritBehavior_t

# MissingParentInheritBehavior_t

> Source: **Build 25175329** · 2026-09-07 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** particles

## Values

| Name | Value | Description |
|------|-------|-------------|
| `MISSING_PARENT_DO_NOTHING` | -1 (`0xffffffff`) | Do Nothing |
| `MISSING_PARENT_KILL` | 0 | Kill Particle |
| `MISSING_PARENT_FIND_NEW` | 1 | Use Next Parent Particle |
| `MISSING_PARENT_SAME_INDEX` | 2 | Use New Particle at Same Index if Possible |
