---
description: Project blurbs and ads for research assistants
icon: creative-commons-remix
---

# Work With Me

I take on research assistants and engineering assistants at UTEP. Research assistants own a question and are expected to carry it to a paper. Engineering assistants own an artifact, such as an environment, a testbed, or an instrumentation layer, that several projects depend on. Both roles appear on papers when the contribution warrants it.

Each opening below names the thread it belongs to, the question it works on, what you would do, and what you need to be able to do. Read the linked thread page first, then write to me with which opening you are interested in and why.

## Open projects

<table><thead><tr><th width="230">Project</th><th width="130">Role</th><th>Question it works on</th></tr></thead><tbody><tr><td><a href="#a-defender-that-knows-when-its-model-is-wrong">A defender that knows when its model is wrong</a><br><em><a href="../overview/3-year-agenda/cyber-world-modeling/">Cyber World Modeling</a></em></td><td>Research</td><td>How should a defender act when its learned model is most likely to be wrong exactly where the adversary is operating?</td></tr><tr><td><a href="#using-an-inaccurate-world-model-to-cut-the-cost-of-strategic-search">Using an inaccurate world model to cut the cost of strategic search</a><br><em><a href="../overview/3-year-agenda/cyber-world-modeling/">Cyber World Modeling</a></em></td><td>Research</td><td>Do simulated rollouts from an imperfect model reduce the cost of computing strategic responses, or bias the empirical game?</td></tr><tr><td><a href="#learning-the-operations-instead-of-naming-them">Learning the operations instead of naming them</a><br><em><a href="../overview/3-year-agenda/mental-world-modeling/">Mental World Modeling</a></em></td><td>Research</td><td>Can an agent learn its own vocabulary of problem-solving operations rather than being given one?</td></tr><tr><td><a href="#eliciting-reasoning-from-people-under-time-pressure">Eliciting reasoning from people under time pressure</a><br><em><a href="../overview/3-year-agenda/mental-world-modeling/">Mental World Modeling</a></em></td><td>Research</td><td>How do you recover how someone solved a problem when you cannot ask them to think aloud while they work?</td></tr><tr><td><a href="#measuring-whether-a-human-ai-team-is-actually-complementary">Measuring whether a human-AI team is actually complementary</a><br><em><a href="../overview/3-year-agenda/human-ai-complementarity/">Human-AI Complementarity</a></em></td><td>Research</td><td>Did the pair reach a decision neither would have reached alone, or did one party carry the other?</td></tr><tr><td><a href="#the-chart-testbed">The CHART testbed</a><br><em><a href="../overview/3-year-agenda/human-ai-complementarity/">Human-AI Complementarity</a></em></td><td>Engineering</td><td>Making team structure a directed graph the software enforces, so it can be varied as a controlled manipulation.</td></tr><tr><td><a href="#instrumenting-agent-workflows">Instrumenting agent workflows</a><br><em><a href="../overview/3-year-agenda/human-ai-complementarity/">Human-AI Complementarity</a></em></td><td>Engineering</td><td>Recording what an agent did in enough detail to locate where a team failed.</td></tr><tr><td><a href="#testing-whether-a-transferred-policy-wins-for-the-right-reasons">Testing whether a transferred policy wins for the right reasons</a><br><em><a href="../overview/3-year-agenda/toward-deployment/">Toward Deployment</a></em></td><td>Research</td><td>Can a policy that scores well in a new environment be shown to have learned the task rather than the benchmark?</td></tr><tr><td><a href="#moving-agents-between-cyber-environments">Moving agents between cyber environments</a><br><em><a href="../overview/3-year-agenda/toward-deployment/">Toward Deployment</a></em></td><td>Engineering</td><td>Running the same agent across simulators, emulators, and ranges so results can be compared at all.</td></tr></tbody></table>

## Cyber World Modeling

### A defender that knows when its model is wrong

**Role:** research assistant · **Thread:** [Cyber World Modeling](../overview/3-year-agenda/cyber-world-modeling/) → [Next](../overview/3-year-agenda/cyber-world-modeling/next.md)

A model learned from data is wrong somewhere. Against an adversary that error is not random, because the adversary has an incentive to find the regions where the defender's model is wrong and to operate there. This project asks how a defender should behave under that condition: how to detect that the model of the adversary has become unreliable, how to bound the cost of acting on a model that is wrong, and whether a model that represents its own uncertainty is safer to act on than one that is confident and wrong.

You would work on top of [FOE-Dreamer](../overview/3-year-agenda/cyber-world-modeling/environment.md), where the adversary is held in a separate latent variable, which is what makes it possible to ask whether the error is localized rather than spread across the whole representation.

**What you need:** reinforcement learning at the level of implementing and modifying an existing agent; PyTorch; comfort reading model-based RL papers, since you will be working from Dreamer-style architectures rather than a clean textbook setting. Prior exposure to POMDPs helps.

### Using an inaccurate world model to cut the cost of strategic search

**Role:** research assistant · **Thread:** [Cyber World Modeling](../overview/3-year-agenda/cyber-world-modeling/) → [Next](../overview/3-year-agenda/cyber-world-modeling/next.md)

In PSRO each new best response is learned through repeated interaction with the environment, which is the expensive part. A world model can supply some of those interactions as simulated rollouts. Co-learning a world model with the empirical game already exists, in Dyna-PSRO. The open part is what happens when the model is inaccurate: whether imagined rollouts still reduce the total cost of reaching a strategically robust policy, or whether the model's errors propagate into the empirical game and the responses computed from it. The project is to find the conditions under which the model helps and the conditions under which slower interaction with the real environment is better.

**What you need:** game theory through normal-form solution concepts and best response; enough familiarity with empirical game-theoretic analysis to read the PSRO literature; Python and reinforcement learning implementation. Being willing to run and account for a lot of compute matters here, because the claim is fundamentally about cost.

## Mental World Modeling

### Learning the operations instead of naming them

**Role:** research assistant · **Thread:** [Mental World Modeling](../overview/3-year-agenda/mental-world-modeling/) → [Next](../overview/3-year-agenda/mental-world-modeling/next.md)

Every account of problem-solving in this thread so far takes its operations as given: they are named in advance and then located in the data. Research on mental operations has never settled on a single agreed set, and the right level of detail depends on the scale of analysis. This project asks whether an agent can instead learn its own operations as reusable sub-behaviors, in the way hierarchical reinforcement learning learns options or program-synthesis systems build and reuse a library of procedures, so that the grain is determined by what proves useful. A second part concerns the control of the operations rather than the operations themselves: choosing which to apply, noticing that an approach is failing, and deciding when to stop.

**What you need:** reinforcement learning, ideally including hierarchical RL or options; Python; interest in cognitive science, since the target is a description of human problem-solving and not only an agent that performs well.

### Eliciting reasoning from people under time pressure

**Role:** research assistant · **Thread:** [Mental World Modeling](../overview/3-year-agenda/mental-world-modeling/) → [Problem-Solving](../overview/3-year-agenda/mental-world-modeling/problem-solving/)

Thinking aloud while working is the most reliable way to recover how someone solved a problem, and it is unusable in a timed competition or an operational setting. The approach here is to replay people their own session afterward as a retrieval cue, anchored to submission logs so that the recall has timestamps to attach to. The work is running these sessions with capture-the-flag competitors, building a coding scheme coarse enough that independent observers agree on it, and establishing that agreement quantitatively.

**What you need:** willingness to run studies with human participants and to work within IRB requirements; qualitative coding and inter-rater reliability, or willingness to learn them properly; enough security background to follow what a competitor is doing during a challenge.

## Human-AI Complementarity

### Measuring whether a human-AI team is actually complementary

**Role:** research assistant · **Thread:** [Human-AI Complementarity](../overview/3-year-agenda/human-ai-complementarity/) → [Next](../overview/3-year-agenda/human-ai-complementarity/next.md)

A team can succeed because it combined what the person and the agent each contributed, or because one capable party compensated for the other. Overall success does not separate these. This project builds a measure that does, which requires estimating what each party would have done alone and comparing that with what the pair did. The experiments run in [CHART](../overview/3-year-agenda/human-ai-complementarity/chart.md) and the [Team Defense Game](../overview/3-year-agenda/human-ai-complementarity/team-defense-game.md), where the team's structure is set explicitly and can be varied.

**What you need:** experimental design and statistics beyond a first course, since the measure is the contribution; experience running human-participant studies; Python for analysis. Familiarity with counterfactual or causal estimation is an advantage.

### The CHART testbed

**Role:** engineering assistant · **Thread:** [Human-AI Complementarity](../overview/3-year-agenda/human-ai-complementarity/) → [CHART](../overview/3-year-agenda/human-ai-complementarity/chart.md)

CHART represents a human-AI team's structure as a directed graph that the software enforces: approvals travel along control edges, explanations reach the parties entitled to them, messages route by mention. Because the structure is enforced rather than described, changing the graph is a controlled manipulation rather than an instruction to participants. The work is extending the platform to support new team configurations, agent behaviors, and interaction modalities, and keeping it stable enough to run studies on.

**What you need:** solid software engineering in Python, including a web stack and real-time messaging; the ability to design an interface that a study participant can use without training; version control and testing habits that hold up when other people's experiments depend on your code.

### Instrumenting agent workflows

**Role:** engineering assistant · **Thread:** [Human-AI Complementarity](../overview/3-year-agenda/human-ai-complementarity/) → [CyberAgentFlow](../overview/3-year-agenda/human-ai-complementarity/cyberagenttrace.md)

When a human-AI team performs poorly, the failure has to be attributable: an approval that routed incorrectly, an explanation that never arrived, a decision that was wrong on its merits. That requires recording what agents actually did rather than inferring it afterward. This project builds the tracing layer for agent workflows in penetration-testing and defense sessions, including the representation of events and their dependencies.

**What you need:** Python; experience with logging, tracing, or observability; some exposure to LLM agent frameworks; enough security knowledge to know which events in a session are worth recording.

## Toward Deployment

### Testing whether a transferred policy wins for the right reasons

**Role:** research assistant · **Thread:** [Toward Deployment](../overview/3-year-agenda/toward-deployment/) → [Next](../overview/3-year-agenda/toward-deployment/next.md)

A policy moved to a new environment and scoring well has either learned the task or learned features specific to the benchmark, and the score does not distinguish them. This project builds tests that do: perturbing the parts of an environment a competent policy should depend on and a benchmark-specific one should not, evaluating on forms of realism the policy never trained against, and constructing cases designed to fail a policy that has memorized surface structure.

**What you need:** reinforcement learning and evaluation methodology; Python; the disposition to design experiments intended to break a result rather than confirm it, which is the actual skill this project requires.

### Moving agents between cyber environments

**Role:** engineering assistant · **Thread:** [Toward Deployment](../overview/3-year-agenda/toward-deployment/) → [Cyber Environments & Benchmarks](../overview/3-year-agenda/toward-deployment/cyber-environments-and-benchmarks/)

Claims about transfer are only meaningful if the same agent can actually be run across a simulator, an emulator, and a range, and if what differs between them is documented. This project maintains that path: interfaces to environments such as CybORG, Cyber Wheel, and CyberVAN, the harness that runs agents across them, and the record of what each environment represents and omits.

**What you need:** Python and comfort in Linux, networking, and containers; patience with other people's research code, since much of the work is making existing environments run and keeping them running; clear documentation habits.

## Applying

Write to me with the opening you are interested in, what you have done that is relevant, and what you want to get out of it. If you are a UTEP student, say what year you are in and how many hours a week you can commit. Undergraduates are welcome to apply for the engineering roles and for [Eliciting reasoning from people under time pressure](#eliciting-reasoning-from-people-under-time-pressure).

Funded positions, when available, are listed on [Opportunities](../overview-4/). Current and past students are on [Mentor](../mentor/).

_Last updated: 2026-08_
