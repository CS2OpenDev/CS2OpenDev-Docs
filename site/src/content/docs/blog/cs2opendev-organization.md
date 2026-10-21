---
title: Introducing the CS2OpenDev Organization
date: 2026-10-21
excerpt: What CS2OpenDev is, why it exists, and what it commits to for the Counter-Strike 2 community.
---

## What is CS2OpenDev

CS2OpenDev is a GitHub organization and a set of free, MIT-licensed projects for people building Counter-Strike 2 tools. It isn't a product, a service, or a company. It's a home for the infrastructure that every CS2 project ends up rebuilding, so the next person doesn't have to build it again.

There are four repositories, and each one feeds the next:

| Project | What it does |
|---|---|
| [CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker) | Reads the shipped CS2 binaries for each game build and produces a deterministic, provenance-tracked set of files: entity schemas with offsets, a prebuilt protobuf descriptor set, ConVars, commands, game events, and game content. One set per build and platform. |
| [CS2OpenDev-Docs](https://github.com/CS2OpenDev/CS2OpenDev-Docs) | The reference site you're reading this on. Every page is generated from one SchemaTracker artifact set, with hand-written community notes layered on top. |
| [CS2OpenDev-SDK](https://github.com/CS2OpenDev/CS2OpenDev-SDK) | Turns the same schema into a strongly typed C# SDK (entity wrappers, game event records, protobuf types), published on nuget.org. |
| [CS2DemoKit](https://github.com/CS2OpenDev/CS2DemoKit) | .NET libraries for parsing and analyzing demo files, built on top of everything above. |

Everything comes from one place. The offsets on the reference site, the constants in the SDK, and the field names the demo parser reads all trace back to the same SchemaTracker output. When two of them disagree, it's because one is pinned to an older build and needs a version bump, not because two people did the research separately and got different answers.

## Why we created CS2OpenDev

Because the same work keeps getting done from scratch, and then keeps getting lost.

The CS2 tooling community has a lot of excellent projects. It also has a lot of half-finished ones: a schema dumper that stopped tracking builds after its author moved on, a parser that works fine on last year's demos, a reference page someone maintained by hand until they didn't. That's nobody's fault. It's what happens when the layer underneath everything is a personal side project instead of shared infrastructure.

What I kept running into is that the schema layer is the hard part, and it's nobody's idea of a fun problem. You want to write a demo parser, or a plugin, or an analysis tool. You don't want to reverse-engineer where `m_iHealth` lives this patch. So everyone does that work privately, at slightly different times, and gets slightly different answers. CS2OpenDev is an attempt to do it once, in public, and keep doing it.

## Our goals

**Track the game automatically.** SchemaTracker checks for a new public CS2 build every few hours and regenerates its output when one appears. A project that depends on a CS2OpenDev package should be able to pick up a new game build by bumping a version number, not by redoing research.

**Generate everything that can be generated, and test it.** Documentation pages, editor schemas, SDK types and rule catalogs are generated from upstream data and committed, and tests fail the build when a committed copy goes out of date. A hand-maintained list in the middle of a pipeline will eventually be wrong, and nobody will notice for months.

I have a small piece of evidence for that. When I recently went through CS2DemoKit's documentation and checked its claims against the code, everything that came from a generated file or was covered by a CI check was accurate. The two places that had gone wrong were both ordinary hand-written prose. One had been wrong since the day it was written. The other was right when written and was broken later by a commit that changed the behavior it described. That's a good argument for more automated checks, and a reminder that prose, including this post, needs a second look.

**Publish in formats people can actually use.** The same data is available as a browsable site, as raw Markdown that renders in an IDE or on GitHub, and as flat JSON and `.proto` files meant for build tools rather than people.

**Be honest about limits.** Every project here documents what it can't do as carefully as what it can. When a value can't be recovered from the data, we say so instead of filling in something plausible. When a published measurement turns out to be wrong, we correct it in place and leave the correction visible.

**Stay boring and stay maintained.** No rewrites for their own sake, no pile of dependencies, no "v2 that fixes everything". Infrastructure is mostly valuable because it's still there next year.

## Our commitment to the Counter-Strike community

These are listed roughly in order of how hard they would be for us to walk back.

**Free forever, MIT, no exceptions.** No paid tier, no "source-available" license, no open-core. More on this below.

**No telemetry and no accounts.** Nothing in these projects reports anything anywhere. The CS2DemoKit and SDK libraries make no network calls, so once you have a demo file, everything runs offline.

**Breaking changes are written down with the fix.** CS2DemoKit is pre-1.0, and its API still changes between versions. Every breaking change ships with a note explaining what broke, how you'll notice (a compile error, a runtime exception, or, worst case, a number that quietly changes), and what to change in your code. That list only ever gets added to.

**Measured claims, or no claims.** Performance numbers are published along with the machine, the demos used, the method, and the raw results. When a number doesn't reproduce, we say so, including when it was our own. The CS2DemoKit performance documentation has a section titled "Figures that do not reproduce", and it's there because that happened.

That performance document reads more like a lab notebook than a results page. It keeps its own retractions, the ideas that were ruled out, and the raw CSV for a measurement that went wrong. In one case, taking the median of three runs showed a 44.9% slowdown. Ten runs showed it was actually a 20.2% speedup: the timings fell into two clusters, and three samples happened to land in the wrong one. That CSV is committed, and it's more useful than the conclusion it failed to support.

**Issues get answered.** Not always quickly, and not always with a fix, but a bug report won't sit unacknowledged.

## Free and open source promise

As part of this work I created the CS2OpenDev organization on GitHub as the home for CS2DemoKit and the sibling projects that make it possible. When choosing a license, I wanted something permissive for every kind of downstream use, including commercial use. I chose MIT mainly in the hope that it encourages people with commercial plans to build on these projects instead of starting another one from scratch. Ideally, that means more of the community's effort goes into one shared set of tools, which makes new features, bug fixes, and maintenance easier for everyone.

If you're not familiar with the MIT license, here's a brief summary. Please read the full license if you have questions.

|      Can       |       Cannot        |        Must       |
|----------------|---------------------|-------------------|
| Commercial Use | Hold Project Liable | Include Copyright |
| Modify         |                     | Include License   |
| Distribute     |                     |                   |
| Sublicense     |                     |                   |
| Private Use    |                     |                   |

I'm committed to keeping all CS2OpenDev projects free and open source forever. I have no interest in personal financial gain from these or future tools that are broadly useful to the community. I'd love for the community to get behind a set of open tools and build great new projects that are also free and open source, but I want to leave the door open for anyone downstream to build great things either way.

That said, members of this organization, contributors to its projects, and anyone else involved are free to use these tools downstream under the license, the same as anyone else.

## Our position on AI tooling

I use AI tools on these projects, and I'd rather say that plainly than have you work it out yourself.

My position is that it changes *how* the work gets done, not *what the work has to prove*. The standard hasn't moved. Everything that can be generated is generated from upstream data and checked by a test. Every performance claim is measured on a named machine against named demos, with the raw results committed alongside it. The shipped rulesets' output is pinned against golden files, so a change that moves a number has to update a reviewed file too. Determinism is tested, not assumed. None of that is specific to AI. It's ordinary engineering discipline, and it's what makes "is this line right?" a more useful question than "who typed it?".

Where AI tools have been most useful is in arguing against me: asking for the case that a change is wrong, then going and measuring. That's how the "Figures that do not reproduce" section came about. A published build-speedup number turned out to be mostly the core count of the machine it ran on, not the improvement it was credited to. The corrected number is smaller and better documented.

The same approach produced a full review of the codebase that came back with a ranked list of problems. One of them was a real gap in how CS2DemoKit limits memory use on hostile input, sitting right under a README sentence that claimed the opposite. The README has been corrected, and the gap is described in [Part 1 of the technical blog](../cs2demokit-parser/#bounds-with-the-attack-written-next-to-them).

The one place I don't let it decide anything is what the game actually does. If the documentation says a field means something, that's because it was observed in real demo data, usually across a lot of frames, and the observation is written down. A plausible-sounding explanation of engine behavior is exactly the mistake to guard against, and people make it too.

These projects are also *used by* AI tools. `AGENTS.md` in the docs repository is a context file meant for other people's AI assistants to load, and the reference data is published as raw Markdown and flat JSON partly because that's what those tools fetch. Accurate, machine-readable CS2 reference data with a build id on it is useful whether you work in an editor or with an assistant, and I'd rather the community's answer to "where does `m_iHealth` live?" be a generated file than a forum post from 2023.

If you disagree with any of this, the projects are MIT and every artifact can be regenerated from the game's own files. You don't have to take my word for anything.

## How you can help

**Use it and file issues.** This is the most valuable thing you can do. Every project here has been developed against a limited set of demos, maps and game builds, and the bugs we haven't seen yet are the ones in your files.

**Send demos, or tell us what's in yours.** CS2DemoKit's tests run in CI against a small committed sample demo (four rounds), and that's the biggest gap in its test coverage. Full-match demos from different maps and game builds exercise the code paths that matter. Unusual recordings (POV demos, FACEIT or ESEA files, demos from older builds, anything that breaks) are worth more than ones that already work.

**Annotate the reference data.** The generated pages only contain what's in the game files. Community notes, like what a field means, what a ConVar actually does, or which values are safe, live in hand-edited overlay files that get merged into the generated pages. The [overlays README](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/docs/overlays/README.md) explains the format. A one-line description of a single confusing field is a perfectly good contribution.

**Write rules and share them.** CS2DemoKit's rules language exists so that "here's how I measure entry fragging" can be a file someone hands you, not a paragraph you have to turn into code yourself. A ruleset is a plain text file with no dependencies.

**Build something and tell us what was awkward.** Some of the most useful reports we've had weren't crashes. They were "I expected this to be here and it wasn't" and "I couldn't tell whether zero meant zero or meant it didn't run". Awkward APIs are real bugs.

**Contribute code.** Pull requests are welcome on all four repositories. Fair warning that the standards above apply: a performance claim needs a measurement, a behavior change needs a test, and a documentation claim about how the game works needs an observation behind it.

## Legal disclaimer, trademark and copyright acknowledgement

Counter-Strike, Counter-Strike 2, Source, Source 2, Steam and Valve are trademarks and/or registered trademarks of Valve Corporation. **CS2OpenDev is not affiliated with, endorsed by, sponsored by, or in any way officially connected to Valve Corporation.** No claim of ownership is made over any Valve intellectual property, and Valve trademarks are used here only descriptively, to identify the game these tools work with.

All original code in CS2OpenDev repositories is licensed under the MIT license. Each repository has its own `LICENSE` file and, where needed, a `THIRD-PARTY-NOTICES.md` listing adapted third-party code and its license terms. CS2DemoKit, for example, adapts parts of its bit-level decoder from [demofile-net](https://github.com/saul/demofile-net), which is also MIT licensed, and reproduces the upstream license text in full.

Data taken from Valve's shipped game files (entity schemas, protobuf definitions, console variable tables, and baked map collision geometry) remains Valve's. The tooling that extracts, transforms and presents it is ours and is MIT licensed; the game data itself isn't ours to relicense, and we don't try to. That's also why map collision data is distributed separately from the NuGet packages instead of inside them.

These projects are provided "as is", without warranty of any kind, as the MIT license says at greater length. Nothing here replaces reading the license.

If you're at Valve and something here is a problem, please [open an issue](https://github.com/CS2OpenDev/CS2OpenDev-Docs/issues) and we'll address it.
