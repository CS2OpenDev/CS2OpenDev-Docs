---
title: CHintMessageQueue
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CHintMessageQueue

# CHintMessageQueue

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** n/a (unspecified) · **Module:** server

**Relationships:**

```mermaid
classDiagram
    CHintMessageQueue --> CHintMessage
    CHintMessageQueue --> CBasePlayerController
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_tmMessageEnd` | float32 |  |  |
| `0x8` | `m_messages` | CUtlVector< [CHintMessage](../server/CHintMessage.md)* > |  |  |
| `0x20` | `m_pPlayerController` | [CBasePlayerController](../server/CBasePlayerController.md)* |  |  |
