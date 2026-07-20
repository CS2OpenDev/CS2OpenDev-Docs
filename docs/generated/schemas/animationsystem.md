---
layout: default
title: animationsystem
parent: Schemas
nav_exclude: true
---

# Module: animationsystem

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [PulseBestOutflowRules_t](#pulsebestoutflowrules_t) | enum |  | 2 |
| [PulseCursorCancelPriority_t](#pulsecursorcancelpriority_t) | enum |  | 4 |
| [PulseCursorWakePriority_t](#pulsecursorwakepriority_t) | enum |  | 2 |
| [PulseMethodCallMode_t](#pulsemethodcallmode_t) | enum |  | 2 |

---

### PulseBestOutflowRules_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `SORT_BY_NUMBER_OF_VALID_CRITERIA` | 0 | Choose Best — Choose the best outflow with all rules passing, as determined by number of passing rules (specificity). |
| `SORT_BY_OUTFLOW_INDEX` | 1 | Choose First — Choose the first outflow with all rules passing, from left to right |

### PulseCursorCancelPriority_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Keep running normally. |
| `CancelOnSucceeded` | 1 | Kill After. — Do not stop the current yielding node, but do not continue to the next node afterwards. |
| `SoftCancel` | 2 | Kill Elegantly. — Request elegant wind-down of any associated work (e.g. vcd interrupt). |
| `HardCancel` | 3 | Kill Immediately. — Stop without any wind-down. |

### PulseCursorWakePriority_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `WakeElegantly` | 0 | Proceed Elegantly. — Request elegant wind-down of any associated work (e.g. vcd interrupt), then proceed afterwards. |
| `WakeImmediate` | 1 | Proceed Immediately. — Stop the node action without any wind-down, then proceed afterwards. |

### PulseMethodCallMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `SYNC_WAIT_FOR_COMPLETION` | 0 | Wait For Completion — Synchronous - Wait for this node to fully complete before proceeding. |
| `ASYNC_FIRE_AND_FORGET` | 1 | Proceed Immediately — Asynchronous - This node executes independently using a new Cursor. Formerly 'Fire and Forget'. Equivalent to scheduling using an additional 'Fire Child Cursors' node. |
