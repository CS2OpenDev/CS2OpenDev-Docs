# Downstream codegen schemas

Machine-readable schemas for CS2 entity classes, structs, enums, and game
events — projected straight from
[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)'s
per-build artifacts so consumers get one deterministic, provenance-tracked
source instead of a chain of third-party dumps.

## Platform & provenance

Every file here projects **one** `(build, platform)` artifact set:
`windows-x86_64` (CS2 build `24537688`).  The `build_id` (the Steam CS2 game build,
numeric and monotonic) and `platform` are stamped into each schema's header
alongside the walker `revision` and the build timestamps — read them there
rather than assuming.

Windows is the canonical render because it is the superset: it carries the
tool-side modules (`hammer`, `sfm`, `modeldoc_editor`, …) that have no Linux
binaries.  A consumer that assumes Linux would get a silently wrong answer
about which classes exist, so the platform is named explicitly in every
header.  If both platforms are ever published, select by the header's
`platform` field.

## How duplicate class registrations are collapsed

`cs2_schema.json` emits **one record per `(projectName, name)`**, not one per
upstream `(binary-module, name)`.  `projectName` is SchemaTracker's
coarse-grained project axis (`client`, `server`, `entity2`,
`pulse_runtime_lib`, `particleslib`, `animgraphlib`); the finer `module` /
`cppName` from upstream are preserved verbatim on each record.

- A class registered in several binaries that all roll up to the **same**
  `projectName` collapses to a single record.  This dominates the
  `pulse_runtime_lib` cell classes (e.g. `CBasePulseGraphInstance`), which are
  statically linked into many tool binaries but describe one type.
- A name that legitimately appears under **different** `projectName`s — the
  cross-project case such as `CCSPlayerController` in both `client` and
  `server` — keeps one record per project.  So a name appearing more than once
  is expected, and the discriminator is the record's `projectName`.

## Files

- **`cs2_schema.json`** — the entity schema in SchemaTracker's **native**
  shape (`schema_format_version` `2.0`).  Top-level: `generator`, `build_id`,
  `platform`, `revision`, `version_date`, `version_time`, `classes`, `enums`.
  Each class carries `name`, `module` (the binary it lives in), `projectName`,
  `cppName`, `size`, `alignment`, `flags` / `flags2`, `parents[]`, `fields[]`
  (`name`, `offset`, `type`, `typeModule`, `metadata`), and inheritance
  depths; each enum carries `alignment` (underlying integer type) and
  `members[]`.  Integer offsets / sizes are **string-encoded** and type
  `category` values are **UPPERCASE** (`BUILTIN`, `ATOMIC`, `DECLARED_CLASS`,
  `PTR`, `FIXED_ARRAY`, `BITFIELD`, …).  Optional `annotations` blocks layer
  in community-curated descriptions / notes / warnings, and an optional
  `diagram_url` on a class points at its module's UML inheritance diagram.
  Records are keyed by `(projectName, name)` — see [How duplicate class
  registrations are collapsed](#how-duplicate-class-registrations-are-collapsed)
  below.

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

- **`proto/*.proto`** — the build's protobuf definitions as text, copied from
  SchemaTracker (including the vendored `google/protobuf/*` well-knowns) and
  normalised with a single shared
  `option csharp_namespace = "CS2OpenDev.Protobuf";` so C# codegen doesn't
  drop every message into the global namespace (a CS0433 collision hazard).
  Unresolvable (dangling) imports are dropped.  No `package` statement is
  added — the decompiled protos use hundreds of root-qualified (`.Type`)
  cross-references that assume the empty package, so packaging them would break
  resolution.  This is a **per-file reference, not a set that compiles as a
  unit** — see [below](#proto--a-per-file-reference-not-a-compilable-set).
  Most consumers should prefer SchemaTracker's prebuilt `protos.descriptorset`
  (`protoc --descriptor_set_in`, which skips text parsing and import
  resolution entirely); these files are for compiling the protos from source.

- **`field_history.json`** — whole-history evolution of every
  `(class, field)`, projected from SchemaTracker's cumulative
  `schema_evolution.json` (Layer A).  Top-level: `baseline_build`,
  `latest_build`, `transition_count`, `fields` list (each `class` /
  `field` / `firstSeenBuild` / `lastSeenBuild` / `typeHistory`, plus an
  overlay-supplied `confirmedRename` where the community has verified one),
  and `enums`.  Serves alias resolution / forward-back schema migration
  for demo parsers and SDKs.  See the [Schema History](../schema-history.html)
  page for the human-readable break radar.

All six files share a single top-level `schema_format_version` string
that is bumped as a family.  Bump the major when a field is removed or
renamed in any of them; bump the minor when a field is added.
Additive `annotations` blocks do not require a bump.

## Coverage — runtime only

SchemaTracker walks the **shipped CS2 runtime binaries** in-process, so
`cs2_schema.json` covers exactly the schema those binaries register
(`client`, `server`, `entity2`, `pulse_runtime_lib`, `particleslib`,
`animgraphlib`).  The Source 2 editor / tooling schema (hammer, modeldoc,
resourcecompiler, worldrenderer, …) is intentionally **not** present — it
never ships in the game.

## Class records with `size > 0` and no fields

234 classes in `cs2_schema.json` report a non-zero `size` but
expose zero fields.  These are internal Source 2 runtime classes that the
schema system knows the binary size of but never registers field-level
reflection for.  Downstream codegen consumers can safely emit them as
empty classes; field-level layout is not recoverable from the binary.

## Format reference

Full per-key documentation lives in
[`AGENTS.md`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/AGENTS.md#cs2_schemajson-format)
at the repository root.

## `proto/` — a per-file reference, not a compilable set

The `.proto/` directory mirrors SchemaTracker's decompiled protobuf
sources (the vendored `google/protobuf/*` well-knowns are included so
imports resolve).  Because the decompiled files share the **empty**
package, a few global symbols are defined in more than one file, so
`protoc *.proto` over the whole directory fails on a redefinition.
Each collision below is between exactly **two** files; compile any
subset that does not include both files of a listed pair and it
resolves cleanly (the demo/engine closure used by CS2 demo parsers
is one such subset).

**Cross-file symbol collisions** (same global identifier defined in two files — a `protoc` redefinition error):

- message `CMsgProtoBufHeader` — `steammessages.proto`, `steammessages_base.proto`
- enum value `k_EMsgGCSystemMessage` — `base_gcmessages.proto`, `enums_clientserver.proto`

**Dropped unresolved imports** (dangling in the decompile; each is marked with a comment in the file):

- `cs_prediction_events.proto: prediction_events.proto`

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

`bool`, `char`, `float32`, `float64`, `int16`, `int32`, `int8`, `uint16`, `uint32`, `uint64`, `uint8`, `void`

### `atomic` type names

`BASEPTR`, `CAnimGraph2ParamAutoResetOptionalRef`, `CAnimGraph2ParamOptionalRef< CGlobalSymbol >`, `CAnimGraph2ParamOptionalRef< CNmTarget >`, `CAnimGraph2ParamOptionalRef< CTransform >`, `CAnimGraph2ParamOptionalRef< bool >`, `CAnimGraph2ParamOptionalRef< float32 >`, `CAnimNetVar< Vector >`, `CAnimNetVar< bool >`, `CAnimNetVar< float32 >`, `CAnimNetVar< int32 >`, `CAnimNetVar< uint32 >`, `CAnimNetVar< uint64 >`, `CAnimNetVar< uint8 >`, `CAnimScriptParam< float32 >`, `CAnimValue< float32 >`, `CAnimVariant`, `CAttachmentNameSymbolWithStorage`, `CBitVec< 10 >`, `CBufferString`, `CColorGradient`, `CEntityHandle`, `CEntityIndex`, `CEntityNameString`, `CEntityOutputTemplate< CBaseModelEntity::OnDamageLevelChangedArgs_t >`, `CEntityOutputTemplate< CEntityNameString >`, `CEntityOutputTemplate< CHandle< CBaseEntity > >`, `CEntityOutputTemplate< CTestPulseIO::EntityHandleIntArgs_t >`, `CEntityOutputTemplate< CTestPulseIO::EntityNameStringArgs_t >`, `CEntityOutputTemplate< CTestPulseIO::FloatStringArgs_t >`, `CEntityOutputTemplate< CTestPulseIO::ThreeStringArgs_t >`, `CEntityOutputTemplate< CUtlString >`, `CEntityOutputTemplate< CUtlSymbolLarge >`, `CEntityOutputTemplate< CUtlVector< CEntityHandle > >`, `CEntityOutputTemplate< Color >`, `CEntityOutputTemplate< SndOpEventGuid_t >`, `CEntityOutputTemplate< TestInputOutputCombinationsEnum_t >`, `CEntityOutputTemplate< Vector >`, `CEntityOutputTemplate< bool >`, `CEntityOutputTemplate< float32 >`, `CEntityOutputTemplate< int32 >`, `CGameSoundEventName`, `CGlobalSymbol`, `CGlobalSymbolCaseSensitive`, `CHandle< CBaseAnimGraph >`, `CHandle< CBaseEntity >`, `CHandle< CBaseFilter >`, `CHandle< CBaseModelEntity >`, `CHandle< CBasePlayerController >`, `CHandle< CBasePlayerPawn >`, `CHandle< CBasePlayerWeapon >`, `CHandle< CBasePropDoor >`, `CHandle< CBeam >`, `CHandle< CCSObserverPawn >`, `CHandle< CCSPlayerController >`, `CHandle< CCSPlayerPawn >`, `CHandle< CCSPlayerPawnBase >`, `CHandle< CCSWeaponBase >`, `CHandle< CColorCorrection >`, `CHandle< CEconWearable >`, `CHandle< CEntityBlocker >`, `CHandle< CEnvSoundscape >`, `CHandle< CEnvSoundscapeTriggerable >`, `CHandle< CFish >`, `CHandle< CFishPool >`, `CHandle< CFogController >`, `CHandle< CFuncMover >`, `CHandle< CFuncMoverRouter >`, `CHandle< CFuncPlat >`, `CHandle< CFuncShatterglass >`, `CHandle< CFuncTrackTrain >`, `CHandle< CInfoFan >`, `CHandle< CInfoLadderDismount >`, `CHandle< CItemGeneric >`, `CHandle< CItemGenericTriggerHelper >`, `CHandle< CLightEntity >`, `CHandle< CMoverPathNode >`, `CHandle< CPathKeyFrame >`, `CHandle< CPathMover >`, `CHandle< CPathMoverEntitySpawner >`, `CHandle< CPathNode >`, `CHandle< CPathSimple >`, `CHandle< CPathTrack >`, `CHandle< CPathWithDynamicNodes >`, `CHandle< CPlayerPing >`, `CHandle< CPointCamera >`, `CHandle< CPointCommentaryNode >`, `CHandle< CPointPrefab >`, `CHandle< CPostProcessingVolume >`, `CHandle< CSceneEntity >`, `CHandle< CSceneListManager >`, `CHandle< CScriptedSequence >`, `CHandle< CShatterGlassShardPhysics >`, `CHandle< CSkyCamera >`, `CHandle< CSprite >`, `CHandle< CTonemapController2 >`, `CHandle< C_BaseEntity >`, `CHandle< C_BaseModelEntity >`, `CHandle< C_BasePlayerPawn >`, `CHandle< C_BasePlayerWeapon >`, `CHandle< C_BasePropDoor >`, `CHandle< C_CS2HudModelArms >`, `CHandle< C_CSObserverPawn >`, `CHandle< C_CSPlayerPawn >`, `CHandle< C_CSWeaponBase >`, `CHandle< C_ColorCorrection >`, `CHandle< C_EconWearable >`, `CHandle< C_FogController >`, `CHandle< C_InfoLadderDismount >`, `CHandle< C_Multimeter >`, `CHandle< C_PlantedC4 >`, `CHandle< C_PlayerPing >`, `CHandle< C_PointCamera >`, `CHandle< C_PostProcessingVolume >`, `CHandle< C_SkyCamera >`, `CHandle< C_TonemapController2 >`, `CHandle< SpawnPoint >`, `CKV3MemberNameSet`, `CKV3MemberNameWithStorage`, `CModelAnimNameWithDeltas`, `CModelMaterialGroupName`, `CMotionTransform`, `CNetworkUtlVectorBase< CGlobalSymbol >`, `CNetworkUtlVectorBase< CHandle< CBaseAnimGraph > >`, `CNetworkUtlVectorBase< CHandle< CBaseEntity > >`, `CNetworkUtlVectorBase< CHandle< CBaseModelEntity > >`, `CNetworkUtlVectorBase< CHandle< CBasePlayerController > >`, `CNetworkUtlVectorBase< CHandle< CBasePlayerPawn > >`, `CNetworkUtlVectorBase< CHandle< CBasePlayerWeapon > >`, `CNetworkUtlVectorBase< CHandle< CEconWearable > >`, `CNetworkUtlVectorBase< CHandle< CPathNode > >`, `CNetworkUtlVectorBase< CHandle< CPostProcessingVolume > >`, `CNetworkUtlVectorBase< CTransform >`, `CNetworkUtlVectorBase< CUtlString >`, `CNetworkUtlVectorBase< CUtlSymbolLarge >`, `CNetworkUtlVectorBase< QAngle >`, `CNetworkUtlVectorBase< ResourceId_t >`, `CNetworkUtlVectorBase< SoundeventPathCornerPairNetworked_t >`, `CNetworkUtlVectorBase< Vector >`, `CNetworkUtlVectorBase< Vector2D >`, `CNetworkUtlVectorBase< Vector4D >`, `CNetworkUtlVectorBase< bool >`, `CNetworkUtlVectorBase< float32 >`, `CNetworkUtlVectorBase< int32 >`, `CNetworkUtlVectorBase< uint16 >`, `CNetworkUtlVectorBase< uint8 >`, `CNetworkedQuantizedFloat`, `CParticleNamedValueRef`, `CPiecewiseCurve`, `CPlayerSlot`, `CPulseObservableExpression< CUtlString >`, `CPulseObservableExpression< bool >`, `CPulseObservableExpression< float32 >`, `CPulseValueFullType`, `CRelativeArray< CMotionTransform >`, `CRelativeArray< float32 >`, `CResourceArray< CResourcePointer< CResourceString > >`, `CResourceName`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCCompositeMaterialKit > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCNmSkeleton > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCSmartProp > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCTextureBase > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCVDataResource > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeIMaterial2 > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >`, `CResourceNameTyped< CWeakHandle< InfoForResourceTypeVMapResourceData_t > >`, `CResourcePointer< CResourceString >`, `CResourceString`, `CRotation`, `CSmartPropAttributeAngles`, `CSmartPropAttributeBool`, `CSmartPropAttributeColor`, `CSmartPropAttributeFloat`, `CSmartPropAttributeInt`, `CSmartPropAttributeMaterialGroup`, `CSmartPropAttributeMaterialName`, `CSmartPropAttributeModelName`, `CSmartPropAttributeStateName`, `CSmartPropAttributeSurfaceProperty`, `CSmartPropAttributeVariableValue`, `CSmartPropAttributeVector`, `CSmartPropAttributeVector2D`, `CSmartPropVariableComparison`, `CSmartPtr< CAnimActionUpdater >`, `CSmartPtr< CAnimComponentUpdater >`, `CSmartPtr< CAnimConflictBase >`, `CSmartPtr< CAnimGraphDoc_Action >`, `CSmartPtr< CAnimGraphDoc_Blend2DItem >`, `CSmartPtr< CAnimGraphDoc_ClipData >`, `CSmartPtr< CAnimGraphDoc_Component >`, `CSmartPtr< CAnimGraphDoc_Condition >`, `CSmartPtr< CAnimGraphDoc_MotionItem >`, `CSmartPtr< CAnimGraphDoc_MotionItemGroup >`, `CSmartPtr< CAnimGraphDoc_MotionMetric >`, `CSmartPtr< CAnimGraphDoc_MotionParameter >`, `CSmartPtr< CAnimGraphDoc_Motor >`, `CSmartPtr< CAnimGraphDoc_Node >`, `CSmartPtr< CAnimGraphDoc_ParamSpan >`, `CSmartPtr< CAnimGraphDoc_State >`, `CSmartPtr< CAnimGraphDoc_StateTransition >`, `CSmartPtr< CAnimGraphDoc_TagSpan >`, `CSmartPtr< CAnimGraphSettingsGroup >`, `CSmartPtr< CAnimGraphSettingsManager >`, `CSmartPtr< CAnimMotorUpdaterBase >`, `CSmartPtr< CAnimParameterBase >`, `CSmartPtr< CAnimParameterManagerUpdater >`, `CSmartPtr< CAnimReplayFrame >`, `CSmartPtr< CAnimScriptManager >`, `CSmartPtr< CAnimSkeleton >`, `CSmartPtr< CAnimTagBase >`, `CSmartPtr< CAnimTagManagerUpdater >`, `CSmartPtr< CAnimUpdateNodeBase >`, `CSmartPtr< CAnimUpdateSharedData >`, `CSmartPtr< CMotionGraph >`, `CSmartPtr< CMotionMetricEvaluator >`, `CSmartPtr< CMotionNode >`, `CSmartPtr< CStaticPoseCacheBuilder >`, `CSoundEventName`, `CSplitScreenSlot`, `CSteamAudioMovableBakedData< CSteamAudioBakedDimensionsData >`, `CSteamAudioMovableBakedData< CSteamAudioBakedPathingData >`, `CSteamAudioMovableBakedData< CSteamAudioBakedReverbData >`, `CStrongHandle< InfoForResourceTypeCAnimData >`, `CStrongHandle< InfoForResourceTypeCAnimationGroup >`, `CStrongHandle< InfoForResourceTypeCChoreoSceneResource >`, `CStrongHandle< InfoForResourceTypeCModel >`, `CStrongHandle< InfoForResourceTypeCNmClip >`, `CStrongHandle< InfoForResourceTypeCNmGraphDefinition >`, `CStrongHandle< InfoForResourceTypeCNmSkeleton >`, `CStrongHandle< InfoForResourceTypeCPhysAggregateData >`, `CStrongHandle< InfoForResourceTypeCPostProcessingResource >`, `CStrongHandle< InfoForResourceTypeCRenderMesh >`, `CStrongHandle< InfoForResourceTypeCSequenceGroupData >`, `CStrongHandle< InfoForResourceTypeCSmartProp >`, `CStrongHandle< InfoForResourceTypeCTextureBase >`, `CStrongHandle< InfoForResourceTypeCVMixListResource >`, `CStrongHandle< InfoForResourceTypeCVoiceContainerBase >`, `CStrongHandle< InfoForResourceTypeIMaterial2 >`, `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`, `CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >`, `CStrongHandle< InfoForResourceTypeIPulseGraphDef >`, `CStrongHandle< InfoForResourceTypeManifestTestResource_t >`, `CStrongHandleCopyable< InfoForResourceTypeCEntityLump >`, `CStrongHandleCopyable< InfoForResourceTypeIMaterial2 >`, `CStrongHandleVoid`, `CTransform`, `CTransformWS`, `CTypedBitVec< 64 >`, `CUtlBinaryBlock`, `CUtlDict< CPhysicsBodyGameMarkup >`, `CUtlDict< GameTime_t >`, `CUtlHashtable< AnimNodeID, CSmartPtr< CAnimGraphDoc_Node > >`, `CUtlHashtable< AnimNodeOutputID, CAnimGraphDoc_NodeConnection >`, `CUtlHashtable< AnimParamID, int32 >`, `CUtlHashtable< CAnimNodePath, int32 >`, `CUtlHashtable< CAnimParamHandle, int16 >`, `CUtlHashtable< CHandle< CFuncMover >, PathMoverEntitySpawn >`, `CUtlHashtable< CUtlString, CSmartPtr< CAnimGraphDoc_ClipData > >`, `CUtlHashtable< CUtlString, CUtlString >`, `CUtlHashtable< CUtlString, int32 >`, `CUtlHashtable< CUtlStringToken, int32 >`, `CUtlHashtable< PulseCursorID_t, int32 >`, `CUtlHashtable< uint16, int16 >`, `CUtlLeanVector< AABB_t >`, `CUtlLeanVector< CAudioSentence >`, `CUtlLeanVector< CBaseConstraint* >`, `CUtlLeanVector< CConstraintSlave >`, `CUtlLeanVector< CDebugSnapshotData_t >`, `CUtlLeanVector< CGlobalSymbol >`, `CUtlLeanVector< CMaterialDrawDescriptor >`, `CUtlLeanVector< CMaterialDrawDescriptor::RigidMeshPart_t >`, `CUtlLeanVector< CMeshletDescriptor >`, `CUtlLeanVector< CNmBoneWeightList >`, `CUtlLeanVector< CNmClipDocEventTrack >`, `CUtlLeanVector< CNmFloatChannelSet_t >`, `CUtlLeanVector< CNmGraphDocument::DebugParameterSet_t >`, `CUtlLeanVector< CNmSkeleton::SecondarySkeleton_t >`, `CUtlLeanVector< CPAssignment_t >`, `CUtlLeanVector< CPulseRuntimeMethodArg >`, `CUtlLeanVector< CPulse_InstructionDebug >`, `CUtlLeanVector< CPulse_RegisterInfo >`, `CUtlLeanVector< CSceneObjectData::RTProxyDrawDescriptor_t >`, `CUtlLeanVector< CUtlString >`, `CUtlLeanVector< Color >`, `CUtlLeanVector< DestructiblePartDamageRequest_t >`, `CUtlLeanVector< EntityKeyValueData_t >`, `CUtlLeanVector< FloatInputMaterialVariable_t >`, `CUtlLeanVector< NmBoneMaskSetDefinition_t >`, `CUtlLeanVector< PGDInstruction_t >`, `CUtlLeanVector< TextureGroup_t >`, `CUtlLeanVector< VecInputMaterialVariable_t >`, `CUtlLeanVector< Vector4D >`, `CUtlLeanVector< bool >`, `CUtlLeanVector< float32 >`, `CUtlLeanVector< float64 >`, `CUtlLeanVector< std::pair< CGlobalSymbol, CGlobalSymbol > >`, `CUtlLeanVector< std::pair< CGlobalSymbol, CNmTarget > >`, `CUtlLeanVector< std::pair< CGlobalSymbol, Vector > >`, `CUtlLeanVector< std::pair< CGlobalSymbol, bool > >`, `CUtlLeanVector< std::pair< CGlobalSymbol, float32 > >`, `CUtlLeanVector< uint16 >`, `CUtlLeanVector< uint64 >`, `CUtlLeanVectorFixedGrowable< CGlobalSymbol, 3 >`, `CUtlLeanVectorFixedGrowable< CGlobalSymbol, 4 >`, `CUtlLeanVectorFixedGrowable< CGlobalSymbol, 5 >`, `CUtlLeanVectorFixedGrowable< CGlobalSymbol, 7 >`, `CUtlLeanVectorFixedGrowable< CNmLayerBlendNode::LayerDefinition_t, 3 >`, `CUtlLeanVectorFixedGrowable< CNmParameterizedBlendNode::BlendRange_t, 5 >`, `CUtlLeanVectorFixedGrowable< CNmStateMachineNode::StateDefinition_t, 5 >`, `CUtlLeanVectorFixedGrowable< CNmStateMachineNode::TransitionDefinition_t, 5 >`, `CUtlLeanVectorFixedGrowable< CNmStateNode::TimedEvent_t, 1 >`, `CUtlLeanVectorFixedGrowable< CNmSyncTrack::Event_t, 10 >`, `CUtlLeanVectorFixedGrowable< CSceneObjectData, 1 >`, `CUtlLeanVectorFixedGrowable< NmGraphDocPin_t, 1 >`, `CUtlLeanVectorFixedGrowable< NmGraphDocPin_t, 4 >`, `CUtlLeanVectorFixedGrowable< Vector, 8 >`, `CUtlLeanVectorFixedGrowable< Vector2D, 10 >`, `CUtlLeanVectorFixedGrowable< float32, 5 >`, `CUtlLeanVectorFixedGrowable< int16, 4 >`, `CUtlLeanVectorFixedGrowable< int16, 5 >`, `CUtlLeanVectorFixedGrowable< int16, 8 >`, `CUtlLeanVectorFixedGrowable< uint8, 10 >`, `CUtlLeanVectorFixedGrowable< uint8, 30 >`, `CUtlLeanVectorFixedGrowable< uint8, 8 >`, `CUtlOrderedMap< CGlobalSymbol, int32 >`, `CUtlOrderedMap< CUtlStringTokenNoRegistration, Attribute_t >`, `CUtlOrderedMap< CUtlStringTokenNoRegistration, CUtlString >`, `CUtlOrderedMap< HitGroup_t, CDestructiblePart >`, `CUtlOrderedMap< PulseCursorID_t, PulseGraphExecutionHistoryCursorDesc_t* >`, `CUtlOrderedMap< PulseDocNodeID_t, PulseGraphExecutionHistoryNodeDesc_t* >`, `CUtlOrderedMap< WeaponSound_t, CSoundEventName >`, `CUtlString`, `CUtlStringMap< CMotionAnalysisSettings_Foot >`, `CUtlStringMap< CTextureSheetDoc_Sequence* >`, `CUtlStringToken`, `CUtlStringTokenNoRegistration`, `CUtlStringTokenWithStorage`, `CUtlSymbol`, `CUtlSymbolLarge`, `CUtlVector< AI_DefaultNPC_DebugSnapshotData_t::PathQuery_t >`, `CUtlVector< AI_GroundRootMotionMotor_DebugSnapshotData_t::Event_t >`, `CUtlVector< AI_MotorServices_DebugSnapshotData_t::MotorPathWaypoint_t >`, `CUtlVector< AI_Navigator_DebugSnapshotData_t::Waypoint_t >`, `CUtlVector< ActorMapping_t >`, `CUtlVector< AggregateInstanceStreamOnDiskData_t >`, `CUtlVector< AggregateLODSetup_t >`, `CUtlVector< AggregateMeshInfo_t >`, `CUtlVector< AggregateRTProxySceneObject_t >`, `CUtlVector< AggregateSceneObject_t >`, `CUtlVector< AggregateVertexAlbedoStreamOnDiskData_t >`, `CUtlVector< AggregateVertexEmissiveStreamOnDiskData_t >`, `CUtlVector< AnimTagID >`, `CUtlVector< AnimationDecodeDebugDumpElement_t >`, `CUtlVector< AssetEngineCommand_t >`, `CUtlVector< AutoRoomDoorwayPairs_t >`, `CUtlVector< BakedLightingInfo_t::BakedShadowAssignment_t >`, `CUtlVector< BlendItem_t >`, `CUtlVector< BoneDemoCaptureSettings_t >`, `CUtlVector< CAI_Expresser* >`, `CUtlVector< CAnimActivity >`, `CUtlVector< CAnimBone >`, `CUtlVector< CAnimBoneDifference >`, `CUtlVector< CAnimDataChannelDesc >`, `CUtlVector< CAnimDecoder >`, `CUtlVector< CAnimDesc >`, `CUtlVector< CAnimEventDefinition >`, `CUtlVector< CAnimFoot >`, `CUtlVector< CAnimFrameBlockAnim >`, `CUtlVector< CAnimFrameSegment >`, `CUtlVector< CAnimGraphControllerBase* >`, `CUtlVector< CAnimGraphDoc_AimCameraNode_PropJoint >`, `CUtlVector< CAnimGraphDoc_Node* >`, `CUtlVector< CAnimGraphDoc_NodeConnection >`, `CUtlVector< CAnimGraphDoc_ParamSpanSample >`, `CUtlVector< CAnimGraphDoc_RigidBodyWeightList >`, `CUtlVector< CAnimGraphDoc_State* >`, `CUtlVector< CAnimLocalHierarchy >`, `CUtlVector< CAnimMorphDifference >`, `CUtlVector< CAnimMovement >`, `CUtlVector< CAnimNodePath >`, `CUtlVector< CAnimParamHandle >`, `CUtlVector< CAnimUpdateNodeRef >`, `CUtlVector< CAnimUser >`, `CUtlVector< CAnimUserDifference >`, `CUtlVector< CAssetWarning* >`, `CUtlVector< CAssetWarningCheck >`, `CUtlVector< CAttributeManager::cached_attribute_float_t >`, `CUtlVector< CAudioEmphasisSample >`, `CUtlVector< CAudioPhonemeTag >`, `CUtlVector< CBaseIssue* >`, `CUtlVector< CBlendNodeChild >`, `CUtlVector< CBodyGroupSetting >`, `CUtlVector< CBoneConstraintPoseSpaceBone::Input_t >`, `CUtlVector< CBoneConstraintPoseSpaceMorph::Input_t >`, `CUtlVector< CBufferString >`, `CUtlVector< CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t >`, `CUtlVector< CCachedPose >`, `CUtlVector< CChoiceNodeChild >`, `CUtlVector< CColorCorrectionLayer* >`, `CUtlVector< CConnectionProxyItem >`, `CUtlVector< CConstraintTarget >`, `CUtlVector< CDSPMixgroupModifier >`, `CUtlVector< CDampedValueItem >`, `CUtlVector< CDampedValueUpdateItem >`, `CUtlVector< CDebugDrawHistoryData* >`, `CUtlVector< CDestructiblePart_DamageLevel >`, `CUtlVector< CDetailPropModel >`, `CUtlVector< CDirectPlaybackTagData >`, `CUtlVector< CDspPresetModifierList >`, `CUtlVector< CEngineToolInfo >`, `CUtlVector< CEntityHandle >`, `CUtlVector< CEntityIndex >`, `CUtlVector< CExternalToolInfo >`, `CUtlVector< CFeIndexedJiggleBone >`, `CUtlVector< CFish* >`, `CUtlVector< CFlexController >`, `CUtlVector< CFlexDesc >`, `CUtlVector< CFlexOp >`, `CUtlVector< CFlexRule >`, `CUtlVector< CFootLockItem >`, `CUtlVector< CFootMotion >`, `CUtlVector< CFootPinningItem >`, `CUtlVector< CFootStepTriggerItem >`, `CUtlVector< CFootStride >`, `CUtlVector< CFootTrajectory >`, `CUtlVector< CGlobalSymbol >`, `CUtlVector< CHandle< CBaseEntity > >`, `CUtlVector< CHandle< CBaseModelEntity > >`, `CUtlVector< CHandle< CBasePlayerController > >`, `CUtlVector< CHandle< CBasePlayerPawn > >`, `CUtlVector< CHandle< CBasePropDoor > >`, `CUtlVector< CHandle< CEnvSoundscapeTriggerable > >`, `CUtlVector< CHandle< CFish > >`, `CUtlVector< CHandle< CFuncMover > >`, `CUtlVector< CHandle< CInfoLadderDismount > >`, `CUtlVector< CHandle< CLightEntity > >`, `CUtlVector< CHandle< CPathMoverEntitySpawner > >`, `CUtlVector< CHandle< CPointCommentaryNode > >`, `CUtlVector< CHandle< CSceneEntity > >`, `CUtlVector< CHandle< CSceneListManager > >`, `CUtlVector< CHandle< C_BaseEntity > >`, `CUtlVector< CHandle< C_BaseModelEntity > >`, `CUtlVector< CHandle< C_InfoLadderDismount > >`, `CUtlVector< CHandle< SpawnPoint > >`, `CUtlVector< CHintMessage* >`, `CUtlVector< CHitBox >`, `CUtlVector< CHitBoxSet >`, `CUtlVector< CInfoChoreoAnchorPosition >`, `CUtlVector< CJiggleBoneItem >`, `CUtlVector< CLightRigPointLight >`, `CUtlVector< CLightRigSpotLight >`, `CUtlVector< CLightRigSunLight >`, `CUtlVector< CManifestInfo >`, `CUtlVector< CModelConfig* >`, `CUtlVector< CModelConfigElement* >`, `CUtlVector< CMorphBundleData >`, `CUtlVector< CMorphData >`, `CUtlVector< CMorphRectData >`, `CUtlVector< CMotionGraphConfig >`, `CUtlVector< CMotionGraphGroup >`, `CUtlVector< CMotionSearchNode* >`, `CUtlVector< CNmBlendSpace1D::Point_t >`, `CUtlVector< CNmClip::ModelSpaceSamplingChainLink_t >`, `CUtlVector< CNmClipDocEvent* >`, `CUtlVector< CNmFloatChannelData::ChannelSettings_t >`, `CUtlVector< CNmFloatChannelSet_t >`, `CUtlVector< CNmGraphDefinition::ExternalGraphSlot_t >`, `CUtlVector< CNmGraphDefinition::ExternalPoseSlot_t >`, `CUtlVector< CNmGraphDefinition::ReferencedGraphSlot_t >`, `CUtlVector< CNmGraphDocDataDictionary::IDSet_t >`, `CUtlVector< CNmGraphDocDataDictionary::ParameterSet_t >`, `CUtlVector< CNmGraphDocDataDictionary::Parameter_t >`, `CUtlVector< CNmGraphDocFloatSelectorNode::Option_t >`, `CUtlVector< CNmGraphDocFlowGraph::Connection_t >`, `CUtlVector< CNmGraphDocGraphEventConditionNode::Condition_t >`, `CUtlVector< CNmGraphDocIDToFloatNode::Mapping_t >`, `CUtlVector< CNmGraphDocNode* >`, `CUtlVector< CNmGraphDocStateNode::StateEvent_t >`, `CUtlVector< CNmGraphDocStateNode::TimedStateEvent_t >`, `CUtlVector< CNmGraphDocVariationDataNode::OverrideValue_t >`, `CUtlVector< CNmPreviewArchetype::SecondarySkeleton_t >`, `CUtlVector< CNmSkeletonDocument::SecondarySkeleton_t >`, `CUtlVector< CParticleFunctionConstraint* >`, `CUtlVector< CParticleFunctionEmitter* >`, `CUtlVector< CParticleFunctionForce* >`, `CUtlVector< CParticleFunctionInitializer* >`, `CUtlVector< CParticleFunctionOperator* >`, `CUtlVector< CParticleFunctionPreEmission* >`, `CUtlVector< CParticleFunctionRenderer* >`, `CUtlVector< CPhysSurfaceProperties* >`, `CUtlVector< CPlayerSlot >`, `CUtlVector< CPreviewEntry >`, `CUtlVector< CPulseCell_Base* >`, `CUtlVector< CPulseCell_Outflow_PlayVCD::VCDRequirementInfo_t >`, `CUtlVector< CPulseCell_Timeline::TimelineEvent_t >`, `CUtlVector< CPulse_BlackboardReference >`, `CUtlVector< CPulse_CallInfo* >`, `CUtlVector< CPulse_Chunk* >`, `CUtlVector< CPulse_Constant >`, `CUtlVector< CPulse_DomainValue >`, `CUtlVector< CPulse_InvokeBinding* >`, `CUtlVector< CPulse_OutflowConnection >`, `CUtlVector< CPulse_OutputConnection* >`, `CUtlVector< CPulse_PublicOutput >`, `CUtlVector< CPulse_Variable >`, `CUtlVector< CRemapValueItem >`, `CUtlVector< CRemapValueUpdateItem >`, `CUtlVector< CResourceNameTyped< CWeakHandle< InfoForResourceTypeCCompositeMaterialKit > > >`, `CUtlVector< CRigidBodyWeight >`, `CUtlVector< CSSDSEndFrameViewInfo >`, `CUtlVector< CSSDSMsg_ViewTarget >`, `CUtlVector< CSelectableSubgraph >`, `CUtlVector< CSeqAutoLayer >`, `CUtlVector< CSeqBoneMaskList >`, `CUtlVector< CSeqCmdLayer >`, `CUtlVector< CSeqCmdSeqDesc >`, `CUtlVector< CSeqIKLock >`, `CUtlVector< CSeqPoseParamDesc >`, `CUtlVector< CSeqPoseSetting >`, `CUtlVector< CSeqS1SeqDesc >`, `CUtlVector< CSeqScaleSet >`, `CUtlVector< CSeqSynthAnimDesc >`, `CUtlVector< CSimpleAssetTypeInfo* >`, `CUtlVector< CSmartPropAttributeVariableValue >`, `CUtlVector< CSmartPropAttributeVector >`, `CUtlVector< CSmartPropChoice* >`, `CUtlVector< CSmartPropChoiceOption >`, `CUtlVector< CSmartPropElement* >`, `CUtlVector< CSmartPropMaterialReplacement >`, `CUtlVector< CSmartPropModifier* >`, `CUtlVector< CSmartPropSelectionCriteria* >`, `CUtlVector< CSmartPropVariable* >`, `CUtlVector< CSmartPtr< CAnimActionUpdater > >`, `CUtlVector< CSmartPtr< CAnimComponentUpdater > >`, `CUtlVector< CSmartPtr< CAnimConflictBase > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_Action > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_Blend2DItem > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_Component > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_Condition > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_MotionItem > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_MotionItemGroup > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_MotionMetric > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_MotionParameter > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_Motor > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_ParamSpan > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_State > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_StateTransition > >`, `CUtlVector< CSmartPtr< CAnimGraphDoc_TagSpan > >`, `CUtlVector< CSmartPtr< CAnimGraphSettingsGroup > >`, `CUtlVector< CSmartPtr< CAnimMotorUpdaterBase > >`, `CUtlVector< CSmartPtr< CAnimParameterBase > >`, `CUtlVector< CSmartPtr< CAnimReplayFrame > >`, `CUtlVector< CSmartPtr< CAnimTagBase > >`, `CUtlVector< CSmartPtr< CAnimUpdateNodeBase > >`, `CUtlVector< CSmartPtr< CMotionGraph > >`, `CUtlVector< CSmartPtr< CMotionMetricEvaluator > >`, `CUtlVector< CSndBeatPattern >`, `CUtlVector< CSndBeatTrack >`, `CUtlVector< CSolveIKChainAnimNodeChainData >`, `CUtlVector< CSolveIKTargetHandle_t >`, `CUtlVector< CSosGroupActionSchema* >`, `CUtlVector< CSoundContainerReference >`, `CUtlVector< CSprayedDataPresetElement >`, `CUtlVector< CStateAction >`, `CUtlVector< CStateActionUpdater >`, `CUtlVector< CStateNodeStateData >`, `CUtlVector< CStateNodeTransitionData >`, `CUtlVector< CStateUpdateData >`, `CUtlVector< CSteamAudioAmbisonicsField >`, `CUtlVector< CSteamAudioProbeLineSegment >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCAnimData > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCAnimationGroup > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCModel > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCNmSkeleton > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCPhysAggregateData > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCRenderMesh > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCSequenceGroupData > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCTextureBase > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeCVoiceContainerBase > >`, `CUtlVector< CStrongHandle< InfoForResourceTypeIMaterial2 > >`, `CUtlVector< CStrongHandleCopyable< InfoForResourceTypeCEntityLump > >`, `CUtlVector< CStrongHandleVoid >`, `CUtlVector< CSubassetTypeInfo* >`, `CUtlVector< CTargetSelectorChild >`, `CUtlVector< CTextureSheetDoc_Frame >`, `CUtlVector< CTransform >`, `CUtlVector< CTransitionUpdateData >`, `CUtlVector< CUtlBinaryBlock >`, `CUtlVector< CUtlString >`, `CUtlVector< CUtlSymbolLarge >`, `CUtlVector< CUtlVector< SampleCode > >`, `CUtlVector< CUtlVector< float32 > >`, `CUtlVector< CUtlVector< int32 > >`, `CUtlVector< CVMixEditorEdge >`, `CUtlVector< CVMixEditorNode >`, `CUtlVector< CVectorQuantizer >`, `CUtlVector< CVoiceContainerBase* >`, `CUtlVector< CVoiceContainerSetElement >`, `CUtlVector< CVoiceContainerStaticAdditiveSynth::CHarmonic >`, `CUtlVector< CVoiceContainerStaticAdditiveSynth::CTone >`, `CUtlVector< C_BulletHitModel* >`, `CUtlVector< C_EconEntity::AttachedModelData_t >`, `CUtlVector< C_SceneEntity::QueuedEvents_t >`, `CUtlVector< ChainToSolveData_t >`, `CUtlVector< ClutterSceneObject_t >`, `CUtlVector< ClutterTile_t >`, `CUtlVector< CollisionDetailLayerInfo_t::Name_t >`, `CUtlVector< Color >`, `CUtlVector< ColorChoice_t >`, `CUtlVector< CompMatMutatorCondition_t >`, `CUtlVector< CompMatPropertyMutator_t >`, `CUtlVector< CompositeMaterialAssemblyProcedure_t >`, `CUtlVector< CompositeMaterialEditorPoint_t >`, `CUtlVector< CompositeMaterialInputContainer_t >`, `CUtlVector< CompositeMaterialInputLooseVariable_t >`, `CUtlVector< CompositeMaterialMatchFilter_t >`, `CUtlVector< CompositeMaterial_t >`, `CUtlVector< ConstantInfo_t >`, `CUtlVector< DecalGroupOption_t >`, `CUtlVector< DynamicVolumeDef_t >`, `CUtlVector< EMaterialLayer_t >`, `CUtlVector< EMaterialVariable_t >`, `CUtlVector< EntityIOConnectionData_t >`, `CUtlVector< ExtraVertexStreamOverride_t >`, `CUtlVector< FeAnimStrayRadius_t >`, `CUtlVector< FeAntiTunnelProbe_t >`, `CUtlVector< FeAxialEdgeBend_t >`, `CUtlVector< FeBoneMergeLink_t >`, `CUtlVector< FeBoxRigid_t >`, `CUtlVector< FeCollisionPlane_t >`, `CUtlVector< FeCtrlOffset_t >`, `CUtlVector< FeCtrlOsOffset_t >`, `CUtlVector< FeCtrlSoftOffset_t >`, `CUtlVector< FeDynKinLink_t >`, `CUtlVector< FeEffectDesc_t >`, `CUtlVector< FeFitMatrix_t >`, `CUtlVector< FeFitWeight_t >`, `CUtlVector< FeFollowNode_t >`, `CUtlVector< FeHingeLimit_t >`, `CUtlVector< FeKelagerBend2_t >`, `CUtlVector< FeModelSelfCollisionLayer_t >`, `CUtlVector< FeMorphLayerDepr_t >`, `CUtlVector< FeNodeBase_t >`, `CUtlVector< FeNodeIntegrator_t >`, `CUtlVector< FeNodeReverseOffset_t >`, `CUtlVector< FeNodeStrayBox_t >`, `CUtlVector< FeNodeWindBase_t >`, `CUtlVector< FeQuad_t >`, `CUtlVector< FeRigidColliderIndices_t >`, `CUtlVector< FeRodConstraint_t >`, `CUtlVector< FeSDFRigid_t >`, `CUtlVector< FeSimdAnimStrayRadius_t >`, `CUtlVector< FeSimdNodeBase_t >`, `CUtlVector< FeSimdQuad_t >`, `CUtlVector< FeSimdRodConstraintAnim_t >`, `CUtlVector< FeSimdRodConstraint_t >`, `CUtlVector< FeSimdSpringIntegrator_t >`, `CUtlVector< FeSimdTri_t >`, `CUtlVector< FeSphereRigid_t >`, `CUtlVector< FeSpringIntegrator_t >`, `CUtlVector< FeTaperedCapsuleRigid_t >`, `CUtlVector< FeTaperedCapsuleStretch_t >`, `CUtlVector< FeTreeChildren_t >`, `CUtlVector< FeTri_t >`, `CUtlVector< FeTwistConstraint_t >`, `CUtlVector< FeVertexMapBuild_t* >`, `CUtlVector< FeVertexMapDesc_t >`, `CUtlVector< FeWorldCollisionParams_t >`, `CUtlVector< FootFixedData_t >`, `CUtlVector< FootFixedSettings >`, `CUtlVector< FootStepTrigger >`, `CUtlVector< FunctionInfo_t >`, `CUtlVector< FuseVariableIndex_t >`, `CUtlVector< GeneratedTextureHandle_t >`, `CUtlVector< HSequence >`, `CUtlVector< HitGroup_t >`, `CUtlVector< IKDemoCaptureSettings_t >`, `CUtlVector< INavObstacle* >`, `CUtlVector< JiggleBoneSettings_t >`, `CUtlVector< LookAtBone_t >`, `CUtlVector< MaterialGroupChoice_t >`, `CUtlVector< MaterialGroup_t >`, `CUtlVector< MaterialOverride_t >`, `CUtlVector< MaterialParamBuffer_t >`, `CUtlVector< MaterialParamFloat_t >`, `CUtlVector< MaterialParamInt_t >`, `CUtlVector< MaterialParamString_t >`, `CUtlVector< MaterialParamTexture_t >`, `CUtlVector< MaterialParamVector_t >`, `CUtlVector< MaterialVariable_t >`, `CUtlVector< ModelAnimGraph2Ref_t >`, `CUtlVector< ModelBoneFlexDriverControl_t >`, `CUtlVector< ModelBoneFlexDriver_t >`, `CUtlVector< ModelMeshBufferData_t >`, `CUtlVector< ModelReference_t >`, `CUtlVector< MoodAnimationLayer_t >`, `CUtlVector< MoodAnimation_t >`, `CUtlVector< MorphBundleType_t >`, `CUtlVector< MotionBlendItem >`, `CUtlVector< MotionDBIndex >`, `CUtlVector< NmBoneMaskSetDefinition_t >`, `CUtlVector< NmCompressionSettings_t >`, `CUtlVector< NmVariation_t >`, `CUtlVector< NodeData_t >`, `CUtlVector< OutflowWithRequirements_t >`, `CUtlVector< ParamSpanSample_t >`, `CUtlVector< ParamSpan_t >`, `CUtlVector< ParticleChildrenInfo_t >`, `CUtlVector< ParticleControlPointConfiguration_t >`, `CUtlVector< ParticleControlPointDriver_t >`, `CUtlVector< ParticleMultiSegmentSpecialCharacter_t >`, `CUtlVector< ParticleNamedValueSource_t* >`, `CUtlVector< ParticlePreviewBodyGroup_t >`, `CUtlVector< PermModelDataAnimatedMaterialAttribute_t >`, `CUtlVector< PermModelExtPart_t >`, `CUtlVector< PhysShapeMarkup_t >`, `CUtlVector< PointDefinitionWithTimeValues_t >`, `CUtlVector< PointDefinition_t >`, `CUtlVector< PulseCursorID_t >`, `CUtlVector< PulseDocNodeID_t >`, `CUtlVector< PulseGraphExecutionHistoryEntry_t* >`, `CUtlVector< PulseNodeDynamicOutflows_t::DynamicOutflow_t >`, `CUtlVector< PulseScriptedSequenceData_t >`, `CUtlVector< Quaternion >`, `CUtlVector< QuaternionStorage >`, `CUtlVector< RTProxyBLAS_t >`, `CUtlVector< RTProxyInstanceInfo_t >`, `CUtlVector< RelationshipOverride_t >`, `CUtlVector< RenderHairStrandInfo_t >`, `CUtlVector< RenderInputLayoutField_t >`, `CUtlVector< RenderProjectedMaterial_t >`, `CUtlVector< RenderSkeletonBone_t >`, `CUtlVector< ResourceBlockTypeInfo_t >`, `CUtlVector< ResponseContext_t >`, `CUtlVector< RnCapsuleDesc_t >`, `CUtlVector< RnCapsule_t >`, `CUtlVector< RnFace_t >`, `CUtlVector< RnHalfEdge_t >`, `CUtlVector< RnHullDesc_t >`, `CUtlVector< RnHull_t >`, `CUtlVector< RnMeshDesc_t >`, `CUtlVector< RnMesh_t >`, `CUtlVector< RnNode_t >`, `CUtlVector< RnPlane_t >`, `CUtlVector< RnSoftbodyCapsule_t >`, `CUtlVector< RnSoftbodyParticle_t >`, `CUtlVector< RnSoftbodySpring_t >`, `CUtlVector< RnSphereDesc_t >`, `CUtlVector< RnSphere_t >`, `CUtlVector< RnTriangle_t >`, `CUtlVector< RnVertex_t >`, `CUtlVector< RnWing_t >`, `CUtlVector< SampleCode >`, `CUtlVector< SceneObject_t >`, `CUtlVector< ScriptInfo_t >`, `CUtlVector< SequenceWeightedList_t >`, `CUtlVector< SkeletonAnimCapture_t* >`, `CUtlVector< SkeletonAnimCapture_t::Bone_t >`, `CUtlVector< SkeletonAnimCapture_t::Camera_t >`, `CUtlVector< SkeletonAnimCapture_t::Frame_t >`, `CUtlVector< SndBeatEventKeyedFloats_t >`, `CUtlVector< SndBeatEventKeyedMidiNotes_t >`, `CUtlVector< SndBeatEventKeyedSndEvts_t >`, `CUtlVector< SndBeatEventKeys_t >`, `CUtlVector< SosEditItemInfo_t >`, `CUtlVector< SoundOpvarTraceResult_t >`, `CUtlVector< StanceInfo_t >`, `CUtlVector< SummaryTakeDamageInfo_t* >`, `CUtlVector< TagSpan_t >`, `CUtlVector< VPhysXBodyPart_t >`, `CUtlVector< VPhysXCollisionAttributes_t >`, `CUtlVector< VPhysXConstraint2_t >`, `CUtlVector< VPhysXJoint_t >`, `CUtlVector< V_uuid_t >`, `CUtlVector< VariableInfo_t >`, `CUtlVector< Vector >`, `CUtlVector< Vector2D >`, `CUtlVector< Vector4D >`, `CUtlVector< VectorAligned >`, `CUtlVector< VectorWS >`, `CUtlVector< VsInputSignatureElement_t >`, `CUtlVector< WeightList >`, `CUtlVector< WorldNodeOnDiskBufferData_t >`, `CUtlVector< char* >`, `CUtlVector< float32 >`, `CUtlVector< globalentity_t >`, `CUtlVector< int16 >`, `CUtlVector< int32 >`, `CUtlVector< int8 >`, `CUtlVector< lerpdata_t >`, `CUtlVector< magnetted_objects_t >`, `CUtlVector< matrix3x4_t >`, `CUtlVector< matrix3x4a_t >`, `CUtlVector< modifiedconvars_t >`, `CUtlVector< ragdollelement_t >`, `CUtlVector< ragdollhierarchyjoint_t >`, `CUtlVector< sndopvarlatchdata_t >`, `CUtlVector< std::pair< CAnimParamHandle, CAnimVariant > >`, `CUtlVector< std::pair< CBufferString, float32 > >`, `CUtlVector< std::pair< CUtlString, CUtlString > >`, `CUtlVector< std::pair< CUtlString, uint32 > >`, `CUtlVector< thinkfunc_t >`, `CUtlVector< uint16 >`, `CUtlVector< uint32 >`, `CUtlVector< uint64 >`, `CUtlVector< uint8 >`, `CUtlVectorEmbeddedNetworkVar< AnimGraph2SerializedPoseRecipeSlot_t >`, `CUtlVectorEmbeddedNetworkVar< CDamageRecord >`, `CUtlVectorEmbeddedNetworkVar< CEconItemAttribute >`, `CUtlVectorEmbeddedNetworkVar< CSPerRoundStats_t >`, `CUtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >`, `CUtlVectorEmbeddedNetworkVar< SellbackPurchaseEntry_t >`, `CUtlVectorEmbeddedNetworkVar< ServerAuthoritativeWeaponSlot_t >`, `CUtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >`, `CUtlVectorEmbeddedNetworkVar< WeaponPurchaseCount_t >`, `CUtlVectorFixedGrowable< CGlobalSymbol, 2 >`, `CUtlVectorFixedGrowable< CGlobalSymbol, 5 >`, `CUtlVectorFixedGrowable< CNmClip*, 1 >`, `CUtlVectorFixedGrowable< CNmFloatChannelData*, 2 >`, `CUtlVectorFixedGrowable< CNmGraphEventConditionNode::Condition_t, 5 >`, `CUtlVectorFixedGrowable< CTransform, 128 >`, `CUtlVectorFixedGrowable< float32, 5 >`, `CUtlVectorFixedGrowable< uint8, 8 >`, `CUtlVectorSIMDPaddedVector`, `CVariantBase< CVariantDefaultAllocator >`, `CWeakHandle< InfoForResourceTypeCCompositeMaterialKit >`, `CWeakHandle< InfoForResourceTypeCModel >`, `CWeakHandle< InfoForResourceTypeCNmSkeleton >`, `CWeakHandle< InfoForResourceTypeCSmartProp >`, `CWeakHandle< InfoForResourceTypeCTextureBase >`, `CWeakHandle< InfoForResourceTypeCVDataResource >`, `CWeakHandle< InfoForResourceTypeIMaterial2 >`, `CWeakHandle< InfoForResourceTypeIParticleSystemDefinition >`, `CWeakHandle< InfoForResourceTypeVMapResourceData_t >`, `C_NetworkUtlVectorBase< CGlobalSymbol >`, `C_NetworkUtlVectorBase< CHandle< CBaseAnimGraph > >`, `C_NetworkUtlVectorBase< CHandle< CBasePlayerController > >`, `C_NetworkUtlVectorBase< CHandle< CPathNode > >`, `C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >`, `C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >`, `C_NetworkUtlVectorBase< CHandle< C_BasePlayerPawn > >`, `C_NetworkUtlVectorBase< CHandle< C_BasePlayerWeapon > >`, `C_NetworkUtlVectorBase< CHandle< C_EconWearable > >`, `C_NetworkUtlVectorBase< CHandle< C_PostProcessingVolume > >`, `C_NetworkUtlVectorBase< CTransform >`, `C_NetworkUtlVectorBase< CUtlString >`, `C_NetworkUtlVectorBase< CUtlSymbolLarge >`, `C_NetworkUtlVectorBase< QAngle >`, `C_NetworkUtlVectorBase< ResourceId_t >`, `C_NetworkUtlVectorBase< SoundeventPathCornerPairNetworked_t >`, `C_NetworkUtlVectorBase< Vector >`, `C_NetworkUtlVectorBase< Vector2D >`, `C_NetworkUtlVectorBase< Vector4D >`, `C_NetworkUtlVectorBase< bool >`, `C_NetworkUtlVectorBase< float32 >`, `C_NetworkUtlVectorBase< int32 >`, `C_NetworkUtlVectorBase< uint16 >`, `C_NetworkUtlVectorBase< uint8 >`, `C_UtlVectorEmbeddedNetworkVar< AnimGraph2SerializedPoseRecipeSlot_t >`, `C_UtlVectorEmbeddedNetworkVar< CDamageRecord >`, `C_UtlVectorEmbeddedNetworkVar< CEconItemAttribute >`, `C_UtlVectorEmbeddedNetworkVar< CSPerRoundStats_t >`, `C_UtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >`, `C_UtlVectorEmbeddedNetworkVar< SellbackPurchaseEntry_t >`, `C_UtlVectorEmbeddedNetworkVar< ServerAuthoritativeWeaponSlot_t >`, `C_UtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >`, `C_UtlVectorEmbeddedNetworkVar< WeaponPurchaseCount_t >`, `Color`, `DegreeEuler`, `ENTITYFUNCPTR`, `FourVectors`, `HPulseCell< CPulseCell_TestWaitWithCursorState >`, `HPulseCellBase`, `HSCRIPT`, `HYieldedCursor`, `IPLCompressedEnergyFields`, `IPLProbeBatch`, `IPLScene`, `IPLStaticMesh`, `KeyValues`, `KeyValues3`, `ParticleParamID_t`, `PulseSymbol_t`, `QAngle`, `Quaternion`, `QuaternionStorage`, `RadianEuler`, `Range_t`, `RnSphere_t`, `RotationVector`, `SndOpEventGuid_t`, `USEPTR`, `V_uuid_t`, `Vector`, `Vector2D`, `Vector4D`, `VectorAligned`, `VectorWS`, `WorldGroupId_t`, `fltx4`, `matrix3x4_t`, `matrix3x4a_t`, `std::pair< CAnimParamHandle, CAnimVariant >`, `std::pair< CBufferString, float32 >`, `std::pair< CGlobalSymbol, CGlobalSymbol >`, `std::pair< CGlobalSymbol, CNmTarget >`, `std::pair< CGlobalSymbol, Vector >`, `std::pair< CGlobalSymbol, bool >`, `std::pair< CGlobalSymbol, float32 >`, `std::pair< CUtlString, CUtlString >`, `std::pair< CUtlString, uint32 >`

### Metadata keys (class / field / enum / member)

- `MAlternateSemanticName`
- `MCustomFGDMetadata`
- `MDebugSnapshotDataRenderFn`
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
- `MPulseEditorCanvasItemSpecKV3`
- `MPulseEditorHeaderHelper`
- `MPulseEditorHeaderIcon`
- `MPulseEditorHeaderText`
- `MPulseEditorSubHeaderText`
- `MPulseFGDSkipField`
- `MPulseFunctionHiddenInTool`
- `MResourceTypeForInfoType`
- `MSaveBehavior`
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


_Last regenerated against CS2 build `hl2sdk-cs2/5f891c9026230cce0fc0a3fc4b5fef1c467a1385/v1/3d1200e346019c59` (2026-08-03)._
