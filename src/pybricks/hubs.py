# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® Programmable Hubs."""
from . import _common
from .ev3dev import _speaker
from .media.ev3dev import Image as _Image
from .parameters import Button as _Button, Axis


class EV3Brick:
    """LEGO® MINDSTORMS® EV3 Brick."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.UP,
            _Button.DOWN,
        ]
    )
    screen = _Image("_screen_")
    speaker = _speaker.Speaker()
    battery = _common.Battery()
    light = _common.ColorLight()


class MoveHub:
    """LEGO® BOOST Move Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.SimpleAccelerometer()
    system = _common.System()
    button = _common.Keypad([_Button.CENTER])


class CityHub:
    """LEGO® City Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    system = _common.System()
    button = _common.Keypad([_Button.CENTER])


class TechnicHub:
    """LEGO® Technic Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    button = _common.Keypad([_Button.CENTER])

    def __init__(self, top_side: Axis = Axis.Z, front_side: Axis = Axis.X):
        """TechnicHub(top_side=Axis.Z, front_side=Axis.X)

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


class EssentialHub:
    """LEGO® SPIKE Essential Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    button = _common.Keypad([_Button.CENTER])
    charger = _common.Charger()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()

    def __init__(self, top_side=Axis.Z, front_side=Axis.X):
        """__init__(top_side=Axis.Z, front_side=Axis.X)

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the button) and the front side (with the USB
        port, and I/O ports A and B) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
        """
        pass


class PrimeHub:
    """LEGO® SPIKE Prime Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.BLUETOOTH,
        ]
    )
    charger = _common.Charger()
    light = _common.ColorLight()
    display = _common.LightMatrix(5, 5)
    speaker = _common.Speaker()
    imu = _common.IMU()
    system = _common.System()

    def __init__(self, top_side: Axis = Axis.Z, front_side: Axis = Axis.X):
        """PrimeHub(top_side=Axis.Z, front_side=Axis.X)

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


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""


# HACK: hide from jedi
del Axis
