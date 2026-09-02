---
layout: default
title: ResponseFollowup
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / ResponseFollowup

# ResponseFollowup

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 49 bytes (`0x31`) · **Align:** n/a (unspecified) · **Module:** server

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `followup_concept` | char* |  |  |
| `0x8` | `followup_contexts` | char* |  |  |
| `0x10` | `followup_delay` | float32 |  |  |
| `0x14` | `followup_target` | char* |  |  |
| `0x1c` | `followup_entityiotarget` | char* |  |  |
| `0x24` | `followup_entityioinput` | char* |  |  |
| `0x2c` | `followup_entityiodelay` | float32 |  |  |
| `0x30` | `bFired` | bool |  |  |
