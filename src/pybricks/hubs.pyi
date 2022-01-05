# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from ._common import Speaker, Battery, ColorLight, LightMatrix, Keypad
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


class CityHub:
    battery: Battery
    light: ColorLight


class TechnicHub:
    def __init__(self, top_size: Axis, front_side: Axis): ...
    battery: Battery
    light: ColorLight


class PrimeHub:
    def __init__(self, top_side: Axis = Axis.Z, front_side: Axis = Axis.X): ...
    battery: Battery
    light: ColorLight
    display: LightMatrix
    buttons: Keypad
    speaker: Speaker


class InventorHub(PrimeHub): ...
