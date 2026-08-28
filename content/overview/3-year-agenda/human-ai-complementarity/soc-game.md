---
description: Whether the graph can hold a real centre, and the three places I expect it to fail.
icon: headset
---

# SOC Game

Not a fifth platform. The test that decides whether the fourth one is a formalism or a description.

## The question, asked twice already

I have put this question to myself twice, once on the [cluster overview](./) and once on the [CHART](../../../artifacts/chart/) software page, in almost the same words both times. Can CHART express the teamwork in a SOC center or an incident response team? Can we prescribe, monitor, and diagnose human-agent teamwork represented with CHART?

The direction of the work runs both ways: encoding real team structures to find what the graph cannot say, and extending the platform so that the structures it can express actually run.

The honest statement of it today is that the graph has been shown to run and has not been shown to hold anything real. The five dependency types were each drawn from a coordination pattern in security operations, so the graph is expected to fit. That expectation is exactly why the test has to be run against a centre nobody designed the types from.

## What the test is

Take a real shift's coordination pattern and try to write it as nodes and typed edges. Every part that needs a footnote in prose instead of an edge is a finding, and the count of those footnotes is the result. The dependent variable is the notation, not the team.

Two ways a notation can fail, and the repairs differ. **Incomplete**, when a real arrangement has no expression in it, is repaired by a new construct. **Not succinct**, when the arrangement has an expression but only as a large and unreadable one, is repaired by an abbreviation over constructs that already exist, and adding a construct for it makes the notation worse. Keeping the two apart is what stops the test from ending in a request for a sixth dependency type.

## The centre's own vocabulary

A **security operations centre** is the standing team that monitors an organization's systems for security events, decides which of them matter, and drives the response, staffed in shifts and running continuously. An **incident response team** assembles around a confirmed incident and dissolves when it closes. My own sentence asks about both in one breath, which hides that they are two different tests. A response team is one commander with temporary authority over specialists, and CHART writes it in one line. A centre is standing tiered authority over a queue that never empties, staffed by people who change every eight hours. The graph is very likely to pass the first test and fail the second, and the failure is the result worth having.

**Tier.** The centre's division of its own labour by decision authority: the first tier triages against written procedure, the second investigates what the first sends up and may take containment actions the first may not, the third hunts for what no detector raised. Tiers are defined by which actions a person may take without asking, which is a graph property rather than a personnel one. This is the most direct fit between the centre and the notation, since tiering is a chain of control edges and the escalation chain and the risk-tier gating are already configurable inputs on the control type. If the SOC Game finds nothing else, it should confirm this.

**Escalation.** Handing an alert upward because it exceeds the authority or the scope of the person holding it. Distinct from the escalation chain in CHART, which is the configured route the handing-up follows. The chain is the notation; escalation is the act, and it carries something the chain does not, which is the judgement that this one is above me, made by the person least equipped to make it. Ask what happens if nobody escalates. In a centre the alert closes as a false positive and nothing marks the error. Under a control edge the action simply does not fire. One of the two failures is silent, and the graph has no place to put the silent one.

**Playbook.** The written procedure for a class of alert, saying what to check in what order and what to do with each outcome. Longer than a temporal dependency: it is the ordering plus the branch conditions plus what counts as enough checking, and only the first of the three has an edge type. Try to write a playbook as edges and the steps go in while the conditions under which a step is skipped do not. This is where I expect the succinctness failure rather than the completeness one.

**Alert fatigue.** The degradation in judgement that follows from a volume of alerts beyond what the team can process, showing up as unexamined queues, delayed investigation, and missed detections rather than as visible error. Practitioner surveys put a median team near a thousand alerts a day, and a substantial share are never looked at by anyone. Workload as my own studies measure it is asked of a participant after a session with a questionnaire. Fatigue in a centre is a property of a queue over months, and no session-length instrument reaches it. It is the reason human-AI teaming is proposed for centres at all, and the outcome variable a SOC Game would most want and least be able to produce.

**Shift handover.** The transfer of an open picture between two sets of people at a shift boundary: what is running, what was decided, what was deliberately left. A CHART graph is a structure over teammates present in one session. A handover changes who the teammates are without ending the work, and the graph has no construct for the same role held by a different person an hour later. This is the first place I expect the encoding to fail outright, and the most interesting failure, because a construct for it would be a construct for continuity of authority across a change of personnel, which is a general teaming problem and not a cyber one.

## Three things the graph does not yet say

_**Queue depth.**_ The number of alerts standing unjudged at a moment, and the rate at which the number is changing. The trace records what the team did. Queue depth is a fact about what the team did not reach, and it cannot be recovered from a record of actions taken. Adding it is not a change to the dependency graph. It is a change to what a session contains: a stream of work arriving faster than it can be cleared, which none of my four studies has.

_**Authority that shifts.**_ Reassignment of who may act without asking, during the task, triggered by the state of the task. My own [Next](next.md) page already names this as the third open question of the cluster, on general grounds. The centre is where it stops being a refinement and becomes the ordinary case. Ask whether the same action needs approval at hour one and at hour three. In a centre under a live incident it does not.

_**Tacit knowledge between two people.**_ What an experienced analyst knows about their own network that is not in any playbook and is transferred, when it is transferred at all, by sitting next to somebody. The cluster's first challenge is that complementarity depends on knowledge neither side can fully state. A centre is the setting where that claim has actually been studied, by interview and by embedded fieldwork, and it is the reason those field studies are on my reading table rather than my platform papers.

## Prescribe, monitor, diagnose

Three things a written structure would have to support beyond being written. A recorded structure tells you what the team was configured to do. A **prescribed** one refuses what falls outside it, a **monitored** one says while the shift is running that the team has drifted out of it, and a **diagnosed** one says afterwards which edge was the fault. Ask when the fault becomes visible. Afterwards is diagnosis. During, in time to change something, is monitoring, and only the second is any use to the people on shift. Monitoring is the one nothing in the platform currently does, because everything in it is built to be read after the session.

There is a design problem inside the third. A monitor that watches the graph during a mission is an authority in the session, and nothing in the architecture says who it reports to.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/hac_soc_game.pdf)

_Last updated: 2026-08_
