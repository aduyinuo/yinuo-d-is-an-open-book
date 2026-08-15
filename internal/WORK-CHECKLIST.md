# Working checklist

Everything assigned, sorted by what kind of work it is rather than by page.
Task numbers refer to the task list.

---

## 1. Collect

Material that has to be in reach before anything else can be done properly.

### From the machine
- [ ] ARL white paper `ARL_Tactical_Workflows_White_Paper_2026.docx` — binary on G:, not
      readable by the file tools and G: is not mounted in bash. Route: copy the one file
      into `Documents\GitHub`, unzip, read `word/document.xml`. (#17)
- [ ] `Research Opportunity Topic OPT-0122.pdf` — password-protected. Needs an
      unprotected copy. (#17)
- [ ] Meeting notes and transcripts, per project, for deck vocabulary (#4):
      LucidWorld `Feedback\01.30 PSRO Env + FOEDreamer`, PickYourBattles
      `meeting_transcripts` (incl. two Lanier sessions), BeRealistic
      `notes\meeting notes`, UnitedForces `Grace-SOC`, DesignTheGame
      `2025 Fall Pilot Developer Interview Scripts`.
- [ ] FOE-Dreamer experiment material: `architecture.pdf`, `COSE Figures\*`,
      `liam_bringup`, `imagination.pdf`, `c2.pdf`. (#22)
- [ ] Learn Structure state: `Notes\Latex\cards\*`, `sections\*`,
      `cited_works_inventory.md`. (#4)
- [ ] CyGym: `Code\env_cygym\cygym-papers\978-3-032-08064-6_8.txt`, Lanier talk and
      interview transcripts. (#16)
- [ ] Proof-technique bank: `AAAI27_git\agent assistance\co-lit rev\philosophy and
      methods of taxonomies\` — eight files. (#8)
- [ ] qcard protocol, `polya_heuristics.rmd`, method registry. (#8)
- [ ] 5-researcher profiling material, `[9] Strings Attached\2026 Reinstatement
      Application`. (#21)
- [ ] Resources source PDFs in `[7] Growth\research` for the download boxes. (#18)

### From the web

**The named reading list** (#6)
- [ ] ICLR world-models workshop — the organizers' own submission. The 2nd
      Workshop on World Models: Understanding, Modelling and Scaling is the likely
      venue; find the organizers' paper, not just the CFP.
- [ ] ICML talk on causal models and transformers — speaker not yet identified.
- [ ] Arvind Narayanan, ICML 2026 keynote — annotated slides page located.
- [ ] Fung, *Embodied AI Agents: Modeling the World*, arXiv 2506.22355 — located,
      notes drafted, full PDF still to store.
- [ ] Yilun Du, compositional paper — compositional generation / composing models,
      2024 or 2025.
- [ ] ICML position paper on cognitive AI.
- [ ] More Karpeles writing, as style samples beyond the one Medium essay. (#8)

**Prior work each deck has to represent** (#4)

Metrion — read off the paper's own reference list, so these six are exact:
- [ ] Grimaldi, Ribiollet, Nespoli & Garcia-Alfaro 2023. *Toward next-generation
      cyber range: a comparative study of training platforms.* ESORICS workshops,
      Springer, 271–290.
- [ ] Janisch, Pevný & Lisý 2023. *NASimEmu: Network Attack Simulator & Emulator
      for Training Agents Generalizing to Novel Scenarios.* ESORICS 2023 workshops,
      589–608. doi:10.1007/978-3-031-54129-2_35
- [ ] Nguyen, Chen, Hasegawa, Fukushima & Beuran 2024. *PenGym: Pentesting Training
      Framework for Reinforcement Learning Agents.* ICISSP, 498–509.
- [ ] Orange Cyberdefense. *GOAD: Game of Active Directory.*
      github.com/Orange-Cyberdefense/GOAD
- [ ] MITRE ATT&CK, enterprise matrix, v19.1.
- [ ] MITRE D3FEND.

Cyber-Agent-Flow — likewise from its reference list:
- [ ] Deng et al. 2024. *PentestGPT.*
- [ ] Shen et al. 2024. *PentestAgent.*
- [ ] Ghanem & Chen 2023. *IAPTF*, RL for automated penetration testing.
- [ ] Aletkin et al. 2024. *EnIGMA.*
- [ ] Muzsai, Imolai & Lukács 2024. *HackSynth.*
- [ ] Ji et al. 2025. *CTFAgent.*
- [ ] Zhu et al. 2025. *CVE-Bench.*
- [ ] HexStrike AI 2026.
- [ ] Anthropic and MCP contributors 2025. *Model Context Protocol.*
- [ ] Offensive Security 2026. Kali MCP server.
- [ ] Ollama 2023; BerriAI *LiteLLM* 2023.
- [ ] Acosta, Medina, Ellis, Clarke, Rivas & Newcomb 2021. Network data curation
      toolkit — the source of the pivoting scenario.
- [ ] Deng et al. 2026, on planning and context-management limits of LLM pentest
      agents.

CTF Universe — the 3-page PDF's reference list was truncated in extraction;
pull the seven entries from the file itself, then collect.

CHART — cited in the introduction; full citations to pull from the chapter:
- [ ] Stoll et al. 2021 (alert fatigue), Boyarchuk et al. 2021 (speed of lateral
      movement), Holland et al. 2022 (deceptive signals), Chen et al. 2018
      (tiered authority), Lee & See 2004 (trust calibration).

FOE-Dreamer — several PDFs already sit in the project's `Literature` folder
(`Option-Critic.pdf`, `LIAM.pdf`, `LIAM_full.pdf`, `IFactor.pdf`, `AM.pdf`,
`RL-Murphy.pdf`); confirm each identifier before citing:
- [ ] Hafner, Lillicrap, Norouzi & Ba. *Mastering Atari with Discrete World
      Models* (DreamerV2), arXiv:2010.02193.
- [ ] Hafner, Pasukonis, Ba & Lillicrap. *Mastering Diverse Domains through World
      Models* (DreamerV3), arXiv:2301.04104.
- [ ] Papoudakis, Christianos & Albrecht. *Agent Modelling under Partial
      Observability for Deep Reinforcement Learning* (LIAM), NeurIPS 2021.
- [ ] Liu et al. *Learning World Models with Identifiable Factorization*
      (IFactor), NeurIPS 2023, arXiv:2306.06561.
- [ ] Bacon, Harb & Precup. *The Option-Critic Architecture*, AAAI 2017.
- [ ] Yu et al. *Model-Based Opponent Modeling* (MBOM), NeurIPS 2022,
      arXiv:2108.01843.

Learn Structure — identifiers to verify against the project's
`cited_works_inventory.md` and `references.bib`:
- [ ] Wellman, Tuyls & Greenwald 2024. *Empirical Game-Theoretic Analysis: A
      Survey*, JAIR 79, arXiv:2403.04018.
- [ ] Lanctot et al. 2017. *A Unified Game-Theoretic Approach to Multiagent
      Reinforcement Learning* (PSRO), arXiv:1711.00832.
- [ ] McMahan, Gordon & Blum 2003. Double oracle, ICML.
- [ ] Smith & Wellman 2024. *Co-Learning Empirical Games and World Models*
      (Dyna-PSRO), RLC, arXiv:2305.14223.
- [ ] Schvartzman & Wellman 2009 (RL oracle); Phelps et al. 2006 (genetic oracle).
- [ ] Kearns, Littman & Singh 2001. *Graphical Models for Game Theory*, UAI.
- [ ] Candogan, Menache, Ozdaglar & Parrilo 2011. Flows and decompositions of
      games; and Cai, Candogan, Daskalakis & Parrilo 2016.
- [ ] Givan, Dean & Greig 2003 (model minimization); Ferns, Panangaden & Precup
      2004 (bisimulation metrics); Abel, Hershkowitz & Littman 2016 (value loss
      under abstraction).
- [ ] Boutilier, Dean & Hanks 1999 (factored MDPs).
- [ ] Spirtes, Glymour & Scheines 2000. *Causation, Prediction, and Search.*
- [ ] Gilpin & Sandholm 2006 (value-similarity abstraction).
- [ ] Wellman & Prakash 2014 (EGTA in adaptive cyber-defense).

**Canonical sources per teaching concept** (#8) — one original per concept:
- [ ] ELBO: Kingma & Welling, *Auto-Encoding Variational Bayes*, arXiv:1312.6114;
      Blei, Kucukelbir & McAuliffe, *Variational Inference: A Review for
      Statisticians*, arXiv:1601.00670; Jordan, Ghahramani, Jaakkola & Saul 1999.
- [ ] RSSM: Hafner et al. 2019, *Learning Latent Dynamics for Planning from
      Pixels* (PlaNet), arXiv:1811.04551, plus DreamerV2/V3 above.
- [ ] Identifiability: IFactor above, and a causal-representation-learning source
      for the identifiability framing.
- [ ] EGTA: the Wellman survey, for regret and exploitability as defined there.
- [ ] Causal models: Pearl 1995 on causal diagrams (back-door, front-door) and
      Pearl 2009, *Causality.*
- [ ] Options: Sutton, Precup & Singh 1999.
- [ ] Library learning: Ellis et al., *DreamCoder*; Sumers, Yao, Narasimhan &
      Griffiths, *CoALA*, arXiv:2309.02427.
- [ ] Protocol analysis: Ericsson & Simon, *Protocol Analysis: Verbal Reports as
      Data* — already on the Resources shelf.
- [ ] Critical decision method: Crandall, Klein & Hoffman 2006, *Working Minds* —
      already on the shelf.
- [ ] Inter-rater reliability: Cohen 1960 (kappa), Krippendorff (alpha), Hallgren
      2012 (tutorial).

**Environments** (#16, #22)
- [ ] CyGym — Lanier et al., Springer chapter, doi 10.1007/978-3-032-08064-6_8;
      text already in the PickYourBattles folder. Repository too.
- [ ] CybORG — Standen et al. 2021, arXiv:2108.09118.
- [ ] CyberBattleSim — Microsoft 2021.
- [ ] Cyber Wheel — Oak Ridge National Laboratory.
- [ ] CyberVAN — Chadha et al. 2016.
- [ ] GOAD, NASimEmu, PenGym — as listed under Metrion.

Identifiers above that were not read directly off a reference list this session
are marked by being unlisted in the Metrion and Cyber-Agent-Flow blocks; verify
each before it appears on a slide or a page.

**Publication links** (#20)
- [ ] A link for each of roughly twenty published items — DOI, publisher page,
      arXiv, or hosted PDF. Every one exists; not finding one means not looking
      hard enough.

**For specific builds**
- [ ] Guidance on visualizing a research agenda, plus real examples of agenda
      diagrams from faculty and lab pages worth learning from. (#21)
- [ ] LinkedIn posts 7485515295332196352 and Hui Zhang 7485366203754934273, and
      whether Iframely lists LinkedIn as a supported provider. (#23)
- [ ] ICML and NeurIPS oral talk recordings or slide decks, as models for pacing a
      20-minute talk. (#4)

### Waiting on Max
- [ ] Photos — shared album or Drive folder, dumped whole. (photo pipeline built)
- [ ] Headshots: Nazim, Saika, Nowmi, Guerra, Akbar, Song, Keim; reading-group
      tiles for Siyu Liu, Michael Lanier, students. (#14)
- [ ] Thesis proposal / Google Slides deck — under the CMU account, unreachable
      from the connected Drive. (#11)
- [ ] Kaizen (TRI): submitted date, role, what it proposed. (#13)
- [ ] Yansi Keim affiliation — UTEP on the page, Albany in the public record. (#15)
- [ ] GitBook personal access token, to publish the slides integration. (#10)

---

## 2. Read

In full, not skimmed. Notes in LaTeX, one item per file, `subfiles`, compiled to
`build/`. Every note records: what it is, what it argues, rephraseable sentences
kept verbatim, and where it should surface in the 5-year vista pages.

- [ ] ARL white paper and topic OPT-0122. (#17)
- [ ] The six world-model items. (#6)
- [ ] CHART chapter — 29 pages, only the abstract and intro read so far. (#3)
- [ ] Metrion, Cyber-Agent-Flow, CTF Universe — text extracted, spines drafted. (#3)
- [ ] Meeting notes per project, for vocabulary. (#4)
- [ ] The taxonomies / axiomatic-method bank. (#8)
- [ ] 5-researcher profiling material, read for evaluation criteria. (#21)

---

## 3. Reason

Judgment that has to happen before writing, and that is where the last few
attempts went wrong.

- [ ] Per project: what is genuinely teaching-worthy — portable, derivable,
      wrong-able, teachable. ELBO is the worked example. (#8)
- [ ] The big chunks for Learn With Me and what sits under each: empirical
      game-theoretic analysis, world modeling, causal models, user research, and
      whatever else the reading turns up. (#8)
- [ ] Per deck: the four questions — why the problem matters; what this does that
      prior work does not, and what idea makes that possible; the evidence and its
      circumstances; the one idea to take home. (#4)
- [ ] What the agenda diagram must *show*, derived from the criteria used to judge
      those five careers. Shallow is the failure mode to avoid. (#21)
- [ ] Which experiments and which realism claims carry the Training page. (#22)
- [ ] A badge scheme that makes workshop versus full paper obvious in column one. (#12)
- [ ] What belongs in the publications link column, and how to keep it compact. (#20)
- [ ] What counts as a meaningful activity update, given it must never be a count
      of events or bytes. (#7)

---

## 4. Create

- [ ] Reading notes, one `.tex` per item, individually compilable. (#6, #17)
- [ ] A 20-minute deck per project, with annotation, in the project's own
      vocabulary. Placeholders where results do not exist. (#4)
- [ ] Learn With Me: hub, big-chunk pages, concept pages, linked from each
      project page. Written in the Karpeles register. (#8)
- [ ] Every project page in three sections: TL;DR, slide show, the rest. (#9)
- [ ] Training in Realistic Environments, rewritten as FOE-Dreamer, with its own
      diagram or animation. (#22)
- [ ] CyGym page and figure. (#16)
- [ ] The research-agenda diagram. (#21)
- [ ] Publications: fourth column, and the badge fix. (#12, #20)
- [ ] Resources: a download box at the head of each page; text stripped back to
      facts. (#18, #19)
- [ ] Photo walls, once photos exist. (pipeline built)
- [ ] Activity board: GitHub Projects as a signal, generated update text, the
      avatar on the active project, click-through detail. (#7)
- [ ] LinkedIn posts on the Opinion page — real embed if Iframely supports it,
      screenshot plus link otherwise. (#23)
- [ ] CV: preprints, posters, the 2026 items, references commented out. (in flight)
- [ ] The inline slide viewer, published and installed. (#10)

---

## 5. Verify

Nothing counts as done until it has been checked, and the check is mine to run.

- [ ] Decks: slide count, narration length against 20 minutes at 140 wpm, notes on
      every slide, renders through the pptx-to-page pipeline.
- [ ] Pages: every link and image resolves, no conflict markers, no leaked paths.
- [ ] Reading notes: each compiles alone and through `main.tex`.
- [ ] CV: compiles under XeLaTeX into `build/`, bibliography sections populated.
- [ ] Photo pipeline on real photos: dates parsed, duplicates caught, GPS stripped
      from published copies.
- [ ] Activity board: reflects real collected data, not seeded placeholders.

---

## Priority

Stated by Max: presentable diagrams for the research, including the 5-year vista
pages, and sharper discussion around them, which depends on reading the position
and insight papers. That feeds the RREP Year-1 report. Everything else matters
but comes after.

Collection serves two purposes at once. It is what the writing needs, and it is
what Max reads while the coding happens. So it goes first and gets delivered as a
bundle rather than consumed silently.

## Order

**First, and delivered as a reading bundle**
1. CyLab autonomy whitepaper; competitive cybersecurity learning whitepapers. (#24)
2. The six named world-model items, plus the ARL white paper. (#6, #17)
3. The position and insight papers behind the three 5-year vista pages. (#26)

Each arrives as a PDF plus a LaTeX note recording what it argues, sentences worth
reusing verbatim, and where it bears on the vista pages and the report.

**Then, the priority build**
4. The research-agenda diagram, with depth taken from the profiling criteria. (#21)
5. A diagram per 5-year vista page, and the discussion sharpened against the
   reading. (#26)
6. The RREP Year-1 report. (#25)

**Then everything else, in this order**
7. CV (in flight), publications link column and badges — self-contained.
8. Decks, then the three-section project-page restructure that carries them.
9. Learn With Me, which depends on the reading and the concept decisions.
10. Training-page rewrite and CyGym.
11. Resources rewrite and download boxes.
12. Activity board, LinkedIn embeds, inline slide viewer.
13. Photos when they arrive.
