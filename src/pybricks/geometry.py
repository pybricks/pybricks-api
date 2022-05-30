# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Core linear algebra functionality for orientation sensors and robotics."""

from __future__ import annotations

from typing import Tuple, Collection, overload


class Matrix:
    """Mathematical representation of a matrix. It supports
    addition (``A + B``), subtraction (``A - B``),
    and matrix multiplication (``A * B``) for matrices of compatible size.

    It also supports scalar multiplication (``c * A`` or ``A * c``)
    and scalar division (``A / c``).

    A :class:`.Matrix` object is immutable."""

    def __add__(self, other) -> Matrix:
        ...

    def __iadd__(self, other) -> Matrix:
        ...

    def __sub__(self, other) -> Matrix:
        ...

    def __isub__(self, other) -> Matrix:
        ...

    def __mul__(self, other) -> Matrix:
        ...

    def __rmul__(self, other) -> Matrix:
        ...

    def __imul__(self, other) -> Matrix:
        ...

    def __truediv__(self, other) -> Matrix:
        ...

    def __itruediv__(self, other) -> Matrix:
        ...

    def __floordiv__(self, other) -> Matrix:
        ...

    def __ifloordiv__(self, other) -> Matrix:
        ...

    def __init__(self, rows: Collection[Collection[int]]):
        """Matrix(rows)

        Arguments:
            rows (list): List of rows. Each row is itself a list of numbers.

        """

    @property
    def T(self) -> Matrix:
        """Returns a new :class:`.Matrix` that is the transpose of the
        original."""
        pass

    @property
    def shape(self) -> Tuple[int, int]:
        """Returns a tuple (``m``, ``n``),
        where ``m`` is the number of rows and ``n`` is the number of columns.
        """
        pass


@overload
def vector(x: float, y: float) -> Matrix:
    ...


@overload
def vector(x: float, y: float, z: float) -> Matrix:
    ...


def vector(*args):
    """
    vector(x, y) -> Matrix
    vector(x, y, z) -> Matrix

    Convenience function to create a :class:`.Matrix` with the
    shape (``2``, ``1``) or (``3``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.
        z (float): z-coordinate of the vector (optional).

    Returns:
        A matrix with the shape of a column vector.
    """
    pass


class Axis:
    """Unit axes of a coordinate system.

    .. data:: X = vector(1, 0, 0)
    .. data:: Y = vector(0, 1, 0)
    .. data:: Z = vector(0, 0, 1)

    """

    X: Matrix = vector(1, 0, 0)
    Y: Matrix = vector(0, 1, 0)
    Z: Matrix = vector(0, 0, 1)
