---
title: EntityIOQueuePrioritizedEvent_t
module: entity2
kind: class
---

[Schemas](../../schemas.md) / [entity2](../entity2.md) / EntityIOQueuePrioritizedEvent_t

# EntityIOQueuePrioritizedEvent_t

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 248 bytes (`0xf8`) · **Align:** 8 · **Module:** entity2

**Relationships:**

```mermaid
classDiagram
    EntityIOQueuePrioritizedEvent_t *-- GameTime_t
    EntityIOQueuePrioritizedEvent_t *-- EntityIOTargetType_t
    EntityIOQueuePrioritizedEvent_t *-- CVariantDefaultAllocator
```

## Memory layout

10 fields (10 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x4` | `m_flFireTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x8` | `m_targetType` | [EntityIOTargetType_t](../entity2/EntityIOTargetType_t.md) |  |  |
| `0x10` | `m_pTarget` | CUtlSymbolLarge |  |  |
| `0x18` | `m_pTargetInput` | CUtlSymbolLarge |  |  |
| `0x20` | `m_hActivator` | CEntityHandle |  |  |
| `0x24` | `m_hCaller` | CEntityHandle |  |  |
| `0x28` | `m_hEntTarget` | CEntityHandle |  |  |
| `0x30` | `m_variantValue` | CVariantBase< [CVariantDefaultAllocator](../entity2/CVariantDefaultAllocator.md) > |  | `MKV3TransferSaveOpsForField GetVariantSaveDataOps` |
| `0x40` | `m_PulseArguments` | CPulseArgumentPack |  |  |
| `0xd0` | `m_paramMap` | CPulseInputParamMap |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flFireTime&quot;: null,
	&quot;m_targetType&quot;: 0,
	&quot;m_pTarget&quot;: &quot;&quot;,
	&quot;m_pTargetInput&quot;: &quot;&quot;,
	&quot;m_hActivator&quot;: null,
	&quot;m_hCaller&quot;: null,
	&quot;m_hEntTarget&quot;: null,
	&quot;m_PulseArguments&quot;:
	{
	},
	&quot;m_paramMap&quot;:
	{
		&quot;--forward-all-args--&quot;: false
	}
}</pre>
</details>
