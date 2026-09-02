---
title: ActiveModelConfig_t (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / ActiveModelConfig_t

# ActiveModelConfig_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 8 · **Module:** client

**Twin:** [ActiveModelConfig_t (server)](../server/ActiveModelConfig_t.md)

**Relationships:**

```mermaid
classDiagram
    ActiveModelConfig_t *-- ModelConfigHandle_t
    ActiveModelConfig_t --> C_BaseModelEntity
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x30` | `m_Handle` | [ModelConfigHandle_t](../server/ModelConfigHandle_t.md) |  |  |
| `0x38` | `m_Name` | CUtlSymbolLarge |  |  |
| `0x40` | `m_AssociatedEntities` | C_NetworkUtlVectorBase< CHandle< [C_BaseModelEntity](../client/C_BaseModelEntity.md) > > |  |  |
| `0x58` | `m_AssociatedEntityNames` | C_NetworkUtlVectorBase< CUtlSymbolLarge > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;ActiveModelConfig_t&quot;,
	&quot;m_Handle&quot;: 0,
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_AssociatedEntities&quot;:
	[
	],
	&quot;m_AssociatedEntityNames&quot;:
	[
	]
}</pre>
</details>
