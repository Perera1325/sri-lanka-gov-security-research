# LaTeX manuscript

`manuscript.tex` is an IEEE-conference-style version. It is **not** submitted or IEEE-approved.

## Compile
1. This uses the official `IEEEtran` document class, which is **not** bundled here. Use a TeX
   distribution that provides it (TeX Live, MiKTeX) or Overleaf, or place `IEEEtran.cls` beside
   `manuscript.tex`.
2. `pdflatex manuscript` → `bibtex manuscript` → `pdflatex manuscript` (twice).
3. The `.tex` references figures as `.pdf` (e.g. `fig1-incident-classification.pdf`). The
   repository ships `.png` versions in `../figures/`; convert them to PDF, or change the
   `\includegraphics` extensions to `.png`. Render `methodology-flowchart.md` (Mermaid) to
   `methodology-flowchart.pdf` first.

## Notes
- The in-`.tex` tables are compact stand-ins; port the full Markdown tables from `../tables/`
  and keep every number identical to the source data.
- `references.bib` holds the 13 verified references. No DOI was invented.
