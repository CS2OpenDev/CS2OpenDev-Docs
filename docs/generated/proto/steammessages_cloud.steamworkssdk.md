---
layout: default
title: steammessages_cloud.steamworkssdk.proto
parent: Protobufs
nav_exclude: true
---

# `steammessages_cloud.steamworkssdk.proto`

**Imports:** `steammessages_unified_base.steamworkssdk.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CCloud_GetUploadServerInfo_Request {
    +uint32 appid
  }

  class CCloud_GetUploadServerInfo_Response {
    +string server_url
  }

  class CCloud_GetFileDetails_Request {
    +uint64 ugcid
    +uint32 appid
  }

  class CCloud_UserFile {
    +uint32 appid
    +uint64 ugcid
    +string filename
    +uint64 timestamp
    +uint32 file_size
    +string url
    +fixed64 steamid_creator
  }

  class CCloud_GetFileDetails_Response {
    +CCloud_UserFile details
  }

  class CCloud_EnumerateUserFiles_Request {
    +uint32 appid
    +bool extended_details
    +uint32 count
    +uint32 start_index
  }

  class CCloud_EnumerateUserFiles_Response {
    +List~CCloud_UserFile~ files
    +uint32 total_files
  }

  class CCloud_Delete_Request {
    +string filename
    +uint32 appid
  }

  class CCloud_Delete_Response {
  }

  CCloud_GetFileDetails_Response --> CCloud_UserFile : details
  CCloud_EnumerateUserFiles_Response --> CCloud_UserFile : files[]

```

## Messages

### `CCloud_GetUploadServerInfo_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |

### `CCloud_GetUploadServerInfo_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `server_url` | 1 | string | optional |  |

### `CCloud_GetFileDetails_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ugcid` | 1 | uint64 | optional |  |
| `appid` | 2 | uint32 | optional |  |

### `CCloud_UserFile`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `ugcid` | 2 | uint64 | optional |  |
| `filename` | 3 | string | optional |  |
| `timestamp` | 4 | uint64 | optional |  |
| `file_size` | 5 | uint32 | optional |  |
| `url` | 6 | string | optional |  |
| `steamid_creator` | 7 | fixed64 | optional |  |

### `CCloud_GetFileDetails_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `details` | 1 | [CCloud_UserFile](#ccloud_userfile) | optional |  |

### `CCloud_EnumerateUserFiles_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `appid` | 1 | uint32 | optional |  |
| `extended_details` | 2 | bool | optional |  |
| `count` | 3 | uint32 | optional |  |
| `start_index` | 4 | uint32 | optional |  |

### `CCloud_EnumerateUserFiles_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `files` | 1 | [CCloud_UserFile](#ccloud_userfile) | repeated |  |
| `total_files` | 2 | uint32 | optional |  |

### `CCloud_Delete_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `filename` | 1 | string | optional |  |
| `appid` | 2 | uint32 | optional |  |

### `CCloud_Delete_Response`
