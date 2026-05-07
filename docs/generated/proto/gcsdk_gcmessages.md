---
layout: default
title: gcsdk_gcmessages.proto
parent: Protobufs
nav_exclude: true
---

# `gcsdk_gcmessages.proto`

**Imports:** `steammessages.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CMsgSOIDOwner {
    +uint32 type
    +uint64 id
  }

  class CMsgSOSingleObject {
    +int32 type_id
    +bytes object_data
    +fixed64 version
    +CMsgSOIDOwner owner_soid
  }

  class CMsgSOMultipleObjects {
    +List~CMsgSOMultipleObjects.SingleObject~ objects_modified
    +fixed64 version
    +CMsgSOIDOwner owner_soid
  }

  class SingleObject {
    +int32 type_id
    +bytes object_data
  }

  class CMsgSOCacheSubscribed {
    +List~CMsgSOCacheSubscribed.SubscribedType~ objects
    +fixed64 version
    +CMsgSOIDOwner owner_soid
  }

  class SubscribedType {
    +int32 type_id
    +List~bytes~ object_data
  }

  class CMsgSOCacheUnsubscribed {
    +CMsgSOIDOwner owner_soid
  }

  class CMsgSOCacheSubscriptionCheck {
    +fixed64 version
    +CMsgSOIDOwner owner_soid
  }

  class CMsgSOCacheSubscriptionRefresh {
    +CMsgSOIDOwner owner_soid
  }

  class CMsgSOCacheVersion {
    +fixed64 version
  }

  class CMsgAccountDetails {
    +bool valid
    +string account_name
    +bool public_profile
    +bool public_inventory
    +bool vac_banned
    +bool cyber_cafe
    +bool school_account
    +bool free_trial_account
    +bool subscribed
    +bool low_violence
    +bool limited
    +bool trusted
    +uint32 package
    +fixed32 time_cached
    +bool account_locked
    +bool community_banned
    +bool trade_banned
    +bool eligible_for_community_market
  }

  class CMsgGCMultiplexMessage {
    +uint32 msgtype
    +bytes payload
    +List~fixed64~ steamids
    +bool replytogc
  }

  class CMsgGCMultiplexMessage_Response {
    +uint32 msgtype
  }

  class CGCToGCMsgMasterAck {
    +uint32 dir_index
    +uint32 gc_type
  }

  class CGCToGCMsgMasterAck_Response {
    +int32 eresult
  }

  class CGCToGCMsgMasterStartupComplete {
  }

  class CGCToGCMsgRouted {
    +uint32 msg_type
    +fixed64 sender_id
    +bytes net_message
    +uint32 ip
  }

  class CGCToGCMsgRoutedReply {
    +uint32 msg_type
    +bytes net_message
  }

  class CMsgGCUpdateSessionIP {
    +fixed64 steamid
    +fixed32 ip
  }

  class CMsgGCRequestSessionIP {
    +fixed64 steamid
  }

  class CMsgGCRequestSessionIPResponse {
    +fixed32 ip
  }

  class CMsgSOCacheHaveVersion {
    +CMsgSOIDOwner soid
    +fixed64 version
  }

  class CMsgClientHello {
    +uint32 version
    +List~CMsgSOCacheHaveVersion~ socache_have_versions
    +uint32 client_session_need
    +uint32 client_launcher
    +uint32 partner_srcid
    +uint32 partner_accountid
    +uint32 partner_accountflags
    +uint32 partner_accountbalance
    +uint32 steam_launcher
  }

  class CMsgServerHello {
    +uint32 version
    +List~CMsgSOCacheHaveVersion~ socache_have_versions
    +uint32 legacy_client_session_need
    +uint32 client_launcher
    +bytes legacy_steamdatagram_routing
    +uint32 required_internal_addr
    +bytes steamdatagram_login
    +uint32 socache_control
  }

  class CMsgClientWelcome {
    +uint32 version
    +bytes game_data
    +List~CMsgSOCacheSubscribed~ outofdate_subscribed_caches
    +List~CMsgSOCacheSubscriptionCheck~ uptodate_subscribed_caches
    +CMsgClientWelcome.Location location
    +bytes game_data2
    +uint32 rtime32_gc_welcome_timestamp
    +uint32 currency
    +uint32 balance
    +string balance_url
    +string txn_country_code
  }

  class Location {
    +float latitude
    +float longitude
    +string country
  }

  class CMsgConnectionStatus {
    +GCConnectionStatus status
    +uint32 client_session_need
    +int32 queue_position
    +int32 queue_size
    +int32 wait_seconds
    +int32 estimated_wait_seconds_remaining
  }

  class CWorkshop_PopulateItemDescriptions_Request {
    +uint32 appid
    +List~CWorkshop_PopulateItemDescriptions_Request.ItemDescriptionsLanguageBlock~ languages
  }

  class SingleItemDescription {
    +uint32 gameitemid
    +string item_description
    +bool one_per_account
  }

  class ItemDescriptionsLanguageBlock {
    +string language
    +List~CWorkshop_PopulateItemDescriptions_Request.SingleItemDescription~ descriptions
  }

  class CWorkshop_GetContributors_Request {
    +uint32 appid
    +uint32 gameitemid
  }

  class CWorkshop_GetContributors_Response {
    +List~fixed64~ contributors
  }

  class CWorkshop_SetItemPaymentRules_Request {
    +uint32 appid
    +uint32 gameitemid
    +List~CWorkshop_SetItemPaymentRules_Request.WorkshopItemPaymentRule~ associated_workshop_files
    +List~CWorkshop_SetItemPaymentRules_Request.PartnerItemPaymentRule~ partner_accounts
    +bool validate_only
    +bool make_workshop_files_subscribable
    +CWorkshop_SetItemPaymentRules_Request.WorkshopDirectPaymentRule associated_workshop_file_for_direct_payments
  }

  class WorkshopItemPaymentRule {
    +uint64 workshop_file_id
    +float revenue_percentage
    +string rule_description
    +uint32 rule_type
  }

  class WorkshopDirectPaymentRule {
    +uint64 workshop_file_id
    +string rule_description
  }

  class PartnerItemPaymentRule {
    +uint32 account_id
    +float revenue_percentage
    +string rule_description
  }

  class CWorkshop_SetItemPaymentRules_Response {
  }

  class CGameServers_AggregationQuery_Request {
    +string filter
    +List~string~ group_fields
  }

  class CGameServers_AggregationQuery_Response {
    +List~CGameServers_AggregationQuery_Response.Group~ groups
  }

  class Group {
    +List~string~ group_values
    +uint32 servers_empty
    +uint32 servers_full
    +uint32 servers_total
    +uint32 players_humans
    +uint32 players_bots
    +uint32 player_capacity
  }

  class CWorkshop_AddSpecialPayment_Request {
    +uint32 appid
    +uint32 gameitemid
    +string date
    +uint64 payment_us_usd
    +uint64 payment_row_usd
  }

  class CWorkshop_AddSpecialPayment_Response {
  }

  class CProductInfo_SetRichPresenceLocalization_Request {
    +uint32 appid
    +List~CProductInfo_SetRichPresenceLocalization_Request.LanguageSection~ languages
    +uint64 steamid
  }

  class Token {
    +string token
    +string value
  }

  class LanguageSection {
    +string language
    +List~CProductInfo_SetRichPresenceLocalization_Request.Token~ tokens
  }

  class CProductInfo_SetRichPresenceLocalization_Response {
  }

  class CMsgSerializedSOCache {
    +uint32 file_version
    +List~CMsgSerializedSOCache.Cache~ caches
    +uint32 gc_socache_file_version
  }

  class TypeCache {
    +uint32 type
    +List~bytes~ objects
    +uint32 service_id
  }

  class Cache {
    +uint32 type
    +uint64 id
    +List~CMsgSerializedSOCache.Cache.Version~ versions
    +List~CMsgSerializedSOCache.TypeCache~ type_caches
  }

  class Version {
    +uint32 service
    +uint64 version
  }

  CMsgSOSingleObject --> CMsgSOIDOwner : owner_soid
  CMsgSOMultipleObjects --> SingleObject : objects_modified[]
  CMsgSOMultipleObjects --> CMsgSOIDOwner : owner_soid
  CMsgSOCacheSubscribed --> SubscribedType : objects[]
  CMsgSOCacheSubscribed --> CMsgSOIDOwner : owner_soid
  CMsgSOCacheUnsubscribed --> CMsgSOIDOwner : owner_soid
  CMsgSOCacheSubscriptionCheck --> CMsgSOIDOwner : owner_soid
  CMsgSOCacheSubscriptionRefresh --> CMsgSOIDOwner : owner_soid
  CMsgSOCacheHaveVersion --> CMsgSOIDOwner : soid
  CMsgClientHello --> CMsgSOCacheHaveVersion : socache_have_versions[]
  CMsgServerHello --> CMsgSOCacheHaveVersion : socache_have_versions[]
  CMsgClientWelcome --> CMsgSOCacheSubscribed : outofdate_subscribed_caches[]
  CMsgClientWelcome --> CMsgSOCacheSubscriptionCheck : uptodate_subscribed_caches[]
  CMsgClientWelcome --> Location : location
  CMsgConnectionStatus --> GCConnectionStatus : status
  CWorkshop_PopulateItemDescriptions_Request --> ItemDescriptionsLanguageBlock : languages[]
  ItemDescriptionsLanguageBlock --> SingleItemDescription : descriptions[]
  CWorkshop_SetItemPaymentRules_Request --> WorkshopItemPaymentRule : associated_workshop_files[]
  CWorkshop_SetItemPaymentRules_Request --> PartnerItemPaymentRule : partner_accounts[]
  CWorkshop_SetItemPaymentRules_Request --> WorkshopDirectPaymentRule : associated_workshop_file_for_direct_payments
  CGameServers_AggregationQuery_Response --> Group : groups[]
  CProductInfo_SetRichPresenceLocalization_Request --> LanguageSection : languages[]
  LanguageSection --> Token : tokens[]
  CMsgSerializedSOCache --> Cache : caches[]
  Cache --> Version : versions[]
  Cache --> TypeCache : type_caches[]

  class GCClientLauncherType{
    <<enumeration>>
    GCClientLauncherType_DEFAULT
    GCClientLauncherType_PERFECTWORLD
    GCClientLauncherType_STEAMCHINA
    GCClientLauncherType_SOURCE2
  }

  class GCConnectionStatus{
    <<enumeration>>
    GCConnectionStatus_HAVE_SESSION
    GCConnectionStatus_GC_GOING_DOWN
    GCConnectionStatus_NO_SESSION
    GCConnectionStatus_NO_SESSION_IN_LOGON_QUEUE
    GCConnectionStatus_NO_STEAM
  }

```

## Enums

### `GCClientLauncherType`

| Name | Value |
|------|-------|
| `GCClientLauncherType_DEFAULT` | 0 |
| `GCClientLauncherType_PERFECTWORLD` | 1 |
| `GCClientLauncherType_STEAMCHINA` | 2 |
| `GCClientLauncherType_SOURCE2` | 3 |

### `GCConnectionStatus`

| Name | Value |
|------|-------|
| `GCConnectionStatus_HAVE_SESSION` | 0 |
| `GCConnectionStatus_GC_GOING_DOWN` | 1 |
| `GCConnectionStatus_NO_SESSION` | 2 |
| `GCConnectionStatus_NO_SESSION_IN_LOGON_QUEUE` | 3 |
| `GCConnectionStatus_NO_STEAM` | 4 |

## Messages

### `CMsgSOIDOwner`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `type` | 1 | uint32 | optional |  |
| `id` | 2 | uint64 | optional |  |

### `CMsgSOSingleObject`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `type_id` | 2 | int32 | optional |  |
| `object_data` | 3 | bytes | optional |  |
| `version` | 4 | fixed64 | optional |  |
| `owner_soid` | 5 | [CMsgSOIDOwner](#cmsgsoidowner) | optional |  |

### `CMsgSOMultipleObjects`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `objects_modified` | 2 | CMsgSOMultipleObjects.SingleObject | repeated |  |
| `version` | 3 | fixed64 | optional |  |
| `owner_soid` | 6 | [CMsgSOIDOwner](#cmsgsoidowner) | optional |  |

### `CMsgSOCacheSubscribed`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `objects` | 2 | CMsgSOCacheSubscribed.SubscribedType | repeated |  |
| `version` | 3 | fixed64 | optional |  |
| `owner_soid` | 4 | [CMsgSOIDOwner](#cmsgsoidowner) | optional |  |

### `CMsgSOCacheUnsubscribed`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `owner_soid` | 2 | [CMsgSOIDOwner](#cmsgsoidowner) | optional |  |

### `CMsgSOCacheSubscriptionCheck`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 2 | fixed64 | optional |  |
| `owner_soid` | 3 | [CMsgSOIDOwner](#cmsgsoidowner) | optional |  |

### `CMsgSOCacheSubscriptionRefresh`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `owner_soid` | 2 | [CMsgSOIDOwner](#cmsgsoidowner) | optional |  |

### `CMsgSOCacheVersion`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 1 | fixed64 | optional |  |

### `CMsgAccountDetails`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `valid` | 1 | bool | optional |  |
| `account_name` | 2 | string | optional |  |
| `public_profile` | 4 | bool | optional |  |
| `public_inventory` | 5 | bool | optional |  |
| `vac_banned` | 6 | bool | optional |  |
| `cyber_cafe` | 7 | bool | optional |  |
| `school_account` | 8 | bool | optional |  |
| `free_trial_account` | 9 | bool | optional |  |
| `subscribed` | 10 | bool | optional |  |
| `low_violence` | 11 | bool | optional |  |
| `limited` | 12 | bool | optional |  |
| `trusted` | 13 | bool | optional |  |
| `package` | 14 | uint32 | optional |  |
| `time_cached` | 15 | fixed32 | optional |  |
| `account_locked` | 16 | bool | optional |  |
| `community_banned` | 17 | bool | optional |  |
| `trade_banned` | 18 | bool | optional |  |
| `eligible_for_community_market` | 19 | bool | optional |  |

### `CMsgGCMultiplexMessage`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `msgtype` | 1 | uint32 | optional |  |
| `payload` | 2 | bytes | optional |  |
| `steamids` | 3 | fixed64 | repeated |  |
| `replytogc` | 4 | bool | optional |  |

### `CMsgGCMultiplexMessage_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `msgtype` | 1 | uint32 | optional |  |

### `CGCToGCMsgMasterAck`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `dir_index` | 1 | uint32 | optional |  |
| `gc_type` | 2 | uint32 | optional |  |

### `CGCToGCMsgMasterAck_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `eresult` | 1 | int32 | optional | *(default: `2`)* |

### `CGCToGCMsgMasterStartupComplete`

### `CGCToGCMsgRouted`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `msg_type` | 1 | uint32 | optional |  |
| `sender_id` | 2 | fixed64 | optional |  |
| `net_message` | 3 | bytes | optional |  |
| `ip` | 4 | uint32 | optional |  |

### `CGCToGCMsgRoutedReply`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `msg_type` | 1 | uint32 | optional |  |
| `net_message` | 2 | bytes | optional |  |

### `CMsgGCUpdateSessionIP`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `steamid` | 1 | fixed64 | optional |  |
| `ip` | 2 | fixed32 | optional |  |

### `CMsgGCRequestSessionIP`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `steamid` | 1 | fixed64 | optional |  |

### `CMsgGCRequestSessionIPResponse`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ip` | 1 | fixed32 | optional |  |

### `CMsgSOCacheHaveVersion`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `soid` | 1 | [CMsgSOIDOwner](#cmsgsoidowner) | optional |  |
| `version` | 2 | fixed64 | optional |  |

### `CMsgClientHello`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 1 | uint32 | optional |  |
| `socache_have_versions` | 2 | [CMsgSOCacheHaveVersion](#cmsgsocachehaveversion) | repeated |  |
| `client_session_need` | 3 | uint32 | optional |  |
| `client_launcher` | 4 | uint32 | optional |  |
| `partner_srcid` | 5 | uint32 | optional |  |
| `partner_accountid` | 6 | uint32 | optional |  |
| `partner_accountflags` | 7 | uint32 | optional |  |
| `partner_accountbalance` | 8 | uint32 | optional |  |
| `steam_launcher` | 9 | uint32 | optional |  |

### `CMsgServerHello`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 1 | uint32 | optional |  |
| `socache_have_versions` | 2 | [CMsgSOCacheHaveVersion](#cmsgsocachehaveversion) | repeated |  |
| `legacy_client_session_need` | 3 | uint32 | optional |  |
| `client_launcher` | 4 | uint32 | optional |  |
| `legacy_steamdatagram_routing` | 6 | bytes | optional |  |
| `required_internal_addr` | 7 | uint32 | optional |  |
| `steamdatagram_login` | 8 | bytes | optional |  |
| `socache_control` | 9 | uint32 | optional |  |

### `CMsgClientWelcome`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 1 | uint32 | optional |  |
| `game_data` | 2 | bytes | optional |  |
| `outofdate_subscribed_caches` | 3 | [CMsgSOCacheSubscribed](#cmsgsocachesubscribed) | repeated |  |
| `uptodate_subscribed_caches` | 4 | [CMsgSOCacheSubscriptionCheck](#cmsgsocachesubscriptioncheck) | repeated |  |
| `location` | 5 | CMsgClientWelcome.Location | optional |  |
| `game_data2` | 6 | bytes | optional |  |
| `rtime32_gc_welcome_timestamp` | 7 | uint32 | optional |  |
| `currency` | 8 | uint32 | optional |  |
| `balance` | 9 | uint32 | optional |  |
| `balance_url` | 10 | string | optional |  |
| `txn_country_code` | 11 | string | optional |  |

### `CMsgConnectionStatus`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `status` | 1 | [GCConnectionStatus](#gcconnectionstatus) | optional | *(default: `GCConnectionStatus_HAVE_SESSION`)* |
| `client_session_need` | 2 | uint32 | optional |  |
| `queue_position` | 3 | int32 | optional |  |
| `queue_size` | 4 | int32 | optional |  |
| `wait_seconds` | 5 | int32 | optional |  |
| `estimated_wait_seconds_remaining` | 6 | int32 | optional |  |

### `CWorkshop_PopulateItemDescriptions_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `languages` | 2 | CWorkshop_PopulateItemDescriptions_Request.ItemDescriptionsLanguageBlock | repeated |  |

### `CWorkshop_GetContributors_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `gameitemid` | 2 | uint32 | optional |  |

### `CWorkshop_GetContributors_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `contributors` | 1 | fixed64 | repeated |  |

### `CWorkshop_SetItemPaymentRules_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `gameitemid` | 2 | uint32 | optional |  |
| `associated_workshop_files` | 3 | CWorkshop_SetItemPaymentRules_Request.WorkshopItemPaymentRule | repeated |  |
| `partner_accounts` | 4 | CWorkshop_SetItemPaymentRules_Request.PartnerItemPaymentRule | repeated |  |
| `validate_only` | 5 | bool | optional |  |
| `make_workshop_files_subscribable` | 6 | bool | optional |  |
| `associated_workshop_file_for_direct_payments` | 7 | CWorkshop_SetItemPaymentRules_Request.WorkshopDirectPaymentRule | optional |  |

### `CWorkshop_SetItemPaymentRules_Response`

### `CGameServers_AggregationQuery_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `filter` | 1 | string | optional |  |
| `group_fields` | 3 | string | repeated |  |

### `CGameServers_AggregationQuery_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `groups` | 1 | CGameServers_AggregationQuery_Response.Group | repeated |  |

### `CWorkshop_AddSpecialPayment_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `gameitemid` | 2 | uint32 | optional |  |
| `date` | 3 | string | optional |  |
| `payment_us_usd` | 4 | uint64 | optional |  |
| `payment_row_usd` | 5 | uint64 | optional |  |

### `CWorkshop_AddSpecialPayment_Response`

### `CProductInfo_SetRichPresenceLocalization_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `languages` | 2 | CProductInfo_SetRichPresenceLocalization_Request.LanguageSection | repeated |  |
| `steamid` | 3 | uint64 | optional |  |

### `CProductInfo_SetRichPresenceLocalization_Response`

### `CMsgSerializedSOCache`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `file_version` | 1 | uint32 | optional |  |
| `caches` | 2 | CMsgSerializedSOCache.Cache | repeated |  |
| `gc_socache_file_version` | 3 | uint32 | optional |  |
