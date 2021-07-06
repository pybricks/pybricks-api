# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/random.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
This module implements pseudo-random number generators.

.. note:: This module is not available on the BOOST Move Hub.

    You can make your own random number generator like this instead::

        _rand = hub.battery.voltage() + hub.battery.current()  # seed

        # Return a random integer N such that a <= N <= b.
        def randint(a, b):
            global _rand
            _rand = 75 * _rand % 65537  # Lehmer
            return _rand * (b - a + 1) // 65537 + a
"""

from typing import Any, Optional, Sequence, overload


[
    "random",
    "uniform",
]

# bookkeeping


def seed(a: Optional[int] = None) -> None:
    """
    Initialize the random number generator.

    Args:
        a: Optional seed value. If ``None``, the system timer will be used.

    .. tip:: This is called when the module is imported, so normally you do
        not need to call this.
    """


# integers


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
    Returns a randomly selected element from ``range(start, stop, step)``.
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
    Return the next random floating point number in the range [0.0, 1.0).

    .. tip:: The `interval notation`_ indicates that this includes 0.0 and
        excludes 1.0.

    .. _interval notation:
        https://en.wikipedia.org/wiki/Interval_(mathematics)#Notations_for_intervals
    """


def uniform(a: float, b: float) -> float:
    """
    Returns a random floating point number *N* such that ``a`` <= *N* <= ``b``
    for ``a`` <= ``b`` and ``b`` <= *N* <= ``a`` for ``b`` < ``a``.

    The end-point value ``b`` may or may not be included in the range depending
    on floating-point rounding in the equation ``a + (b-a) * random()``.
    """
