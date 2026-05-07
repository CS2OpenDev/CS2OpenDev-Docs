---
layout: default
title: steammessages_oauth.steamworkssdk.proto
parent: Protobufs
nav_exclude: true
---

# `steammessages_oauth.steamworkssdk.proto`

**Imports:** `steammessages_unified_base.steamworkssdk.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class COAuthToken_ImplicitGrantNoPrompt_Request {
    +string clientid
  }

  class COAuthToken_ImplicitGrantNoPrompt_Response {
    +string access_token
    +string redirect_uri
  }

```

## Messages

### `COAuthToken_ImplicitGrantNoPrompt_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `clientid` | 1 | string | optional |  |

### `COAuthToken_ImplicitGrantNoPrompt_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `access_token` | 1 | string | optional |  |
| `redirect_uri` | 2 | string | optional |  |
