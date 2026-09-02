---
layout: default
title: dynpitchvol_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / dynpitchvol_t

# dynpitchvol_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 100 bytes (`0x64`) · **Align:** 4 · **Module:** server

**Inherits from:** [dynpitchvol_base_t](../server/dynpitchvol_base_t.md)

**Relationships:**

```mermaid
classDiagram
    dynpitchvol_base_t <|-- dynpitchvol_t
```

## Memory layout

25 fields (0 declared here, 25 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `preset` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x4` | `pitchrun` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x8` | `pitchstart` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0xc` | `spinup` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x10` | `spindown` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x14` | `volrun` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x18` | `volstart` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x1c` | `fadein` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x20` | `fadeout` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x24` | `lfotype` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x28` | `lforate` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x2c` | `lfomodpitch` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x30` | `lfomodvol` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x34` | `cspinup` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x38` | `cspincount` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x3c` | `pitch` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x40` | `spinupsav` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x44` | `spindownsav` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x48` | `pitchfrac` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x4c` | `vol` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x50` | `fadeinsav` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x54` | `fadeoutsav` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x58` | `volfrac` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x5c` | `lfofrac` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |
| `0x60` | `lfomult` | int32 | [dynpitchvol_base_t](../server/dynpitchvol_base_t.md) |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;preset&quot;: 0,
	&quot;pitchrun&quot;: 0,
	&quot;pitchstart&quot;: 0,
	&quot;spinup&quot;: 0,
	&quot;spindown&quot;: 0,
	&quot;volrun&quot;: 0,
	&quot;volstart&quot;: 0,
	&quot;fadein&quot;: 0,
	&quot;fadeout&quot;: 0,
	&quot;lfotype&quot;: 0,
	&quot;lforate&quot;: 0,
	&quot;lfomodpitch&quot;: 0,
	&quot;lfomodvol&quot;: 0,
	&quot;cspinup&quot;: 0,
	&quot;cspincount&quot;: 0,
	&quot;pitch&quot;: 0,
	&quot;spinupsav&quot;: 0,
	&quot;spindownsav&quot;: 0,
	&quot;pitchfrac&quot;: &lt;HIDDEN FOR DIFF&gt;,
	&quot;vol&quot;: 32765,
	&quot;fadeinsav&quot;: 0,
	&quot;fadeoutsav&quot;: 0,
	&quot;volfrac&quot;: 0,
	&quot;lfofrac&quot;: 0,
	&quot;lfomult&quot;: 0
}</pre>
</details>
