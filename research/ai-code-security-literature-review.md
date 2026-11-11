# AI-generated code security: literature review

This is a separate academic strand about software built with AI coding assistants in general. No source found for this project says that any Sri Lankan government website was built with AI-generated code, and this review makes no such claim about any institution.

Status: first pass, 2026-11-11. Part A lists sources whose key statements were checked against the paper or its abstract in this session. Part B lists sources still to be read; nothing in Part B should be cited yet.

## Why the strand is here

Government sites are often built by small vendor teams under time pressure, and AI assistants are now common in such teams worldwide. If generated code is accepted without review, the weaknesses the literature describes are the same ones Sri Lanka CERT's guideline is meant to prevent: missing server-side validation, weak authentication, and unreviewed third-party components. The practical output of this strand is a set of review questions for anyone procuring or accepting a government website. It is not a detection method.

## Part A — Sources checked

### A1. Generated code often contains known weakness patterns

Pearce and colleagues prompted GitHub Copilot with 89 scenarios built around high-risk weakness classes, producing 1,689 programs, and found about 40 percent of them vulnerable ([Pearce et al., 2022](https://arxiv.org/abs/2108.09293)). The study measured an early version of one tool on scenarios chosen because they were risky, so the figure is not a general rate for all generated code.

- **Relevance:** injection and weak cryptography were among the classes studied, matching OWASP's long-standing categories.
- **Limit:** scenario design favours risky prompts; the tool has changed since 2021.

### A2. Developers with an assistant wrote less secure code and trusted it more

In a controlled user study, participants with access to an AI assistant produced insecure solutions more often than those without for most tasks, and were more likely to believe their code was secure ([Perry et al., 2023](https://arxiv.org/abs/2211.03622)). Participants who trusted the assistant less and worked more on their prompts produced fewer flaws.

- **Relevance:** the risk is partly human. Over-confidence reduces the review that would catch a flaw.
- **Limit:** a laboratory study with a limited participant pool and task set.

### A3. Assistants recommend software packages that do not exist

Spracklen and colleagues generated 576,000 code samples in Python and JavaScript using 16 models and analysed them for references to packages that do not exist, which they call package hallucinations; they describe this as a new form of package-confusion threat to the software supply chain and report that mitigation strategies reduced it ([Spracklen et al., 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)).

- **Relevance:** an attacker can register a commonly hallucinated name. A developer who installs it without checking brings hostile code into the build.
- **Limit:** the specific rates quoted in secondary summaries were not checked against the paper's tables in this session and are not repeated here.

### A4. Recognized risk catalogues

- OWASP Top 10 for web applications: the reference list of web risk classes used across this project ([OWASP, n.d.](https://owasp.org/Top10/)).
- OWASP Top 10 for Large Language Model Applications: risks of applications that *use* a language model, which is a different question from code *written by* one ([OWASP, n.d.](https://owasp.org/www-project-top-10-for-large-language-model-applications/)).

Neither catalogue was re-read in this session; they are cited for their existence and scope only.

## Risk patterns named in the research brief

The table sets out the eight patterns the project asked about and how far Part A supports each.

| Pattern | Support in Part A | Status |
| --- | --- | --- |
| Insecure code patterns in generated output | A1 | Supported for the scenarios studied |
| Authentication mistakes | None specific | Not yet sourced |
| Missing server-side validation | A1 covers injection classes generally | Partly supported; no source specific to validation placement |
| Insecure authorization design | None | Not yet sourced |
| Dependency vulnerabilities | A3 (non-existent packages) | Supported for hallucinated packages; outdated-version suggestions not yet sourced |
| Hardcoded secrets | None | Not yet sourced |
| Insecure API integrations | None | Not yet sourced |
| Insufficient security testing of generated code | A2 (over-confidence) | Indirectly supported |

Four of the eight patterns have no checked source yet. They remain hypotheses for this review until Part B is read.

## Part B — Sources to locate and read

These are recalled from general knowledge of the field and have not been opened in this session. Titles, venues and findings must be confirmed before use.

- [ ] Sandoval et al., a user study of security bugs with an AI assistant in C ("Lost at C"), USENIX Security 2023
- [ ] Khoury et al., an evaluation of the security of code generated by ChatGPT, 2023
- [ ] Fu et al., an empirical study of security weaknesses in Copilot-generated code found in public GitHub projects
- [ ] An industry measurement of security flaws in generated code across many models and languages (for example Veracode's report on generative AI code security)
- [ ] A study or industry report on secrets committed to public repositories and any link to assistant use
- [ ] OWASP guidance on secure use of AI coding assistants, if published
- [ ] Any study of authentication or authorization logic in generated web application code
- [ ] Any Sri Lankan or regional source on AI-assisted development in public-sector procurement

## Review questions for procurement and acceptance

These follow from Part A and from Sri Lanka CERT's guideline. They are questions an institution can put to a vendor; they are not findings.

1. Were AI coding assistants used, and is generated code reviewed by a second person before merge?
2. Is every input validated on the server, regardless of client-side checks?
3. Does every dependency exist in the official registry, with a pinned version and a recorded reason for inclusion?
4. Are secrets kept out of source code and checked for automatically before each commit?
5. Has authentication and per-object authorization been tested by someone other than the author?
6. Was a security assessment completed before release, as the national guideline requires?

## Rule for this project

A statement that a named institution used AI-generated code may appear in this repository only if the institution or its vendor has said so publicly, with the source cited and saved. Appearance, code style or the date a site was launched are not evidence.

## References

OWASP Foundation. (n.d.). *OWASP Top 10*. <https://owasp.org/Top10/>

OWASP Foundation. (n.d.). *OWASP Top 10 for Large Language Model Applications*. <https://owasp.org/www-project-top-10-for-large-language-model-applications/>

Pearce, H., Ahmad, B., Tan, B., Dolan-Gavitt, B., & Karri, R. (2022). Asleep at the keyboard? Assessing the security of GitHub Copilot's code contributions. *IEEE Symposium on Security and Privacy*. <https://arxiv.org/abs/2108.09293>

Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). Do users write more insecure code with AI assistants? *ACM Conference on Computer and Communications Security*. <https://arxiv.org/abs/2211.03622>

Spracklen, J., Wijewickrama, R., Sakib, A. H. M. N., Maiti, A., Viswanath, B., & Jadliwala, M. (2025). We have a package for you! A comprehensive analysis of package hallucinations by code generating LLMs. *34th USENIX Security Symposium*, 3687–3706. <https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen>

Sri Lanka CERT. (2022). *Website security guidelines for government organizations* (Version 1). <https://cert.gov.lk/wp-content/uploads/2023/07/Website-Security-Guidelines-for-Government-Organizations_2022.pdf>
