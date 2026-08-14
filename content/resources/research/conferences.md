# Conferences

Venue fit is a property of the pair — the paper and the track — not of the paper alone. And an increasing amount of what decides a paper's fate happens before review begins, in the registration metadata.

## Where an ML-for-security paper belongs

**Source: [USENIX Security '26 call for papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers), "Submitting ML Work"; mirrored by the [CCS 2026 CfP](https://www.sigsac.org/ccs/CCS2026/call-for/call-for-papers.html).**

Mark the paper's primary field as **the field of the problem you are solving**, not the technique you solved it with. A novel ML method for intrusion detection is a Network Security paper, not a Security-and-Privacy-of-ML paper.

The worked examples are the fastest way to calibrate:

<table><thead><tr><th width="330">Paper</th><th>Track</th></tr></thead><tbody><tr><td>ML for phishing website detection</td><td>Web Security</td></tr><tr><td>ML for vulnerability detection</td><td>Software Security</td></tr><tr><td>LLMs for penetration testing</td><td>Systems Security</td></tr><tr><td>Website fingerprinting</td><td>Privacy and Anonymity</td></tr><tr><td>Prompt injection against LLMs</td><td>Security of ML — the vulnerability itself is an ML vulnerability</td></tr></tbody></table>

Two consequences worth internalizing. **Robustness alone is not a security contribution** — work that mainly improves ML functionality or efficiency, including robustness to noise or spurious artifacts, is out of scope. If that's the framing, reframe around an adversary: who, what surface, how general, how practical. And **the Security-of-ML track expects an explicit threat model** with those same four parts; if you believe your paper belongs there without one, the justification statement is where you have to say why.

## What the registration metadata is actually for

**Source: [ACM CCS 2026 Between-Cycle Transparency Report](https://github.com/ACM-CCS-2026/Transparency-Report), Véronique Cortier and Zhiqiang Lin, 20 April 2026.**

The chairs are explicit that title, abstract, track and track justification "are used operationally for reviewer assignment and conflict handling." Assignment ran through an AI-assisted matcher generating roughly twenty candidate papers per PC member for bidding, built from submitted abstracts and PC members' own representative publications.

So the 200 words are not a note to reviewers. They are input to a routing system, read by a track chair deciding who should bid. Write in the vocabulary the PC members of your intended track use to describe their own work — not in generic ML language, which will match nobody.

Metadata drift is policed: roughly eighty papers were manually reviewed for abstract divergence in Cycle A, and from Cycle B the abstract field becomes read-only after registration. Whatever you register is the paper.

**The compliance numbers are the real lesson.** Of 1,206 submissions, 225 were desk-rejected. The causes:

<table><thead><tr><th width="380">Reason</th><th>Share of desk rejects</th></tr></thead><tbody><tr><td>Missing or empty Open Science artifact</td><td>54.2%</td></tr><tr><td>Format violations</td><td>26.2%</td></tr><tr><td>Hallucinated or invalid references</td><td>18.2%</td></tr><tr><td>Anonymity violation</td><td>8.4%</td></tr><tr><td>Missing ethics section</td><td>5.8%</td></tr></tbody></table>

88.4% of them were flagged for a **single** reason. Nobody lost a paper on a close judgment call about scope; they lost it on one avoidable omission. Two categories deserve naming: the Open Science appendix is still being treated as boilerplate by a majority of the authors who fell over, and hallucinated references are now a real desk-reject category that did not meaningfully exist before.

Also worth knowing: about half of all submissions had at least one missing conflict of interest, which the chairs read as ordinary memory failure at scale rather than gaming.

## Drafting the justification

Consolidating the above:

1. Open with the **security primitive** the paper attacks or defends, in the vocabulary of the intended track. Name the technique in the second sentence, not the first.
2. Anchor to the track's existing work — an analogous accepted paper, or at minimum the sub-area. The matcher and the bidders are anchored on representative publications.
3. Name the most plausible alternative track and say why it isn't the better fit. The CfP asks for this in both directions.
4. If there's an adversary in the loop, put the threat model in the 200 words even for a domain track — one sentence: attacker, surface, generality, practicality.
5. Treat it as a compliance artifact. Empty or boilerplate justifications are flagged; rambling ones compete with twenty other candidate papers for one PC member's attention.

_Last updated: 2026-08_
