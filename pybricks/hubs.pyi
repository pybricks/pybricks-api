# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from ._common import Speaker, Battery, ColorLight, KeyPad
from .media.ev3dev import Image

class EV3Brick:
    screen: Image
    speaker: Speaker
    battery: Battery
    light: ColorLight
    buttons = KeyPad
