# Diagram references — for the research-agenda figure and the vista figures

Collected August 2026. Working material for tasks #21 (agenda diagram) and #26 (vista diagrams). Not published to the site.

## Exemplars worth imitating

| # | What it is | Source | Link |
| - | ---------- | ------ | ---- |
| 1 | NSF ERC **three-plane strategic chart** — how to build one, plus the canonical chart | ERC Association / NSF | https://erc-assoc.org/content/three-plane-diagram |
| 2 | A filled-in three-plane chart for an operating center (thrusts × testbeds) | NSF ERC CMaT, Georgia Tech | https://cellmanufacturingusa.org/cmat-3-plane-chart |
| 3 | CBMM Center Project Figure 1 — four interacting modules | MIT Center for Brains, Minds & Machines | https://cbmm.mit.edu/research/modules |
| 4 | Annotated real research statement, Fig 1 "common system components" / Fig 2 "common system architecture" | Elena Glassman, via MIT EECS Comm Lab | https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2021/09/Elena-Glassman-research-statement-annotated.pdf |
| 5 | The research-statement genre: hourglass structure, two annotated real statements | MIT EECS Communication Lab | https://mitcommlab.mit.edu/eecs/commkit/faculty-application-research-statement/ |
| 6 | AI alignment landscape — whole-field decomposition tree with own work highlighted | Paul Christiano | https://ai-alignment.com/ai-alignment-landscape-d3773c37ae38 |
| 7 | Thread: Circuits — a research program published as claims plus an accumulating artifact list | Olah, Cammarata et al., Distill | https://distill.pub/2020/circuits |

## Guidance and notation

| # | What it is | Source | Link |
| - | ---------- | ------ | ---- |
| 8 | Roadmapping for strategy and innovation — four real roadmaps (Motorola, generic multi-layer, EU Graphene Flagship, T-Plan grids) | Robert Phaal, IfM Cambridge | https://www.ifm.eng.cam.ac.uk/uploads/Research/CTM/Roadmapping/roadmapping_overview.pdf |
| 9 | Technology roadmapping — a planning framework for evolution and revolution | Phaal, Farrukh, Probert, *TFSC* 2004 | https://www.sciencedirect.com/science/article/abs/pii/S0040162503000726 |
| 10 | Free roadmap templates and toolkits (layers, sub-layers, linking grids) | IfM Engage, Cambridge | https://engage.ifm.eng.cam.ac.uk/roadmapping-templates/ |
| 11 | Visualizing Thought — correspondence and use; what dots, lines, arrows, boxes actually assert | Barbara Tversky, *Topics in Cognitive Science* 2011 | https://hci.ucsd.edu/220/TverskyCogtiveDesign.pdf |
| 12 | *Envisioning Information* — escaping flatland, layering and separation, small multiples, 1+1=3 | Edward Tufte | https://www.edwardtufte.com/book/envisioning-information/ |
| 13 | Design for an Audience — ~40 before/after redesigns of scientific figures, full transcript | Jonathan Corum, NYT | https://style.org/ku/ |
| 14 | Ten Simple Rules for Better Figures | Rougier et al., *PLOS Comp Biol* 2014 | https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1003833 |
| 15 | Points of View: Salience, Layout, Gestalt | Bang Wong, *Nature Methods* | https://www.nature.com/articles/nmeth.1711 |
| 16 | Strategy map — one page, four causal layers, bottom feeds top | Kaplan & Norton, *HBR* 2000 | https://hbr.org/2000/09/having-trouble-with-your-strategy-then-map-it |
| 17 | Theory of change (backwards mapping) / logic model / concept map cross-links | Center for Theory of Change; Kellogg Fdn; Novak & Cañas | https://www.theoryofchange.org/what-is-theory-of-change/how-does-theory-of-change-work/example/backwards-mapping/ |

Also noted: Wardley maps (value chain × maturity — positions work on a novelty axis, does not show causality) https://blog.gardeviance.org/2015/02/an-introduction-to-wardley-value-chain.html ; NASA Technology Area Breakdown Structure (strict three-level hierarchy — good for completeness, poor for coherence); visual-abstract primer https://static1.squarespace.com/static/5854aaa044024321a353bb0d/t/5a527aa89140b76bbfb2028a/1515354827682/VisualAbstract_Primer_v4_1.pdf

## The three structural ideas

**Three-plane chart (#1, #2).** A vertical stack of levels of abstraction — fundamental knowledge, enabling technology, systems and testbeds. Requirements flow down, results flow up. A named **barrier** is pinned at each level. The depth is in the barriers: the chart states what is currently impossible, so it can be wrong. Its own stated success test: a stranger who has read the vision statement should be able to paraphrase the research efforts, the obstacles, and the demonstrations from the figure alone.

**Architecture-as-claim (#3).** The program is drawn as the hypothesized architecture of the object being studied. Each thread is a component of the conjectured system; each collaboration is an interface. The diagram doubles as a falsifiable scientific claim, which is why it cannot read as decoration.

**Decomposition with negative space (#6).** Decompose the whole field top-down into a tree of subproblems, then highlight only the small subtree occupied. The threads get their meaning from the adjacent work not being done.

## Why the rejected version failed

Recorded so the next attempt does not repeat it. The rejected figure was parallel horizontal trajectory lanes, one per thread, filled dots for finished work and hollow rings for open questions.

1. **The geometry made no claim.** Four parallel lanes assert only "there are four of these." No ordering, no dependency, no level, no containment. Tversky's correspondence principle is the diagnosis: if position on the page does not map to something conceptual, the reader is decoding decoration.
2. **Status encoding substituted for intellectual structure.** Filled = done, hollow = open is a project-management fact. It answers "what is finished?" when the reader is asking "why does this cohere?" The ERC chart never encodes completion status — it encodes barriers.
3. **No named obstacle, so nothing could be wrong.** Every strong figure in the sample names what is currently impossible. Figures that name only topics are unfalsifiable and weightless. This is the largest separator between deep and shallow across the sample.
4. **Framework outweighed content.** Corum's repeated finding: keys, legends, and colour codes with nearly as many entries as data points. Anything the reader must hold in working memory and apply back to the figure is a failure. Label in place.
5. **A time axis with no time claim.** Roadmapping earns a horizontal axis only when items are dated *and* dependent. Spreading finished work left and future work right is a CV wearing a timeline costume — which is what the lanes were.
6. **Arrows with undefined semantics.** An arrow asserts an asymmetric relation. If some mean "causes," some "then," and some "is related to," the figure is unparseable. One meaning per line style, stated.
