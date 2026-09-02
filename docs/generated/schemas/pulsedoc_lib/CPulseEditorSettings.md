---
layout: default
title: CPulseEditorSettings
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulsedoc_lib](../pulsedoc_lib.md) / CPulseEditorSettings

# CPulseEditorSettings

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 488 bytes (`0x1e8`) · **Align:** 8 · **Module:** pulsedoc_lib

## Memory layout

101 fields (101 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_colCanvasBackground` | Color |  |  |
| `0x4` | `m_colCanvasBackgroundWhenDebugging` | Color |  |  |
| `0x8` | `m_flGridSnapV2` | float32 |  | `MPropertyStartGroup +Grid` |
| `0xc` | `m_bSnapAbsToGrid` | bool |  |  |
| `0xd` | `m_bSnapSizeToGrid` | bool |  |  |
| `0xe` | `m_bGridMinorPoints` | bool |  |  |
| `0x10` | `m_flGridMinorSpacingV2` | float32 |  |  |
| `0x14` | `m_flSuppressMinorGridFurtherThan` | float32 |  |  |
| `0x18` | `m_colGridMinorColor` | Color |  |  |
| `0x1c` | `m_flGridMinorWidth` | float32 |  |  |
| `0x20` | `m_nGridMajorMultiple` | int32 |  | `MPropertyAttributeRange 1 25` |
| `0x24` | `m_colGridMajorColor` | Color |  |  |
| `0x28` | `m_flGridMajorWidth` | float32 |  |  |
| `0x2c` | `m_colGridOriginColor` | Color |  |  |
| `0x30` | `m_flGridOriginWidth` | float32 |  |  |
| `0x34` | `m_nFlowTooltipBoxMargin` | float32 |  | `MPropertyAttributeRange 0 32` `MPropertyStartGroup +Ports` |
| `0x38` | `m_FontSequencePoint` | CUtlString |  | `MPropertyAttributeEditor Font()` |
| `0x40` | `m_flSequencePointRadius` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x44` | `m_flSequencePointLinkWidth` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x48` | `m_colSequencePointFadeOverlay` | Color |  | `MPropertyColorPlusAlpha` |
| `0x4c` | `m_colSequencePointSpontaneous` | Color |  |  |
| `0x50` | `m_colSequencePointYield` | Color |  |  |
| `0x54` | `m_colSequencePoint` | Color |  |  |
| `0x58` | `m_colSequencePointLink` | Color |  |  |
| `0x5c` | `m_colSequencePointLinkYield` | Color |  |  |
| `0x60` | `m_colSequencePointName` | Color |  |  |
| `0x64` | `m_colFlowTooltipBorder` | Color |  |  |
| `0x68` | `m_colFlowTooltipBackground` | Color |  |  |
| `0x6c` | `m_colFlowTooltipForeground` | Color |  |  |
| `0x70` | `m_flPortDragOffCreateThreshold` | float32 |  | `MPropertyAttributeRange -1 128` |
| `0x74` | `m_colBool` | Color |  | `MPropertyStartGroup +Types` |
| `0x78` | `m_colNumber` | Color |  |  |
| `0x7c` | `m_colString` | Color |  |  |
| `0x80` | `m_colOther` | Color |  |  |
| `0x84` | `m_colCursorFlow` | Color |  |  |
| `0x88` | `m_FontFlowTooltip` | CUtlString |  | `MPropertyAttributeEditor Font()` `MPropertyStartGroup +Fonts` |
| `0x90` | `m_FontLiteral` | CUtlString |  | `MPropertyAttributeEditor Font()` |
| `0x98` | `m_FontDomainName` | CUtlString |  | `MPropertyAttributeEditor Font()` |
| `0xa0` | `m_vDomainNameOffsetPX` | Vector2D |  |  |
| `0xa8` | `m_colDomainName` | Color |  |  |
| `0xac` | `m_colDomainNameWhenDebugging` | Color |  |  |
| `0xb0` | `m_FontParentAssets` | CUtlString |  | `MPropertyAttributeEditor Font()` |
| `0xb8` | `m_colParentAssets` | Color |  |  |
| `0xbc` | `m_colParentAssetsBroken` | Color |  |  |
| `0xc0` | `m_flLiteralLabelSpacing` | float32 |  | `MPropertyAttributeRange 0 32` `MPropertyStartGroup +Literals` |
| `0xc4` | `m_colDebuggerBrokenBorder` | Color |  | `MPropertyStartGroup +Debugger` |
| `0xc8` | `m_DebuggerBrokenImg` | CUtlString |  |  |
| `0xd0` | `m_DebuggerBrokenOtherImg` | CUtlString |  |  |
| `0xd8` | `m_flDebuggerBrokenMarkerOffset` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0xdc` | `m_flDebuggerBrokenMarkerSize` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0xe0` | `m_DebuggerBreakpointImg` | CUtlString |  |  |
| `0xe8` | `m_DebuggerBreakpointDisabledImg` | CUtlString |  |  |
| `0xf0` | `m_flYieldedCursorStackOffset` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0xf8` | `m_GraphInstanceImg` | CUtlString |  |  |
| `0x100` | `m_flRecentExecTimeoutSec` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x104` | `m_flRecentExecStartOffset` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x108` | `m_flRecentExecEndOffset` | float32 |  | `MPropertyAttributeRange 0 64` |
| `0x10c` | `m_flRecentExecLineWidth` | float32 |  | `MPropertyAttributeRange 0 8` |
| `0x110` | `m_colRecentExecStartColor` | Color |  | `MPropertyColorPlusAlpha` |
| `0x114` | `m_colRecentExecEndColor` | Color |  | `MPropertyColorPlusAlpha` |
| `0x118` | `m_colRecentExecRequirementFailStartColor` | Color |  | `MPropertyColorPlusAlpha` |
| `0x11c` | `m_colRecentExecRequirementFailEndColor` | Color |  | `MPropertyColorPlusAlpha` |
| `0x120` | `m_flRecentExecConnectionIndicatorSize` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x128` | `m_RecentExecConnectionIndicatorImg` | CUtlString |  |  |
| `0x130` | `m_bBreakOnExceptions` | bool |  |  |
| `0x131` | `m_bShowExecutionHistory` | bool |  |  |
| `0x132` | `m_bBoxSelectRequiresFullyContained` | bool |  |  |
| `0x134` | `m_flFlowMinWidth` | float32 |  | `MPropertyStartGroup +Group Layout` |
| `0x138` | `m_colSelectedBorder` | Color |  |  |
| `0x13c` | `m_flAppendButtonSize` | float32 |  | `MPropertyAttributeRange 0 64` |
| `0x140` | `m_colAppendHover` | Color |  |  |
| `0x148` | `m_AppendImg` | CUtlString |  |  |
| `0x150` | `m_flMoveChildArrowOffset` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x154` | `m_flMoveChildArrowSize` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x158` | `m_MoveChildArrowImg` | CUtlString |  |  |
| `0x160` | `m_colMoveChildArrow` | Color |  |  |
| `0x164` | `m_flConnectionTangentStrength` | float32 |  | `MPropertyAttributeRange 0 500` `MPropertyStartGroup +Connections` |
| `0x168` | `m_flConnectionCurveSpacing` | float32 |  | `MPropertyAttributeRange 1 50` |
| `0x16c` | `m_flConnectionDeltaLimitScale` | float32 |  | `MPropertyAttributeRange 0 2` |
| `0x170` | `m_flBrokenConnectionOffset` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x174` | `m_flConnectionInflowOffset` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x178` | `m_flConnectionInparamOffset` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x17c` | `m_flConnectionInparamOffsetArray` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x180` | `m_flConnectionCapBrokenSize` | float32 |  | `MPropertyAttributeRange 0 32` |
| `0x188` | `m_ConnectionCapBrokenImg` | CUtlString |  |  |
| `0x190` | `m_flConnectionColorLerpPercentageStart` | float32 |  | `MPropertyAttributeRange 0 1` |
| `0x194` | `m_vecBlockCommentDefaultSize` | Vector2D |  | `MPropertyStartGroup +Notes` |
| `0x19c` | `m_vecBlockCommentMinSize` | Vector2D |  |  |
| `0x1a4` | `m_colBlockCommentDefault` | Color |  |  |
| `0x1a8` | `m_colBlockCommentTextLight` | Color |  |  |
| `0x1ac` | `m_colBlockCommentTextDark` | Color |  |  |
| `0x1b0` | `m_flBlockCommentRegionAlpha` | float32 |  |  |
| `0x1b4` | `m_flTimelineSeekBarHeight` | float32 |  | `MPropertyStartGroup +Timelines` |
| `0x1b8` | `m_flTimelinePauseIconSize` | float32 |  |  |
| `0x1bc` | `m_flTimelineCallModeIconSize` | float32 |  |  |
| `0x1c0` | `m_FontTimelineTime` | CUtlString |  | `MPropertyAttributeEditor Font()` |
| `0x1c8` | `m_colTimelineLabel` | Color |  |  |
| `0x1cc` | `m_vecTimelineIconFromPort` | Vector2D |  |  |
| `0x1d4` | `m_vecTimelinePauseIconOffset` | Vector2D |  |  |
| `0x1dc` | `m_flTimelineCursorHeight` | float32 |  |  |
| `0x1e0` | `m_flTimelineCursorTextHeight` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_colCanvasBackground&quot;:
	[
		16,
		16,
		16
	],
	&quot;m_colCanvasBackgroundWhenDebugging&quot;:
	[
		45,
		16,
		16
	],
	&quot;m_flGridSnapV2&quot;: 40.000000,
	&quot;m_bSnapAbsToGrid&quot;: true,
	&quot;m_bSnapSizeToGrid&quot;: true,
	&quot;m_bGridMinorPoints&quot;: true,
	&quot;m_flGridMinorSpacingV2&quot;: 40.000000,
	&quot;m_flSuppressMinorGridFurtherThan&quot;: 5000.000000,
	&quot;m_colGridMinorColor&quot;:
	[
		48,
		48,
		48
	],
	&quot;m_flGridMinorWidth&quot;: 2.000000,
	&quot;m_nGridMajorMultiple&quot;: 10,
	&quot;m_colGridMajorColor&quot;:
	[
		31,
		31,
		31
	],
	&quot;m_flGridMajorWidth&quot;: 1.500000,
	&quot;m_colGridOriginColor&quot;:
	[
		0,
		54,
		55
	],
	&quot;m_flGridOriginWidth&quot;: 1.500000,
	&quot;m_nFlowTooltipBoxMargin&quot;: 4.000000,
	&quot;m_FontSequencePoint&quot;: &quot;Segoe UI,8,-1,5,50,0,0,0,0,0,Regular&quot;,
	&quot;m_flSequencePointRadius&quot;: 21.000000,
	&quot;m_flSequencePointLinkWidth&quot;: 2.000000,
	&quot;m_colSequencePointFadeOverlay&quot;:
	[
		0,
		0,
		0,
		200
	],
	&quot;m_colSequencePointSpontaneous&quot;:
	[
		0,
		255,
		0
	],
	&quot;m_colSequencePointYield&quot;:
	[
		255,
		255,
		0
	],
	&quot;m_colSequencePoint&quot;:
	[
		128,
		128,
		128
	],
	&quot;m_colSequencePointLink&quot;:
	[
		200,
		200,
		200
	],
	&quot;m_colSequencePointLinkYield&quot;:
	[
		200,
		200,
		0
	],
	&quot;m_colSequencePointName&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_colFlowTooltipBorder&quot;:
	[
		0,
		0,
		0
	],
	&quot;m_colFlowTooltipBackground&quot;:
	[
		100,
		100,
		100
	],
	&quot;m_colFlowTooltipForeground&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_flPortDragOffCreateThreshold&quot;: 32.000000,
	&quot;m_colBool&quot;:
	[
		142,
		47,
		0
	],
	&quot;m_colNumber&quot;:
	[
		62,
		187,
		112
	],
	&quot;m_colString&quot;:
	[
		0,
		109,
		187
	],
	&quot;m_colOther&quot;:
	[
		156,
		115,
		0
	],
	&quot;m_colCursorFlow&quot;:
	[
		140,
		140,
		140
	],
	&quot;m_FontFlowTooltip&quot;: &quot;Segoe UI,11,-1,5,50,0,0,0,0,0,Regular&quot;,
	&quot;m_FontLiteral&quot;: &quot;Barlow,13,-1,5,75,0,0,0,0,0,Bold&quot;,
	&quot;m_FontDomainName&quot;: &quot;Lucida Sans,72,-1,5,50,0,0,0,0,0,Regular&quot;,
	&quot;m_vDomainNameOffsetPX&quot;:
	[
		10.000000,
		10.000000
	],
	&quot;m_colDomainName&quot;:
	[
		64,
		64,
		64
	],
	&quot;m_colDomainNameWhenDebugging&quot;:
	[
		128,
		64,
		64
	],
	&quot;m_FontParentAssets&quot;: &quot;Lucida Sans,20,-1,5,50,0,0,0,0,0,Regular&quot;,
	&quot;m_colParentAssets&quot;:
	[
		64,
		64,
		64
	],
	&quot;m_colParentAssetsBroken&quot;:
	[
		255,
		144,
		144
	],
	&quot;m_flLiteralLabelSpacing&quot;: 8.000000,
	&quot;m_colDebuggerBrokenBorder&quot;:
	[
		255,
		144,
		144
	],
	&quot;m_DebuggerBrokenImg&quot;: &quot;tools/images/pulse_editor/debugger_broken.png&quot;,
	&quot;m_DebuggerBrokenOtherImg&quot;: &quot;tools/images/pulse_editor/debugger_broken_other.png&quot;,
	&quot;m_flDebuggerBrokenMarkerOffset&quot;: 2.000000,
	&quot;m_flDebuggerBrokenMarkerSize&quot;: 18.000000,
	&quot;m_DebuggerBreakpointImg&quot;: &quot;tools/images/pulse_editor/debugger_breakpoint.png&quot;,
	&quot;m_DebuggerBreakpointDisabledImg&quot;: &quot;tools/images/pulse_editor/debugger_breakpoint_disabled.png&quot;,
	&quot;m_flYieldedCursorStackOffset&quot;: 8.000000,
	&quot;m_GraphInstanceImg&quot;: &quot;tools/images/pulse_editor/graph_instance.png&quot;,
	&quot;m_flRecentExecTimeoutSec&quot;: 10.000000,
	&quot;m_flRecentExecStartOffset&quot;: 20.000000,
	&quot;m_flRecentExecEndOffset&quot;: 150.000000,
	&quot;m_flRecentExecLineWidth&quot;: 4.000000,
	&quot;m_colRecentExecStartColor&quot;:
	[
		150,
		255,
		150
	],
	&quot;m_colRecentExecEndColor&quot;:
	[
		150,
		255,
		150,
		0
	],
	&quot;m_colRecentExecRequirementFailStartColor&quot;:
	[
		200,
		150,
		150
	],
	&quot;m_colRecentExecRequirementFailEndColor&quot;:
	[
		200,
		150,
		150,
		0
	],
	&quot;m_flRecentExecConnectionIndicatorSize&quot;: 8.000000,
	&quot;m_RecentExecConnectionIndicatorImg&quot;: &quot;tools/images/pulse_editor/connection_execution_history.png&quot;,
	&quot;m_bBreakOnExceptions&quot;: false,
	&quot;m_bShowExecutionHistory&quot;: false,
	&quot;m_bBoxSelectRequiresFullyContained&quot;: false,
	&quot;m_flFlowMinWidth&quot;: 200.000000,
	&quot;m_colSelectedBorder&quot;:
	[
		255,
		255,
		0
	],
	&quot;m_flAppendButtonSize&quot;: 20.000000,
	&quot;m_colAppendHover&quot;:
	[
		146,
		152,
		153
	],
	&quot;m_AppendImg&quot;: &quot;tools/images/pulse_editor/add_to_block.png&quot;,
	&quot;m_flMoveChildArrowOffset&quot;: 5.000000,
	&quot;m_flMoveChildArrowSize&quot;: 25.000000,
	&quot;m_MoveChildArrowImg&quot;: &quot;tools/images/pulse_editor/move_child.png&quot;,
	&quot;m_colMoveChildArrow&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_flConnectionTangentStrength&quot;: 100.000000,
	&quot;m_flConnectionCurveSpacing&quot;: 5.000000,
	&quot;m_flConnectionDeltaLimitScale&quot;: 0.300000,
	&quot;m_flBrokenConnectionOffset&quot;: 80.000000,
	&quot;m_flConnectionInflowOffset&quot;: 0.000000,
	&quot;m_flConnectionInparamOffset&quot;: 0.000000,
	&quot;m_flConnectionInparamOffsetArray&quot;: 4.000000,
	&quot;m_flConnectionCapBrokenSize&quot;: 8.000000,
	&quot;m_ConnectionCapBrokenImg&quot;: &quot;tools/images/pulse_editor/connection_cap_broken.png&quot;,
	&quot;m_flConnectionColorLerpPercentageStart&quot;: 0.500000,
	&quot;m_vecBlockCommentDefaultSize&quot;:
	[
		200.000000,
		200.000000
	],
	&quot;m_vecBlockCommentMinSize&quot;:
	[
		200.000000,
		20.000000
	],
	&quot;m_colBlockCommentDefault&quot;:
	[
		47,
		79,
		79
	],
	&quot;m_colBlockCommentTextLight&quot;:
	[
		211,
		211,
		211
	],
	&quot;m_colBlockCommentTextDark&quot;:
	[
		46,
		46,
		46
	],
	&quot;m_flBlockCommentRegionAlpha&quot;: 0.160000,
	&quot;m_flTimelineSeekBarHeight&quot;: 20.000000,
	&quot;m_flTimelinePauseIconSize&quot;: 10.000000,
	&quot;m_flTimelineCallModeIconSize&quot;: 18.000000,
	&quot;m_FontTimelineTime&quot;: &quot;Segoe UI,11,-1,5,50,0,0,0,0,0,Regular&quot;,
	&quot;m_colTimelineLabel&quot;:
	[
		196,
		196,
		196
	],
	&quot;m_vecTimelineIconFromPort&quot;:
	[
		-4.000000,
		-19.000000
	],
	&quot;m_vecTimelinePauseIconOffset&quot;:
	[
		-8.000000,
		3.000000
	],
	&quot;m_flTimelineCursorHeight&quot;: 12.000000,
	&quot;m_flTimelineCursorTextHeight&quot;: 20.000000
}</pre>
</details>
