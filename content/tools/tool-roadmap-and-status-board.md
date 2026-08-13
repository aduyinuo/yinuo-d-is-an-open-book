# Tool Roadmap and Status Board

## Status lanes
- **Done**: shipped baseline capability
- **WIP**: active implementation
- **WaitList**: queued behind explicit dependencies
- **Flagship Next**: high-priority research-tool candidate

## Current board

| Tool | Lane | Program role | Next milestone |
|---|---|---|---|
| Astrolabe | Done | research artifact + practical analyzer | publish demo workflow and usage rubric |
| Gavel | Done | prior completed tool line | add short retrospective and transfer notes |
| Nanny | WIP | assistive care and reminder system | finalize plugin schema + first adaptive policy bundle |
| Logographer | WaitList (urgent) | writing mediation and personalization | ship preference profile + rewrite pipeline MVP |
| Opportunity Scout Suite | WaitList | opportunity intelligence pipeline | lock shared entity schema + ingest adapters |
| LinkedIn Notes Processor | WaitList | low-friction signal capture and routing | ship capture, classification, and handoff flow |
| Omni Message Hub | WaitList | unified communication and relationship maintenance | design identity/thread model + core channel adapters |
| Agentic Laboratory Collector | WaitList | consented researcher-agent interaction analysis | define event ontology + graph storage baseline |
| MDP Generator (tentative) | Flagship Next | research-to-tool bridge from LucidWorld | finalize control parameters and evaluation harness |

## Dependency map

| Tool | Hard dependencies | Notes |
|---|---|---|
| Logographer | none (foundational) | can start immediately; outputs feed communication tools |
| Opportunity Scout Suite | shared entity schema, scheduling primitives | upstream dependency for ranking + routing features |
| LinkedIn Notes Processor | routing taxonomy, opportunity schema | relies on shared tags/entities from scout suite |
| Omni Message Hub | identity resolution model, channel adapters | depends on schemas stabilized by Logographer + Scout |
| Nanny | plugin schema, reminder policy engine | can run in parallel with Omni once identity model is stable |
| Agentic Laboratory Collector | consent protocol, event ontology, graph store | must precede large-scale connector expansion |
| MDP Generator | Learn Structure generator controls, metric definitions | blocked on LucidWorld generator specification closure |

## Phased milestones

### Phase 1 — Foundation (Weeks 1–3)
- Logographer MVP (preference model + rewrite pass)
- Shared entity/routing schemas (for Opportunity + LinkedIn tools)
- Milestone gate: schema validation on at least two real workflow traces

### Phase 2 — Workflow Acceleration (Weeks 4–6)
- Opportunity ingestion + ranking baseline
- LinkedIn Notes Processor MVP
- Topic-to-calendar linkage prototype
- Milestone gate: end-to-end triage from captured signal to ranked action

### Phase 3 — Communication and Care (Weeks 7–9)
- Omni Message Hub MVP (identity/thread baseline + adapters)
- Nanny adaptive reminders MVP
- Milestone gate: unified thread view with one-click task routing + reminder loop

### Phase 4 — Research Meta-Layer (Weeks 10–12)
- Agentic Laboratory Collector ontology + storage baseline
- MDP Generator prototype aligned with LucidWorld Learn Structure controls
- Milestone gate: first closed-loop demonstration from collected interaction traces to generator-backed experiment setup

## Sequencing rule
Prioritize tools that unlock shared schemas first, then communication integration, then research meta-layer expansion.
