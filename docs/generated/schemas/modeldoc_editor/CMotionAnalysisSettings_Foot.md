---
layout: default
title: CMotionAnalysisSettings_Foot
nav_exclude: true
---

[Schemas](../../schemas.md) / [modeldoc_editor](../modeldoc_editor.md) / CMotionAnalysisSettings_Foot

# CMotionAnalysisSettings_Foot

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** modeldoc_editor

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_AnkleBoneNames` | CUtlVector< CGlobalSymbol > |  | `MPropertyAutoExpandSelf` `MPropertyDescription Bone name(s) that represent the 'ankle' for this foot. Used for motion analysis. If multiple specified, use the first one found in the skeleton.` |
| `0x18` | `m_AttachmentNames` | CUtlVector< CGlobalSymbol > |  | `MPropertyAutoExpandSelf` `MPropertyDescription Attachment point(s) generated footstep events should have their 'attachment' key set. If multiple specified, use the first one found in the model.` |
| `0x30` | `m_DebugColor` | Color |  |  |
| `0x38` | `m_CreatedEventType` | CUtlString |  | `MPropertyDescription Type of anim event` |
| `0x40` | `m_CreatedEventFootValue` | CUtlString |  | `MPropertyDescription Value to set the 'foot' key (if nonempty)` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_AnkleBoneNames&quot;:
	[
	],
	&quot;m_AttachmentNames&quot;:
	[
	],
	&quot;m_DebugColor&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_CreatedEventType&quot;: &quot;AE_FOOTSTEP&quot;,
	&quot;m_CreatedEventFootValue&quot;: &quot;&quot;
}</pre>
</details>
