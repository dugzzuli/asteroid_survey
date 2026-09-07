# Detection, linking and orbit determination

## Scope and terminology

This chapter separates three questions that are often conflated.

| Task | Question | Input | Output |
|---|---|---|---|
| Discovery linking | Which observations belong to one moving object? | Detections or tracklets | Candidate associations |
| Orbit determination | Which trajectory best explains those observations? | Astrometry and times | Orbit plus uncertainty/posterior |
| Attribution | Does a new short arc belong to an already known orbit? | New arc and orbit catalogue | Accepted/rejected association |

## Method evolution

| Era | Representative method | Main change | Key references |
|---|---|---|---|
| 2001 onward | Statistical ranging and admissible-region methods | Treat unknown range and range rate probabilistically for short arcs | `VirtanenMuinonenBowell2001`; `MilaniSansaturioChesley2001` |
| 2007 onward | kd-tree and tracklet pipelines | Make intra- and inter-night association computationally tractable | `KubicaEtAl2007`; `DenneauEtAl2013` |
| 2015 onward | Systematic ranging for impact monitoring | Scan the poorly constrained range dimensions to quantify near-term impact probability | `FarnocchiaChesleyMicheli2015`; `SpotoEtAl2018` |
| 2018 onward | Heliocentric transformation | Cluster tracklets after propagation to a common heliocentric epoch | `HolmanEtAl2018` |
| 2021 onward | Tracklet-less discovery | Test-orbit transformations enable multi-epoch clustering without an intra-night tracklet requirement | `MoeyensEtAl2021` |
| 2022 onward | ML-assisted candidate detection | Improve faint fast-streak candidate generation and filtering | `WangGeWillis2022`; `DuevEtAl2019` |
| 2025 onward | Non-linear digital tracking | Coadd sparse observations along orbit-curved paths using HPC | `GolovichEtAl2025` |

## Review structure

1. Source detection and stationary-source rejection.
2. Candidate filtering, including streak morphology and ML/DL.
3. Same-night tracklet formation.
4. Inter-night linking: kd-trees, MOPS, and heliocentric transformations.
5. Tracklet-less discovery with THOR.
6. Initial orbit determination: statistical ranging, systematic ranging, and admissible regions.
7. Orbit refinement and attribution.
8. Impact monitoring, with 2014 AA as a short case study.
9. Emerging survey-scale methods: non-linear digital tracking and Rubin-era compute requirements.

## Comparison rule for the final survey table

Compare methods only at stated completeness, purity, cadence, astrometric-error model, population, and compute budget. A discovery count is not by itself a like-for-like measure of linking performance.

## Curation note

The proposed Milani et al. (2012) item, *Innovative Observing Strategy and Orbit Determination for Low Earth Orbit Space Debris*, is excluded from this asteroid-focused register. It concerns space debris rather than asteroid/NEO discovery.
