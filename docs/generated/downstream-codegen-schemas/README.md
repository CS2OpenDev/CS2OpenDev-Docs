# Downstream codegen schemas

Machine-readable schemas for CS2 entity classes, structs, enums, and game
events — kept in shapes that mirror upstream sources so any tooling that
already targets those sources works unchanged.

## Files

- **`cs2_schema.json`** — community-enriched mirror of
  [DumpSource2's `cs2.json.gz`](https://github.com/ValveResourceFormat/SchemaExplorer/blob/main/schemas/cs2.json.gz).
  Top-level: `generator`, `revision`, `version_date`, `version_time`,
  `classes`, `enums` — exactly upstream's shape.  Optional
  `annotations` blocks layer in community-curated descriptions / notes
  / warnings.  Cross-module twins (e.g. `CCSPlayerController` in both
  `client` and `server`) emit one record per `(module, name)`.

- **`gameevents_schema.json`** — community-enriched mirror of the
  parsed `.gameevents` KV1 registry.  Top-level: `events` list; each
  record preserves its parsed `name` / `comment` / `source` /
  `properties` / `fields` from the upstream KV1 source.  Same
  `annotations` enrichment pattern as `cs2_schema.json`.

- **`convars_schema.json`** — structured projection of
  `DumpSource2/convars.txt`.  Top-level: `convars` list; each entry has
  `name` / `default` / `flags` / `description`.  Codegen-friendly
  counterpart to `convars.md`.

- **`commands_schema.json`** — structured projection of
  `DumpSource2/commands.txt`.  Top-level: `commands` list; each entry
  has `name` / `flags` / `description`.

- **`well_known_constants.json`** — community-curated reference tables
  for integer / enum values that downstream tooling needs but that
  DumpSource2 doesn't expose as named enum types (team numbers,
  `m_gamePhase`, `CSWeaponState_t`, …).  Top-level: `constants` list;
  each entry has `name` / `comment` / `members[]` with the same
  `annotations` pattern as the schema files.

All five files share a single top-level `schema_format_version` string
that is bumped as a family.  Bump the major when a field is removed or
renamed in any of the five; bump the minor when a field is added.
Additive `annotations` blocks do not require a bump.

## Class records with `size > 0` and no fields

167 classes in `cs2_schema.json` report a non-zero `size` but
expose zero fields — `CNmGraphInstance` (992 B),
`CBasePulseGraphInstance`, `CPulseExecCursor`, `CNavVolume`, `CBtNode`,
etc.  These are internal Source 2 runtime classes that the schema
reflection system knows the binary size of but never registers
field-level reflection for.  Downstream codegen consumers can safely
emit them as empty classes; field-level layout is not recoverable from
the dump.

## Why some upstream fields are absent

The mirror only emits what the upstream `cs2.json.gz` carries.  Several
fields that *were* present in older SchemaExplorer dumps no longer
appear and so are absent here too: per-class `abstract`, per-enum
`flags`, per-atomic `handle_kind`, per-enum `storage_size`.  These are
recoverable from the runtime but are not currently projected by
DumpSource2 — file upstream at `ValveResourceFormat/SchemaExplorer` if
you need them restored.

## Why this shape (and not JSON Schema 2020-12)

`cs2_schema.json` and `gameevents_schema.json` were originally JSON
Schema 2020-12 documents.  Standard codegens (quicktype, NJsonSchema,
json-schema-to-typescript) couldn't handle the layered `allOf` /
`$ref` inheritance and the synthetic defs needed to model native CS2
types (`CHandle<X>`, `CUtlVector<T>`, `Vector`, …).  Mirroring the
upstream structured shape lets each consumer apply its own
type-mapping policy without fighting JSON Schema's vocabulary.  The
three companion files (`convars_schema.json`, `commands_schema.json`,
`well_known_constants.json`) follow the same shape-pragmatic pattern:
plain JSON objects with conventional field names, no schema header.

## Format reference

Full per-key documentation lives in
[`AGENTS.md`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/AGENTS.md#cs2_schemajson-format)
at the repository root.

## Auto-generated — do not hand-edit

These files are regenerated every 4 hours from upstream by
[`.github/workflows/generate-docs.yml`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/.github/workflows/generate-docs.yml).
To change the generated output, edit the generator
(`docs/generate_docs.py`) or the community overlays under
`docs/overlays/` instead.

## Type vocabulary observed in this build

Auto-derived from the actual content of `cs2_schema.json` so
the documented vocabulary tracks upstream additions.

### Field `type.category` values

`atomic`, `bitfield`, `builtin`, `declared_class`, `declared_enum`, `fixed_array`, `ptr`

### `builtin` type names

`bool`, `char`, `float32`, `float64`, `int16`, `int32`, `int8`, `uint16`, `uint32`, `uint64`, `uint8`, `void`

### `atomic` type names

`BASEPTR`, `CAnimGraph2ParamAutoResetOptionalRef`, `CAnimGraph2ParamOptionalRef`, `CAnimNetVar`, `CAnimScriptParam`, `CAnimValue`, `CAnimVariant`, `CAttachmentNameSymbolWithStorage`, `CBitVec`, `CBufferString`, `CColorGradient`, `CCompressor`, `CEntityHandle`, `CEntityIndex`, `CEntityNameString`, `CEntityOutputTemplate`, `CGlobalSymbol`, `CGlobalSymbolCaseSensitive`, `CHandle`, `CKV3MemberNameSet`, `CKV3MemberNameWithStorage`, `CModelAnimNameWithDeltas`, `CModelMaterialGroupName`, `CMotionTransform`, `CNetworkUtlVectorBase`, `CNetworkedQuantizedFloat`, `CParticleNamedValueRef`, `CPiecewiseCurve`, `CPlayerSlot`, `CPulseValueFullType`, `CRelativeArray`, `CResourceArray`, `CResourceName`, `CResourceNameTyped`, `CResourcePointer`, `CResourceString`, `CRotation`, `CSmartPropAttributeAngles`, `CSmartPropAttributeBool`, `CSmartPropAttributeColor`, `CSmartPropAttributeFloat`, `CSmartPropAttributeInt`, `CSmartPropAttributeMaterialGroup`, `CSmartPropAttributeMaterialName`, `CSmartPropAttributeModelName`, `CSmartPropAttributeStateName`, `CSmartPropAttributeSurfaceProperty`, `CSmartPropAttributeVariableValue`, `CSmartPropAttributeVector`, `CSmartPropAttributeVector2D`, `CSmartPropVariableComparison`, `CSmartPtr`, `CSoundEventName`, `CSplitScreenSlot`, `CSteamAudioMovableBakedData`, `CStrongHandle`, `CStrongHandleCopyable`, `CStrongHandleVoid`, `CTransform`, `CTransformWS`, `CTypedBitVec`, `CUtlBinaryBlock`, `CUtlHashtable`, `CUtlLeanVector`, `CUtlLeanVectorFixedGrowable`, `CUtlOrderedMap`, `CUtlString`, `CUtlStringMap`, `CUtlStringToken`, `CUtlStringTokenWithStorage`, `CUtlSymbol`, `CUtlSymbolLarge`, `CUtlVector`, `CUtlVectorEmbeddedNetworkVar`, `CUtlVectorFixedGrowable`, `CUtlVectorSIMDPaddedVector`, `CVariantBase`, `CWeakHandle`, `C_NetworkUtlVectorBase`, `C_UtlVectorEmbeddedNetworkVar`, `Color`, `DegreeEuler`, `ENTITYFUNCPTR`, `FourVectors`, `HSCRIPT`, `IPLCompressedEnergyFields`, `IPLProbeBatch`, `IPLScene`, `IPLStaticMesh`, `KeyValues`, `KeyValues3`, `ParticleParamID_t`, `PulseSymbol_t`, `QAngle`, `Quaternion`, `QuaternionStorage`, `RadianEuler`, `Range_t`, `RotationVector`, `SndOpEventGuid_t`, `SphereBase_t`, `USEPTR`, `V_uuid_t`, `Vector`, `Vector2D`, `Vector4D`, `VectorAligned`, `VectorWS`, `WorldGroupId_t`, `fltx4`, `matrix3x4_t`, `matrix3x4a_t`, `std::pair`

### Metadata keys (class / field / enum / member)

- `MAlternateSemanticName`
- `MCustomFGDMetadata`
- `MDebugSnapshotDataRenderByDefault`
- `MDebugSnapshotDataRenderable`
- `MDebugSnapshotDataSummaryFn`
- `MEntityAllowsPortraitWorldSpawn`
- `MEntitySubclassScopeFile`
- `MEnumeratorIsNotAFlag`
- `MFgdFromSchemaCompletelySkipField`
- `MFgdHelper`
- `MGPUParticleFunction`
- `MGetKV3ClassDefaults`
- `MIsBoxedFloatType`
- `MIsBoxedIntegerType`
- `MKV3TransferName`
- `MKV3TransferSaveOpsForField`
- `MModelGameData`
- `MNotSaved`
- `MObsoleteParticleFunction`
- `MParticleAdvancedField`
- `MParticleHelpField`
- `MParticleInputOptional`
- `MParticleMaxVersion`
- `MParticleMinVersion`
- `MParticleReplacementOp`
- `MParticleRequireDefaultArrayEntry`
- `MPhysPtr`
- `MPropertyArrayElementNameKey`
- `MPropertyAttrStateCallback`
- `MPropertyAttributeChoiceName`
- `MPropertyAttributeEditor`
- `MPropertyAttributeRange`
- `MPropertyAttributeSuggestionName`
- `MPropertyAutoExpandSelf`
- `MPropertyAutoRebuildOnChange`
- `MPropertyColorPlusAlpha`
- `MPropertyCustomEditor`
- `MPropertyCustomFGDType`
- `MPropertyDescription`
- `MPropertyEditContextOverrideKey`
- `MPropertyElementNameFn`
- `MPropertyFlattenIntoParentRow`
- `MPropertyFriendlyName`
- `MPropertyGroupName`
- `MPropertyHideField`
- `MPropertyLeafChoiceProviderFn`
- `MPropertyPolymorphicClass`
- `MPropertyProvidesEditContextString`
- `MPropertyReadOnly`
- `MPropertyReadonlyExpr`
- `MPropertyResizable`
- `MPropertySortPriority`
- `MPropertyStartGroup`
- `MPropertySuppressBaseClassField`
- `MPropertySuppressEnumerator`
- `MPropertySuppressExpr`
- `MPropertySuppressField`
- `MPtrAutoallocate`
- `MPulseEditorCanvasItemSpecKV3`
- `MPulseEditorHeaderIcon`
- `MPulseEditorHeaderText`
- `MPulseEditorSubHeaderText`
- `MPulseFunctionHiddenInTool`
- `MResourceTypeForInfoType`
- `MSaveFlags`
- `MSaveOpsForField`
- `MSmartPropClassVersion`
- `MVDataAnonymousNode`
- `MVDataAssociatedFile`
- `MVDataBase`
- `MVDataClassGroup`
- `MVDataComponentRequiresAncestor`
- `MVDataComponentValidGrandParents`
- `MVDataEnableKey`
- `MVDataExperimentalNodeSet`
- `MVDataFileExtension`
- `MVDataGroupNodeClass`
- `MVDataHideNodeClass`
- `MVDataNodeTintColor`
- `MVDataNodeType`
- `MVDataOutlinerAssetNameExpr`
- `MVDataOutlinerDefaultExpanded`
- `MVDataOutlinerDetailExpr`
- `MVDataOutlinerIconExpr`
- `MVDataOutlinerLabelExpr`
- `MVDataOutlinerLeafColorFn`
- `MVDataOutlinerLeafDetailFn`
- `MVDataOutlinerLeafNameFn`
- `MVDataOutlinerNameExpr`
- `MVDataOverlayType`
- `MVDataPostSaveFixupFn`
- `MVDataPreLoadFixupFn`
- `MVDataPreviewWidget`
- `MVDataPromoteField`
- `MVDataRoot`
- `MVDataSingleton`
- `MVDataUniqueMonotonicInt`
- `MVDataUseLinkedEntityClasses`
- `MVDataUsesComponentEditor`
- `MVDataVirtualNodeFactoryFn`
- `MVectorIsCoordinate`
- `MVectorIsSometimesCoordinate`


_Last regenerated against CS2 build `10677034` (May 21 2026)._
