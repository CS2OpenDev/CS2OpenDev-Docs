---
layout: default
title: valveextensions.proto
parent: Protobufs
nav_exclude: true
---

# `valveextensions.proto`

**Imports:** `google/protobuf/descriptor.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class EProtoDebugVisiblity{
    <<enumeration>>
    k_EProtoDebugVisibility_Always
    k_EProtoDebugVisibility_Server
    k_EProtoDebugVisibility_ValveServer
    k_EProtoDebugVisibility_GC
    k_EProtoDebugVisibility_Never
  }

```

## Enums

### `EProtoDebugVisiblity`

| Name | Value |
|------|-------|
| `k_EProtoDebugVisibility_Always` | 0 |
| `k_EProtoDebugVisibility_Server` | 70 |
| `k_EProtoDebugVisibility_ValveServer` | 80 |
| `k_EProtoDebugVisibility_GC` | 90 |
| `k_EProtoDebugVisibility_Never` | 100 |
