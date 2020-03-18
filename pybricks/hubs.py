# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Programmable Hubs."""
from ._common import (Speaker as _Speaker, Battery as _Battery,
                      ColorLight as _ColorLight, KeyPad as _KeyPad)
from .media.ev3dev import Image as _Image


class EV3Brick:
    """LEGO® MINDSTORMS® EV3 Brick."""
    screen = _Image('_screen_')
    speaker = _Speaker()
    battery = _Battery()
    light = _ColorLight()
    buttons = _KeyPad()


class MoveHub:
    """LEGO® Powered Up Move Hub."""
    battery = _Battery()
    light = _ColorLight()


class CityHub:
    """LEGO® Powered Up City Hub."""
    battery = _Battery()
    light = _ColorLight()
