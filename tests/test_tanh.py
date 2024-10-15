import numpy as np
from acsefunctions import tanh

def test_tanh_known_values():
    # Test known values
    assert np.isclose(tanh(0), 0.0), "tanh(0) should be 0"
    assert np.isclose(tanh(1), np.tanh(1)), "tanh(1) should match numpy's tanh(1)"
    assert np.isclose(tanh(-1), np.tanh(-1)), "tanh(-1) should match numpy's tanh(-1)"

def test_tanh_against_numpy():
    # Test against numpy's tanh function for a range of small to moderate values
    x_values = np.array([-5, -2, -1, 0, 1, 2, 5])
    for x in x_values:
        assert np.isclose(tanh(x), np.tanh(x), rtol=1e-5), f"tanh({x}) should match numpy's tanh({x})"

def test_tanh_array_input():
    # Test array input
    x_array = np.array([0, 1, 2, 3])
    expected = np.tanh(x_array)
    result = tanh(x_array)
    assert np.allclose(result, expected, rtol=1e-5), "tanh(array) should match numpy's tanh(array)"

def test_tanh_small_values():
    # Test small values to check for precision with values close to zero
    x_small = np.array([1e-10, -1e-10, 1e-15])
    expected = np.tanh(x_small)
    result = tanh(x_small)
    assert np.allclose(result, expected, rtol=1e-10), "tanh(small values) should match numpy's tanh(small values)"

def test_tanh_negative_values():
    # Test negative values (excluding large ones)
    x_negative = np.array([-1, -2, -5])
    expected = np.tanh(x_negative)
    result = tanh(x_negative)
    assert np.allclose(result, expected, rtol=1e-5), "tanh(negative values) should match numpy's tanh(negative values)"