# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Core linear algebra functionality for orientation sensors and robotics."""


class Matrix:
    """Mathematical representation of a matrix. It supports common operations
    such as matrix addition (``+``), subtraction (``-``),
    and multiplication (``*``). A :class:`.Matrix` object is immutable."""

    def __init__(self, rows):
        """

        Arguments:
            rows (list): List of rows. Each row is itself a list of numbers.

        """

    @property
    def T(self):
        """Returns a new :class:`.Matrix` that is the transpose of the
        original."""
        pass

    @property
    def shape(self):
        """Returns a tuple (``m``, ``n``),
        where ``m`` is the number of rows and ``n`` is the number of columns.
        """
        pass


def vector(x, y, z=None):
    """Convenience function to create a :class:`.Matrix` with the
    shape (``3``, ``1``) or (``2``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.
        z (float): z-coordinate of the vector (optional).


    Returns:
            Matrix: A matrix with the shape of a column vector.
    """
    pass


class Axis():
    """Unit axes of a coordinate system.

    .. data:: X = vector(1, 0, 0)
    .. data:: Y = vector(0, 1, 0)
    .. data:: Z = vector(0, 0, 1)

    """
    X = vector(1, 0, 0)
    Y = vector(0, 1, 0)
    Z = vector(0, 0, 1)
