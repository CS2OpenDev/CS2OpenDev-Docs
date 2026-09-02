---
title: View3DOptionsEditableData_t
module: hammer
kind: class
---

[Schemas](../../schemas.md) / [hammer](../hammer.md) / View3DOptionsEditableData_t

# View3DOptionsEditableData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** n/a (unspecified) · **Module:** hammer

## Memory layout

21 fields (21 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `bReverseY` | bool |  | `MPropertyFriendlyName Reverse Y` |
| `0x4` | `flPanSpeed` | float32 |  | `MPropertyFriendlyName Pan Speed` |
| `0x8` | `flRotationScale` | float32 |  | `MPropertyFriendlyName Rotation scale` |
| `0xc` | `nForwardSpeedMax` | int32 |  | `MPropertyFriendlyName Forward speed max (world units/sec)` |
| `0x10` | `nTimeToMaxSpeed` | int32 |  | `MPropertyFriendlyName Time to max speed (ms)` |
| `0x14` | `flFOV` | int32 |  | `MPropertyFriendlyName Field of View (degrees)` |
| `0x18` | `szResolutionGate` | CUtlString |  | `MPropertyFriendlyName Resolution Gate` |
| `0x20` | `iBackPlane` | int32 |  | `MPropertyFriendlyName Backplane distance` |
| `0x24` | `flNearPlane` | float32 |  | `MPropertyFriendlyName Nearplane distance` |
| `0x28` | `flShadowFarPlane` | float32 |  | `MPropertyFriendlyName Default light_environment draw distance` |
| `0x2c` | `bMouseWheelControlsFarPlane` | bool |  | `MPropertyFriendlyName Alt+Mouse wheel adjusts backplane distance` |
| `0x30` | `nMouseMoveZoomSensitivity` | int32 |  | `MPropertyFriendlyName Zoom sensitivity using mouse move` |
| `0x34` | `nMouseWheelZoomSensitivity` | int32 |  | `MPropertyFriendlyName Zoom sensitivity using mousewheel` |
| `0x38` | `nCameraTargetDist` | int32 |  | `MPropertyFriendlyName Default distance of camera from point it is set to center view on` |
| `0x3c` | `iGridIntensity` | int32 |  | `MPropertyFriendlyName Grid Intensity` |
| `0x40` | `fSelectionOverlayAlpha` | float32 |  | `MPropertyFriendlyName Alpha of selection mask (0..1)` |
| `0x44` | `bShowSelectionOutline` | bool |  | `MPropertyFriendlyName Outline selected objects` |
| `0x45` | `bSelectionOutlineDepth` | bool |  | `MPropertyFriendlyName Use depth for selection outline` |
| `0x48` | `fToolsVisSSAORadiusScale` | float32 |  | `MPropertyFriendlyName Unlit SSAO Radius Scale` |
| `0x4c` | `fToolsVisSSAOPowerScale` | float32 |  | `MPropertyFriendlyName Unlit SSAO Power Scale` |
| `0x50` | `bPostProcessingEnabled` | bool |  | `MPropertyFriendlyName Enable Post Processing` |
