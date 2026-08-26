---
icon: question
---

# How to choose venue for AI4Security papers

[_**USENIX Security**_](https://www.usenix.org/conference/usenixsecurity26/call-for-papers)  _**&**&#x20;_&#x20;[_**CCS**_](https://www.sigsac.org/ccs/CCS2026/call-for/call-for-papers.html)

Mark the paper's primary field as **the field of the problem you are solving**, not the technique you solved it with. A novel ML method for intrusion detection is a Network Security paper, not a Security-and-Privacy-of-ML paper.

The worked examples are the fastest way to calibrate:

<table><thead><tr><th width="330">Paper</th><th>Track</th></tr></thead><tbody><tr><td>ML for phishing website detection</td><td>Web Security</td></tr><tr><td>ML for vulnerability detection</td><td>Software Security</td></tr><tr><td>LLMs for penetration testing</td><td>Systems Security</td></tr><tr><td>Website fingerprinting</td><td>Privacy and Anonymity</td></tr><tr><td>Prompt injection against LLMs</td><td>Security of ML — the vulnerability itself is an ML vulnerability</td></tr></tbody></table>

**Work that mainly improves ML functionality or efficiency, including robustness to noise or spurious artifacts, is out of scope**. If that's the framing, reframe around an adversary: who, what surface, how general, how practical. And **the Security-of-ML track expects an explicit threat model** with those same four parts; if you believe your paper belongs there without one, the justification statement is where you have to say why.
