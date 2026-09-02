---
layout: default
title: VMixGraphCommandID_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_lowlevel](../soundsystem_lowlevel.md) / VMixGraphCommandID_t

# VMixGraphCommandID_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** soundsystem_lowlevel

## Values

| Name | Value | Description |
|------|-------|-------------|
| `CMD_INVALID` | -1 (`0xffffffff`) |  |
| `CMD_CONTROL_INPUT_STORE` | 1 |  |
| `CMD_CONTROL_INPUT_STORE_DB` | 2 |  |
| `CMD_CONTROL_TRANSIENT_INPUT_STORE` | 3 |  |
| `CMD_CONTROL_TRANSIENT_INPUT_RESET` | 4 |  |
| `CMD_CONTROL_OUTPUT_STORE` | 5 |  |
| `CMD_CONTROL_EVALUATE_CURVE` | 6 |  |
| `CMD_CONTROL_COPY` | 7 |  |
| `CMD_CONTROL_COND_COPY_IF_NEGATIVE` | 8 |  |
| `CMD_CONTROL_REMAP_LINEAR` | 9 |  |
| `CMD_CONTROL_REMAP_SINE` | 10 |  |
| `CMD_CONTROL_REMAP_LOGLINEAR` | 11 |  |
| `CMD_CONTROL_MAX` | 12 |  |
| `CMD_CONTROL_RESET_TIMER` | 13 |  |
| `CMD_CONTROL_INCREMENT_TIMER` | 14 |  |
| `CMD_CONTROL_EVAL_ENVELOPE` | 15 |  |
| `CMD_CONTROL_SINE_BLEND` | 16 |  |
| `CMD_PROCESSOR_SET_CONTROL_VALUE` | 17 |  |
| `CMD_PROCESSOR_SET_NAME_INPUT` | 18 |  |
| `CMD_PROCESSOR_SET_CONTROL_ARRAYVALUE` | 19 |  |
| `CMD_PROCESSOR_STORE_CONTROL_VALUE` | 20 |  |
| `CMD_PROCESSOR_SET_VSND_VALUE` | 21 |  |
| `CMD_SUBMIX_PROCESS` | 22 |  |
| `CMD_SUBMIX_GENERATE` | 23 |  |
| `CMD_SUBMIX_GENERATE_SIDECHAIN` | 24 |  |
| `CMD_SUBMIX_EXTRACTCONTAINER` | 25 |  |
| `CMD_SUBMIX_DEBUG` | 26 |  |
| `CMD_SUBMIX_MIX2x1` | 27 |  |
| `CMD_SUBMIX_OUTPUT` | 28 |  |
| `CMD_SUBMIX_OUTPUTx2` | 29 |  |
| `CMD_SUBMIX_COPY` | 30 |  |
| `CMD_SUBMIX_ACCUMULATE` | 31 |  |
| `CMD_SUBMIX_METER` | 32 |  |
| `CMD_SUBMIX_METER_SPECTRUM` | 33 |  |
| `CMD_IMPULSERESPONSE_INPUT_STORE` | 34 |  |
| `CMD_PROCESSOR_SET_IMPULSERESPONSE_VALUE` | 35 |  |
| `CMD_REMAP_VSND_TO_IMPULSERESPONSE` | 36 |  |
| `CMD_IMPULSERESPONSE_RESET` | 37 |  |
| `CMD_BLEND_VSNDS_TO_IMPULSERESPONSE` | 38 |  |
| `CMD_IMPULSERESPONSE_DELAY` | 39 |  |
