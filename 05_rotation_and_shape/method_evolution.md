# Photometry, rotation and shape inference

## Inference chain

```text
calibrated photometry → reduced brightness and phase model → period search
    → spin-axis and shape inversion → validation against independent data
```

Each arrow has a different failure mode. A plausible period does not itself validate a pole or a shape model.

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
