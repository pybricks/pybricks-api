# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of the documentation copied and adapted from:
# https://docs.python.org/3/library/math.html
# Copyright (c) 2001-2021 Python Software Foundation


"""
Math functions.
"""

from typing import Tuple as Tuple


e = 2.718282
"""The mathematical constant e."""


pi = 3.141593
"""The mathematical constant π."""


def sin(x: float) -> float:
    """sin(x) -> float

    Gets the sine of an angle.

    Arguments:
        x (float): Angle in radians.

    Returns:
        Sine of ``x``.
    """


def asin(x: float) -> float:
    """asin(x) -> float

    Applies the inverse sine operation.

    Arguments:
        x (float): Opposite / hypotenuse.

    Returns:
        Arcsine of ``x``, in radians.
    """


def cos(x: float) -> float:
    """cos(x) -> float

    Gets the cosine of an angle.

    Arguments:
        x (float): Angle in radians.

    Returns:
        Cosine of ``x``.
    """


def acos(x: float) -> float:
    """acos(x) -> float

    Applies the inverse cosine operation.

    Arguments:
        x (float): Adjacent / hypotenuse.

    Returns:
        Arccosine of ``x``, in radians.
    """


def tan(x: float) -> float:
    """tan(x) -> float

    Gets the tangent of an angle.

    Arguments:
        x (float): Angle in radians.

    Returns:
        Tangent of ``x``.
    """


def atan(x: float) -> float:
    """atan(x) -> float

    Applies the inverse tangent operation.

    Arguments:
        x (float): Opposite / adjacent.

    Returns:
        Arctangent of ``x``, in radians.
    """


def atan2(b: float, a: float) -> float:
    """atan2(b, a) -> float

    Applies the inverse tangent operation on ``b / a``, and accounts for
    the signs of ``b`` and ``a`` to produce the expected angle.

    Arguments:
        b (float): Opposite side of the triangle.
        a (float): Adjacent side of the triangle.

    Returns:
        Arctangent of ``b / a``, in radians.
    """


def degrees(x: float) -> float:
    """degrees(x) -> float

    Converts an angle from radians to degrees.

    Arguments:
        x (float): Angle in radians.

    Returns:
        Angle in degrees.
    """


def radians(x: float) -> float:
    """radians(x) -> float

    Converts an angle from degrees to radians.

    Arguments:
        x (float): Angle in degrees.

    Returns:
        Angle in radians.
    """


def pow(x: float, y: float) -> float:
    """pow(x, y) -> float

    Gets ``x`` raised to the power of ``y``.

    Arguments:
        x (float): The base number.
        y (float): The exponent.

    Returns:
        ``x`` raised to the power of ``y``.
    """


def exp(x: float) -> float:
    """exp(x) -> float

    Gets :attr:`e` raised to the power of ``x``.

    Arguments:
        x (float): The exponent.

    Returns:
        :attr:`e` raised to the power of ``x``.
    """


def log(x: float) -> float:
    """log(x) -> float

    Gets the natural logarithm.

    Arguments:
        x (float): The value.

    Returns:
        The natural logarithm of ``x``.
    """


def sqrt(x: float) -> float:
    """sqrt(x) -> float

    Gets the square root.

    Arguments:
        x (float): The value ``x``.

    Returns:
        The square root of ``x``.
    """


def ceil(x: float) -> int:
    """ceil(x) -> int

    Rounds up.

    Arguments:
        x (float): The value to be rounded.

    Returns:
        Value rounded towards positive infinity.
    """


def floor(x: float) -> int:
    """floor(x) -> int

    Rounds down.

    Arguments:
        x (float): The value to be rounded.

    Returns:
        Value rounded towards negative infinity.
    """


def trunc(x: float) -> int:
    """trunc(x) -> int

    Truncates decimals to get the integer part of a value.

    This is the same as rounding towards ``0``.

    Arguments:
        x (float): The value to be truncated.

    Returns:
        Integer part of the value.
    """


def fmod(x: float, y: float) -> float:
    """fmod(x, y) -> float

    Gets the remainder of ``x / y``.

    Not to be confused with :func:`modf`.

    Arguments:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        Remainder after division
    """


def fabs(x: float) -> float:
    """fabs(x) -> float

    Gets the absolute value.

    Arguments:
        x (float): The value.

    Returns:
        Absolute value of ``x``.
    """


def modf(x: float) -> Tuple[float, float]:
    """modf(x) -> Tuple[float, float]

    Gets the fractional and integral parts of ``x``, both with the same sign
    as ``x``.

    Not to be confused with :func:`fmod`.

    Arguments:
        x (float): The value to be decomposed.

    Returns:
        Tuple of fractional and integral parts.
    """


def frexp(x: float) -> Tuple[float, int]:
    """frexp(x) -> Tuple[float, float]

    Decomposes a value ``x`` into a
    tuple ``(m, p)``, such that ``x == m * (2 ** p)``.

    Arguments:
        x (float): The value to be decomposed.

    Returns:
        Tuple of ``m`` and ``p``.
    """


def ldexp(m: float, p: int) -> float:
    """ldexp(m, p) -> float

    Computes ``m * (2 ** p)``.

    Arguments:
        m (float): The value.
        p (float): The exponent.

    Returns:
        Result of ``m * (2 ** p)``.
    """


def copysign(x: float, y: float) -> float:
    """copysign(x, y) -> float

    Gets ``x`` with the sign of ``y``.

    Arguments:
        x (float): Determines the magnitude of the return value.
        y (float): Determines the sign of the return value.

    Returns:
        ``x`` with the sign of ``y``.
    """


def isfinite(x: float) -> bool:
    """isfinite(x) -> bool

    Checks if a value is finite.

    Arguments:
        x (float): The value to be checked.

    Returns:
        ``True`` if ``x`` is finite, else ``False``.
    """


def isinfinite(x: float) -> bool:
    """isinfinite(x) -> bool

    Checks if a value is infinite.

    Arguments:
        x (float): The value to be checked.

    Returns:
        ``True`` if ``x`` is infinite, else ``False``.
    """


def isnan(x: float) -> bool:
    """isnan(x) -> bool

    Checks if a value is not-a-number.

    Arguments:
        x (float): The value to be checked.

    Returns:
        ``True`` if ``x`` is not-a-number, else ``False``.
    """
