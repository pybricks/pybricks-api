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

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload

if TYPE_CHECKING:
    from collections.abc import Sequence


def seed(a: int | None = None) -> None:
    """
    seed(value=None)

    Initializes the random number generator.

    This gets called when the module is imported, so normally you do
    not need to call this.

    Arguments:
        value: Seed value. When using ``None``, the system timer will be used.
    """


@overload
def randrange(stop: int) -> int: ...


@overload
def randrange(start: int, stop: int) -> int: ...


@overload
def randrange(start: int, stop: int, step: int) -> int: ...


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
    randint(a, b) -> int

    Gets a random integer N satisfying a ≤ N ≤ b.

    Arguments:
        a (int): Lowest value. This value *is* included in the range.
        b (int): Highest value. This value *is* included in the range.

    Returns:
        The random integer.
    """


def getrandbits(k: int) -> int:
    """
    getrandbits(k) -> int

    Gets a random integer N satisfying 0 ≤ N < ``2**k``.

    Arguments:
        k (int): How many bits to use for the result.
    """


def choice(seq: Sequence[Any]) -> Any:
    """
    choice(sequence) -> Any

    Gets a random element from a sequence such as a tuple or list.

    Arguments:
        sequence: Sequence from which to select a random element.

    Returns:
        The randomly selected element.

    Raises:
        ``IndexError``: If the sequence is empty.
    """


def random() -> float:
    """
    random() -> float

    Gets a random value x satisfying 0 ≤ x < 1.

    Returns:
        The random value.
    """


def uniform(a: float, b: float) -> float:
    """
    uniform(a, b) -> float

    Gets a random floating point value x satisfying a ≤ x ≤ b.

    Arguments:
        a (float): Lowest value.
        b (float): Highest value.

    Returns:
        The random value.
    """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del Sequence
