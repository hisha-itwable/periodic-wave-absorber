# periodic-wave-absorber
Python-based simulation using MEEP for periodic wave absorption studies

## Overview
This repository contains simulation scripts for studying wave absorption in periodic structures using the MEEP (MIT Electromagnetic Equation Propagation) FDTD solver. The primary focus is on accurately modeling oblique wave incidence and minimizing artificial reflections from boundary layers.

## Key Features
- Periodic boundary conditions for infinite‑periodic structures
- Customizable PML (Perfectly Matched Layer) parameters optimized for grazing‑angle incidence
- Interior flux monitors for calculating total transmission and reflection
- Boundary‑layer meshing around monitoring planes for improved flux integration

## Recent Improvements
- **PML for grazing angles**: Updated PML profile uses a higher‑order polynomial grading (`m=4`) and increased thickness (`2.0`) to reduce reflections at incidence angles >75°.
- **Asymptotic reflection**: Set `R_asymptotic=1e‑9` to enforce low residual reflection.
- These changes address issue #15 where standard PML grading caused significant reflection contamination at oblique incidence.

## File Structure
- `main_simulation.py` – main simulation script with geometry, sources, and PML definition
- `utils/data_analysis.py` – post‑processing utilities for computing transmitted/reflected power
- `utils/mesh_generator.py` – mesh generation tools, including boundary‑layer meshes
- `results/baseline.dat` – example data from previous runs

## Usage
1. Install MEEP and its dependencies (see [MEEP documentation](https://meep.readthedocs.io)).
2. Run `python main_simulation.py` to execute the simulation.
3. Use the functions in `utils/data_analysis.py` to extract transmission/reflection coefficients.

## Contributing
Please open an issue or submit a pull request for any improvements or bug fixes. For major changes, discuss them first in an issue.

## License
[MIT](LICENSE)