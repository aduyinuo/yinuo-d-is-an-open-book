---
icon: diaspora
---

# CHART

Most teams describe how they work together and then hope. CHART writes it down as a graph and makes the software enforce it.

<figure><img src="../../.gitbook/assets/chart-interaction.gif" alt="A CHART session: the dependency graph, an approval routed along the control edge, an agent-generated explanation, and a routed chat message"><figcaption><p>One session. The structure is not a description — it decides what can happen.</p></figcaption></figure>

## The graph

Teammates are nodes; the edges between them are typed dependencies. Control, pool, temporal, informational — and, in the full scheme, synchrony. A directed acyclic graph, so the structure can be walked and queried rather than only read.

## Approval

The agent proposes to isolate a host. The proposal doesn't execute — it travels along the **control** edge to the teammate who holds it, and waits there.

The constraint that makes this real: only the teammate on the other end of that control connection can approve. The analyst, who has an informational edge to the agent but not a control one, cannot sign off no matter how sensible the action looks. Authority is a property of the graph, not of the interface.

## Explanation

Once an action is on the table, the agent generates an explanation and passes it to the panel — why this host, what it costs, what it protects. Which explanation modality is available depends on what kind of agent it is, so the panel is not one fixed format.

## Chat

Messages are routed, not broadcast. A mention sends a message to a specific teammate along the structure that already exists, so who heard what is recorded rather than assumed.

## Afterwards

Because every one of those moves is an edge traversal, the session leaves a graph rather than a log. You can ask it who approved what, how long each approval sat waiting, and which dependencies were exercised versus which merely existed on paper.

_Last updated: 2026-08_
