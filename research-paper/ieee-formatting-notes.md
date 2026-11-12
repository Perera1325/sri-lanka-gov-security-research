# IEEE formatting notes

This draft is written in Markdown for review. To produce an IEEE-style PDF, use the LaTeX
version in [`latex/`](latex/).

## Honest status

- This paper is **not** peer reviewed, **not** submitted, and **not** approved by IEEE.
- No specific IEEE conference or journal is named as a destination; choose one only after the
  paper is complete and a co-author/supervisor has reviewed it.
- "IEEE-style" refers to structure and the LaTeX template only.

## Building the LaTeX version

1. The template uses the official `IEEEtran` document class. It is **not** included here;
   obtain `IEEEtran.cls` from IEEE or CTAN and place it beside `manuscript.tex`, or build on a
   TeX distribution (TeX Live / MiKTeX / Overleaf) that provides it.
2. Compile: `pdflatex manuscript` → `bibtex manuscript` → `pdflatex manuscript` ×2.
3. On Overleaf, upload `manuscript.tex` and `references.bib`, set the compiler to pdfLaTeX, and
   add the figure files from `../figures/`.

## Figures

- Figures 1–3 are PNGs in [`figures/`](figures/). For a camera-ready IEEE PDF, regenerate them
  as vector PDF/EPS for crisp print output.
- Figure 4 (methodology) is Mermaid source in `figures/methodology-flowchart.md`; render it to
  PNG or PDF (for example with the Mermaid CLI or a diagram tool) before including it.

## Tables

- The tables in [`tables/`](tables/) are Markdown generated from repository data. Port them to
  IEEE `table` environments in the LaTeX file; keep the numbers identical to the source.

## Before submission (not yet done)

- Add author affiliation, email and ORCID.
- Add a co-author/supervisor review.
- Convert figures to vector format.
- Run a plagiarism/similarity check (the draft paraphrases all sources; there are no long
  quotations).
