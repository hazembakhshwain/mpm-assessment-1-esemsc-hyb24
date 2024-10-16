from acsefunctions import fact


def test_fact_known_values():
    # Test known values of the factorial function
    assert fact(0) == 1, "fact(0) should be 1"
    assert fact(1) == 1, "fact(1) should be 1"
    assert fact(5) == 120, "fact(5) should be 120"
    assert fact(10) == 3628800, "fact(10) should be 3628800"


def test_fact_against_large_input():
    # Test larger input to ensure performance (not too large to avoid overflow)
    assert fact(15) == 1307674368000, "fact(15) should be 1307674368000"
