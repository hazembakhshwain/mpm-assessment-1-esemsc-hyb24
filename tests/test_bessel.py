import numpy as np
from acsefunctions import bessel
from scipy.special import jv as scipy_jv


def test_bessel_known_values():
    # Test known values for order alpha = 0
    assert np.isclose(bessel(0, 0), 1.0), "J_0(0) should be 1"
    assert np.isclose(
        bessel(0, 1), scipy_jv(0, 1)
    ), "J_0(1) should match scipy's J_0(1)"
    assert np.isclose(
        bessel(0, 2), scipy_jv(0, 2)
    ), "J_0(2) should match scipy's J_0(2)"


def test_bessel_against_scipy():
    # Test against scipy's Bessel function for a range of values
    alpha_values = [0, 1, 2]
    x_values = np.array([0.5, 1, 2, 3])
    for alpha in alpha_values:
        for x in x_values:
            assert np.isclose(
                bessel(alpha, x), scipy_jv(alpha, x), rtol=1e-5
            ), f"J_{alpha}({x}) should match scipy's J_{alpha}({x})"


def test_bessel_array_input():
    # Test array input for Bessel function
    x_array = np.array([0, 1, 2])
    alpha = 1
    expected = scipy_jv(alpha, x_array)
    result = bessel(alpha, x_array)
    assert np.allclose(
        result, expected, rtol=1e-5
    ), f"J_{alpha}(array) should match scipy's J_{alpha}(array)"


def test_bessel_small_values():
    # Test small x values to check precision with x close to zero for a = 0
    x_small = np.array([1e-1, 1e-2])
    alpha = 0
    for x in x_small:
        assert np.isclose(
            bessel(alpha, x), scipy_jv(alpha, x), rtol=1e-5
        ), f"J_{alpha}({x}) should match scipy's J_{alpha}({x})"
