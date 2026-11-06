---
title: Changelog
---

# Build Changelog

> Source: **Build 26445667** · 2026-11-05 · `windows-x86_64` · schema `0.13.0`

Difference between build **26393695** and **26445667** (`windows-x86_64`), grouped by data family.

Families diffed: `classes`, `enums`, `convars`, `commands`, `engine_constants`, `cs_script_api`, `entity_io`.

## cs_script_api (+14 / −0 / ~9)

**Added:** `CSPlayerController.GetControlledBotPawn#0`, `CSPlayerController.IsControllingBot#0`, `CSPlayerPawn.Reset#0`, `Entity.FireInput#0`, `EntityKeyValue`, `IEntities`, `IEntities.ConnectOutput#0`, `IEntities.DisconnectOutput#0`, `IEntities.FindByClass#0`, `IEntities.FindByName#0`, `IEntities.FireInput#0`, `IEntities.Spawn#0`, `IPointScript.OnBotControl#0`, `export:Entities`

| Entry | Field changes |
|-------|---------------|
| `IPointScript.ConnectOutput#0` | deprecated: `false` → `true`; doc: `Connect the output of an entity to a callback. The return value is a connection id that can be used in `DisconnectOutput`` →  |
| `IPointScript.DisconnectOutput#0` | deprecated: `false` → `true`; doc: `Find entities by name.` →  |
| `IPointScript.EntFireAtName#0` | deprecated: `false` → `true`; doc: `Fire the input on all targets matching the specified names.` →  |
| `IPointScript.EntFireAtTarget#0` | deprecated: `false` → `true`; doc: `Fire the input on the specified target.` →  |
| `IPointScript.FindEntitiesByClass#0` | deprecated: `false` → `true`; doc: `Find entities of the specified class name.` →  |
| `IPointScript.FindEntitiesByName#0` | deprecated: `false` → `true`; doc: `Find entities matching the specified name.` →  |
| `IPointScript.FindEntityByClass#0` | deprecated: `false` → `true`; doc: `Find the first entity of the specified class name.` →  |
| `IPointScript.FindEntityByName#0` | deprecated: `false` → `true`; doc: `Find the first entity matching the specified name.` →  |
| `IPointScript.Precache#0` | doc: `Loads resources on the server and clients to avoid hitches when later referenced. Supports .vmdl, .vpcf, .vmat, and .vsnd resources.` → `Loads resources on the server and clients to avoid hitches when later referenced. `resources` supports .vmdl, .vpcf, .vmat, and .vsnd resources. `entities` takes entity class names or subclass names.`; signature: `Precache(config: { resources: string[] }): CSPrecache &#124; undefined` → `Precache(config: { resources?: string[], entities?: string[] }): CSPrecache &#124; undefined` |
