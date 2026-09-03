---
title: "CNmPreviewArchetype::SecondarySkeleton_t"
module: animdoclib
kind: class
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmPreviewArchetype::SecondarySkeleton_t

# CNmPreviewArchetype::SecondarySkeleton_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animdoclib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_skeleton` | CUtlString |  | `MPropertyAttributeEditor AssetBrowse( vnmskel, *requiredoubleclick )` |
| `0x8` | `m_previewModel` | CUtlString |  | `MPropertyAttributeEditor AssetBrowse( vmdl, *requiredoubleclick )` |
| `0x10` | `m_bodyPartChoiceName` | CUtlString |  |  |
| `0x18` | `m_attachToBoneName` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_skeleton&quot;: &quot;&quot;,
	&quot;m_previewModel&quot;: &quot;&quot;,
	&quot;m_bodyPartChoiceName&quot;: &quot;&quot;,
	&quot;m_attachToBoneName&quot;: &quot;&quot;
}</pre>
</details>
