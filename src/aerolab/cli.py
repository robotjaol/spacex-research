"""Reproduce demonstrations and record numeric provenance; no network calls."""

import argparse
from dataclasses import asdict, replace
import json
from pathlib import Path
import platform
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy

from . import __version__
from .models import (LandingConfig, landing, navigation, orbit,
                     constellation_coverage, thermal, fault_injection)


def _csv(path, names, arrays):
    np.savetxt(path, np.column_stack(arrays), delimiter=",",
               header=",".join(names), comments="", fmt="%.12g")


def _figure(path, title, lines, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    for x, y, label in lines:
        ax.plot(x, y, label=label, linewidth=1.5)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.grid(alpha=.2)
    ax.legend(loc="best")
    fig.savefig(path, dpi=160)
    plt.close(fig)


def run_landing(out, seed):
    c = LandingConfig()
    data, summary = landing(c)
    ballistic, baseline = landing(c, controlled=False)
    _csv(out / "landing.csv", ["time_s", "height_m", "velocity_mps", "thrust_accel_mps2"], data.T)
    _figure(out / "landing.png", "Generic vertical descent | synthetic parameters",
            [(data[:, 0], data[:, 1], "PD feedback"),
             (ballistic[:, 0], ballistic[:, 1], "Unpowered baseline")], "Time (s)", "Height (m)")
    rng = np.random.default_rng(seed)
    trials = []
    for _ in range(50):
        cc = replace(c, height_m=rng.uniform(80, 120), velocity_mps=rng.uniform(-15, -5),
                     max_thrust_accel_mps2=rng.uniform(16, 20))
        _, m = landing(cc)
        trials.append((cc.height_m, cc.velocity_mps, cc.max_thrust_accel_mps2,
                       m["contact"], m["contact_velocity_mps"] if m["contact"] else np.nan))
    _csv(out / "landing_trials.csv", ["height_m", "initial_velocity_mps", "max_accel_mps2",
                                     "contact", "contact_velocity_mps"], np.array(trials).T)
    passed = sum(bool(r[3]) and abs(r[4]) < 1 for r in trials)
    fine, _ = landing(replace(c, dt_s=c.dt_s/2))
    return {"parameters": asdict(c), **summary, "unpowered_baseline": baseline,
            "sampled_success_count": passed, "sampled_trial_count": len(trials),
            "success_definition": "contact within 90 s and abs(contact velocity) < 1 m/s",
            "dt_halving_contact_speed_difference_mps": float(abs(data[-1,2]-fine[-1,2])),
            "scope": "Constant mass; ideal actuator; no drag, fuel, attitude, or sensor noise"}


def run_navigation(out, seed):
    d = navigation(seed)
    t, truth, est = d["time_s"], d["truth"], d["estimate"]
    _csv(out / "navigation.csv", ["time_s", "true_position_m", "measurement_m",
                                  "estimated_position_m", "estimated_velocity_mps", "position_sigma_m"],
         [t, truth[:,0], d["observation_m"], est[:,0], est[:,1], np.sqrt(d["covariance"][:,0,0])])
    _figure(out / "navigation.png", "Kalman position error | synthetic observation outage 40–50 s",
            [(t, d["observation_m"]-truth[:,0], "Measurement error"),
             (t, est[:,0]-truth[:,0], "Filter error"),
             (t, 2*np.sqrt(d["covariance"][:,0,0]), "+2 posterior sigma")],
            "Time (s)", "Position error (m)")
    records = []
    for s in range(seed, seed+30):
        q = navigation(s)
        available = np.isfinite(q["observation_m"]) & (q["time_s"] >= 10)
        err = q["estimate"][:,0]-q["truth"][:,0]
        rmse = float(np.sqrt(np.mean(err[available]**2)))
        raw = float(np.sqrt(np.mean((q["observation_m"][available]-q["truth"][available,0])**2)))
        records.append((s, rmse, raw))
    _csv(out / "navigation_trials.csv", ["seed", "filter_rmse_m", "measurement_rmse_m"], np.array(records).T)
    return {"trial_count": len(records), "mean_filter_rmse_m": float(np.mean(np.array(records)[:,1])),
            "mean_measurement_rmse_m": float(np.mean(np.array(records)[:,2])),
            "evaluation_mask": "t >= 10 s and observation available; same timestamps for both errors",
            "single_run_outage_rmse_m": float(np.sqrt(np.mean((est[(t>=40)&(t<50),0]-truth[(t>=40)&(t<50),0])**2))),
            "scope": "Matched synthetic process/noise model; no IMU bias or real GNSS data"}


def run_orbit(out, seed):
    d, cov = orbit(), constellation_coverage()
    t, state = d["time_s"], d["state"]
    _csv(out / "orbit.csv", ["time_s", "x_m", "y_m", "z_m", "vx_mps", "vy_mps", "vz_mps", "analytic_error_m"],
         [t, *state.T, d["position_error_m"]])
    _csv(out / "coverage.csv", ["time_s", "visible_satellites"], [cov["time_s"], cov["visible_count"]])
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), layout="constrained")
    axes[0].plot(state[:,0]/1e3, state[:,1]/1e3)
    axes[0].set(xlabel="Inertial x (km)", ylabel="Inertial y (km)", title="Two-body circular orbit")
    axes[0].axis("equal")
    axes[1].plot(cov["time_s"]/3600, cov["visible_count"])
    axes[1].set(xlabel="Synthetic elapsed time (h)", ylabel="Visible satellites", title="72 synthetic satellites | 25° mask")
    for ax in axes:
        ax.grid(alpha=.2)
    fig.savefig(out / "orbit.png", dpi=160)
    plt.close(fig)
    return {"period_s": d["period_s"],
            "max_relative_energy_drift": float(np.max(np.abs(d["energy_j_per_kg"]/d["energy_j_per_kg"][0]-1))),
            "max_relative_angular_momentum_drift": float(np.max(np.abs(d["momentum_m2_per_s"]/d["momentum_m2_per_s"][0]-1))),
            "max_analytic_position_error_m": float(d["position_error_m"].max()),
            "sampled_visibility_fraction": cov["sampled_visibility_fraction"],
            "station_deg": [-7.25,112.75], "constellation": "6 planes x 12 satellites; 550 km; inclination 53 deg",
            "scope": "Synthetic constellation, simplified frames; visibility does not imply Starlink service"}


def run_thermal(out, seed):
    d = thermal()
    _csv(out / "thermal.csv", ["time_s", "temperature_k", "analytic_temperature_k", "heat_flow_w"],
         [d["time_s"], d["temperature_k"], d["analytic_k"], d["heat_flow_w"]])
    _figure(out / "thermal.png", "Lumped sensible heating | abstract cryogenic thermal body",
            [(d["time_s"]/3600, d["temperature_k"], "Numerical"),
             (d["time_s"]/3600, d["analytic_k"], "Analytic")], "Time (h)", "Temperature (K)")
    return {"max_analytic_error_k": float(np.max(np.abs(d["temperature_k"]-d["analytic_k"]))),
            "stored_energy_j": d["stored_energy_j"], "integrated_heat_j": d["integrated_heat_j"],
            "relative_energy_balance_error": abs(d["integrated_heat_j"]-d["stored_energy_j"])/d["stored_energy_j"],
            "final_temperature_k": float(d["temperature_k"][-1]),
            "scope": "Constant effective thermal capacity and conductance; no actual tank or fluid properties"}


def run_avionics(out, seed):
    d = fault_injection(seed)
    _csv(out / "avionics.csv", ["time_s", "truth", "sensor_1", "sensor_2", "sensor_3", "estimate", "mode"],
         [d["time_s"], d["truth"], *d["sensors"].T, d["estimate"], d["mode"]])
    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=True, layout="constrained")
    for i in range(3):
        axes[0].plot(d["time_s"], d["sensors"][:,i], alpha=.55, label=f"Sensor {i+1}")
    axes[0].plot(d["time_s"], d["estimate"], color="black", label="Voted estimate")
    axes[0].set(ylabel="Synthetic sensor units", title="Fault injection | SAFE is latched until explicit reset")
    axes[0].legend(ncol=2)
    axes[1].step(d["time_s"], d["mode"], where="post")
    axes[1].set(xlabel="Time (s)", ylabel="Mode", yticks=[0,1,2], yticklabels=["NOMINAL","DEGRADED","SAFE"])
    fig.savefig(out / "avionics.png", dpi=160)
    plt.close(fig)
    safe = d["mode"] == 2
    return {"samples": len(safe), "safe_samples": int(safe.sum()),
            "safe_estimates_are_unavailable": bool(np.all(np.isnan(d["estimate"][safe]))),
            "fault_schedule_s": {"one_biased_sensor": [15,30], "three_disagreeing": [30,40],
                                 "manual_reset": 45, "missing_sensor": [50,55]},
            "scope": "Scripted software experiment; no scheduling, radiation, bus, or hardware validation"}


RUNNERS = {"landing": run_landing, "navigation": run_navigation, "orbit": run_orbit,
           "thermal": run_thermal, "avionics": run_avionics}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", choices=["all", *RUNNERS])
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    if args.seed < 0:
        parser.error("seed must be nonnegative")
    args.output.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    report = {"version": __version__, "seed": args.seed,
              "environment": {"python": platform.python_version(), "platform": platform.platform(),
                              "numpy": np.__version__, "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
              "evidence_class": "educational approximation; synthetic inputs", "projects": {}}
    names = list(RUNNERS) if args.project == "all" else [args.project]
    for name in names:
        report["projects"][name] = RUNNERS[name](args.output, args.seed)
    report["wall_time_s"] = time.perf_counter()-start
    destination = args.output / ("results.json" if args.project == "all" else f"{args.project}_results.json")
    destination.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(f"Wrote {len(names)} experiment(s) to {args.output}; metrics: {destination}")


if __name__ == "__main__":
    main()
