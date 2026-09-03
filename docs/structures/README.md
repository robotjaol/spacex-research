# Structures and materials

Scope: stainless steel, composites, cryogenic tanks, structural optimization, FEA, buckling, thermal stress.

Begin with analytic beam/plate benchmarks, then add geometric and temperature-dependent complexity.

## Evidence and source use

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [Final Tiered Environmental Assessment: Starship/Super Heavy Increased Cadence at Boca Chica](https://www.faa.gov/media/94346); [2.080 Structural Mechanics Lecture4: Development of Constitutive Equations of Continuum, Beams and Plates](https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/32670f14cec210d98c5c7fe9dbf73eb6_MIT2_080JF13_Lecture4.pdf).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Analytic-to-FEA structural benchmark](../../projects/13-structural-benchmark/README.md); [Manufacturing tolerance propagation](../../projects/20-manufacturing-variation/README.md).

## Missing evidence and next decision

An attractive CAD assembly or converged mesh does not establish structural margins or flight qualification.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
