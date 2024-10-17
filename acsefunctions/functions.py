"""
This module contains mathematical functions.

functions include such as factorial, exp, sinh, cosh, and tanh.
"""

import numpy as np
from functools import cache


@cache
def _scalar_fact(n):
    if n == 0 or n == 1:
        return 1
    return n * _scalar_fact(n - 1)


def fact(x):
    """Calculate the factorial of a non-negative integer or NumPyarray.

    Parameters
    ----------
    x : int or np.ndarray
        The non-negative integer or array of integers for which the factorial
        is computed.

    Returns
    -------
    int or np.ndarray
        The factorial of x (x!) if x is a scalar, or an array of factorials
        if x is a NumPy array.

    Examples
    --------
    >>> fact(5)
    120

    >>> fact(np.array([0, 1, 2, 3, 4]))
    array([ 1,  1,  2,  6, 24])

    Notes
    -----
    Uses recursion and caching (@cache) for efficiency in scalar calculations.
    For NumPy arrays, the function is vectorized to handle each element.
    """
    if np.isscalar(x):
        return _scalar_fact(x)
    else:
        vectorized_fact = np.vectorize(_scalar_fact)
        return vectorized_fact(x)


def exp(x, N=100):
    """Compute the exponential of x using the truncated Taylor series.

    This function approximates the value of e^x using a truncated Taylor series
    up to N terms. It supports scalar and array inputs, computing the result
    element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute e^x.
        Can be a scalar or a NumPy array.
    N : int, optional
        The number of terms in the Taylor series to use for the approximation
        (default is 100).
        Higher values increase accuracy but also increase computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of e^x as a NumPy array.
        If the input is scalar, a scalar value is returned;
        otherwise, an array of the same shape as the input.

    Examples
    --------
    >>> exp(1)
    2.718281828459045

    >>> exp(np.array([1, 2, 3]))
    array([ 2.71828183,  7.3890561 , 20.08553692])

    Notes
    -----
    - The calculation is performed using NumPy's
     vectorized operations to support both scalar and array inputs efficiently.
    - The function incrementally computes each term in the series using the
      previous term,
      which helps minimize the risk of overflow and maximizes efficiency.
    """
    x = np.asarray(x, dtype=np.float64)  # Ensure input is a NumPy array
    result = np.ones_like(x, dtype=np.float64)  # Initialize result with ones
    term = np.ones_like(x, dtype=np.float64)  # Start with x^0 / 0! = 1

    # For large x, break down x into x/2 to avoid overflow
    large_mask = np.abs(x) > 50  # Threshold based on observed issues
    x_large = x[large_mask] / 2
    x[large_mask] = x_large

    for n in range(1, N + 1):
        term *= x / n
        result += term

    # Square the result for large values (e^(x/2) -> (e^(x/2))^2)
    result[large_mask] = result[large_mask] ** 2

    # Handle extremely large values directly as inf
    result[np.abs(x) > 80] = np.inf

    return result


def sinh(x, N=10):
    """Compute the hyperbolic sine of x using the truncated Taylor series.

    This function approximates the value of sinh(x)
    using a truncated Taylor series
    up to N terms. It supports scalar and array inputs, computing the result
    element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute sinh(x). Can be a scalar or a
        NumPy array.
    N : int, optional
        The number of terms in the Taylor series to use for the approximation
        (default is 100). Higher values increase accuracy but also increase
        computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of sinh(x) as a NumPy array.
        If the input is scalar,
        a scalar value is returned; otherwise,
        an array of the same shape as the input.

    Examples
    --------
    >>> sinh(0)
    0.0

    >>> sinh(1)
    1.1752011936438014

    >>> sinh(np.array([1, 2, 3]))
    array([ 1.17520119,  3.62686041, 10.01787493])

    Notes
    -----
    - The calculation is performed using NumPy's vectorized operations to
    support
      both scalar and array inputs efficiently.
    - The function incrementally computes each term in the series using the
    previous
      power of x, which helps minimize computational overhead.
    """
    x = np.array(x, dtype=float)  # Convert input to a NumPy array for vect
    result = np.zeros_like(x)
    px = x.copy()

    for n in range(N + 1):
        result += px / fact(2 * n + 1)
        px *= x**2

    return result


def cosh(x, N=10):
    """Compute the hyperbolic cosine of x using the truncated Taylor series.

    This function approximates the value of cosh(x) using a
    truncated Taylor series
    up to N terms. It supports scalar and array inputs, computing the result
    element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute cosh(x). Can be a scalar or a
        NumPy array.
    N : int, optional
        The number of terms in the Taylor series to use for the approximation
        (default is 100). Higher values increase accuracy but also
        increase computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of cosh(x) as a NumPy array.
        If the input is scalar,
        a scalar value is returned; otherwise, an array of the same shape as
        the input.

    Examples
    --------
    >>> cosh(0)
    1.0

    >>> cosh(1)
    1.5430806348152437

    >>> cosh(np.array([1, 2, 3]))
    array([ 1.54308063,  3.76219569, 10.06766199])

    Notes
    -----
    - The calculation is performed using NumPy's vectorized
    operations to support
      both scalar and array inputs efficiently.
    - The function incrementally computes each term in the series using the
    previous
      term, optimizing performance and reducing the risk of overflow.
    """
    x = np.asarray(x)  # Convert input to a NumPy array if needed
    result = np.ones_like(
        x, dtype=np.float64
    )  # Initialize result with the first term (1)
    term = np.ones_like(x, dtype=np.float64)  # Start with x^0 / 0! = 1

    for n in range(1, N + 1):
        term *= x**2 / (
            2 * n * (2 * n - 1)
        )  # Incrementally update the term (x^(2n) / (2n)!)
        result += term  # Add the current term to the result

    return result


def tanh(x, N=10):
    """Compute the hyperbolic tangent of x using sinh(x) and cosh(x).

    This function calculates tanh(x) as the ratio of sinh(x) and cosh(x), using
    a truncated Taylor series up to N terms.
    It supports scalar and array inputs,
    computing the result element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute tanh(x). Can be a scalar or a
        NumPy array.
    N : int, optional
        The number of terms in the Taylor series used for sinh(x) and cosh(x)
        approximations (default is 100). Higher values increase accuracy but
        also increase computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of tanh(x) as a NumPy array. If the input
        is scalar,
        a scalar value is returned; otherwise, an array of the same shape as
        the input.

    Examples
    --------
    >>> tanh(0)
    0.0

    >>> tanh(1)
    0.7615941559557649

    >>> tanh(np.array([1, 2, 3]))
    array([0.76159416, 0.96402758, 0.99505475])

    Notes
    -----
    - This function uses the sinh(x) and cosh(x) functions previously defined,
      which are based on truncated Taylor series expansions.
    - The calculation is performed using NumPy's vectorized operations to
    support
      both scalar and array inputs efficiently.
    """
    sinh_x = sinh(x, N)
    cosh_x = cosh(x, N)
    return sinh_x / cosh_x  # Return the ratio of sinh(x) and cosh(x)


def gamma(z):
    """Compute the gamma function Γ(z) using the Lanczos approximation.

    This function uses the Lanczos approximation, which is known for its
    accuracy
    and efficiency in computing the gamma function.

    Parameters
    ----------
    z : float
        The input value for which to compute the gamma function.
        Should be positive.

    Returns
    -------
    float
        The computed value of Γ(z).

    Notes
    -----
    The Lanczos approximation formula is:
        Γ(z) ≈ sqrt(2π) * (z + g - 0.5)^(z - 0.5) * exp(-(z + g - 0.5)) * A(z)
    where A(z) is a weighted sum of coefficients.
    """
    # Coefficients for the Lanczos approximation (g = 7, common choice)
    g = 7
    coefficients = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ]

    if z < 0.5:
        # Use the reflection formula for values less than 0.5
        return np.pi / (np.sin(np.pi * z) * gamma(1 - z))
    else:
        z -= 1
        x = coefficients[0]
        for i in range(1, len(coefficients)):
            x += coefficients[i] / (z + i)

        t = z + g + 0.5
        return np.sqrt(2 * np.pi) * (t ** (z + 0.5)) * np.exp(-t) * x


def bessel(alpha, x, N=100):
    """Compute the Bessel function J_alpha(x) using series expansion.

    This function approximates the Bessel function using a truncated
    series expansion
    up to N terms.

    Parameters
    ----------
    alpha : float
        The order of the Bessel function (can be any real number).
    x : float or array-like
        The value(s) for which to compute the Bessel function.
    N : int, optional
        The number of terms in the series to use for the approximation
        (default is 100).

    Returns
    -------
    np.ndarray
        The computed value(s) of J_alpha(x).

    Notes
    -----
    The Bessel function of the first kind is defined as:
    J_alpha(x) = Σ (from m=0 to ∞) [(-1)^m / (m! * Γ(m + α + 1))]
    * (x/2)^(2m + α)
    This implementation uses a truncated series expansionto approximate the
    result.
    """
    x = np.asarray(x, dtype=np.float64)
    result = np.zeros_like(x)
    half_x = x / 2  # To avoid recalculating x/2 repeatedly

    for m in range(N):
        # Compute each term in the series
        numerator = (-1) ** m * (half_x ** (2 * m + alpha))
        denominator = fact(m) * gamma(m + alpha + 1)
        term = numerator / denominator

        # Add the term to the result
        result += term

    return result
