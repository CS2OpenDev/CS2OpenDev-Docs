---
layout: default
title: usermessages.proto
parent: Protobufs
nav_exclude: true
---

# `usermessages.proto`

**Imports:** `networkbasetypes.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CUserMessageAchievementEvent {
    +uint32 achievement
  }

  class CUserMessageCloseCaption {
    +fixed32 hash
    +float duration
    +bool from_player
    +int32 ent_index
  }

  class CUserMessageCloseCaptionDirect {
    +fixed32 hash
    +float duration
    +bool from_player
    +int32 ent_index
  }

  class CUserMessageCloseCaptionPlaceholder {
    +string string
    +float duration
    +bool from_player
    +int32 ent_index
  }

  class CUserMessageCurrentTimescale {
    +float current
  }

  class CUserMessageDesiredTimescale {
    +float desired
    +float acceleration
    +float minblendrate
    +float blenddeltamultiplier
  }

  class CUserMessageFade {
    +uint32 duration
    +uint32 hold_time
    +uint32 flags
    +fixed32 color
  }

  class CUserMessageShake {
    +uint32 command
    +float amplitude
    +float frequency
    +float duration
  }

  class CUserMessageShakeDir {
    +CUserMessageShake shake
    +CMsgVector direction
  }

  class CUserMessageWaterShake {
    +uint32 command
    +float amplitude
    +float frequency
    +float duration
  }

  class CUserMessageScreenTilt {
    +uint32 command
    +bool ease_in_out
    +CMsgVector angle
    +float duration
    +float time
  }

  class CUserMessageSayText {
    +int32 playerindex
    +string text
    +bool chat
  }

  class CUserMessageSayText2 {
    +int32 entityindex
    +bool chat
    +string messagename
    +string param1
    +string param2
    +string param3
    +string param4
  }

  class CUserMessageHudMsg {
    +uint32 channel
    +float x
    +float y
    +fixed32 color1
    +fixed32 color2
    +uint32 effect
    +string message
  }

  class CUserMessageHudText {
    +string message
  }

  class CUserMessageTextMsg {
    +uint32 dest
    +List~string~ param
  }

  class CUserMessageGameTitle {
  }

  class CUserMessageResetHUD {
  }

  class CUserMessageSendAudio {
    +string soundname
    +bool stop
  }

  class CUserMessageAudioParameter {
    +uint32 parameter_type
    +uint32 name_hash_code
    +float value
    +uint32 int_value
  }

  class CUserMessageVoiceMask {
    +List~uint32~ gamerules_masks
    +List~uint32~ ban_masks
    +bool mod_enable
  }

  class CUserMessageRequestState {
  }

  class CUserMessageRumble {
    +int32 index
    +int32 data
    +int32 flags
  }

  class CUserMessageSayTextChannel {
    +int32 player
    +int32 channel
    +string text
  }

  class CUserMessageColoredText {
    +uint32 color
    +string text
    +bool reset
    +int32 context_player_slot
    +int32 context_value
    +int32 context_team_id
  }

  class CUserMessageItemPickup {
    +string itemname
  }

  class CUserMessageAmmoDenied {
    +uint32 ammo_id
  }

  class CUserMessageShowMenu {
    +uint32 validslots
    +uint32 displaytime
    +bool needmore
    +string menustring
  }

  class CUserMessageCreditsMsg {
    +eRollType rolltype
    +float logo_length
  }

  class CEntityMessagePlayJingle {
    +CEntityMsg entity_msg
  }

  class CEntityMessageScreenOverlay {
    +bool start_effect
    +CEntityMsg entity_msg
  }

  class CEntityMessageRemoveAllDecals {
    +bool remove_decals
    +CEntityMsg entity_msg
  }

  class CEntityMessagePropagateForce {
    +CMsgVector impulse
    +CEntityMsg entity_msg
  }

  class CEntityMessageDoSpark {
    +CMsgVector origin
    +int32 entityindex
    +float radius
    +fixed32 color
    +uint32 beams
    +float thick
    +float duration
    +CEntityMsg entity_msg
  }

  class CEntityMessageFixAngle {
    +bool relative
    +CMsgQAngle angle
    +CEntityMsg entity_msg
  }

  class CUserMessageCameraTransition {
    +uint32 camera_type
    +float duration
    +CUserMessageCameraTransition.Transition_DataDriven params_data_driven
  }

  class Transition_DataDriven {
    +string filename
    +int32 attach_ent_index
    +float duration
  }

  class CUserMsg_ParticleManager {
    +PARTICLE_MESSAGE type
    +uint32 index
    +CUserMsg_ParticleManager.ReleaseParticleIndex release_particle_index
    +CUserMsg_ParticleManager.CreateParticle create_particle
    +CUserMsg_ParticleManager.DestroyParticle destroy_particle
    +CUserMsg_ParticleManager.DestroyParticleInvolving destroy_particle_involving
    +CUserMsg_ParticleManager.UpdateParticle_OBSOLETE update_particle
    +CUserMsg_ParticleManager.UpdateParticleFwd_OBSOLETE update_particle_fwd
    +CUserMsg_ParticleManager.UpdateParticleOrient_OBSOLETE update_particle_orient
    +CUserMsg_ParticleManager.UpdateParticleFallback update_particle_fallback
    +CUserMsg_ParticleManager.UpdateParticleOffset update_particle_offset
    +CUserMsg_ParticleManager.UpdateParticleEnt update_particle_ent
    +CUserMsg_ParticleManager.UpdateParticleShouldDraw update_particle_should_draw
    +CUserMsg_ParticleManager.UpdateParticleSetFrozen update_particle_set_frozen
    +CUserMsg_ParticleManager.ChangeControlPointAttachment change_control_point_attachment
    +CUserMsg_ParticleManager.UpdateEntityPosition update_entity_position
    +CUserMsg_ParticleManager.SetParticleFoWProperties set_particle_fow_properties
    +CUserMsg_ParticleManager.SetParticleText set_particle_text
    +CUserMsg_ParticleManager.SetParticleShouldCheckFoW set_particle_should_check_fow
    +CUserMsg_ParticleManager.SetControlPointModel set_control_point_model
    +CUserMsg_ParticleManager.SetControlPointSnapshot set_control_point_snapshot
    +CUserMsg_ParticleManager.SetTextureAttribute set_texture_attribute
    +CUserMsg_ParticleManager.SetSceneObjectGenericFlag set_scene_object_generic_flag
    +CUserMsg_ParticleManager.SetSceneObjectTintAndDesat set_scene_object_tint_and_desat
    +CUserMsg_ParticleManager.DestroyParticleNamed destroy_particle_named
    +CUserMsg_ParticleManager.ParticleSkipToTime particle_skip_to_time
    +CUserMsg_ParticleManager.ParticleCanFreeze particle_can_freeze
    +CUserMsg_ParticleManager.SetParticleNamedValueContext set_named_value_context
    +CUserMsg_ParticleManager.UpdateParticleTransform update_particle_transform
    +CUserMsg_ParticleManager.ParticleFreezeTransitionOverride particle_freeze_transition_override
    +CUserMsg_ParticleManager.FreezeParticleInvolving freeze_particle_involving
    +CUserMsg_ParticleManager.AddModellistOverrideElement add_modellist_override_element
    +CUserMsg_ParticleManager.ClearModellistOverride clear_modellist_override
    +CUserMsg_ParticleManager.CreatePhysicsSim create_physics_sim
    +CUserMsg_ParticleManager.DestroyPhysicsSim destroy_physics_sim
    +CUserMsg_ParticleManager.SetVData set_vdata
    +CUserMsg_ParticleManager.SetMaterialOverride set_material_override
    +CUserMsg_ParticleManager.AddFan add_fan
    +CUserMsg_ParticleManager.UpdateFan update_fan
    +CUserMsg_ParticleManager.SetParticleClusterGrowth set_particle_cluster_growth
    +CUserMsg_ParticleManager.RemoveFan remove_fan
    +CUserMsg_ParticleManager.CreateSmokeGrid create_smoke_grid
    +CUserMsg_ParticleManager.SetOverrideTexture set_override_texture
  }

  class ReleaseParticleIndex {
  }

  class CreateParticle {
    +fixed64 particle_name_index
    +int32 attach_type
    +uint32 entity_handle
    +uint32 entity_handle_for_modifiers
    +bool apply_voice_ban_rules
    +int32 team_behavior
    +string control_point_configuration
    +bool cluster
    +float endcap_time
    +CMsgVector aggregation_position
  }

  class DestroyParticle {
    +bool destroy_immediately
  }

  class DestroyParticleInvolving {
    +bool destroy_immediately
    +uint32 entity_handle
  }

  class DestroyParticleNamed {
    +fixed64 particle_name_index
    +uint32 entity_handle
    +bool destroy_immediately
    +bool play_endcap
  }

  class UpdateParticle_OBSOLETE {
    +int32 control_point
    +CMsgVector position
  }

  class UpdateParticleFwd_OBSOLETE {
    +int32 control_point
    +CMsgVector forward
  }

  class UpdateParticleOrient_OBSOLETE {
    +int32 control_point
    +CMsgVector forward
    +CMsgVector deprecated_right
    +CMsgVector up
    +CMsgVector left
  }

  class UpdateParticleTransform {
    +int32 control_point
    +CMsgVector position
    +CMsgQuaternion orientation
    +float interpolation_interval
  }

  class UpdateParticleFallback {
    +int32 control_point
    +CMsgVector position
  }

  class UpdateParticleOffset {
    +int32 control_point
    +CMsgVector origin_offset
    +CMsgQAngle angle_offset
  }

  class UpdateParticleEnt {
    +int32 control_point
    +uint32 entity_handle
    +int32 attach_type
    +int32 attachment
    +CMsgVector fallback_position
    +bool include_wearables
    +CMsgVector offset_position
    +CMsgQAngle offset_angles
  }

  class UpdateParticleSetFrozen {
    +bool set_frozen
    +float transition_duration
  }

  class UpdateParticleShouldDraw {
    +bool should_draw
  }

  class ChangeControlPointAttachment {
    +int32 attachment_old
    +int32 attachment_new
    +uint32 entity_handle
  }

  class UpdateEntityPosition {
    +uint32 entity_handle
    +CMsgVector position
  }

  class SetParticleFoWProperties {
    +int32 fow_control_point
    +int32 fow_control_point2
    +float fow_radius
  }

  class SetParticleShouldCheckFoW {
    +bool check_fow
  }

  class SetControlPointModel {
    +int32 control_point
    +string model_name
  }

  class SetControlPointSnapshot {
    +int32 control_point
    +string snapshot_name
  }

  class SetParticleText {
    +string text
    +bool localize
  }

  class SetTextureAttribute {
    +string attribute_name
    +string texture_name
  }

  class SetOverrideTexture {
    +string texture_name
  }

  class SetSceneObjectGenericFlag {
    +bool flag_value
  }

  class SetSceneObjectTintAndDesat {
    +fixed32 tint
    +float desat
  }

  class ParticleSkipToTime {
    +float skip_to_time
  }

  class ParticleCanFreeze {
    +bool can_freeze
  }

  class ParticleFreezeTransitionOverride {
    +float freeze_transition_override
  }

  class FreezeParticleInvolving {
    +bool set_frozen
    +float transition_duration
    +uint32 entity_handle
  }

  class AddModellistOverrideElement {
    +string model_name
    +float spawn_probability
    +uint32 groupid
  }

  class ClearModellistOverride {
    +uint32 groupid
  }

  class SetParticleNamedValueContext {
    +List~CUserMsg_ParticleManager.SetParticleNamedValueContext.FloatContextValue~ float_values
    +List~CUserMsg_ParticleManager.SetParticleNamedValueContext.VectorContextValue~ vector_values
    +List~CUserMsg_ParticleManager.SetParticleNamedValueContext.TransformContextValue~ transform_values
    +List~CUserMsg_ParticleManager.SetParticleNamedValueContext.EHandleContext~ ehandle_values
  }

  class FloatContextValue {
    +uint32 value_name_hash
    +float value
  }

  class VectorContextValue {
    +uint32 value_name_hash
    +CMsgVector value
  }

  class TransformContextValue {
    +uint32 value_name_hash
    +CMsgQAngle angles
    +CMsgVector translation
  }

  class EHandleContext {
    +uint32 value_name_hash
    +uint32 ent_index
  }

  class CreatePhysicsSim {
    +string prop_group_name
    +bool use_high_quality_simulation
    +uint32 max_particle_count
  }

  class DestroyPhysicsSim {
  }

  class CreateSmokeGrid {
    +string vdata_name
  }

  class SetVData {
    +string vdata_name
  }

  class SetMaterialOverride {
    +string material_name
    +bool include_children
  }

  class AddFan {
    +bool active
    +CMsgVector bounds_mins
    +CMsgVector bounds_maxs
    +CMsgVector fan_origin
    +CMsgVector fan_origin_offset
    +CMsgVector fan_direction
    +float force
    +string fan_force_curve
    +bool falloff
    +bool pull_towards_point
    +float curve_min_dist
    +float curve_max_dist
    +uint32 fan_type
    +float cone_start_radius
    +float cone_end_radius
    +float cone_length
    +uint32 entity_handle
    +string attachment_name
  }

  class UpdateFan {
    +bool active
    +CMsgVector fan_origin
    +CMsgVector fan_origin_offset
    +CMsgVector fan_direction
    +float fan_ramp_ratio
    +CMsgVector bounds_mins
    +CMsgVector bounds_maxs
  }

  class RemoveFan {
  }

  class SetParticleClusterGrowth {
    +float duration
    +CMsgVector origin
  }

  class CUserMsg_HudError {
    +int32 order_id
  }

  class CUserMsg_CustomGameEvent {
    +string event_name
    +bytes data
  }

  class CUserMessageHapticsManagerPulse {
    +int32 hand_id
    +float effect_amplitude
    +float effect_frequency
    +float effect_duration
  }

  class CUserMessageHapticsManagerEffect {
    +int32 hand_id
    +uint32 effect_name_hash_code
    +float effect_scale
  }

  class CUserMessageAnimStateGraphState {
    +int32 entity_index
    +bytes data
  }

  class CUserMessageUpdateCssClasses {
    +int32 target_world_panel
    +string css_classes
    +bool is_add
  }

  class CUserMessageServerFrameTime {
    +float frame_time
  }

  class CUserMessageLagCompensationError {
    +float distance
  }

  class CUserMessageRequestDllStatus {
    +string dll_action
    +bool full_report
  }

  class CUserMessageRequestUtilAction {
    +int32 util1
    +int32 util2
    +int32 util3
    +int32 util4
    +int32 util5
  }

  class CUserMessage_UtilMsg_Response {
    +fixed32 crc
    +int32 item_count
    +fixed32 crc2
    +int32 item_count2
    +List~int32~ crc_part
    +List~int32~ crc_part2
    +int32 client_timestamp
    +int32 platform
    +List~CUserMessage_UtilMsg_Response.ItemDetail~ itemdetails
    +int32 itemgroup
    +int32 total_count
    +int32 total_count2
  }

  class ItemDetail {
    +int32 index
    +int32 hash
    +int32 crc
    +string name
  }

  class CUserMessage_DllStatus {
    +string file_report
    +string command_line
    +uint32 total_files
    +uint32 process_id
    +int32 osversion
    +uint64 client_time
    +List~CUserMessage_DllStatus.CVDiagnostic~ diagnostics
    +List~CUserMessage_DllStatus.CModule~ modules
  }

  class CVDiagnostic {
    +uint32 id
    +uint32 extended
    +uint64 value
    +string string_value
  }

  class CModule {
    +uint64 base_addr
    +string name
    +uint32 size
    +uint32 timestamp
  }

  class CUserMessageRequestInventory {
    +int32 inventory
    +int32 offset
    +int32 options
  }

  class CUserMessage_Inventory_Response {
    +fixed32 crc
    +int32 item_count
    +int32 osversion
    +int32 perf_time
    +int32 client_timestamp
    +int32 platform
    +List~CUserMessage_Inventory_Response.InventoryDetail~ inventories
    +List~CUserMessage_Inventory_Response.InventoryDetail~ inventories2
    +List~CUserMessage_Inventory_Response.InventoryDetail~ inventories3
    +int32 inv_type
    +int32 build_version
    +int32 instance
    +int64 start_time
  }

  class InventoryDetail {
    +int32 index
    +int64 primary
    +int64 offset
    +int64 first
    +int64 base
    +string name
    +string base_name
    +int32 base_detail
    +int32 base_time
    +int32 base_hash
  }

  class CUserMessageRequestDiagnostic {
    +List~CUserMessageRequestDiagnostic.Diagnostic~ diagnostics
  }

  class Diagnostic {
    +int32 index
    +int64 offset
    +int32 param
    +int32 length
    +int32 type
    +int64 base
    +int64 range
    +int64 extent
    +int64 detail
    +string name
    +string alias
    +bytes vardetail
    +int32 context
  }

  class CUserMessage_Diagnostic_Response {
    +List~CUserMessage_Diagnostic_Response.Diagnostic~ diagnostics
    +int32 build_version
    +int32 instance
    +int64 start_time
    +int32 osversion
    +int32 platform
  }

  class Diagnostic {
    +int32 index
    +int64 offset
    +int32 param
    +int32 length
    +bytes detail
    +int64 base
    +int64 range
    +int32 type
    +string name
    +string alias
    +bytes backup
    +int32 context
    +int64 control
    +int64 augment
    +int64 placebo
  }

  class CUserMessage_ExtraUserData {
    +int32 item
    +int64 value1
    +int64 value2
    +List~bytes~ detail1
    +List~bytes~ detail2
  }

  class CUserMessage_NotifyResponseFound {
    +int32 ent_index
    +string rule_name
    +string response_value
    +string response_concept
    +List~CUserMessage_NotifyResponseFound.Criteria~ criteria
    +List~uint32~ int_criteria_names
    +List~int32~ int_criteria_values
    +List~uint32~ float_criteria_names
    +List~float~ float_criteria_values
    +List~uint32~ symbol_criteria_names
    +List~uint32~ symbol_criteria_values
    +int32 speak_result
  }

  class Criteria {
    +uint32 name_symbol
    +string value
  }

  class CUserMessage_PlayResponseConditional {
    +int32 ent_index
    +List~int32~ player_slots
    +string response
    +CMsgVector ent_origin
    +float pre_delay
    +int32 mix_priority
  }

  CUserMessageShakeDir --> CUserMessageShake : shake
  CUserMessageCreditsMsg --> eRollType : rolltype
  CUserMessageCameraTransition --> Transition_DataDriven : params_data_driven
  CUserMsg_ParticleManager --> PARTICLE_MESSAGE : type
  CUserMsg_ParticleManager --> ReleaseParticleIndex : release_particle_index
  CUserMsg_ParticleManager --> CreateParticle : create_particle
  CUserMsg_ParticleManager --> DestroyParticle : destroy_particle
  CUserMsg_ParticleManager --> DestroyParticleInvolving : destroy_particle_involving
  CUserMsg_ParticleManager --> UpdateParticle_OBSOLETE : update_particle
  CUserMsg_ParticleManager --> UpdateParticleFwd_OBSOLETE : update_particle_fwd
  CUserMsg_ParticleManager --> UpdateParticleOrient_OBSOLETE : update_particle_orient
  CUserMsg_ParticleManager --> UpdateParticleFallback : update_particle_fallback
  CUserMsg_ParticleManager --> UpdateParticleOffset : update_particle_offset
  CUserMsg_ParticleManager --> UpdateParticleEnt : update_particle_ent
  CUserMsg_ParticleManager --> UpdateParticleShouldDraw : update_particle_should_draw
  CUserMsg_ParticleManager --> UpdateParticleSetFrozen : update_particle_set_frozen
  CUserMsg_ParticleManager --> ChangeControlPointAttachment : change_control_point_attachment
  CUserMsg_ParticleManager --> UpdateEntityPosition : update_entity_position
  CUserMsg_ParticleManager --> SetParticleFoWProperties : set_particle_fow_properties
  CUserMsg_ParticleManager --> SetParticleText : set_particle_text
  CUserMsg_ParticleManager --> SetParticleShouldCheckFoW : set_particle_should_check_fow
  CUserMsg_ParticleManager --> SetControlPointModel : set_control_point_model
  CUserMsg_ParticleManager --> SetControlPointSnapshot : set_control_point_snapshot
  CUserMsg_ParticleManager --> SetTextureAttribute : set_texture_attribute
  CUserMsg_ParticleManager --> SetSceneObjectGenericFlag : set_scene_object_generic_flag
  CUserMsg_ParticleManager --> SetSceneObjectTintAndDesat : set_scene_object_tint_and_desat
  CUserMsg_ParticleManager --> DestroyParticleNamed : destroy_particle_named
  CUserMsg_ParticleManager --> ParticleSkipToTime : particle_skip_to_time
  CUserMsg_ParticleManager --> ParticleCanFreeze : particle_can_freeze
  CUserMsg_ParticleManager --> SetParticleNamedValueContext : set_named_value_context
  CUserMsg_ParticleManager --> UpdateParticleTransform : update_particle_transform
  CUserMsg_ParticleManager --> ParticleFreezeTransitionOverride : particle_freeze_transition_override
  CUserMsg_ParticleManager --> FreezeParticleInvolving : freeze_particle_involving
  CUserMsg_ParticleManager --> AddModellistOverrideElement : add_modellist_override_element
  CUserMsg_ParticleManager --> ClearModellistOverride : clear_modellist_override
  CUserMsg_ParticleManager --> CreatePhysicsSim : create_physics_sim
  CUserMsg_ParticleManager --> DestroyPhysicsSim : destroy_physics_sim
  CUserMsg_ParticleManager --> SetVData : set_vdata
  CUserMsg_ParticleManager --> SetMaterialOverride : set_material_override
  CUserMsg_ParticleManager --> AddFan : add_fan
  CUserMsg_ParticleManager --> UpdateFan : update_fan
  CUserMsg_ParticleManager --> SetParticleClusterGrowth : set_particle_cluster_growth
  CUserMsg_ParticleManager --> RemoveFan : remove_fan
  CUserMsg_ParticleManager --> CreateSmokeGrid : create_smoke_grid
  CUserMsg_ParticleManager --> SetOverrideTexture : set_override_texture
  SetParticleNamedValueContext --> FloatContextValue : float_values[]
  SetParticleNamedValueContext --> VectorContextValue : vector_values[]
  SetParticleNamedValueContext --> TransformContextValue : transform_values[]
  SetParticleNamedValueContext --> EHandleContext : ehandle_values[]
  CUserMessage_UtilMsg_Response --> ItemDetail : itemdetails[]
  CUserMessage_DllStatus --> CVDiagnostic : diagnostics[]
  CUserMessage_DllStatus --> CModule : modules[]
  CUserMessage_Inventory_Response --> InventoryDetail : inventories[]
  CUserMessageRequestDiagnostic --> Diagnostic : diagnostics[]
  CUserMessage_Diagnostic_Response --> Diagnostic : diagnostics[]
  CUserMessage_NotifyResponseFound --> Criteria : criteria[]

  class EBaseUserMessages{
    <<enumeration>>
    UM_AchievementEvent
    UM_CloseCaption
    UM_CloseCaptionDirect
    UM_CurrentTimescale
    UM_DesiredTimescale
    UM_Fade
    UM_GameTitle
    UM_HudMsg
    UM_HudText
    UM_ColoredText
    UM_RequestState
    UM_ResetHUD
    UM_Rumble
    UM_SayText
    UM_SayText2
    UM_SayTextChannel
    UM_Shake
    UM_ShakeDir
    UM_WaterShake
    UM_TextMsg
    UM_ScreenTilt
    UM_VoiceMask
    UM_SendAudio
    UM_ItemPickup
    UM_AmmoDenied
    UM_ShowMenu
    UM_CreditsMsg
    UM_CloseCaptionPlaceholder
    UM_CameraTransition
    UM_AudioParameter
    UM_ParticleManager
    UM_HudError
    UM_CustomGameEvent
    UM_AnimGraphUpdate
    UM_HapticsManagerPulse
    UM_HapticsManagerEffect
    UM_UpdateCssClasses
    UM_ServerFrameTime
    UM_LagCompensationError
    UM_RequestDllStatus
    UM_RequestUtilAction
    UM_UtilActionResponse
    UM_DllStatusResponse
    UM_RequestInventory
    UM_InventoryResponse
    UM_RequestDiagnostic
    UM_DiagnosticResponse
    UM_ExtraUserData
    UM_NotifyResponseFound
    UM_PlayResponseConditional
    UM_MAX_BASE
  }

  class EBaseEntityMessages{
    <<enumeration>>
    EM_PlayJingle
    EM_ScreenOverlay
    EM_RemoveAllDecals
    EM_PropagateForce
    EM_DoSpark
    EM_FixAngle
  }

  class eRollType{
    <<enumeration>>
    ROLL_NONE
    ROLL_STATS
    ROLL_CREDITS
    ROLL_LATE_JOIN_LOGO
    ROLL_OUTTRO
  }

  class PARTICLE_MESSAGE{
    <<enumeration>>
    GAME_PARTICLE_MANAGER_EVENT_CREATE
    GAME_PARTICLE_MANAGER_EVENT_UPDATE
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_FORWARD
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_ORIENTATION
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_FALLBACK
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENT
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_OFFSET
    GAME_PARTICLE_MANAGER_EVENT_DESTROY
    GAME_PARTICLE_MANAGER_EVENT_DESTROY_INVOLVING
    GAME_PARTICLE_MANAGER_EVENT_RELEASE
    GAME_PARTICLE_MANAGER_EVENT_LATENCY
    GAME_PARTICLE_MANAGER_EVENT_SHOULD_DRAW
    GAME_PARTICLE_MANAGER_EVENT_FROZEN
    GAME_PARTICLE_MANAGER_EVENT_CHANGE_CONTROL_POINT_ATTACHMENT
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENTITY_POSITION
    GAME_PARTICLE_MANAGER_EVENT_SET_FOW_PROPERTIES
    GAME_PARTICLE_MANAGER_EVENT_SET_TEXT
    GAME_PARTICLE_MANAGER_EVENT_SET_SHOULD_CHECK_FOW
    GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_MODEL
    GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_SNAPSHOT
    GAME_PARTICLE_MANAGER_EVENT_SET_TEXTURE_ATTRIBUTE
    GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_GENERIC_FLAG
    GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_TINT_AND_DESAT
    GAME_PARTICLE_MANAGER_EVENT_DESTROY_NAMED
    GAME_PARTICLE_MANAGER_EVENT_SKIP_TO_TIME
    GAME_PARTICLE_MANAGER_EVENT_CAN_FREEZE
    GAME_PARTICLE_MANAGER_EVENT_SET_NAMED_VALUE_CONTEXT
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_TRANSFORM
    GAME_PARTICLE_MANAGER_EVENT_FREEZE_TRANSITION_OVERRIDE
    GAME_PARTICLE_MANAGER_EVENT_FREEZE_INVOLVING
    GAME_PARTICLE_MANAGER_EVENT_ADD_MODELLIST_OVERRIDE_ELEMENT
    GAME_PARTICLE_MANAGER_EVENT_CLEAR_MODELLIST_OVERRIDE
    GAME_PARTICLE_MANAGER_EVENT_CREATE_PHYSICS_SIM
    GAME_PARTICLE_MANAGER_EVENT_DESTROY_PHYSICS_SIM
    GAME_PARTICLE_MANAGER_EVENT_SET_VDATA
    GAME_PARTICLE_MANAGER_EVENT_SET_MATERIAL_OVERRIDE
    GAME_PARTICLE_MANAGER_EVENT_ADD_FAN
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_FAN
    GAME_PARTICLE_MANAGER_EVENT_SET_CLUSTER_GROWTH
    GAME_PARTICLE_MANAGER_EVENT_REMOVE_FAN
    GAME_PARTICLE_MANAGER_EVENT_CREATE_SMOKE_GRID
    GAME_PARTICLE_MANAGER_EVENT_SET_OVERRIDE_TEXTURE
  }

  class EHapticPulseType{
    <<enumeration>>
    VR_HAND_HAPTIC_PULSE_LIGHT
    VR_HAND_HAPTIC_PULSE_MEDIUM
    VR_HAND_HAPTIC_PULSE_STRONG
  }

```

## Enums

### `EBaseUserMessages`

| Name | Value |
|------|-------|
| `UM_AchievementEvent` | 101 |
| `UM_CloseCaption` | 102 |
| `UM_CloseCaptionDirect` | 103 |
| `UM_CurrentTimescale` | 104 |
| `UM_DesiredTimescale` | 105 |
| `UM_Fade` | 106 |
| `UM_GameTitle` | 107 |
| `UM_HudMsg` | 110 |
| `UM_HudText` | 111 |
| `UM_ColoredText` | 113 |
| `UM_RequestState` | 114 |
| `UM_ResetHUD` | 115 |
| `UM_Rumble` | 116 |
| `UM_SayText` | 117 |
| `UM_SayText2` | 118 |
| `UM_SayTextChannel` | 119 |
| `UM_Shake` | 120 |
| `UM_ShakeDir` | 121 |
| `UM_WaterShake` | 122 |
| `UM_TextMsg` | 124 |
| `UM_ScreenTilt` | 125 |
| `UM_VoiceMask` | 128 |
| `UM_SendAudio` | 130 |
| `UM_ItemPickup` | 131 |
| `UM_AmmoDenied` | 132 |
| `UM_ShowMenu` | 134 |
| `UM_CreditsMsg` | 135 |
| `UM_CloseCaptionPlaceholder` | 142 |
| `UM_CameraTransition` | 143 |
| `UM_AudioParameter` | 144 |
| `UM_ParticleManager` | 145 |
| `UM_HudError` | 146 |
| `UM_CustomGameEvent` | 148 |
| `UM_AnimGraphUpdate` | 149 |
| `UM_HapticsManagerPulse` | 150 |
| `UM_HapticsManagerEffect` | 151 |
| `UM_UpdateCssClasses` | 153 |
| `UM_ServerFrameTime` | 154 |
| `UM_LagCompensationError` | 155 |
| `UM_RequestDllStatus` | 156 |
| `UM_RequestUtilAction` | 157 |
| `UM_UtilActionResponse` | 158 |
| `UM_DllStatusResponse` | 159 |
| `UM_RequestInventory` | 160 |
| `UM_InventoryResponse` | 161 |
| `UM_RequestDiagnostic` | 162 |
| `UM_DiagnosticResponse` | 163 |
| `UM_ExtraUserData` | 164 |
| `UM_NotifyResponseFound` | 165 |
| `UM_PlayResponseConditional` | 166 |
| `UM_MAX_BASE` | 200 |

### `EBaseEntityMessages`

| Name | Value |
|------|-------|
| `EM_PlayJingle` | 136 |
| `EM_ScreenOverlay` | 137 |
| `EM_RemoveAllDecals` | 138 |
| `EM_PropagateForce` | 139 |
| `EM_DoSpark` | 140 |
| `EM_FixAngle` | 141 |

### `eRollType`

| Name | Value |
|------|-------|
| `ROLL_NONE` | -1 |
| `ROLL_STATS` | 0 |
| `ROLL_CREDITS` | 1 |
| `ROLL_LATE_JOIN_LOGO` | 2 |
| `ROLL_OUTTRO` | 3 |

### `PARTICLE_MESSAGE`

| Name | Value |
|------|-------|
| `GAME_PARTICLE_MANAGER_EVENT_CREATE` | 0 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE` | 1 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_FORWARD` | 2 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_ORIENTATION` | 3 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_FALLBACK` | 4 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENT` | 5 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_OFFSET` | 6 |
| `GAME_PARTICLE_MANAGER_EVENT_DESTROY` | 7 |
| `GAME_PARTICLE_MANAGER_EVENT_DESTROY_INVOLVING` | 8 |
| `GAME_PARTICLE_MANAGER_EVENT_RELEASE` | 9 |
| `GAME_PARTICLE_MANAGER_EVENT_LATENCY` | 10 |
| `GAME_PARTICLE_MANAGER_EVENT_SHOULD_DRAW` | 11 |
| `GAME_PARTICLE_MANAGER_EVENT_FROZEN` | 12 |
| `GAME_PARTICLE_MANAGER_EVENT_CHANGE_CONTROL_POINT_ATTACHMENT` | 13 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENTITY_POSITION` | 14 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_FOW_PROPERTIES` | 15 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_TEXT` | 16 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_SHOULD_CHECK_FOW` | 17 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_MODEL` | 18 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_SNAPSHOT` | 19 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_TEXTURE_ATTRIBUTE` | 20 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_GENERIC_FLAG` | 21 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_TINT_AND_DESAT` | 22 |
| `GAME_PARTICLE_MANAGER_EVENT_DESTROY_NAMED` | 23 |
| `GAME_PARTICLE_MANAGER_EVENT_SKIP_TO_TIME` | 24 |
| `GAME_PARTICLE_MANAGER_EVENT_CAN_FREEZE` | 25 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_NAMED_VALUE_CONTEXT` | 26 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_TRANSFORM` | 27 |
| `GAME_PARTICLE_MANAGER_EVENT_FREEZE_TRANSITION_OVERRIDE` | 28 |
| `GAME_PARTICLE_MANAGER_EVENT_FREEZE_INVOLVING` | 29 |
| `GAME_PARTICLE_MANAGER_EVENT_ADD_MODELLIST_OVERRIDE_ELEMENT` | 30 |
| `GAME_PARTICLE_MANAGER_EVENT_CLEAR_MODELLIST_OVERRIDE` | 31 |
| `GAME_PARTICLE_MANAGER_EVENT_CREATE_PHYSICS_SIM` | 32 |
| `GAME_PARTICLE_MANAGER_EVENT_DESTROY_PHYSICS_SIM` | 33 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_VDATA` | 34 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_MATERIAL_OVERRIDE` | 35 |
| `GAME_PARTICLE_MANAGER_EVENT_ADD_FAN` | 36 |
| `GAME_PARTICLE_MANAGER_EVENT_UPDATE_FAN` | 37 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_CLUSTER_GROWTH` | 38 |
| `GAME_PARTICLE_MANAGER_EVENT_REMOVE_FAN` | 39 |
| `GAME_PARTICLE_MANAGER_EVENT_CREATE_SMOKE_GRID` | 40 |
| `GAME_PARTICLE_MANAGER_EVENT_SET_OVERRIDE_TEXTURE` | 41 |

### `EHapticPulseType`

| Name | Value |
|------|-------|
| `VR_HAND_HAPTIC_PULSE_LIGHT` | 0 |
| `VR_HAND_HAPTIC_PULSE_MEDIUM` | 1 |
| `VR_HAND_HAPTIC_PULSE_STRONG` | 2 |

## Messages

### `CUserMessageAchievementEvent`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `achievement` | 1 | uint32 | optional |  |

### `CUserMessageCloseCaption`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `hash` | 1 | fixed32 | optional |  |
| `duration` | 2 | float | optional |  |
| `from_player` | 3 | bool | optional |  |
| `ent_index` | 4 | int32 | optional | *(default: `-1`)* |

### `CUserMessageCloseCaptionDirect`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `hash` | 1 | fixed32 | optional |  |
| `duration` | 2 | float | optional |  |
| `from_player` | 3 | bool | optional |  |
| `ent_index` | 4 | int32 | optional | *(default: `-1`)* |

### `CUserMessageCloseCaptionPlaceholder`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `string` | 1 | string | optional |  |
| `duration` | 2 | float | optional |  |
| `from_player` | 3 | bool | optional |  |
| `ent_index` | 4 | int32 | optional | *(default: `-1`)* |

### `CUserMessageCurrentTimescale`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `current` | 1 | float | optional |  |

### `CUserMessageDesiredTimescale`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `desired` | 1 | float | optional |  |
| `acceleration` | 2 | float | optional |  |
| `minblendrate` | 3 | float | optional |  |
| `blenddeltamultiplier` | 4 | float | optional |  |

### `CUserMessageFade`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `duration` | 1 | uint32 | optional |  |
| `hold_time` | 2 | uint32 | optional |  |
| `flags` | 3 | uint32 | optional |  |
| `color` | 4 | fixed32 | optional |  |

### `CUserMessageShake`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `command` | 1 | uint32 | optional |  |
| `amplitude` | 2 | float | optional |  |
| `frequency` | 3 | float | optional |  |
| `duration` | 4 | float | optional |  |

### `CUserMessageShakeDir`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `shake` | 1 | [CUserMessageShake](#cusermessageshake) | optional |  |
| `direction` | 2 | CMsgVector | optional |  |

### `CUserMessageWaterShake`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `command` | 1 | uint32 | optional |  |
| `amplitude` | 2 | float | optional |  |
| `frequency` | 3 | float | optional |  |
| `duration` | 4 | float | optional |  |

### `CUserMessageScreenTilt`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `command` | 1 | uint32 | optional |  |
| `ease_in_out` | 2 | bool | optional |  |
| `angle` | 3 | CMsgVector | optional |  |
| `duration` | 4 | float | optional |  |
| `time` | 5 | float | optional |  |

### `CUserMessageSayText`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `playerindex` | 1 | int32 | optional | *(default: `-1`)* |
| `text` | 2 | string | optional |  |
| `chat` | 3 | bool | optional |  |

### `CUserMessageSayText2`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entityindex` | 1 | int32 | optional | *(default: `-1`)* |
| `chat` | 2 | bool | optional |  |
| `messagename` | 3 | string | optional |  |
| `param1` | 4 | string | optional |  |
| `param2` | 5 | string | optional |  |
| `param3` | 6 | string | optional |  |
| `param4` | 7 | string | optional |  |

### `CUserMessageHudMsg`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `channel` | 1 | uint32 | optional |  |
| `x` | 2 | float | optional |  |
| `y` | 3 | float | optional |  |
| `color1` | 4 | fixed32 | optional |  |
| `color2` | 5 | fixed32 | optional |  |
| `effect` | 6 | uint32 | optional |  |
| `message` | 11 | string | optional |  |

### `CUserMessageHudText`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `message` | 1 | string | optional |  |

### `CUserMessageTextMsg`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `dest` | 1 | uint32 | optional |  |
| `param` | 2 | string | repeated |  |

### `CUserMessageGameTitle`

### `CUserMessageResetHUD`

### `CUserMessageSendAudio`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `soundname` | 1 | string | optional |  |
| `stop` | 2 | bool | optional |  |

### `CUserMessageAudioParameter`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `parameter_type` | 1 | uint32 | optional |  |
| `name_hash_code` | 2 | uint32 | optional |  |
| `value` | 3 | float | optional |  |
| `int_value` | 4 | uint32 | optional |  |

### `CUserMessageVoiceMask`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `gamerules_masks` | 1 | uint32 | repeated |  |
| `ban_masks` | 2 | uint32 | repeated |  |
| `mod_enable` | 3 | bool | optional |  |

### `CUserMessageRequestState`

### `CUserMessageRumble`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `index` | 1 | int32 | optional |  |
| `data` | 2 | int32 | optional |  |
| `flags` | 3 | int32 | optional |  |

### `CUserMessageSayTextChannel`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `player` | 1 | int32 | optional |  |
| `channel` | 2 | int32 | optional |  |
| `text` | 3 | string | optional |  |

### `CUserMessageColoredText`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `color` | 1 | uint32 | optional |  |
| `text` | 2 | string | optional |  |
| `reset` | 3 | bool | optional |  |
| `context_player_slot` | 4 | int32 | optional | *(default: `-1`)* |
| `context_value` | 5 | int32 | optional |  |
| `context_team_id` | 6 | int32 | optional |  |

### `CUserMessageItemPickup`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `itemname` | 1 | string | optional |  |

### `CUserMessageAmmoDenied`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ammo_id` | 1 | uint32 | optional |  |

### `CUserMessageShowMenu`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `validslots` | 1 | uint32 | optional |  |
| `displaytime` | 2 | uint32 | optional |  |
| `needmore` | 3 | bool | optional |  |
| `menustring` | 4 | string | optional |  |

### `CUserMessageCreditsMsg`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `rolltype` | 1 | [eRollType](#erolltype) | optional | *(default: `ROLL_NONE`)* |
| `logo_length` | 2 | float | optional |  |

### `CEntityMessagePlayJingle`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entity_msg` | 1 | CEntityMsg | optional |  |

### `CEntityMessageScreenOverlay`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `start_effect` | 1 | bool | optional |  |
| `entity_msg` | 2 | CEntityMsg | optional |  |

### `CEntityMessageRemoveAllDecals`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `remove_decals` | 1 | bool | optional |  |
| `entity_msg` | 2 | CEntityMsg | optional |  |

### `CEntityMessagePropagateForce`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `impulse` | 1 | CMsgVector | optional |  |
| `entity_msg` | 2 | CEntityMsg | optional |  |

### `CEntityMessageDoSpark`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `origin` | 1 | CMsgVector | optional |  |
| `entityindex` | 2 | int32 | optional | *(default: `-1`)* |
| `radius` | 3 | float | optional |  |
| `color` | 4 | fixed32 | optional |  |
| `beams` | 5 | uint32 | optional |  |
| `thick` | 6 | float | optional |  |
| `duration` | 7 | float | optional |  |
| `entity_msg` | 8 | CEntityMsg | optional |  |

### `CEntityMessageFixAngle`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `relative` | 1 | bool | optional |  |
| `angle` | 2 | CMsgQAngle | optional |  |
| `entity_msg` | 3 | CEntityMsg | optional |  |

### `CUserMessageCameraTransition`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `camera_type` | 1 | uint32 | optional |  |
| `duration` | 2 | float | optional |  |
| `params_data_driven` | 3 | CUserMessageCameraTransition.Transition_DataDriven | optional |  |

### `CUserMsg_ParticleManager`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `type` | 1 | [PARTICLE_MESSAGE](#particle_message) | optional | *(default: `GAME_PARTICLE_MANAGER_EVENT_CREATE`)* |
| `index` | 2 | uint32 | optional |  |
| `release_particle_index` | 3 | CUserMsg_ParticleManager.ReleaseParticleIndex | optional |  |
| `create_particle` | 4 | CUserMsg_ParticleManager.CreateParticle | optional |  |
| `destroy_particle` | 5 | CUserMsg_ParticleManager.DestroyParticle | optional |  |
| `destroy_particle_involving` | 6 | CUserMsg_ParticleManager.DestroyParticleInvolving | optional |  |
| `update_particle` | 7 | CUserMsg_ParticleManager.UpdateParticle_OBSOLETE | optional |  |
| `update_particle_fwd` | 8 | CUserMsg_ParticleManager.UpdateParticleFwd_OBSOLETE | optional |  |
| `update_particle_orient` | 9 | CUserMsg_ParticleManager.UpdateParticleOrient_OBSOLETE | optional |  |
| `update_particle_fallback` | 10 | CUserMsg_ParticleManager.UpdateParticleFallback | optional |  |
| `update_particle_offset` | 11 | CUserMsg_ParticleManager.UpdateParticleOffset | optional |  |
| `update_particle_ent` | 12 | CUserMsg_ParticleManager.UpdateParticleEnt | optional |  |
| `update_particle_should_draw` | 14 | CUserMsg_ParticleManager.UpdateParticleShouldDraw | optional |  |
| `update_particle_set_frozen` | 15 | CUserMsg_ParticleManager.UpdateParticleSetFrozen | optional |  |
| `change_control_point_attachment` | 16 | CUserMsg_ParticleManager.ChangeControlPointAttachment | optional |  |
| `update_entity_position` | 17 | CUserMsg_ParticleManager.UpdateEntityPosition | optional |  |
| `set_particle_fow_properties` | 18 | CUserMsg_ParticleManager.SetParticleFoWProperties | optional |  |
| `set_particle_text` | 19 | CUserMsg_ParticleManager.SetParticleText | optional |  |
| `set_particle_should_check_fow` | 20 | CUserMsg_ParticleManager.SetParticleShouldCheckFoW | optional |  |
| `set_control_point_model` | 21 | CUserMsg_ParticleManager.SetControlPointModel | optional |  |
| `set_control_point_snapshot` | 22 | CUserMsg_ParticleManager.SetControlPointSnapshot | optional |  |
| `set_texture_attribute` | 23 | CUserMsg_ParticleManager.SetTextureAttribute | optional |  |
| `set_scene_object_generic_flag` | 24 | CUserMsg_ParticleManager.SetSceneObjectGenericFlag | optional |  |
| `set_scene_object_tint_and_desat` | 25 | CUserMsg_ParticleManager.SetSceneObjectTintAndDesat | optional |  |
| `destroy_particle_named` | 26 | CUserMsg_ParticleManager.DestroyParticleNamed | optional |  |
| `particle_skip_to_time` | 27 | CUserMsg_ParticleManager.ParticleSkipToTime | optional |  |
| `particle_can_freeze` | 28 | CUserMsg_ParticleManager.ParticleCanFreeze | optional |  |
| `set_named_value_context` | 29 | CUserMsg_ParticleManager.SetParticleNamedValueContext | optional |  |
| `update_particle_transform` | 30 | CUserMsg_ParticleManager.UpdateParticleTransform | optional |  |
| `particle_freeze_transition_override` | 31 | CUserMsg_ParticleManager.ParticleFreezeTransitionOverride | optional |  |
| `freeze_particle_involving` | 32 | CUserMsg_ParticleManager.FreezeParticleInvolving | optional |  |
| `add_modellist_override_element` | 33 | CUserMsg_ParticleManager.AddModellistOverrideElement | optional |  |
| `clear_modellist_override` | 34 | CUserMsg_ParticleManager.ClearModellistOverride | optional |  |
| `create_physics_sim` | 35 | CUserMsg_ParticleManager.CreatePhysicsSim | optional |  |
| `destroy_physics_sim` | 36 | CUserMsg_ParticleManager.DestroyPhysicsSim | optional |  |
| `set_vdata` | 37 | CUserMsg_ParticleManager.SetVData | optional |  |
| `set_material_override` | 38 | CUserMsg_ParticleManager.SetMaterialOverride | optional |  |
| `add_fan` | 39 | CUserMsg_ParticleManager.AddFan | optional |  |
| `update_fan` | 40 | CUserMsg_ParticleManager.UpdateFan | optional |  |
| `set_particle_cluster_growth` | 41 | CUserMsg_ParticleManager.SetParticleClusterGrowth | optional |  |
| `remove_fan` | 42 | CUserMsg_ParticleManager.RemoveFan | optional |  |
| `create_smoke_grid` | 43 | CUserMsg_ParticleManager.CreateSmokeGrid | optional |  |
| `set_override_texture` | 44 | CUserMsg_ParticleManager.SetOverrideTexture | optional |  |

### `CUserMsg_HudError`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `order_id` | 1 | int32 | optional |  |

### `CUserMsg_CustomGameEvent`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `event_name` | 1 | string | optional |  |
| `data` | 2 | bytes | optional |  |

### `CUserMessageHapticsManagerPulse`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `hand_id` | 1 | int32 | optional |  |
| `effect_amplitude` | 2 | float | optional |  |
| `effect_frequency` | 3 | float | optional |  |
| `effect_duration` | 4 | float | optional |  |

### `CUserMessageHapticsManagerEffect`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `hand_id` | 1 | int32 | optional |  |
| `effect_name_hash_code` | 2 | uint32 | optional |  |
| `effect_scale` | 3 | float | optional |  |

### `CUserMessageAnimStateGraphState`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entity_index` | 1 | int32 | optional |  |
| `data` | 2 | bytes | optional |  |

### `CUserMessageUpdateCssClasses`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `target_world_panel` | 1 | int32 | optional |  |
| `css_classes` | 2 | string | optional |  |
| `is_add` | 3 | bool | optional |  |

### `CUserMessageServerFrameTime`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `frame_time` | 1 | float | optional |  |

### `CUserMessageLagCompensationError`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `distance` | 1 | float | optional |  |

### `CUserMessageRequestDllStatus`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `dll_action` | 1 | string | optional |  |
| `full_report` | 2 | bool | optional |  |

### `CUserMessageRequestUtilAction`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `util1` | 2 | int32 | optional |  |
| `util2` | 3 | int32 | optional |  |
| `util3` | 4 | int32 | optional |  |
| `util4` | 5 | int32 | optional |  |
| `util5` | 6 | int32 | optional |  |

### `CUserMessage_UtilMsg_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `crc` | 1 | fixed32 | optional |  |
| `item_count` | 2 | int32 | optional |  |
| `crc2` | 3 | fixed32 | optional |  |
| `item_count2` | 4 | int32 | optional |  |
| `crc_part` | 5 | int32 | repeated |  |
| `crc_part2` | 6 | int32 | repeated |  |
| `client_timestamp` | 7 | int32 | optional |  |
| `platform` | 8 | int32 | optional |  |
| `itemdetails` | 9 | CUserMessage_UtilMsg_Response.ItemDetail | repeated |  |
| `itemgroup` | 10 | int32 | optional |  |
| `total_count` | 11 | int32 | optional |  |
| `total_count2` | 12 | int32 | optional |  |

### `CUserMessage_DllStatus`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `file_report` | 1 | string | optional |  |
| `command_line` | 2 | string | optional |  |
| `total_files` | 3 | uint32 | optional |  |
| `process_id` | 4 | uint32 | optional |  |
| `osversion` | 5 | int32 | optional |  |
| `client_time` | 6 | uint64 | optional |  |
| `diagnostics` | 7 | CUserMessage_DllStatus.CVDiagnostic | repeated |  |
| `modules` | 8 | CUserMessage_DllStatus.CModule | repeated |  |

### `CUserMessageRequestInventory`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `inventory` | 1 | int32 | optional |  |
| `offset` | 2 | int32 | optional |  |
| `options` | 3 | int32 | optional |  |

### `CUserMessage_Inventory_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `crc` | 1 | fixed32 | optional |  |
| `item_count` | 2 | int32 | optional |  |
| `osversion` | 5 | int32 | optional |  |
| `perf_time` | 6 | int32 | optional |  |
| `client_timestamp` | 7 | int32 | optional |  |
| `platform` | 8 | int32 | optional |  |
| `inventories` | 9 | CUserMessage_Inventory_Response.InventoryDetail | repeated |  |
| `inventories2` | 10 | CUserMessage_Inventory_Response.InventoryDetail | repeated |  |
| `inv_type` | 11 | int32 | optional |  |
| `build_version` | 12 | int32 | optional |  |
| `instance` | 13 | int32 | optional |  |
| `inventories3` | 14 | CUserMessage_Inventory_Response.InventoryDetail | repeated |  |
| `start_time` | 15 | int64 | optional |  |

### `CUserMessageRequestDiagnostic`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `diagnostics` | 1 | CUserMessageRequestDiagnostic.Diagnostic | repeated |  |

### `CUserMessage_Diagnostic_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `diagnostics` | 1 | CUserMessage_Diagnostic_Response.Diagnostic | repeated |  |
| `build_version` | 2 | int32 | optional |  |
| `instance` | 3 | int32 | optional |  |
| `start_time` | 4 | int64 | optional |  |
| `osversion` | 5 | int32 | optional |  |
| `platform` | 6 | int32 | optional |  |

### `CUserMessage_ExtraUserData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `item` | 1 | int32 | optional |  |
| `value1` | 2 | int64 | optional |  |
| `value2` | 3 | int64 | optional |  |
| `detail1` | 4 | bytes | repeated |  |
| `detail2` | 5 | bytes | repeated |  |

### `CUserMessage_NotifyResponseFound`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ent_index` | 1 | int32 | optional | *(default: `-1`)* |
| `rule_name` | 2 | string | optional |  |
| `response_value` | 3 | string | optional |  |
| `response_concept` | 4 | string | optional |  |
| `criteria` | 5 | CUserMessage_NotifyResponseFound.Criteria | repeated |  |
| `int_criteria_names` | 6 | uint32 | repeated | *(packed)* |
| `int_criteria_values` | 7 | int32 | repeated | *(packed)* |
| `float_criteria_names` | 8 | uint32 | repeated | *(packed)* |
| `float_criteria_values` | 9 | float | repeated |  |
| `symbol_criteria_names` | 10 | uint32 | repeated | *(packed)* |
| `symbol_criteria_values` | 11 | uint32 | repeated | *(packed)* |
| `speak_result` | 12 | int32 | optional |  |

### `CUserMessage_PlayResponseConditional`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ent_index` | 1 | int32 | optional | *(default: `-1`)* |
| `player_slots` | 2 | int32 | repeated |  |
| `response` | 3 | string | optional |  |
| `ent_origin` | 4 | CMsgVector | optional |  |
| `pre_delay` | 5 | float | optional |  |
| `mix_priority` | 6 | int32 | optional |  |
