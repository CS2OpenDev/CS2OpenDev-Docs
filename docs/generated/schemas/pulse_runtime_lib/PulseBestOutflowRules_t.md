---
title: PulseBestOutflowRules_t
module: pulse_runtime_lib
kind: enum
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / PulseBestOutflowRules_t

# PulseBestOutflowRules_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** pulse_runtime_lib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `SORT_BY_NUMBER_OF_VALID_CRITERIA` | 0 | Choose Best — Choose the best outflow with all rules passing, as determined by number of passing rules (specificity). |
| `SORT_BY_OUTFLOW_INDEX` | 1 | Choose First — Choose the first outflow with all rules passing, from left to right |
