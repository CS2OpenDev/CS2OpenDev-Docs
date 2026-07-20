# Downstream codegen schemas

Machine-readable schemas for CS2 entity classes, structs, enums, and game
events — projected straight from
[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)'s
per-build artifacts so consumers get one deterministic, provenance-tracked
source instead of a chain of third-party dumps.

## Files

- **`cs2_schema.json`** — the entity schema in SchemaTracker's **native**
  shape (`schema_format_version` `2.0`).  Top-level: `generator`, `revision`,
  `version_date`, `version_time`, `classes`, `enums`.  Each class carries
  `name`, `module` (the binary it lives in), `projectName`, `cppName`,
  `size`, `alignment`, `flags` / `flags2`, `parents[]`, `fields[]`
  (`name`, `offset`, `type`, `typeModule`, `metadata`), and inheritance
  depths; each enum carries `alignment` (underlying integer type) and
  `members[]`.  Integer offsets / sizes are **string-encoded** and type
  `category` values are **UPPERCASE** (`BUILTIN`, `ATOMIC`, `DECLARED_CLASS`,
  `PTR`, `FIXED_ARRAY`, `BITFIELD`, …).  Optional `annotations` blocks layer
  in community-curated descriptions / notes / warnings.  A class registered
  in more than one binary emits one record per `(module, name)`.

- **`gameevents_schema.json`** — the game-event registry.  Top-level:
  `events` list; each record has `name` / `comment` / `source` /
  `properties` / `fields`.  Same `annotations` enrichment pattern.

- **`convars_schema.json`** — the console-variable table.  Top-level:
  `convars` list; each entry has `name` / `default` / `flags` /
  `description` (SchemaTracker additionally exposes `valueType` and min/max
  in the source artifact).  Codegen-friendly counterpart to `convars.md`.

- **`commands_schema.json`** — the console-command table.  Top-level:
  `commands` list; each entry has `name` / `flags` / `description`.

- **`well_known_constants.json`** — community-curated reference tables
  for integer / enum values downstream tooling needs but that the schema
  doesn't expose as named enum types (team numbers, `m_gamePhase`,
  `CSWeaponState_t`, …).  Top-level: `constants` list; each entry has
  `name` / `comment` / `members[]` with the same `annotations` pattern.

All five files share a single top-level `schema_format_version` string
that is bumped as a family.  Bump the major when a field is removed or
renamed in any of the five; bump the minor when a field is added.
Additive `annotations` blocks do not require a bump.

## Coverage — runtime only

SchemaTracker walks the **shipped CS2 runtime binaries** in-process, so
`cs2_schema.json` covers exactly the schema those binaries register
(`client`, `server`, `entity2`, `pulse_runtime_lib`, `particleslib`,
`animgraphlib`).  The Source 2 editor / tooling schema (hammer, modeldoc,
resourcecompiler, worldrenderer, …) is intentionally **not** present — it
never ships in the game.

## Class records with `size > 0` and no fields

104 classes in `cs2_schema.json` report a non-zero `size` but
expose zero fields.  These are internal Source 2 runtime classes that the
schema system knows the binary size of but never registers field-level
reflection for.  Downstream codegen consumers can safely emit them as
empty classes; field-level layout is not recoverable from the binary.

## Format reference

Full per-key documentation lives in
[`AGENTS.md`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/AGENTS.md#cs2_schemajson-format)
at the repository root.

## Auto-generated — do not hand-edit

These files are regenerated every 4 hours from the latest
CS2OpenDev-SchemaTracker build by
[`.github/workflows/generate-docs.yml`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/.github/workflows/generate-docs.yml).
To change the generated output, edit the generator
(`docs/generate_docs.py`) or the community overlays under
`docs/overlays/` instead.

## Type vocabulary observed in this build

Auto-derived from the actual content of `cs2_schema.json` so
the documented vocabulary tracks upstream additions.

### Field `type.category` values

`ATOMIC`, `BITFIELD`, `BUILTIN`, `DECLARED_CLASS`, `DECLARED_ENUM`, `FIXED_ARRAY`, `PTR`

### `builtin` type names

`bool`, `char`, `float32`, `float64`, `int16`, `int32`, `int8`, `uint16`, `uint32`, `uint64`, `uint8`

### `atomic` type names

`BASEPTR`, `CAnimGraph2ParamOptionalRef< CGlobalSymbol >`, `CAnimGraph2ParamOptionalRef< CNmTarget >`, `CAnimGraph2ParamOptionalRef< bool >`, `CAnimGraph2ParamOptionalRef< float32 >`, `CAnimNetVar< float32 >`, `CAnimNetVar< int32 >`, `CAttachmentNameSymbolWithStorage`, `CBitVec< 10 >`, `CColorGradient`, `CEntityHandle`, `CEntityIndex`, `CEntityNameString`, `CEntityOutputTemplate< CBaseModelEntity::OnDamageLevelChangedArgs_t >`, `CEntityOutputTemplate< CEntityNameString >`, `CEntityOutputTemplate< CHandle< CBaseEntity > >`, `CEntityOutputTemplate< CTestPulseIO::EntityHandleIntArgs_t >`, `CEntityOutputTemplate< CTestPulseIO::EntityNameStringArgs_t >`, `CEntityOutputTemplate< CTestPulseIO::FloatStringArgs_t >`, `CEntityOutputTemplate< CTestPulseIO::ThreeStringArgs_t >`, `CEntityOutputTemplate< CUtlString >`, `CEntityOutputTemplate< CUtlSymbolLarge >`, `CEntityOutputTemplate< CUtlVector< CEntityHandle > >`, `CEntityOutputTemplate< Color >`, `CEntityOutputTemplate< SndOpEventGuid_t >`, `CEntityOutputTemplate< TestInputOutputCombinationsEnum_t >`, `CEntityOutputTemplate< Vector >`, `CEntityOutputTemplate< bool >`, `CEntityOutputTemplate< float32 >`, `CEntityOutputTemplate< int32 >`, `CGameSoundEventName`, `CGlobalSymbol`, `CHandle< CBaseAnimGraph >`, `CHandle< CBaseEntity >`, `CHandle< CBaseFilter >`, `CHandle< CBaseModelEntity >`, `CHandle< CBasePlayerController >`, `CHandle< CBasePlayerPawn >`, `CHandle< CBasePlayerWeapon >`, `CHandle< CBasePropDoor >`, `CHandle< CBeam >`, `CHandle< CCSObserverPawn >`, `CHandle< CCSPlayerController >`, `CHandle< CCSPlayerPawn >`, `CHandle< CCSPlayerPawnBase >`, `CHandle< CCSWeaponBase >`, `CHandle< CColorCorrection >`, `CHandle< CEconWearable >`, `CHandle< CEntityBlocker >`, `CHandle< CEnvSoundscape >`, `CHandle< CEnvSoundscapeTriggerable >`, `CHandle< CFish >`, `CHandle< CFishPool >`, `CHandle< CFogController >`, `CHandle< CFuncMover >`, `CHandle< CFuncMoverRouter >`, `CHandle< CFuncPlat >`, `CHandle< CFuncTrackTrain >`, `CHandle< CInfoFan >`, `CHandle< CInfoLadderDismount >`, `CHandle< CItemGeneric >`, `CHandle< CItemGenericTriggerHelper >`, `CHandle< CLightEntity >`, `CHandle< CMoverPathNode >`, `CHandle< CPathKeyFrame >`, `CHandle< CPathMover >`, `CHandle< CPathMoverEntitySpawner >`, `CHandle< CPathNode >`, `CHandle< CPathSimple >`, `CHandle< CPathTrack >`, `CHandle< CPathWithDynamicNodes >`, `CHandle< CPlayerPing >`, `CHandle< CPointCamera >`, `CHandle< CPointPrefab >`, `CHandle< CPostProcessingVolume >`, `CHandle< CSceneEntity >`, `CHandle< CSceneListManager >`, `CHandle< CScriptedSequence >`, `CHandle< CSkyCamera >`, `CHandle< CSprite >`, `CHandle< CTonemapController2 >`, `CHandle< C_BaseEntity >`, `CHandle< C_BaseModelEntity >`, `CHandle< C_BasePlayerPawn >`, `CHandle< C_BasePlayerWeapon >`, `CHandle< C_BasePropDoor >`, `CHandle< C_CS2HudModelArms >`, `CHandle< C_CSObserverPawn >`, `CHandle< C_CSPlayerPawn >`, `CHandle< C_CSWeaponBase >`, `CHandle< C_ColorCorrection >`, `CHandle< C_EconWearable >`, `CHandle< C_FogController >`, `CHandle< C_InfoLadderDismount >`, `CHandle< C_Multimeter >`, `CHandle< C_PlantedC4 >`, `CHandle< C_PlayerPing >`, `CHandle< C_PointCamera >`, `CHandle< C_PostProcessingVolume >`, `CHandle< C_SkyCamera >`, `CHandle< C_TonemapController2 >`, `CHandle< SpawnPoint >`, `CNetworkUtlVectorBase< CGlobalSymbol >`, `CNetworkUtlVectorBase< CHandle< CBaseAnimGraph > >`, `CNetworkUtlVectorBase< CHandle< CBaseEntity > >`, `CNetworkUtlVectorBase< CHandle< CBaseModelEntity > >`, `CNetworkUtlVectorBase< CHandle< CBasePlayerController > >`, `CNetworkUtlVectorBase< CHandle< CBasePlayerPawn > >`, `CNetworkUtlVectorBase< CHandle< CBasePlayerWeapon > >`, `CNetworkUtlVectorBase< CHandle< CEconWearable > >`, `CNetworkUtlVectorBase< CHandle< CPathNode > >`, `CNetworkUtlVectorBase< CHandle< CPostProcessingVolume > >`, `CNetworkUtlVectorBase< CTransform >`, `CNetworkUtlVectorBase< CUtlString >`, `CNetworkUtlVectorBase< CUtlSymbolLarge >`, `CNetworkUtlVectorBase< QAngle >`, `CNetworkUtlVectorBase< ResourceId_t >`, `CNetworkUtlVectorBase< SoundeventPathCornerPairNetworked_t >`, `CNetworkUtlVectorBase< Vector >`, `CNetworkUtlVectorBase< Vector2D >`, `CNetworkUtlVectorBase< Vector4D >`, `CNetworkUtlVectorBase< bool >`, `CNetworkUtlVectorBase< float32 >`, `CNetworkUtlVectorBase< int32 >`, `CNetworkUtlVectorBase< uint16 >`, `CNetworkUtlVectorBase< uint8 >`, `CNetworkedQuantizedFloat`, `CPiecewiseCurve`, `CPlayerSlot`, `CPulseObservableExpression< bool >`, `CPulseValueFullType`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCNmSkeleton > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >`, `CSoundEventName`, `CSplitScreenSlot`, `CStrongHandle< InfoForResourceTypeCChoreoSceneResource >`, `CStrongHandle< InfoForResourceTypeCModel >`, `CStrongHandle< InfoForResourceTypeCNmGraphDefinition >`, `CStrongHandle< InfoForResourceTypeCPostProcessingResource >`, `CStrongHandle< InfoForResourceTypeCTextureBase >`, `CStrongHandle< InfoForResourceTypeIMaterial2 >`, `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`, `CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >`, `CStrongHandle< InfoForResourceTypeIPulseGraphDef >`, `CTransform`, `CTransformWS`, `CTypedBitVec< 64 >`, `CUtlBinaryBlock`, `CUtlHashtable< CHandle< CFuncMover >, PathMoverEntitySpawn >`, `CUtlHashtable< PulseCursorID_t, int32 >`, `CUtlLeanVector< CPulseRuntimeMethodArg >`, `CUtlOrderedMap< CGlobalSymbol, int32 >`, `CUtlOrderedMap< WeaponSound_t, CSoundEventName >`, `CUtlString`, `CUtlStringToken`, `CUtlSymbolLarge`, `CUtlVector< ActorMapping_t >`, `CUtlVector< AutoRoomDoorwayPairs_t >`, `CUtlVector< CAttributeManager::cached_attribute_float_t >`, `CUtlVector< CBaseIssue* >`, `CUtlVector< CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t >`, `CUtlVector< CEntityHandle >`, `CUtlVector< CFish* >`, `CUtlVector< CGlobalSymbol >`, `CUtlVector< CHandle< CBaseEntity > >`, `CUtlVector< CHandle< CBaseModelEntity > >`, `CUtlVector< CHandle< CBasePlayerController > >`, `CUtlVector< CHandle< CBasePlayerPawn > >`, `CUtlVector< CHandle< CBasePropDoor > >`, `CUtlVector< CHandle< CEnvSoundscapeTriggerable > >`, `CUtlVector< CHandle< CFish > >`, `CUtlVector< CHandle< CFuncMover > >`, `CUtlVector< CHandle< CInfoLadderDismount > >`, `CUtlVector< CHandle< CLightEntity > >`, `CUtlVector< CHandle< CPathMoverEntitySpawner > >`, `CUtlVector< CHandle< CSceneEntity > >`, `CUtlVector< CHandle< CSceneListManager > >`, `CUtlVector< CHandle< C_BaseEntity > >`, `CUtlVector< CHandle< C_BaseModelEntity > >`, `CUtlVector< CHandle< C_InfoLadderDismount > >`, `CUtlVector< CHandle< SpawnPoint > >`, `CUtlVector< CInfoChoreoAnchorPosition >`, `CUtlVector< CPulseCell_Base* >`, `CUtlVector< CPulseCell_Outflow_PlayVCD::VCDRequirementInfo_t >`, `CUtlVector< CPulseCell_Timeline::TimelineEvent_t >`, `CUtlVector< CPulse_BlackboardReference >`, `CUtlVector< CPulse_CallInfo* >`, `CUtlVector< CPulse_Chunk* >`, `CUtlVector< CPulse_Constant >`, `CUtlVector< CPulse_DomainValue >`, `CUtlVector< CPulse_InvokeBinding* >`, `CUtlVector< CPulse_OutflowConnection >`, `CUtlVector< CPulse_OutputConnection* >`, `CUtlVector< CPulse_PublicOutput >`, `CUtlVector< CPulse_Variable >`, `CUtlVector< CUtlSymbolLarge >`, `CUtlVector< C_BulletHitModel* >`, `CUtlVector< C_EconEntity::AttachedModelData_t >`, `CUtlVector< C_SceneEntity::QueuedEvents_t >`, `CUtlVector< DynamicVolumeDef_t >`, `CUtlVector< INavObstacle* >`, `CUtlVector< OutflowWithRequirements_t >`, `CUtlVector< PulseDocNodeID_t >`, `CUtlVector< PulseNodeDynamicOutflows_t::DynamicOutflow_t >`, `CUtlVector< PulseScriptedSequenceData_t >`, `CUtlVector< Quaternion >`, `CUtlVector< RelationshipOverride_t >`, `CUtlVector< ResponseContext_t >`, `CUtlVector< SoundOpvarTraceResult_t >`, `CUtlVector< Vector >`, `CUtlVector< Vector4D >`, `CUtlVector< VectorWS >`, `CUtlVector< char* >`, `CUtlVector< float32 >`, `CUtlVector< int32 >`, `CUtlVector< lerpdata_t >`, `CUtlVector< magnetted_objects_t >`, `CUtlVector< sndopvarlatchdata_t >`, `CUtlVector< thinkfunc_t >`, `CUtlVector< uint16 >`, `CUtlVector< uint32 >`, `CUtlVectorEmbeddedNetworkVar< AnimGraph2SerializedPoseRecipeSlot_t >`, `CUtlVectorEmbeddedNetworkVar< CDamageRecord >`, `CUtlVectorEmbeddedNetworkVar< CEconItemAttribute >`, `CUtlVectorEmbeddedNetworkVar< CSPerRoundStats_t >`, `CUtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >`, `CUtlVectorEmbeddedNetworkVar< SellbackPurchaseEntry_t >`, `CUtlVectorEmbeddedNetworkVar< ServerAuthoritativeWeaponSlot_t >`, `CUtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >`, `CUtlVectorEmbeddedNetworkVar< WeaponPurchaseCount_t >`, `CUtlVectorFixedGrowable< uint8, 8 >`, `CVariantBase< CVariantDefaultAllocator >`, `CWeakHandle< InfoForResourceTypeCModel >`, `CWeakHandle< InfoForResourceTypeCNmSkeleton >`, `CWeakHandle< InfoForResourceTypeIParticleSystemDefinition >`, `C_NetworkUtlVectorBase< CGlobalSymbol >`, `C_NetworkUtlVectorBase< CHandle< CBaseAnimGraph > >`, `C_NetworkUtlVectorBase< CHandle< CBasePlayerController > >`, `C_NetworkUtlVectorBase< CHandle< CPathNode > >`, `C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >`, `C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >`, `C_NetworkUtlVectorBase< CHandle< C_BasePlayerPawn > >`, `C_NetworkUtlVectorBase< CHandle< C_BasePlayerWeapon > >`, `C_NetworkUtlVectorBase< CHandle< C_EconWearable > >`, `C_NetworkUtlVectorBase< CHandle< C_PostProcessingVolume > >`, `C_NetworkUtlVectorBase< CTransform >`, `C_NetworkUtlVectorBase< CUtlString >`, `C_NetworkUtlVectorBase< CUtlSymbolLarge >`, `C_NetworkUtlVectorBase< QAngle >`, `C_NetworkUtlVectorBase< ResourceId_t >`, `C_NetworkUtlVectorBase< SoundeventPathCornerPairNetworked_t >`, `C_NetworkUtlVectorBase< Vector >`, `C_NetworkUtlVectorBase< Vector2D >`, `C_NetworkUtlVectorBase< Vector4D >`, `C_NetworkUtlVectorBase< bool >`, `C_NetworkUtlVectorBase< float32 >`, `C_NetworkUtlVectorBase< int32 >`, `C_NetworkUtlVectorBase< uint16 >`, `C_NetworkUtlVectorBase< uint8 >`, `C_UtlVectorEmbeddedNetworkVar< AnimGraph2SerializedPoseRecipeSlot_t >`, `C_UtlVectorEmbeddedNetworkVar< CDamageRecord >`, `C_UtlVectorEmbeddedNetworkVar< CEconItemAttribute >`, `C_UtlVectorEmbeddedNetworkVar< CSPerRoundStats_t >`, `C_UtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >`, `C_UtlVectorEmbeddedNetworkVar< SellbackPurchaseEntry_t >`, `C_UtlVectorEmbeddedNetworkVar< ServerAuthoritativeWeaponSlot_t >`, `C_UtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >`, `C_UtlVectorEmbeddedNetworkVar< WeaponPurchaseCount_t >`, `Color`, `ENTITYFUNCPTR`, `HSCRIPT`, `KeyValues3`, `PulseSymbol_t`, `QAngle`, `Quaternion`, `RotationVector`, `SndOpEventGuid_t`, `USEPTR`, `Vector`, `Vector2D`, `Vector4D`, `VectorWS`, `WorldGroupId_t`, `matrix3x4_t`

### Metadata keys (class / field / enum / member)

- `MCustomFGDMetadata`
- `MEntityAllowsPortraitWorldSpawn`
- `MFgdFromSchemaCompletelySkipField`
- `MGetKV3ClassDefaults`
- `MKV3TransferSaveOpsForField`
- `MNotSaved`
- `MPhysPtr`
- `MPropertyAttributeEditor`
- `MPropertyAttributeRange`
- `MPropertyAttributeSuggestionName`
- `MPropertyCustomFGDType`
- `MPropertyDescription`
- `MPropertyEditContextOverrideKey`
- `MPropertyFlattenIntoParentRow`
- `MPropertyFriendlyName`
- `MPropertyGroupName`
- `MPropertyProvidesEditContextString`
- `MPropertyStartGroup`
- `MPropertySuppressBaseClassField`
- `MPulseEditorCanvasItemSpecKV3`
- `MPulseEditorHeaderHelper`
- `MPulseEditorHeaderIcon`
- `MPulseEditorSubHeaderText`
- `MPulseFGDSkipField`
- `MPulseFunctionHiddenInTool`
- `MSaveBehavior`
- `MVDataAssociatedFile`
- `MVDataOverlayType`
- `MVDataRoot`


_Last regenerated against CS2 build `hl2sdk-cs2/5f891c9026230cce0fc0a3fc4b5fef1c467a1385/v1/3d1200e346019c59` (2026-07-09)._
