# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Programmable Hubs."""
from ._common import (Speaker as _Speaker, Battery as _Battery,
                      ColorLight as _ColorLight, KeyPad as _KeyPad,
                      LightMatrix as _LightMatrix)
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


class TechnicHub:
    """LEGO® Technic Hub."""
    battery = _Battery()
    light = _ColorLight()


class PrimeHub:
    """LEGO® SPIKE Prime Hub."""
    battery = _Battery()
    light = _ColorLight()
    display = _LightMatrix(5, 5)
    buttons = _KeyPad()


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""
    pass
