# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from ._common import (
    Battery,
    ColorLight,
    Charger,
    IMU,
    Keypad,
    LightMatrix,
    SimpleAccelerometer,
    Speaker,
    System,
)
from .ev3dev._speaker import Speaker as EV3Speaker
from .geometry import Axis
from .media.ev3dev import Image

class EV3Brick:
    screen: Image
    speaker: EV3Speaker
    battery: Battery
    light: ColorLight
    buttons = Keypad

class MoveHub:
    battery: Battery
    light: ColorLight
    system: System
    imu: SimpleAccelerometer

class CityHub:
    battery: Battery
    light: ColorLight
    system: System

class TechnicHub:
    def __init__(self, top_size: Axis, front_side: Axis): ...
    battery: Battery
    light: ColorLight
    system: System
    imu: IMU

class PrimeHub:
    def __init__(self, top_side: Axis = Axis.Z, front_side: Axis = Axis.X): ...
    battery: Battery
    light: ColorLight
    display: LightMatrix
    buttons: Keypad
    speaker: Speaker
    system: System
    imu: IMU
    charger: Charger

class InventorHub(PrimeHub): ...
