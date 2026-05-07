---
layout: default
title: networksystem_protomessages.proto
parent: Protobufs
nav_exclude: true
---

# `networksystem_protomessages.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class NetMessageSplitscreenUserChanged {
    +uint32 slot
  }

  class NetMessageConnectionClosed {
    +uint32 reason
    +string message
  }

  class NetMessageConnectionCrashed {
    +uint32 reason
    +string message
  }

  class NetMessagePacketStart {
  }

  class NetMessagePacketEnd {
  }

```

## Messages

### `NetMessageSplitscreenUserChanged`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `slot` | 1 | uint32 | optional |  |

### `NetMessageConnectionClosed`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `reason` | 1 | uint32 | optional |  |
| `message` | 2 | string | optional |  |

### `NetMessageConnectionCrashed`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `reason` | 1 | uint32 | optional |  |
| `message` | 2 | string | optional |  |

### `NetMessagePacketStart`

### `NetMessagePacketEnd`
