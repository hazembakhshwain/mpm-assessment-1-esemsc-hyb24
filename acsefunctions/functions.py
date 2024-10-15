import numpy as np
from functools import cache

@cache
def fact(x):
    """
    Calculate the factorial of a non-negative integer x using recursion and caching.

    Parameters
    ----------
    x : int
        The non-negative integer for which the factorial is to be computed.

    Returns
    -------
    int
        The factorial of x (x!).

    Examples
    --------
    >>> fact(5)
    120

    >>> fact(0)
    1

    Notes
    -----
    This function uses recursion and caching (via @cache) to store previously
    computed factorial values for efficiency. Be cautious when using very large
    values of x, as the recursion depth may cause a stack overflow.
    """
    if x == 0 or x == 1:
        return 1
    return x * fact(x - 1)

def exp(x, N=100):
    """
    Compute the exponential of x using the truncated Taylor series.

    This function approximates the value of e^x using a truncated Taylor series 
    up to N terms. It supports scalar and array inputs, computing the result 
    element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute e^x. Can be a scalar or a NumPy array.
    N : int, optional
        The number of terms in the Taylor series to use for the approximation 
        (default is 100). Higher values increase accuracy but also increase computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of e^x as a NumPy array. If the input is scalar, a 
        scalar value is returned; otherwise, an array of the same shape as the input.

    Examples
    --------
    >>> exp(1)
    2.718281828459045

    >>> exp(np.array([1, 2, 3]))
    array([ 2.71828183,  7.3890561 , 20.08553692])

    Notes
    -----
    - The calculation is performed using NumPy's vectorized operations to support 
      both scalar and array inputs efficiently.
    - The function incrementally computes each term in the series using the 
      previous term, which helps minimize the risk of overflow and maximizes efficiency.

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
    """
    Compute the hyperbolic sine of x using the truncated Taylor series.

    This function approximates the value of sinh(x) using a truncated Taylor series 
    up to N terms. It supports scalar and array inputs, computing the result 
    element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute sinh(x). Can be a scalar or a NumPy array.
    N : int, optional
        The number of terms in the Taylor series to use for the approximation 
        (default is 100). Higher values increase accuracy but also increase computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of sinh(x) as a NumPy array. If the input is scalar, 
        a scalar value is returned; otherwise, an array of the same shape as the input.

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
    - The calculation is performed using NumPy's vectorized operations to support 
      both scalar and array inputs efficiently.
    - The function incrementally computes each term in the series using the previous 
      power of x, which helps minimize computational overhead.

    """
    x = np.array(x, dtype=float)  # Convert input to a NumPy array for vectorization
    result = np.zeros_like(x)
    px = x.copy()
    
    for n in range(N + 1):
        result += px / fact(2 * n + 1)
        px *= x**2
        
    return result

def cosh(x, N=10):
    """
    Compute the hyperbolic cosine of x using the truncated Taylor series.

    This function approximates the value of cosh(x) using a truncated Taylor series 
    up to N terms. It supports scalar and array inputs, computing the result 
    element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute cosh(x). Can be a scalar or a NumPy array.
    N : int, optional
        The number of terms in the Taylor series to use for the approximation 
        (default is 100). Higher values increase accuracy but also increase computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of cosh(x) as a NumPy array. If the input is scalar, 
        a scalar value is returned; otherwise, an array of the same shape as the input.

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
    - The calculation is performed using NumPy's vectorized operations to support 
      both scalar and array inputs efficiently.
    - The function incrementally computes each term in the series using the previous 
      term, optimizing performance and reducing the risk of overflow.

    """
    x = np.asarray(x)  # Convert input to a NumPy array if needed
    result = np.ones_like(x, dtype=np.float64)  # Initialize result with the first term (1)
    term = np.ones_like(x, dtype=np.float64)  # Start with x^0 / 0! = 1

    for n in range(1, N + 1):
        term *= x**2 / (2 * n * (2 * n - 1))  # Incrementally update the term (x^(2n) / (2n)!)
        result += term  # Add the current term to the result

    return result

def tanh(x, N=10):
    """
    Compute the hyperbolic tangent of x using sinh(x) and cosh(x).

    This function calculates tanh(x) as the ratio of sinh(x) and cosh(x), using 
    a truncated Taylor series up to N terms. It supports scalar and array inputs, 
    computing the result element-wise for arrays.

    Parameters
    ----------
    x : float or array-like
        The input value(s) for which to compute tanh(x). Can be a scalar or a NumPy array.
    N : int, optional
        The number of terms in the Taylor series used for sinh(x) and cosh(x) 
        approximations (default is 100). Higher values increase accuracy but 
        also increase computation time.

    Returns
    -------
    np.ndarray
        The computed value(s) of tanh(x) as a NumPy array. If the input is scalar, 
        a scalar value is returned; otherwise, an array of the same shape as the input.

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
    - The calculation is performed using NumPy's vectorized operations to support 
      both scalar and array inputs efficiently.

    """
    sinh_x = sinh(x, N)
    cosh_x = cosh(x, N)
    return sinh_x / cosh_x  # Return the ratio of sinh(x) and cosh(x)