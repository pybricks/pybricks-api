# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/random.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
This module implements pseudo-random number generators.

All functions in this module should be used with positional arguments. Keyword
arguments are not supported.
"""

from typing import Any, Optional, Sequence, overload


def seed(a: Optional[int] = None) -> None:
    """
    seed(value=None)

    Initializes the random number generator.

    This gets called when the module is imported, so normally you do
    not need to call this.

    Arguments:
        value: Seed value. When using ``None``, the system timer will be used.
    """


@overload
def randrange(stop: int) -> int:
    ...


@overload
def randrange(start: int, stop: int) -> int:
    ...


@overload
def randrange(start: int, stop: int, step: int) -> int:
    ...


def randrange(start, stop, step):
    """
    randrange(stop) -> int
    randrange(start, stop) -> int
    randrange(start, stop, step) -> int

    Returns a randomly selected element from ``range(start, stop, step)``.

    For example, ``randrange(1, 7, 2)`` returns random numbers from ``1`` up to
    (but excluding) ``7``, in increments of ``2``. In other words, it
    returns ``1``, ``3``, or ``5``.


    Arguments:
        start (int): Lowest value. Defaults to ``0`` if only one argument is given.
        stop (int): Highest value. This value is *not* included in the range.
        step (int): Increment between values. Defaults to ``1`` if only one
            or two arguments are given.

    Returns:
        The random number.
    """


def randint(a: int, b: int) -> int:
    """
    Returns a random integer *N* such that ``a`` <= *N* <= ``b``.
    """


def getrandbits(k: int) -> int:
    """
    Returns a non-negative integer with ``k`` random bits.
    """


# sequences


def choice(seq: Sequence[Any]) -> Any:
    """
    Returns a random element from the non-empty sequence ``seq``.

    If ``seq`` is empty, raises ``IndexError``.
    """


# real


def random() -> float:
    """
    random() -> float

    Gets a random value between ``0`` and ``1``.

    Returns:
        A random value satisfying :math:`0 \\leq x < 1`.
    """


def uniform(a: float, b: float) -> float:
    """
    Returns a random floating point number *N* such that ``a`` <= *N* <= ``b``
    for ``a`` <= ``b`` and ``b`` <= *N* <= ``a`` for ``b`` < ``a``.

    The end-point value ``b`` may or may not be included in the range depending
    on floating-point rounding in the equation ``a + (b-a) * random()``.
    """
