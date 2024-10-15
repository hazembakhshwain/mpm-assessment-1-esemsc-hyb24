import numpy as np
from acsefunctions import cosh

def test_cosh_known_values():
    # Test known values
    assert np.isclose(cosh(0), 1.0), "cosh(0) should be 1"
    assert np.isclose(cosh(1), np.cosh(1)), "cosh(1) should match numpy's cosh(1)"
    assert np.isclose(cosh(-1), np.cosh(-1)), "cosh(-1) should match numpy's cosh(-1)"

def test_cosh_against_numpy():
    # Test against numpy's cosh function for a range of small to moderate values
    x_values = np.array([-5, -2, -1, 0, 1, 2, 5])
    for x in x_values:
        assert np.isclose(cosh(x), np.cosh(x), rtol=1e-5), f"cosh({x}) should match numpy's cosh({x})"

def test_cosh_array_input():
    # Test array input
    x_array = np.array([0, 1, 2, 3])
    expected = np.cosh(x_array)
    result = cosh(x_array)
    assert np.allclose(result, expected, rtol=1e-5), "cosh(array) should match numpy's cosh(array)"

def test_cosh_small_values():
    # Test small values to check for precision with values close to zero
    x_small = np.array([1e-10, -1e-10, 1e-15])
    expected = np.cosh(x_small)
    result = cosh(x_small)
    assert np.allclose(result, expected, rtol=1e-10), "cosh(small values) should match numpy's cosh(small values)"

def test_cosh_negative_values():
    # Test negative values (excluding large ones)
    x_negative = np.array([-1, -2, -5])
    expected = np.cosh(x_negative)
    result = cosh(x_negative)
    assert np.allclose(result, expected, rtol=1e-5), "cosh(negative values) should match numpy's cosh(negative values)"