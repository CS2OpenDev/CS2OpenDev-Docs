---
title: CVMixEditorNode
module: sounddoc_lib
kind: class
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CVMixEditorNode

# CVMixEditorNode

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** sounddoc_lib

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  | `MKV3TransferName name` |
| `0x8` | `m_friendlyName` | CUtlString |  | `MKV3TransferName friendlyname` |
| `0x10` | `m_type` | CUtlString |  | `MKV3TransferName type` |
| `0x18` | `m_vPos` | Vector2D |  | `MKV3TransferName editor_pos` |
| `0x20` | `m_vSize` | Vector2D |  | `MKV3TransferName editor_size` |
| `0x28` | `m_properties` | KeyValues3 |  | `MKV3TransferName properties` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;name&quot;: &quot;&quot;,
	&quot;friendlyname&quot;: &quot;&quot;,
	&quot;type&quot;: &quot;&quot;,
	&quot;editor_pos&quot;:
	[
		0.000000,
		0.000000
	],
	&quot;editor_size&quot;:
	[
		0.000000,
		0.000000
	],
	&quot;properties&quot;: null
}</pre>
</details>
