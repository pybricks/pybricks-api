# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from geometry import Matrix

class Color:
    BLACK: Color
    BLUE: Color
    BROWN: Color
    CYAN: Color
    GRAY: Color
    GREEN: Color
    MAGENTA: Color
    NONE: Color
    ORANGE: Color
    RED: Color
    VIOLET: Color
    WHITE: Color
    YELLOW: Color
    def __init__(self, h: int, s: int = 100, v: int = 100): ...
    def __eq__(self, other: "Color") -> bool: ...
    def __mul__(self, scale: float) -> Color: ...
    def __rmul__(self, scale: float) -> Color: ...
    def __truediv__(self, scale: float) -> Color: ...
    def __floordiv__(self, scale: int) -> Color: ...

class Port:
    A: Port
    B: Port
    C: Port
    D: Port
    E: Port
    F: Port
    S1: Port
    S2: Port
    S3: Port
    S4: Port

class Stop:
    COAST: Stop
    BRAKE: Stop
    HOLD: Stop

class Direction:
    CLOCKWISE: Direction
    COUNTERCLOCKWISE: Direction

class Button:
    LEFT_DOWN: Button
    LEFT_MINUS: Button
    DOWN: Button
    RIGHT_DOWN: Button
    RIGHT_MINUS: Button
    LEFT: Button
    CENTER: Button
    RIGHT: Button
    LEFT_UP: Button
    LEFT_PLUS: Button
    UP: Button
    BEACON: Button
    RIGHT_UP: Button
    RIGHT_PLUS: Button
    BLUETOOTH: Button

class Side:
    RIGHT: Side
    FRONT: Side
    TOP: Side
    LEFT: Side
    BACK: Side
    BOTTOM: Side

class Icon:
    UP: Matrix
    DOWN: Matrix
    LEFT: Matrix
    RIGHT: Matrix
    ARROW_RIGHT_UP: Matrix
    ARROW_RIGHT_DOWN: Matrix
    ARROW_LEFT_UP: Matrix
    ARROW_LEFT_DOWN: Matrix
    ARROW_UP: Matrix
    ARROW_DOWN: Matrix
    ARROW_LEFT: Matrix
    ARROW_RIGHT: Matrix
    HAPPY: Matrix
    SAD: Matrix
    EYE_LEFT: Matrix
    EYE_RIGHT: Matrix
    EYE_LEFT_BLINK: Matrix
    EYE_RIGHT_BLINK: Matrix
    EYE_RIGHT_BROW: Matrix
    EYE_LEFT_BROW: Matrix
    EYE_LEFT_BROW_UP: Matrix
    EYE_RIGHT_BROW_UP: Matrix
    HEART: Matrix
    PAUSE: Matrix
    EMPTY: Matrix
    FULL: Matrix
    SQUARE: Matrix
    TRIANGLE_RIGHT: Matrix
    TRIANGLE_LEFT: Matrix
    TRIANGLE_UP: Matrix
    TRIANGLE_DOWN: Matrix
    CIRCLE: Matrix
    CLOCKWISE: Matrix
    COUNTERCLOCKWISE: Matrix
    TRUE: Matrix
    FALSE: Matrix
