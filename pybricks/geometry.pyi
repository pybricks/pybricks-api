# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from typing import Collection, Optional, Tuple

class Matrix:
    def __init__(self, rows: Collection[int]): ...
    @property
    def T(self) -> Matrix: ...
    @property
    def shape(self) -> Tuple[int, int]: ...

def vector(x: float, y: float, z: Optional[float] = None) -> Matrix: ...

class Axis:
    X: Matrix
    Y: Matrix
    Z: Matrix
