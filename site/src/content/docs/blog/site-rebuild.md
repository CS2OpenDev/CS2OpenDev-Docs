---
title: The reference moved to Astro
date: 2026-09-02
excerpt: New URLs, working diagrams, real tables on ConVars and Commands, and a search index that no longer downloads 25 MB on every page load.
---

The reference site is off Jekyll. Same data, same build pipeline behind it, but the
pages are now rendered straight from the schema and protobuf artifacts instead of
through a generated-Markdown step, and that fixed a list of problems we had been
carrying for a while.

## URLs changed

Every old page under `/generated/...` is still served, as a static stub at its old
`.html` address that forwards to the new page and carries any `#anchor` across with it,
so a bookmark or a deep link keeps working without a 404 in between. Anything under
`/generated/` the stubs do not cover falls back to the 404 page, which applies the same
rules.

- `/generated/schemas/server/CCSPlayerPawn.html` is now `/schemas/server/CCSPlayerPawn/`
- `/generated/proto/netmessages.html` is now `/protobufs/netmessages/`
- `/generated/convars.html` is now `/convars/`
- `/generated/diagrams/server_hierarchy.html` is now `/schemas/hierarchy/`, and every
  module gets its own `/schemas/<module>/hierarchy/`

Case is preserved in entity names (`C_CSPlayerPawn` stays `C_CSPlayerPawn`, it does not
get lowercased), and `::` in a nested type name becomes `.` in the URL because that is
the one character a path cannot carry.

## What was actually wrong before

A few of these had been broken long enough that we stopped noticing:

**Server pages could show client offsets.** Base-class resolution picked whichever
same-named class it found first, so some server entities inherited fields at the
client build's offsets instead of the server build's. An offset is useless if it is
from the wrong binary, and there was no way to tell from the page that it had happened.
The new generator resolves a class's bases within its own project first and asserts
against the whole schema at build time that this never regresses.

**ConVars and Commands had no table.** Multi-line descriptions broke the Markdown
table syntax, the entire block fell back to one paragraph, and both pages had been
rendering as a wall of pipe characters since at least July. You could not read either
page. Both are now rendered straight from the structured console-variable and
console-command data instead of through hand-escaped Markdown, which is what was
breaking.

**Diagrams did not render.** A quoting bug meant any class name containing `::`
produced a mermaid parse error instead of a diagram, and that included the module
diagrams for `server`, `client`, and the site's one hierarchy overview. We replaced
the module diagrams with collapsible inheritance trees, which scale to a
thousand-plus classes in a module in a way a single diagram never will, and kept a
diagram alongside the tree for the modules small enough for one to still be useful.

**Nested protobuf types were undocumented.** 153 nested messages and 15 nested enums,
including the string-table row type and the type that carries every game event's
key-value pairs, had no heading anywhere on the old proto pages. Fields pointing at
them were dead text pointing nowhere. The new protobuf pages are built to flatten and
link nested types instead of only walking the top-level ones.

## Search that does not download 25 MB

The old search index was a single 25 MB JSON file, rebuilt in the browser on every
page load: about four seconds of main-thread work and roughly a gigabyte of heap,
every time, whether or not you searched. It's a chunked, prebuilt index now, so a
search costs tens of kilobytes for the terms you actually typed rather than the whole
site up front.

## Report a problem

Something look wrong, missing, or worse than the old site in a specific way? File it
on [the GitHub repo](https://github.com/CS2OpenDev/CS2OpenDev-Docs/issues).
