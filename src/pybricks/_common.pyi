# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Pybricks Authors

from typing import Collection, Iterable, Optional, Tuple, Union, overload

from .geometry import Axis, Matrix, vector
from .parameters import Button, Color, Direction, Side, Stop, Port

class IMU(Accelerometer):
    def heading(self) -> int: ...
    def reset_heading(self, angle): ...
    @overload
    def gyro(self) -> vector[float, float, float]: ...
    @overload
    def gyro(self, axis: Axis) -> int: ...
