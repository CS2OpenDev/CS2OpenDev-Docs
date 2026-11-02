---
title: CGraphPreviewList
module: sounddoc_lib
kind: class
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CGraphPreviewList

# CGraphPreviewList

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** sounddoc_lib

**Relationships:**

```mermaid
classDiagram
    CGraphPreviewList *-- CPreviewList
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flVolume` | float32 |  |  |
| `0x8` | `m_previewList` | [CPreviewList](../sounddoc_lib/CPreviewList.md) |  |  |
| `0x28` | `m_previewGraphName` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flVolume&quot;: 1.000000,
	&quot;m_previewList&quot;:
	{
		&quot;m_sounds&quot;:
		[
		],
		&quot;m_bPreviewInGame&quot;: false
	},
	&quot;m_previewGraphName&quot;: &quot;&quot;
}</pre>
</details>
