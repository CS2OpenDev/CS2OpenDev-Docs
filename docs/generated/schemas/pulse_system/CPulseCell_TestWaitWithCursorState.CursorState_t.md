---
layout: default
title: "CPulseCell_TestWaitWithCursorState::CursorState_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_system](../pulse_system.md) / CPulseCell_TestWaitWithCursorState::CursorState_t

# CPulseCell_TestWaitWithCursorState::CursorState_t

**Kind:** class · **Size:** 36 bytes (`0x24`) · **Align:** 4 · **Module:** pulse_system

**Relationships:**

```mermaid
classDiagram
    "CPulseCell_TestWaitWithCursorState::CursorState_t" *-- CPulseCell_TestWaitWithCursorState
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `flWaitValue` | float32 |  |  |
| `0x4` | `bFail` | bool |  |  |
| `0x8` | `m_hSelfCursor` | HYieldedCursor |  |  |
| `0x14` | `m_hSelfCellInstanceUntyped` | HPulseCellBase |  |  |
| `0x1c` | `m_hSelfCellInstance` | HPulseCell< [CPulseCell_TestWaitWithCursorState](../pulse_system/CPulseCell_TestWaitWithCursorState.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;flWaitValue&quot;: 0.000000,
	&quot;bFail&quot;: false,
	&quot;m_hSelfCursor&quot;:
	{
		&quot;m_hGraph&quot;:
		{
			&quot;m_nGraphID&quot;: 0
		},
		&quot;m_nCursorID&quot;: -1,
		&quot;m_nYieldToken&quot;: -1
	},
	&quot;m_hSelfCellInstanceUntyped&quot;:
	{
		&quot;m_hGraph&quot;:
		{
			&quot;m_nGraphID&quot;: 0
		},
		&quot;m_nCellID&quot;: -1
	},
	&quot;m_hSelfCellInstance&quot;:
	{
		&quot;m_hGraph&quot;:
		{
			&quot;m_nGraphID&quot;: 0
		},
		&quot;m_nCellID&quot;: -1
	}
}</pre>
</details>
