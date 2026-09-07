# Review architecture v2

The database now follows four connected scientific blocks. Existing technical directories remain in place during curation; the mapping below prevents duplicate coverage while a later, clean migration can rename directories in one reviewable commit.

| Block | Primary question | Current and planned locations |
|---|---|---|
| Observation and discovery | How do survey images become linked orbits? | `01_surveys`, `02_detection`, `03_linking_and_orbits`, `09_machine_learning` |
| Physical characterisation | How do photons become spin, shape, taxonomy, size, and surface properties? | `04_photometry`, `05_rotation_and_shape`, `06_physical_properties`, `07_taxonomy`, `07_thermal_properties` |
| Dynamics and evolution | How do collisions, families, and thermal forces reshape populations? | `10_asteroid_families`, `11_yarkovsky_yorp`, `12_NEO_and_population` |
| Internal structure and formation | What do mass, density, and multiple systems reveal? | `08_mass_density_internal_structure`, `09_binary_multiple_systems` |

Space missions and next-generation facilities are cross-cutting validation and outlook chapters: `15_space_missions` and `16_future_surveys`.

## Chapter rule

Each synthesis must follow: **science question → observational evidence → methodology → major findings → unresolved problems**. A facility or algorithm belongs in a chapter only insofar as it changes the evidence or the answer.

## Core causal chain

```text
Collisions → families → Yarkovsky/YORP drift → resonances → NEO population
```

```text
Dense lightcurves → convex inversion → sparse survey photometry → Gaia population-scale inversion
```
