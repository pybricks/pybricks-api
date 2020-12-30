# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Programmable Hubs."""
from ._common import (Speaker as _Speaker, Battery as _Battery,
                      ColorLight as _ColorLight, Keypad as _Keypad,
                      LightMatrix as _LightMatrix, IMU as _IMU)
from .media.ev3dev import Image as _Image
from .parameters import Button as _Button


class EV3Brick:
    """LEGO® MINDSTORMS® EV3 Brick."""
    buttons = _Keypad((
        _Button.LEFT,
        _Button.RIGHT,
        _Button.CENTER,
        _Button.UP,
        _Button.DOWN,
    ))
    screen = _Image('_screen_')
    speaker = _Speaker()
    battery = _Battery()
    light = _ColorLight()


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
    imu = _IMU()


class PrimeHub:
    """LEGO® SPIKE Prime Hub."""
    battery = _Battery()
    buttons = _Keypad((
        _Button.LEFT,
        _Button.RIGHT,
        _Button.CENTER,
        _Button.BLUETOOTH,
    ))
    light = _ColorLight()
    display = _LightMatrix(5, 5)
    speaker = _Speaker()
    imu = _IMU()


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""
    pass
