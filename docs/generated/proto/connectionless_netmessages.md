---
layout: default
title: connectionless_netmessages.proto
parent: Protobufs
nav_exclude: true
---

# `connectionless_netmessages.proto`

**Imports:** `netmessages.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class C2S_CONNECT_SameProcessCheck {
    +uint64 localhost_process_id
    +uint64 key
  }

  class C2S_CONNECT_Message {
    +uint32 host_version
    +uint32 auth_protocol
    +uint32 challenge_number
    +fixed64 reservation_cookie
    +bool low_violence
    +bytes encrypted_password
    +List~CCLCMsg_SplitPlayerConnect~ splitplayers
    +bytes auth_steam
    +string challenge_context
    +C2S_CONNECT_SameProcessCheck localhost_same_process_check
  }

  class C2S_CONNECTION_Message {
    +string addon_name
    +C2S_CONNECT_SameProcessCheck localhost_same_process_check
  }

  C2S_CONNECT_Message --> C2S_CONNECT_SameProcessCheck : localhost_same_process_check
  C2S_CONNECTION_Message --> C2S_CONNECT_SameProcessCheck : localhost_same_process_check

```

## Messages

### `C2S_CONNECT_SameProcessCheck`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `localhost_process_id` | 1 | uint64 | optional |  |
| `key` | 2 | uint64 | optional |  |

### `C2S_CONNECT_Message`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `host_version` | 1 | uint32 | optional |  |
| `auth_protocol` | 2 | uint32 | optional |  |
| `challenge_number` | 3 | uint32 | optional |  |
| `reservation_cookie` | 4 | fixed64 | optional |  |
| `low_violence` | 5 | bool | optional |  |
| `encrypted_password` | 6 | bytes | optional |  |
| `splitplayers` | 7 | CCLCMsg_SplitPlayerConnect | repeated |  |
| `auth_steam` | 8 | bytes | optional |  |
| `challenge_context` | 9 | string | optional |  |
| `localhost_same_process_check` | 10 | [C2S_CONNECT_SameProcessCheck](#c2s_connect_sameprocesscheck) | optional |  |

### `C2S_CONNECTION_Message`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `addon_name` | 1 | string | optional |  |
| `localhost_same_process_check` | 2 | [C2S_CONNECT_SameProcessCheck](#c2s_connect_sameprocesscheck) | optional |  |
