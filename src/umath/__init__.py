# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/math.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module provides some basic mathematical functions for
working with floating-point numbers.

.. note:: This module is not available on the BOOST Move hub.
"""

# constants

from typing import Tuple


e: float
"""
Base of the natural logarithm.
"""

pi: float
"""
The ratio of a circle's circumference to its diameter.
"""

# functions


def acos(x: float) -> float:
    """
    Returns the inverse cosine of ``x``.
    """


def asin(x: float) -> float:
    """
    Returns the inverse sine of ``x``.
    """


def atan(x: float) -> float:
    """
    Returns the inverse tangent of ``x``.
    """


def atan2(y: float, x: float) -> float:
    """
    Returns the principal value of the inverse tangent of ``y/x``.
    """


def ceil(x: float) -> int:
    """
    Returns an integer, being ``x`` rounded towards positive infinity.
    """


def copysign(x: float, y: float) -> float:
    """
    Returns ``x`` with the sign of ``y``.
    """


def cos(x: float) -> float:
    """
    Returns the cosine of ``x``.
    """


def degrees(x: float) -> float:
    """
    Returns radians ``x`` converted to degrees.
    """


def exp(x: float) -> float:
    """
    Returns the exponential of ``x``.
    """


def fabs(x: float) -> float:
    """
    Returns the absolute value of ``x``.

    Use ``abs(x)`` instead for integers.
    """


def floor(x: float) -> float:
    """
    Returns an integer, being ``x`` rounded towards negative infinity.
    """


def fmod(x: float, y: float) -> float:
    """
    Returns the remainder of ``x/y``.

    Use ``x % y`` instead for integers.
    """


def frexp(x: float) -> Tuple[float, int]:
    """
    Decomposes a floating-point number into its mantissa and exponent.
    The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
    exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
    the relation ``0.5 <= abs(m) < 1`` holds.
    """


def isfinite(x: float) -> bool:
    """
    Returns ``True`` if ``x`` is finite.
    """


def isinf(x: float) -> bool:
    """
    Returns ``True`` if ``x`` is infinite.
    """


def isnan(x: float) -> bool:
    """
    Returns ``True`` if ``x`` is not-a-number
    """


def ldexp(x: float, exp: int) -> float:
    """
    Returns ``x * (2**exp)``.
    """


def log(x: float) -> float:
    """
    Returns the natural logarithm of ``x``.
    """


def modf(x: float) -> Tuple[float, float]:
    """
    Returns a tuple of two floats, being the fractional and integral parts of
    ``x``.  Both return values have the same sign as ``x``.
    """


def pow(x: float, y: float) -> float:
    """
    Returns ``x`` to the power of ``y``.

    Use ``x ** y`` instead for intergers.
    """


def radians(x: float) -> float:
    """
    Returns degrees ``x`` converted to radians.
    """


def sin(x: float) -> float:
    """
    Returns the sine of ``x``.
    """


def sqrt(x: float) -> float:
    """
    Returns the square root of ``x``.
    """


def tan(x: float) -> float:
    """
    Returns the tangent of ``x``.
    """


def trunc(x: float) -> int:
    """
    Returns an integer, being ``x`` rounded towards 0.
    """
