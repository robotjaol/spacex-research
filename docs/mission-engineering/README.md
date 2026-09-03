# Mission engineering

Scope: orbital mechanics, launch windows, transfer orbits, rendezvous, payload deployment, mission optimization.

Specify epoch, frames, objectives and constraints before comparing propagation or mission tools.

## Evidence and source use

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [SpaceX Crew Dragon Completes First NASA Commercial Crew Flight Test](https://www.nasa.gov/wp-content/uploads/2015/05/spm_march_2019_web.pdf); [Revisiting Spacetrack Report#3](https://celestrak.org/publications/AIAA/2006-6753/AIAA-2006-6753-Rev3.pdf); [Astrodynamic Parameters](https://ssd.jpl.nasa.gov/astro_par.html).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Two-body orbit and synthetic constellation coverage](../../projects/03-orbit-coverage/README.md); [Launch trajectory transcription](../../projects/06-launch-trajectory/README.md); [Orbital rendezvous state-machine study](../../projects/16-rendezvous/README.md); [Launch-window geometry explorer](../../projects/22-launch-window/README.md).

## Missing evidence and next decision

The educational mission models do not establish executable flight plans, range clearance or collision-screening results.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
