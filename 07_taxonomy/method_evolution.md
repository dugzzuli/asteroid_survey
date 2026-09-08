# Spectroscopy, colours, taxonomy and composition

## Inference boundary

```text
reflectance spectrum → spectral features → taxonomic class → mineralogical interpretation → composition
```

A taxonomic label is a reproducible grouping of observables. It is not a unique mineralogical composition: grain size, space weathering, surface texture and incomplete wavelength coverage can produce degeneracy.

## Method evolution

| Era | Data and method | Advance | Limitation | References |
|---|---|---|---|---|
| 2002 | SMASS CCD spectra and Bus classes | Homogeneous visible taxonomy | Missing full NIR diagnostic bands | `BusBinzel2002a`; `BusBinzel2002b` |
| 2009 | Bus--DeMeo VIS--NIR taxonomy | Extends classes to 0.45--2.45 µm | Targeted, relatively small sample | `DeMeoEtAl2009` |
| 2013 | SDSS multiband taxonomy with bias correction | Population-scale composition proxies | Broadband colour degeneracy | `DeMeoCarry2013` |
| 2022 | Spectra plus albedo, probabilistic assignment | Retains uncertainty and helps resolve X-complex degeneracy | Model/training-sample dependence | `MahlkeCarryMattei2022` |
| 2023--26 | Gaia reflectance spectra and quality-selected taxonomy | Homogeneous survey-scale spectral samples | Artifacts and quality cuts reduce the usable sample | `GaiaGalluccioEtAl2023`; `TinautRuanoEtAl2026` |
| 2023 onward | Meteorite-supervised ML | Maps spectra toward mineralogical analogues | Domain transfer is not direct ground truth | `DyarEtAl2023` |

## Survey comparison rule

Always report wavelength range, spectral resolution or filter set, albedo use, quality cuts, class scheme, and whether output is a hard label or a probability. Population fractions should specify whether they are number-, area-, volume-, or mass-weighted.
