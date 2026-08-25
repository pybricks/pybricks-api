# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Constant parameters/arguments for the Pybricks API."""

from __future__ import annotations

import os
from enum import Enum
from typing import TYPE_CHECKING, overload

from .tools import Matrix as _Matrix
from .tools import vector as _vector

if TYPE_CHECKING:
    from typing import Any, Literal

if TYPE_CHECKING or os.environ.get("SPHINX_BUILD") == "True":
    Number = int | float
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
        return f"{type(self).__name__}.{self.name}"

    def __repr__(self):
        return str(self)


class Axis:
    """Unit axes of a coordinate system."""

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

    def __setattr__(self, key, value):
        if key not in ("h", "s", "v"):
            raise AttributeError("Can't modify unknown attribute: " + key)
        if hasattr(self, key):  # immutable after __init__
            raise AttributeError("Can't modify immutable attribute: " + key)
        super().__setattr__(key, value)

    def __iter__(self):
        """Allows unpacking of the Color instance into h, s, and v."""
        return iter((self.h, self.s, self.v))

    def __repr__(self):
        return f"Color(h={self.h}, s={self.s}, v={self.v})"

    def __eq__(self, other: Color) -> bool:
        return self.h == other.h and self.s == other.s and self.v == other.v

    def __hash__(self) -> int:
        return hash((self.h, self.s, self.v))

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v))

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)

    def __lshift__(self, shift: int) -> Color:
        return self.__rshift__(-shift)

    def __rshift__(self, shift: int) -> Color:
        return Color((self.h + shift) % 360, self.s, self.v)


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


class Image:
    """Object representing a graphics image. This can either be an in-memory
    copy of an image or the image displayed on a screen."""

    # Documentation note: This class is also treated as the `screen` object
    # on EV3 so we use |this image| when it would make sense to say "the screen"
    # in that context and it is automatically replaced when the documentation
    # is generated.

    @overload
    def __init__(self, /, source: Image | ImageFile): ...

    @overload
    def __init__(
        self, /, source: Image, sub: Literal[False], x1: int, y1: int, x2: int, y2: int
    ): ...

    def __init__(self, *args):
        """Image(source, sub=False)


        Arguments:
            source (Image):
                The source image. The new object will contain a copy of
                the ``source`` image object.

            sub (bool):
                If ``sub`` is ``True``, then the image object will act as a
                sub-image of the ``source`` image.

                Additional keyword arguments ``x1``, ``y1``, ``x2``, ``y2`` are
                needed when ``sub=True``. These specify the top-left and
                bottom-right coordinates in the ``source`` image that will be
                used as the bounds for the sub-image.
        """

    @property
    def width(self) -> int:
        """Gets the width of |this image| in pixels."""
        return 0

    @property
    def height(self) -> int:
        """Gets the height of |this image| in pixels."""
        return 0

    def clear(self) -> None:
        """clear()

        Clears |this image|. All pixels on |this image| will be set to
        :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.
        """

    def draw_pixel(self, x: int, y: int, color: Color = Color.BLACK) -> None:
        """draw_pixel(x, y, color=Color.BLACK)

        Draws a single pixel on |this image|.

        Arguments:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
            color (Color): The color of the pixel.
        """

    def draw_line(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        width: int = 1,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_line(x1, y1, x2, y2, width=1, color=Color.BLACK)

        Draws a line on |this image|.

        Arguments:
            x1 (int): The x coordinate of the starting point of the line.
            y1 (int): The y coordinate of the starting point of the line.
            x2 (int): The x coordinate of the ending point of the line.
            y2 (int): The y coordinate of the ending point of the line.
            width (int): The width of the line in pixels.
            color (Color): The color of the line.
        """

    def draw_box(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        r: int = 0,
        fill: bool = False,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_box(x1, y1, x2, y2, r=0, fill=False, color=Color.BLACK)

        Draws a box on |this image|.

        Arguments:
            x1 (int): The x coordinate of the left side of the box.
            y1 (int): The y coordinate of the top of the box.
            x2 (int): The x coordinate of the right side of the box.
            y2 (int): The y coordinate of the bottom of the box.
            r (int): The radius of the corners of the box.
            fill (bool): If ``True``, the box will be filled with ``color``,
                otherwise only the outline of the box will be drawn.
            color (Color): The color of the box.
        """

    def draw_circle(
        self, x: int, y: int, r: int, fill: bool = False, color: Color = Color.BLACK
    ) -> None:
        """draw_circle(x, y, r, fill=False, color=Color.BLACK)

        Draws a circle on |this image|.

        Arguments:
            x (int): The x coordinate of the center of the circle.
            y (int): The y coordinate of the center of the circle.
            r (int): The radius of the circle.
            fill (bool): If ``True``, the circle will be filled with
                ``color``, otherwise only the circumference will be drawn.
            color (Color): The color of the circle.
        """

    def draw_image(
        self,
        x: int,
        y: int,
        source: Image | ImageFile,
        transparent: Color | None = None,
    ) -> None:
        """draw_image(x, y, source, transparent=None)

        Draws the ``source`` image on |this image|.

        Arguments:
            x (int):
                The x-axis value where the left side of the image will start.
            y (int):
                The y-axis value where the top of the image will start.
            source (Image):
                The source :class:`Image <pybricks.parameters.Image>`.
            transparent (Color):
                The color of ``image`` to treat as transparent or ``None`` for
                no transparency.
        """

    def load_image(self, source: Image | ImageFile) -> None:
        """load_image(source)

        Clears this image, then draws the ``source`` image centered in
        |this image|.

        Arguments:
            source (Image):
                The source :class:`Image <pybricks.parameters.Image>`.
        """

    def draw_text(
        self,
        x: int,
        y: int,
        text: str,
        text_color: Color = Color.BLACK,
        background_color: Color | None = None,
    ) -> None:
        """draw_text(x, y, text, text_color=Color.BLACK, background_color=None)

        Draws text on |this image|.

        The most recent font set using :meth:`.set_font` will be used or
        :data:`Font.DEFAULT <pybricks.parameters.Font.DEFAULT>` if no font
        has been set yet.

        Arguments:
            x (int):
                The x-axis value where the left side of the text will start.
            y (int):
                The y-axis value where the top of the text will start.
            text (str):
                The text to draw.
            text_color (Color):
                The color used for drawing the text.
            background_color (Color):
                The color used to fill the rectangle behind the text or
                ``None`` for transparent background.
        """

    def print(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        """print(*args, sep=" ", end="\\n")

        Prints a line of text on |this image|.

        This method works like the builtin ``print()`` function, but it writes
        on |this image| instead.

        You can set the font using :meth:`.set_font`. If no font has been set,
        :data:`Font.DEFAULT <pybricks.parameters.Font.DEFAULT>` will be
        used. The text is always printed used black text with a white
        background.

        Unlike the builtin ``print()``, the text does not wrap if it is too
        wide to fit on |this image|. It just gets cut off. But if the text
        would go off of the bottom of |this image|, the entire image is
        scrolled up and the text is printed in the new blank area at the
        bottom of |this image|.

        Arguments:
            args (Any): Zero or more objects to print.
            sep (str): Separator that will be placed between each object that
                is printed.
            end (str): End of line that will be printed after the last object.
        """

    def set_font(self, font: Font) -> None:
        """set_font(font)

        Sets the font used for writing on |this image|.

        The font is used for both :meth:`.draw_text` and :meth:`.print`.

        Arguments:
            font (Font):
                The font to use.
        """

    @staticmethod
    def empty(width: int = 178, height: int = 128) -> Image:
        """empty(width=178, height=128) -> Image

        Creates a new empty :class:`Image` object.

        Arguments:
            width (int):
                The width of the image in pixels.
            height (int):
                The height of the image in pixels.

        Returns:
            A new image with all pixels set
            to :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.

        Raises:
            TypeError:
                If ``width`` or ``height`` is not a number.
            ValueError:
                If ``width`` or ``height`` is less than 1.
            RuntimeError:
                If there was a problem allocating a new image.
        """


class Font:
    """Object that represents a font for writing text."""

    DEFAULT: Font = ...
    """The default font."""

    TERMINUS_16: Font = ...
    """The Terminus font with a height of 16 pixels."""

    LIBERATIONSANS_14: Font = ...
    """The Liberation Sans regular font with a height of 14 pixels."""

    MONO_8X5_8: Font = ...
    """A monospaced font with a height of 8 pixels and a width of 5 pixels."""

    @property
    def family(self) -> str:
        """Gets the family name of the font."""
        return "Lucida"

    @property
    def style(self) -> str:
        """style -> str

        Gets a string describing the font style.

        Can be "Regular" or "Bold".
        """
        return "Regular"

    @property
    def width(self) -> int:
        """Gets the width of the widest character of the font."""
        return 0

    @property
    def height(self) -> int:
        """Gets the height of the font."""
        return 0

    def text_width(self, text: str) -> int:
        """text_width(text)

        Gets the width of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The width in pixels.
        """
        return 0

    def text_height(self, text: str) -> int:
        """text_height(text)

        Gets the height of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The height in pixels.
        """
        return 0


class ImageFile:
    """Paths to standard EV3 images."""

    _BASE_PATH: str = "/usr/share/images/ev3dev/mono/"
    RIGHT: str = _BASE_PATH + "information/right.png"
    FORWARD: str = _BASE_PATH + "information/forward.png"
    ACCEPT: str = _BASE_PATH + "information/accept.png"
    QUESTION_MARK: str = _BASE_PATH + "information/question_mark.png"
    STOP_1: str = _BASE_PATH + "information/stop_1.png"
    LEFT: str = _BASE_PATH + "information/left.png"
    DECLINE: str = _BASE_PATH + "information/decline.png"
    THUMBS_DOWN: str = _BASE_PATH + "information/thumbs_down.png"
    BACKWARD: str = _BASE_PATH + "information/backward.png"
    NO_GO: str = _BASE_PATH + "information/no_go.png"
    WARNING: str = _BASE_PATH + "information/warning.png"
    STOP_2: str = _BASE_PATH + "information/stop_2.png"
    THUMBS_UP: str = _BASE_PATH + "information/thumbs_up.png"
    EV3: str = _BASE_PATH + "lego/ev3.png"
    EV3_ICON: str = _BASE_PATH + "lego/ev3_icon.png"
    TARGET: str = _BASE_PATH + "objects/target.png"
    BOTTOM_RIGHT: str = _BASE_PATH + "eyes/bottom_right.png"
    BOTTOM_LEFT: str = _BASE_PATH + "eyes/bottom_left.png"
    EVIL: str = _BASE_PATH + "eyes/evil.png"
    CRAZY_2: str = _BASE_PATH + "eyes/crazy_2.png"
    KNOCKED_OUT: str = _BASE_PATH + "eyes/knocked_out.png"
    PINCHED_RIGHT: str = _BASE_PATH + "eyes/pinched_right.png"
    WINKING: str = _BASE_PATH + "eyes/winking.png"
    DIZZY: str = _BASE_PATH + "eyes/dizzy.png"
    DOWN: str = _BASE_PATH + "eyes/down.png"
    TIRED_MIDDLE: str = _BASE_PATH + "eyes/tired_middle.png"
    MIDDLE_RIGHT: str = _BASE_PATH + "eyes/middle_right.png"
    SLEEPING: str = _BASE_PATH + "eyes/sleeping.png"
    MIDDLE_LEFT: str = _BASE_PATH + "eyes/middle_left.png"
    TIRED_RIGHT: str = _BASE_PATH + "eyes/tired_right.png"
    PINCHED_LEFT: str = _BASE_PATH + "eyes/pinched_left.png"
    PINCHED_MIDDLE: str = _BASE_PATH + "eyes/pinched_middle.png"
    CRAZY_1: str = _BASE_PATH + "eyes/crazy_1.png"
    NEUTRAL: str = _BASE_PATH + "eyes/neutral.png"
    AWAKE: str = _BASE_PATH + "eyes/awake.png"
    UP: str = _BASE_PATH + "eyes/up.png"
    TIRED_LEFT: str = _BASE_PATH + "eyes/tired_left.png"
    ANGRY: str = _BASE_PATH + "eyes/angry.png"
