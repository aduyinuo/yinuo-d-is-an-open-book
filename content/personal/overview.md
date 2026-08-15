# What is she reading?

A working bundle, assembled August 2026. Every entry below was checked against arXiv, Crossref, OpenAlex, or the publisher record before it was listed here.

Two layers run through each section:

**Insight** — position papers, critiques, and SoKs. Short, argumentative, written to change what the field does. These carry sentences worth borrowing.

**Foundation** — the machinery an insight paper assumes. Longer, slower, and the reason an argument built on it holds up under a question.

Papers only. No books.

Links go to a free full text wherever one exists, and to the DOI otherwise. Everything with an arXiv link, plus both CyLab papers, is downloaded to `internal/reading/pdfs/` in the site repo.

***

## The two CyLab papers

### [Creating a Scientific Foundation for Cyber Autonomy](https://kilthub.cmu.edu/articles/report/Creating_a_Scientific_Foundation_for_Cyber_Autonomy/31769038)

Bauer, Brumley, Calandrino, Christin, Fanti, Gligor, Parno, Patel, Sekar, Sherry — CyLab, v1.0.0, March 2026. 22 pages.

Self-described as manifesto-style, with "more questions than answers." The argument: AI-driven offense keeps improving while systems grow, so defense that runs on human timescales becomes inadequate, and the field's siloed structure is the obstacle to fixing it. It calls for end-to-end designs of both autonomous defense *and* red-team systems, frameworks spanning operators, AI vendors, security vendors, and platform providers, and empirical study of how attack and defense systems interact in realistic environments. Four thrusts: algorithmic foundations; data-plane and control-plane systems support (emulation systems, training datasets, sandboxing and verification, scalable telemetry); human-AI collaboration; and a **Cyber Autonomy Arena** — a neutral leaderboard evaluating end-to-end attack systems against defense systems on realistic networked systems, modeled on ImageNet, SPEC, and TPC. It criticizes existing efforts for focusing on CTF-style challenges and component datasets, and states explicitly that foundations must go beyond autonomously solving CTFs and code challenges. Ambition is quantified at roughly 100×. The running example is an enterprise SOC mapped onto an OODA loop.

Bears directly on *Toward Deployment*, the realism taxonomy, and the operational-world-model vista.

### [Skill or Shortcut? AI, Competitive Cybersecurity Learning, and the Growing Gap Between Performance and Expertise](https://cylabacademy.org/pdfs/Skill_or_Shortcut_WhitePaper.pdf)

Kearns, Jones, Liang, Yin — CyLab Security and Privacy Institute, April 2026. 21 pages.

Six years of picoCTF platform data: 1M+ registered users, 14K+ classrooms, 10.7M+ solves across 561 problems. Median time-to-first-solve on hard challenges ran 40–340 minutes across 2021–2025 and fell to 5 minutes in 2026. Field-wide hard solve rates roughly tripled, from 5–7% to above 18%. The rank-1 to rank-50 score gap fell from 5,150 points in 2021 to 0 in 2026, so rankings were decided purely on completion time. Among returning users, 84% improved their score percentile on a second attempt pre-AI versus 41% post-2023 — a 43-point gap (n=800 and n=3,824). Section 3 rules out three alternatives: challenge difficulty calibration stayed stable, leak signatures were absent, and a stronger cohort would have lifted performance uniformly rather than splitting entrants from returners. The authors flag ceiling effects and demographic breadth as partial alternative explanations themselves. The conclusion is a measurement claim rather than an anti-AI one: a first-place finish now indexes efficiency of execution rather than depth of understanding.

Bears directly on the competitive-learning vista and the capture-the-flag work. Two of its load-bearing citations — "Gupta et al. (2025)" and "Mayoral-Vilches et al. (2025)" — were not verified here.

***

## 1 · Realism and the deployment gap

Feeds *Toward Deployment*, *Sim2Sim before Sim2Real*, the operational-world-model vista, and the RREP report.

**Insight**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity](https://arxiv.org/abs/2602.08690) — McFadden, Foley, Bates, Tsingenopoulos, Vyas, Mavroudis, Hicks, Pierazzi | USENIX Security 2026 | Eleven pitfalls across 66 papers. 40.9% evaluate in oversimplified environments. |
| [Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy](https://arxiv.org/abs/2606.28433) — Vandergrift, Elelimy, White | ICML 2026 Position Track | Argues optimizing a simulator score has quietly replaced studying decision-making. Simulator-as-target versus simulator-as-proxy. |
| [Building Better Environments for Autonomous Cyber Defence](https://arxiv.org/abs/2604.08805) — Hicks, Bates, McFadden, Symes Thompson, Foley, Chapman et al. | arXiv, Apr 2026 | What a cyber training environment would need to be for results to transfer. |
| [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/system/files/sec22-arp.pdf) — Arp, Quiring, Pendlebury, Warnecke, Pierazzi, Wressnegger, Cavallaro, Rieck | USENIX Security 2022 | Ten pitfalls in ML-for-security experiment design, with prevalence counts and worked demonstrations of the damage each causes. |
| [Chasing Shadows: Pitfalls in LLM Security Research](https://arxiv.org/abs/2512.09549) — Evertz, Risse, Neuer, Müller et al. (incl. Wressnegger, Quiring, Arp, Schönherr) | NDSS 2026 | The LLM-era sequel: nine pitfalls, audited across 72 peer-reviewed LLM-security papers from 2023–2024. |
| [Less is more? Rewards in RL for Cyber Defence](https://arxiv.org/abs/2503.03245) — Bates, Hicks, Mavroudis | arXiv, 2025 (4pp) | Attacks dense scaffolded rewards in cyber gyms; proposes a ground-truth score beyond return. |
| [Beyond Rewards in Reinforcement Learning for Cyber Defence](https://arxiv.org/abs/2602.04809) — Bates, Hicks, Mavroudis | arXiv, 2026 | The follow-up. |

**Foundation**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Towards the Deployment of Realistic Autonomous Cyber Network Defence: A Systematic Review](https://dl.acm.org/doi/pdf/10.1145/3729213) — Vyas, Mavroudis, Burnap | ACM Computing Surveys 58(1), Art. 5, 2026 | Systematic review of the distance between RL cyber-defence research and real network deployment. |
| [Multi-Agent Reinforcement Learning in Cybersecurity: From Fundamentals to Applications](https://arxiv.org/abs/2505.19837) — Landolt, Würsch, Meier, Mermoud, Jang-Jaccard | arXiv, 2025 | Current map of MARL cyber defense, AICA agents, and cyber gyms. |
| [CyGym: A Simulation-Based Game-Theoretic Analysis Framework for Cybersecurity](https://arxiv.org/abs/2506.21688) — Lanier, Vorobeychik | arXiv, 2025 | Zero-day simulator with a PSRO-style equilibrium framework over it. |
| [An Empirical Game-Theoretic Analysis of Autonomous Cyber-Defence Agents](https://arxiv.org/abs/2501.19206) — Palmer, Swaby, Harrold, Stewart, Hiles, Willis, Miles, Farmer | arXiv, 2025 | Double-oracle EGTA over blue and red DRL cyber agents at scale. |

***

## 2 · What a world model must contain

Feeds *Cyber World Modeling* and the operational-world-model vista.

**Insight**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [General agents contain world models](https://arxiv.org/abs/2506.01622) — Richens, Abel, Bellot, Everitt | ICML 2025 | Any agent that generalizes to a broad enough set of goals must have learned a predictive model, and that model can be recovered from its policy. |
| [What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://arxiv.org/abs/2507.06952) — Vafa, Chang, Rambachan, Mullainathan | ICML 2025 | Probes for whether a model that predicts well has actually recovered the generating structure. |
| [Evaluating the World Model Implicit in a Generative Model](https://arxiv.org/abs/2406.03689) — Vafa, Chen, Rambachan, Kleinberg, Mullainathan | NeurIPS 2024 (Spotlight) | Myhill–Nerode-based metrics. Implicit world models come out incoherent despite strong task performance. |
| [Critique of World Model](https://arxiv.org/abs/2507.05169) — Xing, Deng, Hou | arXiv, 2025 (v5 2026) | Sets the competing schools of world modeling against each other and argues for simulating actionable possibilities. |
| [How Far is Video Generation from World Model: A Physical Law Perspective](https://arxiv.org/abs/2411.02385) — Kang, Yue, Lu, Lin, Zhao, Wang, Huang, Feng | ICML 2025 | Video diffusion generalizes case-based from the nearest training example and fails out-of-distribution physics. |
| [World Models as an Intermediary between Agents and the Real World](https://arxiv.org/abs/2602.00785) — Yang | arXiv, Jan 2026 | Single-author framing piece. |

**Foundation**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748) — Chu, Zhang, Lin, Kong et al. (49 authors) | arXiv, 2026 | Levels-by-Laws taxonomy. Names a "social" law regime. |
| [Training Agents Inside of Scalable World Models](https://arxiv.org/abs/2509.24527) — Hafner, Yan, Lillicrap | arXiv, 2025 | Dreamer 4. Drops RSSM for transformer shortcut forcing. |
| [A Survey of State Representation Learning for Deep Reinforcement Learning](https://arxiv.org/abs/2506.17518) — Echchahed, Castro | arXiv, 2025 | Six-class taxonomy plus representation-quality metrics. |

***

## 3 · Factorization, identifiability, and the opponent latent

Feeds *FOE-Dreamer* and *Learn Structure*.

**Insight**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Rethinking State Disentanglement in Causal Reinforcement Learning](https://arxiv.org/abs/2408.13498) — Cao, Zhang, Cai, Liu, Zou, Abbasnejad, Huang, Gong, van den Hengel, Shi | arXiv, 2024 | Argues RL-specific structure makes heavy causal identifiability assumptions unnecessary — two constraints suffice. Contradicts the premise under a factored-latent design. |
| [R2-Dreamer: Redundancy-Reduced World Models without Decoders or Augmentation](https://arxiv.org/abs/2603.18202) — Morihira, Nahar, Bharadwaj, Kato, Hayashi, Harada | ICLR 2026 | Argues reconstruction spends capacity on task-irrelevant regions. |
| [Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.31361) — Leroy-Stone | 2026 World Modeling Workshop (5pp poster) | RSSM latent split into environment and teammate components with a theory-of-mind head. Cooperative case. |
| [Factored Latent Action World Models](https://arxiv.org/abs/2602.16229) — Wang, Shi, Hu, Rohling, Martín-Martín, Zhang, Stone | arXiv, 2026 | Per-entity factored latents evaluated against Genie and AdaWorld. |

**Foundation**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [From Identifiable Causal Representations to Controllable Counterfactual Generation: A Survey on Causal Generative Modeling](https://arxiv.org/abs/2310.11011) — Komanduri, Wu, Wu, Chen | TMLR 2024 | 72 pages. The identifiability assumption catalogue that block-identifiability proofs draw from. |
| [Unifying Causal Reinforcement Learning: Survey, Taxonomy, Algorithms and Applications](https://arxiv.org/abs/2512.18135) — da Costa Cunha, Liu, French, Mian | arXiv, 2025 | Places causal representation learning inside RL rather than beside it. |

***

## 4 · Strategic structure

Feeds *Learn Structure* and *Opponent (Agent) Modeling*.

**Insight**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Global Policy-Space Response Oracles for Two-Player Zero-Sum Games](https://arxiv.org/abs/2605.28273) — Zhang, Yang, Wang, Wang, Zhang | ICML 2026 | Best responses computed from restricted-game payoffs can look locally good while barely reducing global exploitability. Introduces population exploitability as a diagnostic. |
| [Policy Abstraction and Nash Refinement in Tree-Exploiting PSRO](https://arxiv.org/abs/2502.02901) — Konicki, Chakraborty, Wellman | AAMAS 2025 | Exploits extensive-form structure; subgame-perfect equilibrium directs exploration. |
| [Co-Learning Empirical Games & World Models](https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_2.pdf) — Smith, Wellman | Reinforcement Learning Journal 1:1–15, RLC 2024 | Dyna-PSRO. The world model and the empirical game learned together. |

**Foundation**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Empirical Game Theoretic Analysis: A Survey](https://www.jair.org/index.php/jair/article/view/16146) — Wellman, Tuyls, Greenwald | JAIR 82:1017–1076, 2025 | The reference statement of the method. |
| [Policy Space Response Oracles: A Survey](https://arxiv.org/abs/2403.02227) — Bighashdel, Wang, McAleer, Savani, Oliehoek | IJCAI 2024 | Catalogues every PSRO variant and the stated open problems. |
| [A Survey on Self-play Methods in Reinforcement Learning](https://arxiv.org/abs/2408.01072) — Zhang et al. | arXiv, 2024 (v4 2025) | Unified frame over PSRO, double oracle, and fictitious play. |

***

## 5 · Complementarity: definition and measurement

Feeds *Human-AI Complementarity*, *CHART*, and *Team Defense Game*.

**Insight**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Toward a science of human–AI teaming for decision making: A complementarity framework](https://doi.org/10.1093/pnasnexus/pgag030) — Gonzalez, Donahue, Goldstein, Heidari, Jalali, Schelble, Singh, Woolley | PNAS Nexus 5(3):pgag030, 2026 | Treats complementarity as an engineering target with named design levers: role partitioning, attention orchestration, knowledge infrastructure. |
| [A Decision Theoretic Framework for Measuring AI Reliance](https://dl.acm.org/doi/pdf/10.1145/3630106.3658901) — Guo, Wu, Hartline, Hullman | FAccT 2024, pp. 221–236 | Separates reliance level from rational belief updating. Defines a benchmark (max attainable with cooperation) and a baseline (max without), turning "neither would have reached this alone" into a measurable gap. |
| [When combinations of humans and AI are useful: A systematic review and meta-analysis](https://www.nature.com/articles/s41562-024-02024-1) — Vaccaro, Almaatouq, Malone | Nature Human Behaviour 8(12):2293–2303, 2024 | 370 effect sizes. On decision tasks, human-AI teams underperform the better of the two alone. |
| [Complementarity in human-AI collaboration: concept, sources, and evidence](https://www.tandfonline.com/doi/pdf/10.1080/0960085X.2025.2475962) — Hemmer, Schemmer, Kühl, Vössing, Satzger | EJIS 34(6):979–1002, 2025 | Separates complementarity *potential* from complementarity *effect*. Names information asymmetry and capability asymmetry as the two sources. |
| [From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making](https://arxiv.org/abs/2604.23896) — Raees, Papangelis | arXiv, Apr 2026 | Three competing views of reliance — Traditional, Appropriateness, Dominance — and the argument that results across them are not comparable. |
| [Two Sides of the Same Coin? Joint Perspectives From Shared Mental Models and Interactive Team Cognition Theories on Human-AI Team Cognition](https://journals.sagepub.com/doi/pdf/10.1177/10711813251358788) — Narayanan, Cohen, Feigh, Cooke | Proc. HFES 69(1):412–417, 2025 | Construct-validity attack on shared-mental-model measures applied to AI teammates; interaction-based alternative. |
| [Human-autonomy Teaming: Need for a guiding team-based framework?](https://doi.org/10.1016/j.chb.2023.107762) — O'Neill, Flathmann, McNeese, Salas | CHB 146:107762, 2023 | Argues definitional and construct-validity problems persist because the field works around the existing teams literature rather than through it. Paywalled. |

**Foundation**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [A Systematic Review and Taxonomy of Human–Agent Teaming Testbeds](https://pmc.ncbi.nlm.nih.gov/articles/PMC12743137/) — Chung, Holder, Shah, Yang | Human Factors 68(2):197–238, 2026 | Ten-attribute taxonomy over 103 testbeds. The frame a reviewer will reach for when asking what CHART adds. |
| [Measuring and Understanding Trust Calibrations for Automated Systems: A Survey of the State-Of-The-Art and Future Directions](https://dl.acm.org/doi/pdf/10.1145/3544548.3581197) — Wischnewski, Krämer, Müller | CHI 2023, Art. 755 | 96 calibration studies audited. Catalogue of measurement choices. |
| [Adaptive Human-Agent Teaming: A Review of Empirical Studies from the Process Dynamics Perspective](https://arxiv.org/abs/2504.10918) — Wang, Wu, Ma, Li, Zhang, Gu, Lu | arXiv, 2025 | T4 phase framework with per-phase metrics. The nearest thing found to authority shifting over the course of an interaction. |

***

## 6 · Difficulty, expertise, and the skill/shortcut question

Feeds the competitive-learning vista and the capture-the-flag work.

**Insight**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245) — Shen, Tamkin | arXiv, 2026 | RCT, n=52 developers learning an unfamiliar library. Evaluation scores 17% lower with AI assistance (d=0.738, p=0.010), with no significant speedup. Identifies which interaction patterns preserve learning. |
| [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/) — Bastani, Bastani, Sungu, Ge, Kabakcı, Mariman | PNAS 122(26):e2422633122, 2025 | +48% with AI access, −17% once it is removed. A correction exists (10.1073/pnas.2518204122). |
| [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) — Becker, Rush, Barnes, Rein | arXiv, 2025 | Experienced developers 19% slower with AI while believing they were 20% faster. |
| [Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study](https://doi.org/10.1016/S2468-1253(25)00133-5) — Budzyń, Romańczyk, Kitala et al. | Lancet Gastro Hep 10(10):896–903, 2025 | Adenoma detection rate in non-AI colonoscopies fell from 28.4% to 22.4% after AI exposure. Cite the Nov 2025 correction alongside it (10.1016/S2468-1253(25)00294-8). |
| [Navigating the Jagged Technological Frontier](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321) — Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon, Lakhani | Organization Science 37(2):403–423, 2026 | 12.2% more tasks and 25.1% faster inside the frontier; 19% less likely to be correct outside it. |
| [Deliberate Practice and Performance in Music, Games, Sports, Education, and Professions: A Meta-Analysis](https://doi.org/10.1177/0956797614535810) — Macnamara, Hambrick, Oswald | Psychological Science 25(8):1608–1618, 2014 | Deliberate practice explains under 1% of performance variance in professions. Paywalled; a repository record exists at Rice. |

**Foundation**

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [The linear logistic test model as an instrument in educational research](https://doi.org/10.1016/0001-6918(73)90003-6) — Fischer | Acta Psychologica 37(6):359–374, 1973 | Item difficulty decomposed into a weighted sum of the cognitive operations a task requires, with estimable weights. Paywalled. |
| [A Cognitive Load Theory Approach to Defining and Measuring Task Complexity Through Element Interactivity](https://link.springer.com/content/pdf/10.1007/s10648-023-09782-w.pdf) — Chen, Paas, Sweller | Educational Psychology Review 35, Art. 63, 2023 | Complexity as interacting elements relative to what the solver already holds in long-term memory. Makes difficulty person-relative, as IRT does. |
| [A cognitive design system approach to generating valid tests: Application to abstract reasoning](https://doi.org/10.1037/1082-989X.3.3.380) — Embretson | Psychological Methods 3(3):380–396, 1998 | Designing items to a target difficulty from a theory of the operations they require. Paywalled. |
| [Student Modeling Based on Problem Solving Times](https://link.springer.com/content/pdf/10.1007/s40593-015-0048-x.pdf) — Pelánek, Jarušek | IJAIED 25(4):493–519, 2015 | Models difficulty from time-to-solve rather than correctness. |
| [Psychometric Evaluation of the Cybersecurity Concept Inventory](https://doi.org/10.13016/m2bstz-uvb6) — Poulsen, Herman, Peterson, Golaszewski, Gorti, Oliva, Scheponik, Sherman | ACM TOCE 22(1), Art. 6, 2021 | Full IRT item analysis on a cybersecurity instrument. |
| [Procedural skill retention and decay: A meta-analytic review](https://doi.org/10.1037/bul0000481) — Tatel, Ackerman | Psychological Bulletin 151(6):696–736, 2025 | 1,344 effects. Roughly half of skill gains lost in about 6.5 months. Publisher-side free access is flagged but unconfirmed. |
| [When and where do we apply what we learn?: A taxonomy for far transfer](https://doi.org/10.1037/0033-2909.128.4.612) — Barnett, Ceci | Psychological Bulletin 128(4):612–637, 2002 | Names the dimensions along which a skill has to travel. Paywalled. |
| [Near and Far Transfer in Cognitive Training: A Second-Order Meta-Analysis](https://www.collabra.org/jms/article/view/203) — Sala, Aksaylı, Tatlidil, Tatsumi, Gondo, Gobet | Collabra: Psychology 5(1), Art. 18, 2019 | Meta-analysis of meta-analyses. Effects shrink toward zero as transfer distance grows. |

***

## 7 · Whether an evaluation measures anything

Cross-cutting. Feeds any claim about progress, including the RREP report.

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Position: Benchmarking is Limited in Reinforcement Learning Research](https://arxiv.org/abs/2406.16241) — Jordan, White, Castro da Silva, White, Thomas | ICML 2024 Position Track | Argues RL benchmark comparisons yield unreliable conclusions; proposes alternative experiment designs. |
| [AI Agents That Matter](https://arxiv.org/abs/2407.01502) — Kapoor, Stroebl, Siegel, Nadgir, Narayanan | arXiv, 2024 | Agent benchmarks optimize accuracy while ignoring cost; several leaderboard results collapse under a cost axis. |
| [Establishing Best Practices in Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825) — Zhu, Jin, Pruksachatkun, Zhang et al. | NeurIPS 2025 D&B | Audits agentic benchmarks for task- and outcome-validity errors. Supplies a checklist. |
| [Position: Evaluating Generative AI Systems Is a Social Science Measurement Challenge](https://arxiv.org/abs/2502.00561) — Wallach, Desai, Cooper, Wang et al. | ICML 2025 Position Track | Applies measurement theory, construct validity, and reliability to generative AI evaluation. |
| [Position: Why We Must Rethink Empirical Research in Machine Learning](https://arxiv.org/abs/2405.02200) — Herrmann, Lange, Eggensperger, Casalicchio et al. | ICML 2024 Position Track | ML benchmarking lacks inferential rigor; imports validity concepts from empirical statistics. |
| [BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices](https://arxiv.org/abs/2411.12990) — Reuel, Hardy, Smith, Lamparth, Hardy, Kochenderfer | NeurIPS 2024 D&B (Spotlight) | Scores 24 benchmarks against 46 lifecycle criteria. |
| [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879) — Singh, Nan, Wang, D'Souza et al. | NeurIPS 2025 D&B | Documents private testing, data asymmetry, and overfitting distorting arena rankings. |

***

## 8 · Getting reasoning out of an expert

Feeds the problem-solving and capture-the-flag protocols.

| Paper | Where | What it contains |
| ----- | ----- | ---------------- |
| [Cognitive Task Analysis: Eliciting Expert Cognition in Context](https://journals.sagepub.com/doi/pdf/10.1177/10944281241271216) — Brown, Power, Gore | Organizational Research Methods 28(3):375–404, 2025 | Rigor criteria for CTA and Critical Decision Method interviews. |
| [Concurrent or Retrospective Thinking Aloud in Usability Tests: A Meta-Analytic Review](https://dl.acm.org/doi/pdf/10.1145/3665327) — Hertzum | ACM TOCHI 31(3), Art. 37, 2024 | 42 comparisons. Retrospective protocols yield more explanations and more problem formulations than concurrent ones. |
| [Reliability and Inter-rater Reliability in Qualitative Research: Norms and Guidelines for CSCW and HCI Practice](https://dl.acm.org/doi/pdf/10.1145/3359174) — McDonald, Schoenebeck, Forte | PACM HCI 3(CSCW), Art. 72, 2019 | When inter-rater reliability is the wrong instrument, and what to report instead. |

***

## What the searches did not turn up

Stated as scope, not as conclusion. Each line names where the search ran.

- **IRT or Rasch modeling applied to CTF challenge difficulty.** OpenAlex title-and-abstract queries pairing "capture the flag" / "capture-the-flag" / "CTF" with "item response theory" or "Rasch" returned zero. Nine works total pair IRT with cybersecurity at all.
- **AI-induced skill atrophy in security, CTF, or penetration testing specifically.** No peer-reviewed paper or preprint found. Vendor surveys only, which were not verified.
- **A critique of CybORG, CAGE, CyberBattleSim, or Yawning Titan realism at IEEE S&P, CCS, USENIX Security, NDSS, or ACSAC, 2024–2026.** That literature sits on arXiv, in ACM Computing Surveys, and in workshops. The USENIX Security 2026 SoK above is close to the only exception. CCS and ACSAC 2024–2025 coverage was incomplete — DBLP truncated. USENIX Security 2024–2026 and NDSS 2025–2026 were scanned in full.
- **A 2023–2026 survey of opponent or agent modelling in MARL.** Searches returned Albrecht & Stone (2018) and Hernandez-Leal et al. (2017/2019). The self-play survey above is the nearest in-window substitute.
- **A definition or measurement of "strategic dependence"** — where in a long interaction a best action actually depends on the adversary. Searches returned opponent shaping, adversarial minority influence, and multi-agent influence diagrams. Nothing matching.
- **Forward citations of Dyna-PSRO from 2024–2026**, beyond its own RLC/RLJ version.
- **A standalone critique or reproducibility study of DreamerV3.** Criticism exists only inside method papers.
- **Tacit knowledge across the human-AI boundary, as a defined and measured construct**, in HCI or CSCW 2022–2026.
- **Stimulated recall anchored to logs, as a validated method.** The validity literature on stimulated recall is pre-2022 or sits in education and sport-coaching journals.
- **A human-AI complementarity position paper at a core ML venue**, and a flagship causal-representation-learning identifiability position paper.

_Last updated: 2026-08_
