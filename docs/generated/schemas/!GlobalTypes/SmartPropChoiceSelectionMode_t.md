---
layout: default
title: SmartPropChoiceSelectionMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / SmartPropChoiceSelectionMode_t

# SmartPropChoiceSelectionMode_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `RANDOM` | 0 | Random — Randomly pick a choice. If the choices have weights, the weights will be used to determine the probability of picking a given choice |
| `FIRST` | 1 | First — Pick the first valid choice. Selection criteria may be added to a choice to determine if it is valid. |
| `SPECIFIC` | 2 | Specific — Pick a choice specified by an additional authored value. |
