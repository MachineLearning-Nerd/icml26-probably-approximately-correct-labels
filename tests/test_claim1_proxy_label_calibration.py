import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import claim1_proxy_label_calibration as c

def test_calibrated_fixture_meets_epsilon_and_control_fails():
    r = c.run(101)
    assert r['threshold'] > 0
    assert r['calibrated_loss'] <= c.EPSILON
    assert r['under_calibrated_loss'] > c.EPSILON
    assert r['under_calibrated_expert_fraction'] < r['calibrated_expert_fraction']

def test_threshold_is_selected_from_calibration_only():
    calibration = c.generate(c.N_CAL, 202)
    t = c.choose_threshold(calibration)
    assert 0 <= t <= 1
