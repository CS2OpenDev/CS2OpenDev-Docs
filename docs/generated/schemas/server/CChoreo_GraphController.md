---
title: CChoreo_GraphController
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CChoreo_GraphController

# CChoreo_GraphController

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 264 bytes (`0x108`) · **Align:** 8 · **Module:** server

**Inherits from:** [CAnimGraphControllerBase](../server/CAnimGraphControllerBase.md)

**Relationships:**

```mermaid
classDiagram
    CAnimGraphControllerBase <|-- CChoreo_GraphController
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x4c` | `m_hExternalGraph` | [ExternalAnimGraphHandle_t](../server/ExternalAnimGraphHandle_t.md) | [CAnimGraphControllerBase](../server/CAnimGraphControllerBase.md) |  |
| `0xc0` | `m_eChoreoState` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |  |
| `0xd8` | `m_tChoreoTargetWarp` | CAnimGraph2ParamOptionalRef< CTransform > |  |  |
| `0xf0` | `m_tChoreoExitWarp` | CAnimGraph2ParamOptionalRef< CTransform > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CChoreo_GraphController&quot;,
	&quot;m_hExternalGraph&quot;: 4294967295,
	&quot;m_eChoreoState&quot;: null,
	&quot;m_tChoreoTargetWarp&quot;: null,
	&quot;m_tChoreoExitWarp&quot;: null
}</pre>
</details>
