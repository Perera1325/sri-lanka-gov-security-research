# AI-generated code security: literature review

The research literature shows that code produced by AI assistants often contains known weakness patterns, and that human review is the control that matters. Results on whether assistants make developers' finished code less secure are mixed.

This review concerns software development in general. Section 8 states what it does and does not say about Sri Lankan government websites: no source found for this project says that any of them was built with AI-generated code.

Status: third pass, 2026-11-12: title, authors, year, venue and DOI or proceedings page confirmed for all eight papers. Second pass, 2026-11-11. Eight papers are included. For each, the stated findings were checked in this session against the paper's abstract, its publisher or conference page, or the paper text. Full texts were not read end to end, and figures should be re-checked against the published version before being quoted.

## 1. Sources and how they were checked

| Ref | Study | Venue | Type of evidence | Checked against |
| --- | --- | --- | --- | --- |
| P1 | Pearce et al., *Asleep at the Keyboard?* | IEEE S&P 2022 | Generated code analysed in designed scenarios | Paper abstract and CACM research highlight |
| P2 | Perry et al., *Do Users Write More Insecure Code with AI Assistants?* | ACM CCS 2023 | Controlled user study | arXiv abstract |
| P3 | Sandoval et al., *Lost at C* | USENIX Security 2023 | Controlled user study | USENIX page and arXiv abstract |
| P4 | Fu et al., *Security Weaknesses of Copilot-Generated Code in GitHub Projects* | ACM TOSEM 2025 | Generated code found in public repositories | arXiv abstract, latest version |
| P5 | Vero et al., *BaxBench* | ICML 2025 | Benchmark with functional tests and exploits | arXiv abstract and conference page |
| P6 | Spracklen et al., *We Have a Package for You!* | USENIX Security 2025 | Large-scale generation experiment | arXiv abstract and USENIX page |
| P7 | Huang et al., *Your Code Secret Belongs to Me* | ACM FSE 2024 | Extraction experiment on code completion tools | arXiv abstract |
| P8 | Klemmer et al., *Using AI Assistants in Software Development* | ACM CCS 2024 | Interviews and forum analysis | arXiv abstract and institutional record |

Full references are at the end.

## 2. LLM-generated insecure code

Three studies measure weaknesses in generated code directly, in increasingly realistic settings.

- **Designed scenarios.** P1 prompted GitHub Copilot with 89 scenarios built around high-risk weakness classes, producing 1,689 programs, of which about 40 percent were found vulnerable ([Pearce et al., 2022](https://arxiv.org/abs/2108.09293)).
- **Code in real projects.** P4 collected 733 code snippets attributed to Copilot and two other tools from public GitHub projects. It reports security weaknesses in 29.5 percent of the Python snippets and 24.2 percent of the JavaScript snippets, across 43 weakness categories, some of which are in the 2023 CWE Top 25 ([Fu et al., 2025](https://arxiv.org/abs/2310.02059)).
- **Whole application back ends.** P5 asked models to build complete back-end applications over 392 tasks and then ran functional tests and real exploits. The best model reached 62 percent on correctness, and exploits succeeded on around half of the programs that were functionally correct ([Vero et al., 2025](https://arxiv.org/abs/2502.11844)).

**Limits.** P1 chose scenarios because they were risky, so its figure is not a general rate. P4 depends on developers having labelled code as generated and on static analysis tools. P5 measures unaided generation, which is not how most teams work. Tools change quickly, and each figure belongs to the tool versions tested.

## 3. Authentication flaws

No checked source isolates authentication code as its subject. The nearest evidence is indirect.

- P5's scenarios are web back ends exposed to untrusted users, and its conference summary gives a login module as an example scenario. Its finding that about half of functionally correct programs could be exploited therefore covers the kind of code where authentication lives, without separating it out ([Vero et al., 2025](https://arxiv.org/abs/2502.11844)).
- P4 found insufficiently random values to be the most frequent weakness category in generated code in real projects ([Fu et al., 2025](https://arxiv.org/abs/2310.02059)). Weak randomness matters for session identifiers and tokens, though the paper does not tie its count to authentication specifically.

**Status:** partly supported. A study aimed specifically at generated authentication and authorization logic is still to be found.

## 4. Input validation mistakes

- P4 lists code injection and cross-site scripting among the significant weakness categories in generated code found in real projects ([Fu et al., 2025](https://arxiv.org/abs/2310.02059)). Both arise when input is used without adequate validation or encoding.
- P1 examined how the wording of a prompt changed the likelihood of SQL-injection-prone output ([Pearce et al., 2022](https://arxiv.org/abs/2108.09293)).
- P2 included a SQL injection task among its five tasks; across the study, assisted participants wrote insecure solutions more often on four of the five tasks ([Perry et al., 2023](https://arxiv.org/abs/2211.03622)). The per-task result for the SQL task should be checked in the full paper before it is quoted on its own.

**Limit.** None of these studies measures whether validation was placed on the server as well as the client, which is what Sri Lanka CERT's guidelines require.

## 5. Dependency and secret-handling risks

- **Non-existent packages.** P6 generated 576,000 code samples in Python and JavaScript with 16 models and analysed references to packages that do not exist. The authors describe this as a new form of package-confusion threat to the software supply chain, and show that mitigation strategies reduce it ([Spracklen et al., 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)).
- **Memorized credentials.** P7 showed that code completion tools can reproduce hard-coded credentials from their training data, and identified two valid credentials during its experiments ([Huang et al., 2024](https://arxiv.org/abs/2309.07639)).
- **Hard-coded credentials in output.** P4's weakness table includes use of hard-coded credentials among the categories found, at a low frequency ([Fu et al., 2025](https://arxiv.org/abs/2310.02059)).

**Limit.** No checked source measures how often assistants suggest real but outdated or vulnerable package versions.

## 6. Security review limitations

- **Over-confidence.** In P2, participants with an assistant were more likely to believe their code was secure while producing insecure solutions more often on most tasks ([Perry et al., 2023](https://arxiv.org/abs/2211.03622)). Confidence that outruns correctness reduces the review that would catch a flaw.
- **Automated repair is partial.** P4 gave the assistant the static-analysis warnings for its own code and found it could fix up to 55.5 percent of the issues, with success varying by weakness type ([Fu et al., 2025](https://arxiv.org/abs/2310.02059)).
- **Functional tests miss security.** In P5, programs that passed functional tests were still exploitable about half the time ([Vero et al., 2025](https://arxiv.org/abs/2502.11844)). Passing tests is not evidence of security.

## 7. Human verification of AI-generated code

The evidence on human oversight points both ways, and both results should be reported.

- **Oversight can be sufficient.** P3 studied 58 student programmers writing low-level C code and found that the assisted group produced critical security bugs at a rate no more than 10 percent higher than the control group. The authors conclude that, in their setting, assistance did not introduce new security risks ([Sandoval et al., 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/sandoval)).
- **Oversight can fail.** P2, with different tasks and languages, found assisted participants wrote less secure code. Participants who trusted the assistant less and worked more on their prompts produced fewer flaws ([Perry et al., 2023](https://arxiv.org/abs/2211.03622)).
- **What professionals report doing.** P8 interviewed 27 software professionals and reviewed 190 relevant Reddit posts and comments. Despite security and quality concerns, participants used assistants widely, including for security-critical tasks; their general mistrust led them to check suggestions in much the same way as human-written code ([Klemmer et al., 2024](https://arxiv.org/abs/2405.06371)).

**Reading these together.** P2 and P3 differ in language, task and participants, so they do not contradict each other; they show that the outcome depends on the setting and on how critically the developer works. The consistent message is that review by a person who does not simply trust the output is the control that matters.

## 8. What this does and does not say about government websites

This section is deliberately separate from the research summary above.

**What the literature supports**

- AI coding assistants are a general software-engineering risk factor wherever generated code is accepted without independent review.
- The weakness classes involved are the ones Sri Lanka CERT's guidelines already target: input validation, credential handling, third-party components and assessment before release. See the [web application guideline mapping](cert-web-application-guideline-mapping.md).

**What it does not support**

- That any Sri Lankan government website was built with AI-generated code. No source found for this project says so.
- That any incident in the [timeline](../reports/historical-incident-timeline.md) had anything to do with AI-generated code. Where a cause was reported at all, it concerned maintenance and assessment.
- Any way of telling from outside whether a site was generated by AI.

**Rule for this project.** A site's appearance, layout, code style, launch date or vendor is never evidence of how it was written. A statement that a named institution used AI-generated code may appear in this repository only if the institution or its vendor has said so publicly, with the source cited and saved.

## 9. Coverage of the topics requested

| Topic | Sources | State |
| --- | --- | --- |
| LLM-generated insecure code | P1, P4, P5 | Supported |
| AI-assisted authentication flaws | P5, P4 (indirect) | Partly supported; no dedicated study found |
| Input validation mistakes | P1, P2, P4 | Supported for injection classes; server-side placement not studied |
| Dependency vulnerabilities | P6; P7 and P4 for credentials | Supported for hallucinated packages; outdated versions not sourced |
| Security review limitations | P2, P4, P5 | Supported |
| Human verification of generated code | P2, P3, P8 | Supported, with mixed results reported |

## 10. Still to find

- [ ] A study focused on authentication and authorization logic in generated web application code
- [ ] A study of outdated or vulnerable dependency versions suggested by assistants
- [ ] A study of server-side versus client-side validation in generated web code
- [ ] Any Sri Lankan or regional source on AI-assisted development in public-sector software procurement
- [ ] OWASP guidance on secure use of AI coding assistants, if published

## 11. Review questions for procurement and acceptance

These follow from the literature and from Sri Lanka CERT's guidelines. They are questions an institution can put to a vendor. They are not findings.

1. Were AI coding assistants used, and is generated code reviewed by a second person before merge?
2. Is every input validated on the server, regardless of client-side checks?
3. Does every dependency exist in the official registry, with a pinned version and a recorded reason for inclusion?
4. Are secrets kept out of source code and checked for automatically before each commit?
5. Has authentication and per-object authorization been tested by someone other than the author?
6. Was security tested separately from functional testing, and was a Sri Lanka CERT assessment completed before release?

## References

Fu, Y., Liang, P., Tahir, A., Li, Z., Shahin, M., Yu, J., & Chen, J. (2025). Security weaknesses of Copilot-generated code in GitHub projects: An empirical study. *ACM Transactions on Software Engineering and Methodology*. https://doi.org/10.1145/3716848 (preprint: <https://arxiv.org/abs/2310.02059>)

Huang, Y., Li, Y., Wu, W., Zhang, J., & Lyu, M. R. (2024). Your code secret belongs to me: Neural code completion tools can memorize hard-coded credentials. *Proceedings of the ACM on Software Engineering, 1*(FSE), Article 111. https://doi.org/10.1145/3660818

Klemmer, J. H., Horstmann, S. A., Patnaik, N., Ludden, C., Burton, C., Jr., Powers, C., Massacci, F., Rahman, A., Votipka, D., Lipford, H. R., Rashid, A., Naiakshina, A., & Fahl, S. (2024). Using AI assistants in software development: A qualitative study on security practices and concerns. *Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security*, 2726–2740. https://doi.org/10.1145/3658644.3690283

Pearce, H., Ahmad, B., Tan, B., Dolan-Gavitt, B., & Karri, R. (2022). Asleep at the keyboard? Assessing the security of GitHub Copilot's code contributions. *2022 IEEE Symposium on Security and Privacy (SP)*, 754–768. https://doi.org/10.1109/SP46214.2022.9833571

Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). Do users write more insecure code with AI assistants? *Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security*, 2785–2799. https://doi.org/10.1145/3576915.3623157

Sandoval, G., Pearce, H., Nys, T., Karri, R., Garg, S., & Dolan-Gavitt, B. (2023). Lost at C: A user study on the security implications of large language model code assistants. *32nd USENIX Security Symposium*, 2205–2222. <https://www.usenix.org/conference/usenixsecurity23/presentation/sandoval>

Spracklen, J., Wijewickrama, R., Sakib, A. H. M. N., Maiti, A., Viswanath, B., & Jadliwala, M. (2025). We have a package for you! A comprehensive analysis of package hallucinations by code generating LLMs. *34th USENIX Security Symposium*, 3687–3706. <https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen>

Sri Lanka CERT. (2022). *Web application security guidelines for government organizations* (Version 1). <https://cert.gov.lk/wp-content/uploads/2023/07/Web-Application-Security-Guidelines-for-Government-Organizations_2022.pdf>

Vero, M., Mündler, N., Chibotaru, V., Raychev, V., Baader, M., Jovanović, N., He, J., & Vechev, M. (2025). BaxBench: Can LLMs generate correct and secure backends? *Proceedings of the 42nd International Conference on Machine Learning*, PMLR 267, 61344–61390. <https://proceedings.mlr.press/v267/vero25a.html>
