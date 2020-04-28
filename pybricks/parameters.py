# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Constant parameters/arguments for the Pybricks API."""

from enum import Enum as _Enum


class _PybricksEnumMeta(type(_Enum)):
    def __dir__(cls):
        yield '__class__'
        yield '__name__'
        for member in cls:
            yield member.name


class _PybricksEnum(_Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield '__class__'
        for member in type(self):
            yield member.name

    def __str__(self):
        return '{}.{}'.format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Color(_PybricksEnum):
    """Light or surface color.

    .. data:: BLACK
    .. data:: BLUE
    .. data:: GREEN
    .. data:: YELLOW
    .. data:: RED
    .. data:: WHITE
    .. data:: BROWN
    .. data:: ORANGE
    .. data:: PURPLE
    """

    BLACK = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    RED = 5
    WHITE = 6
    BROWN = 7
    ORANGE = 8
    PURPLE = 9


class Port(_PybricksEnum):
    """Port on the programmable brick or hub."""

    # Generic motor/sensor ports
    A = ord('A')
    B = ord('B')
    C = ord('C')
    D = ord('D')
    E = ord('E')
    F = ord('F')

    # NXT/EV3 sensor ports
    S1 = ord('1')
    S2 = ord('2')
    S3 = ord('3')
    S4 = ord('4')


class Stop(_PybricksEnum):
    """Action after the motor stops: coast, brake, or hold.

    .. data:: COAST

        Let the motor move freely.

    .. data:: BRAKE

        Passively resist small external forces.

    .. data:: HOLD

        Keep controlling the motor to hold it at the commanded angle. This is
        only available on motors with encoders.
    """

    COAST = 0
    BRAKE = 1
    HOLD = 2


class Direction(_PybricksEnum):
    """Rotational direction for positive speed or angle values.

    .. data:: CLOCKWISE

        A positive speed value should make the motor move clockwise.

    .. data:: COUNTERCLOCKWISE

        A positive speed value should make the motor move counterclockwise.

    +--------------------------------+-------------------+-----------------+
    | ``positive_direction =``       | Positive speed:   | Negative speed: |
    +================================+===================+=================+
    | ``Direction.CLOCKWISE``        | clockwise         | counterclockwise|
    +--------------------------------+-------------------+-----------------+
    | ``Direction.COUNTERCLOCKWISE`` | counterclockwise  | clockwise       |
    +--------------------------------+-------------------+-----------------+
    """

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1


class Button(_PybricksEnum):
    """Buttons on a brick or remote:

    .. data:: LEFT_DOWN
    .. data:: DOWN
    .. data:: RIGHT_DOWN
    .. data:: LEFT
    .. data:: CENTER
    .. data:: RIGHT
    .. data:: LEFT_UP
    .. data:: UP
    .. data:: BEACON
    .. data:: RIGHT_UP

    +-----------+----------+-----------+
    |           |          |           |
    | LEFT_UP   |UP/BEACON | RIGHT_UP  |
    |           |          |           |
    +-----------+----------+-----------+
    |           |          |           |
    | LEFT      |  CENTER  | RIGHT     |
    |           |          |           |
    +-----------+----------+-----------+
    |           |          |           |
    | LEFT_DOWN |   DOWN   | RIGHT_DOWN|
    |           |          |           |
    +-----------+----------+-----------+
    """

    LEFT_DOWN = 1
    DOWN = 2
    RIGHT_DOWN = 3
    LEFT = 4
    CENTER = 5
    RIGHT = 6
    LEFT_UP = 7
    UP = 8
    BEACON = 8
    RIGHT_UP = 9


class Axis(_PybricksEnum):
    """Unit axes of a coordinate system.

    .. data:: X
    .. data:: Y
    .. data:: Z

    Some methods let you measure along all axes at once:

    .. data:: ALL
    """
    X = (1, 0, 0)
    Y = (0, 1, 0)
    Z = (0, 0, 1)
    ALL = None


class Side(_PybricksEnum):
    """Sides or face of a device such as a hub or a sensor. Such devices are
    usually shaped like a rectangular box with six of the following sides:

    .. data:: TOP
    .. data:: BOTTOM
    .. data:: FRONT
    .. data:: BACK
    .. data:: LEFT
    .. data:: RIGHT
    """

    RIGHT = 6
    FRONT = 0
    TOP = 8
    LEFT = 4
    BACK = 5
    BOTTOM = 2
