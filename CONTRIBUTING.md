# Curation guide

## One paper, one structured record

Use a stable `ID` and never silently overwrite a record. Prefer DOI; add ADS and arXiv identifiers where available. Use semicolons for multiple values inside a CSV field, quote fields containing commas, and use `unknown` instead of guessing.

## Required analytical fields

For each paper, fill `Main_question`, `Method`, `Innovation`, and `Limitation` in plain, comparative language. A limitation can be a stated assumption, selection effect, scale constraint, reproducibility gap, or untested regime.

## Topic notes

Topic files synthesize across papers. They should state the evolving problem, compare approaches, record evidence gaps, and use cite keys from `references.bib`. Do not duplicate a paper's abstract.
