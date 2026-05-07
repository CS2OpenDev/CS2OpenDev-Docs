---
layout: default
title: qcontrols
parent: Schemas
nav_exclude: true
---

# Module: qcontrols

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [GraphCanvasBackgroundImageSize_t](#graphcanvasbackgroundimagesize_t) | enum |  | 4 |
| [GraphCanvasBackgroundPosition_t](#graphcanvasbackgroundposition_t) | enum |  | 5 |
| [GraphCanvasBackgroundRepeat_t](#graphcanvasbackgroundrepeat_t) | enum |  | 4 |
| [GraphCanvasBorderDrawBehavior_t](#graphcanvasborderdrawbehavior_t) | enum |  | 3 |
| [GraphCanvasChildLayoutAlgorithm_t](#graphcanvaschildlayoutalgorithm_t) | enum |  | 5 |
| [GraphCanvasHAlign_t](#graphcanvashalign_t) | enum |  | 4 |
| [GraphCanvasInteractionPriority_t](#graphcanvasinteractionpriority_t) | enum |  | 9 |
| [GraphCanvasItemHoverBehavior_t](#graphcanvasitemhoverbehavior_t) | enum |  | 2 |
| [GraphCanvasPositioning_t](#graphcanvaspositioning_t) | enum |  | 4 |
| [GraphCanvasPseudoClass_t](#graphcanvaspseudoclass_t) | enum |  | 13 |
| [GraphCanvasRenderLayer_t](#graphcanvasrenderlayer_t) | enum |  | 13 |
| [GraphCanvasTextClipMode_t](#graphcanvastextclipmode_t) | enum |  | 4 |
| [GraphCanvasVAlign_t](#graphcanvasvalign_t) | enum |  | 4 |
| [GraphCanvasVisibilityState_t](#graphcanvasvisibilitystate_t) | enum |  | 3 |
| [LayoutAxis_t](#layoutaxis_t) | enum |  | 2 |

---

### GraphCanvasBackgroundImageSize_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Natural` | 0 |  |
| `Contain` | 1 |  |
| `Cover` | 2 |  |
| `Stretch` | 3 |  |

### GraphCanvasBackgroundPosition_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Top` | 0 |  |
| `Left` | 0 |  |
| `Center` | 1 |  |
| `Bottom` | 2 |  |
| `Right` | 2 |  |

### GraphCanvasBackgroundRepeat_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Repeat` | 0 |  |
| `NoRepeat` | 1 |  |
| `RepeatX` | 2 |  |
| `RepeatY` | 3 |  |

### GraphCanvasBorderDrawBehavior_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Centered` | 0 |  |
| `Inside` | 1 |  |
| `Outside` | 2 |  |

### GraphCanvasChildLayoutAlgorithm_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `DEFAULT` | 0 |  |
| `VBOX` | 1 |  |
| `VBOX_REVERSE` | 2 |  |
| `HBOX` | 3 |  |
| `HBOX_REVERSE` | 4 |  |

### GraphCanvasHAlign_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LEFT` | 0 |  |
| `CENTER` | 1 |  |
| `RIGHT` | 2 |  |
| `STRETCH` | 3 |  |

### GraphCanvasInteractionPriority_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `NONINTERACTIVE` | -9999 |  |
| `GROUP` | 0 |  |
| `BASE` | 1 |  |
| `DRAG_HANDLE` | 2 |  |
| `RESIZE_EDGE` | 3 |  |
| `RESIZE_CORNER` | 4 |  |
| `ADD_FLOW` | 5 |  |
| `PORT` | 6 |  |
| `ANCHOR` | 7 |  |

### GraphCanvasItemHoverBehavior_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `HOVER_PROPAGATE` | 0 |  |
| `HOVER_STOP_PROPAGATION` | 1 |  |

### GraphCanvasPositioning_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `AUTO` | 0 |  |
| `INSIDE_PARENT` | 1 |  |
| `OUTSIDE_PARENT` | 2 |  |
| `ON_PARENT_BORDER` | 3 |  |

### GraphCanvasPseudoClass_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `INVALID` | 0 |  |
| `FIRST_CHILD` | 1 |  |
| `LAST_CHILD` | 2 |  |
| `NTH_CHILD` | 3 |  |
| `NTH_LAST_CHILD` | 4 |  |
| `ONLY_CHILD` | 5 |  |
| `HOVER_ANCESTOR` | 6 |  |
| `HOVER_DESCENDANT` | 7 |  |
| `HOVER_CUSTOM_A` | 8 |  |
| `HOVER_CUSTOM_B` | 9 |  |
| `HOVER_CUSTOM_C` | 10 |  |
| `SELECTED` | 11 |  |
| `HOVER_SELF` | 12 |  |

### GraphCanvasRenderLayer_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `INVALID` | -1 |  |
| `COMMENTS` | 0 |  |
| `CONNECTIONS_BACKGROUND` | 1 |  |
| `GROUP_BACKGROUND` | 2 |  |
| `DEFAULT` | 3 |  |
| `NODES` | 4 |  |
| `CONNECTIONS_FOREGROUND` | 5 |  |
| `COMMENT_OVERLAY` | 6 |  |
| `SELECTION_OVERLAY` | 7 |  |
| `HOVER_OVERLAY` | 8 |  |
| `STANDARD_LAYER_COUNT` | 9 |  |
| `SPECIAL_DEBUGGER_OVERLAY` | 10 |  |
| `SPECIAL_LAYER_HOVER_TOOLTIP` | 11 |  |

### GraphCanvasTextClipMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `EXPAND_ITEM` | 0 |  |
| `CLIP_TEXT` | 1 |  |
| `ELIDE_TEXT_END` | 2 |  |
| `WORD_WRAP` | 3 |  |

### GraphCanvasVAlign_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `TOP` | 0 |  |
| `CENTER` | 1 |  |
| `BOTTOM` | 2 |  |
| `STRETCH` | 3 |  |

### GraphCanvasVisibilityState_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `VISIBLE` | 0 |  |
| `HIDDEN` | 1 |  |
| `COLLAPSE` | 2 |  |

### LayoutAxis_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `X` | 0 |  |
| `Y` | 1 |  |
