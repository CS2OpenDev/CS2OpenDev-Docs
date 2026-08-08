---
layout: default
title: "CNmSkeletonDocument::SecondarySkeleton_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmSkeletonDocument::SecondarySkeleton_t

# CNmSkeletonDocument::SecondarySkeleton_t

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animdoclib

**Metadata:** `MPropertyAutoExpandSelf`

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_skeleton` | CUtlString |  | `MPropertyAttributeEditor AssetBrowse( vnmskel, *requiredoubleclick )` |
| `0x8` | `m_attachToBoneID` | CGlobalSymbol |  | `MPropertyDescription The bone that we expect this skeleton to be attached to in the parent` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_skeleton&quot;: &quot;&quot;,
	&quot;m_attachToBoneID&quot;: &quot;&quot;
}</pre>
</details>
