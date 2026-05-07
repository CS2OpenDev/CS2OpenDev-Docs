---
layout: default
title: engine_gcmessages.proto
parent: Protobufs
nav_exclude: true
---

# `engine_gcmessages.proto`

**Imports:** `google/protobuf/descriptor.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CEngineGotvSyncPacket {
    +uint64 match_id
    +uint32 instance_id
    +uint32 signupfragment
    +uint32 currentfragment
    +float tickrate
    +uint32 tick
    +float rtdelay
    +float rcvage
    +float keyframe_interval
    +uint32 cdndelay
  }

```

## Messages

### `CEngineGotvSyncPacket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `match_id` | 1 | uint64 | optional |  |
| `instance_id` | 2 | uint32 | optional |  |
| `signupfragment` | 3 | uint32 | optional |  |
| `currentfragment` | 4 | uint32 | optional |  |
| `tickrate` | 5 | float | optional |  |
| `tick` | 6 | uint32 | optional |  |
| `rtdelay` | 8 | float | optional |  |
| `rcvage` | 9 | float | optional |  |
| `keyframe_interval` | 10 | float | optional |  |
| `cdndelay` | 11 | uint32 | optional |  |
