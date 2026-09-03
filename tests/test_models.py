"""Numerical checks against independent analytic solutions and failure cases."""

from dataclasses import replace
import unittest
import numpy as np

from aerolab.models import (LandingConfig, landing, navigation, orbit, thermal, elevation_deg,
                           vote, Mode, fault_injection, constellation_coverage)


class LandingTests(unittest.TestCase):
    def test_free_fall_contact_matches_closed_form(self):
        c = LandingConfig(velocity_mps=-3.0, dt_s=.13)
        d, m = landing(c, controlled=False)
        expected_v = -np.sqrt(c.velocity_mps**2 + 2*c.gravity_mps2*c.height_m)
        expected_t = (c.velocity_mps-expected_v)/c.gravity_mps2
        self.assertAlmostEqual(m["time_s"], expected_t, places=10)
        self.assertAlmostEqual(d[-1,2], expected_v, places=9)

    def test_nominal_contact_and_refinement(self):
        c = LandingConfig()
        coarse, m = landing(c)
        fine, _ = landing(replace(c, dt_s=.01))
        self.assertTrue(m["contact"])
        self.assertLess(abs(coarse[-1,2]), 1)
        self.assertLess(abs(coarse[-1,2]-fine[-1,2]), .02)
        self.assertEqual(coarse[-1,1], 0)

    def test_invalid_or_unfinished_run_is_explicit(self):
        with self.assertRaises(ValueError):
            landing(LandingConfig(dt_s=0))
        _, m = landing(LandingConfig(horizon_s=.1))
        self.assertFalse(m["contact"])
        self.assertIsNone(m["contact_velocity_mps"])


class NavigationTests(unittest.TestCase):
    def test_covariance_remains_psd_and_outage_increases_uncertainty(self):
        d = navigation()
        self.assertGreaterEqual(np.linalg.eigvalsh(d["covariance"]).min(), -1e-10)
        t, P = d["time_s"], d["covariance"]
        i, j = np.searchsorted(t, [40,49.8])
        self.assertGreater(P[j,0,0], P[i,0,0])
        self.assertTrue(np.all(np.isnan(d["observation_m"][i:j+1])))

    def test_matched_trials_improve_position_rmse(self):
        filtered, raw = [], []
        for seed in range(7,17):
            d = navigation(seed)
            mask = np.isfinite(d["observation_m"]) & (d["time_s"] >= 10)
            filtered.append(np.mean((d["estimate"][mask,0]-d["truth"][mask,0])**2))
            raw.append(np.mean((d["observation_m"][mask]-d["truth"][mask,0])**2))
        self.assertLess(np.mean(filtered), np.mean(raw))


class OrbitTests(unittest.TestCase):
    def test_independent_elevation_cases(self):
        ground = np.array([10.,0.,0.])
        self.assertAlmostEqual(elevation_deg([11,0,0],ground), 90)
        self.assertAlmostEqual(elevation_deg([10,2,0],ground), 0)
        self.assertLess(elevation_deg([-11,0,0],ground), 0)
        with self.assertRaises(ValueError):
            elevation_deg(ground,ground)

    def test_circular_solution_and_invariants(self):
        d = orbit()
        self.assertLess(d["position_error_m"].max(), 1)
        for field in ["energy_j_per_kg", "momentum_m2_per_s"]:
            self.assertLess(np.max(np.abs(d[field]/d[field][0]-1)), 1e-8)

    def test_lower_elevation_mask_never_reduces_visibility(self):
        a = constellation_coverage(min_elevation_deg=0)
        b = constellation_coverage(min_elevation_deg=25)
        self.assertTrue(np.all(a["visible_count"] >= b["visible_count"]))
        self.assertTrue(np.all(b["visible_count"] <= 72))
        with self.assertRaises(ValueError):
            constellation_coverage(latitude_deg=100)


class ThermalTests(unittest.TestCase):
    def test_analytic_solution_and_energy_balance(self):
        d = thermal()
        self.assertLess(np.max(np.abs(d["temperature_k"]-d["analytic_k"])), 1e-6)
        self.assertLess(abs(d["integrated_heat_j"]/d["stored_energy_j"]-1), 1e-5)
        self.assertTrue(np.all(np.diff(d["temperature_k"]) > 0))

    def test_equilibrium_and_cooling(self):
        eq = thermal(initial_k=100, ambient_k=100)
        self.assertTrue(np.all(eq["temperature_k"] == 100))
        cool = thermal(initial_k=110, ambient_k=90)
        self.assertLess(cool["stored_energy_j"], 0)
        self.assertTrue(np.all(np.diff(cool["temperature_k"]) < 0))


class AvionicsTests(unittest.TestCase):
    def test_single_fault_and_missing_data(self):
        estimate, mode = vote([10,10.1,100])
        self.assertEqual(mode, Mode.DEGRADED)
        self.assertLess(abs(estimate-10), .2)
        for values in ([0,10,20], [10,np.nan,10]):
            estimate, mode = vote(values)
            self.assertEqual(mode, Mode.SAFE)
            self.assertTrue(np.isnan(estimate))

    def test_common_mode_is_an_exposed_limitation(self):
        estimate, mode = vote([100,100.1,100.2])
        self.assertEqual(mode, Mode.NOMINAL)
        self.assertGreater(abs(estimate-10), 80)

    def test_safe_latch_requires_reset_and_blocks_outputs(self):
        d = fault_injection()
        t, modes = d["time_s"], d["mode"]
        self.assertTrue(np.all(modes[(t>=30)&(t<45)] == Mode.SAFE))
        self.assertTrue(np.all(modes[(t>=45)&(t<50)] == Mode.NOMINAL))
        self.assertTrue(np.all(modes[t>=50] == Mode.SAFE))
        self.assertTrue(np.all(np.isnan(d["estimate"][modes==Mode.SAFE])))


if __name__ == "__main__":
    unittest.main()
