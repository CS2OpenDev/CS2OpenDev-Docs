---
title: CAnimGraphDoc_ProxyNodeBase
module: animgraphdoclib
kind: class
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_ProxyNodeBase

# CAnimGraphDoc_ProxyNodeBase

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** n/a (unspecified) · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md)

**Derived by:** [CAnimGraphDoc_GroupInputNode](../animgraphdoclib/CAnimGraphDoc_GroupInputNode.md), [CAnimGraphDoc_GroupOutputNode](../animgraphdoclib/CAnimGraphDoc_GroupOutputNode.md)

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_Node <|-- CAnimGraphDoc_ProxyNodeBase
    CAnimGraphDoc_ProxyNodeBase <|-- CAnimGraphDoc_GroupInputNode
    CAnimGraphDoc_ProxyNodeBase <|-- CAnimGraphDoc_GroupOutputNode
    CAnimGraphDoc_ProxyNodeBase *-- CConnectionProxyItem
```

## Memory layout

6 fields (1 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_sName` | CUtlString | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |
| `0x28` | `m_vecPosition` | Vector2D | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x30` | `m_nNodeID` | [AnimNodeID](../modellib/AnimNodeID.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x34` | `m_bDebugThisNode` | bool | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Debug This Node` `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x38` | `m_networkMode` | [AnimNodeNetworkMode](../animgraphlib/AnimNodeNetworkMode.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Network Mode` `MPropertySortPriority -110` |
| `0x48` | `m_proxyItems` | CUtlVector< [CConnectionProxyItem](../animgraphdoclib/CConnectionProxyItem.md) > |  | `MPropertyAutoExpandSelf` `MPropertyFriendlyName External Connections` |
