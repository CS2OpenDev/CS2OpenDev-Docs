---
layout: default
title: AimCameraOpFixedSettings_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / AimCameraOpFixedSettings_t

# AimCameraOpFixedSettings_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animgraphlib

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nChainIndex` | int32 |  |  |
| `0x4` | `m_nCameraJointIndex` | int32 |  |  |
| `0x8` | `m_nPelvisJointIndex` | int32 |  |  |
| `0xc` | `m_nClavicleLeftJointIndex` | int32 |  |  |
| `0x10` | `m_nClavicleRightJointIndex` | int32 |  |  |
| `0x14` | `m_nDepenetrationJointIndex` | int32 |  |  |
| `0x18` | `m_propJoints` | CUtlVector< int32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nChainIndex&quot;: -1,
	&quot;m_nCameraJointIndex&quot;: -1,
	&quot;m_nPelvisJointIndex&quot;: -1,
	&quot;m_nClavicleLeftJointIndex&quot;: -1,
	&quot;m_nClavicleRightJointIndex&quot;: -1,
	&quot;m_nDepenetrationJointIndex&quot;: -1,
	&quot;m_propJoints&quot;:
	[
	]
}</pre>
</details>
