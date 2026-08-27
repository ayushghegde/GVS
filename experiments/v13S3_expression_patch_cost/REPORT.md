# GVS v13S3 — Expression Patch Cost Sensitivity

**Verdict: MODEL PASS.** A common ECC base plus role-specific Expression Patches keeps the large duplication savings of v13R differentiation while tolerating substantial patch-interface overhead.

## Model
64-cell region, five optional role modules (`grammar`, `template`, `binding`, `constraint`, `exact`) and four General Reserve cells carrying all five patch options. Specialized counts reuse the v13R/v13S composition.

Module costs are independently swept log-uniformly from 0.25x to 8x one common ECC-body unit for 20,000 deterministic trials (seed 132).

## Results
- universal optional-module copies: **320**
- differentiated/patch copies: **60**
- copy reduction: **81.25%**
- mean total normalized hardware reduction: **73.38%**
- 5th percentile: **65.74%**
- median: **73.92%**
- 95th percentile: **78.97%**
- 5th-percentile interface headroom: **3.76 common-base cost units per installed patch** before the universal-cell baseline becomes cheaper.

## Decision
KEEP the common ECC base + Expression Patch strategy. Do not interpret the cost units as mm^2, dollars, or transistor counts; physical patch area/interface capacitance remains open. The result only shows the architecture is not fragile to moderate module-cost uncertainty.
