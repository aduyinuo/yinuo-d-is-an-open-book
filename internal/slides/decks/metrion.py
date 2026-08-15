import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from deckbuilder import Deck

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                   "slides-source", "metrion.pptx")

d = Deck("Realistic Enough for What?",
         "Metrion: a multidimensional framework for evaluating cyber environments\n"
         "Maria Rigaki · Yinuo Du · Carlos A. Catania",
         "Good morning. I'm Yinuo Du, from the University of Texas at El Paso, and this "
         "is joint work with Maria Rigaki and Carlos Catania at Czech Technical "
         "University in Prague.\n---\n"
         "The title is the question we think the field is not asking. We describe "
         "environments as realistic, but realistic enough for what?")

d.statement("A defender that looks excellent may have been tested against nothing",
            "Alerts fire. Routine activity is sparse.",
            "Picture a benchmark for an autonomous defender. Attacks generate alerts, but "
            "the routine life of the enterprise is barely there: few normal logins, little "
            "administrator maintenance, limited file-share access, almost no background "
            "traffic.\n---\n"
            "The defender scores well. But it scored well because malicious behavior was "
            "presented against a clean baseline. That result is valid for the benchmark. It "
            "does not support a claim about deployment in an enterprise, where the whole "
            "difficulty is separating attacks from noisy legitimate activity.")

d.points("The same gap appears on the offensive side",
         ["In NASimEmu an action succeeds in simulation,",
          "and fails against the real service.",
          "PenGym reports the same simulation-to-reality gap."],
         "This is not only a defensive problem. In NASimEmu, an attack action can succeed "
         "deterministically in the simulator and then fail against the corresponding real "
         "service in the emulator, because the simulator abstracts away the service and "
         "operating-system fidelity that decides whether an exploit actually works. PenGym "
         "reports an analogous gap.\n---\n"
         "So an agent that looks competent in the abstract configuration need not stay "
         "competent against real software. Its score reflects its capability and also which "
         "environmental conditions the environment happened to model or omit.")

d.statement("Feature lists do not tell you what a claim needs",
            "Hosts, vulnerabilities, services, actions — none of these say whether the "
            "environment supports the claim being made.",
            "Environment papers describe what they implement: hosts, vulnerabilities, "
            "services, available actions. That tells you what is inside. It does not tell "
            "you whether the environment can support a particular evaluation claim.\n---\n"
            "Alert triage depends on benign activity and telemetry. Privilege escalation "
            "depends on identity state, credential artifacts, operating-system behavior, and "
            "the consequences of actions. Exfiltration depends on external channels, "
            "monitoring, baselines, and defensive controls. Different claims, different "
            "requirements.")

d.statement("So ask a different question", 
            "Not: is this environment realistic?\nBut: does it have the realism the "
            "objective requires?",
            "That reframing is the whole contribution. We stop asking whether an environment "
            "is realistic in general, and start asking whether it contains the realism "
            "properties required by a given evaluation objective.\n---\n"
            "If you remember one thing from this talk, remember that suitability is not a "
            "property of an environment. It is a property of an environment paired with an "
            "objective.")

d.section("How the framework is built",
          "Three steps: derive, mark, grade. Let me take them in order.")

d.points("Derive requirements from what techniques need",
         ["Walk ATT&CK and D3FEND technique by technique.",
          "Record what each needs the environment to provide, model, or emit.",
          "Cluster into eleven realism dimensions.",
          "115 concrete scoring elements underneath them."],
         "First, we derive realism elements from MITRE ATT&CK and D3FEND. For each "
         "technique we record what it requires an environment to provide, to model, or to "
         "emit.\n---\n"
         "Clustering those per-technique requirements gives eleven realism dimensions. Under "
         "the dimensions sit 115 concrete scoring elements. An element is pitched at the "
         "level where a missing property makes a whole class of techniques either "
         "inexpressible or unobservable.\n---\n"
         "Note the direction of derivation. We are not cataloguing what environments happen "
         "to implement. We are asking what the techniques demand.")

d.figure("Eleven dimensions, in five groups",
         "Infrastructure · organizational behavior · security layer · agent interface · "
         "external context",
         "The eleven dimensions group by which part of the evaluation they affect.\n---\n"
         "Infrastructure covers topological, service, and operating-system realism: do the "
         "network, services, and hosts resemble a real technical system?\n---\n"
         "Organizational behavior covers identity, temporal, and benign activity: are there "
         "realistic users, credentials, routine activity, and time-dependent behavior?\n---\n"
         "The security layer covers defensive controls and telemetry. The agent interface "
         "covers action and observation realism. External context covers the ecosystem "
         "outside the lab network.",
         label="Table 1 — dimensions grouped by what they affect")

d.points("Then mark the objective, and grade the environment",
         ["Each element: critical, useful, or not needed.",
          "Each environment: full, partial, absent, or unknown.",
          "Weights 2 and 1; coverage 1, 0.5, 0.",
          "Fit score is the weighted average."],
         "Second, for a given evaluation objective, we mark each element critical, useful, "
         "or unnecessary. Third, we grade how well an environment covers each element as "
         "full, partial, absent, or unknown, reading its papers, documentation, and "
         "code.\n---\n"
         "Combining them: importance gives a weight, two for critical and one for useful. "
         "Coverage gives a value, one for full, a half for partial, zero for absent. The fit "
         "score is the weighted average, from zero to one. Unknown coverage is excluded from "
         "the average and instead lowers a separate completeness measure, so ignorance never "
         "flatters an environment.")

d.statement("One rule overrides the score",
            "A single missing critical property invalidates the evaluation, whatever the "
            "average says.",
            "One rule overrides the fit score. If any critical requirement is absent, the "
            "environment is not suitable for that objective, full stop.\n---\n"
            "We do this because a weighted average can hide a fatal hole. A single missing "
            "critical property can invalidate the evaluation no matter how good everything "
            "else looks. Otherwise, an environment is suitable above a threshold, "
            "provisionally 0.75, partially suitable below it, and incomplete when too much of "
            "the profile is unknown. Those weights and that threshold are provisional, and "
            "they are one of the things we want feedback on.")

d.section("A worked example: GOAD, twice",
          "The clearest way to show what this buys you is to run one environment against "
          "two objectives.")

d.figure("GOAD, unchanged, judged against two objectives",
         "Dashed polygon: what the objective requires. Solid polygon: what GOAD covers.",
         "GOAD is an emulated multi-domain Active Directory environment. It gives you "
         "realistic Windows hosts, Active Directory services, credentials, and "
         "attacker-facing interactions. It has no benign background activity, no defensive "
         "monitoring, no telemetry, no temporal dynamics, no external ecosystem.\n---\n"
         "In each radar, the dashed polygon is the objective's requirement and the solid "
         "polygon is GOAD's coverage. A dimension is met when the solid polygon reaches the "
         "dashed contour.\n---\n"
         "I should be honest about the status of these grades: they are a preliminary, "
         "dimension-level reading of GOAD's documentation and code, not element-level "
         "scoring.",
         label="Figure 2 — GOAD radars, both use cases")

d.two_col("Same environment, opposite verdicts",
          "Credential privilege escalation",
          ["Critical: service, OS, identity, action, observation",
           "GOAD covers all five fully",
           "Fit 0.88 — suitable"],
          "Targeted data exfiltration",
          ["Critical also: temporal, defensive, benign, telemetry, external",
           "GOAD absent on all five",
           "Fit 0.39 — not suitable"],
          "For credential-based privilege escalation, the critical requirements are service, "
          "operating-system, identity, action, and observation realism. GOAD covers all five "
          "fully. The axes it leaves partly unmet, topological and temporal, are only useful, "
          "not critical. Fit score 0.88, nothing critical missing, so GOAD is "
          "suitable.\n---\n"
          "For targeted data exfiltration the requirement extends along the context axes: "
          "temporal dynamics, defensive controls, benign activity, telemetry, and external "
          "ecosystem are all critical. GOAD is absent on exactly those five. The solid "
          "polygon collapses toward the center precisely where the objective needs it to "
          "reach. Fit 0.39, five critical requirements unmet, the hard constraint fires, and "
          "GOAD is not suitable.\n---\n"
          "Same environment. Not changed in any way. Suitable for one objective, unsuitable "
          "for the other.")

d.statement("What this makes visible",
            "Environment limitations stop being a matter of taste and become a list of "
            "unmet requirements.",
            "The framework makes limitations explicit by connecting an evaluation claim to "
            "the realism properties it requires. The GOAD example is the intended use in "
            "miniature: the same environment supports one objective and fails another "
            "because the missing properties differ.\n---\n"
            "This is different from prior environment taxonomies, which classify environments "
            "by the features they implement. We classify by what techniques require.")

d.points("What is preliminary, said plainly",
         ["Dimension-level proxy grades, not element-level scoring.",
          "Thirteen environments, first-pass reading, not validated.",
          "ATT&CK and D3FEND are themselves curated abstractions.",
          "Enterprise IT matrix only."],
         "I want to be clear about what is not yet done. The framework is designed for "
         "element-level scoring across 115 elements, but the current comparison of thirteen "
         "publicly inspectable environments uses dimension-level proxy grades over the eleven "
         "dimensions. Those grades are a first-pass reading and are not yet validated, so "
         "they miss finer distinctions that element-level scoring would surface.\n---\n"
         "ATT&CK and D3FEND are themselves curated abstractions, so the dimension set needs "
         "external validation. And we use the enterprise IT matrix; other domains are future "
         "work.")

d.points("Validation is interviews, then a survey",
         ["Practitioners in offensive, defensive, and environment-building roles.",
          "Which dimensions to add, remove, split, or merge?",
          "Do they agree on importance for a given objective?"],
         "The validation plan is semi-structured interviews with practitioners across "
         "offensive, defensive, and environment-development roles. The interviews ask whether "
         "the dimensions match how experts actually assess realism, whether any are redundant "
         "or missing, and whether the three-level scale is appropriate.\n---\n"
         "That addresses two questions: which dimensions practitioners would add, remove, "
         "split, or merge, and whether they agree with each other on a dimension's importance "
         "for a given objective. We will consolidate the set from the results, and a broader "
         "survey follows.")

d.points("Three questions I would like your help with",
         ["Are eleven dimensions and 115 elements the right granularity?",
          "Does critical / useful / not needed capture what an objective needs?",
          "Is deriving from ATT&CK and D3FEND a sound basis?"],
         "This is a poster, and the work is preliminary, so I would genuinely like feedback "
         "on three things.\n---\n"
         "First, granularity: are eleven dimensions decomposed into 115 scoring elements at "
         "the right level? Second, the scale: does critical, useful, not needed adequately "
         "represent what an objective requires? Third, the basis: is deriving realism "
         "requirements from ATT&CK and D3FEND, rather than cataloguing environment features, "
         "the right foundation for comparing environments?")

d.statement("Realistic enough for what?",
            "Suitability belongs to the pair, not the environment.\n"
            "Scorecard: stratosphereips.github.io/realism-framework",
            "So, to leave you with one idea: suitability is a property of the environment and "
            "the objective together, never of the environment alone.\n---\n"
            "The interactive scorecard, the requirement profiles, and the per-environment "
            "evaluations are online at the address on the slide. Please come and argue with "
            "me at the poster. Thank you.")

d.save(os.path.abspath(OUT))
print("built", os.path.abspath(OUT))
