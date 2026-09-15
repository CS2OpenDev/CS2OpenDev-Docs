---
title: CS2OpenDev Organization Introduction
date: 2026-09-12
excerpt: An introduction for the CS2OpenDev organization, its goals and commitments to the Counter-Strike 2 Community
---

## What is CS2OpenDev

CS2OpenDev is a GitHub organization and a set of free, MIT-licensed projects for people building Counter-Strike 2 tools. It is not a product, a service, or a company. It is a place to put the unglamorous infrastructure that every CS2 project ends up rebuilding, so that the next person does not have to.

Four repositories, each feeding the next:

| Project | What it does |
|---|---|
| [CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker) | Walks the shipped CS2 binaries on every game build and emits a deterministic, provenance-tracked artifact set: entity schemas with offsets, a prebuilt protobuf descriptor set, ConVars, commands, game events, and a game-content layer. One artifact set per build and platform. |
| [CS2OpenDev-Docs](https://github.com/CS2OpenDev/CS2OpenDev-Docs) | The reference site you are reading this on. Every page is generated from one SchemaTracker artifact set, with hand-written community annotations layered on top. |
| [CS2OpenDev-SDK](https://github.com/CS2OpenDev/CS2OpenDev-SDK) | Turns the same upstream schema into a statically typed C# SDK — entity wrappers, game event records, protobuf types — published to nuget.org. |
| [CS2DemoKit](https://github.com/CS2OpenDev/CS2DemoKit) | .NET libraries for parsing and analysing demo files, built on top of all of the above. |

The through-line is that everything derives from one place. The offsets on the reference site, the constants in the SDK, and the field names the demo parser reads are all projections of the same artifact set, so they describe the same game build and cannot quietly drift apart. That is the whole architectural idea, and most of the work is in keeping it true.

## Why Did We Create CS2OpenDev

Because the same work keeps being done from scratch, and then keeps being lost.

The CS2 tooling community is full of genuinely excellent projects. It is also full of half-finished ones — a schema dumper that stopped tracking builds after the author moved on, a parser that works beautifully on last year's demos, a reference page someone maintained by hand until they did not. None of that is anyone's fault. It is what happens when the boring layer underneath everything is a personal side project rather than shared infrastructure.

The specific thing I kept running into was that the schema layer is the hard part and it is *nobody's* interesting problem. You want to write a demo parser, or a plugin, or an analysis tool. You do not want to reverse-engineer where `m_iHealth` lives this patch. So everyone pays that tax privately, at a slightly different time, and gets a slightly different answer.

CS2OpenDev exists to pay that tax once, in public, and to keep paying it.

## What Are Our Goals

**Track the game, automatically.** Schema tracking runs on a schedule and rebuilds on every new game build. A project that pins to a CS2OpenDev package should be able to pick up a new CS2 build by bumping a version number, not by re-doing research.

**Generate everything that can be generated, and gate it.** Documentation pages, editor schemas, SDK types, rule catalogues — all generated from upstream artifacts and committed, with tests that fail the build when a committed copy goes stale. A hand-maintained list in the middle of a pipeline is a list that will eventually be wrong, and wrong in a way nobody notices for months.

We have accidental evidence for that one. A recent full audit of CS2DemoKit's documentation checked every claim against the code, and the result split cleanly: **everything anchored to a generated artifact or a CI gate was accurate, and the only two confirmed rot sites were ungated narrative prose.** Not the oldest docs. Not the longest ones. The ungated ones. One had been wrong since the day it was written; the other was true when written and was quietly inverted by a later commit that changed the behaviour it described. Accuracy tracked the presence of a gate and nothing else — which is a good argument for having more gates and a sobering one about prose in general, this post included.

**Publish in shapes that are actually consumable.** The same data is available as a browsable site, as raw Markdown that renders in an IDE or on GitHub, and as flat JSON and `.proto` files meant for a build step rather than a human. Different consumers, same source.

**Be honest about limits.** Every project here documents what it cannot do as carefully as what it can. Where a value is not recoverable from the data, we say so rather than interpolating something plausible. Where a published measurement turned out to be wrong, we correct it in place and leave the correction visible. That is a slower way to write documentation and it is the only version worth having.

**Stay boring and stay maintained.** No breaking rewrites for their own sake, no dependency sprawl, no "v2 that fixes everything". The value of infrastructure is almost entirely in it still being there next year.

## Our Commitment to the Counter-Strike Community

Concretely, and in order of how much they would cost us to walk back:

**Free forever, MIT, no exceptions.** Not free-with-a-commercial-tier, not source-available, not open-core. See the next section.

**No telemetry, no phoning home, no account.** Nothing in any of these projects reports anything anywhere. The libraries do not make network calls. You can run all of it air-gapped.

**Breaking changes get written down with their mechanism and their fix.** CS2DemoKit is pre-1.0 and the API does still move. Every break ships with an entry explaining what breaks, how you will find out (compile error, runtime exception, or — worst case — a silently different number), and what to change. That list is append-only.

**Measured claims, or no claims.** Performance numbers get published with the machine, the corpus, the methodology and the raw rows. When a number does not reproduce, we say it does not reproduce, including when it was our own number. There is a section in the CS2DemoKit performance documentation titled "Figures that do not reproduce", and it exists because that is exactly what happened.

The performance doc is kept as a lab notebook rather than a results page: it carries its own retractions, the hypotheses that were ruled out and what ruling them out cost, and the raw CSV for a measurement that went wrong. Three-run medians once manufactured a 44.9% regression that ten runs resolved to a 20.2% *improvement*, because the distribution was bimodal and three samples can land entirely in the wrong mode. That CSV is committed. It is more useful than the conclusion it failed to support.

**Issues get answered.** Not always quickly, and not always with a fix, but a bug report will not sit unacknowledged.

## Free and Open Source Promise

As part of the effort that I have put into this project I created the CS2OpenDev organization on GitHub which is the home for CS2DemoKit and its sibling projects that make it possible. When picking a license for these projects I wanted to select something that is permissive for all types of downstream usage, including commercial use. The reason I selected the MIT license was mainly from a hope that it would encourage those that have financial ambitions to leverage this project instead of simply creating another. Ideally this would mean more usage and resources from the community would be channeled to this project making adding new features, finding and fixing bugs, and other maintenance tasks easier.

For those unfamiliar with the MIT license this is a brief summary, please review the full license if you have questions

|      Can       |       Cannot        |        Must       |
|----------------|---------------------|-------------------|
| Commercial Use | Hold Project Liable | Include Copyright |
| Modify         |                     | Include License   |
| Distribute     |                     |                   |
| Sublicense     |                     |                   |
| Private Use    |                     |                   |

I am committed to keeping all CS2OpenDev projects free and open source forever. I have no desire for personal financial gain when it comes to these and future tools that are broadly useful to the community at large. I would love for the community to get behind a set of open tools and help build awesome new projects that are also free and open source, but I want to leave the door open for downstream users to make awesome things regardless.

That said members of this organization, contributors to any of its projects, and anyone else involved is free to use these tools downstream in compliance with the license in the same way as anyone else.

## LLM/AI Tooling Usage and Position

I use AI tooling on these projects, and I would rather say that plainly than have you work it out from the commit history.

My position is that it changes *how* the work gets done and not *what the work has to prove*. The standard has not moved. Everything that can be generated is generated from upstream artifacts and gated by a test. Every performance claim is measured on a named machine against a named corpus with the raw rows committed beside it. Every shipped ruleset has a pinned golden fixture, so a change that moves a number has to move a reviewed file too. Determinism is tested rather than assumed. None of that is AI-specific — it is ordinary engineering discipline — but it is the discipline that makes the question of who typed a line less interesting than whether the line is right.

Where I have found it genuinely useful is the adversarial direction: asking for the case that a change is wrong, then going and measuring. That is how the "figures that do not reproduce" section came to exist. A published build-speedup number turned out to be the core count of the machine it was run on rather than the improvement it was attributed to, and the honest version is smaller and better documented than the flattering one was.

The same instinct produced a full-repo review that came back with a ranked punch list — including a high-severity gap in our own input hardening, sitting directly underneath a README sentence claiming the opposite. A review that returns nothing is not a review that found nothing. It is a review that was not looking.

Where I do not let it near anything: claims about what the game does. If the documentation says a field means something, that is because it was observed in data, usually across a lot of frames, and the observation is written down. Plausible-sounding explanations of engine behaviour are exactly the failure mode to guard against, and it is a failure mode humans have too.

There is a second angle worth mentioning, which is that these projects are also *consumed* by AI tooling. `AGENTS.md` in the docs repository exists specifically as a context file for someone else's AI assistant to load, and the reference data is published as raw Markdown and flat JSON partly because that is what tools fetch. Accurate, machine-readable, provenance-tracked CS2 reference data is useful to a person with an editor and it is useful to a person with an assistant, and I would rather the community's shared answer to "where does `m_iHealth` live" be a generated artifact with a build id on it than a forum post from 2023.

If you disagree with any of this, the projects are MIT and every artifact is reproducible from the upstream binaries. You are not required to take my word for anything.

## How You Can Help

**Use it and file issues.** This is genuinely the most valuable thing. Every project here has been developed against a limited set of demos, maps and game builds. The failure modes we have not seen are the ones in your files.

**Send demos, or tell us what is in yours.** CS2DemoKit's test suite runs in CI against a committed four-round sample, which is the single largest gap in its coverage. Full-match demos across different maps and different game builds are what exercise the decode paths that matter. If you have unusual recordings — POV demos, FACEIT or ESEA files, demos from older builds, anything that breaks — those are worth more than working ones.

**Annotate the reference data.** The generated pages carry only what is in the binaries. Community annotations — what a field actually means, what a ConVar actually does, which values are safe — live in hand-edited overlay files and get merged into the generated output. The [overlays README](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/docs/overlays/README.md) explains the format, and a one-line description of one confusing field is a completely legitimate contribution.

**Write rules and share them.** CS2DemoKit's rules language exists so that "here is how I measure entry-fragging" can be a file someone hands you rather than a paragraph you have to reimplement. A ruleset is a text file with no dependencies.

**Build something and tell us it was awkward.** The most useful bug reports we have had are not crashes. They are "I expected this to be here and it wasn't", and "I could not tell whether zero meant zero or meant it didn't run". Ergonomic complaints about a library are real bugs.

**Contribute code.** Pull requests are welcome on all four repositories. Fair warning that the standards described above apply — a performance claim wants a measurement, a behaviour change wants a test, and a documentation claim about engine behaviour wants an observation behind it.

## Legal Disclaimer, Trademark and Copyright Acknowledgement

Counter-Strike, Counter-Strike 2, Source, Source 2, Steam and Valve are trademarks and/or registered trademarks of Valve Corporation. **CS2OpenDev is not affiliated with, endorsed by, sponsored by, or in any way officially connected to Valve Corporation.** No claim of ownership is made over any Valve intellectual property, and no Valve trademark is used here except descriptively, to identify the game these tools work with.

All original code in CS2OpenDev repositories is licensed under the MIT license, and each repository carries its own `LICENSE` file and, where applicable, a `THIRD-PARTY-NOTICES.md` documenting adapted third-party code and its license terms. CS2DemoKit, for example, adapts portions of its bit-level decoder from [demofile-net](https://github.com/saul/demofile-net), also MIT licensed, and says so with the upstream license text reproduced in full.

Data derived from Valve's shipped game files — entity schemas, protobuf definitions, console variable tables, and baked map collision geometry — remains Valve's. The tooling that extracts, transforms and presents it is ours and is MIT licensed; the underlying game data is not ours to relicense and we do not attempt to. This is also why map collision bakes are distributed separately from the NuGet packages rather than inside them.

These projects are provided "as is", without warranty of any kind, as the MIT license states at somewhat greater length. Nothing here is a substitute for reading the license.

If you are at Valve and something here is a problem, please [open an issue](https://github.com/CS2OpenDev/CS2OpenDev-Docs/issues) and we will address it.
