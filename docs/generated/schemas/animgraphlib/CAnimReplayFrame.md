---
title: CAnimReplayFrame
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CAnimReplayFrame

# CAnimReplayFrame

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 144 bytes (`0x90`) · **Align:** 16 · **Module:** animgraphlib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_inputDataBlocks` | CUtlVector< CUtlBinaryBlock > |  |  |
| `0x28` | `m_instanceData` | CUtlBinaryBlock |  |  |
| `0x40` | `m_startingLocalToWorldTransform` | CTransform |  |  |
| `0x60` | `m_localToWorldTransform` | CTransform |  |  |
| `0x80` | `m_timeStamp` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimReplayFrame&quot;,
	&quot;m_inputDataBlocks&quot;:
	[
	],
	&quot;m_instanceData&quot;: &quot;[BINARY BLOB]&quot;,
	&quot;m_startingLocalToWorldTransform&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000,
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_localToWorldTransform&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000,
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_timeStamp&quot;: 0.000000
}</pre>
</details>
