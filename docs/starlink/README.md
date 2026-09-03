# Starlink

Scope: constellations, orbital mechanics, inter-satellite links, phased arrays, networking, routing, constellation optimization, ground stations.

Connect orbit geometry to visibility, then link scheduling and packet behavior. Regulatory authorization is a separate layer.

## Evidence and source use

[Antenna modules for phased array antennas, US11018436B2](https://patents.google.com/patent/US11018436B2/en); [SpaceX NGSO Satellite System: Authorization and Order, DA 26-36](https://docs.fcc.gov/public/attachments/DA-26-36A1.pdf); [Brightness Mitigation Best Practices for Satellite Operators](https://starlink.com/public-files/BrightnessMitigationBestPracticesSatelliteOperators.pdf); [Mini Specifications](https://starlink.com/public-files/specification_sheet_mini.pdf); [Exploring the Internet from space with Hypatia](https://bdebopam.github.io/papers/imc2020-hypatia.pdf); [Revisiting Spacetrack Report#3](https://celestrak.org/publications/AIAA/2006-6753/AIAA-2006-6753-Rev3.pdf).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Two-body orbit and synthetic constellation coverage](../../projects/03-orbit-coverage/README.md); [Inter-satellite routing experiment](../../projects/15-isl-routing/README.md); [Phased-array beam pattern explorer](../../projects/19-array-pattern/README.md).

## Missing evidence and next decision

Synthetic geometry is not current deployed fleet data or an internet service-quality estimate.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
