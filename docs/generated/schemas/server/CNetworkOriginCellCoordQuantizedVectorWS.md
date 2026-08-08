---
layout: default
title: CNetworkOriginCellCoordQuantizedVectorWS
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CNetworkOriginCellCoordQuantizedVectorWS

# CNetworkOriginCellCoordQuantizedVectorWS

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 255 · **Module:** server

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
