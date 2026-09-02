---
layout: default
title: smartprops
parent: Schemas
nav_exclude: true
---

# Module: smartprops

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/smartprops.md)

167 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CPulseGraphInstance_SmartPropEval](smartprops/CPulseGraphInstance_SmartPropEval.md) | class | 288 | 0 | [CBasePulseGraphInstance](pulse_runtime_lib/CBasePulseGraphInstance.md) |
| [CSmartPropAPI](smartprops/CSmartPropAPI.md) | class | 1 | 0 |  |
| [CSmartPropAttributeApplyColorMode](smartprops/CSmartPropAttributeApplyColorMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeChoiceSelectionMode](smartprops/CSmartPropAttributeChoiceSelectionMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeColorSelectionMode](smartprops/CSmartPropAttributeColorSelectionMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeCoordinateSpace](smartprops/CSmartPropAttributeCoordinateSpace.md) | class | 64 | 0 |  |
| [CSmartPropAttributeDirection](smartprops/CSmartPropAttributeDirection.md) | class | 64 | 0 |  |
| [CSmartPropAttributeDistributionMode](smartprops/CSmartPropAttributeDistributionMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeGridOriginMode](smartprops/CSmartPropAttributeGridOriginMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeGridPlacementMode](smartprops/CSmartPropAttributeGridPlacementMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeOrientationMode](smartprops/CSmartPropAttributeOrientationMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributePathPositions](smartprops/CSmartPropAttributePathPositions.md) | class | 64 | 0 |  |
| [CSmartPropAttributePickMode](smartprops/CSmartPropAttributePickMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeRadiusPlacementMode](smartprops/CSmartPropAttributeRadiusPlacementMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeScaleMode](smartprops/CSmartPropAttributeScaleMode.md) | class | 64 | 0 |  |
| [CSmartPropAttributeTraceNoHit](smartprops/CSmartPropAttributeTraceNoHit.md) | class | 64 | 0 |  |
| [CSmartPropChoice](smartprops/CSmartPropChoice.md) | class | 56 | 3 | [CSmartPropParameter](smartprops/CSmartPropParameter.md) |
| [CSmartPropChoiceOption](smartprops/CSmartPropChoiceOption.md) | class | 40 | 3 |  |
| [CSmartPropElement](smartprops/CSmartPropElement.md) | class | 136 | 5 |  |
| [CSmartPropElement_BendDeformer](smartprops/CSmartPropElement_BendDeformer.md) | class | 608 | 7 | [CSmartPropElement_Deformer](smartprops/CSmartPropElement_Deformer.md) |
| [CSmartPropElement_Deformer](smartprops/CSmartPropElement_Deformer.md) | class | 160 | 0 | [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) |
| [CSmartPropElement_FitOnLine](smartprops/CSmartPropElement_FitOnLine.md) | class | 736 | 9 | [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) |
| [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) | class | 160 | 1 | [CSmartPropElement](smartprops/CSmartPropElement.md) |
| [CSmartPropElement_Layout2DGrid](smartprops/CSmartPropElement_Layout2DGrid.md) | class | 928 | 12 | [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) |
| [CSmartPropElement_MidpointDeformer](smartprops/CSmartPropElement_MidpointDeformer.md) | class | 744 | 10 | [CSmartPropElement_Deformer](smartprops/CSmartPropElement_Deformer.md) |
| [CSmartPropElement_Model](smartprops/CSmartPropElement_Model.md) | class | 784 | 11 | [CSmartPropElement](smartprops/CSmartPropElement.md) |
| [CSmartPropElement_ModelEntity](smartprops/CSmartPropElement_ModelEntity.md) | class | 400 | 6 | [CSmartPropElement](smartprops/CSmartPropElement.md) |
| [CSmartPropElement_ModifyState](smartprops/CSmartPropElement_ModifyState.md) | class | 136 | 0 | [CSmartPropElement](smartprops/CSmartPropElement.md) |
| [CSmartPropElement_PickOne](smartprops/CSmartPropElement_PickOne.md) | class | 560 | 8 | [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) |
| [CSmartPropElement_PlaceInSphere](smartprops/CSmartPropElement_PlaceInSphere.md) | class | 800 | 10 | [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) |
| [CSmartPropElement_PlaceMultiple](smartprops/CSmartPropElement_PlaceMultiple.md) | class | 232 | 2 | [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) |
| [CSmartPropElement_PlaceOnMesh](smartprops/CSmartPropElement_PlaceOnMesh.md) | class | 232 | 2 | [CSmartPropElement_Deformer](smartprops/CSmartPropElement_Deformer.md) |
| [CSmartPropElement_PlaceOnPath](smartprops/CSmartPropElement_PlaceOnPath.md) | class | 768 | 11 | [CSmartPropElement_Group](smartprops/CSmartPropElement_Group.md) |
| [CSmartPropElement_PropDynamic](smartprops/CSmartPropElement_PropDynamic.md) | class | 400 | 0 | [CSmartPropElement_ModelEntity](smartprops/CSmartPropElement_ModelEntity.md) |
| [CSmartPropElement_PropPhysics](smartprops/CSmartPropElement_PropPhysics.md) | class | 464 | 1 | [CSmartPropElement_ModelEntity](smartprops/CSmartPropElement_ModelEntity.md) |
| [CSmartPropElement_SmartProp](smartprops/CSmartPropElement_SmartProp.md) | class | 368 | 2 | [CSmartPropElement](smartprops/CSmartPropElement.md) |
| [CSmartPropExprAPI](smartprops/CSmartPropExprAPI.md) | class | 1 | 0 |  |
| [CSmartPropFilter](smartprops/CSmartPropFilter.md) | class | 80 | 0 | [CSmartPropModifier](smartprops/CSmartPropModifier.md) |
| [CSmartPropFilterAPI](smartprops/CSmartPropFilterAPI.md) | class | 1 | 0 |  |
| [CSmartPropFilter_Expression](smartprops/CSmartPropFilter_Expression.md) | class | 88 | 1 | [CSmartPropFilter](smartprops/CSmartPropFilter.md) |
| [CSmartPropFilter_MaterialAttributes](smartprops/CSmartPropFilter_MaterialAttributes.md) | class | 128 | 2 | [CSmartPropFilter](smartprops/CSmartPropFilter.md) |
| [CSmartPropFilter_Probability](smartprops/CSmartPropFilter_Probability.md) | class | 144 | 1 | [CSmartPropFilter](smartprops/CSmartPropFilter.md) |
| [CSmartPropFilter_SurfaceAngle](smartprops/CSmartPropFilter_SurfaceAngle.md) | class | 208 | 2 | [CSmartPropFilter](smartprops/CSmartPropFilter.md) |
| [CSmartPropFilter_SurfaceProperties](smartprops/CSmartPropFilter_SurfaceProperties.md) | class | 128 | 2 | [CSmartPropFilter](smartprops/CSmartPropFilter.md) |
| [CSmartPropFilter_VariableValue](smartprops/CSmartPropFilter_VariableValue.md) | class | 112 | 1 | [CSmartPropFilter](smartprops/CSmartPropFilter.md) |
| [CSmartPropMaterialReplacement](smartprops/CSmartPropMaterialReplacement.md) | class | 128 | 2 |  |
| [CSmartPropModifier](smartprops/CSmartPropModifier.md) | class | 80 | 1 |  |
| [CSmartPropOperation](smartprops/CSmartPropOperation.md) | class | 80 | 0 | [CSmartPropModifier](smartprops/CSmartPropModifier.md) |
| [CSmartPropOperationAPI](smartprops/CSmartPropOperationAPI.md) | class | 1 | 0 |  |
| [CSmartPropOperation_ComputeCrossProduct3D](smartprops/CSmartPropOperation_ComputeCrossProduct3D.md) | class | 216 | 3 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_ComputeDistance3D](smartprops/CSmartPropOperation_ComputeDistance3D.md) | class | 408 | 6 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_ComputeDotProduct3D](smartprops/CSmartPropOperation_ComputeDotProduct3D.md) | class | 216 | 3 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_ComputeNormalizedVector3D](smartprops/CSmartPropOperation_ComputeNormalizedVector3D.md) | class | 152 | 2 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_ComputeProjectVector3D](smartprops/CSmartPropOperation_ComputeProjectVector3D.md) | class | 472 | 7 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_ComputeVectorBetweenPoints3D](smartprops/CSmartPropOperation_ComputeVectorBetweenPoints3D.md) | class | 472 | 7 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_CreateLocator](smartprops/CSmartPropOperation_CreateLocator.md) | class | 472 | 7 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_CreateRotator](smartprops/CSmartPropOperation_CreateRotator.md) | class | 800 | 13 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_CreateSizer](smartprops/CSmartPropOperation_CreateSizer.md) | class | 968 | 20 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_MaterialOverride](smartprops/CSmartPropOperation_MaterialOverride.md) | class | 168 | 2 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_MaterialReplacementAPI](smartprops/CSmartPropOperation_MaterialReplacementAPI.md) | class | 1 | 0 |  |
| [CSmartPropOperation_MaterialTint](smartprops/CSmartPropOperation_MaterialTint.md) | class | 360 | 5 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_RandomColorTintColor](smartprops/CSmartPropOperation_RandomColorTintColor.md) | class | 240 | 4 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_RandomOffset](smartprops/CSmartPropOperation_RandomOffset.md) | class | 272 | 3 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_RandomRotation](smartprops/CSmartPropOperation_RandomRotation.md) | class | 272 | 3 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_RandomScale](smartprops/CSmartPropOperation_RandomScale.md) | class | 272 | 3 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_ResetRotation](smartprops/CSmartPropOperation_ResetRotation.md) | class | 336 | 4 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_ResetScale](smartprops/CSmartPropOperation_ResetScale.md) | class | 144 | 1 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_RestoreState](smartprops/CSmartPropOperation_RestoreState.md) | class | 208 | 2 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_RigidDeformation](smartprops/CSmartPropOperation_RigidDeformation.md) | class | 80 | 0 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_Rotate](smartprops/CSmartPropOperation_Rotate.md) | class | 144 | 1 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_RotateTowards](smartprops/CSmartPropOperation_RotateTowards.md) | class | 528 | 7 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_SaveColor](smartprops/CSmartPropOperation_SaveColor.md) | class | 88 | 1 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_SaveDirection](smartprops/CSmartPropOperation_SaveDirection.md) | class | 216 | 3 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_SavePosition](smartprops/CSmartPropOperation_SavePosition.md) | class | 152 | 2 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_SaveScale](smartprops/CSmartPropOperation_SaveScale.md) | class | 88 | 1 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_SaveState](smartprops/CSmartPropOperation_SaveState.md) | class | 88 | 1 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_SaveSurfaceNormal](smartprops/CSmartPropOperation_SaveSurfaceNormal.md) | class | 152 | 2 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_Scale](smartprops/CSmartPropOperation_Scale.md) | class | 144 | 1 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_SetMateraialGroupChoice](smartprops/CSmartPropOperation_SetMateraialGroupChoice.md) | class | 240 | 4 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_SetOrientation](smartprops/CSmartPropOperation_SetOrientation.md) | class | 400 | 5 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_SetPosition](smartprops/CSmartPropOperation_SetPosition.md) | class | 208 | 2 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_SetTintColor](smartprops/CSmartPropOperation_SetTintColor.md) | class | 296 | 4 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_SetVariable](smartprops/CSmartPropOperation_SetVariable.md) | class | 144 | 1 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropOperation_Trace](smartprops/CSmartPropOperation_Trace.md) | class | 848 | 12 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropOperation_TraceInDirection](smartprops/CSmartPropOperation_TraceInDirection.md) | class | 1040 | 3 | [CSmartPropOperation_Trace](smartprops/CSmartPropOperation_Trace.md) |
| [CSmartPropOperation_TraceToLine](smartprops/CSmartPropOperation_TraceToLine.md) | class | 1232 | 6 | [CSmartPropOperation_Trace](smartprops/CSmartPropOperation_Trace.md) |
| [CSmartPropOperation_TraceToPoint](smartprops/CSmartPropOperation_TraceToPoint.md) | class | 1104 | 4 | [CSmartPropOperation_Trace](smartprops/CSmartPropOperation_Trace.md) |
| [CSmartPropOperation_Translate](smartprops/CSmartPropOperation_Translate.md) | class | 208 | 2 | [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) |
| [CSmartPropParameter](smartprops/CSmartPropParameter.md) | class | 16 | 1 |  |
| [CSmartPropPulse_BaseQueryableFlow](smartprops/CSmartPropPulse_BaseQueryableFlow.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropPulse_CreateLocator](smartprops/CSmartPropPulse_CreateLocator.md) | class | 80 | 1 | [CSmartPropPulse_BaseQueryableFlow](smartprops/CSmartPropPulse_BaseQueryableFlow.md) |
| [CSmartPropPulse_CreateRotator](smartprops/CSmartPropPulse_CreateRotator.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropPulse_CreateSizer](smartprops/CSmartPropPulse_CreateSizer.md) | class | 88 | 7 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropPulse_CriteriaPathPosition](smartprops/CSmartPropPulse_CriteriaPathPosition.md) | class | 72 | 0 | [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) |
| [CSmartPropPulse_CriteriaPathPosition::Criteria_t](smartprops/CSmartPropPulse_CriteriaPathPosition.Criteria_t.md) | class | 16 | 5 |  |
| [CSmartPropPulse_FitOnLine](smartprops/CSmartPropPulse_FitOnLine.md) | class | 96 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropPulse_Group](smartprops/CSmartPropPulse_Group.md) | class | 96 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropPulse_PickOneSelector](smartprops/CSmartPropPulse_PickOneSelector.md) | class | 104 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropPulse_PlaceInSphere](smartprops/CSmartPropPulse_PlaceInSphere.md) | class | 144 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropPulse_PlaceOnPath](smartprops/CSmartPropPulse_PlaceOnPath.md) | class | 104 | 2 | [CSmartPropPulse_BaseQueryableFlow](smartprops/CSmartPropPulse_BaseQueryableFlow.md) |
| [CSmartPropPulse_SelectionChoiceWeight](smartprops/CSmartPropPulse_SelectionChoiceWeight.md) | class | 72 | 0 | [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) |
| [CSmartPropPulse_SelectionChoiceWeight::Criteria_t](smartprops/CSmartPropPulse_SelectionChoiceWeight.Criteria_t.md) | class | 4 | 1 |  |
| [CSmartPropPulse_SelectionEndCap](smartprops/CSmartPropPulse_SelectionEndCap.md) | class | 72 | 0 | [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) |
| [CSmartPropPulse_SelectionEndCap::Criteria_t](smartprops/CSmartPropPulse_SelectionEndCap.Criteria_t.md) | class | 2 | 2 |  |
| [CSmartPropPulse_SelectionLinearLength](smartprops/CSmartPropPulse_SelectionLinearLength.md) | class | 72 | 0 | [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) |
| [CSmartPropPulse_SelectionLinearLength::Criteria_t](smartprops/CSmartPropPulse_SelectionLinearLength.Criteria_t.md) | class | 16 | 4 |  |
| [CSmartPropPulse_SmartProp](smartprops/CSmartPropPulse_SmartProp.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CSmartPropRoot](smartprops/CSmartPropRoot.md) | class | 208 | 7 |  |
| [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) | class | 72 | 1 |  |
| [CSmartPropSelectionCriteria_ChoiceWeight](smartprops/CSmartPropSelectionCriteria_ChoiceWeight.md) | class | 136 | 1 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_EdgeAngleCriteria](smartprops/CSmartPropSelectionCriteria_EdgeAngleCriteria.md) | class | 264 | 3 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_EndCap](smartprops/CSmartPropSelectionCriteria_EndCap.md) | class | 200 | 2 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_IsValid](smartprops/CSmartPropSelectionCriteria_IsValid.md) | class | 80 | 1 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_LinearLength](smartprops/CSmartPropSelectionCriteria_LinearLength.md) | class | 328 | 4 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_MaterialCriteria](smartprops/CSmartPropSelectionCriteria_MaterialCriteria.md) | class | 200 | 2 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_PathPosition](smartprops/CSmartPropSelectionCriteria_PathPosition.md) | class | 392 | 5 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_TopoEdgeCountCriteria](smartprops/CSmartPropSelectionCriteria_TopoEdgeCountCriteria.md) | class | 264 | 3 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropSelectionCriteria_VertexCountCriteria](smartprops/CSmartPropSelectionCriteria_VertexCountCriteria.md) | class | 136 | 1 | [CSmartPropSelectionCriteria](smartprops/CSmartPropSelectionCriteria.md) |
| [CSmartPropTransformOperation](smartprops/CSmartPropTransformOperation.md) | class | 80 | 0 | [CSmartPropOperation](smartprops/CSmartPropOperation.md) |
| [CSmartPropVariable](smartprops/CSmartPropVariable.md) | class | 56 | 5 | [CSmartPropParameter](smartprops/CSmartPropParameter.md) |
| [CSmartPropVariable_Angles](smartprops/CSmartPropVariable_Angles.md) | class | 72 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_ApplyColorMode](smartprops/CSmartPropVariable_ApplyColorMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Bool](smartprops/CSmartPropVariable_Bool.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_ChoiceSelectionMode](smartprops/CSmartPropVariable_ChoiceSelectionMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Color](smartprops/CSmartPropVariable_Color.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_ColorSelectionMode](smartprops/CSmartPropVariable_ColorSelectionMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_CoordinateSpace](smartprops/CSmartPropVariable_CoordinateSpace.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_DirectionVector](smartprops/CSmartPropVariable_DirectionVector.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_DistributionMode](smartprops/CSmartPropVariable_DistributionMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Float](smartprops/CSmartPropVariable_Float.md) | class | 72 | 3 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_GridOriginMode](smartprops/CSmartPropVariable_GridOriginMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_GridPlacementMode](smartprops/CSmartPropVariable_GridPlacementMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Int](smartprops/CSmartPropVariable_Int.md) | class | 72 | 3 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Material](smartprops/CSmartPropVariable_Material.md) | class | 280 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_MaterialGroup](smartprops/CSmartPropVariable_MaterialGroup.md) | class | 288 | 2 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Model](smartprops/CSmartPropVariable_Model.md) | class | 280 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_OrientationMode](smartprops/CSmartPropVariable_OrientationMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_PathPositions](smartprops/CSmartPropVariable_PathPositions.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_PickMode](smartprops/CSmartPropVariable_PickMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_RadiusPlacementMode](smartprops/CSmartPropVariable_RadiusPlacementMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_ScaleMode](smartprops/CSmartPropVariable_ScaleMode.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_String](smartprops/CSmartPropVariable_String.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_SurfaceProperty](smartprops/CSmartPropVariable_SurfaceProperty.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_TraceNoHit](smartprops/CSmartPropVariable_TraceNoHit.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Vector2D](smartprops/CSmartPropVariable_Vector2D.md) | class | 64 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Vector3D](smartprops/CSmartPropVariable_Vector3D.md) | class | 72 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [CSmartPropVariable_Vector4D](smartprops/CSmartPropVariable_Vector4D.md) | class | 72 | 1 | [CSmartPropVariable](smartprops/CSmartPropVariable.md) |
| [ColorChoice_t](smartprops/ColorChoice_t.md) | class | 128 | 2 |  |
| [MaterialGroupChoice_t](smartprops/MaterialGroupChoice_t.md) | class | 128 | 2 |  |
| [ApplyColorMode_t](smartprops/ApplyColorMode_t.md) | enum | — | 3 |  |
| [ConfigurationHandleShape_t](smartprops/ConfigurationHandleShape_t.md) | enum | — | 4 |  |
| [PickMode_t](smartprops/PickMode_t.md) | enum | — | 3 |  |
| [ScaleMode_t](smartprops/ScaleMode_t.md) | enum | — | 4 |  |
| [SmartPropChoiceSelectionMode_t](smartprops/SmartPropChoiceSelectionMode_t.md) | enum | — | 3 |  |
| [SmartPropColorSelectionMode_t](smartprops/SmartPropColorSelectionMode_t.md) | enum | — | 4 |  |
| [SmartPropDeformableAttachMode_t](smartprops/SmartPropDeformableAttachMode_t.md) | enum | — | 3 |  |
| [SmartPropDeformableOrientMode_t](smartprops/SmartPropDeformableOrientMode_t.md) | enum | — | 5 |  |
| [SmartPropDetailFadeLevel_t](smartprops/SmartPropDetailFadeLevel_t.md) | enum | — | 6 |  |
| [SmartPropDirection_t](smartprops/SmartPropDirection_t.md) | enum | — | 3 |  |
| [SmartPropDistributionMode_t](smartprops/SmartPropDistributionMode_t.md) | enum | — | 2 |  |
| [SmartPropGridOriginBasis_t](smartprops/SmartPropGridOriginBasis_t.md) | enum | — | 2 |  |
| [SmartPropGridPlacementMode_t](smartprops/SmartPropGridPlacementMode_t.md) | enum | — | 2 |  |
| [SmartPropPathPositions_t](smartprops/SmartPropPathPositions_t.md) | enum | — | 4 |  |
| [SmartPropPlaceMeshOrientationMode_t](smartprops/SmartPropPlaceMeshOrientationMode_t.md) | enum | — | 4 |  |
| [SmartPropRadiusPlacementMode_t](smartprops/SmartPropRadiusPlacementMode_t.md) | enum | — | 2 |  |
| [SmartPropSpace_t](smartprops/SmartPropSpace_t.md) | enum | — | 3 |  |
| [TraceNoHitResult_t](smartprops/TraceNoHitResult_t.md) | enum | — | 4 |  |
