---
layout: default
title: CSchemaSystemInternalRegistration
nav_exclude: true
---

[Schemas](../../schemas.md) / [schemasystem](../schemasystem.md) / CSchemaSystemInternalRegistration

# CSchemaSystemInternalRegistration

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 384 bytes (`0x180`) · **Align:** n/a (unspecified) · **Module:** schemasystem

## Memory layout

23 fields (23 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Vector2D` | Vector2D |  |  |
| `0x8` | `m_Vector` | Vector |  |  |
| `0x14` | `m_VectorWS` | VectorWS |  |  |
| `0x20` | `m_VectorAligned` | VectorAligned |  |  |
| `0x30` | `m_Quaternion` | Quaternion |  |  |
| `0x40` | `m_QAngle` | QAngle |  |  |
| `0x4c` | `m_RotationVector` | RotationVector |  |  |
| `0x58` | `m_RadianEuler` | RadianEuler |  |  |
| `0x64` | `m_DegreeEuler` | DegreeEuler |  |  |
| `0x70` | `m_QuaternionStorage` | QuaternionStorage |  |  |
| `0x80` | `m_matrix3x4_t` | matrix3x4_t |  |  |
| `0xb0` | `m_matrix3x4a_t` | matrix3x4a_t |  |  |
| `0xe0` | `m_Color` | Color |  |  |
| `0xe4` | `m_Vector4D` | Vector4D |  |  |
| `0x100` | `m_CTransform` | CTransform |  |  |
| `0x120` | `m_pKeyValues` | KeyValues* |  |  |
| `0x128` | `m_CUtlBinaryBlock` | CUtlBinaryBlock |  |  |
| `0x138` | `m_CUtlString` | CUtlString |  |  |
| `0x140` | `m_CUtlSymbol` | CUtlSymbol |  |  |
| `0x144` | `m_stringToken` | CUtlStringToken |  |  |
| `0x148` | `m_stringTokenWithStorage` | CUtlStringTokenWithStorage |  |  |
| `0x160` | `m_ResourceTypes` | CResourceArray< CResourcePointer< CResourceString > > |  |  |
| `0x168` | `m_KV3` | KeyValues3 |  |  |
