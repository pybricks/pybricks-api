# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Programmable Hubs."""

from typing import Sequence

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
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self, broadcast_channel: int = None, observe_channels: Sequence[int] = []
    ):
        """MoveHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class CityHub:
    """LEGO® City Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self, broadcast_channel: int = None, observe_channels: Sequence[int] = []
    ):
        """CityHub(broadcast_channel=None, observe_channels=[])

        Arguments:
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class TechnicHub:
    """LEGO® Technic Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """TechnicHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the button) and front side
        (with the light) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class EssentialHub:
    """LEGO® SPIKE Essential Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    buttons = _common.Keypad([_Button.CENTER])
    charger = _common.Charger()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """EssentialHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the button) and the front side (with the USB
        port, and I/O ports A and B) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
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
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """PrimeHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the buttons) and front side (with the USB
        port) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""


# HACK: hide from jedi
del Axis
