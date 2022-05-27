# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Programmable Hubs."""
from ._common import (
    Speaker as _Speaker,
    Battery as _Battery,
    ColorLight as _ColorLight,
    Keypad as _Keypad,
    LightMatrix as _LightMatrix,
    IMU as _IMU,
    Charger as _Charger,
    System as _System,
    SimpleAccelerometer as _SimpleAccelerometer,
)
from .ev3dev._speaker import Speaker as _EV3Speaker
from .geometry import Axis as _Axis
from .media.ev3dev import Image as _Image
from .parameters import Button as _Button


class EV3Brick:
    """LEGO® MINDSTORMS® EV3 Brick."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    buttons = _Keypad(
        (
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.UP,
            _Button.DOWN,
        )
    )
    screen = _Image("_screen_")
    speaker = _EV3Speaker()
    battery = _Battery()
    light = _ColorLight()


class MoveHub:
    """LEGO® BOOST Move Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _Battery()
    light = _ColorLight()
    imu = _SimpleAccelerometer()
    system = _System()
    button = _Keypad((_Button.CENTER,))


class CityHub:
    """LEGO® City Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _Battery()
    light = _ColorLight()
    system = _System()
    button = _Keypad((_Button.CENTER,))


class TechnicHub:
    """LEGO® Technic Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _Battery()
    light = _ColorLight()
    imu = _IMU()
    system = _System()
    button = _Keypad((_Button.CENTER,))

    def __init__(self, top_side=_Axis.Z, front_side=_Axis.X):
        """__init__(top_side=Axis.Z, front_side=Axis.X)

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the button) and front side
        (with the light) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
        """
        pass


class PrimeHub:
    """LEGO® SPIKE Prime Hub or LEGO® MINDSTORMS Inventor Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _Battery()
    buttons = _Keypad(
        (
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.BLUETOOTH,
        )
    )
    charger = _Charger()
    light = _ColorLight()
    display = _LightMatrix(5, 5)
    speaker = _Speaker()
    imu = _IMU()
    system = _System()

    def __init__(self, top_side=_Axis.Z, front_side=_Axis.X):
        """__init__(top_side=Axis.Z, front_side=Axis.X)

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the buttons) and front side (with the USB
        port) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
        """
        pass


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""

    pass
