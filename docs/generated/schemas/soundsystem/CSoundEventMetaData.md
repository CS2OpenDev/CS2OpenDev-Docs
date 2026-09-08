---
title: CSoundEventMetaData
module: soundsystem
kind: class
---

[Schemas](../../schemas.md) / [soundsystem](../soundsystem.md) / CSoundEventMetaData

# CSoundEventMetaData

> Source: **Build 25175329** · 2026-09-07 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 8 · **Module:** soundsystem

**Relationships:**

```mermaid
classDiagram
    CSoundEventMetaData *-- InfoForResourceTypeCVMixListResource
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_soundEventVMix` | CStrongHandle< [InfoForResourceTypeCVMixListResource](../resourcesystem/InfoForResourceTypeCVMixListResource.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_soundEventVMix&quot;: &quot;&quot;
}</pre>
</details>
