---
title: CCSCustomHudLayoutState (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSCustomHudLayoutState

# CCSCustomHudLayoutState

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 408 bytes (`0x198`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CCSCustomHudLayoutState (client)](../client/CCSCustomHudLayoutState.md)

**Relationships:**

```mermaid
classDiagram
    CCSCustomHudLayoutState *-- HUDPanelHasClass_t
    CCSCustomHudLayoutState *-- HUDPanelDialogVariableString_t
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x30` | `m_playerSlot` | CPlayerSlot |  |  |
| `0x34` | `m_bInputCaptureEnabled` | bool |  |  |
| `0x38` | `m_vecHasClasses` | CNetworkUtlVectorBase< [HUDPanelHasClass_t](../server/HUDPanelHasClass_t.md) > |  |  |
| `0x98` | `m_vecDialogVariableStrings` | CNetworkUtlVectorBase< [HUDPanelDialogVariableString_t](../server/HUDPanelDialogVariableString_t.md) > |  |  |
