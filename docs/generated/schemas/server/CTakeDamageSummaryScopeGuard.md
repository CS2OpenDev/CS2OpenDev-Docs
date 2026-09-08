---
title: CTakeDamageSummaryScopeGuard
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CTakeDamageSummaryScopeGuard

# CTakeDamageSummaryScopeGuard

> Source: **Build 25175329** · 2026-09-07 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** n/a (unspecified) · **Module:** server

**Relationships:**

```mermaid
classDiagram
    CTakeDamageSummaryScopeGuard --> SummaryTakeDamageInfo_t
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_vecSummaries` | CUtlVector< [SummaryTakeDamageInfo_t](../server/SummaryTakeDamageInfo_t.md)* > |  |  |
