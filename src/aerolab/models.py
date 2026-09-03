"""Small, inspectable models with SI units and explicit assumptions.

The equations are documented in projects/. All vehicle and sensor inputs are
synthetic educational choices. Earth constants are attributed in references/.
"""

from dataclasses import dataclass
from enum import IntEnum

import numpy as np
from scipy.integrate import solve_ivp

EARTH_MU = 398600.435507e9  # m^3/s^2, JPL DE440, references/D01
EARTH_RADIUS = 6371.0084e3  # m, mean radius, JPL, references/D02
SIDEREAL_DAY = 86164.09054  # s, JPL, references/D01


def _positive(*values):
    if not all(np.isfinite(v) and v > 0 for v in values):
        raise ValueError("Expected positive finite inputs")


def _finite(*values):
    if not all(np.isfinite(v) for v in values):
        raise ValueError("Expected finite inputs")


@dataclass(frozen=True)
class LandingConfig:
    height_m: float = 100.0
    velocity_mps: float = -10.0
    gravity_mps2: float = 9.80665
    max_thrust_accel_mps2: float = 18.0
    kp_per_s2: float = 0.12
    kd_per_s: float = 0.70
    target_height_m: float = -0.50
    dt_s: float = 0.02
    horizon_s: float = 90.0


def landing(config=LandingConfig(), controlled=True):
    """Sampled PD, constant mass, vertical axis, zero-order-held acceleration.

    Contact truncates a ballistic segment at its exact quadratic root. The
    pre-contact velocity is returned, never overwritten with zero. The virtual
    setpoint is below the surface to obtain contact instead of asymptotic hover.
    This is not an engine ignition, guidance, or real landing-leg model.
    """
    c = config
    _positive(c.height_m, c.gravity_mps2, c.max_thrust_accel_mps2,
              c.kp_per_s2, c.kd_per_s, c.dt_s, c.horizon_s)
    _finite(c.velocity_mps, c.target_height_m)
    t, h, v = 0.0, c.height_m, c.velocity_mps
    rows = []
    touched = False
    while t < c.horizon_s - 1e-12:
        thrust = float(np.clip(c.gravity_mps2 + c.kp_per_s2 *
                              (c.target_height_m - h) - c.kd_per_s * v,
                              0, c.max_thrust_accel_mps2)) if controlled else 0.0
        rows.append((t, h, v, thrust))
        a = thrust - c.gravity_mps2
        dt = min(c.dt_s, c.horizon_s - t)
        hn = h + v * dt + 0.5 * a * dt**2
        # Detect downward crossing even if a long segment would rise again.
        roots = np.roots([0.5 * a, v, h]) if abs(a) > 1e-12 else (
            np.array([-h / v]) if v < 0 else np.array([]))
        contact = [float(x.real) for x in roots if abs(x.imag) < 1e-9
                   and 0 < x.real <= dt and v + a * x.real < 0]
        if contact:
            tau = min(contact)
            t, h, v = t + tau, 0.0, v + a * tau
            touched = True
            rows.append((t, h, v, thrust))
            break
        t, h, v = t + dt, hn, v + a * dt
    if not touched:
        rows.append((t, h, v, thrust))
    return np.array(rows), {"contact": touched, "time_s": t,
                           "contact_velocity_mps": v if touched else None}


def navigation(seed=7, dt=0.2, duration=100.0, measurement_sigma=5.0,
               process_accel_sigma=0.10, dropout=(40.0, 50.0)):
    """Position/velocity Kalman filter with known acceleration input.

    Piecewise independent acceleration noise has covariance sigma_a^2 G G^T.
    The filter only reads noisy positions, known commands, and its prior.
    Joseph covariance update preserves symmetry and numerical stability.
    """
    _positive(dt, duration, measurement_sigma, process_accel_sigma)
    if duration < dt:
        raise ValueError("duration must be at least dt")
    if len(dropout) != 2 or not 0 <= dropout[0] <= dropout[1]:
        raise ValueError("dropout must be an ordered nonnegative interval")
    rng = np.random.default_rng(seed)
    t = np.arange(int(duration / dt) + 1) * dt
    F = np.array([[1.0, dt], [0.0, 1.0]])
    G = np.array([0.5 * dt**2, dt])
    H = np.array([[1.0, 0.0]])
    Q = process_accel_sigma**2 * np.outer(G, G)
    R = measurement_sigma**2
    truth = np.zeros((len(t), 2))
    truth[0] = [100.0, 2.0]
    commands = 0.3 * np.sin(0.15 * t)
    for k in range(1, len(t)):
        truth[k] = F @ truth[k-1] + G * (
            commands[k-1] + rng.normal(0, process_accel_sigma))
    z = truth[:, 0] + rng.normal(0, measurement_sigma, len(t))
    z[(t >= dropout[0]) & (t < dropout[1])] = np.nan
    if not np.isfinite(z[0]):
        raise ValueError("The first observation is required for initialization")
    x = np.array([z[0], 0.0])
    P = np.diag([R, 25.0])
    est, covariance = np.zeros_like(truth), np.zeros((len(t), 2, 2))
    est[0], covariance[0] = x, P
    for k in range(1, len(t)):
        x, P = F @ x + G * commands[k-1], F @ P @ F.T + Q
        if np.isfinite(z[k]):
            gain = (P @ H.T) / float((H @ P @ H.T)[0, 0] + R)
            x = x + gain[:, 0] * (z[k] - float((H @ x)[0]))
            A = np.eye(2) - gain @ H
            P = A @ P @ A.T + gain @ gain.T * R
        P = (P + P.T) / 2
        est[k], covariance[k] = x, P
    return {"time_s": t, "truth": truth, "observation_m": z,
            "estimate": est, "covariance": covariance}


def orbit(altitude_m=550e3, revolutions=2.0, samples=1201, rtol=1e-10):
    """Cartesian two-body circular orbit, inertial frame; no TLE inputs."""
    _positive(altitude_m, revolutions, rtol)
    if samples < 3 or int(samples) != samples:
        raise ValueError("samples must be an integer >= 3")
    radius = EARTH_RADIUS + altitude_m
    speed = np.sqrt(EARTH_MU / radius)
    period = 2 * np.pi * np.sqrt(radius**3 / EARTH_MU)
    initial = np.array([radius, 0, 0, 0, speed, 0])

    def rhs(t, state):
        r = state[:3]
        return np.r_[state[3:], -EARTH_MU * r / np.linalg.norm(r)**3]

    t = np.linspace(0, period * revolutions, samples)
    sol = solve_ivp(rhs, (0, t[-1]), initial, t_eval=t, method="DOP853",
                    rtol=rtol, atol=np.array([1e-4]*3 + [1e-7]*3))
    if not sol.success:
        raise RuntimeError(sol.message)
    state = sol.y.T
    radius_t = np.linalg.norm(state[:, :3], axis=1)
    energy = np.sum(state[:, 3:]**2, axis=1) / 2 - EARTH_MU / radius_t
    momentum = np.linalg.norm(np.cross(state[:, :3], state[:, 3:]), axis=1)
    phase = 2 * np.pi * t / period
    analytic = radius * np.c_[np.cos(phase), np.sin(phase), np.zeros(len(t))]
    return {"time_s": t, "state": state, "period_s": period,
            "energy_j_per_kg": energy, "momentum_m2_per_s": momentum,
            "position_error_m": np.linalg.norm(state[:, :3] - analytic, axis=1)}


def elevation_deg(satellite_ecef, ground_ecef):
    """Spherical-local elevation from Earth-fixed vectors in the same units."""
    satellite = np.asarray(satellite_ecef, dtype=float)
    ground = np.asarray(ground_ecef, dtype=float)
    if ground.shape != (3,) or satellite.shape[-1:] != (3,):
        raise ValueError("Expected ground (3,) and satellite (...,3) vectors")
    if not np.all(np.isfinite(ground)) or not np.all(np.isfinite(satellite)):
        raise ValueError("Coordinates must be finite")
    _positive(np.linalg.norm(ground))
    los = satellite-ground
    distance = np.linalg.norm(los, axis=-1)
    if np.any(distance <= 0):
        raise ValueError("Satellite and station must be distinct")
    sine = (los @ (ground/np.linalg.norm(ground))) / distance
    return np.rad2deg(np.arcsin(np.clip(sine,-1,1)))


def constellation_coverage(planes=6, satellites_per_plane=12, altitude_m=550e3,
                           inclination_deg=53.0, min_elevation_deg=25.0,
                           latitude_deg=-7.25, longitude_deg=112.75):
    """Synthetic circular constellation; local visibility, not network service.

    Sampling is every 60 s for one sidereal day. ECI-to-ECEF uses a constant
    Earth rotation rate and a chosen zero rotation phase, not an actual epoch.
    """
    _positive(altitude_m)
    if any(int(v) != v or v < 1 for v in (planes, satellites_per_plane)):
        raise ValueError("Plane and satellite counts must be positive integers")
    _finite(inclination_deg, min_elevation_deg, latitude_deg, longitude_deg)
    if not 0 <= inclination_deg <= 180 or not 0 <= min_elevation_deg <= 90:
        raise ValueError("Invalid inclination or elevation")
    if not -90 <= latitude_deg <= 90 or not -180 <= longitude_deg <= 180:
        raise ValueError("Invalid station coordinates")
    radius = EARTH_RADIUS + altitude_m
    n = np.sqrt(EARTH_MU / radius**3)
    t = np.arange(0.0, SIDEREAL_DAY, 60.0)
    lat, lon, inc = np.deg2rad([latitude_deg, longitude_deg, inclination_deg])
    up = np.array([np.cos(lat)*np.cos(lon), np.cos(lat)*np.sin(lon), np.sin(lat)])
    ground = EARTH_RADIUS * up
    visible = np.zeros(len(t), dtype=int)
    rotation = 2*np.pi*t/SIDEREAL_DAY
    cr, sr = np.cos(rotation), np.sin(rotation)
    for p in range(planes):
        raan = 2*np.pi*p/planes
        for s in range(satellites_per_plane):
            u = n*t + 2*np.pi*s/satellites_per_plane + 2*np.pi*p/(planes*satellites_per_plane)
            x = radius*(np.cos(raan)*np.cos(u) - np.sin(raan)*np.sin(u)*np.cos(inc))
            y = radius*(np.sin(raan)*np.cos(u) + np.cos(raan)*np.sin(u)*np.cos(inc))
            z = radius*np.sin(u)*np.sin(inc)
            ecef = np.c_[cr*x+sr*y, -sr*x+cr*y, z]
            visible += elevation_deg(ecef, ground) >= min_elevation_deg
    return {"time_s": t, "visible_count": visible,
            "sampled_visibility_fraction": float(np.mean(visible > 0))}


def thermal(initial_k=90.0, ambient_k=120.0, capacity_j_per_k=2e5,
            conductance_w_per_k=5.0, duration_s=7200.0):
    """Single lump sensible heating: C dT/dt = UA (T_ambient - T).

    Inputs define an abstract thermal body initially at a cryogenic temperature.
    They are not fluid properties. No pressure, phase change, or boiloff model.
    """
    _positive(initial_k, ambient_k, capacity_j_per_k, conductance_w_per_k, duration_s)
    t = np.linspace(0, duration_s, 301)
    sol = solve_ivp(lambda _, y: conductance_w_per_k*(ambient_k-y)/capacity_j_per_k,
                    (0, duration_s), [initial_k], t_eval=t, rtol=1e-10, atol=1e-10)
    if not sol.success:
        raise RuntimeError(sol.message)
    T = sol.y[0]
    exact = ambient_k+(initial_k-ambient_k)*np.exp(-conductance_w_per_k*t/capacity_j_per_k)
    flux = conductance_w_per_k*(ambient_k-T)
    integrated = np.trapezoid(flux, t)
    stored = capacity_j_per_k*(T[-1]-T[0])
    return {"time_s": t, "temperature_k": T, "analytic_k": exact,
            "heat_flow_w": flux, "stored_energy_j": stored,
            "integrated_heat_j": float(integrated)}


class Mode(IntEnum):
    NOMINAL = 0
    DEGRADED = 1
    SAFE = 2


def vote(sensors, max_spread=2.0):
    """Require three fresh values and an agreeing pair. SAFE has no estimate.

    A median can tolerate one arbitrary outlier under the independent-fault
    assumption. Two agreeing bad sensors can defeat it. Missing data fails closed.
    """
    _positive(max_spread)
    values = np.asarray(sensors, dtype=float)
    if values.shape != (3,):
        raise ValueError("Exactly three readings are required")
    if not np.all(np.isfinite(values)):
        return np.nan, Mode.SAFE
    ordered = np.sort(values)
    if ordered[-1]-ordered[0] <= max_spread:
        return float(ordered[1]), Mode.NOMINAL
    if np.min(np.diff(ordered)) <= max_spread:
        return float(ordered[1]), Mode.DEGRADED
    return np.nan, Mode.SAFE


def fault_injection(seed=7):
    """Scripted synthetic faults, a latched SAFE state, and explicit reset."""
    rng = np.random.default_rng(seed)
    t = np.arange(0, 60, 0.1)
    truth = 20+2*np.sin(t/10)
    sensors = truth[:, None] + rng.normal(0, 0.2, (len(t), 3))
    sensors[(t >= 15) & (t < 30), 0] += 10
    sensors[(t >= 30) & (t < 40)] += np.array([-10, 0, 10])
    sensors[(t >= 50) & (t < 55), 0] = np.nan
    modes, estimates, latch = [], [], False
    for k, reading in enumerate(sensors):
        value, mode = vote(reading)
        if mode == Mode.SAFE:
            latch = True
        if k == 450 and mode == Mode.NOMINAL:  # explicit reset request at 45 s
            latch = False
        modes.append(int(Mode.SAFE if latch else mode))
        estimates.append(np.nan if latch else value)
    return {"time_s": t, "truth": truth, "sensors": sensors,
            "estimate": np.asarray(estimates), "mode": np.asarray(modes)}
