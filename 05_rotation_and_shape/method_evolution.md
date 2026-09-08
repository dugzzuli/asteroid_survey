# Photometry, rotation and shape inference

## Inference chain

```text
calibrated photometry → reduced brightness and phase model → period search
    → spin-axis and shape inversion → validation against independent data
```

Each arrow has a different failure mode. A plausible period does not itself validate a pole or a shape model.

## Four levels of inference

| Level | Typical result | What it does not establish |
|---|---|---|
| Period recovery | Rotation period \(P\) | Pole direction or a unique shape |
| Spin-state inference | \(P\) plus pole coordinates | Surface concavities or a detailed physical shape |
| Convex inversion | \(P\), pole, convex hull and scattering model | A unique non-convex body |
| Population-scale inversion | Screened distributions of spin, shape proxy and phase parameters | An unbiased population without a selection-function model |

## Dense versus sparse photometry

Dense lightcurves sample a rotation continuously for hours and are efficient for period and amplitude recovery. Sparse survey photometry sacrifices within-night coverage but can span many viewing and phase geometries. It can therefore constrain selected spin/shape solutions, provided that the time baseline, signal-to-noise ratio and geometry are adequate.

The two data modes must not be treated as interchangeable. Sparse inversion is an inference and selection problem, not merely a lower-cadence period search.

## Representative methods

| Family | Input | Output | Strength | Limitation | References |
|---|---|---|---|---|---|
| Dense-lightcurve inversion | Multi-apparition lightcurves | Period, pole, convex shape | Strong viewing-geometry leverage | Expensive dedicated observations | `KaasalainenTorppa2001`; `KaasalainenEtAl2001` |
| Sparse-survey inversion | Survey epoch photometry | Selected shape/spin solutions | Scales to large archives | Aliases and selective recoverability | `HanusDurech2013`; `DurechEtAl2016` |
| Joint period and phase fitting | Sparse single-opposition lightcurves | Period plus phase parameters | Uses survey data efficiently | Sampling and amplitude drive reliability | `WaszczakEtAl2015` |
| Multi-data inversion | Optical plus thermal lightcurves | Shape, spin, thermal model | Complementary constraints | Cross-survey calibration and geometry matter | `AliLagoaEtAl2018` |
| Gaia population inversion | Gaia sparse photometry | Screened spin states | Uniform astrometry/photometry and scale | Cadence aliases need external validation | `DurechHanus2018`; `DurechHanus2023` |
| Learned inversion | Lightcurves plus geometry | Predicted shape representation | Fast candidate generation after training | Domain transfer and uncertainty calibration unresolved | `TangEtAl2025` |

## Minimum reporting standard

For every period or inversion result, record the observing time span, number of points, phase-angle range, period-search range, alias treatment, photometric error model, and independent validation source. A final review should not compare model counts without these fields.

## Selection effect to carry into the final review

Low-amplitude, nearly spherical objects are harder to recover from sparse photometry than elongated, high-amplitude objects. Consequently, an observed inversion-model distribution is not automatically a shape distribution for the discovered population. The review should distinguish detection selection from inversion selection and require injection--recovery or an equivalent validation before population-level interpretation.
