---
layout: default
title: IKSolverType
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / IKSolverType

# IKSolverType

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** animgraphlib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `IKSOLVER_Perlin` | 0 | Perlin — Classic perlin 2-bone solver |
| `IKSOLVER_TwoBone` | 1 | Two Bone — 2-bone solver that does not have singularities that Perlin does, and should be used as a default starting point for 2 bone solves. |
| `IKSOLVER_Fabrik` | 2 | FABRIK — Forward And Backward Reaching Inverse Kinematics" solver - A solver that can handle any number of bones and works by iteratively solving for the position of each bone in the chain. |
| `IKSOLVER_DogLeg3Bone` | 3 | Dog Leg (3-Bone) — A 3-bone solver that uses two 2-bone solves under the hood to emulate a dog leg. |
| `IKSOLVER_CCD` | 4 | CCD — Cyclic Coordinate Descent solver - A solver that can handle any number of bones and works by iteratively solving for the rotation of each bone in the chain. |
| `IKSOLVER_COUNT` | 5 |  |
