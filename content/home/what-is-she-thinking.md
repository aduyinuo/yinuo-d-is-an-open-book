---
description: Questions on my mind and others' opinions
icon: face-thinking
---

# Headspace

<p align="right"><a href="https://open.spotify.com/playlist/61BcFgUWfw0sHiW9b54BYr?si=91057be82b53477e"><em>Spotify Playlist</em></a></p>

<mark style="color:$primary;">When is a cybersecurity decision an RL problem?</mark> How to find <mark style="color:$primary;">interesting cybersecurity challenges</mark> that can motivate methodological innovations in <mark style="color:$primary;">(model-based) reinforcement learning</mark> (i.e., impose pressure on the central challenges in RL, for ex, distributional shift)?

* [A rule of thumb: is counterfactual reasoning hard and non-obvious?](https://nanjiang.cs.illinois.edu/applied/) _(by Nan Jiang)_
* [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/system/files/sec22-arp.pdf)
* [Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy](https://arxiv.org/abs/2606.28433)
* [SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity](https://arxiv.org/abs/2602.08690)
* [World Models: Understanding, Modeling, and Scaling](https://openreview.net/pdf?id=KR1PsFVRYo)

What is "<mark style="color:$primary;">Human-Centered</mark> Cybersecurity"?

* [NIST concept paper on HCC](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=962460)

If there's <mark style="color:$primary;">a genie of world modeling</mark>, what wishes should I make?

* [Introspective Interpretability](https://lingo.csail.mit.edu/blog/introspective_interpretability/) (by _Belinda Z. Li)_
* [Failure-aware Causal Training](https://arxiv.org/pdf/2608.10232) _(by Nicklas Hansen)_
* [Test-Time Continual Learning](https://ttcl-agents.github.io/) (continuously <mark style="color:$primary;">acquire, consolidate, and refine</mark> knowledge and capabilities during <mark style="color:$primary;">deployment</mark>, without catastrophic forgetting or repeated large-scale retraining.)
* [Factored Latent Action World Models](https://arxiv.org/abs/2602.16229)
* [Generalizable Action-Conditioned World Models](https://arxiv.org/pdf/2607.27599) _(by Yilun Du)_
* [Critique of World Model](https://arxiv.org/abs/2507.05169)
* When does an <mark style="color:$primary;">agent</mark> have the need to model the world in the first place?
  * [World Model as Intermediary](https://github.com/aduyinuo/yinuo-d-is-an-open-book/blob/main/content/.gitbook/assets/world-models-as-intermediary.pdf) _(by Sherry Yang)_
  * [The Self Requires Learning ](https://philpapers.org/archive/RENTSR.pdf)_(by Mengye Ren)_
  * [General agents contain world models](https://arxiv.org/abs/2506.01622)

How can we rethink problems from <mark style="color:$primary;">a multi-model/agent perspective</mark>?

* [Taesoo Kim](https://taesoo.kim/)'s [interview ](https://commandline.microsoft.com/taesoo-kim-interview-mdash-security-research/)for FORGE
* [Communicative World Model](https://arxiv.org/abs/2508.06659) for Adaptive RL
* [A Single Model is Not All You Need](https://proceedings.mlr.press/v235/du24d.html)

<mark style="color:$primary;">How much "human" do we want "in the loop"</mark> of cybersecurity decision-making?

* A [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7485366207047692288/) (&#x62;_&#x79; Hui Zhang_)

What is <mark style="color:$primary;">mind</mark> and what is <mark style="color:$primary;">muscle</mark>?

* [Tricki](https://gowers.wordpress.com/2008/11/28/very-brief-tricki-update/)
* When does a \`\`<mark style="color:$primary;">trick</mark>'' become <mark style="color:$primary;">domain-specific</mark>? At a larger scale, how does academic/<mark style="color:$primary;">professional training</mark> shape a person's <mark style="color:$primary;">thinking style</mark>? When does it turn sour and become "<mark style="color:$primary;">set in one's own way</mark>"?  Can we call that <mark style="color:$primary;">bias</mark>?

What are the relationship between <mark style="color:$primary;">cyber agents</mark> and <mark style="color:$primary;">physical agents</mark>? What are their respective unique challenges? What are transferable across these two domains?

* What are the agentic methods/tricks embraced by the industry so far? Can we observe any patterns?
* What agentic approaches does current SOC stack involve? What ML approaches does current <mark style="color:$primary;">SOC stack</mark> involve?
  * [NSF CyberAI Innovation: Adversarial Causal Reasoning for SOC](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2622986) (by [Wajih Ul Hassan](https://www.linkedin.com/in/wajihulhassan/?skipRedirect=true))
* What telemetry should a defense agent engage with? Is it feasible/beneficial to reform the stack?

What are the existing ways to determine the exit condition in an algorithm? In general, how to make the judgement that "enough is enough"?

* How many use-cases are needed to design the taxonomy of realism?
* How many human-subjects are needed to ensure the power of statistic significance?

How exactly can <mark style="color:$primary;">opponent modeling</mark> benefit network defense? What <mark style="color:$primary;">network security (or specifically, adversary emulation, threat modeling, etc)</mark> constrains and demands pose interesting challenges on opponent modeling?

* In the rise of <mark style="color:$primary;">agentic end point defense solutions</mark>, is it feasible to design and evaluate a prototype of defender agent? In practice, what do defenders want to predict about adversaries? what is the reality of data availability? &#x20;
* What is <mark style="color:$primary;">zero-day</mark>? Is the defense against zero-days a <mark style="color:$primary;">zero-shot</mark> or <mark style="color:$primary;">few-shot</mark> challenge?&#x20;
* Are there any exising opponent modeling approaches can help <mark style="color:$primary;">differentiate human vs AI adversaries</mark>? Is that something worthy to model and predict (i.e., is it strategically relevant)? What evidence / conjectures do we have so far about how humans and AI adversaries differ? If we manage to acquire such an opponent model, how do we <mark style="color:$primary;">design experiments to empirically demonstrate its benefits</mark> and relevance to network security?

When does the <mark style="color:$primary;">algorithmic making</mark> of an agent matter?&#x20;

* Do we need to care about whether an agent is rule-based, RL-based, or LLM-based, if their <mark style="color:$primary;">behavior</mark> are similar?  Are they truly similar or is it a matter of perspective, perception, and metric?&#x20;
* What <mark style="color:$primary;">algorithmic characteristics</mark> translate smoother to <mark style="color:$primary;">behavioral signals</mark>, and which tend to get lost?&#x20;
* Are there <mark style="color:$primary;">optical illusions between human and agents</mark>, analogous to Müller-Lyer Illusion, for ex, when there's actually important distinctions, only humans' subject perception cannot capture it, or vice versa?&#x20;
* [NeurIPS IAB](https://iab-agents.github.io/#about) ([Interprete Agent Behavior](http://arxiv.org/pdf/2605.13625)) : the field still lacks the <mark style="color:$primary;">vocabulary</mark>, <mark style="color:$primary;">methods</mark>, and <mark style="color:$primary;">tools</mark> to <mark style="color:$primary;">describe and analyze</mark> agent behavior <mark style="color:$primary;">at scale</mark>.

