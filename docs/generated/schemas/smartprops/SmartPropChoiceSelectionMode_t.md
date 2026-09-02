---
layout: default
title: SmartPropChoiceSelectionMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / SmartPropChoiceSelectionMode_t

# SmartPropChoiceSelectionMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `RANDOM` | 0 | Random — Randomly pick a choice. If the choices have weights, the weights will be used to determine the probability of picking a given choice |
| `FIRST` | 1 | First — Pick the first valid choice. Selection criteria may be added to a choice to determine if it is valid. |
| `SPECIFIC` | 2 | Specific — Pick a choice specified by an additional authored value. |
