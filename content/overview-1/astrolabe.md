# Astrolabe

A local research app for turning recorded work sessions into coded, comparable data.

Built for the problem-solving studies: get a transcript in, let several people annotate it against a shared scheme, and find out whether they actually agree.

## What it does

**Intake.** Typed text, uploaded transcripts as plain text or JSON, or audio recorded straight from the browser and transcribed with Whisper.

**Annotation.** Multiple coders label the same session against a shared scheme, with optional item identifiers so segments line up.

**Agreement.** Stage-level percent agreement and Cohen's kappa between annotators, exportable as CSV. Where coders diverge is treated as a result, not a defect.

**Structure.** The research question-cards the project is organised around, with persistent hypergraph overlays for grouping operations at more than one scale.

**Assistance.** Reusable prompt scaffolds and templates for candidate actions, operations, concepts and questions, wired to configurable model providers — or to a mock provider when you want the pipeline without the calls.

**Export.** Six formats: SQLite, JSON, and CSV for graph, scores, timeline, and agreement.

## Two commitments

It runs entirely on your own machine. Nothing is hosted.

It never writes to your source material. On first load it takes one snapshot and works from that, keeps all its own state in a separate database, and hands changes back as text you paste yourself. You can keep editing the original while the app is running.

_Last updated: 2026-08_
