# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Constant parameters/arguments for the Pybricks API."""

from __future__ import annotations

from enum import Enum
from typing import Union, TYPE_CHECKING
import os

from .tools import Matrix as _Matrix, vector as _vector

if TYPE_CHECKING or os.environ.get("SPHINX_BUILD") == "True":
    Number = Union[int, float]
    """
    Numbers can be represented as integers or floating point values:

        * Integers (:class:`int <ubuiltins.int>`) are whole numbers
          like ``15`` or ``-123``.
        * Floating point values (:class:`float <ubuiltins.float>`) are decimal
          numbers like ``3.14`` or ``-123.45``.

    If you see :class:`Number` as the argument type, both
    :class:`int <ubuiltins.int>` and :class:`float <ubuiltins.float>` may be used.

    For example, :func:`wait(15) <pybricks.tools.wait>` and
    :func:`wait(15.75) <pybricks.tools.wait>` are both allowed. In most functions,
    however, your input value will be truncated to a whole number anyway. In this
    example, either command makes the program pause for just 15 milliseconds.

    .. note::
        The BOOST Move hub doesn't support floating point numbers due to
        limited system resources. Only integers can be used on that hub.
    """


class _PybricksEnumMeta(type(Enum)):
    @classmethod
    def __dir__(cls):
        yield "__class__"
        yield "__name__"
        for member in cls:
            yield member.name


class _PybricksEnum(Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield "__class__"
        for member in type(self):
            yield member.name

    def __str__(self):
        return "{}.{}".format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Axis:
    """Unit axes of a coordinate system.

    .. data:: X = vector(1, 0, 0)
    .. data:: Y = vector(0, 1, 0)
    .. data:: Z = vector(0, 0, 1)

    """

    X: _Matrix = _vector(1, 0, 0)
    Y: _Matrix = _vector(0, 1, 0)
    Z: _Matrix = _vector(0, 0, 1)


class Color:
    """Light or surface color."""

    NONE: Color = ...
    BLACK: Color = ...
    GRAY: Color = ...
    WHITE: Color = ...
    RED: Color = ...
    ORANGE: Color = ...
    BROWN: Color = ...
    YELLOW: Color = ...
    GREEN: Color = ...
    CYAN: Color = ...
    BLUE: Color = ...
    VIOLET: Color = ...
    MAGENTA: Color = ...

    def __init__(self, h: Number, s: Number = 100, v: Number = 100):
        """Color(h, s=100, v=100)

        Arguments:
            h (Number, deg): Hue.
            s (Number, %): Saturation.
            v (Number, %): Brightness value.
        """

        self.h = int(h) % 360
        """
        The hue.
        """

        self.s = max(0, min(int(s), 100))
        """
        The saturation.
        """

        self.v = max(0, min(int(v), 100))
        """
        The brightness value.
        """

    def __iter__(self):
        """Allows unpacking of the Color instance into h, s, and v."""
        return iter((self.h, self.s, self.v))

    def __repr__(self):
        return "Color(h={}, s={}, v={})".format(self.h, self.s, self.v)

    def __eq__(self, other: Color) -> bool: ...

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v), self.name)

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)


Color.NONE = Color(0, 0, 0)
Color.BLACK = Color(0, 0, 10)
Color.GRAY = Color(0, 0, 50)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(0, 100, 100)
Color.ORANGE = Color(30, 100, 100)
Color.BROWN = Color(30, 100, 50)
Color.YELLOW = Color(60, 100, 100)
Color.GREEN = Color(120, 100, 100)
Color.CYAN = Color(180, 100, 100)
Color.BLUE = Color(240, 100, 100)
Color.VIOLET = Color(270, 100, 100)
Color.MAGENTA = Color(300, 100, 100)


class Port(_PybricksEnum):
    """Port on the programmable brick or hub."""

    # Generic motor/sensor ports
    A: Port = ord("A")
    B: Port = ord("B")
    C: Port = ord("C")
    D: Port = ord("D")
    E: Port = ord("E")
    F: Port = ord("F")

    # NXT/EV3 sensor ports
    S1: Port = ord("1")
    S2: Port = ord("2")
    S3: Port = ord("3")
    S4: Port = ord("4")


class Stop(_PybricksEnum):
    """Action after the motor stops or reaches its target."""

    COAST: Stop = 0
    """Let the motor move freely."""

    COAST_SMART: Stop = 4
    """
    Let the motor move freely. For the next relative angle maneuver,
    take the last target angle (instead of the current angle) as the new
    starting point. This reduces cumulative errors. This will apply only if the
    current angle is less than twice the configured position tolerance.
    """

    BRAKE: Stop = 1
    """Passively resist small external forces."""

    HOLD: Stop = 2
    """Keep controlling the motor to hold it at the commanded angle."""

    NONE: Stop = 3
    """
    Do not decelerate when approaching the target position. This can be used
    to concatenate multiple motor or drive base maneuvers without stopping. If
    no further commands are given, the motor will proceed to run indefinitely
    at the given speed.
    """


class Direction(_PybricksEnum):
    """Rotational direction for positive speed or angle values."""

    CLOCKWISE: Direction = 0
    """A positive speed value should make the motor move clockwise."""

    COUNTERCLOCKWISE: Direction = 1
    """A positive speed value should make the motor move counterclockwise."""


class Button(_PybricksEnum):
    """Buttons on a hub or remote."""

    LEFT_DOWN: Button = 1
    LEFT_MINUS: Button = 1
    DOWN: Button = 2
    RIGHT_DOWN: Button = 3
    RIGHT_MINUS: Button = 3
    LEFT: Button = 4
    CENTER: Button = 5
    RIGHT: Button = 6
    LEFT_UP: Button = 7
    LEFT_PLUS: Button = 7
    UP: Button = 8
    BEACON: Button = 8
    RIGHT_UP: Button = 9
    RIGHT_PLUS: Button = 9
    BLUETOOTH: Button = 9
    A: Button = 0
    B: Button = 0
    X: Button = 0
    Y: Button = 0
    LB: Button = 0
    RB: Button = 0
    LJ: Button = 0
    RJ: Button = 0
    P1: Button = 0
    P2: Button = 0
    P3: Button = 0
    P4: Button = 0
    GUIDE: Button = 0
    MENU: Button = 0
    UPLOAD: Button = 0
    VIEW: Button = 0


class Side(_PybricksEnum):
    """Side of a hub or a sensor."""

    RIGHT: Side = 6
    FRONT: Side = 0
    TOP: Side = 8
    LEFT: Side = 4
    BACK: Side = 5
    BOTTOM: Side = 2


class Icon:
    """Icons to display on a light matrix.

    Each of the following attributes are matrices. This means you can scale
    icons to adjust the brightness or add icons to make composites.
    """

    UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    """
    DOWN: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨🟨
    | ⬜⬜🟨⬜⬜
    """
    RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | 🟨🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT_UP: _Matrix = ...
    """
    | ⬜⬜🟨🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    | 🟨⬜⬜⬜⬜
    """
    ARROW_RIGHT_DOWN: _Matrix = ...
    """
    | 🟨⬜⬜⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨🟨🟨
    """
    ARROW_LEFT_UP: _Matrix = ...
    """
    | 🟨🟨🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | ⬜⬜⬜⬜🟨
    """
    ARROW_LEFT_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨🟨⬜⬜
    """
    ARROW_UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜🟨⬜🟨
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_DOWN: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    | 🟨⬜🟨⬜🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    HAPPY: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | 🟨⬜⬜⬜🟨
    | ⬜🟨🟨🟨⬜
    """
    SAD: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜⬜⬜🟨
    """
    EYE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW_UP: _Matrix = ...
    """
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW_UP: _Matrix = ...
    """
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    HEART: _Matrix = ...
    """
    | ⬜🟨⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    PAUSE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    EMPTY: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FULL: _Matrix = ...
    """
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    """
    SQUARE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_RIGHT: _Matrix = ...
    """
    | ⬜🟨⬜⬜⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    """
    TRIANGLE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜⬜⬜🟨⬜
    """
    TRIANGLE_UP: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    CIRCLE: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    """
    CLOCKWISE: _Matrix = ...
    """
    | 🟨🟨🟨🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    """
    COUNTERCLOCKWISE: _Matrix = ...
    """
    | ⬜🟨🟨🟨🟨
    | ⬜🟨⬜⬜🟨
    | ⬜🟨⬜⬜🟨
    | 🟨🟨🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    """
    TRUE: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FALSE: _Matrix = ...
    """
    | 🟨⬜⬜⬜🟨
    | ⬜🟨⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜🟨⬜
    | 🟨⬜⬜⬜🟨
    """
