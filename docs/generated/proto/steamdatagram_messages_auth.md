---
layout: default
title: steamdatagram_messages_auth.proto
parent: Protobufs
nav_exclude: true
---

# `steamdatagram_messages_auth.proto`

**Imports:** `steamnetworkingsockets_messages_certs.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CMsgSteamDatagramRelayAuthTicket {
    +fixed32 time_expiry
    +string authorized_client_identity_string
    +string gameserver_identity_string
    +fixed32 authorized_public_ip
    +bytes gameserver_address
    +uint32 app_id
    +uint32 virtual_port
    +List~CMsgSteamDatagramRelayAuthTicket.ExtraField~ extra_fields
    +fixed64 legacy_authorized_steam_id
    +fixed64 legacy_gameserver_steam_id
    +fixed32 legacy_gameserver_pop_id
    +bytes legacy_authorized_client_identity_binary
    +bytes legacy_gameserver_identity_binary
  }

  class ExtraField {
    +string name
    +string string_value
    +sint64 int64_value
    +fixed64 fixed64_value
  }

  class CMsgSteamDatagramSignedRelayAuthTicket {
    +fixed64 reserved_do_not_use
    +bytes ticket
    +bytes signature
    +fixed64 key_id
    +List~CMsgSteamDatagramCertificateSigned~ certs
  }

  class CMsgSteamDatagramCachedCredentialsForApp {
    +bytes private_key
    +bytes cert
    +List~bytes~ relay_tickets
  }

  class CMsgSteamDatagramGameCoordinatorServerLogin {
    +uint32 time_generated
    +uint32 appid
    +bytes routing
    +bytes appdata
    +bytes legacy_identity_binary
    +string identity_string
    +fixed64 dummy_steam_id
  }

  class CMsgSteamDatagramSignedGameCoordinatorServerLogin {
    +CMsgSteamDatagramCertificateSigned cert
    +bytes login
    +bytes signature
  }

  class CMsgSteamDatagramHostedServerAddressPlaintext {
    +fixed32 ipv4
    +bytes ipv6
    +uint32 port
    +fixed64 routing_secret
    +uint32 protocol_version
  }

  CMsgSteamDatagramRelayAuthTicket --> ExtraField : extra_fields[]

```

## Messages

### `CMsgSteamDatagramRelayAuthTicket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `time_expiry` | 1 | fixed32 | optional |  |
| `legacy_authorized_steam_id` | 2 | fixed64 | optional |  |
| `authorized_public_ip` | 3 | fixed32 | optional |  |
| `legacy_gameserver_steam_id` | 4 | fixed64 | optional |  |
| `app_id` | 7 | uint32 | optional |  |
| `extra_fields` | 8 | CMsgSteamDatagramRelayAuthTicket.ExtraField | repeated |  |
| `legacy_gameserver_pop_id` | 9 | fixed32 | optional |  |
| `virtual_port` | 10 | uint32 | optional |  |
| `gameserver_address` | 11 | bytes | optional |  |
| `legacy_authorized_client_identity_binary` | 12 | bytes | optional |  |
| `legacy_gameserver_identity_binary` | 13 | bytes | optional |  |
| `authorized_client_identity_string` | 14 | string | optional |  |
| `gameserver_identity_string` | 15 | string | optional |  |

### `CMsgSteamDatagramSignedRelayAuthTicket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `reserved_do_not_use` | 1 | fixed64 | optional |  |
| `key_id` | 2 | fixed64 | optional |  |
| `ticket` | 3 | bytes | optional |  |
| `signature` | 4 | bytes | optional |  |
| `certs` | 5 | CMsgSteamDatagramCertificateSigned | repeated |  |

### `CMsgSteamDatagramCachedCredentialsForApp`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `private_key` | 1 | bytes | optional |  |
| `cert` | 2 | bytes | optional |  |
| `relay_tickets` | 3 | bytes | repeated |  |

### `CMsgSteamDatagramGameCoordinatorServerLogin`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `time_generated` | 1 | uint32 | optional |  |
| `appid` | 2 | uint32 | optional |  |
| `routing` | 3 | bytes | optional |  |
| `appdata` | 4 | bytes | optional |  |
| `legacy_identity_binary` | 5 | bytes | optional |  |
| `identity_string` | 6 | string | optional |  |
| `dummy_steam_id` | 99 | fixed64 | optional |  |

### `CMsgSteamDatagramSignedGameCoordinatorServerLogin`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `cert` | 1 | CMsgSteamDatagramCertificateSigned | optional |  |
| `login` | 2 | bytes | optional |  |
| `signature` | 3 | bytes | optional |  |

### `CMsgSteamDatagramHostedServerAddressPlaintext`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ipv4` | 1 | fixed32 | optional |  |
| `ipv6` | 2 | bytes | optional |  |
| `port` | 3 | uint32 | optional |  |
| `routing_secret` | 4 | fixed64 | optional |  |
| `protocol_version` | 5 | uint32 | optional |  |
