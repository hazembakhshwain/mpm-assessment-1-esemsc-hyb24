import numpy as np
from acsefunctions import exp

def test_exp_known_values():
    # Test known values
    assert np.isclose(exp(0), 1.0), "exp(0) should be 1"
    assert np.isclose(exp(1), np.e), "exp(1) should be approximately equal to e (~2.71828)"
    assert np.isclose(exp(-1), 1 / np.e), "exp(-1) should be approximately 1/e (~0.36788)"
    
def test_exp_against_numpy():
    # Test against numpy's exp function for a range of values
    x_values = np.array([-10, -1, 0, 1, 10, 20])
    for x in x_values:
        assert np.isclose(exp(x), np.exp(x)), f"exp({x}) should match numpy's exp({x})"

def test_exp_array_input():
    # Test array input
    x_array = np.array([0, 1, 2, 3])
    expected = np.exp(x_array)
    result = exp(x_array)
    assert np.allclose(result, expected), "exp(array) should match numpy's exp(array)"

def test_exp_large_values():
    # Test large values to ensure it handles them correctly
    x_large = np.array([20, 50, 100])
    expected = np.exp(x_large)
    result = exp(x_large)
    assert np.allclose(result, expected), "exp(large values) should match numpy's exp(large values)"

def test_exp_small_values():
    # Test small values to check for precision with values close to zero
    x_small = np.array([1e-10, -1e-10, 1e-15])
    expected = np.exp(x_small)
    result = exp(x_small)
    assert np.allclose(result, expected), "exp(small values) should match numpy's exp(small values)"

def test_exp_negative_values():
    # Test negative values
    x_negative = np.array([-1, -2, -5])
    expected = np.exp(x_negative)
    result = exp(x_negative)
    assert np.allclose(result, expected), "exp(negative values) should match numpy's exp(negative values)"
