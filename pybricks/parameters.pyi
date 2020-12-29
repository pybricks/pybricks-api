# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

class Color:
    BLACK: Color
    BLUE: Color
    GREEN: Color
    YELLOW: Color
    RED: Color
    WHITE: Color
    BROWN: Color
    ORANGE: Color
    PURPLE: Color
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
    DOWN: Button
    RIGHT_DOWN: Button
    LEFT: Button
    CENTER: Button
    RIGHT: Button
    LEFT_UP: Button
    UP: Button
    BEACON: Button
    RIGHT_UP: Button

class Axis:
    X: Axis
    Y: Axis
    Z: Axis
    ALL: Axis

class Side:
    RIGHT: Side
    FRONT: Side
    TOP: Side
    LEFT: Side
    BACK: Side
    BOTTOM: Side