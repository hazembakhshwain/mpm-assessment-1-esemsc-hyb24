import numpy as np
from acsefunctions import gamma
from scipy.special import gamma as scipy_gamma


def test_gamma_known_values():
    # Test known values
    assert np.isclose(gamma(1), 1.0), "gamma(1) should be 1"
    assert np.isclose(gamma(2), 1.0), "gamma(2) should be 1 (equivalent to 1!)"
    assert np.isclose(gamma(3), 2.0), "gamma(3) should be 2 (equivalent to 2!)"
    assert np.isclose(gamma(4), 6.0), "gamma(4) should be 6 (equivalent to 3!)"


def test_gamma_against_scipy():
    # Test against scipy's gamma function for a range of values
    x_values = np.array([0.5, 1.5, 2.5, 5.5])
    for x in x_values:
        assert np.isclose(
            gamma(x), scipy_gamma(x), rtol=1e-5
        ), f"gamma({x}) should match scipy's gamma({x})"


def test_gamma_small_values():
    # Test small values to check for precision
    x_small = np.array([1e-1, 1e-2])
    for x in x_small:
        assert np.isclose(
            gamma(x), scipy_gamma(x), rtol=1e-5
        ), f"gamma({x}) should match scipy's gamma({x})"
