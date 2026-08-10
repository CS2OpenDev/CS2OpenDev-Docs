---
layout: default
title: PulseInstructionCode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / PulseInstructionCode_t

# PulseInstructionCode_t

**Kind:** enum · **Underlying:** `uint16_t` · **Module:** pulse_runtime_lib

## Values

| Name | Value | Description |
|------|-------|-------------|
| `INVALID` | 0 |  |
| `IMMEDIATE_HALT` | 1 |  |
| `RETURN_VOID` | 2 |  |
| `RETURN_VALUE` | 3 |  |
| `NOP` | 4 |  |
| `JUMP` | 5 |  |
| `JUMP_COND` | 6 |  |
| `CHUNK_LEAP` | 7 |  |
| `CHUNK_LEAP_COND` | 8 |  |
| `PULSE_CALL_SYNC` | 9 |  |
| `PULSE_CALL_ASYNC_FIRE` | 10 |  |
| `CREATE_CHILD_CURSOR_OUTFLOW` | 11 |  |
| `CELL_INVOKE` | 12 |  |
| `LIBRARY_INVOKE` | 13 |  |
| `SET_VAR` | 14 |  |
| `GET_VAR` | 15 |  |
| `GET_VAR_DETACH` | 16 |  |
| `DETACH_REGISTER` | 17 |  |
| `SET_VAR_ARRAY_ELEMENT_1D` | 18 |  |
| `SET_VAR_OBSERVABLE` | 19 |  |
| `GET_CONST` | 20 |  |
| `GET_ARRAY_ELEMENT` | 21 |  |
| `GET_DOMAIN_VALUE` | 22 |  |
| `COPY` | 23 |  |
| `NOT` | 24 |  |
| `NEGATE` | 25 |  |
| `ADD` | 26 |  |
| `SUB` | 27 |  |
| `MUL` | 28 |  |
| `DIV` | 29 |  |
| `MOD` | 30 |  |
| `LT` | 31 |  |
| `LTE` | 32 |  |
| `EQ` | 33 |  |
| `NE` | 34 |  |
| `AND` | 35 |  |
| `OR` | 36 |  |
| `SCALE` | 37 |  |
| `SCALE_INV` | 38 |  |
| `ELEMENT_ACCESS` | 39 |  |
| `CONVERT_VALUE` | 40 |  |
| `REINTERPRET_INSTANCE` | 41 |  |
| `GET_BLACKBOARD_REFERENCE` | 42 |  |
| `SET_BLACKBOARD_REFERENCE` | 43 |  |
| `LAST_SERIALIZED_CODE` | 44 |  |
| `NEGATE_INT` | 45 |  |
| `NEGATE_FLOAT` | 46 |  |
| `NEGATE_VEC2` | 47 |  |
| `NEGATE_VEC3` | 48 |  |
| `NEGATE_VEC4` | 49 |  |
| `ADD_INT` | 50 |  |
| `ADD_FLOAT` | 51 |  |
| `ADD_STRING` | 52 |  |
| `ADD_VEC2` | 53 |  |
| `ADD_VEC3` | 54 |  |
| `ADD_VEC3WS_VEC3` | 55 |  |
| `ADD_VEC3_VEC3WS` | 56 |  |
| `ADD_VEC4` | 57 |  |
| `ADD_GAMETIME_FLOAT` | 58 |  |
| `ADD_FLOAT_GAMETIME` | 59 |  |
| `SUB_INT` | 60 |  |
| `SUB_FLOAT` | 61 |  |
| `SUB_VEC2` | 62 |  |
| `SUB_VEC3` | 63 |  |
| `SUB_VEC3WS_VEC3` | 64 |  |
| `SUB_VEC3WS_VEC3WS` | 65 |  |
| `SUB_VEC4` | 66 |  |
| `SUB_GAMETIME_FLOAT` | 67 |  |
| `SUB_GAMETIME` | 68 |  |
| `MUL_INT` | 69 |  |
| `MUL_FLOAT` | 70 |  |
| `DIV_FLOAT` | 71 |  |
| `MOD_INT` | 72 |  |
| `MOD_FLOAT` | 73 |  |
| `LT_INT` | 74 |  |
| `LT_FLOAT` | 75 |  |
| `LT_GAMETIME` | 76 |  |
| `LTE_INT` | 77 |  |
| `LTE_FLOAT` | 78 |  |
| `LTE_GAMETIME` | 79 |  |
| `EQ_BOOL` | 80 |  |
| `EQ_INT` | 81 |  |
| `EQ_FLOAT` | 82 |  |
| `EQ_VEC2` | 83 |  |
| `EQ_VEC3` | 84 |  |
| `EQ_VEC3WS` | 85 |  |
| `EQ_VEC4` | 86 |  |
| `EQ_STRING` | 87 |  |
| `EQ_ENTITY_NAME` | 88 |  |
| `EQ_SCHEMA_ENUM` | 89 |  |
| `EQ_EHANDLE` | 90 |  |
| `EQ_PANEL_HANDLE` | 91 |  |
| `EQ_OPAQUE_HANDLE` | 92 |  |
| `EQ_TEST_HANDLE` | 93 |  |
| `EQ_COLOR_RGB` | 94 |  |
| `EQ_ARRAY` | 95 |  |
| `EQ_GAMETIME` | 96 |  |
| `NE_BOOL` | 97 |  |
| `NE_INT` | 98 |  |
| `NE_FLOAT` | 99 |  |
| `NE_VEC2` | 100 |  |
| `NE_VEC3` | 101 |  |
| `NE_VEC3WS` | 102 |  |
| `NE_VEC4` | 103 |  |
| `NE_STRING` | 104 |  |
| `NE_ENTITY_NAME` | 105 |  |
| `NE_SCHEMA_ENUM` | 106 |  |
| `NE_EHANDLE` | 107 |  |
| `NE_PANEL_HANDLE` | 108 |  |
| `NE_OPAQUE_HANDLE` | 109 |  |
| `NE_TEST_HANDLE` | 110 |  |
| `NE_COLOR_RGB` | 111 |  |
| `NE_ARRAY` | 112 |  |
| `NE_GAMETIME` | 113 |  |
| `SCALE_VEC3` | 114 |  |
| `SCALE_VEC2` | 115 |  |
| `SCALE_VEC4` | 116 |  |
| `SCALE_INV_VEC3` | 117 |  |
| `SCALE_INV_VEC2` | 118 |  |
| `SCALE_INV_VEC4` | 119 |  |
| `ELEMENT_ACCESS_VEC2` | 120 |  |
| `ELEMENT_ACCESS_VEC3` | 121 |  |
| `ELEMENT_ACCESS_VEC3WS` | 122 |  |
| `ELEMENT_ACCESS_VEC4` | 123 |  |
| `ELEMENT_ACCESS_COLOR_RGB` | 124 |  |
| `GET_CONST_INLINE_STORAGE` | 125 |  |
