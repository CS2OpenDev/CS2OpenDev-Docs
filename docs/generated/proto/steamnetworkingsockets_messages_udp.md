---
layout: default
title: steamnetworkingsockets_messages_udp.proto
parent: Protobufs
nav_exclude: true
---

# `steamnetworkingsockets_messages_udp.proto`

**Imports:** [`steamnetworkingsockets_messages_certs.proto`](steamnetworkingsockets_messages_certs.md), [`steamnetworkingsockets_messages.proto`](steamnetworkingsockets_messages.md)

## Diagram

```mermaid
classDiagram
direction LR

  class CMsgSteamSockets_UDP_ChallengeRequest {
    +fixed32 connection_id
    +fixed64 my_timestamp
    +uint32 protocol_version
  }

  class CMsgSteamSockets_UDP_ChallengeReply {
    +fixed32 connection_id
    +fixed64 challenge
    +fixed64 your_timestamp
    +uint32 protocol_version
  }

  class CMsgSteamSockets_UDP_ConnectRequest {
    +fixed32 client_connection_id
    +fixed64 challenge
    +fixed64 my_timestamp
    +uint32 ping_est_ms
    +CMsgSteamDatagramSessionCryptInfoSigned crypt
    +CMsgSteamDatagramCertificateSigned cert
    +uint32 legacy_protocol_version
    +string identity_string
    +fixed64 legacy_client_steam_id
    +CMsgSteamNetworkingIdentityLegacyBinary legacy_identity_binary
  }

  class CMsgSteamSockets_UDP_ConnectOK {
    +fixed32 client_connection_id
    +fixed32 server_connection_id
    +fixed64 your_timestamp
    +uint32 delay_time_usec
    +CMsgSteamDatagramSessionCryptInfoSigned crypt
    +CMsgSteamDatagramCertificateSigned cert
    +string identity_string
    +fixed64 legacy_server_steam_id
    +CMsgSteamNetworkingIdentityLegacyBinary legacy_identity_binary
  }

  class CMsgSteamSockets_UDP_ConnectionClosed {
    +fixed32 to_connection_id
    +fixed32 from_connection_id
    +string debug
    +uint32 reason_code
  }

  class CMsgSteamSockets_UDP_NoConnection {
    +fixed32 from_connection_id
    +fixed32 to_connection_id
  }

  class CMsgSteamSockets_UDP_Stats {
    +CMsgSteamDatagramConnectionQuality stats
    +uint32 flags
  }

  class ESteamNetworkingUDPMsgID{
    <<enumeration>>
    k_ESteamNetworkingUDPMsg_ChallengeRequest
    k_ESteamNetworkingUDPMsg_ChallengeReply
    k_ESteamNetworkingUDPMsg_ConnectRequest
    k_ESteamNetworkingUDPMsg_ConnectOK
    k_ESteamNetworkingUDPMsg_ConnectionClosed
    k_ESteamNetworkingUDPMsg_NoConnection
  }

  class CMsgSteamSockets_UDP_Stats_Flags["CMsgSteamSockets_UDP_Stats.Flags"]{
    <<enumeration>>
    ACK_REQUEST_E2E
    ACK_REQUEST_IMMEDIATE
    NOT_PRIMARY_TRANSPORT_E2E
  }

```

## Enums

### `ESteamNetworkingUDPMsgID`

| Name | Value |
|------|-------|
| `k_ESteamNetworkingUDPMsg_ChallengeRequest` | 32 |
| `k_ESteamNetworkingUDPMsg_ChallengeReply` | 33 |
| `k_ESteamNetworkingUDPMsg_ConnectRequest` | 34 |
| `k_ESteamNetworkingUDPMsg_ConnectOK` | 35 |
| `k_ESteamNetworkingUDPMsg_ConnectionClosed` | 36 |
| `k_ESteamNetworkingUDPMsg_NoConnection` | 37 |

## Messages

### `CMsgSteamSockets_UDP_ChallengeRequest`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `connection_id` | 1 | fixed32 | optional |  |
| `my_timestamp` | 3 | fixed64 | optional |  |
| `protocol_version` | 4 | uint32 | optional |  |

### `CMsgSteamSockets_UDP_ChallengeReply`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `connection_id` | 1 | fixed32 | optional |  |
| `challenge` | 2 | fixed64 | optional |  |
| `your_timestamp` | 3 | fixed64 | optional |  |
| `protocol_version` | 4 | uint32 | optional |  |

### `CMsgSteamSockets_UDP_ConnectRequest`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `client_connection_id` | 1 | fixed32 | optional |  |
| `challenge` | 2 | fixed64 | optional |  |
| `legacy_client_steam_id` | 3 | fixed64 | optional |  |
| `cert` | 4 | [CMsgSteamDatagramCertificateSigned](steamnetworkingsockets_messages_certs.md#cmsgsteamdatagramcertificatesigned) | optional |  |
| `my_timestamp` | 5 | fixed64 | optional |  |
| `ping_est_ms` | 6 | uint32 | optional |  |
| `crypt` | 7 | [CMsgSteamDatagramSessionCryptInfoSigned](steamnetworkingsockets_messages.md#cmsgsteamdatagramsessioncryptinfosigned) | optional |  |
| `legacy_protocol_version` | 8 | uint32 | optional |  |
| `legacy_identity_binary` | 9 | [CMsgSteamNetworkingIdentityLegacyBinary](steamnetworkingsockets_messages_certs.md#cmsgsteamnetworkingidentitylegacybinary) | optional |  |
| `identity_string` | 10 | string | optional |  |

### `CMsgSteamSockets_UDP_ConnectOK`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `client_connection_id` | 1 | fixed32 | optional |  |
| `legacy_server_steam_id` | 2 | fixed64 | optional |  |
| `your_timestamp` | 3 | fixed64 | optional |  |
| `delay_time_usec` | 4 | uint32 | optional |  |
| `server_connection_id` | 5 | fixed32 | optional |  |
| `crypt` | 7 | [CMsgSteamDatagramSessionCryptInfoSigned](steamnetworkingsockets_messages.md#cmsgsteamdatagramsessioncryptinfosigned) | optional |  |
| `cert` | 8 | [CMsgSteamDatagramCertificateSigned](steamnetworkingsockets_messages_certs.md#cmsgsteamdatagramcertificatesigned) | optional |  |
| `legacy_identity_binary` | 10 | [CMsgSteamNetworkingIdentityLegacyBinary](steamnetworkingsockets_messages_certs.md#cmsgsteamnetworkingidentitylegacybinary) | optional |  |
| `identity_string` | 11 | string | optional |  |

### `CMsgSteamSockets_UDP_ConnectionClosed`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `debug` | 2 | string | optional |  |
| `reason_code` | 3 | uint32 | optional |  |
| `to_connection_id` | 4 | fixed32 | optional |  |
| `from_connection_id` | 5 | fixed32 | optional |  |

### `CMsgSteamSockets_UDP_NoConnection`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `from_connection_id` | 2 | fixed32 | optional |  |
| `to_connection_id` | 3 | fixed32 | optional |  |

### `CMsgSteamSockets_UDP_Stats`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `stats` | 1 | [CMsgSteamDatagramConnectionQuality](steamnetworkingsockets_messages.md#cmsgsteamdatagramconnectionquality) | optional |  |
| `flags` | 3 | uint32 | optional |  |

#### `CMsgSteamSockets_UDP_Stats.Flags`

| Name | Value |
|------|-------|
| `ACK_REQUEST_E2E` | 2 |
| `ACK_REQUEST_IMMEDIATE` | 4 |
| `NOT_PRIMARY_TRANSPORT_E2E` | 16 |
