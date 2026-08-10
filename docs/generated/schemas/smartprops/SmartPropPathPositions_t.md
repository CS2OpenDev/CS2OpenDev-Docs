---
layout: default
title: SmartPropPathPositions_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / SmartPropPathPositions_t

# SmartPropPathPositions_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** smartprops

## Values

| Name | Value | Description |
|------|-------|-------------|
| `ALL` | 0 | All positions — Place at all positions along the path |
| `NTH` | 1 | Every N positions — Place at every Nth position along the path, skipping over the other positions |
| `START_AND_END` | 2 | Only at start and end — Only place at the start or end of the path |
| `CONTROL_POINTS` | 3 | Path control points — Place at path control points instead of every point along the path, when this is selected the path spacing no longer applies |
