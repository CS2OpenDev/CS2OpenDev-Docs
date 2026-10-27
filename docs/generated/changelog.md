---
title: Changelog
---

# Build Changelog

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

Difference between build **25966348** and **26144732** (`windows-x86_64`), grouped by data family.

Families diffed: `classes`, `enums`, `convars`, `commands`, `engine_constants`.

## classes (+0 / −1 / ~6)

**Removed:** `!GlobalTypes/InfoForResourceTypeCVMixListResource`

| Entry | Field changes |
|-------|---------------|
| `!GlobalTypes/CGraphPreviewList` | field_count: `2` → `3` |
| `!GlobalTypes/CMixTrack` | field_count: `4` → `5` |
| `!GlobalTypes/CVMixSubmix` | field_count: `6` → `7` |
| `!GlobalTypes/CVoiceContainerBase` | field_count: `2` → `4` |
| `!GlobalTypes/CVoiceContainerVMixSnd` | field_count: `0` → `1` |
| `server.dll/CHostage` | field_count: `39` → `40` |

## enums (+1 / −0 / ~0)

**Added:** `!GlobalTypes/VMixUpMixRule_t`

## convars (+9 / −0 / ~0)

**Added:** `voice_webrtc_aec`, `voice_webrtc_agc`, `voice_webrtc_apm`, `voice_webrtc_fixed_gain_db`, `voice_webrtc_hpf`, `voice_webrtc_ns`, `voice_webrtc_ns_level`, `voice_webrtc_stats`, `voice_webrtc_stream_delay_ms`

## engine_constants (+2 / −0 / ~0)

**Added:** `schema_enum:!GlobalTypes/VMixUpMixRule_t/VMixUpMixRule_t::BROADCAST`, `schema_enum:!GlobalTypes/VMixUpMixRule_t/VMixUpMixRule_t::DIVIDE`
