---
title: networksystem_protomessages.proto
proto: networksystem_protomessages.proto
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

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `slot` | 1 | uint32 | optional |  |

### `NetMessageConnectionClosed`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `reason` | 1 | uint32 | optional |  |
| `message` | 2 | string | optional |  |

### `NetMessageConnectionCrashed`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `reason` | 1 | uint32 | optional |  |
| `message` | 2 | string | optional |  |

### `NetMessagePacketStart`

*(no fields)*

### `NetMessagePacketEnd`

*(no fields)*
