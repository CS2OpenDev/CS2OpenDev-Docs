---
layout: default
title: modifiedconvars_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / modifiedconvars_t

# modifiedconvars_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 384 bytes (`0x180`) · **Align:** 1 · **Module:** server

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `pszConvar` | char[128] |  |  |
| `0x80` | `pszCurrentValue` | char[128] |  |  |
| `0x100` | `pszOrgValue` | char[128] |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;pszConvar&quot;: &quot;&quot;,
	&quot;pszCurrentValue&quot;: &quot;&quot;,
	&quot;pszOrgValue&quot;: &quot;&quot;
}</pre>
</details>
