import numpy as np
from acsefunctions import sinh


def test_sinh_known_values():
    # Test known values
    assert np.isclose(sinh(0), 0.0), "sinh(0) should be 0"
    assert np.isclose(sinh(1), np.sinh(1)), "should match numpy's sinh(1)"
    assert np.isclose(sinh(-1), np.sinh(-1)), "should match numpy's sinh(-1)"


def test_sinh_against_numpy():
    # Test against numpy's sinh function for a range of small values
    x_values = np.array([-5, -2, -1, 0, 1, 2, 5])
    for x in x_values:
        assert np.isclose(
            sinh(x), np.sinh(x), rtol=1e-5
        ), f"sinh({x}) should match numpy's sinh({x})"


def test_sinh_array_input():
    # Test array input
    x_array = np.array([0, 1, 2, 3])
    expected = np.sinh(x_array)
    result = sinh(x_array)
    assert np.allclose(
        result, expected, rtol=1e-5
    ), "sinh(array) should match numpy's sinh(array)"


def test_sinh_small_values():
    # Test small values to check for precision with values close to zero
    x_small = np.array([1e-10, -1e-10, 1e-15])
    expected = np.sinh(x_small)
    result = sinh(x_small)
    assert np.allclose(
        result, expected, rtol=1e-10
    ), "sinh(small values) should match numpy's sinh(small values)"


def test_sinh_negative_values():
    # Test negative values (excluding large ones)
    x_negative = np.array([-1, -2, -5])
    expected = np.sinh(x_negative)
    result = sinh(x_negative)
    assert np.allclose(
        result, expected, rtol=1e-5
    ), "sinh(negative values) should match numpy's sinh(negative values)"
