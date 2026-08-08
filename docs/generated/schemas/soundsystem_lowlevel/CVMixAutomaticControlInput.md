---
layout: default
title: CVMixAutomaticControlInput
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / CVMixAutomaticControlInput

# CVMixAutomaticControlInput

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** soundsystem_lowlevel

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  |  |
| `0x8` | `m_nControlInputIndex` | int32 |  |  |
| `0xc` | `m_bIsTrackSend` | bool |  |  |
| `0xd` | `m_bIsStackVar` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;play time&quot;,
	&quot;m_nControlInputIndex&quot;: -1,
	&quot;m_bIsTrackSend&quot;: false,
	&quot;m_bIsStackVar&quot;: false
}</pre>
</details>
