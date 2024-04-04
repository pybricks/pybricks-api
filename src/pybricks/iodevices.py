# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Generic input/output devices."""

from __future__ import annotations

from typing import Dict, Tuple, Optional, overload, TYPE_CHECKING

from . import _common
from .parameters import Port as _Port

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


class PUPDevice:
    """Powered Up motor or sensor."""

    def __init__(self, port: _Port):
        """PUPDevice(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def info(self) -> Dict[str, str]:
        """info() -> Dict

        Gets information about the device.

        Returns:
            Dictionary with information, such as the device ``id``.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Reads values from a given mode.

        Arguments:
            mode (int): Device mode.

        Returns:
            Values read from the sensor.
        """

    def write(self, mode: int, data: Tuple) -> MaybeAwaitable:
        """write(mode, data)

        Writes values to the sensor. Only selected sensors and modes support
        this.

        Arguments:
            mode (int): Device mode.
            data (tuple): Values to be written.
        """


class LUMPDevice:
    """Devices using the LEGO UART Messaging Protocol."""

    def __init__(self, port: _Port):
        """LUMPDevice(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Reads values from a given mode.

        Arguments:
            mode (int): Device mode.

        Returns:
            Values read from the sensor.
        """


class DCMotor(_common.DCMotor):
    """DC Motor for LEGO® MINDSTORMS EV3."""


class Ev3devSensor:
    """Read values of an ev3dev-compatible sensor."""

    sensor_index: int
    """Index of the ev3dev sysfs `lego-sensor`_ class."""

    port_index: int
    """Index of the ev3dev sysfs `lego-port`_ class."""

    def __init__(self, port: _Port):
        """Ev3devSensor(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def read(self, mode: str) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Reads values at a given mode.

        Arguments:
            mode (str): `Mode name`_.

        Returns:
            values read from the sensor.
        """


class AnalogSensor:
    """Generic or custom analog sensor."""

    def __init__(self, port: _Port):
        """AnalogSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Measures analog voltage.

        Returns:
            Analog voltage.
        """

    def resistance(self) -> int:
        """resistance() -> int: Ω

        Measures resistance.

        This value is only meaningful if the analog device is a passive load
        such as a resistor or thermistor.

        Returns:
            Resistance of the analog device.
        """

    def active(self) -> None:
        """active()

        Sets sensor to active mode. This sets pin 5 of the sensor
        port to `high`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light on.
        From then on, ``voltage()`` returns the raw reflected light value.
        """

    def passive(self) -> None:
        """passive()

        Sets sensor to passive mode. This sets pin 5 of the sensor
        port to `low`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light off.
        From then on, ``voltage()`` returns the raw ambient light value.
        """


class I2CDevice:
    """Generic or custom I2C device."""

    def __init__(self, port: _Port, address: int):
        """I2CDevice(port, address)

        Arguments:
            port (Port): Port to which the device is connected.
            address(int): I2C address of the client device. See
                :ref:`I2C Addresses <i2caddress>`.
        """

    def read(self, reg: Optional[int], length: Optional[int] = 1) -> bytes:
        """read(reg, length=1)

        Reads bytes, starting at a given register.

        Arguments:
            reg (int): Register at which to begin
                reading: 0--255 or 0x00--0xFF.
            length (int): How many bytes to read.

        Returns:
            Bytes returned from the device.
        """

    def write(self, reg: Optional[int], data: Optional[bytes] = None) -> None:
        """write(reg, data=None)

        Writes bytes, starting at a given register.

        Arguments:
            reg (int): Register at which to begin
                writing: 0--255 or 0x00--0xFF.
            data (bytes): Bytes to be written.
        """


class UARTDevice:
    """Generic UART device."""

    def __init__(self, port: _Port, baudrate: int, timeout: Optional[int] = None):
        """UARTDevice(port, baudrate, timeout=None)

        Arguments:
            port (Port): Port to which the device is connected.
            baudrate (int): Baudrate of the UART device.
            timeout (Number, ms): How long to wait
                during ``read`` before giving up. If you choose ``None``,
                it will wait forever.
        """

    def read(self, length: int = 1) -> bytes:
        """read(length=1) -> bytes

        Reads a given number of bytes from the buffer.

        Your program will wait until the requested number of bytes are
        received. If this takes longer than ``timeout``, the ``ETIMEDOUT``
        exception is raised.

        Arguments:
            length (int): How many bytes to read.

        Returns:
            Bytes returned from the device.
        """

    def read_all(self) -> bytes:
        """read_all() -> bytes

        Reads all bytes from the buffer.

        Returns:
            Bytes returned from the device.
        """

    def write(self, data: bytes) -> None:
        """write(data)

        Writes bytes.

        Arguments:
            data (bytes): Bytes to be written.
        """

    def waiting(self) -> int:
        """waiting() -> int

        Gets how many bytes are still waiting to be read.

        Returns:
            Number of bytes in the buffer.
        """

    def clear(self) -> None:
        """clear()

        Empties the buffer."""


class LWP3Device:
    """
    Connects to a hub running official LEGO firmware using the
    `LEGO Wireless Protocol v3`_

    .. _`LEGO Wireless Protocol v3`:
        https://lego.github.io/lego-ble-wireless-protocol-docs/
    """

    def __init__(self, hub_kind: int, name: str = None, timeout: int = 10000):
        """LWP3Device(hub_kind, name=None, timeout=10000)

        Arguments:
            hub_kind (int):
                The `hub type identifier`_ of the hub to connect to.
            name (str):
                The name of the hub to connect to or ``None`` to connect to any
                hub.
            timeout (int):
                The time, in milliseconds, to wait for a connection before
                raising an exception.


        .. _`hub type identifier`:
            https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#hub-type-ids
        """

    @overload
    def name(self, name: str) -> MaybeAwaitable: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Sets or gets the Bluetooth name of the device.

        Arguments:
            name (str): New Bluetooth name of the device. If no name is given,
                this method returns the current name.
        """

    def write(self, buf: bytes) -> MaybeAwaitable:
        """write(buf)

        Sends a message to the remote hub.

        Arguments:
            buf (bytes): The raw binary message to send.
        """

    def read(self) -> bytes:
        """read() -> bytes

        Retrieves the most recent message received from the remote hub.

        If a message has not been received since the last read, the method will
        block until a message is received.

        Returns:
            The raw binary message.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Disconnects the remote LWP3Device from the hub.
        """


class XboxController:
    """Use the Microsoft® Xbox® controller as a sensor in your projects to
    control them remotely.

    The hub will scan for the controller and connect to it. It will disconnect
    when the program ends.

    For tips on connectivity and pairing, see :ref:`below <xbox-controller-pairing>`.
    """

    buttons = _common.Keypad([])

    def __init__(self):
        """"""

    def joystick_left(self) -> Tuple[int, int]:
        """joystick_left() -> Tuple

        Gets the left joystick position as percentages between -100%
        and 100%. The center position is (0, 0).

        Returns:
            Tuple of X (horizontal) and Y (vertical) position.
        """

    def joystick_right(self) -> Tuple[int, int]:
        """joystick_right() -> Tuple

        Gets the right joystick position as percentages between -100%
        and 100%. The center position is (0, 0).

        Returns:
            Tuple of X (horizontal) and Y (vertical) position.
        """

    def triggers(self) -> Tuple[int, int]:
        """triggers() -> Tuple

        Gets the left and right trigger positions as percentages between 0%
        and 100%.

        Returns:
            Tuple of left and right trigger positions.
        """

    def dpad(self) -> int:
        """dpad() -> int

        Gets the direction-pad value. ``1`` is up, ``2`` is up-right, ``3``
        is right, ``4`` is down-right, ``5`` is down, ``6`` is down-left,
        ``7`` is left, ``8`` is up-left, and ``0`` is not pressed.

        This is essentially the same as reading the state of the
        ``Button.UP``, ``Button.RIGHT``, ``Button.DOWN``, and ``Button.LEFT``
        buttons, but this method conveniently returns a number that indicates
        a direction.

        Returns:
            Direction-pad position, indicating a direction.
        """

    def profile(self) -> int:
        """profile() -> int

        Gets the current profile of the controller. Only available on the
        Xbox Elite Controller Series 2.

        Returns:
            Profile number.
        """

    def rumble(
        self,
        power: Number | Tuple[Number, Number, Number, Number] = 100,
        duration: int = 200,
        count: int = 1,
        delay: int = 100,
    ) -> MaybeAwaitable:
        """rumble(power=100, duration=200, count=1, delay=100)

        Makes the builtin actuators rumble, creating force feedback.

        If you give a single ``power`` value, the left and right main actuators
        will both rumble with that power. For more fine-grained control, set
        ``power`` as a tuple of four values, which control the left main
        actuator, right main actuator, left trigger actuator, and the right
        trigger actuator, respectively. For example, ``power=(0, 0, 100, 0)``
        makes the left trigger rumble at full power.

        The rumble runs in the background while your program continues. To
        make your program wait, just pause the program for a matching duration.
        For one rumble, this equals ``duration``. For multiple rumbles, this
        equals ``count * (duration + delay)``.

        Arguments:
            power (Number, % or tuple): Rumble power.
            duration (Number, ms): Rumble duration.
            count (int): Rumble count.
            delay (Number, ms): Delay before each rumble. Only if ``count > 1``.
        """


# hide from jedi
if TYPE_CHECKING:
    del MaybeAwaitable
    del MaybeAwaitableTuple
    del Number
