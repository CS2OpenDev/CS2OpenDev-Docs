---
layout: default
title: Network Messages
nav_order: 8
---

# Network & Demo Messages

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

The wire-protocol tables: integer message IDs mapped to the protobuf message type carried, recovered from a static RTTI scan of the shipped binaries.  Each type links to its definition on the [protobuf pages](protobufs.md).

## Bidirectional

3 message ids.

| ID | Message type |
|----|--------------|
| 16 | `CBidirMsg_RebroadcastGameEvent` |
| 17 | `CBidirMsg_RebroadcastSource` |
| 19 | `CBidirMsg_PredictionEvent` |

## ClcMessages

4 message ids.

| ID | Message type |
|----|--------------|
| 20 | `CCLCMsg_ClientInfo` |
| 21 | `CCLCMsg_Move` |
| 22 | `CCLCMsg_VoiceData` |
| 23 | `CCLCMsg_BaselineAck` |

## ClientMessages

3 message ids.

| ID | Message type |
|----|--------------|
| 280 | `CClientMsg_CustomGameEvent` |
| 281 | `CClientMsg_CustomGameEventBounce` |
| 282 | `CClientMsg_ClientUIEvent` |

## Demo stream messages

6 command ids in the `.dem` stream.

The command-ID table for demo playback — a flat id space where a single id can bind more than one message type.

| ID | Message type |
|----|--------------|
| 0 | [`CDemoStop`](proto/demo.md#cdemostop) |
| 1 | [`CDemoFileHeader`](proto/demo.md#cdemofileheader) |
| 2 | [`CDemoFileInfo`](proto/demo.md#cdemofileinfo) |
| 3 | [`CDemoSyncTick`](proto/demo.md#cdemosynctick) |
| 4 | [`CDemoSendTables`](proto/demo.md#cdemosendtables) |
| 5 | [`CDemoClassInfo`](proto/demo.md#cdemoclassinfo) |
