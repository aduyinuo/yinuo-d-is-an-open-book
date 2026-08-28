---
icon: hexagon-nodes-bolt
---

# Many Trustworthy, Controllable, Causal Models for Operational Network Defense







## Three adjectives, three demands

The title carries three adjectives and each is a separate demand with a separate literature and a separate way of going wrong.

**Trustworthy** is a claim about what an operator can rely on, and not a claim that the model is accurate. The version I mean is already on the [Cyber World Modeling Next](../../3-year-agenda/cyber-world-modeling/next.md) page as a preference between two ways of being wrong: a model that fails honestly, wide and uncertain, over one that fails silently, sharp and wrong.

**Controllable** does two jobs at once. Inside [FOE-Dreamer](../../3-year-agenda/cyber-world-modeling/environment.md) it names the block of the latent state whose evolution is conditioned on the defender's own action. In the title it names a property of the deployed system, that a person can constrain what the defender does and can say afterwards why it did it.

**Causal** is the strongest of the three and the only one with an identifiability theory standing behind it. It is also the word my own [Learn Structure](../../3-year-agenda/cyber-world-modeling/strategic-structure.md) page lists as a contrast case, in the sentence saying what strategic dependence is not.

## The claim, and the null that competes with it

The thesis is that the failures of a world-model network defender are structured. They concentrate where the environment carries dependence types the world model cannot represent or learn, and they are therefore predictable in advance from a structural analysis of the environment. The null is that failure severity is explained by model bias alone, open-loop error growth over horizon, with no additional dependence on the type of structure in the environment.

Three experiments separate them. Train the learner on generator instances that differ only in planted dependence type and degree, and measure failure per type. Read model bias directly off open-loop prediction error at fixed horizons, which is the null's only explanatory variable. Then ask whether the type profile predicts which failure modes actually appear on the testbed at matched bias. The thesis predicts a type-ordered failure profile and the null predicts a flat one, and either result is publishable, which is the property that makes this a project rather than a mood.

Two planned outputs follow: a failure taxonomy for factored world models, and a drift detector whose success criterion is fixed in advance, that it fires before the attacker reaches the region the model is wrong about, at a false-alarm rate an operator will accept.

## What could take two adjectives away

The decision rule is written and it can end the project. Causal integration is supported only if it resolves a documented security-relevant failure more reliably than the four simpler alternatives, which are a language-model-only defender, a non-causal state tracker, a predictive world model, and a learned policy with rules extracted afterwards. If state tracking or rule extraction supplies the same benefit, the evidence supports that simpler architecture. And if nothing succeeds, the result identifies an unresolved problem without proving that causal modeling was the missing piece.

The vocabulary this needs before it can say any of that, including the four places my own pages already use one of these words in two ways, is on the [Lexicon](lexicon.md) page.

## Stewing...

