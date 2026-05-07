---
layout: default
title: steammessages_helprequest.steamworkssdk.proto
parent: Protobufs
nav_exclude: true
---

# `steammessages_helprequest.steamworkssdk.proto`

**Imports:** `steammessages_unified_base.steamworkssdk.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CHelpRequestLogs_UploadUserApplicationLog_Request {
    +uint32 appid
    +string log_type
    +string version_string
    +string log_contents
  }

  class CHelpRequestLogs_UploadUserApplicationLog_Response {
    +uint64 id
  }

```

## Messages

### `CHelpRequestLogs_UploadUserApplicationLog_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `log_type` | 2 | string | optional |  |
| `version_string` | 3 | string | optional |  |
| `log_contents` | 4 | string | optional |  |

### `CHelpRequestLogs_UploadUserApplicationLog_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `id` | 1 | uint64 | optional |  |
