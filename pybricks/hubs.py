# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Programmable Hubs."""
from .builtins import Speaker, Battery, ColorLight, KeyPad
from .media.ev3dev import Image


class EV3Brick:
    """LEGO® MINDSTORMS® EV3 Brick."""
    screen = Image('_screen_')
    speaker = Speaker()
    battery = Battery()
    light = ColorLight()
    buttons = KeyPad()


class MoveHub:
    """LEGO® Powered Up Move Hub."""
    battery = Battery()
    light = ColorLight()


class CityHub:
    """LEGO® Powered Up City Hub."""
    battery = Battery()
    light = ColorLight()
