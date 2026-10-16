---
title: pet_gcmessages.proto
proto: pet_gcmessages.proto
---

# `pet_gcmessages.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CMsgAckPetEvent {
    +uint64 pet_item_id
  }

  class EGCPetMsg{
    <<enumeration>>
    k_EMsgGCAckPetEvent
  }

```

## Enums

### `EGCPetMsg`

| Name | Value |
|------|-------|
| `k_EMsgGCAckPetEvent` | 2538 |

## Messages

### `CMsgAckPetEvent`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `pet_item_id` | 1 | uint64 | optional |  |
