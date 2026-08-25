---
icon: diaspora
---

# CHART

A configurable testbed where the structure of a human–AI team is the thing you manipulate — written down as a graph and enforced by the software.

<figure><img src="../../.gitbook/assets/chart-interaction.gif" alt="A CHART session: the dependency graph, an approval routed along a control edge, an agent-generated explanation, and a routed chat message"><figcaption><p>One session. The structure is not a description — it decides what can happen.</p></figcaption></figure>

CHART is the **Configurable Human-AI Research Testbed**. Existing platforms fix the team; CHART makes the team the independent variable. Teammates are nodes, dependencies are typed edges, and the interaction interfaces — approvals, explanations, chat — are configurable modalities layered on top. Every step is instrumented, so a session leaves a linked trace rather than a flat log.

The research write-up, with the five dependency types and the four modalities in full, lives on the research page: [**Human-AI Complementarity → CHART**](../../overview/3-year-agenda/human-ai-complementarity/chart.md). These pages cover it as a piece of software.

## What the next version has to answer

CHART so far captures the syntax of human-agent teamwork, and whether that syntax is complete or succinct has not been tested.

* Can it express how a security operations centre or an incident-response team actually works?
* Can teamwork written in CHART be prescribed and enforced as well as recorded?
* Can it be monitored during a session and diagnosed afterwards, so a structural fault surfaces while it is still correctable?

## More

* [Design](design.md) — the DAG, the modalities, and the trace
* [Use](use.md) — configuring a study and reading the results

_Last updated: 2026-08_
