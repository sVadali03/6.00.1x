# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    val = 0
    for i in poly:
        val += (poly[(poly.index(i))]) * (x ** (poly.index(i)))
    return val

print(evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0) , -13))

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    der = ()
    for i in poly:
        if (poly.index(i)) > 0:
            der = der + (((poly.index(i)) * i),)
    return der

print(compute_deriv((0.0, 0.0, 5.0, 9.3, 7.0)))

def compute_root(poly, x_0, epsilon,x):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    x_n = x
    i = 1.0
    der = compute_deriv(poly)
    
    while abs(evaluate_poly(poly, x_n)) > epsilon:
        x_n = x_n - evaluate_poly(poly, x_n) / evaluate_poly(der, x_n)
        i += 1.0
    return x_n, i

print(compute_root((-13.39, 0.0, 17.5, 3.0, 1.0), 0.1, .0001,-13))

