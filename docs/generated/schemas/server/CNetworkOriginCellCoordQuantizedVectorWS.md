---
title: CNetworkOriginCellCoordQuantizedVectorWS
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CNetworkOriginCellCoordQuantizedVectorWS

# CNetworkOriginCellCoordQuantizedVectorWS

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** n/a (unspecified) · **Module:** server

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_cellX` | uint16 |  |  |
| `0x12` | `m_cellY` | uint16 |  |  |
| `0x14` | `m_cellZ` | uint16 |  |  |
| `0x16` | `m_nOutsideWorld` | uint16 |  |  |
| `0x18` | `m_vecX` | CNetworkedQuantizedFloat |  |  |
| `0x20` | `m_vecY` | CNetworkedQuantizedFloat |  |  |
| `0x28` | `m_vecZ` | CNetworkedQuantizedFloat |  |  |
