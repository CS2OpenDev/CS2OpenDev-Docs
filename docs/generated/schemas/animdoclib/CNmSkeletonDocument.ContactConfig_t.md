---
title: "CNmSkeletonDocument::ContactConfig_t"
module: animdoclib
kind: class
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmSkeletonDocument::ContactConfig_t

# CNmSkeletonDocument::ContactConfig_t

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** animdoclib

**Metadata:** `MPropertyAutoExpandSelf`

**Relationships:**

```mermaid
classDiagram
    `CNmSkeletonDocument::ContactConfig_t` *-- NmContactAudioInfo_t
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_ID` | CGlobalSymbol |  |  |
| `0x8` | `m_boneID` | CGlobalSymbol |  |  |
| `0x10` | `m_vBoneLocalProbeDir` | Vector |  |  |
| `0x1c` | `m_flProbeMaxDist` | float32 |  |  |
| `0x20` | `m_audioInfo` | [NmContactAudioInfo_t](../animlib/NmContactAudioInfo_t.md) |  | `MPropertyFriendlyName Audio` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_ID&quot;: &lt;HIDDEN FOR DIFF&gt;,
	&quot;m_boneID&quot;: &quot;&quot;,
	&quot;m_vBoneLocalProbeDir&quot;:
	[
		1.000000,
		0.000000,
		0.000000
	],
	&quot;m_flProbeMaxDist&quot;: 5.000000,
	&quot;m_audioInfo&quot;:
	{
		&quot;m_audioActionID&quot;: &quot;&quot;,
		&quot;m_audioTypeID&quot;: &quot;&quot;,
		&quot;m_soundeventOverrideID&quot;: &quot;&quot;
	}
}</pre>
</details>
