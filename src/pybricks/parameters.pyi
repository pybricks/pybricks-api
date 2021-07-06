# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

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
    def __mul__(self, scale: float) -> Color: ...
    def __rmul__(self, scale: float) -> Color: ...
    def __truediv__(self, scale: float) -> Color: ...
    def __floordiv__(self, scale: int) -> Color: ...

class Port:
    A: Port
    B: Port
    C: Port
    D: Port
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
