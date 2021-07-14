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

from typing import Tuple as _Tuple


e = 2.718282
"""The mathematical constant e."""


pi = 3.141593
"""The mathematical constant π."""


def sin(x: float) -> float:
    """Gets the sine of the given angle ``x``.

    Arguments:
        x: Angle in radians.

    Returns:
        Sine of ``x``.
    """
    pass


def asin(x: float) -> float:
    """Applies the inverse sine operation on ``x``.

    Arguments:
        x: Opposite / hypotenuse.

    Returns:
        Arcsine of ``x``, in radians.
    """
    pass


def cos(x: float) -> float:
    """Gets the cosine of the given angle ``x``.

    Arguments:
        x: Angle in radians.

    Returns:
        Cosine of ``x``.
    """
    pass


def acos(x: float) -> float:
    """Applies the inverse cosine operation on ``x``.

    Arguments:
        x: Adjacent / hypotenuse.

    Returns:
        Arccosine of ``x``, in radians.
    """
    pass


def tan(x: float) -> float:
    """Gets the tangent of the given angle ``x``.

    Arguments:
        x: Angle in radians.

    Returns:
        Tangent of ``x``.
    """
    pass


def atan(x: float) -> float:
    """Applies the inverse tangent operation on ``x``.

    Arguments:
        x: Opposite / adjacent.

    Returns:
        Arctangent of ``x``, in radians.
    """
    pass


def atan2(b: float, a: float) -> float:
    """Applies the inverse tangent operation on ``b / a``, and accounts for
    the signs of ``b`` and ``a`` to produce the expected angle.

    Arguments:
        b: Opposite side of the triangle.
        a: Adjacent side of the triangle.

    Returns:
        Arctangent of ``b / a``, in radians.
    """
    pass


def degrees(x: float) -> float:
    """Converts an angle ``x`` from radians to degrees.

    Arguments:
        x: Angle in radians.

    Returns:
        Angle in degrees.
    """
    pass


def radians(x: float) -> float:
    """Converts an angle ``x`` from degrees to radians.

    Arguments:
        x: Angle in degrees.

    Returns:
        Angle in radians.
    """
    pass


def pow(x: float, y: float) -> float:
    """Gets ``x`` raised to the power of ``y``.

    Arguments:
        x: The base number.
        y: The exponent.

    Returns:
        ``x`` raised to the power of ``y``.
    """
    pass


def exp(x: float) -> float:
    """Gets :attr:`e` raised to the power of ``x``.

    Arguments:
        x: The exponent.

    Returns:
        :attr:`e` raised to the power of ``x``.
    """
    pass


def log(x: float) -> float:
    """Gets the natural logarithm of ``x``.

    Arguments:
        x: The value ``x``.

    Returns:
        The natural logarithm of ``x``.
    """
    pass


def sqrt(x: float) -> float:
    """Gets the square root of ``x``.

    Arguments:
        x: The value ``x``.

    Returns:
        The square root of ``x``.
    """
    pass


def ceil(x: float) -> int:
    """Rounds up.

    Arguments:
        x: The value ``x``.

    Returns:
        Value rounded towards positive infinity.
    """
    pass


def floor(x: float) -> int:
    """Rounds down.

    Arguments:
        x: The value ``x``.

    Returns:
        Value rounded towards negative infinity.
    """
    pass


def trunc(x: float) -> int:
    """Truncates decimals to get the integer part of a value.

    This is the same as rounding towards ``0``.

    Arguments:
        x: The value ``x``.

    Returns:
        Integer part of the value.
    """
    pass


def fmod(x: float, y: float) -> float:
    """Gets the remainder of ``x / y``.

    Not to be confused with :func:`modf`.

    Arguments:
        x: The numerator.
        y: The denominator.

    Returns:
        Remainder after division
    """
    pass


def fabs(x: float) -> float:
    """Gets the absolute value of ``x``.

    Arguments:
        x: The value.

    Returns:
        Absolute value.
    """
    pass


def modf(x: float) -> _Tuple[float, float]:
    """Gets the fractional and integral parts of ``x``, both with the same sign
    as ``x``.

    Not to be confused with :func:`fmod`.

    Arguments:
        x: The value to be decomposed.

    Returns:
        Tuple of fractional and integral parts.
    """
    pass


def frexp(x: float) -> _Tuple[float, int]:
    """Decomposes a value ``x`` into a
    tuple ``(m, p)``, such that ``x == m * (2 ** p)``.

    Arguments:
        x: The value to be decomposed.

    Returns:
        Tuple of ``m`` and ``p``.
    """
    pass


def ldexp(m: float, p: int) -> float:
    """Computes ``m * (2 ** p)``.

    Arguments:
        m: The value.
        p: The exponent.

    Returns:
        Result of ``m * (2 ** p)``.
    """
    pass


def copysign(x: float, y: float) -> float:
    """Gets ``x`` with the sign of ``y``.

    Arguments:
        x: Determines the magnitude of the return value.
        y: Determines the sign of the return value.

    Returns:
        ``x`` with the sign of ``y``.
    """
    pass


def isfinite(x: float) -> bool:
    """Checks if ``x`` is finite.

    Returns:
        ``True`` if ``x`` is finite, else ``False``.
    """
    pass


def isinfinite(x: float) -> bool:
    """Checks if ``x`` is infinite.

    Returns:
        ``True`` if ``x`` is infinite, else ``False``.
    """
    pass


def isnan(x: float) -> bool:
    """Checks if ``x`` is not-a-number.

    Returns:
        ``True`` if ``x`` is not-a-number, else ``False``.
    """
    pass
